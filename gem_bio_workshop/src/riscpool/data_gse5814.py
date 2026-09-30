"""
D1: GSE5814 (Jackson et al. 2006, RNA 12:1179) parser.

Two-colour Rosetta/Agilent arrays. Per GEO's own column definitions:
    VALUE       corrected (normalised) log10 ratio of channels CH2/CH1
    LOGINTENSITY corrected average log intensity of channels
    INTENSITY1  raw Cy3 intensity, CH1  -> mock-transfected control channel
    INTENSITY2  raw Cy5 intensity, CH2  -> siRNA-transfected channel
    PVALUE      p-value of the log ratio
    QUALITY     1 if good and non-control, 0 otherwise

CH1 is mock and CH2 is siRNA for every HeLa sample in this series (verified
from !Sample_characteristics_ch1/ch2, not assumed). So VALUE < 0 means the
transcript went DOWN on siRNA transfection. INTENSITY1 is therefore the
mock-control abundance channel that D4 calls for.
"""

import gzip
import os
import re

import numpy as np
import pandas as pd

from .provenance import DATA

SOFT = os.path.join(DATA, "raw", "GSE5814_family.soft.gz")
SAMPLE_COLS = ["ID_REF", "VALUE", "LOGINTENSITY", "INTENSITY1", "INTENSITY2",
               "PVALUE", "QUALITY"]


def parse_soft(soft_path=SOFT):
    """Single streaming pass over the SOFT family file."""
    platforms, samples, sample_meta = {}, {}, {}
    cur_kind = cur_id = None
    in_table = False
    header = None
    rows = []

    with gzip.open(soft_path, "rt", errors="replace") as fh:
        for line in fh:
            line = line.rstrip("\n").rstrip("\r")
            if not line:
                continue
            c = line[0]
            if c == "^":
                k, _, v = line[1:].partition(" = ")
                cur_kind, cur_id = k.strip().upper(), v.strip()
                if cur_kind == "SAMPLE":
                    sample_meta.setdefault(cur_id, {"geo_accession": cur_id})
                continue
            if c == "!":
                tag = line[1:]
                low = tag.lower()
                if low.startswith("platform_table_begin") or \
                        low.startswith("sample_table_begin"):
                    in_table, header, rows = True, None, []
                    continue
                if low.startswith("platform_table_end"):
                    in_table = False
                    platforms[cur_id] = pd.DataFrame(rows, columns=header)
                    continue
                if low.startswith("sample_table_end"):
                    in_table = False
                    samples[cur_id] = pd.DataFrame(rows, columns=header)
                    continue
                if cur_kind == "SAMPLE" and " = " in tag:
                    k, _, v = tag.partition(" = ")
                    k = k.strip()
                    d = sample_meta[cur_id]
                    if k in d:
                        d[k] = f"{d[k]} | {v.strip()}"
                    else:
                        d[k] = v.strip()
                continue
            if c == "#":
                continue
            if in_table:
                parts = line.split("\t")
                if header is None:
                    header = parts
                else:
                    if len(parts) < len(header):
                        parts = parts + [""] * (len(header) - len(parts))
                    rows.append(parts[:len(header)])
    return platforms, samples, sample_meta


_POS = re.compile(r"pos\s*(\d+)\s*mut", re.I)


def parse_construct(ch2_text, title):
    """
    Turn the GEO sample annotation into a construct identity. Nothing here is
    invented: every field is read off the submitter's own free-text label.
    Returns dict or None if the sample is not a HeLa siRNA transfection.
    """
    s = (ch2_text or "") + " || " + (title or "")
    low = s.lower()
    if "doxycycline" in low or "ht29" in low:
        return None                      # inducible shRNA line, not a siRNA
    rep = None
    m = re.search(r"24 hr,\s*([abc])\b", s)
    if m:
        rep = m.group(1)
    mp = _POS.search(s)
    if "mapk14" in low:
        if mp:
            n = int(mp.group(1))
            return {"target_gene": "MAPK14", "backbone": "MAPK14-193",
                    "variant": f"pos{n:02d}mut", "mut_position": n,
                    "seed_altered": bool(2 <= n <= 8), "replicate": rep,
                    "construct": f"MAPK14-193_pos{n:02d}mut"}
        if "normal" in low or re.search(r"mapk14-193|193-mapk14", low):
            return {"target_gene": "MAPK14", "backbone": "MAPK14-193",
                    "variant": "parent", "mut_position": 0,
                    "seed_altered": False, "replicate": rep,
                    "construct": "MAPK14-193_parent"}
    if "pik3cb" in low:
        m2 = re.search(r"pik3cb-(\d+)", low)
        sid = m2.group(1) if m2 else "NA"
        return {"target_gene": "PIK3CB", "backbone": f"PIK3CB-{sid}",
                "variant": "parent", "mut_position": 0, "seed_altered": False,
                "replicate": rep, "construct": f"PIK3CB-{sid}_parent"}
    if "plk" in low:
        m2 = re.search(r"plk1?[-\s]?(\d{3,4})", low)
        sid = m2.group(1) if m2 else "NA"
        return {"target_gene": "PLK1", "backbone": f"PLK1-{sid}",
                "variant": "parent", "mut_position": 0, "seed_altered": False,
                "replicate": rep, "construct": f"PLK1-{sid}_parent"}
    if re.search(r"\bluc\b", low):
        return {"target_gene": "LUC_CONTROL", "backbone": "Luc",
                "variant": "parent", "mut_position": 0, "seed_altered": False,
                "replicate": rep, "construct": "Luc_control"}
    return None


