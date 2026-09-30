"""
Binned background for truncated retrieval (e4b).

e4 showed that the linearised background (1 + beta) f fails at shallow
retrieval depth. The linearisation replaces

    X_bg f / (K_bg + f)   by   (X_bg / K_bg) f

which is the first term of the expansion in f / K_bg, so it is accurate only
where K_bg >> f. At R = 25 the omitted set is not the weak-binding tail at
all: ordering by x/K does not guarantee that the transcripts left out have
large K, and e4 measured that the assumption held in only a handful of rows.

The fix here keeps a Michaelis form for the omitted mass but does not pretend
to resolve it transcript by transcript. Omitted transcripts are partitioned
into B bins by log K, and each bin contributes one saturable term:

    F(f) = f + sum_{j in R} x_j f/(K_j+f) + sum_b X_b f/(K_b+f) - M

with

    X_b = sum_{j in b} x_j                    the bin's abundance mass
    K_b = X_b / sum_{j in b} x_j / K_j        abundance-weighted harmonic mean

The harmonic mean is the right summary, not the arithmetic one. In the weak
limit each transcript contributes (x_j/K_j) f, so the bin contributes
(sum_j x_j/K_j) f, and X_b/K_b reproduces exactly that sum by construction.
The binned form is therefore exact in the weak limit for any binning, and
becomes exact everywhere as the bins narrow. B = 1 collapsed to its own weak
limit is the linear rule of e4, which is what makes that case a regression
check rather than a new number.

Nothing in this module changes the equilibrium solver. A bin is algebraically
indistinguishable from a retained transcript with abundance X_b and affinity
K_b, so the existing solver is called with the bins appended to the retained
vectors and beta = 0. That keeps every result already recorded in results/
untouched.
"""

import numpy as np
import torch

from .equilibrium import risc_equilibrium


def harmonic_bin_summary(K, x):
    """(X_b, K_b) for one bin: abundance mass and abundance-weighted harmonic
    mean affinity. Returns (0.0, nan) for an empty or zero-mass bin."""
    K = np.asarray(K, dtype=np.float64)
    x = np.asarray(x, dtype=np.float64)
    X = float(x.sum())
    if X <= 0 or K.size == 0:
        return 0.0, float("nan")
    denom = float((x / K).sum())
    if denom <= 0:
        return X, float("inf")
    return X, X / denom


def bin_edges(logK, B, rule="quantile"):
    """B+1 edges over log10 K. Quantile bins put equal transcript counts in
    each bin; equal-width bins cut the log K range evenly. Both are reported
    because the choice is ours, not the data's."""
    lo, hi = float(logK.min()), float(logK.max())
    if B <= 1 or lo == hi:
        return np.array([lo - 1e-9, hi + 1e-9])
    if rule == "equal_width":
        e = np.linspace(lo, hi, B + 1)
    elif rule == "quantile":
        e = np.quantile(logK, np.linspace(0.0, 1.0, B + 1))
    else:
        raise ValueError(f"unknown binning rule {rule!r}")
    e = np.asarray(e, dtype=np.float64).copy()
    e[0] -= 1e-9
    e[-1] += 1e-9
    return e


def bin_omitted(K_out, x_out, B, rule="quantile"):
    """
    Partition the omitted transcripts into at most B bins by log K.

    Returns (X_bins, K_bins, detail). Empty bins are dropped and the number
    actually used is reported, so a quantile binning that collapses because
    of ties cannot silently pretend to a resolution it does not have.
    """
    K_out = np.asarray(K_out, dtype=np.float64)
    x_out = np.asarray(x_out, dtype=np.float64)
    if K_out.size == 0:
        return (np.zeros(0), np.zeros(0),
                {"n_bins_requested": int(B), "n_bins_used": 0,
                 "n_omitted": 0, "edges_log10K": []})
    logK = np.log10(K_out)
    edges = bin_edges(logK, B, rule)
    which = np.clip(np.digitize(logK, edges[1:-1]), 0, len(edges) - 2)
    X, Kb, members = [], [], []
    for b in range(len(edges) - 1):
        m = which == b
        if not m.any():
            continue
        Xb, Kbb = harmonic_bin_summary(K_out[m], x_out[m])
        if Xb <= 0 or not np.isfinite(Kbb):
            continue
        X.append(Xb)
        Kb.append(Kbb)
        members.append(int(m.sum()))
    detail = {
        "n_bins_requested": int(B),
        "n_bins_used": len(X),
        "n_omitted": int(K_out.size),
        "binning_rule": rule,
        "edges_log10K": [float(e) for e in edges],
        "bin_n_transcripts": members,
        "bin_abundance_mass": [float(v) for v in X],
        "bin_K_harmonic": [float(v) for v in Kb],
        "omitted_log10K_min": float(logK.min()),
        "omitted_log10K_max": float(logK.max()),
    }
    return np.asarray(X), np.asarray(Kb), detail


def solve_binned(K_in, x_in, X_bins, K_bins, M):
    """
    Solve the conservation equation with the retained transcripts scored
    individually and the omitted mass carried by saturable bins.

    A bin enters exactly as a transcript does, so this calls the same solver
    that every other experiment in the repository calls. Returns
    (f, o_retained, o_bins).
    """
    K_all = np.concatenate([np.asarray(K_in, dtype=np.float64),
                            np.asarray(K_bins, dtype=np.float64)])
    x_all = np.concatenate([np.asarray(x_in, dtype=np.float64),
                            np.asarray(X_bins, dtype=np.float64)])
    Kt = torch.tensor(K_all, dtype=torch.float64)[None, :]
    xt = torch.tensor(x_all, dtype=torch.float64)[None, :]
    Mt = torch.tensor([[float(M)]], dtype=torch.float64)
    bt = torch.zeros_like(Mt)
    f, o = risc_equilibrium(Kt, xt, Mt, bt)
    o = o[0].numpy()
    n = len(K_in)
    return float(f.item()), o[:n], o[n:]


def solve_linear(K_in, x_in, beta, M):
    """The e4 rule: the omitted mass collapsed to a single linear term.
    Kept here so the regression check runs through this module rather than
    through a copy of the e4 code."""
    Kt = torch.tensor(np.asarray(K_in, dtype=np.float64),
                      dtype=torch.float64)[None, :]
    xt = torch.tensor(np.asarray(x_in, dtype=np.float64),
                      dtype=torch.float64)[None, :]
    Mt = torch.tensor([[float(M)]], dtype=torch.float64)
    bt = torch.tensor([[float(beta)]], dtype=torch.float64)
    f, o = risc_equilibrium(Kt, xt, Mt, bt)
    return float(f.item()), o[0].numpy()


def dF_df(f, K, x, X_bins=None, K_bins=None, beta=0.0):
    """
    Jacobian of the conservation equation, extended for bins.

        dF/df = (1 + beta) + sum_j x_j K_j/(K_j+f)^2 + sum_b X_b K_b/(K_b+f)^2

    The bin term has the same form as a transcript term, which is the whole
    point: no new gradient machinery is needed and the implicit-function
    gradients of equilibrium.py extend unchanged.
    """
    K = np.asarray(K, dtype=np.float64)
    x = np.asarray(x, dtype=np.float64)
    d = (1.0 + float(beta)) + float((x * K / (K + f) ** 2).sum())
    if X_bins is not None and len(X_bins):
        Xb = np.asarray(X_bins, dtype=np.float64)
        Kb = np.asarray(K_bins, dtype=np.float64)
        d += float((Xb * Kb / (Kb + f) ** 2).sum())
    return d
