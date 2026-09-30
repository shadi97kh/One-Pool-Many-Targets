"""
D7 / e9: the Caffrey 2011 dose series.

Why this dataset. Proposition 3 says that at a FIXED dose, within one
construct, the equilibrium and independent scorings induce the same ranking,
so no rank statistic can separate them. It says nothing about how one
construct behaves ACROSS doses, because dose changes M and therefore f. The
two models disagree there:

  independent   the effective pool is M_d, exactly proportional to dose, so
                the log-log exponent is exactly 1
  equilibrium   f_d solves (1+beta) f + sum_j x_j f/(K_j+f) = M_d. Added
                complex is absorbed by targets, so f_d lags in LEVEL, but the
                buffering saturates, so f is convex in M and the exponent is
                at least 1. See riscpool.dosefit for the bounds.

Both readings assume M_d is proportional to the administered dose, which is
an assumption about uptake and loading rather than a property of the design.

This module supplies the measured side of that comparison: the expression
matrix, the dose and construct assignment, the abundance vector, and the
guide sequences.

Three facts about this deposit that are not in the paper's abstract and that
every downstream number depends on:

1. The cell line is NOT the same for every construct. STAT3-1676 and
   STAT3-1676M were profiled in MCF-7; HK2-3581, HK2-3581M and HK2-4031 were
   profiled in Hep3B. GEO's own `cell line` characteristic says so. The
   abundance vector is therefore built per cell line, from the zero-dose
   arrays of that cell line.

2. Total transfected duplex is held CONSTANT across doses by topping up with
   non-targeting control siRNA. The CEL file names record the make-up
   explicitly: STAT3-1676 at 10 nM is `10nM-15nMsg2`, at 1 nM `1nM-24nMsg2`,
   at 0 nM `0nM-25nMsg2`. HK2-4031 is topped up with AllStars to 10 nM
   instead. This matters more than it looks: transfection efficiency and
   total Argonaute loading are held fixed, so M_d proportional to dose is a
   design property of the experiment rather than an assumption we impose.

3. For STAT3-1676, and for no other construct, the dose recorded in
   `!Sample_title` and `!Sample_characteristics_ch1` DISAGREES with the dose
   in the CEL file name: the 25 nM and 0 nM labels are exchanged. The
   conflict is resolved from the data, not by preference. On-target STAT3
   must fall when STAT3 siRNA is added, and under the characteristics
   labelling it does while under the CEL labelling it would rise. See
   `dose_label_audit`, which reports the check rather than performing it
   silently.
"""

import gzip
import os
import re
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd

from . import kmers
from .data_gencode import canonical_by_symbol
from .provenance import DATA

MATRIX = os.path.join(DATA, "raw", "GSE28786_series_matrix.txt.gz")
GENEINFO = os.path.join(DATA, "raw", "Homo_sapiens.gene_info.gz")
FULLTEXT = os.path.join(DATA, "lit", "caffrey2011",
                        "PMC3130022_fulltext.xml")

EXPR = os.path.join(DATA, "gse28786_expression.parquet")
SAMPLES = os.path.join(DATA, "gse28786_samples.parquet")
ABUND = os.path.join(DATA, "gse28786_abundance.parquet")
RESP = os.path.join(DATA, "gse28786_response.parquet")
CAND = os.path.join(DATA, "candidate_utr3_gse28786.parquet")
ACC = os.path.join(DATA, "accessibility_gse28786_u8_u15.npz")
FEAT = os.path.join(DATA, "features_gse28786.parquet")

TARGET_OF = {"STAT3-1676": "STAT3", "STAT3-1676M": "STAT3",
             "HK2-3581": "HK2", "HK2-3581M": "HK2", "HK2-4031": "HK2"}


# ------------------------------------------------------- guide sequences --

