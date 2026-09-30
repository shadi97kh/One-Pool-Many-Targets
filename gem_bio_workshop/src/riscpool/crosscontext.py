"""
D8 / e10: the same guide in two transcriptomes.

WHY THIS EVADES PROPOSITION 3. The rank-invariance result fixes the dose and
the construct and compares two scorings of one transcript set. Here the
construct is fixed and the TRANSCRIPTOME changes. K_j is a property of
sequence and structure and is identical in both contexts by construction;
what differs is the abundance vector x^(c), and therefore the competitor mass
the free pool has to satisfy. The two models say different things about that:

  independent scoring   the bound fraction is M/(K_j+M). M does not depend on
                        the transcriptome, so the off-target signature is
                        predicted to be IDENTICAL in the two cell lines up to
                        which transcripts are expressed at all.
  equilibrium           the free pool f^(c) solves conservation against
                        x^(c), so a context whose expressed transcripts carry
                        more high-affinity mass leaves less free pool and a
                        weaker off-target signature, by a specific amount.

THE MEASUREMENT. Exactly the estimator e9 uses for dose, applied to context:
one effective pool per context, one amplitude shared between them, K held
fixed. The observed ratio of the two fitted pools is then compared against
1, which is what independent scoring predicts, and against the ratio the
conservation equation predicts from the two measured abundance vectors.

WHAT IS NOT AVAILABLE, AND WHAT IS DONE INSTEAD. The guide sequences are not
in the deposit and the article is not open access; both failures are recorded
in data/PROVENANCE.json. The seed is therefore RECOVERED FROM THE MEASURED
RESPONSE by the same enrichment scan riscpool.kmers already uses for GSE5814,
where it reproduced the published sequences. Recovery gives guide positions
2-8 and nothing else, so the affinity model here is built on the seed duplex
alone rather than on the full guide. That is a weaker K than the HeLa
pipeline's, and it is weaker in a way that costs power rather than validity:
the cross-context test needs K to be the SAME in both contexts, which it is,
not to be the best possible affinity model. Recovery is run separately in
each cell line and the two answers are compared, so a failure of recovery
shows up as a disagreement rather than as a silent wrong seed.
"""

import gzip
import os

import numpy as np
import pandas as pd

from . import kmers
from .data_gencode import canonical_by_symbol
from .provenance import DATA

MATRIX = os.path.join(DATA, "raw", "GSE14073-GPL6793_series_matrix.txt.gz")
PLATFORM = os.path.join(DATA, "raw", "GPL6793_family.soft.gz")

EXPR = os.path.join(DATA, "gse14073_expression.parquet")
SAMPLES = os.path.join(DATA, "gse14073_samples.parquet")
ABUND = os.path.join(DATA, "gse14073_abundance.parquet")
RESP = os.path.join(DATA, "gse14073_response.parquet")
CAND = os.path.join(DATA, "candidate_utr3_gse14073.parquet")
ACC = os.path.join(DATA, "accessibility_gse14073_u8_u15.npz")
FEAT = os.path.join(DATA, "features_gse14073.parquet")

MOCK = "Mock"
TARGET_OF = {"APOB-Hs1": "APOB", "APOB-Hs2": "APOB", "APOB-Hs3": "APOB",
             "APOB-Hs4": "APOB", "Apob-Mm1": "APOB", "Apob-Mm2": "APOB",
             "RAD18": "RAD18"}


def parse_series_matrix(path=MATRIX):
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
            rows.append([float(x) if x not in ("", "NA", "null", "NULL")
                         else np.nan for x in p[1:]])
    X = pd.DataFrame(rows, index=ids, columns=cols[1:])

    titles = hdr["!Sample_title"][0]
    cell, construct, hours = [], [], []
    for t in titles:
        parts = [p.strip() for p in t.split(",")]
        cell.append(parts[0])
        construct.append(parts[1])
        hours.append(float(parts[-1].rstrip("h")))
    meta = pd.DataFrame({
        "geo_accession": hdr["!Sample_geo_accession"][0],
        "title": titles, "cell_line": cell, "construct": construct,
        "hours": hours,
        "dose_label": [p[2].strip() if len(p := [q.strip()
                                                 for q in t.split(",")]) == 4
                       else "0nM" for t in titles],
    })
    meta["is_mock"] = meta.construct == MOCK
    meta["target_gene"] = meta.construct.map(TARGET_OF)
    return X, meta


