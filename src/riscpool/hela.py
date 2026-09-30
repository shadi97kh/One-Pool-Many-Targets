"""
D4: relative transcript abundance in the cells the off-target response was
measured in.

The abundance vector comes from the mock-transfection control channel of
GSE5814 itself (INTENSITY1 = raw Cy3 = CH1 = mock, per GEO's own column
definition). Same cells, same passage, same platform, same hybridisation as the
response being predicted, so platform bias is shared between the abundance
vector and the response rather than introduced by an external dataset.

Probes are collapsed to gene symbols and then joined to the GENCODE canonical
transcript per symbol. What leaves this module is a RELATIVE abundance vector
that sums to one; the conversion to molecules per cell is a separate, stated,
cited step and lives in e5 where it is reported as a limitation.
"""

import os

import numpy as np
import pandas as pd

from .data_gencode import canonical_by_symbol
from .data_gse5814 import load
from .provenance import DATA

OUT = os.path.join(DATA, "hela_abundance.parquet")


def build(min_quality=1, out=OUT):
    ann, smeta, expr = load()
    hela = smeta[smeta.is_sirna_hela].geo_accession.tolist()
    e = expr[expr.geo_accession.isin(hela)].copy()

    n_before = len(e)
    if min_quality is not None and "QUALITY" in e.columns:
        e = e[e.QUALITY >= min_quality]
    e = e[np.isfinite(e.INTENSITY1) & (e.INTENSITY1 > 0)]

    # per probe, robust centre across every mock channel that saw it
    probe = (e.groupby("probe_id")
              .agg(mock_intensity_median=("INTENSITY1", "median"),
                   mock_intensity_mean=("INTENSITY1", "mean"),
                   n_arrays=("INTENSITY1", "size"))
              .reset_index())

    amap = (ann.dropna(subset=["gene_symbol"])
               .drop_duplicates(subset=["probe_id"])[["probe_id",
                                                     "gene_symbol",
                                                     "accession"]])
    probe = probe.merge(amap, on="probe_id", how="inner")
    probe = probe[probe.gene_symbol.str.len() > 0]

    gene = (probe.groupby("gene_symbol")
                 .agg(mock_intensity=("mock_intensity_median", "median"),
                      n_probes=("probe_id", "size"),
                      n_arrays=("n_arrays", "max"))
                 .reset_index())

    can = canonical_by_symbol()[["gene_symbol", "transcript_id", "gene_id",
                                 "utr3_len", "cds_len", "tx_len",
                                 "mane_select"]]
    df = gene.merge(can, on="gene_symbol", how="inner")
    df = df[df.utr3_len > 0].copy()
    df["x_rel"] = df.mock_intensity / df.mock_intensity.sum()
    df = df.sort_values("x_rel", ascending=False).reset_index(drop=True)
    df.to_parquet(out, index=False, compression="zstd")

    return {
        "n_expr_rows_before_quality_filter": int(n_before),
        "n_expr_rows_after": int(len(e)),
        "n_mock_arrays_used": int(len(hela)),
        "n_probes_with_signal": int(len(probe)),
        "n_gene_symbols": int(len(gene)),
        "n_genes_joined_to_gencode_canonical_with_utr3": int(len(df)),
        "abundance_gini_like_top1pct_share": float(
            df.x_rel.iloc[:max(1, len(df) // 100)].sum()),
        "abundance_dynamic_range_log10": float(
            np.log10(df.mock_intensity.max() / df.mock_intensity.min())),
        "path": out,
    }


def load_abundance():
    return pd.read_parquet(OUT)
