"""
Measured off-target response per construct, and data-driven seed recovery.

Response. For each construct, VALUE (log10 of siRNA channel over mock channel)
is collapsed probe -> gene symbol -> GENCODE canonical transcript. Negative
means repressed. Per-array responses are kept so that seed recovery and
evaluation can be done on disjoint arrays.

Seed recovery. See kmers.py for why this is measured rather than assumed.
"""

import os

import numpy as np
import pandas as pd

from . import kmers
from .data_gencode import canonical_by_symbol
from .data_gse5814 import load
from .provenance import DATA

RESP = os.path.join(DATA, "gse5814_gene_response.parquet")
UTR = os.path.join(DATA, "candidate_utr3.parquet")


def build_candidate_utrs(out=UTR):
    """The transcripts that are both expressed in these cells and have a
    GENCODE canonical 3'UTR. This is the retrieval universe for everything
    downstream."""
    from .hela import load_abundance
    ab = load_abundance()
    can = canonical_by_symbol()[["gene_symbol", "transcript_id", "utr3_seq",
                                 "cds_seq", "utr5_seq", "utr3_len", "cds_len"]]
    ab = ab.drop(columns=[c for c in ("utr3_len", "cds_len") if c in ab.columns])
    df = ab.merge(can, on=["gene_symbol", "transcript_id"], how="inner")
    df = df[df.utr3_len >= 10].reset_index(drop=True)
    df.to_parquet(out, index=False, compression="zstd")
    return df


def load_candidates():
    return pd.read_parquet(UTR)


def build_gene_response(out=RESP):
    ann, smeta, expr = load()
    sir = smeta[smeta.is_sirna_hela]
    amap = (ann.dropna(subset=["gene_symbol"])
               .drop_duplicates(subset=["probe_id"])[["probe_id",
                                                      "gene_symbol"]])
    e = expr[expr.geo_accession.isin(sir.geo_accession)].copy()
    if "QUALITY" in e.columns:
        e = e[e.QUALITY >= 1]
    e = e[np.isfinite(e.VALUE)]
    e = e.merge(amap, on="probe_id", how="inner")
    per_array = (e.groupby(["geo_accession", "gene_symbol"])
                  .agg(value=("VALUE", "median"),
                       pvalue=("PVALUE", "median"),
                       logint=("LOGINTENSITY", "median"))
                  .reset_index())
    meta = sir[["geo_accession", "construct", "target_gene", "backbone",
                "variant", "mut_position", "seed_altered", "replicate",
                "platform"]]
    per_array = per_array.merge(meta, on="geo_accession", how="left")
    per_array.to_parquet(out, index=False, compression="zstd")
    return per_array


def load_response():
    return pd.read_parquet(RESP)


def construct_response(resp, construct, arrays=None, candidates=None):
    """Median measured log10 ratio per gene for one construct."""
    d = resp[resp.construct == construct]
    if arrays is not None:
        d = d[d.geo_accession.isin(arrays)]
    g = (d.groupby("gene_symbol")
          .agg(value=("value", "median"), n=("value", "size"))
          .reset_index())
    if candidates is not None:
        g = g[g.gene_symbol.isin(candidates)]
    return g


def scan_construct(G, cand_symbols, resp, construct, arrays=None, k=7,
                   min_n=30):
    """
    Enrichment scan for one construct against the prebuilt incidence matrix G
    whose rows are cand_symbols in order.
    Returns (ranked DataFrame, n_genes_used).
    """
    g = construct_response(resp, construct, arrays=arrays,
                           candidates=set(cand_symbols))
    pos = pd.Series(np.arange(len(cand_symbols)), index=cand_symbols)
    idx = pos.reindex(g.gene_symbol).to_numpy()
    sub = G[idx]
    delta, t, n1 = kmers.enrichment_scan(sub, g.value.to_numpy(),
                                         min_n=min_n)
    order = np.argsort(np.where(np.isnan(t), np.inf, t))   # most negative t
    top = order[:50]
    out = pd.DataFrame({
        "site_kmer": [kmers.index_to_kmer(int(i), k) for i in top],
        "delta_mean_log10ratio": delta[top],
        "welch_t": t[top],
        "n_transcripts_with_site": n1[top].astype(int),
    })
    return out, int(len(g))