def guides_from_table1(path=FULLTEXT):
    """
    Parse Table 1 of the paper out of the recorded full-text XML.

    Not typed in. The sequences are read from the same bytes that
    data/PROVENANCE.json hashes, so a reader can re-derive them. The table
    marks the seed with <underline> and the 3' overhang in lowercase, both of
    which are used here rather than being re-imposed by us:

        U<underline>UGGUCA</underline>GCAUGUUGUACCuu

    Each guide is checked against its own passenger strand: the passenger
    must be the reverse complement of the 19-mer guide body. A row that fails
    that check is reported, never silently repaired.
    """
    tree = ET.parse(path)
    root = tree.getroot()
    tw = None
    for t in root.iter("table-wrap"):
        lab = t.find("label")
        cap = t.find(".//caption/title")
        if (lab is not None and (lab.text or "").strip() == "Table 1"
                and cap is not None and "sequences" in (cap.text or "")):
            tw = t
            break
    if tw is None:
        raise ValueError(f"Table 1 not found in {path}")

    def celltext(td):
        return "".join(td.itertext())

    rows = []
    for tr in tw.iter("tr"):
        tds = list(tr.iter("td"))
        if len(tds) != 3:
            continue
        name = celltext(tds[0]).strip()
        guide = re.sub(r"\s+", "", celltext(tds[1]))
        passenger = re.sub(r"\s+", "", celltext(tds[2]))
        if name.lower().startswith("sirna") or guide.lower() == "pool":
            continue
        if not re.fullmatch(r"[ACGUacgu]+", guide or "x"):
            continue
        # lowercase is the 3' overhang, per the table footnote
        body = re.sub(r"[acgu]+$", "", guide)
        pass_body = re.sub(r"[acgu]+$", "", passenger)
        seed_el = tds[1].find(".//underline")
        seed_marked = (seed_el.text or "").upper() if seed_el is not None \
            else ""
        g_dna = body.upper().replace("U", "T")
        rows.append({
            "table_row_label": name,
            "guide_with_overhang_rna": guide,
            "guide_5to3_rna": body.upper(),
            "guide_5to3_dna": g_dna,
            "guide_len": len(body),
            "overhang_rna": guide[len(body):],
            "passenger_5to3_rna": pass_body.upper(),
            "seed_underlined_in_table_rna": seed_marked,
            "seed_positions_2_7_from_guide_rna": body.upper()[1:7],
            "seed_2_8_dna": g_dna[1:8],
            "site_7mer_m8_dna": kmers.revcomp(g_dna[1:8]),
            "site_6mer_dna": kmers.revcomp(g_dna[1:7]),
            "passenger_is_revcomp_of_guide": bool(
                kmers.revcomp(g_dna)
                == pass_body.upper().replace("U", "T")),
            "underlined_seed_matches_positions_2_7": bool(
                seed_marked == body.upper()[1:7]) if seed_marked else None,
        })
    d = pd.DataFrame(rows)
    # one physical duplex serves two constructs (M = 2'-O-methyl at guide
    # position 2, identical sequence), so the table row expands to both
    out = []
    for _, r in d.iterrows():
        for name in str(r.table_row_label).split("/"):
            name = name.strip()
            rr = dict(r)
            rr["construct"] = name
            rr["is_2ome_modified"] = name.endswith("M")
            rr["target_gene"] = TARGET_OF.get(name)
            out.append(rr)
    return pd.DataFrame(out)


# ----------------------------------------------------------- expression --

def parse_series_matrix(path=MATRIX):
    """Returns (expression DataFrame indexed by probeset, sample metadata)."""
    hdr = {}
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("!series_matrix_table_begin"):
                break
            if line.startswith("!Sample_"):
                k = line.split("\t")[0]
                v = [x.strip().strip('"')
                     for x in line.rstrip("\n").split("\t")[1:]]
                hdr.setdefault(k, []).append(v)
        cols = [x.strip().strip('"')
                for x in fh.readline().rstrip("\n").split("\t")]
        ids, rows = [], []
        for line in fh:
            if line.startswith("!series_matrix_table_end"):
                break
            p = line.rstrip("\n").split("\t")
            ids.append(p[0].strip('"'))
            rows.append([float(x) for x in p[1:]])
    X = pd.DataFrame(rows, index=ids, columns=cols[1:])

    ch = hdr["!Sample_characteristics_ch1"]

    def char(prefix):
        for block in ch:
            if all(v.startswith(prefix) for v in block):
                return [v.split(": ", 1)[1] for v in block]
        raise KeyError(prefix)

    desc = hdr["!Sample_description"]
    cel = next((b for b in desc if all(v.endswith(".CEL") for v in b)), None)
    meta = pd.DataFrame({
        "geo_accession": hdr["!Sample_geo_accession"][0],
        "title": hdr["!Sample_title"][0],
        "cell_line": char("cell line"),
        "construct": char("sirna"),
        "dose_label": char("sirna concentration"),
        "biological_replicate": char("biological replicate"),
        "cel_file": cel if cel is not None else [""] * X.shape[1],
    })
    meta["dose_nM"] = [float(s.replace("nM", "")) for s in meta.dose_label]

    def cel_dose(s):
        m = re.match(r"^[A-Za-z0-9\-]+_(\d+)nM", s or "")
        return float(m.group(1)) if m else np.nan

    meta["dose_nM_from_cel_filename"] = [cel_dose(s) for s in meta.cel_file]
    meta["dose_labels_agree"] = (
        meta.dose_nM == meta.dose_nM_from_cel_filename)
    meta["target_gene"] = meta.construct.map(TARGET_OF)
    return X, meta


