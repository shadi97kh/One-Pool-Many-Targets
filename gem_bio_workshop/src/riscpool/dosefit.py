"""
Fitting one effective free pool per dose, and inverting it for rho.

THE TEST. Proposition 3 blocks any rank statistic taken at a fixed dose
within one construct. It does not block a statement about how the same
construct behaves across doses, because dose changes the pool:

  independent scoring   the effective pool is M_d, exactly proportional to
                        dose, so log(pool) against log(dose) has slope 1
  equilibrium           f_d solves (1+beta) f + sum_j x_j f/(K_j+f) = M_d.
                        M is concave in f, so f is CONVEX in M, and with
                        f(0) = 0 this forces d log f / d log M >= 1. The
                        slope is at or ABOVE 1, never below it.

The direction is worth stating twice because the intuition runs the other
way: added complex is absorbed by targets, so one expects the free pool to
lag. It does lag in LEVEL, and the bounds are

    M / (1 + beta + sum_j x_j/K_j)  <=  f(M)  <=  M / (1 + beta),

the lower bound from f/(K_j+f) <= f/K_j and the upper from the occupancy
terms being nonnegative. But the buffering capacity saturates, so each added
unit is absorbed less than the last and the EXPONENT is at least 1. A level
below a line through the origin and an exponent below 1 are different
statements and only the first is true.

So the experiment is: hold K_j fixed at the feature-derived values, fit one
scalar pool per dose, and look at the exponent. A slope of 1 does not
discriminate, a slope above 1 is evidence of competition, and a slope below 1
is predicted by neither model as formulated and indicates that some premise
has failed, most plausibly the assumed proportionality of M to dose.

WHAT THE EXPONENT TEST ASSUMES. That the intracellular guide-specific loaded
pool M is proportional to the administered guide dose. This is an assumption,
not a property of the design. Holding total transfected duplex constant with
non-targeting control makes it more plausible, but it does not establish
proportional uptake, strand selection, Argonaute loading, displacement or
recycling. Inverting the fitted pools through conservation gives an implied
M per dose whose own log-log slope is a direct check on it.

THE MODEL. For construct s, dose d and transcript j,

    y_{d,j} = a_d - c_s * b_j(p_d) + eps,     b_j(p) = p / (K_j + p)

y is the measured log2 fold change against the zero-dose arrays, a_d is a
per-dose intercept, and c_s is the log2 repression produced by a fully
occupied transcript.

WHY c IS SHARED ACROSS DOSES, and why that is the whole identifying
assumption. c_s is the efficacy of a bound complex. It is a property of the
guide and of the silencing machinery, not of how much siRNA was pipetted
onto the cells, so it cannot depend on dose. Everything dose-dependent is
carried by p_d. If c were free per dose, the model would have a per-dose
amplitude and a per-dose pool and nothing would be identified at all.

WHAT IS AND IS NOT IDENTIFIED. In the weak-binding limit K_j >> p_d,
b_j -> p_d / K_j and the fit sees only the product c_s * p_d. The absolute
pool is then not identified; only its dose scaling is, because c_s is
constant and log(c_s p_d) and log(p_d) differ by a constant. That is a
convenient asymmetry and it is stated here rather than discovered later:

  * the SLOPE of log pool against log dose is identified even in the fully
    degenerate limit;
  * the ABSOLUTE pool, and therefore rho, is identified only through
    curvature, i.e. only to the extent that some sites actually saturate.

So a tight slope with a wide rho is the expected outcome, not a failure.

FITTING. Given the pool vector, a_d and c_s are linear, so they are profiled
out in closed form: centre y and b within each dose, then c_s is a single
regression coefficient pooled over doses. Only log p_d is optimised
numerically. Errors are taken homoscedastic within a construct; the per-dose
residual spread is reported separately as a diagnostic rather than being
modelled, because with three doses a per-dose variance is barely estimable.
"""

import numpy as np
from scipy import optimize


def bound_fraction(K, p):
    return p / (K + p)