def build(soft_path=SOFT, out_dir=DATA):
    platforms, samples, meta = parse_soft(soft_path)

    # ---- platform probe annotation, normalised across the three designs ----
    ann = []
    for gpl, df in platforms.items():
        sym_col = "GeneSymbol" if "GeneSymbol" in df.columns else "ORF"
        acc_col = "GB_ACC" if "GB_ACC" in df.columns else "SEQUENCE_ID"
        sub = pd.DataFrame({
            "platform": gpl,
            "probe_id": df["ID"].astype(str),
            "gene_symbol": df[sym_col].astype(str).str.strip(),
            "accession": df[acc_col].astype(str).str.strip(),
        })
        ann.append(sub)
    ann = pd.concat(ann, ignore_index=True)
    ann.loc[ann.gene_symbol.isin(["", "nan", "None"]), "gene_symbol"] = np.nan

    # ---- sample metadata + construct assignment ----
    srows = []
    for gsm, d in meta.items():
        rec = {
            "geo_accession": gsm,
            "title": d.get("Sample_title", ""),
            "platform": d.get("Sample_platform_id", ""),
            "ch1": d.get("Sample_characteristics_ch1", ""),
            "ch2": d.get("Sample_characteristics_ch2", ""),
            "label_ch1": d.get("Sample_label_ch1", ""),
            "label_ch2": d.get("Sample_label_ch2", ""),
        }
        con = parse_construct(rec["ch2"], rec["title"])
        rec["is_sirna_hela"] = con is not None
        rec.update(con or {"target_gene": None, "backbone": None,
                           "variant": None, "mut_position": None,
                           "seed_altered": None, "replicate": None,
                           "construct": None})
        srows.append(rec)
    smeta = pd.DataFrame(srows).sort_values("geo_accession").reset_index(drop=True)

    # ---- expression tables ----
    keep = []
    for gsm, df in samples.items():
        cols = [c for c in SAMPLE_COLS if c in df.columns]
        sub = df[cols].copy()
        sub.insert(0, "geo_accession", gsm)
        keep.append(sub)
    expr = pd.concat(keep, ignore_index=True)
    for c in ("VALUE", "LOGINTENSITY", "INTENSITY1", "INTENSITY2", "PVALUE",
              "QUALITY"):
        if c in expr.columns:
            expr[c] = pd.to_numeric(expr[c], errors="coerce")
    expr = expr.rename(columns={"ID_REF": "probe_id"})
    expr["probe_id"] = expr["probe_id"].astype(str)

    os.makedirs(out_dir, exist_ok=True)
    p_ann = os.path.join(out_dir, "gse5814_probe_annotation.parquet")
    p_smp = os.path.join(out_dir, "gse5814_samples.tsv")
    p_exp = os.path.join(out_dir, "gse5814_expression.parquet")
    ann.to_parquet(p_ann, index=False)
    smeta.to_csv(p_smp, sep="\t", index=False)
    expr.to_parquet(p_exp, index=False)
    return {"annotation": p_ann, "samples": p_smp, "expression": p_exp,
            "n_platforms": len(platforms), "n_samples": len(samples),
            "n_expr_rows": int(len(expr)),
            "n_sirna_hela_samples": int(smeta.is_sirna_hela.sum()),
            "n_constructs": int(smeta.loc[smeta.is_sirna_hela,
                                          "construct"].nunique())}


def load():
    return (pd.read_parquet(os.path.join(DATA,
                                         "gse5814_probe_annotation.parquet")),
            pd.read_csv(os.path.join(DATA, "gse5814_samples.tsv"), sep="\t"),
            pd.read_parquet(os.path.join(DATA, "gse5814_expression.parquet")))
