"""
Real siRNA sequences for GSE5814, per GSM accession.

The GEO deposit contains no sequences and the RNA 2006 publisher releases no
machine-readable full text (both failures are recorded in
data/PROVENANCE.json). The guide strands are instead taken from the
supplementary table of

  Garcia DM, Baek D, Shin C, Bell GW, Grimson A, Bartel DP.
  "Weak seed-pairing stability and high target-site abundance decrease the
  proficiency of lsy-6 and other microRNAs." Nat Struct Mol Biol 2011;
  18:1139-1146. doi:10.1038/nsmb.2115

whose Supplementary Table (MOESM7) lists, for all 175 microarrays it
reanalysed, the array's GEO accession alongside the guide-strand sequence,
the seed (positions 2-8) and the 7mer-m8 site. 66 of those rows are GSE5814.
Joining on GSM accession means no sequence is matched to a sample by name or
by guesswork.

The sequences are independently corroborated inside this repository by
seeds.py, which recovers the same 7mer-m8 sites from the measured expression
response without using this file at all.
"""

import os
import warnings

import pandas as pd

from . import kmers
from .provenance import DATA

warnings.filterwarnings("ignore", category=UserWarning)

GARCIA = os.path.join(DATA, "lit", "garcia2011", "nsmb2115_MOESM7.xlsx")
SHEET = "175 microarrays analyzed"
OUT = os.path.join(DATA, "sirna_sequences.parquet")


def build(out=OUT):
    from .data_gse5814 import load
    _, smeta, _ = load()
    d = pd.read_excel(GARCIA, SHEET)
    d = d[d["Data set ID"].astype(str).str.strip() == "GSE5814"].copy()
    d = d.rename(columns={
        "Array ID": "geo_accession",
        "Seed + nt 8": "seed_2_8_rna",
        "7mer-m8 site": "site_7mer_m8_rna",
        "sRNA sequence": "guide_5to3_rna",
        "7mer-m8 SPS (kcal/mol)": "sps_7mer_m8_kcal",
        "6mer SPS (kcal/mol)": "sps_6mer_kcal",
        "TA HeLa (log10)": "target_abundance_hela_log10",
    })
    keep = ["geo_accession", "guide_5to3_rna", "seed_2_8_rna",
            "site_7mer_m8_rna", "sps_7mer_m8_kcal", "sps_6mer_kcal",
            "target_abundance_hela_log10"]
    d = d[[c for c in keep if c in d.columns]]
    for c in ("guide_5to3_rna", "seed_2_8_rna", "site_7mer_m8_rna"):
        d[c] = d[c].astype(str).str.strip().str.upper()

    # DNA forms, and the site recomputed from the guide rather than trusted
    d["guide_5to3_dna"] = d.guide_5to3_rna.str.replace("U", "T")
    d["seed_2_8_dna"] = d.seed_2_8_rna.str.replace("U", "T")
    d["site_7mer_m8_dna"] = d.site_7mer_m8_rna.str.replace("U", "T")
    d["seed_from_guide"] = d.guide_5to3_dna.str[1:8]
    d["site_from_guide"] = d.seed_from_guide.map(kmers.revcomp)
    d["site_6mer_dna"] = d.guide_5to3_dna.str[1:7].map(kmers.revcomp)
    d["internally_consistent"] = (
        (d.seed_from_guide == d.seed_2_8_dna)
        & (d.site_from_guide == d.site_7mer_m8_dna))
    d["guide_len"] = d.guide_5to3_dna.str.len()

    m = smeta[["geo_accession", "construct", "target_gene", "backbone",
               "variant", "mut_position", "seed_altered", "platform",
               "replicate", "title"]]
    d = d.merge(m, on="geo_accession", how="left")
    d.to_parquet(out, index=False, compression="zstd")
    return d


def load_sequences():
    return pd.read_parquet(OUT)


def per_construct():
    """One guide sequence per construct, with an explicit check that every
    array of a construct carries the same sequence."""
    d = load_sequences().dropna(subset=["construct"])
    g = (d.groupby("construct")
          .agg(n_arrays=("geo_accession", "size"),
               n_distinct_guides=("guide_5to3_dna", "nunique"),
               guide_5to3_dna=("guide_5to3_dna", "first"),
               seed_2_8_dna=("seed_from_guide", "first"),
               site_7mer_m8_dna=("site_from_guide", "first"),
               site_6mer_dna=("site_6mer_dna", "first"),
               target_gene=("target_gene", "first"),
               mut_position=("mut_position", "first"),
               sps_7mer_m8_kcal=("sps_7mer_m8_kcal", "first"))
          .reset_index())
    return g
