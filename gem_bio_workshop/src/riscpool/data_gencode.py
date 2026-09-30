"""
D3: GENCODE human transcriptome. 3'UTR and CDS extraction.

GENCODE's pc_transcripts FASTA carries the UTR5/CDS/UTR3 coordinate blocks in
the header, so the segmentation is GENCODE's own, not ours:

  >ENST|ENSG|OTTHUMG|OTTHUMT|tx_name|gene_symbol|length|UTR5:a-b|CDS:c-d|UTR3:e-f|

Seed-mediated off-targeting is predominantly but not exclusively 3'UTR, so CDS
is extracted alongside and both are searchable downstream.

Release version is read from the file name recorded in data/PROVENANCE.json,
never hard-coded in an analysis script.
"""

import gzip
import os
import re

import pandas as pd

from .provenance import DATA

RELEASE = "50"
FASTA = os.path.join(DATA, "raw", f"gencode.v{RELEASE}.pc_transcripts.fa.gz")
GTF = os.path.join(DATA, "raw", f"gencode.v{RELEASE}.annotation.gtf.gz")
TX_PARQUET = os.path.join(DATA, "gencode_transcripts.parquet")

_BLOCK = re.compile(r"^(UTR5|CDS|UTR3):(\d+)-(\d+)$")


def _iter_fasta(path):
    name, chunks = None, []
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith(">"):
                if name is not None:
                    yield name, "".join(chunks)
                name, chunks = line[1:].strip(), []
            else:
                chunks.append(line.strip())
    if name is not None:
        yield name, "".join(chunks)


def build_transcripts(fasta=FASTA, out=TX_PARQUET):
    rows = []
    for header, seq in _iter_fasta(fasta):
        f = header.split("|")
        if len(f) < 7:
            continue
        rec = {"transcript_id": f[0], "gene_id": f[1],
               "transcript_name": f[4], "gene_symbol": f[5],
               "tx_len": int(f[6])}
        blocks = {}
        for tok in f[7:]:
            m = _BLOCK.match(tok)
            if m:
                blocks[m.group(1)] = (int(m.group(2)), int(m.group(3)))
        for key, tag in (("UTR5", "utr5"), ("CDS", "cds"), ("UTR3", "utr3")):
            if key in blocks:
                a, b = blocks[key]
                rec[f"{tag}_start"], rec[f"{tag}_end"] = a, b
                rec[f"{tag}_seq"] = seq[a - 1:b]
            else:
                rec[f"{tag}_start"] = rec[f"{tag}_end"] = 0
                rec[f"{tag}_seq"] = ""
        rec["utr3_len"] = len(rec["utr3_seq"])
        rec["cds_len"] = len(rec["cds_seq"])
        rows.append(rec)
    df = pd.DataFrame(rows)
    df.to_parquet(out, index=False, compression="zstd")
    return df


def build_gtf_tags(gtf=GTF, out=os.path.join(DATA, "gencode_tx_tags.parquet")):
    """MANE_Select / Ensembl_canonical flags, so 'one transcript per gene' is
    GENCODE's designation rather than an arbitrary pick of ours."""
    rows = []
    with gzip.open(gtf, "rt") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            p = line.split("\t")
            if len(p) < 9 or p[2] != "transcript":
                continue
            a = p[8]
            def g(k):
                m = re.search(rf'{k} "([^"]+)"', a)
                return m.group(1) if m else ""
            tags = re.findall(r'tag "([^"]+)"', a)
            rows.append({
                "transcript_id": g("transcript_id"),
                "gene_id": g("gene_id"),
                "gene_symbol": g("gene_name"),
                "transcript_type": g("transcript_type"),
                "gene_type": g("gene_type"),
                "level": g("level"),
                "tsl": g("transcript_support_level"),
                "mane_select": "MANE_Select" in tags,
                "ensembl_canonical": "Ensembl_canonical" in tags,
                "basic": "basic" in tags,
            })
    df = pd.DataFrame(rows)
    df.to_parquet(out, index=False, compression="zstd")
    return df


def load_transcripts():
    return pd.read_parquet(TX_PARQUET)


def load_tags():
    return pd.read_parquet(os.path.join(DATA, "gencode_tx_tags.parquet"))


def canonical_by_symbol(min_utr3=1):
    """
    One representative transcript per gene symbol: MANE Select where GENCODE
    defines one, else Ensembl canonical, else the longest 3'UTR. Returns a
    DataFrame with sequences attached.
    """
    tx = load_transcripts()
    tags = load_tags()[["transcript_id", "mane_select", "ensembl_canonical",
                        "transcript_type", "gene_type", "tsl", "level"]]
    df = tx.merge(tags, on="transcript_id", how="left")
    df["mane_select"] = df["mane_select"].fillna(False)
    df["ensembl_canonical"] = df["ensembl_canonical"].fillna(False)
    df = df[df.utr3_len >= min_utr3].copy()
    df["rank"] = (df.mane_select.astype(int) * 2
                  + df.ensembl_canonical.astype(int))
    df = df.sort_values(["gene_symbol", "rank", "utr3_len"],
                        ascending=[True, False, False])
    out = df.groupby("gene_symbol", as_index=False).first()
    return out
