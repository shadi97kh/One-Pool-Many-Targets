"""
Local target-site accessibility on the real 3'UTR sequences.

RNA.pfl_fold on a sliding window, not a whole-transcript partition function:
the latter is O(n^3) and would not finish on 21.5 Mb of UTR. pfl_fold_up
returns, for every position i, the probability that the k nucleotides ending
at i are simultaneously unpaired. Two stretch lengths are kept, k = 8 (the
seed match itself) and k = 15 (the seed match plus flank), because the opening
cost that matters is for the whole footprint, not a single base.

Window parameters are the ViennaRNA defaults for local folding, W = 80,
L = 40, recorded in the output so a rerun cannot silently use different ones.
"""

import os

import numpy as np

from .provenance import DATA

OUT = os.path.join(DATA, "accessibility_u8_u15.npz")
W, L, U = 80, 40, 15
KEEP = (8, 15)


def _one(seq):
    import RNA
    up = RNA.pfl_fold_up(seq, U, W, L)
    n = len(seq)
    out = np.zeros((len(KEEP), n), dtype=np.float32)
    for r, k in enumerate(KEEP):
        for i in range(1, n + 1):
            row = up[i]
            out[r, i - 1] = row[k] if k < len(row) else 0.0
    return out


def _worker(args):
    tid, seq = args
    try:
        return tid, _one(seq)
    except Exception as exc:                # record it, do not substitute
        return tid, None if False else ("ERROR", f"{type(exc).__name__}: {exc}")


def build(out=OUT, nproc=None):
    from multiprocessing import Pool
    from .offtarget import load_candidates
    cand = load_candidates()
    items = list(zip(cand.transcript_id.tolist(), cand.utr3_seq.tolist()))
    nproc = nproc or max(1, (os.cpu_count() or 4) - 2)
    res = {}
    errors = {}
    with Pool(nproc) as p:
        for tid, val in p.imap_unordered(_worker, items, chunksize=16):
            if isinstance(val, tuple):
                errors[tid] = val[1]
            else:
                res[tid] = val
    ids = [t for t in cand.transcript_id if t in res]
    lens = np.array([res[t].shape[1] for t in ids], dtype=np.int64)
    off = np.concatenate([[0], np.cumsum(lens)])
    flat = np.concatenate([res[t] for t in ids], axis=1)
    np.savez_compressed(out, ids=np.array(ids), offsets=off,
                        acc=flat, keep=np.array(KEEP),
                        params=np.array([W, L, U]))
    return {"n_transcripts": len(ids), "n_errors": len(errors),
            "errors": errors, "total_positions": int(lens.sum()),
            "pfl_fold_W": W, "pfl_fold_L": L, "pfl_fold_u_max": U,
            "stretch_lengths_kept": list(KEEP), "path": out}


class Accessibility:
    def __init__(self, path=OUT):
        z = np.load(path, allow_pickle=False)
        self.ids = list(z["ids"])
        self.off = z["offsets"]
        self.acc = z["acc"]
        self.keep = list(z["keep"])
        self.index = {t: i for i, t in enumerate(self.ids)}

    def get(self, tid, k=15):
        i = self.index.get(tid)
        if i is None:
            return None
        r = self.keep.index(k)
        return self.acc[r, self.off[i]:self.off[i + 1]]
