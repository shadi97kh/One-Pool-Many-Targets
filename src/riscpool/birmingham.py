"""
D2: Birmingham et al. 2006, recovered through ArrayExpress.

  Birmingham A, Anderson EM, Reynolds A, Ilsley-Tyree D, Leake D, Fedorov Y,
  Baskerville S, Maksimova E, Robinson K, Karpilow J, Marshall WS,
  Khvorova A. "3' UTR seed matches, but not overall identity, are associated
  with RNAi off-targets." Nat Methods 2006; 3:199-204. PMID 16489337.

The earlier attempt recorded in this repository failed, and the reasons it
gave were correct as far as they went: the article has no PMC identifier,
NCBI elink returns no GEO series for its PMID, and the van Dongen
supplementary archive that reprocesses the data contains only images. What it
missed is that the data was deposited in ArrayExpress rather than GEO, under
an accession the paper's own PMID is attached to.

The accession is not guessed. It was found by searching the ArrayExpress
collection for the article's title phrase, and the identification is checked
against the IDF, which carries the line

    PubMed ID	16489337

alongside the article title and the Dharmacon author list. That check is run
in code, not asserted here: `identify` below refuses the accession if the IDF
does not name the expected PMID.

What the deposit contains that the paper's supplementary material does not:
the SDRF gives the SENSE STRAND SEQUENCE of every siRNA as its compound
factor value, so the guide strands are recoverable by reverse complement
rather than by transcription from a figure.
"""

import os
import re

import numpy as np
import pandas as pd

from . import kmers
from .provenance import DATA

ACCESSION = "E-MEXP-668"
EXPECTED_PMID = "16489337"
BASE = f"https://www.ebi.ac.uk/biostudies/files/{ACCESSION}"
RAW = os.path.join(DATA, "raw", "birmingham")
IDF = os.path.join(RAW, f"{ACCESSION}.idf.txt")
SDRF = os.path.join(RAW, f"{ACCESSION}.sdrf.txt")
SIRNA = os.path.join(DATA, "birmingham_sirna.parquet")
RESP = os.path.join(DATA, "birmingham_response.parquet")


def identify(idf_path=IDF, expected_pmid=EXPECTED_PMID):
    """Confirm from the IDF that this accession really is the target paper."""
    if not os.path.exists(idf_path):
        return {"identified": False, "reason": "IDF not downloaded"}
    txt = open(idf_path, errors="replace").read()
    pmid = re.search(r"^PubMed ID\t(\S+)", txt, flags=re.M)
    title = re.search(r"^Publication Title\t(.+)$", txt, flags=re.M)
    authors = re.search(r"^Publication Author List\t(.+)$", txt, flags=re.M)
    itit = re.search(r"^Investigation Title\t(.+)$", txt, flags=re.M)
    got = pmid.group(1).strip() if pmid else None
    return {
        "identified": bool(got == expected_pmid),
        "pubmed_id_in_idf": got,
        "expected_pubmed_id": expected_pmid,
        "publication_title_in_idf": title.group(1).strip() if title else None,
        "investigation_title_in_idf": itit.group(1).strip() if itit else None,
        "author_list_in_idf": (authors.group(1).strip()[:300]
                               if authors else None),
    }


def parse_sdrf(path=SDRF):
    """Array data file -> siRNA sense sequence and dose, from the SDRF."""
    d = pd.read_csv(path, sep="\t", dtype=str).fillna("")
    cols = list(d.columns)

    def col(name, which=0):
        hits = [c for c in cols if c.strip().lower() == name.lower()]
        return hits[which] if len(hits) > which else None

    fdata = col("Array Data File")
    comp = [c for c in cols if c.startswith("Factor Value [compound]")]
    dose = [c for c in cols if c.startswith("Factor Value [dose]")]
    lab = col("Label")
    rows = []
    for _, r in d.iterrows():
        f = r[fdata].strip()
        if not f:
            continue
        cv = r[comp[0]].strip() if comp else ""
        m = re.match(r"siRNA sense ([ACGTU]+)", cv)
        rows.append({
            "array_data_file": f,
            "compound": cv,
            "sense_5to3_dna": (m.group(1).replace("U", "T")
                               if m else None),
            "dose": r[dose[0]].strip() if dose else "",
            "label": r[lab].strip() if lab else "",
            "hybridisation": r.get("Hybridization Name", ""),
            "cell_line": r.get("Characteristics [CellLine]", ""),
        })
    s = pd.DataFrame(rows)
    # one row per array: the siRNA-labelled channel names the construct
    per_file = []
    for f, g in s.groupby("array_data_file"):
        sir = g[g.sense_5to3_dna.notna()]
        if sir.empty:
            per_file.append({"array_data_file": f, "sense_5to3_dna": None,
                             "dose": None, "cell_line": g.cell_line.iloc[0],
                             "compound": ";".join(sorted(set(g.compound)))})
            continue
        row = sir.iloc[0]
        per_file.append({
            "array_data_file": f,
            "sense_5to3_dna": row.sense_5to3_dna,
            "dose": row.dose,
            "cell_line": row.cell_line,
            "compound": row.compound,
            "label_of_sirna_channel": row.label,
        })
    p = pd.DataFrame(per_file)
    p["guide_5to3_dna"] = p.sense_5to3_dna.map(
        lambda s: kmers.revcomp(s) if isinstance(s, str) else None)
    p["seed_2_8_dna"] = p.guide_5to3_dna.map(
        lambda s: s[1:8] if isinstance(s, str) else None)
    p["site_7mer_m8_dna"] = p.seed_2_8_dna.map(
        lambda s: kmers.revcomp(s) if isinstance(s, str) else None)
    p["construct"] = [
        f"BIRM-{s[:8]}-{d}nM" if isinstance(s, str) else None
        for s, d in zip(p.sense_5to3_dna, p.dose)]
    return p