def entrez_to_symbol(path=GENEINFO):
    """GeneID -> official symbol, from NCBI Gene. The GPL9324 custom-CDF
    probeset identifiers are Entrez gene ids with an `_at` suffix."""
    keep = ["GeneID", "Symbol", "type_of_gene", "Synonyms"]
    d = pd.read_csv(path, sep="\t", compression="gzip", low_memory=False,
                    usecols=lambda c: c.lstrip("#") in keep)
    d.columns = [c.lstrip("#") for c in d.columns]
    return d[["GeneID", "Symbol", "type_of_gene"]]


def probeset_to_gene(X, gene_info=None):
    """Map probeset ids to official symbols. Probesets that do not parse as
    an Entrez id, or whose id is not in NCBI Gene, are dropped and counted."""
    gi = gene_info if gene_info is not None else entrez_to_symbol()
    ids = pd.Series(X.index, index=X.index)
    ent = ids.str.extract(r"^(\d+)_at$")[0]
    m = pd.DataFrame({"probeset": X.index, "entrez": ent})
    m["entrez"] = pd.to_numeric(m.entrez, errors="coerce")
    m = m.merge(gi, left_on="entrez", right_on="GeneID", how="left")
    m = m.rename(columns={"Symbol": "gene_symbol"})
    return m


def dose_label_audit(X, meta):
    """
    Resolve the STAT3-1676 label conflict from the measurement.

    For each construct, compare the on-target transcript's mean log2 level at
    the top dose against zero dose, once under the GEO characteristics
    labelling and once under the CEL-filename labelling. Silencing must lower
    the on-target. Whichever labelling produces silencing is the one the data
    supports, and the audit reports both numbers so the choice is visible.
    """
    sym = {"STAT3": "6774_at", "HK2": "3099_at"}
    rows = []
    for c, d in meta.groupby("construct"):
        ps = sym[TARGET_OF[c]]
        if ps not in X.index:
            continue
        v = X.loc[ps, d.geo_accession].to_numpy(dtype=float)
        out = {"construct": c, "cell_line": d.cell_line.iloc[0],
               "on_target_gene": TARGET_OF[c], "probeset": ps,
               "n_arrays": int(len(d)),
               "n_arrays_where_labels_agree": int(d.dose_labels_agree.sum())}
        for tag, col in (("characteristics", "dose_nM"),
                         ("cel_filename", "dose_nM_from_cel_filename")):
            dd = d[col].to_numpy(dtype=float)
            top = np.nanmax(dd)
            if not np.isfinite(top):
                continue
            hi = v[dd == top].mean()
            lo = v[dd == 0].mean()
            out[f"on_target_log2_at_zero_{tag}"] = float(lo)
            out[f"on_target_log2_at_top_dose_{tag}"] = float(hi)
            out[f"on_target_log2fc_top_minus_zero_{tag}"] = float(hi - lo)
            out[f"silencing_observed_{tag}"] = bool(hi < lo)
        rows.append(out)
    return rows