def _profile(y_by_dose, b_by_dose):
    """
    Closed-form intercepts and shared amplitude given the pool vector.

    Centring y and b within each dose removes a_d exactly. What remains is a
    single-coefficient regression through the origin pooled over doses, so

        c = - sum_d <y~_d, b~_d> / sum_d <b~_d, b~_d>

    with the minus sign because repression is negative. Returns (c, rss, n).
    """
    num = den = 0.0
    n = 0
    for y, b in zip(y_by_dose, b_by_dose):
        yt = y - y.mean()
        bt = b - b.mean()
        num += float(yt @ bt)
        den += float(bt @ bt)
        n += y.size
    if den <= 0:
        return 0.0, float(sum(float(((y - y.mean()) ** 2).sum())
                              for y in y_by_dose)), n
    c = -num / den
    rss = 0.0
    for y, b in zip(y_by_dose, b_by_dose):
        r = (y - y.mean()) + c * (b - b.mean())
        rss += float(r @ r)
    return c, rss, n


def fit_pools(K, Y, p_init=None, bounds_log10=(-8.0, 8.0),
              restarts=(-3.0, -1.5, 0.0, 1.5, 3.0)):
    """
    Fit one effective pool per dose, K held fixed across doses.

    K   (N,)      affinity per transcript, molecules per cell
    Y   list of (N,) arrays, one per dose, of measured log2 fold change

    Returns a dict with the fitted pools, the shared amplitude, the residual
    sum of squares and per-dose residual spread.
    """
    K = np.asarray(K, dtype=np.float64)
    Y = [np.asarray(y, dtype=np.float64) for y in Y]
    D = len(Y)
    lo, hi = bounds_log10

    def nll(u):
        p = 10.0 ** np.clip(u, lo, hi)
        B = [bound_fraction(K, pi) for pi in p]
        c, rss, n = _profile(Y, B)
        # Gaussian profile likelihood with sigma concentrated out
        return 0.5 * n * np.log(max(rss, 1e-300) / n)

    if p_init is None:
        # start from the median K, the scale at which b is most informative
        u0 = np.full(D, float(np.log10(np.median(K))))
    else:
        u0 = np.log10(np.asarray(p_init, dtype=np.float64))

    best = None
    for shift in restarts:
        r = optimize.minimize(nll, u0 + shift, method="Nelder-Mead",
                              options={"xatol": 1e-8, "fatol": 1e-10,
                                       "maxiter": 20000, "maxfev": 20000})
        if best is None or r.fun < best.fun:
            best = r
    u = np.clip(best.x, lo, hi)
    p = 10.0 ** u
    B = [bound_fraction(K, pi) for pi in p]
    c, rss, n = _profile(Y, B)
    per_dose = []
    for y, b in zip(Y, B):
        r = (y - y.mean()) + c * (b - b.mean())
        per_dose.append(float(np.std(r, ddof=1)))
    return {
        "pool_per_dose": p.tolist(),
        "log10_pool_per_dose": u.tolist(),
        "amplitude_c_log2_per_unit_bound_fraction": float(c),
        "rss": float(rss),
        "n_observations": int(n),
        "sigma_pooled": float(np.sqrt(rss / n)),
        "residual_sd_per_dose": per_dose,
        "mean_bound_fraction_per_dose": [float(b.mean()) for b in B],
        "max_bound_fraction_per_dose": [float(b.max()) for b in B],
        "frac_sites_above_half_saturation_per_dose": [
            float((b > 0.5).mean()) for b in B],
        "optimiser_converged": bool(best.success),
        "nll": float(best.fun),
    }


def loglog_slope(dose, pool):
    """
    Slope of log10 pool on log10 dose by ordinary least squares.

    Slope 1 is the independent-scoring prediction and slope above 1 is the
    equilibrium signature; a slope below 1 is predicted by neither model as
    formulated. With two dose points this is the connecting line and has no
    residual degrees of freedom, which is reported rather than hidden.
    """
    x = np.log10(np.asarray(dose, dtype=np.float64))
    y = np.log10(np.asarray(pool, dtype=np.float64))
    n = x.size
    if n < 2:
        return {"slope": float("nan"), "intercept": float("nan"),
                "n_points": int(n), "residual_df": 0}
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ coef
    return {"slope": float(coef[0]), "intercept": float(coef[1]),
            "n_points": int(n), "residual_df": int(n - 2),
            "residual_rms_log10": float(np.sqrt((resid ** 2).mean()))}


