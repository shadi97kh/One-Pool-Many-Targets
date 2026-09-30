"""Reference mRNAs for the three transfection target genes.

These are the exact accessions the GSE5814 array designs themselves list for
MAPK14, PLK1 and PIK3CB (read out of the GPL2029/GPL3991/GPL3992 platform
tables, not chosen by us). They anchor the positional siRNA naming used by the
submitters (e.g. "MAPK14-193").
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import provenance as P  # noqa: E402

E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
ACC = {"NM_001315": "MAPK14", "NM_005030": "PLK1", "NM_006219": "PIK3CB",
       "NM_139013": "MAPK14_alt"}
for acc, gene in ACC.items():
    P.fetch(f"{E}?db=nuccore&id={acc}&rettype=fasta&retmode=text",
            f"data/raw/refseq_{acc}.fasta", "D1_refseq_targets",
            accession=acc,
            note=f"RefSeq mRNA for {gene}; accession taken from the GSE5814 "
                 f"platform annotation table")