def build(out_expr=EXPR, out_samples=SAMPLES, out_abund=ABUND,
          out_resp=RESP):
    """
    Parse the deposit into the four tables the experiment consumes and write
    them. Returns a dict of counts and audit rows; no number here is typed.
    """
    X, meta = parse_series_matrix()
    audit = dose_label_audit(X, meta)

    pmap = probeset_to_gene(X)
    n_unmapped = int(pmap.gene_symbol.isna().sum())
    pmap = pmap.dropna(subset=["gene_symbol"])

    lin = pd.DataFrame(np.power(2.0, X.to_numpy()), index=X.index,
                       columns=X.columns)

    # abundance: zero-dose arrays only, per cell line, on the linear scale
    ab_rows = []
    for cell, d in meta.groupby("cell_line"):
        z = d[d.dose_nM == 0].geo_accession.tolist()
        v = lin[z].mean(axis=1)
        t = pd.DataFrame({"probeset": v.index, "mock_intensity": v.to_numpy()})
        t = t.merge(pmap[["probeset", "gene_symbol"]], on="probeset",
                    how="inner")
        t = (t.groupby("gene_symbol", as_index=False)
              .agg(mock_intensity=("mock_intensity", "median"),
                   n_probesets=("probeset", "size")))
        t["cell_line"] = cell
        t["n_zero_dose_arrays"] = len(z)
        t["x_rel"] = t.mock_intensity / t.mock_intensity.sum()
        ab_rows.append(t)
    ab = pd.concat(ab_rows, ignore_index=True)

    # response: log2 fold change against the zero-dose arrays of the SAME
    # construct, which carry the same total duplex made up with control siRNA
    r_rows = []
    for c, d in meta.groupby("construct"):
        z = d[d.dose_nM == 0].geo_accession.tolist()
        base = X[z].mean(axis=1)
        for dose, dd in d[d.dose_nM > 0].groupby("dose_nM"):
            arrays = dd.geo_accession.tolist()
            v = X[arrays].mean(axis=1) - base
            sd = X[arrays].std(axis=1, ddof=1) if len(arrays) > 1 else \
                pd.Series(np.nan, index=X.index)
            t = pd.DataFrame({"probeset": v.index,
                              "log2fc": v.to_numpy(),
                              "sd_within_dose": sd.to_numpy()})
            t["construct"] = c
            t["dose_nM"] = dose
            t["n_arrays_dose"] = len(arrays)
            t["n_arrays_zero"] = len(z)
            t["cell_line"] = d.cell_line.iloc[0]
            r_rows.append(t)
    resp = pd.concat(r_rows, ignore_index=True)
    resp = resp.merge(pmap[["probeset", "gene_symbol"]], on="probeset",
                      how="inner")
    resp = (resp.groupby(["construct", "dose_nM", "cell_line", "gene_symbol"],
                         as_index=False)
                .agg(log2fc=("log2fc", "median"),
                     n_probesets=("probeset", "size"),
                     n_arrays_dose=("n_arrays_dose", "first"),
                     n_arrays_zero=("n_arrays_zero", "first")))

    X.reset_index(names="probeset").to_parquet(out_expr, index=False,
                                               compression="zstd")
    meta.to_parquet(out_samples, index=False, compression="zstd")
    ab.to_parquet(out_abund, index=False, compression="zstd")
    resp.to_parquet(out_resp, index=False, compression="zstd")

    return {
        "n_probesets": int(X.shape[0]),
        "n_arrays": int(X.shape[1]),
        "n_probesets_unmapped_to_ncbi_gene": n_unmapped,
        "n_gene_symbols": int(ab.gene_symbol.nunique()),
        "cell_lines": sorted(meta.cell_line.unique()),
        "constructs": sorted(meta.construct.unique()),
        "doses_nM": sorted(meta.dose_nM.unique()),
        "n_arrays_with_conflicting_dose_labels": int(
            (~meta.dose_labels_agree).sum()),
        "constructs_with_conflicting_dose_labels": sorted(
            meta.loc[~meta.dose_labels_agree, "construct"].unique()),
        "dose_label_audit": audit,
        "dose_label_resolution": (
            "the GEO characteristics labelling is used throughout. It is the "
            "labelling under which the on-target transcript falls when its "
            "own siRNA is added, for every construct including STAT3-1676; "
            "the CEL-filename labelling would require STAT3 to be silenced "
            "by zero nanomolar of STAT3 siRNA."),
        "abundance_note": (
            "x_rel is the mean linear-scale RMA intensity over the zero-dose "
            "arrays of that cell line, collapsed probeset to symbol by "
            "median and normalised to sum to one. Zero dose is not untreated: "
            "it carries the same total duplex made up with non-targeting "
            "control siRNA."),
        "response_note": (
            "log2fc is the mean log2 RMA level at the dose minus the mean "
            "over the zero-dose arrays of the same construct. Negative is "
            "repression."),
        "paths": {"expression": out_expr, "samples": out_samples,
                  "abundance": out_abund, "response": out_resp},
    }


def load_expression():
    return pd.read_parquet(EXPR).set_index("probeset")


def load_samples():
    return pd.read_parquet(SAMPLES)


def load_abundance(cell_line=None):
    d = pd.read_parquet(ABUND)
    return d if cell_line is None else d[d.cell_line == cell_line]


def load_response():
    return pd.read_parquet(RESP)


# ------------------------------------------------------------ candidates --