def pooled_slope(rows):
    """
    One slope shared across constructs, with a free intercept per construct.

    Constructs differ in guide loading and in efficacy, so their pools differ
    by a constant factor that has nothing to do with dose. Fixed effects
    absorb that; the shared coefficient on log dose is the quantity of
    interest. `rows` is a list of (construct, dose, pool).
    """
    cons = sorted({r[0] for r in rows})
    idx = {c: i for i, c in enumerate(cons)}
    X = np.zeros((len(rows), len(cons) + 1))
    y = np.zeros(len(rows))
    for i, (c, d, p) in enumerate(rows):
        X[i, idx[c]] = 1.0
        X[i, -1] = np.log10(d)
        y[i] = np.log10(p)
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ coef
    df = len(rows) - X.shape[1]
    return {"slope": float(coef[-1]), "n_points": int(len(rows)),
            "n_constructs": len(cons), "residual_df": int(df),
            "residual_rms_log10": float(np.sqrt((resid ** 2).mean())),
            "construct_intercepts": {c: float(coef[idx[c]]) for c in cons}}


def invert_to_M(pool, K, x, beta=0.0):
    """
    The conservation equation read backwards.

        M = (1 + beta) f + sum_j x_j f / (K_j + f)

    Given the fitted free pool and the measured abundance and affinity
    vectors, this returns the total loaded complex that must have been
    present. No Argonaute copy number and no loaded fraction alpha enter,
    which is the point: rho = M / sum_j x_j then follows from measurement
    alone.
    """
    K = np.asarray(K, dtype=np.float64)
    x = np.asarray(x, dtype=np.float64)
    f = float(pool)
    return float((1.0 + beta) * f + float((x * f / (K + f)).sum()))


def percentile_ci(v, lo=2.5, hi=97.5):
    v = np.asarray([q for q in v if np.isfinite(q)], dtype=np.float64)
    if v.size == 0:
        return [float("nan"), float("nan")]
    return [float(np.percentile(v, lo)), float(np.percentile(v, hi))]


# ------------------------------------------------------ constrained fits --

def free_pool_from_M(M, K, x, beta=0.0):
    """
    Solve (1 + beta) f + sum_j x_j f/(K_j+f) = M for f.

    The same bisection the layer uses everywhere else, called through
    riscpool.equilibrium so there is one solver in the repository and not
    two. Vectorised over a list of M values.
    """
    import torch

    from .equilibrium import solve_free_pool
    M = np.atleast_1d(np.asarray(M, dtype=np.float64))
    Kt = torch.tensor(np.asarray(K, dtype=np.float64),
                      dtype=torch.float64)[None, :].expand(M.size, -1)
    xt = torch.tensor(np.asarray(x, dtype=np.float64),
                      dtype=torch.float64)[None, :].expand(M.size, -1)
    Mt = torch.tensor(M, dtype=torch.float64)[:, None]
    bt = torch.full_like(Mt, float(beta))
    f = solve_free_pool(Kt.contiguous(), xt.contiguous(), Mt, bt)
    return f[:, 0].numpy()


def fit_constrained(K, Y, doses, mode, x=None, beta=0.0,
                    bounds_log10=(-10.0, 10.0)):
    """
    The two models as ONE-parameter families, which is the sharpest form of
    the comparison the dose series makes possible.

    Both models say the total loaded complex is proportional to dose,
    M_d = kappa * dose_d, with kappa the only unknown. They differ in what
    the transcripts then see:

      mode="independent"   the effective pool IS M_d. Every transcript sees
                           the whole pool. p_d = kappa * dose_d.
      mode="equilibrium"   the effective pool is the free pool left after
                           the competitor set has taken its share,
                           p_d = f(kappa * dose_d), f solving conservation.

    Each is a single free parameter fitted to the same observations as the
    unconstrained three-pool fit, so the three are directly comparable by
    residual sum of squares and by AIC. The unconstrained fit cannot do worse
    than either; the question is by how much.
    """
    K = np.asarray(K, dtype=np.float64)
    Y = [np.asarray(y, dtype=np.float64) for y in Y]
    doses = np.asarray(doses, dtype=np.float64)
    lo, hi = bounds_log10

    def pools(u):
        M = 10.0 ** np.clip(u, lo, hi) * doses
        if mode == "independent":
            return M
        if mode == "equilibrium":
            return free_pool_from_M(M, K, x, beta)
        raise ValueError(mode)

    def nll(u):
        p = pools(float(np.atleast_1d(u)[0]))
        if not np.all(np.isfinite(p)) or np.any(p <= 0):
            return 1e18
        B = [bound_fraction(K, pi) for pi in p]
        c, rss, n = _profile(Y, B)
        return 0.5 * n * np.log(max(rss, 1e-300) / n)

    grid = np.linspace(lo, hi, 121)
    vals = [nll(u) for u in grid]
    u0 = float(grid[int(np.argmin(vals))])
    r = optimize.minimize_scalar(nll, bracket=None,
                                 bounds=(max(lo, u0 - 2.0),
                                         min(hi, u0 + 2.0)),
                                 method="bounded",
                                 options={"xatol": 1e-10})
    u = float(r.x)
    p = pools(u)
    B = [bound_fraction(K, pi) for pi in p]
    c, rss, n = _profile(Y, B)
    n_par = 1 + 1 + len(Y) + 1        # kappa, c, per-dose intercepts, sigma
    return {
        "mode": mode,
        "log10_kappa": u,
        "kappa_complexes_per_cell_per_nM": float(10.0 ** u),
        "pool_per_dose": p.tolist(),
        "M_per_dose": (10.0 ** u * doses).tolist(),
        "amplitude_c_log2_per_unit_bound_fraction": float(c),
        "rss": float(rss), "n_observations": int(n),
        "sigma_pooled": float(np.sqrt(rss / n)),
        "n_parameters": int(n_par),
        "aic": float(n * np.log(rss / n) + 2 * n_par),
        "nll": float(0.5 * n * np.log(rss / n)),
    }


