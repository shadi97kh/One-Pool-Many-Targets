"""
Positive extension B: approximation accuracy, gradients and measured runtime.

QUESTION. Can a saturable-bin background reduce forward and backward cost while
preserving the full-reference conservation solution and its gradients on
held-out constructs?

WHAT THE REFERENCE IS. The full retrieved competitor set of each construct.
That is a SITE-FILTERED universe of order a thousand transcripts, not the whole
transcriptome, and it is called the reference here for that reason.

METHODS, all sharing M, K, x and the same reference universe:
  1 full reference
  2 top-R truncation with the omitted competitors simply dropped
  3 top-R plus a linear affinity-weighted background, beta = sum_omitted x_j/K_j
  4 top-R plus saturable affinity-quantile bins,
    X_b = sum x_j, K_b = X_b / sum(x_j/K_j), background_b(f) = X_b f/(K_b+f)

Retrieval order is by x/K, the project's existing rule, which is
response-independent. Bin membership is piecewise constant and no gradient is
claimed through a sorting boundary.

GRADIENTS. f is solved by bisection without gradient, then reattached by the
implicit function theorem using the algebraic identity

    f = f* - F(f*, theta) / (dF/df)|_{f*}

whose value is f* because F(f*)=0 to solver precision, and whose derivative is
the correct -(dF/dtheta)/(dF/df). Autograd then flows through X_b and K_b,
which do depend on the inputs.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np                                            # noqa: E402
import pandas as pd                                           # noqa: E402
import torch                                                  # noqa: E402
torch.set_num_threads(1)
from riscpool import features, runner                         # noqa: E402
from riscpool.background import bin_edges                     # noqa: E402
from riscpool.provenance import DATA, ROOT                    # noqa: E402

OUT = os.path.join(ROOT, "results", "positive_extensions")
RHOS = [0.001, 0.01, 0.1, 0.5, 1.0, 10.0]
RS = [25, 50, 100, 200, 500]
BS = [1, 5, 10, 25, 50, 100, 200]
TOL_OCC, TOL_GRAD = 0.01, 0.01
NEAR_ZERO = 1e-12
WARMUP, REPS = 10, 50
DT = torch.float64


# ------------------------------------------------------------- the solver --
def solve_f(K, x, M, Xb=None, Kb=None, iters=200):
    """Bisection for F(f)=0 on [0, M], no gradient."""
    with torch.no_grad():
        lo = torch.zeros((), dtype=DT)
        hi = M.clone().detach()
        for _ in range(iters):
            mid = 0.5 * (lo + hi)
            F = mid + (x * mid / (K + mid)).sum() - M
            if Xb is not None and Xb.numel():
                F = F + (Xb * mid / (Kb + mid)).sum()
            lo = torch.where(F < 0, mid, lo)
            hi = torch.where(F < 0, hi, mid)
        return 0.5 * (lo + hi)


def residual(f, K, x, M, Xb=None, Kb=None):
    F = f + (x * f / (K + f)).sum() - M
    if Xb is not None and Xb.numel():
        F = F + (Xb * f / (Kb + f)).sum()
    return F


def dF_df(f, K, x, Xb=None, Kb=None):
    D = 1.0 + (x * K / (K + f) ** 2).sum()
    if Xb is not None and Xb.numel():
        D = D + (Xb * Kb / (Kb + f) ** 2).sum()
    return D


def equilibrium(K, x, M, Xb=None, Kb=None):
    """f with correct gradients, by implicit differentiation at the root."""
    fstar = solve_f(K, x, M, Xb, Kb)
    F = residual(fstar, K, x, M, Xb, Kb)
    D = dF_df(fstar, K, x, Xb, Kb)
    return fstar - F / D.detach()


def bins_from(K_out, x_out, B):
    """Differentiable X_b, K_b with piecewise-constant membership."""
    if K_out.numel() == 0 or B < 1:
        return (torch.zeros(0, dtype=DT), torch.ones(0, dtype=DT),
                np.zeros(0, int))
    logK = np.log10(K_out.detach().numpy())
    e = bin_edges(logK, int(B), "quantile")
    who = np.clip(np.digitize(logK, e[1:-1]), 0, len(e) - 2)
    Xs, Ks = [], []
    for b in range(len(e) - 1):
        m = torch.tensor(who == b)
        if not bool(m.any()):
            continue                       # skip zero-mass bins
        X = x_out[m].sum()
        denom = (x_out[m] / K_out[m]).sum()
        Xs.append(X)
        Ks.append(X / denom)
    if not Xs:
        return (torch.zeros(0, dtype=DT), torch.ones(0, dtype=DT), who)
    return torch.stack(Xs), torch.stack(Ks), who


# --------------------------------------------------------------- the loss --
def loss_of(q_focal, q_retained):
    """FROZEN in run_spec.json before any B evaluation:
    L = q_focal + 0.5 * mean(q_retained)."""
    return q_focal + 0.5 * q_retained.mean()


def prepare(K, x, R, B, method, focal=0):
    """Everything that depends only on K, x, R, B and the method.

    Split out so that run_method and every timing path use ONE code path.
    Timing a separately written copy of this logic measures the copy, and the
    two drift. Returns the retained index set, the omitted index set, the
    retained system, the bin aggregates, and the position of the focal target
    inside the retained system.

    Retrieval order is by x/K, the project's existing response-independent
    rule. The focal target is forced into the retained set if the ordering
    would otherwise drop it, which is what keeps a focal prediction defined
    for every configuration. Membership is piecewise constant in the inputs.
    """
    n = K.numel()
    order = torch.argsort(-(x / K))
    keep = order[:R] if R < n else order
    kept = set(keep.tolist())
    if focal not in kept:
        keep = torch.cat([torch.tensor([focal]), keep])[:max(R, 1)]
        kept = set(keep.tolist())
    mask = torch.ones(n, dtype=torch.bool)
    mask[keep] = False
    out = mask.nonzero(as_tuple=True)[0]
    if method == "full":
        keep = torch.arange(n)
        out = torch.zeros(0, dtype=torch.long)
    Ki, xi = K[keep], x[keep]
    Xb = Kb = None
    if method == "linear" and out.numel():
        beta = (x[out] / K[out]).sum()
        Xb = (beta * 1e30).reshape(1)              # X_b/K_b -> beta, K_b huge
        Kb = torch.full((1,), 1e30, dtype=DT)
    elif method == "bins" and out.numel():
        Xb, Kb, _ = bins_from(K[out], x[out], B)
    fi = int((keep == focal).nonzero()[0, 0])
    return {"keep": keep, "out": out, "Ki": Ki, "xi": xi, "Xb": Xb, "Kb": Kb,
            "focal_pos": fi}


def run_method(K, x, M, R, B, method, focal=0, prep=None):
    """Returns (f, q_focal, q_retained, retained index, Xb, Kb, Ki, xi).

    prep lets a caller reuse an already-prepared system, which is what the
    cached-solve timing does. When it is None the preparation is done here,
    through the same prepare() the timing paths call.
    """
    p = prepare(K, x, R, B, method, focal) if prep is None else prep
    f = equilibrium(p["Ki"], p["xi"], M, p["Xb"], p["Kb"])
    q = f / (p["Ki"] + f)
    return (f, q[p["focal_pos"]], q, p["keep"], p["Xb"], p["Kb"],
            p["Ki"], p["xi"])


def full_system_defect(f_hat, K, x, M):
    """The ORIGINAL full-transcript conservation defect at an approximate f.

    F_full(f) = f + sum_j x_j f/(K_j+f) - M over EVERY transcript, with no
    bins and no background of any kind. Bins summarise transcripts that the
    full system already represents individually, so adding them here would
    count that mass twice. This is the quantity that says whether the
    approximate free pool actually satisfies the conservation law of the
    system being approximated, as opposed to the reduced system the method
    happens to solve exactly.
    """
    return f_hat + (x * f_hat / (K + f_hat)).sum() - M


# ---------------------------------------------------------------- systems --
def systems():
    """(K, x, focal) per construct, from both datasets. Computational inputs
    only; no response is read here."""
    from riscpool import calibration
    from riscpool.offtarget import load_candidates
    sc = calibration.build_scale(features.load_features())
    C, n_mrna = sc["K_scale_constant_C"], sc["mrna_molecules_per_cell"]
    cand = load_candidates()[["gene_symbol", "x_rel"]]
    xr = dict(zip(cand.gene_symbol, cand.x_rel))
    out = {}
    for tag, path in (("D1", features.FEAT),
                      ("D2", os.path.join(DATA, "features_emexp668.parquet"))):
        if not os.path.exists(path):
            continue
        df = pd.read_parquet(path)
        tx = features.transcript_level(df)
        tx = tx[np.isfinite(tx.K_transcript) & (tx.K_transcript > 0)]
        for con, g in tx.groupby("construct"):
            xs = np.array([xr.get(s, 0.0) for s in g.gene_symbol]) * n_mrna
            m = xs > 0
            if m.sum() < 60:
                continue
            K = torch.tensor(g.K_transcript.to_numpy()[m] * C, dtype=DT)
            x = torch.tensor(xs[m], dtype=DT)
            out[con] = (tag, K, x, int(torch.argmax(x / K).item()), n_mrna)
    return out


def grads(K, x, M, R, B, method, focal, loss_idx=None):
    """dL/dlogK, dL/dlogx, dL/dlogM for the frozen loss.

    loss_idx names the transcripts the retained-average term runs over. It
    MUST be the same set for the reference and for the approximation being
    compared against it: the full reference explicitly represents every
    transcript, so without this its loss would average over all N while the
    approximation averages over R, and the two gradients would belong to
    different functions. Comparing them then measures the difference between
    two losses rather than the error of an approximation.
    """
    K = K.clone().requires_grad_(True)
    x = x.clone().requires_grad_(True)
    M = M.clone().requires_grad_(True)
    _, qf, q, keep, _, _, _, _ = run_method(K, x, M, R, B, method, focal)
    if loss_idx is not None and q.numel() != loss_idx.numel():
        q = q[loss_idx]                 # full reference restricted to the set
    L = loss_of(qf, q)
    gK, gx, gM = torch.autograd.grad(L, [K, x, M], allow_unused=True)
    gK = torch.zeros_like(K) if gK is None else gK
    gx = torch.zeros_like(x) if gx is None else gx
    gM = torch.zeros_like(M) if gM is None else gM
    # chain to log-parameters; x==0 entries contribute nothing and are kept 0
    return (gK.detach() * K.detach(), gx.detach() * x.detach(),
            gM.detach() * M.detach(), float(L.detach()))


def timeit(fn_, warmup=WARMUP, reps=REPS):
    for _ in range(warmup):
        fn_()
    t = []
    for _ in range(reps):
        a = time.perf_counter()
        fn_()
        t.append(time.perf_counter() - a)
    t = np.array(t)
    return {"median_s": float(np.median(t)), "p90_s": float(np.percentile(t, 90)),
            "min_s": float(t.min()), "iqr_s": float(np.subtract(*np.percentile(t, [75, 25])))}


def _grid(seed=0):
    spec = json.load(open(os.path.join(OUT, "run_spec.json")))
    fam1 = spec["families"]["D1_construct_to_family"]
    fam2 = spec["families"]["D2_construct_to_family"]
    fam_of = {**fam1, **fam2}
    sysd = systems()

    # deterministic family split, balanced by dataset of origin
    by_ds = {}
    for con, (tag, *_r) in sysd.items():
        by_ds.setdefault(tag, set()).add(fam_of[con])
    dev, test = set(), set()
    for tag in sorted(by_ds):
        for i, f in enumerate(sorted(by_ds[tag])):
            (dev if i % 2 == 0 else test).add(f)

    # ---- full-reference implicit gradient vs central differences ---------
    con0 = sorted(sysd)[0]
    _, K0, x0, foc0, nm0 = sysd[con0]
    K0s, x0s = K0[:40].clone(), x0[:40].clone()
    M0 = torch.tensor(0.1 * float(x0s.sum()), dtype=DT)
    gK, gx, gM, _ = grads(K0s, x0s, M0, 10**9, 1, "full", 0)
    fd = []
    for j in range(0, 40, 8):
        h = 1e-6
        Kp = K0s.clone(); Kp[j] *= np.exp(h)
        Km = K0s.clone(); Km[j] *= np.exp(-h)
        def L_of(KK):
            f = equilibrium(KK, x0s, M0)
            q = f / (KK + f)
            return float(loss_of(q[0], q))
        fd.append({"coord": int(j), "analytic": float(gK[j]),
                   "central_difference": (L_of(Kp) - L_of(Km)) / (2 * h)})
    gcheck = {"per_coordinate": fd,
              "max_abs_rel_err": float(max(
                  abs(d["analytic"] - d["central_difference"]) /
                  max(abs(d["central_difference"]), 1e-30) for d in fd))}

    # ---- the full fixed grid --------------------------------------------
    rows = []
    for con, (tag, K, x, foc, nm) in sorted(sysd.items()):
        N = int(K.numel())
        for rho in RHOS:
            M = torch.tensor(rho * nm, dtype=DT)
            fF, qfF, qF, keepF, _, _, KF_, xF_ = run_method(
                K, x, M, 10**9, 1, "full", foc)
            resF = float(abs(residual(fF, KF_, xF_, M)))
            ref_g = {}
            for R in RS:
                exact = R >= N
                # the reference gradient of the SAME loss the approximation
                # at this depth optimises, i.e. averaged over the same
                # retained transcripts
                _, _, _, keepR, _, _, _, _ = run_method(
                    K, x, M, R, 1, "truncate", foc)
                ref_g[R] = grads(K, x, M, 10**9, 1, "full", foc,
                                 loss_idx=keepR)
                for method in ("truncate", "linear", "bins"):
                    for B in (BS if method == "bins" else [0]):
                        if method == "bins" and not exact:
                            n_out = N - min(R, N)
                            if B > n_out:
                                continue
                        f, qf, q, keep, Xb, Kb, Ki_, xi_ = run_method(
                            K, x, M, R, B, method, foc)
                        res = float(abs(residual(f, Ki_, xi_, M, Xb, Kb)))
                        qref = qF[keep]
                        occ_abs = float(abs(qf - qfF))
                        occ_rel = (occ_abs / float(abs(qfF))
                                   if abs(float(qfF)) > NEAR_ZERO else np.nan)
                        ret_abs = float(torch.max(torch.abs(q - qref)))
                        gKF, gxF, gMF, LF = ref_g[R]
                        gK2, gx2, gM2, L2 = grads(K, x, M, R, B, method, foc,
                                                  loss_idx=keep)
                        num = float(torch.linalg.norm(
                            torch.cat([(gK2 - gKF)[keep], (gx2 - gxF)[keep],
                                       (gM2 - gMF).reshape(1)])))
                        den = float(torch.linalg.norm(
                            torch.cat([gKF[keep], gxF[keep],
                                       gMF.reshape(1)])))
                        rows.append({
                            "construct": con, "dataset": tag,
                            "family": fam_of[con], "N_reference": N,
                            "rho": rho, "R": R, "B": B, "method": method,
                            "exact_no_truncation": bool(exact),
                            "n_explicit": int(keep.numel()),
                            "abs_residual": res,
                            "dimensionless_residual": res / max(float(M), 1.0),
                            "full_abs_residual": resF,
                            "focal_q_reference": float(qfF),
                            "focal_abs_err": occ_abs,
                            "focal_rel_err": occ_rel,
                            "retained_max_abs_q_err": ret_abs,
                            "grad_abs_err_l2": num,
                            "grad_rel_l2_err": (num / den if den > NEAR_ZERO
                                                else np.nan),
                            "loss_reference": LF, "loss_method": L2,
                        })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(OUT, "B_grid.csv"), index=False)
    return df, dev, test, gcheck, sysd, fam_of


def fn(seed=0):
    df, dev, test, gcheck, sysd, fam_of = _grid(seed)
    approx = df[~df.exact_no_truncation].copy()

    # ---- selection on DEVELOPMENT families only --------------------------
    d = approx[approx.family.isin(dev)]
    ok = d[(d.focal_rel_err <= TOL_OCC) & (d.grad_rel_l2_err <= TOL_GRAD)]
    # cheapest configuration that meets both tolerances everywhere it is
    # evaluated on development: fewest explicitly scored terms, then fewest
    # bins, then smallest R
    cfg_ok = []
    for (m, R, B), g in ok.groupby(["method", "R", "B"]):
        tot = d[(d.method == m) & (d.R == R) & (d.B == B)]
        if len(g) == len(tot) and len(tot):
            cfg_ok.append({"method": m, "R": int(R), "B": int(B),
                           "cost_terms": int(R + (B if m == "bins" else
                                                  (1 if m == "linear" else 0))),
                           "n_dev_cases": int(len(tot)),
                           "worst_dev_focal_rel_err": float(g.focal_rel_err.max()),
                           "worst_dev_grad_rel_err": float(g.grad_rel_l2_err.max())})
    cfg_ok.sort(key=lambda c: (c["cost_terms"], c["R"]))
    selected = cfg_ok[0] if cfg_ok else None

    # ---- evaluate the SELECTED configuration, unchanged, on TEST --------
    held = {}
    if selected:
        t = approx[(approx.family.isin(test)) & (approx.method == selected["method"]) &
                   (approx.R == selected["R"]) & (approx.B == selected["B"])]
        if len(t):
            held = {
                "n_cases": int(len(t)),
                "n_families": int(t.family.nunique()),
                "median_focal_rel_err": float(t.focal_rel_err.median()),
                "p90_focal_rel_err": float(t.focal_rel_err.quantile(0.9)),
                "worst_focal_rel_err": float(t.focal_rel_err.max()),
                "median_grad_rel_err": float(t.grad_rel_l2_err.median()),
                "p90_grad_rel_err": float(t.grad_rel_l2_err.quantile(0.9)),
                "worst_grad_rel_err": float(t.grad_rel_l2_err.max()),
                "worst_dimensionless_residual": float(t.dimensionless_residual.max()),
                "meets_both_tolerances_on_all_test_cases": bool(
                    (t.focal_rel_err.max() <= TOL_OCC) and
                    (t.grad_rel_l2_err.max() <= TOL_GRAD)),
            }

    # ---- measured runtime, identical device/dtype/threads ---------------
    con = max(sysd, key=lambda c: sysd[c][1].numel())
    tag, K, x, foc, nm = sysd[con]
    M = torch.tensor(0.1 * nm, dtype=DT)
    timing = {"construct": con, "N_reference": int(K.numel()),
              "threads": torch.get_num_threads(), "dtype": "float64",
              "device": "cpu", "torch": torch.__version__,
              "warmup": WARMUP, "repetitions": REPS,
              "note": "timing repetitions are not independent biological "
                      "samples"}
    timing["full_forward"] = timeit(lambda: run_method(K, x, M, 10**9, 1, "full", foc))
    timing["full_forward_backward"] = timeit(
        lambda: grads(K, x, M, 10**9, 1, "full", foc))
    if selected:
        R, B, meth = selected["R"], selected["B"], selected["method"]
        timing["selected_forward"] = timeit(lambda: run_method(K, x, M, R, B, meth, foc))
        timing["selected_forward_backward"] = timeit(
            lambda: grads(K, x, M, R, B, meth, foc))
        n_out = int(K.numel()) - R
        timing["setup_bin_construction"] = timeit(
            lambda: bins_from(K[-n_out:], x[-n_out:], B)) if n_out > 0 else None
        # AMORTISED: K and x are fixed across a dose sweep or an optimisation
        # loop, so the bins are built once and only the solve repeats. This is
        # the number that matters for repeated use; the figures above include
        # bin construction in every call and are the cold-start cost.
        ordr = torch.argsort(-(x / K))
        kp, ot = ordr[:R], ordr[R:]
        Xb_, Kb_, _ = bins_from(K[ot], x[ot], B)
        Ki_, xi_ = K[kp], x[kp]
        timing["selected_forward_amortised"] = timeit(
            lambda: equilibrium(Ki_, xi_, M, Xb_, Kb_))
        timing["full_forward_amortised"] = timeit(
            lambda: equilibrium(K, x, M))
        timing["amortised_forward_speedup"] = float(
            timing["full_forward_amortised"]["median_s"] /
            timing["selected_forward_amortised"]["median_s"])
        sp = (timing["full_forward_backward"]["median_s"] /
              timing["selected_forward_backward"]["median_s"])
        timing["speedup_forward_backward_median"] = float(sp)
        setup = (timing["setup_bin_construction"] or {}).get("median_s", 0.0)
        saved = (timing["full_forward_backward"]["median_s"] -
                 timing["selected_forward_backward"]["median_s"])
        timing["solves_to_amortise_setup"] = (
            float(setup / saved) if saved > 0 else None)

    with open(os.path.join(OUT, "B_selected_and_heldout.json"), "w") as fh:
        json.dump({"selected": selected, "held_out": held, "timing": timing},
                  fh, indent=1)

    frontier = (approx.groupby(["method", "R", "B"])
                .agg(focal_rel_err_p90=("focal_rel_err", lambda v: float(np.nanpercentile(v, 90))),
                     grad_rel_err_p90=("grad_rel_l2_err", lambda v: float(np.nanpercentile(v, 90))),
                     n=("focal_rel_err", "size")).reset_index())
    frontier.to_csv(os.path.join(OUT, "B_frontier.csv"), index=False)

    return {
        "WHAT_THIS_TESTS": (
            "whether a saturable-bin background reproduces the full-reference "
            "solution and its gradients cheaply enough to be worth using. It "
            "is a computational claim, not evidence about coupling or rho."),
        "reference_universe": (
            "the construct's full retrieved competitor set, a site-filtered "
            "universe of order a thousand transcripts. NOT the whole "
            "transcriptome."),
        "n_constructs": int(df.construct.nunique()),
        "n_families": int(df.family.nunique()),
        "development_families": sorted(dev), "test_families": sorted(test),
        "grid": {"rho": RHOS, "R": RS, "B": BS},
        "n_grid_rows": int(len(df)),
        "n_exact_cases_excluded_from_selection": int(df.exact_no_truncation.sum()),
        "tolerances": {"focal_rel_occupancy": TOL_OCC,
                       "grad_rel_l2": TOL_GRAD,
                       "near_zero_abs": NEAR_ZERO,
                       "note": "engineering targets, not biological efficacy "
                               "thresholds"},
        "full_reference_gradient_check": gcheck,
        "selected_on_development": selected,
        "held_out_result": held,
        "timing": timing,
        "worst_full_reference_dimensionless_residual": float(
            (df.full_abs_residual / df.rho.map(lambda r: max(r * 1.0, 1.0))).max()),
        "frontier_path": "results/positive_extensions/B_frontier.csv",
        "grid_path": "results/positive_extensions/B_grid.csv",
    }


if __name__ == "__main__":
    runner.run("pxb_approximation_cost", fn, seed=0)