def platform_annotation(path=PLATFORM):
    rows, intab, cols = [], False, None
    with gzip.open(path, "rt", errors="replace") as fh:
        for line in fh:
            if line.startswith("!platform_table_begin"):
                intab = True
                continue
            if line.startswith("!platform_table_end"):
                break
            if not intab:
                continue
            p = line.rstrip("\n").split("\t")
            if cols is None:
                cols = p
                continue
            rows.append(p[:len(cols)] + [""] * (len(cols) - len(p)))
    d = pd.DataFrame(rows, columns=cols)
    d = d.rename(columns={"ID": "probe_id", "GeneSymbol": "gene_symbol"})
    d["gene_symbol"] = d.gene_symbol.astype(str).str.strip()
    return d[d.gene_symbol.str.len() > 0][["probe_id", "gene_symbol",
                                           "GB_ACC"]]


def build(out_expr=EXPR, out_samples=SAMPLES, out_abund=ABUND,
          out_resp=RESP):
    """
    Parse the deposit into abundance and response tables.

    Values in this series are LINEAR intensities, not log ratios, so the
    response is formed here: log2 of the mean siRNA intensity over the mean
    mock intensity of the same cell line at the same timepoint. Abundance is
    the mock intensity of that cell line, which is the same choice the HeLa
    pipeline makes with the GSE5814 mock channel.
    """
    X, meta = parse_series_matrix()
    ann = platform_annotation()
    amap = ann.drop_duplicates(subset=["probe_id"])[["probe_id",
                                                     "gene_symbol"]]
    n_probes_unannotated = int(X.shape[0] - X.index.isin(amap.probe_id).sum())

    ab_rows = []
    for cell, d in meta[meta.is_mock].groupby("cell_line"):
        v = X[d.geo_accession.tolist()].mean(axis=1)
        t = pd.DataFrame({"probe_id": v.index, "mock_intensity": v.to_numpy()})
        t = t.merge(amap, on="probe_id", how="inner").dropna()
        t = t[np.isfinite(t.mock_intensity) & (t.mock_intensity > 0)]
        t = (t.groupby("gene_symbol", as_index=False)
              .agg(mock_intensity=("mock_intensity", "median"),
                   n_probes=("probe_id", "size")))
        t["cell_line"] = cell
        t["n_mock_arrays"] = len(d)
        t["x_rel"] = t.mock_intensity / t.mock_intensity.sum()
        ab_rows.append(t)
    ab = pd.concat(ab_rows, ignore_index=True)

    r_rows = []
    for (cell, hrs), d in meta[meta.is_mock].groupby(["cell_line", "hours"]):
        base = X[d.geo_accession.tolist()].mean(axis=1)
        sel = meta[(~meta.is_mock) & (meta.cell_line == cell)
                   & (meta.hours == hrs)]
        for _, s in sel.iterrows():
            v = X[s.geo_accession]
            with np.errstate(divide="ignore", invalid="ignore"):
                lfc = np.log2(v / base)
            t = pd.DataFrame({"probe_id": v.index,
                              "log2fc": lfc.to_numpy(),
                              "mock_intensity": base.to_numpy()})
            t["construct"] = s.construct
            t["cell_line"] = cell
            t["hours"] = hrs
            t["geo_accession"] = s.geo_accession
            r_rows.append(t)
    resp = pd.concat(r_rows, ignore_index=True)
    resp = resp.merge(amap, on="probe_id", how="inner")
    resp = resp[np.isfinite(resp.log2fc)]
    resp = (resp.groupby(["construct", "cell_line", "hours", "gene_symbol"],
                         as_index=False)
                .agg(log2fc=("log2fc", "median"),
                     n_probes=("probe_id", "size")))

    X.reset_index(names="probe_id").to_parquet(out_expr, index=False,
                                               compression="zstd")
    meta.to_parquet(out_samples, index=False, compression="zstd")
    ab.to_parquet(out_abund, index=False, compression="zstd")
    resp.to_parquet(out_resp, index=False, compression="zstd")
    return {
        "n_probes": int(X.shape[0]), "n_arrays": int(X.shape[1]),
        "n_probes_without_platform_annotation": n_probes_unannotated,
        "n_gene_symbols": int(ab.gene_symbol.nunique()),
        "cell_lines": sorted(meta.cell_line.unique()),
        "constructs": sorted(meta[~meta.is_mock].construct.unique()),
        "hours": sorted(meta.hours.unique()),
        "n_mock_arrays_per_cell_line": {
            k: int(v) for k, v in
            meta[meta.is_mock].groupby("cell_line").size().items()},
        "timepoints_shared_by_both_cell_lines": sorted(
            set(meta[meta.cell_line == "HUH7"].hours)
            & set(meta[meta.cell_line == "PLC/PRF/5"].hours)),
        "value_scale_note": (
            "the deposited matrix carries linear RMA intensities, not log "
            "ratios; log2fc is formed here against the mock arrays of the "
            "same cell line at the same timepoint"),
        "paths": {"expression": out_expr, "samples": out_samples,
                  "abundance": out_abund, "response": out_resp},
    }