def aic_of_free_fit(fit, n_doses):
    n = fit["n_observations"]
    n_par = n_doses + 1 + n_doses + 1     # pools, c, intercepts, sigma
    return float(n * np.log(fit["rss"] / n) + 2 * n_par), int(n_par)


# ------------------------------------------- site-class affinity variant --

CLASS_ORDER = ["6mer", "7mer-A1", "7mer-m8", "8mer"]


def class_K_vector(counts, K_by_class):
    """
    Transcript affinity from site counts and per-class affinities.

    Sites on one transcript are parallel binding opportunities, so
    1/K_tx = sum_s 1/K_site, which with counts per class is
    1/K_tx = sum_c n_c / K_c. A transcript with no site gets K = infinity and
    therefore zero bound fraction at any pool, which is what anchors the
    per-dose intercept.
    """
    inv = np.zeros(len(next(iter(counts.values()))), dtype=np.float64)
    for c, n in counts.items():
        inv = inv + np.asarray(n, dtype=np.float64) / K_by_class[c]
    with np.errstate(divide="ignore"):
        K = np.where(inv > 0, 1.0 / np.maximum(inv, 1e-300), np.inf)
    return K


def fit_class_pools(counts, Y, K_anchor, anchor_class="7mer-m8",
                    bounds_log10=(-6.0, 12.0), u0=None,
                    shifts=(-2.0, 0.0, 2.0), maxiter=40000):
    """
    One pool per dose with affinity carried by SITE CLASS rather than by a
    per-transcript thermodynamic estimate.

    Why this exists. The purely thermodynamic K used elsewhere in this
    repository does not rank off-target transcripts against the measured
    response, on this dataset or on GSE5814, and a pool fitted through an
    affinity model with no discriminative power is fitted to noise. The site
    class does discriminate: 8mer, 7mer-m8, 7mer-A1 and 6mer sites separate
    cleanly from no-site transcripts in this very dataset. So the affinity
    model here has one parameter per class, shared across doses, with one
    class pinned to the published seed-match dissociation constant to fix the
    common scale that would otherwise trade off against the pools.

    Free parameters: the affinities of the classes other than the anchor, and
    one pool per dose. The amplitude and the per-dose intercepts are profiled
    out in closed form exactly as in fit_pools. Transcripts with no site are
    included and carry zero bound fraction; they are what pins the intercept.

    The recovered class ordering is returned and is a real check: a fit that
    put the 8mer below the 6mer would be reporting that the model has failed.
    """
    Y = [np.asarray(y, dtype=np.float64) for y in Y]
    D = len(Y)
    free = [c for c in CLASS_ORDER if c != anchor_class]
    lo, hi = bounds_log10

    def unpack(u):
        Kc = {anchor_class: float(K_anchor)}
        for i, c in enumerate(free):
            Kc[c] = 10.0 ** float(np.clip(u[i], lo, hi))
        p = 10.0 ** np.clip(np.asarray(u[len(free):], dtype=np.float64),
                            lo, hi)
        return Kc, p

    def nll(u):
        Kc, p = unpack(u)
        K = class_K_vector(counts, Kc)
        B = [bound_fraction(K, pi) for pi in p]
        B = [np.where(np.isfinite(b), b, 0.0) for b in B]
        c, rss, n = _profile(Y, B)
        return 0.5 * n * np.log(max(rss, 1e-300) / n)

    if u0 is None:
        base = float(np.log10(K_anchor))
        u0 = np.array([base] * len(free) + [base] * D, dtype=np.float64)
    best = None
    for shift in shifts:
        s = np.array(u0, dtype=np.float64).copy()
        s[len(free):] += shift
        r = optimize.minimize(nll, s, method="Nelder-Mead",
                              options={"xatol": 1e-8, "fatol": 1e-10,
                                       "maxiter": maxiter, "maxfev": maxiter})
        if best is None or r.fun < best.fun:
            best = r
    Kc, p = unpack(best.x)
    K = class_K_vector(counts, Kc)
    B = [np.where(np.isfinite(b), b, 0.0)
         for b in (bound_fraction(K, pi) for pi in p)]
    c, rss, n = _profile(Y, B)
    order = [k for k, _ in sorted(Kc.items(), key=lambda kv: kv[1])]
    return {
        "pool_per_dose": p.tolist(),
        "log10_pool_per_dose": np.log10(p).tolist(),
        "K_by_class_molecules_per_cell": {k: float(v) for k, v in Kc.items()},
        "log10_K_by_class": {k: float(np.log10(v)) for k, v in Kc.items()},
        "anchor_class": anchor_class,
        "K_anchor_molecules_per_cell": float(K_anchor),
        "class_order_by_increasing_K": order,
        "class_ordering_is_8mer_strongest": bool(order[0] == "8mer"),
        "expected_ordering_if_model_sane": ["8mer", "7mer-m8", "7mer-A1",
                                            "6mer"],
        "amplitude_c_log2_per_unit_bound_fraction": float(c),
        "rss": float(rss), "n_observations": int(n),
        "sigma_pooled": float(np.sqrt(rss / n)),
        "mean_bound_fraction_per_dose": [float(np.mean(b)) for b in B],
        "n_transcripts_with_no_site": int(np.sum(~np.isfinite(K))),
        "optimiser_converged": bool(best.success),
        "u_hat": best.x.tolist(),
        "nll": float(best.fun),
    }


