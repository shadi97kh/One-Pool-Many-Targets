"""
Differentiable shared-resource RISC equilibrium layer.

    F(f) = (1 + beta) f + sum_{j in R} x_j f / (K_j + f) - M = 0

M     total RISC pool loaded with the candidate guide. We model competition
      among transcripts for complexes ALREADY loaded with that guide. Guide
      loading competition and endogenous miRNA occupancy are out of scope and
      enter only through the value of M.
f     free (unbound) loaded RISC
R     explicitly retrieved and individually scored transcripts
x_j   abundance
K_j   learned effective interaction parameter, positive. Not a measured
      binding constant.
beta  linearised background standing in for everything outside R.

Why the background is linear rather than X_bg f/(K_bg + f): the omitted set is
by construction the weak-binding tail, K_bg >> f, where

    X_bg f / (K_bg + f) = (X_bg / K_bg) f + O(f^2 / K_bg^2).

So only the ratio beta = X_bg / K_bg is identifiable, and pretending to fit
X_bg and K_bg separately invites a reviewer to point out the degeneracy. The
one identified parameter also has an exact calibration rule (see retrieval
invariance in theory.py): beta = sum_{j not in R} x_j / K_j. Note this is
affinity weighted. Calibrating from residual abundance mass alone is wrong,
because two transcripts of equal abundance and different affinity do not
contribute equally to the resource budget.

Uniqueness: F(0) = -M < 0, dF/df > 0 everywhere, F(M) >= 0. Unique root
bracketed by [0, M], so bisection is globally convergent and batches cleanly.

Gradients by implicit function theorem, df/dtheta = -(dF/dtheta)/(dF/df):
    D       = dF/df   = (1 + beta) + sum_j x_j K_j / (K_j + f)^2  > 0
    df/dK_j =  x_j f / [(K_j + f)^2 D]
    df/dx_j = -f / [(K_j + f) D]
    df/dM   =  1 / D
    df/dbeta = -f / D
"""

import torch

_SOLVE_DTYPE = torch.float64   # K spans decades once parameterised as exp(-.)


def _residual(f, K, x, M, beta):
    return (1.0 + beta) * f + (x * f / (K + f)).sum(-1, keepdim=True) - M


def _dresidual(f, K, x, beta):
    return (1.0 + beta) + (x * K / (K + f) ** 2).sum(-1, keepdim=True)


def solve_free_pool(K, x, M, beta, iters=90):
    lo, hi = torch.zeros_like(M), M.clone()
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        neg = _residual(mid, K, x, M, beta) < 0
        lo = torch.where(neg, mid, lo)
        hi = torch.where(neg, hi, mid)
    return 0.5 * (lo + hi)


class _FreePool(torch.autograd.Function):
    @staticmethod
    def forward(ctx, K, x, M, beta):
        with torch.no_grad():
            f = solve_free_pool(K, x, M, beta)
        ctx.save_for_backward(f, K, x, beta)
        return f

    @staticmethod
    def backward(ctx, grad_f):
        f, K, x, beta = ctx.saved_tensors
        g = grad_f / _dresidual(f, K, x, beta)
        return (g * (x * f / (K + f) ** 2),
                -g * (f / (K + f)),
                g.clone(),
                -g * f)


def risc_equilibrium(K, x, M, beta=None):
    """Returns f (B,1) and per-transcript occupancy o (B,N)."""
    dt = K.dtype
    Kd, xd, Md = K.to(_SOLVE_DTYPE), x.to(_SOLVE_DTYPE), M.to(_SOLVE_DTYPE)
    b = (torch.zeros_like(Md) if beta is None else beta.to(_SOLVE_DTYPE))
    f = _FreePool.apply(Kd, xd, Md, b)
    o = xd * f / (Kd + f)          # picks up implicit and direct paths
    return f.to(dt), o.to(dt)


def equilibrium_residual(K, x, M, f, beta=None):
    b = torch.zeros_like(M) if beta is None else beta
    return _residual(f.to(_SOLVE_DTYPE), K.to(_SOLVE_DTYPE), x.to(_SOLVE_DTYPE),
                     M.to(_SOLVE_DTYPE), b.to(_SOLVE_DTYPE))


def pairwise_occupancy(K, x, M):
    """
    Independent pairwise counterfactual: every transcript sees the whole pool,
    nothing couples them. Same functional form as the equilibrium expression
    with f pinned to M, which is what isolates the coupling as the only
    difference. This does NOT claim existing predictors emit occupancies.
    """
    return x * M / (K + M)


def pairwise_score(K, x):
    """M-free affinity-weighted-abundance score, the 'pairwise + expression'
    ablation. Proportional to the weak-binding limit of occupancy."""
    return x / K
