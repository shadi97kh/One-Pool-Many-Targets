"""D1 (GSE5814) and D3 (GENCODE human) acquisition. Provenance-recorded."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import provenance as P  # noqa: E402

GEO = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814"
GENCODE_REL = "50"
GC = ("https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/"
      f"release_{GENCODE_REL}")

print("### D1  GSE5814 (Jackson et al. off-target microarrays)")
P.fetch(f"{GEO}/soft/GSE5814_family.soft.gz",
        "data/raw/GSE5814_family.soft.gz", "D1_GSE5814",
        accession="GSE5814",
        note="SOFT family file: platform probe annotation + all GSM sample "
             "data tables (channel intensities and log ratios)")
for gpl in ("GPL2029", "GPL3991", "GPL3992"):
    P.fetch(f"{GEO}/matrix/GSE5814-{gpl}_series_matrix.txt.gz",
            f"data/raw/GSE5814-{gpl}_series_matrix.txt.gz", "D1_GSE5814",
            accession="GSE5814", note=f"series matrix for platform {gpl}")
P.fetch(f"{GEO}/suppl/filelist.txt", "data/raw/GSE5814_filelist.txt",
        "D1_GSE5814", accession="GSE5814", note="supplementary file listing")

print("\n### D3  GENCODE human transcriptome")
P.fetch(f"{GC}/_README.TXT", "data/raw/gencode_README.TXT", "D3_GENCODE",
        version=f"GENCODE release {GENCODE_REL}", note="release readme")
P.fetch(f"{GC}/MD5SUMS", "data/raw/gencode_MD5SUMS.txt", "D3_GENCODE",
        version=f"GENCODE release {GENCODE_REL}",
        note="upstream md5 checksums")
P.fetch(f"{GC}/gencode.v{GENCODE_REL}.pc_transcripts.fa.gz",
        f"data/raw/gencode.v{GENCODE_REL}.pc_transcripts.fa.gz", "D3_GENCODE",
        version=f"GENCODE release {GENCODE_REL}",
        note="protein-coding transcript sequences; FASTA headers carry "
             "UTR5/CDS/UTR3 coordinate blocks and the HGNC gene symbol")
P.fetch(f"{GC}/gencode.v{GENCODE_REL}.annotation.gtf.gz",
        f"data/raw/gencode.v{GENCODE_REL}.annotation.gtf.gz", "D3_GENCODE",
        version=f"GENCODE release {GENCODE_REL}",
        note="full annotation GTF; transcript<->gene<->symbol mapping, "
             "transcript support level, tags")
print("\n### downloads finished")