def intercepts_per_dose(K, Y, pools, c):
    """
    The per-dose intercepts a_d implied by a fit, recovered in closed form.

    _profile centres y and b within each dose, which removes a_d exactly and
    never records it. Predicting a gene that was not in the fit needs it
    back: the centred residual is (y - ybar) + c (b - bbar), so the fitted
    mean is ybar - c (b - bbar), i.e. a_d = ybar_d + c * bbar_d.
    """
    K = np.asarray(K, dtype=np.float64)
    out = []
    for y, p in zip(Y, pools):
        b = bound_fraction(K, p)
        b = np.where(np.isfinite(b), b, 0.0)
        out.append(float(np.mean(y) + c * np.mean(b)))
    return out


def holdout_rss(K, Y, pools, c, a_per_dose):
    """
    Out-of-sample residual sum of squares on genes held out of the fit.

    AIC rewards fit and penalises parameter count under an assumed model.
    Held-out prediction does not assume the model, so a constrained fit that
    is preferred on AIC but predicts worse on unseen genes is telling you the
    penalty, not the physics, did the work. Both are reported.
    """
    K = np.asarray(K, dtype=np.float64)
    rss = 0.0
    n = 0
    for y, p, a in zip(Y, pools, a_per_dose):
        b = bound_fraction(K, p)
        b = np.where(np.isfinite(b), b, 0.0)
        r = np.asarray(y, dtype=np.float64) - (a - c * b)
        rss += float(r @ r)
        n += int(y.size)
    return {"rss": rss, "n": n,
            "rmse": float(np.sqrt(rss / n)) if n else float("nan")}