def load_abundance(cell_line=None):
    d = pd.read_parquet(ABUND)
    return d if cell_line is None else d[d.cell_line == cell_line]


def load_response():
    return pd.read_parquet(RESP)


def load_samples():
    return pd.read_parquet(SAMPLES)


def build_candidates(out=CAND):
    ab = load_abundance()
    can = canonical_by_symbol()[["gene_symbol", "transcript_id", "utr3_seq",
                                 "cds_seq", "utr3_len", "cds_len"]]
    syms = sorted(ab.gene_symbol.unique())
    df = can[can.gene_symbol.isin(syms)].copy()
    df = df[df.utr3_len >= 10].reset_index(drop=True)
    df.to_parquet(out, index=False, compression="zstd")
    return df


def load_candidates():
    return pd.read_parquet(CAND)


# ------------------------------------------------------- seed recovery ----

def recover_seed(resp, construct, cell_line, cand, G=None, k=7, min_n=30,
                 hours=None):
    """
    Recover the 7-mer site from the measured response.

    For every 7-mer, compare the mean log2 fold change of transcripts whose
    3'UTR contains it against those that do not, and take the 7-mer with the
    most negative Welch t. That 7-mer is the site complementary to guide
    positions 2-8. This is the method riscpool.kmers already uses on GSE5814,
    where it reproduced the published guide sequences; here it is the only
    route to the seed at all, because the sequences were never deposited.
    """
    d = resp[(resp.construct == construct) & (resp.cell_line == cell_line)]
    if hours is not None:
        d = d[d.hours == hours]
    d = (d.groupby("gene_symbol", as_index=False)
          .agg(log2fc=("log2fc", "median")))
    syms = cand.gene_symbol.tolist()
    if G is None:
        G = kmers.incidence(cand.utr3_seq.tolist(), k=k)
    pos = pd.Series(np.arange(len(syms)), index=syms)
    idx = pos.reindex(d.gene_symbol).to_numpy()
    ok = np.isfinite(idx.astype(float))
    d = d[ok]
    idx = idx[ok].astype(int)
    delta, t, n1 = kmers.enrichment_scan(G[idx], d.log2fc.to_numpy(),
                                         min_n=min_n)
    order = np.argsort(np.where(np.isnan(t), np.inf, t))
    top = [{"rank": int(r), "site_kmer": kmers.index_to_kmer(int(i), k),
            "welch_t": float(t[i]), "delta_mean_log2fc": float(delta[i]),
            "n_transcripts_with_site": int(n1[i])}
           for r, i in enumerate(order[:10])]
    return top, int(len(d)), G


def pseudo_guide_from_site(site7):
    """
    An 8-nt stand-in guide whose seed reproduces the recovered site.

    riscpool.features derives the 6-mer core as revcomp(guide[1:7]) and the
    t8 base as the complement of guide[7], so a guide whose positions 2-8 are
    revcomp(site7) reproduces exactly the recovered site and its site-class
    logic, without pretending to know the 3' half of the real guide.
    """
    return "A" + kmers.revcomp(site7)


# ------------------------------------------------ accessibility, features --

def build_accessibility(out=ACC, reuse=(), nproc=None):
    """
    Local unpaired probability over the D8 candidate 3'UTRs.

    Accessibility is a property of the transcript sequence alone, so any
    transcript already computed for another candidate set has the same answer
    here. `reuse` names existing .npz caches to draw from; only the remainder
    is folded. Identical ViennaRNA call and window parameters either way.
    """
    from multiprocessing import Pool

    from .accessibility import KEEP, L, U, W, Accessibility, _worker

    cand = load_candidates()
    want = cand.transcript_id.tolist()
    res, n_reused = {}, 0
    for path in reuse:
        if not os.path.exists(path):
            continue
        a = Accessibility(path)
        for t in want:
            if t in res or t not in a.index:
                continue
            i = a.index[t]
            res[t] = a.acc[:, a.off[i]:a.off[i + 1]]
            n_reused += 1
    todo = [(t, s) for t, s in zip(want, cand.utr3_seq.tolist())
            if t not in res]
    errors = {}
    if todo:
        nproc = nproc or max(1, (os.cpu_count() or 4) - 2)
        with Pool(nproc) as p:
            for tid, val in p.imap_unordered(_worker, todo, chunksize=16):
                if isinstance(val, tuple):
                    errors[tid] = val[1]
                else:
                    res[tid] = val
    ids = [t for t in want if t in res]
    lens = np.array([res[t].shape[1] for t in ids], dtype=np.int64)
    off = np.concatenate([[0], np.cumsum(lens)])
    flat = np.concatenate([res[t] for t in ids], axis=1)
    np.savez_compressed(out, ids=np.array(ids), offsets=off, acc=flat,
                        keep=np.array(KEEP), params=np.array([W, L, U]))
    return {"n_transcripts": len(ids), "n_reused_from_existing_caches":
            n_reused, "n_computed_here": len(todo) - len(errors),
            "n_errors": len(errors), "errors": errors,
            "total_positions": int(lens.sum()),
            "pfl_fold_W": W, "pfl_fold_L": L, "pfl_fold_u_max": U,
            "reused_from": list(reuse), "path": out}


