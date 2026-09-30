"""D5: Huesken siRNA efficacy set, located in the OligoFormer repository."""
import json
import os
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import provenance as P  # noqa: E402

RAW = "https://raw.githubusercontent.com/lulab/OligoFormer/main"
CANDS = [
    ("Comparison%20methods/Monopoli-RF/datasets/Hu.csv",
     "data/raw/huesken_Hu.csv", "normalised Huesken efficacy table"),
    ("Comparison%20methods/Monopoli-RF/datasets/Hu_unnorm.csv",
     "data/raw/huesken_Hu_unnorm.csv", "unnormalised Huesken efficacy table"),
    ("Comparison%20methods/siRNAPred/dataset/HuTD.csv",
     "data/raw/huesken_HuTD.csv", "Huesken table with target descriptors"),
    ("data/Huesken.csv", "data/raw/huesken_main.csv",
     "OligoFormer main data directory candidate"),
    ("data/huesken.txt", "data/raw/huesken_main.txt",
     "OligoFormer main data directory candidate"),
]
for rel, dest, note in CANDS:
    P.fetch(f"{RAW}/{rel}", dest, "D5_huesken",
            accession="Huesken et al. 2005 Nat Biotechnol 23:995-1001",
            note=f"{note}; redistributed in the OligoFormer repository "
                 f"(github.com/lulab/OligoFormer)")
P.fetch("https://api.github.com/repos/lulab/OligoFormer/git/trees/main?recursive=1",
        "data/raw/oligoformer_tree.json", "D5_huesken",
        note="repository file listing at time of download, for reproducibility")

# per-gene tables: the target-gene assignment needed for the e8 split
tree = json.load(open(os.path.join(P.ROOT, "data/raw/oligoformer_tree.json")))
genes = [t["path"] for t in tree["tree"]
         if t["path"].startswith("Comparison methods/siRNAPred/siRNAPred/Hu/")
         and t["path"].endswith(".csv")]
for g in genes:
    name = g.split("/")[-1]
    P.fetch(f"{RAW}/{quote(g)}", f"data/raw/huesken_genes/{name}",
            "D5_huesken",
            note=f"Huesken siRNAs for target gene {name[:-4]}; used only for "
                 f"the no-shared-gene train/test split")
print("gene tables done:", len(genes))