def parse_agilent(path):
    """
    One array data file to a per-probe table.

    ArrayExpress serves these as a single flat table with prefixed column
    names (`Software Unknown:ProbeName`, `Feature Extraction Software:
    LogRatio`) rather than in the original three-block Agilent Feature
    Extraction layout. Both are handled; the prefixes are stripped and the
    columns are matched by their bare names.

    Sign convention. Feature Extraction reports LogRatio as
    log10(red/green) = log10(Cy5/Cy3). The SDRF says the siRNA-treated
    extract carries Cy5 on every array that has one, so LogRatio is already
    log10(siRNA/mock) and a negative value is repression. The dye assignment
    is read from the SDRF per array rather than assumed, and an array whose
    siRNA channel were Cy3 would have its sign flipped; see build_response.
    """
    import gzip
    op = gzip.open if str(path).endswith(".gz") else open
    with op(path, "rt", errors="replace") as fh:
        first = fh.readline().rstrip("\n").split("\t")
        flat = any(c.split(":")[-1].strip() == "ProbeName" for c in first)
        if flat:
            names = [c.split(":")[-1].strip() for c in first]
            rows = [line.rstrip("\n").split("\t") for line in fh]
            rows = [r for r in rows if len(r) >= len(names)]
            d = pd.DataFrame([r[:len(names)] for r in rows], columns=names)
        else:
            fh.seek(0)
            header, rows = None, []
            for line in fh:
                p = line.rstrip("\n").split("\t")
                if not p:
                    continue
                if p[0] == "FEATURES":
                    header = p
                    continue
                if p[0] == "DATA" and header is not None:
                    rows.append(p)
            if header is None:
                raise ValueError(f"no parsable feature table in {path}")
            d = pd.DataFrame([r[:len(header)] for r in rows], columns=header)
    keep = {"ProbeName": "probe_name", "GeneName": "gene_symbol",
            "SystematicName": "systematic_name", "LogRatio": "log10_ratio",
            "LogRatioError": "log10_ratio_error",
            "PValueLogRatio": "p_log_ratio", "ControlType": "control_type",
            "gIsWellAboveBG": "green_well_above_bg",
            "rIsWellAboveBG": "red_well_above_bg"}
    have = {k: v for k, v in keep.items() if k in d.columns}
    missing = [k for k in ("ProbeName", "GeneName", "LogRatio")
               if k not in d.columns]
    if missing:
        raise ValueError(f"{path} lacks columns {missing}")
    d = d[list(have)].rename(columns=have)
    for c in ("log10_ratio", "log10_ratio_error", "p_log_ratio"):
        if c in d.columns:
            d[c] = pd.to_numeric(d[c], errors="coerce")
    if "control_type" in d.columns:
        d = d[pd.to_numeric(d.control_type, errors="coerce").fillna(0) == 0]
    d = d[d.gene_symbol.astype(str).str.len() > 0]
    d = d[d.gene_symbol.astype(str) != "null"]
    return d


def build_response(files, sdrf, out=RESP):
    """Collapse every array to a per-gene median log10 ratio per construct."""
    frames = []
    meta = sdrf.set_index("array_data_file")
    for path in files:
        name = os.path.basename(path)
        if name not in meta.index:
            continue
        m = meta.loc[name]
        if not isinstance(m.get("construct"), str):
            continue
        d = parse_agilent(path)
        d = d[np.isfinite(d.log10_ratio)]
        lab = str(m.get("label_of_sirna_channel", "") or "")
        if lab == "Cy3":
            # siRNA on the green channel: LogRatio is log10(mock/siRNA)
            d = d.assign(log10_ratio=-d.log10_ratio)
        elif lab != "Cy5":
            raise ValueError(
                f"array {name} has siRNA channel label {lab!r}; the sign of "
                "the log ratio cannot be established, so it is not used")
        g = (d.groupby("gene_symbol", as_index=False)
              .agg(value=("log10_ratio", "median"),
                   n_probes=("probe_name", "size")))
        g["construct"] = m["construct"]
        g["guide_5to3_dna"] = m["guide_5to3_dna"]
        g["dose_nM"] = float(m["dose"]) if m["dose"] else np.nan
        g["array_data_file"] = name
        g["sirna_channel_label"] = lab
        frames.append(g)
    if not frames:
        raise RuntimeError("no Agilent arrays parsed")
    r = pd.concat(frames, ignore_index=True)
    r.to_parquet(out, index=False, compression="zstd")
    return r


def load_response():
    return pd.read_parquet(RESP)