def fit_class_constrained(counts, Y, doses, K_anchor, mode, x=None, beta=0.0,
                          anchor_class="7mer-m8", bounds_log10=(-6.0, 12.0),
                          u0=None, shifts=(-2.0, 0.0, 2.0), maxiter=40000):
    """
    The two models as one-parameter dose families, in the SITE-CLASS
    affinity parameterisation.

    fit_constrained does the same thing with the per-transcript thermodynamic
    K. That K does not rank off-target transcripts against the measured
    response, so a model comparison carried through it compares two ways of
    being uninformative. The site class does discriminate, so the comparison
    is worth making there, and this is that fit.

    Both models say the total loaded complex is proportional to dose,
    M_d = kappa * dose_d, with kappa >= 0 the only dose parameter, and they
    differ only in what the transcripts see:

      mode="independent"   the effective pool IS M_d.
      mode="equilibrium"   the effective pool is the free pool left after the
                           competitor set has taken its share, p_d = f(M_d).

    The class affinities are free in both, exactly as in the unconstrained
    fit, so the ONLY difference between the three models is how the pools are
    allowed to move with dose: three free pools, one kappa with p = M, or one
    kappa with p = f(M). That is what makes the AIC comparison a comparison
    of the dose mechanism and not of the affinity model.
    """
    Y = [np.asarray(y, dtype=np.float64) for y in Y]
    D = len(Y)
    doses = np.asarray(doses, dtype=np.float64)
    free = [c for c in CLASS_ORDER if c != anchor_class]
    lo, hi = bounds_log10
    if mode not in ("independent", "equilibrium"):
        raise ValueError(mode)
    if mode == "equilibrium" and x is None:
        raise ValueError("equilibrium mode needs the abundance vector x")
    xa = None if x is None else np.asarray(x, dtype=np.float64)

    def unpack(u):
        Kc = {anchor_class: float(K_anchor)}
        for i, cl in enumerate(free):
            Kc[cl] = 10.0 ** float(np.clip(u[i], lo, hi))
        kappa = 10.0 ** float(np.clip(u[len(free)], lo, hi))
        return Kc, kappa

    def pools_and_K(u):
        Kc, kappa = unpack(u)
        K = class_K_vector(counts, Kc)
        M = kappa * doses                      # kappa >= 0 by construction
        if mode == "independent":
            return K, M, Kc, kappa
        fin = np.isfinite(K)
        p = free_pool_from_M(M, K[fin], xa[fin], beta)
        return K, p, Kc, kappa

    def nll(u):
        K, p, _, _ = pools_and_K(u)
        if not np.all(np.isfinite(p)) or np.any(p <= 0):
            return 1e18
        B = [np.where(np.isfinite(b), b, 0.0)
             for b in (bound_fraction(K, pi) for pi in p)]
        _, rss, n = _profile(Y, B)
        return 0.5 * n * np.log(max(rss, 1e-300) / n)

    if u0 is None:
        base = float(np.log10(K_anchor))
        u0 = np.array([base] * len(free) + [base], dtype=np.float64)
    best = None
    for shift in shifts:
        s0 = np.array(u0, dtype=np.float64).copy()
        s0[len(free):] += shift
        r = optimize.minimize(nll, s0, method="Nelder-Mead",
                              options={"xatol": 1e-8, "fatol": 1e-10,
                                       "maxiter": maxiter, "maxfev": maxiter})
        if best is None or r.fun < best.fun:
            best = r
    K, p, Kc, kappa = pools_and_K(best.x)
    B = [np.where(np.isfinite(b), b, 0.0)
         for b in (bound_fraction(K, pi) for pi in p)]
    c, rss, n = _profile(Y, B)
    order = [k for k, _ in sorted(Kc.items(), key=lambda kv: kv[1])]
    n_par = len(free) + 1 + 1 + D + 1   # classes, kappa, c, intercepts, sigma
    return {
        "mode": mode,
        "parameterisation": "site_class",
        "K_by_class_molecules_per_cell": {k: float(v) for k, v in Kc.items()},
        "anchor_class": anchor_class,
        "class_order_by_increasing_K": order,
        "class_ordering_is_8mer_strongest": bool(order[0] == "8mer"),
        "kappa_complexes_per_cell_per_nM": float(kappa),
        "log10_kappa": float(np.log10(kappa)),
        "M_per_dose": (kappa * doses).tolist(),
        "pool_per_dose": np.asarray(p, dtype=np.float64).tolist(),
        "amplitude_c_log2_per_unit_bound_fraction": float(c),
        "intercept_per_dose": intercepts_per_dose(K, Y, p, c),
        "rss": float(rss), "n_observations": int(n),
        "sigma_pooled": float(np.sqrt(rss / n)),
        "n_parameters": int(n_par),
        "aic": float(n * np.log(rss / n) + 2 * n_par),
        "nll": float(best.fun),
        "optimiser_converged": bool(best.success),
        "u_hat": best.x.tolist(),
    }


def aic_of_class_fit(fit, n_doses, n_free_classes=3):
    n = fit["n_observations"]
    n_par = n_free_classes + n_doses + 1 + n_doses + 1
    return float(n * np.log(fit["rss"] / n) + 2 * n_par), int(n_par)