def _seed_pair_features(args):
    """Features for one (construct, transcript) using the SEED duplex only.

    Same algebra as riscpool.features._pair_features: dG_eff is the duplex
    free energy PLUS the cost of opening the site, dG_duplex - RT ln
    P_unpaired, K_site = exp(dG_eff/RT), and sites on one transcript combine
    in parallel as 1/K = sum 1/K_site.
    What differs is that the duplex is formed with guide positions 2-8, the
    only part of the guide the recovery identifies, rather than with the full
    19-mer.
    """
    import RNA

    from .features import AU_WIN, FLANK, RT, find_sites
    (construct, seed_rna, pseudo_guide, tid, symbol, utr3, acc15) = args
    sites = find_sites(pseudo_guide, utr3)
    if not sites:
        return None
    n = len(utr3)
    rows, inv_K = [], 0.0
    for i, cls in sites:
        lo, hi = max(0, i - 1 - FLANK), min(n, i + 6 + 1 + FLANK)
        win = utr3[lo:hi].replace("T", "U")
        try:
            dgd = float(RNA.duplexfold(seed_rna, win).energy)
        except Exception:
            dgd = np.nan
        end = min(n - 1, i + 6)
        p = float(acc15[end]) if acc15 is not None and end < len(acc15) \
            else np.nan
        p = min(max(p, 1e-12), 1.0) if np.isfinite(p) else np.nan
        # see riscpool.features: the opening cost is added, not subtracted
        ddg = dgd - RT * np.log(p) if np.isfinite(p) and np.isfinite(dgd) \
            else np.nan
        a, b = max(0, i - AU_WIN), min(n, i + 6 + AU_WIN)
        loc = utr3[a:b]
        if np.isfinite(ddg):
            inv_K += np.exp(-ddg / RT)
        rows.append({"construct": construct, "transcript_id": tid,
                     "gene_symbol": symbol, "site_start": int(i),
                     "site_class": cls, "dg_duplex_kcal": dgd,
                     "p_unpaired_15": p, "ddG_kcal": ddg,
                     "rel_pos_in_utr3": float(i / max(1, n)),
                     "local_au_content": float(
                         sum(c in "AT" for c in loc) / max(1, len(loc))),
                     "utr3_len": int(n)})
    K = 1.0 / inv_K if inv_K > 0 else np.nan
    for r in rows:
        r["K_transcript"] = K
        r["n_sites"] = len(rows)
    return rows


def build_features(seeds, out=FEAT, nproc=None):
    """`seeds` maps construct -> recovered 7-mer site."""
    from multiprocessing import Pool

    from .accessibility import Accessibility

    cand = load_candidates()
    acc = Accessibility(ACC)
    cache = {t: acc.get(t, 15) for t in cand.transcript_id}
    jobs = []
    for construct, site7 in seeds.items():
        pg = pseudo_guide_from_site(site7)
        seed_rna = kmers.revcomp(site7).replace("T", "U")
        core = kmers.revcomp(pg[1:7])
        for tid, sym, utr3 in zip(cand.transcript_id, cand.gene_symbol,
                                  cand.utr3_seq):
            if core in utr3:
                jobs.append((construct, seed_rna, pg, tid, sym, utr3,
                             cache.get(tid)))
    nproc = nproc or max(1, (os.cpu_count() or 4) - 2)
    rows = []
    with Pool(nproc) as p:
        for r in p.imap_unordered(_seed_pair_features, jobs, chunksize=64):
            if r:
                rows.extend(r)
    df = pd.DataFrame(rows)
    df.to_parquet(out, index=False, compression="zstd")
    return df


def load_features():
    return pd.read_parquet(FEAT)


def transcript_level(df=None):
    from .features import transcript_level as _tl
    d = load_features() if df is None else df
    d = d.copy()
    for c in ("cds_len", "guide_gc", "guide_asymmetry_kcal",
              "seed_pairing_stability_kcal", "x_rel", "dist_to_utr3_start",
              "dist_to_utr3_end"):
        if c not in d.columns:
            d[c] = np.nan
    return _tl(d)