def build_candidates(out=CAND):
    """
    The retrieval universe for this deposit: every gene measured on GPL9324
    that GENCODE gives a canonical 3'UTR. It does not depend on the cell
    line, because both cell lines were run on the same array; only the
    abundance vector differs.
    """
    ab = load_abundance()
    can = canonical_by_symbol()[["gene_symbol", "transcript_id", "utr3_seq",
                                 "cds_seq", "utr5_seq", "utr3_len",
                                 "cds_len"]]
    syms = sorted(ab.gene_symbol.unique())
    df = can[can.gene_symbol.isin(syms)].copy()
    df = df[df.utr3_len >= 10].reset_index(drop=True)
    df.to_parquet(out, index=False, compression="zstd")
    return df


def load_candidates():
    return pd.read_parquet(CAND)


# --------------------------------------------- accessibility and features --

def build_accessibility(out=ACC, nproc=None):
    """
    Local unpaired probability over the D7 candidate 3'UTRs.

    Same ViennaRNA call, same window parameters and same output layout as
    riscpool.accessibility, run over a different candidate set and written to
    a different file. The HeLa cache is not touched, so nothing already
    recorded in results/ can move.
    """
    from multiprocessing import Pool

    from .accessibility import KEEP, L, U, W, _worker

    cand = load_candidates()
    items = list(zip(cand.transcript_id.tolist(), cand.utr3_seq.tolist()))
    nproc = nproc or max(1, (os.cpu_count() or 4) - 2)
    res, errors = {}, {}
    with Pool(nproc) as p:
        for tid, val in p.imap_unordered(_worker, items, chunksize=16):
            if isinstance(val, tuple):
                errors[tid] = val[1]
            else:
                res[tid] = val
    ids = [t for t in cand.transcript_id if t in res]
    lens = np.array([res[t].shape[1] for t in ids], dtype=np.int64)
    off = np.concatenate([[0], np.cumsum(lens)])
    flat = np.concatenate([res[t] for t in ids], axis=1)
    np.savez_compressed(out, ids=np.array(ids), offsets=off, acc=flat,
                        keep=np.array(KEEP), params=np.array([W, L, U]))
    return {"n_transcripts": len(ids), "n_errors": len(errors),
            "errors": errors, "total_positions": int(lens.sum()),
            "pfl_fold_W": W, "pfl_fold_L": L, "pfl_fold_u_max": U,
            "stretch_lengths_kept": list(KEEP), "path": out}


def build_features(out=FEAT, nproc=None, constructs=None):
    """
    Per-site sequence and thermodynamic features for the D7 guides over the
    D7 candidate 3'UTRs.

    Calls riscpool.features._pair_features unchanged, so K is derived exactly
    as it is for the HeLa experiments: dG_eff = dG_duplex - RT ln P_unpaired
    per site, which ADDS the cost of opening the site to the duplex energy,
    sites combined in parallel as 1/K_tx = sum_s 1/K_site. Writing to a
    separate parquet keeps data/features.parquet, and therefore e4, e5 and
    e7, byte-identical.
    """
    from multiprocessing import Pool

    from .accessibility import Accessibility
    from .features import _pair_features, guide_features

    cand = load_candidates()
    acc = Accessibility(ACC)
    g = guides_from_table1()
    g = g[g.target_gene.notna()]          # the two controls have no target
    if constructs is not None:
        g = g[g.construct.isin(constructs)]

    cache = {t: acc.get(t, 15) for t in cand.transcript_id}
    jobs = []
    for _, s in g.iterrows():
        g_dna = s.guide_5to3_dna
        g_rna = g_dna.replace("T", "U")
        core = kmers.revcomp(g_dna[1:7])
        for tid, sym, utr3, cds in zip(cand.transcript_id, cand.gene_symbol,
                                       cand.utr3_seq, cand.cds_seq):
            if core in utr3:
                jobs.append((s.construct, g_rna, g_dna, tid, sym, utr3, cds,
                             cache.get(tid), np.nan))
    nproc = nproc or max(1, (os.cpu_count() or 4) - 2)
    rows = []
    with Pool(nproc) as p:
        for r in p.imap_unordered(_pair_features, jobs, chunksize=64):
            if r:
                rows.extend(r)
    df = pd.DataFrame(rows)
    gf = pd.DataFrame([dict(construct=s.construct,
                            **guide_features(s.guide_5to3_dna))
                       for _, s in g.iterrows()])
    df = df.merge(gf, on="construct", how="left")
    df.to_parquet(out, index=False, compression="zstd")
    return df


def load_features():
    return pd.read_parquet(FEAT)


def transcript_level(df=None):
    """One row per (construct, transcript), same collapse rule as the HeLa
    pipeline."""
    from .features import transcript_level as _tl
    return _tl(load_features() if df is None else df)
