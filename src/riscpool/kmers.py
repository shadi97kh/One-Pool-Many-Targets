"""
k-mer incidence over real 3'UTR sequences, and data-driven seed recovery.

Why this module exists. The GSE5814 submitters did not deposit the siRNA
sequences, and the publisher does not release the paper's full text or
supplementary tables for machine reading. Rather than invent the sequences,
the seed of each construct is RECOVERED FROM THE MEASURED RESPONSE: for every
7-mer, compare the measured log ratio of transcripts whose 3'UTR contains that
7-mer against those that do not. The 7-mer whose presence is most strongly
associated with repression is the site complementary to guide positions 2-8.

This is a measurement, not an assumption, and it is falsifiable: if no 7-mer
separates from the null the recovery has failed and is reported as failed.
It also reproduces the central claim of Jackson et al. 2006 as a positive
control before anything is built on top of it.
"""

import numpy as np
import scipy.sparse as sp

ALPHA = "ACGT"
_CODE = np.full(256, 255, dtype=np.uint8)
for _i, _c in enumerate(ALPHA):
    _CODE[ord(_c)] = _i
    _CODE[ord(_c.lower())] = _i
_COMP = {"A": "T", "C": "G", "G": "C", "T": "A", "U": "A", "N": "N"}


def revcomp(s):
    return "".join(_COMP.get(c, "N") for c in reversed(s.upper()))


def to_rna(s):
    return s.upper().replace("T", "U")


def kmer_index(s):
    """Integer code for one k-mer string; None if it contains an ambiguity."""
    v = _CODE[np.frombuffer(s.encode(), dtype=np.uint8)]
    if (v == 255).any():
        return None
    idx = 0
    for d in v:
        idx = idx * 4 + int(d)
    return idx


def index_to_kmer(idx, k):
    out = []
    for _ in range(k):
        out.append(ALPHA[idx & 3])
        idx >>= 2
    return "".join(reversed(out))


def seq_kmer_codes(seq, k):
    """All valid k-mer codes in seq, in order, as an int64 array."""
    v = _CODE[np.frombuffer(seq.encode(), dtype=np.uint8)].astype(np.int64)
    n = v.size - k + 1
    if n <= 0:
        return np.empty(0, dtype=np.int64)
    win = np.lib.stride_tricks.sliding_window_view(v, k)
    bad = (win == 255).any(axis=1)
    pw = (4 ** np.arange(k - 1, -1, -1)).astype(np.int64)
    codes = win @ pw
    return codes[~bad]


def incidence(seqs, k=7, counts=False):
    """
    Sparse (n_seq, 4**k) matrix. Entry is 1 (or the occurrence count) if the
    k-mer occurs in that sequence.
    """
    rows, cols, vals = [], [], []
    for i, s in enumerate(seqs):
        c = seq_kmer_codes(s, k)
        if c.size == 0:
            continue
        u, n = np.unique(c, return_counts=True)
        rows.append(np.full(u.size, i, dtype=np.int32))
        cols.append(u.astype(np.int32))
        vals.append(n.astype(np.float32) if counts
                    else np.ones(u.size, dtype=np.float32))
    if not rows:
        return sp.csr_matrix((len(seqs), 4 ** k), dtype=np.float32)
    return sp.csr_matrix(
        (np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
        shape=(len(seqs), 4 ** k), dtype=np.float32)


def enrichment_scan(G, y, min_n=30):
    """
    For every k-mer column of G (binary incidence) return the difference in
    mean(y) between sequences carrying it and those not, plus a Welch t
    statistic. Vectorised: no per-k-mer Python loop.
    """
    y = np.asarray(y, dtype=np.float64)
    N = y.size
    n1 = np.asarray(G.sum(axis=0)).ravel()
    s1 = G.T @ y
    s2 = G.T @ (y ** 2)
    tot1, tot2 = y.sum(), (y ** 2).sum()
    n0 = N - n1
    with np.errstate(invalid="ignore", divide="ignore"):
        m1 = s1 / n1
        m0 = (tot1 - s1) / n0
        v1 = np.maximum(s2 / n1 - m1 ** 2, 0) * n1 / np.maximum(n1 - 1, 1)
        v0 = np.maximum((tot2 - s2) / n0 - m0 ** 2, 0) * n0 / np.maximum(n0 - 1, 1)
        se = np.sqrt(v1 / np.maximum(n1, 1) + v0 / np.maximum(n0, 1))
        t = (m1 - m0) / se
    ok = (n1 >= min_n) & (n0 >= min_n)
    delta = np.where(ok, m1 - m0, np.nan)
    t = np.where(ok, t, np.nan)
    return delta, t, n1
