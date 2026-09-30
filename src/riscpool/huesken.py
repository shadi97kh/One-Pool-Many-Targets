"""
D5: Huesken et al. siRNA efficacy set.

Huesken D, Lange J, Mickanin C, Weiler J, Asselbergs F, Warner J, Meloon B,
Engel S, Rosenberg A, Cohen D, Labow M, Reinhardt M, Natt F, Hall J.
"Design of a genome-wide siRNA library using an artificial neural network."
Nat Biotechnol 2005;23:995-1001.

Redistributed in the OligoFormer repository. Two files are used: the efficacy
table (19-mer guide plus measured remaining expression), and the per-gene
tiling tables from the same repository, which give the target gene for every
siRNA. The gene assignment is not taken on trust: each siRNA is matched to a
gene by locating the reverse complement of its guide inside that gene's tiled
target sequences, so the assignment is derived from sequence.
"""

import glob
import os

import pandas as pd

from . import kmers
from .provenance import DATA

HU = os.path.join(DATA, "raw", "huesken_Hu.csv")
GENES = os.path.join(DATA, "raw", "huesken_genes")
OUT = os.path.join(DATA, "huesken.parquet")


def build(out=OUT):
    hu = pd.read_csv(HU)
    hu = hu.rename(columns={"19mer": "guide_19mer_rna",
                            "expression": "remaining_expression_pct"})
    hu["guide_19mer_dna"] = hu.guide_19mer_rna.str.upper().str.replace("U", "T")
    hu["target_site_dna"] = hu.guide_19mer_dna.map(kmers.revcomp)
    hu["efficacy"] = 1.0 - hu.remaining_expression_pct / 100.0

    site_index = {s: i for i, s in enumerate(hu.target_site_dna)}
    assign = {}
    n_tiles = 0
    for f in sorted(glob.glob(os.path.join(GENES, "*.csv"))):
        g = os.path.basename(f)[:-4]
        d = pd.read_csv(f, encoding="utf-8-sig")
        ext = (d[d.columns[0]].astype(str)
               .str.extract(r"--\s*([ACGUTacgut]+)")[0].dropna())
        n_tiles += len(ext)
        for x in ext.str.upper().str.replace("U", "T"):
            for j in range(len(x) - 18):
                k = x[j:j + 19]
                if k in site_index:
                    assign.setdefault(k, g)
    hu["target_gene"] = hu.target_site_dna.map(assign)
    hu.to_parquet(out, index=False, compression="zstd")
    return hu, {"n_sirnas": int(len(hu)),
                "n_assigned_to_a_target_gene": int(hu.target_gene.notna().sum()),
                "n_target_genes": int(hu.target_gene.nunique()),
                "n_tiled_sequences_searched": int(n_tiles),
                "efficacy_mean": float(hu.efficacy.mean()),
                "efficacy_sd": float(hu.efficacy.std()),
                "remaining_expression_pct_min": float(
                    hu.remaining_expression_pct.min()),
                "remaining_expression_pct_max": float(
                    hu.remaining_expression_pct.max())}


def load():
    return pd.read_parquet(OUT)
