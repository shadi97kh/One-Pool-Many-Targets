"""
e9 - the dose series, and a data-driven rho.

WHAT THIS EVADES. Proposition 3 says that at a fixed dose, within one
construct, equilibrium and independent scoring induce the same ranking, so no
rank statistic can separate them. It says nothing about the dose dependence,
because dose changes the pool. This experiment holds K_j fixed at the
feature-derived values and fits one scalar effective pool per dose.

A CORRECTION TO THE PREDICTION AS STATED IN THE BRIEF. The brief says the
equilibrium free pool "grows sublinearly and saturates", so that a log-log
slope below 1 is the signature of competition. That is the wrong direction
and the model says so. Conservation gives

    M(f) = (1 + beta) f + sum_j x_j f/(K_j + f)

with dM/df = (1+beta) + sum_j x_j K_j/(K_j+f)^2 > 0 and
d2M/df2 = -sum_j 2 x_j K_j/(K_j+f)^3 < 0. So M is strictly CONCAVE in f, so f
is strictly CONVEX in M, and since f(0) = 0 the ratio f/M increases with M.
Therefore

    d log f / d log M = (df/dM)(M/f) >= 1     always.

The absorbing capacity of the competitor set saturates, so each extra unit of
complex is buffered less than the last, and the free pool accelerates. What
is true in the brief's sense is a statement about the LEVEL of the pool:

    M / (1 + beta + sum_j x_j/K_j)  <=  f(M)  <=  M / (1 + beta)

the lower bound from f/(K_j+f) <= f/K_j and the upper from the occupancy
terms being nonnegative. f is convex with f(0)=0, so it lies above its
tangent at the origin, which is the lower bound. A level bounded above by a
line through the origin and an exponent below 1 are different statements and
only the first is true. The sign of the test depends on which is meant.

So the discriminating statement is the reverse of the brief's:

  independent scoring   the effective pool IS M_d, exactly proportional to
                        dose, so the slope is exactly 1 at every dose
  equilibrium           the effective pool is f_d, convex in M_d, so the
                        slope is at least 1 and is strictly above 1 unless
                        the system sits in the deep weak-binding limit

A slope of 1 therefore does NOT separate the models: it is what independent
scoring predicts and it is also what equilibrium predicts when rho is small
enough that the layer changes nothing anyway. A slope above 1 is evidence of
competition. A slope below 1 is not predicted by either model as specified.
This is reported as it comes out.

A SHARPER TEST THAN THE SLOPE. Both models are one-parameter families, since
both say M_d = kappa * dose_d and differ only in what the transcripts see.
Fitting each with its single kappa and comparing against the unconstrained
three-pool fit is a direct model comparison, and it is done here alongside
the slope.

THE PROPORTIONAL-LOADING ASSUMPTION. We assume that the intracellular
guide-specific loaded pool M is proportional to the administered guide dose.
The design makes it more plausible: total transfected duplex is constant
across doses, the specific siRNA being made up to 25 nM with non-targeting
control (10 nM for HK2-4031), so the transfected mass and therefore the gross
transfection load do not vary with the specific dose. It does NOT establish
proportional uptake, strand selection, Argonaute loading, displacement of
endogenous microRNA, or recycling, every one of which sits between the
pipette and M. The assumption is testable here: inverting each fitted pool
through conservation gives an implied M per dose, and the log-log slope of
that implied M against dose should be 1 if the assumption holds. It is
reported per construct as a check rather than asserted.
"""
import os
import sys

# Pin the thread pools BEFORE numpy or torch are imported. This experiment is
# thousands of small solves rather than a few large ones, so intra-op
# threading costs far more in contention than it saves in arithmetic: an
# unpinned run burned 22 CPU-hours on roughly 35 minutes of serial work
# without finishing. Thread count does not affect the numbers, only the clock.
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS",
           "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
import torch                                                    # noqa: E402
torch.set_num_threads(1)
import pandas as pd                                             # noqa: E402
from scipy.stats import spearmanr                               # noqa: E402
from riscpool import calibration, dose, dosefit as DF, runner    # noqa: E402
from riscpool.features import RT                                 # noqa: E402

N_BOOT = 300
MIN_TRANSCRIPTS = 100
STRONG_CLASSES = ("7mer-m8", "8mer", "7mer-A1")


def assemble(construct, tx, ab_by_cell, resp, scale):
    """
    The (K, x, y_per_dose) system for one construct.

    Only transcripts measured at EVERY dose enter, so the doses are compared
    on one common set and a change in the fitted pool cannot be an artefact
    of a changing transcript set. The on-target gene is dropped: it is
    cleaved through full complementarity, not through a seed match, and the
    layer makes no claim about it.
    """
    Cs = scale["K_scale_constant_C"]
    n_mrna = scale["mrna_molecules_per_cell"]
    r = resp[resp.construct == construct]
    if r.empty:
        return None
    cell = r.cell_line.iloc[0]
    target = dose.TARGET_OF[construct]
    ab = ab_by_cell[cell][["gene_symbol", "x_rel"]]

    d = tx[(tx.construct == construct) & (tx.gene_symbol != target)].copy()
    d = d[np.isfinite(d.K_transcript) & (d.K_transcript > 0)]
    d["K"] = d.K_transcript * Cs
    # the features table carries a placeholder x_rel column; abundance comes
    # from the arrays of the matching cell line, so drop it before joining
    d = d.drop(columns=[c for c in ("x_rel",) if c in d.columns])
    d = d.merge(ab, on="gene_symbol", how="inner")
    d["x"] = d.x_rel * n_mrna
    d = d[d.x > 0]

    doses = sorted(r.dose_nM.unique())
    wide = None
    for dd in doses:
        s = r[r.dose_nM == dd][["gene_symbol", "log2fc"]].rename(
            columns={"log2fc": f"y_{dd}"})
        wide = s if wide is None else wide.merge(s, on="gene_symbol",
                                                 how="inner")
    d = d.merge(wide, on="gene_symbol", how="inner")
    d = d.drop_duplicates(subset=["gene_symbol"]).reset_index(drop=True)
    for dd in doses:
        d = d[np.isfinite(d[f"y_{dd}"])]
    if len(d) < MIN_TRANSCRIPTS:
        return None

    # the class-affinity fit uses EVERY measured gene, not only the retrieved
    # ones: transcripts with no seed site carry zero bound fraction at any
    # pool and are what pins the per-dose intercept.
    full = ab.merge(wide, on="gene_symbol", how="inner")
    full = full[full.gene_symbol != target]
    cnt = (tx[tx.construct == construct]
           [["gene_symbol", "n_6mer", "n_7mer_A1", "n_7mer_m8", "n_8mer"]]
           .groupby("gene_symbol", as_index=False).sum())
    full = full.merge(cnt, on="gene_symbol", how="left")
    for q in ("n_6mer", "n_7mer_A1", "n_7mer_m8", "n_8mer"):
        full[q] = full[q].fillna(0.0)
    full["x"] = full.x_rel * n_mrna
    full = full[full.x > 0].drop_duplicates(subset=["gene_symbol"])
    for dd in doses:
        full = full[np.isfinite(full[f"y_{dd}"])]
    full = full.reset_index(drop=True)

    return {"construct": construct, "cell_line": cell, "target_gene": target,
            "doses": doses, "frame": d.reset_index(drop=True),
            "full": full, "n_mrna": n_mrna}


def positive_control(s):
    """
    Measured repression by site class against transcripts with no site.

    Nothing model-based. If this control is flat there is no seed-mediated
    signal to fit a pool to, and any exponent recovered from such a dataset
    is an artefact. It is reported per dose so that the growth of the effect
    with dose is visible directly in the measurement, before any model.
    """
    from scipy.stats import mannwhitneyu
    F, doses = s["full"], s["doses"]
    has = ((F.n_6mer + F.n_7mer_A1 + F.n_7mer_m8 + F.n_8mer) > 0).to_numpy()
    strongest = np.where(F.n_8mer > 0, "8mer",
                np.where(F.n_7mer_m8 > 0, "7mer-m8",
                np.where(F.n_7mer_A1 > 0, "7mer-A1",
                np.where(F.n_6mer > 0, "6mer", "none"))))
    rows = []
    for dd in doses:
        y = F[f"y_{dd}"].to_numpy()
        no = y[~has]
        row = {"dose_nM": dd, "n_no_site": int((~has).sum()),
               "median_log2fc_no_site": float(np.median(no))}
        for cl in ["6mer", "7mer-A1", "7mer-m8", "8mer"]:
            m = strongest == cl
            if m.sum() < 10:
                continue
            row[f"n_{cl}"] = int(m.sum())
            row[f"median_log2fc_{cl}"] = float(np.median(y[m]))
            row[f"delta_vs_no_site_{cl}"] = float(
                np.median(y[m]) - np.median(no))
            row[f"mann_whitney_p_less_{cl}"] = float(
                mannwhitneyu(y[m], no, alternative="less").pvalue)
        rows.append(row)
    return rows


N_FOLDS = 5


def class_model_comparison(counts, Yf, Xf, doses, kd_anchor, cls, rng):
    """
    The dose mechanism compared three ways, in the site-class
    parameterisation, by AIC and by held-out-gene prediction.

      free           one pool per dose, unconstrained
      independent    M_d = kappa * dose_d and p_d = M_d
      equilibrium    M_d = kappa * dose_d and p_d = f(M_d)

    The class affinities are free in all three, so the comparison isolates
    the dose mechanism. AIC alone can prefer a constrained model because the
    penalty saved exceeds the fit lost, which is a statement about parameter
    counting rather than about competition, so the same three models are also
    scored on genes held out of the fit. Folds are over GENES, because a gene
    appears at every dose and splitting observations rather than genes would
    leak the answer across the split.
    """
    n = len(Yf[0])
    # start the class affinities at the unconstrained solution and kappa at
    # the value that reproduces the unconstrained pools on average
    n_free_cls = len(DF.CLASS_ORDER) - 1
    k0 = float(np.log10(np.mean([q / dd for q, dd
                                 in zip(cls["pool_per_dose"], doses)])))
    u_start = list(cls["u_hat"][:n_free_cls]) + [k0]
    ind = DF.fit_class_constrained(counts, Yf, doses, kd_anchor,
                                   "independent", u0=u_start,
                                   shifts=(-1.0, 0.0, 1.0))
    eq = DF.fit_class_constrained(counts, Yf, doses, kd_anchor,
                                  "equilibrium", x=Xf, beta=0.0,
                                  u0=u_start, shifts=(-1.0, 0.0, 1.0))
    aic_free, npar_free = DF.aic_of_class_fit(cls, len(doses))

    fold = rng.integers(0, N_FOLDS, n)
    cv = {"free": [], "independent": [], "equilibrium": []}
    for k in range(N_FOLDS):
        tr, te = fold != k, fold == k
        ctr = {c: v[tr] for c, v in counts.items()}
        cte = {c: v[te] for c, v in counts.items()}
        Ytr = [y[tr] for y in Yf]
        Yte = [y[te] for y in Yf]
        try:
            f_tr = DF.fit_class_pools(ctr, Ytr, kd_anchor, u0=cls["u_hat"],
                                      shifts=(0.0,), maxiter=8000)
            i_tr = DF.fit_class_constrained(ctr, Ytr, doses, kd_anchor,
                                            "independent", u0=ind["u_hat"],
                                            shifts=(0.0,), maxiter=8000)
            e_tr = DF.fit_class_constrained(ctr, Ytr, doses, kd_anchor,
                                            "equilibrium", x=Xf[tr], beta=0.0,
                                            u0=eq["u_hat"], shifts=(0.0,),
                                            maxiter=8000)
        except Exception:
            continue
        for tag, ft in (("free", f_tr), ("independent", i_tr),
                        ("equilibrium", e_tr)):
            Kte = DF.class_K_vector(cte, ft["K_by_class_molecules_per_cell"])
            Ktr = DF.class_K_vector(ctr, ft["K_by_class_molecules_per_cell"])
            c = ft["amplitude_c_log2_per_unit_bound_fraction"]
            a = DF.intercepts_per_dose(Ktr, Ytr, ft["pool_per_dose"], c)
            cv[tag].append(DF.holdout_rss(Kte, Yte, ft["pool_per_dose"],
                                          c, a))
    out = {
        "n_folds_completed": len(cv["free"]),
        "fold_assignment": "random over genes, one draw, shared by all three",
        "aic_free_unconstrained": aic_free,
        "n_parameters_free": npar_free,
        "aic_independent": ind["aic"], "aic_equilibrium": eq["aic"],
        "aic_equilibrium_minus_independent": eq["aic"] - ind["aic"],
        "aic_free_minus_best_constrained": aic_free - min(ind["aic"],
                                                          eq["aic"]),
        "preferred_by_aic": min(
            (("free", aic_free), ("independent", ind["aic"]),
             ("equilibrium", eq["aic"])), key=lambda kv: kv[1])[0],
        "constrained_independent": ind,
        "constrained_equilibrium": eq,
    }
    for tag in ("free", "independent", "equilibrium"):
        if cv[tag]:
            rss = sum(q["rss"] for q in cv[tag])
            nn = sum(q["n"] for q in cv[tag])
            out[f"heldout_gene_rmse_{tag}"] = float(np.sqrt(rss / nn))
            out[f"heldout_gene_n_{tag}"] = int(nn)
    if all(f"heldout_gene_rmse_{t}" in out
           for t in ("free", "independent", "equilibrium")):
        r = {t: out[f"heldout_gene_rmse_{t}"]
             for t in ("free", "independent", "equilibrium")}
        out["preferred_by_heldout_gene_rmse"] = min(r, key=r.get)
        out["heldout_rmse_equilibrium_minus_independent"] = (
            r["equilibrium"] - r["independent"])
    return out


def fit_one(sys_, K, X, Y, doses, beta, restarts=None):
    kw = {} if restarts is None else {"restarts": restarts}
    free = DF.fit_pools(K, Y, **kw)
    ind = DF.fit_constrained(K, Y, doses, "independent")
    eq = DF.fit_constrained(K, Y, doses, "equilibrium", x=X, beta=beta)
    return free, ind, eq


def fn(seed=0):
    rng = np.random.default_rng(seed)
    feats = dose.load_features()
    scale = calibration.build_scale(feats)
    cst = calibration.load_constants()
    tx = dose.transcript_level()
    resp = dose.load_response()
    ab_all = dose.load_abundance()
    ab_by_cell = {c: g for c, g in ab_all.groupby("cell_line")}

    K_nonspecific = calibration.kd_molar_to_molecules_per_cell(
        cst["kd_seed_mismatched_molar"]["central"],
        cst["hela_cell_volume_litres"]["central"])

    constructs = sorted(dose.TARGET_OF)
    ctrl_of = {}
    per_construct, pooled_rows, boot_slopes = [], [], []
    pooled_rows_class, boot_pooled_class = [], []
    boot_pooled = []
    systems = {}

    for c in constructs:
        s = assemble(c, tx, ab_by_cell, resp, scale)
        if s is None:
            per_construct.append({"construct": c, "status": "SKIPPED",
                                  "reason": "fewer than "
                                            f"{MIN_TRANSCRIPTS} transcripts "
                                            "retrieved at every dose"})
            continue
        systems[c] = s
        ctrl_of[c] = positive_control(s)
        d, doses = s["frame"], s["doses"]
        K = d.K.to_numpy()
        X = d.x.to_numpy()
        Y = [d[f"y_{dd}"].to_numpy() for dd in doses]
        n_mrna = s["n_mrna"]

        # background bracket, exactly as e5 does it: no background binding at
        # all, and every non-retrieved transcript binding at the published
        # seed-mismatched Kd
        x_retrieved = float(X.sum())
        x_rest = max(0.0, n_mrna - x_retrieved)
        beta_hi = x_rest / K_nonspecific

        free, ind, eq = fit_one(s, K, X, Y, doses, 0.0)
        slope = DF.loglog_slope(doses, free["pool_per_dose"])

        # ---- the site-class affinity variant --------------------------
        F = s["full"]
        counts = {"6mer": F.n_6mer.to_numpy(),
                  "7mer-A1": F.n_7mer_A1.to_numpy(),
                  "7mer-m8": F.n_7mer_m8.to_numpy(),
                  "8mer": F.n_8mer.to_numpy()}
        Yf = [F[f"y_{dd}"].to_numpy() for dd in doses]
        Xf = F.x.to_numpy()
        kd_anchor = calibration.kd_molar_to_molecules_per_cell(
            cst["kd_seed_match_molar"]["central"],
            cst["hela_cell_volume_litres"]["central"])
        cls = DF.fit_class_pools(counts, Yf, kd_anchor)
        cls_slope = DF.loglog_slope(doses, cls["pool_per_dose"])
        cls_cmp = class_model_comparison(counts, Yf, Xf, doses, kd_anchor,
                                         cls, rng)
        Kcls = DF.class_K_vector(counts, cls["K_by_class_molecules_per_cell"])
        finite = np.isfinite(Kcls)
        x_nosite = float(Xf[~finite].sum())
        beta_hi_cls = x_nosite / K_nonspecific
        cls_rho = []
        for beta, tag in ((0.0, "zero_background"),
                          (beta_hi_cls, "max_background_bracket")):
            M = [DF.invert_to_M(q, Kcls[finite], Xf[finite], beta)
                 for q in cls["pool_per_dose"]]
            cls_rho.append({
                "beta_case": tag, "beta": beta,
                "M_per_dose_molecules_per_cell": M,
                "rho_per_dose": [m / n_mrna for m in M],
                "M_over_dose": [m / dd for m, dd in zip(M, doses)],
                "loglog_slope_M_vs_dose": DF.loglog_slope(doses, M)["slope"],
                "implied_alpha_loaded_fraction_low_ago2": [
                    m / cst["ago2_copies_per_cell"]["low"] for m in M],
                "implied_alpha_loaded_fraction_high_ago2": [
                    m / cst["ago2_copies_per_cell"]["high"] for m in M]})

        # invert the fitted free pools to total complex, and to rho
        rho_rows = []
        for beta, tag in ((0.0, "zero_background"),
                          (beta_hi, "max_background_bracket")):
            M = [DF.invert_to_M(p, K, X, beta)
                 for p in free["pool_per_dose"]]
            rho_rows.append({
                "beta_case": tag, "beta": beta,
                "M_per_dose_molecules_per_cell": M,
                "rho_per_dose": [m / n_mrna for m in M],
                "M_over_dose": [m / dd for m, dd in zip(M, doses)],
                "loglog_slope_M_vs_dose": DF.loglog_slope(doses, M)["slope"],
                "implied_alpha_loaded_fraction_low_ago2": [
                    m / cst["ago2_copies_per_cell"]["low"] for m in M],
                "implied_alpha_loaded_fraction_high_ago2": [
                    m / cst["ago2_copies_per_cell"]["high"] for m in M],
            })

        aic_free, npar_free = DF.aic_of_free_fit(free, len(doses))

        # sensitivity: strong site classes only, and dropping the top dose
        sens = {}
        strong = d[d.site_class.isin(STRONG_CLASSES)]
        if len(strong) >= MIN_TRANSCRIPTS:
            f2 = DF.fit_pools(strong.K.to_numpy(),
                              [strong[f"y_{dd}"].to_numpy() for dd in doses])
            sens["strong_sites_only"] = {
                "n_transcripts": int(len(strong)),
                "site_classes": list(STRONG_CLASSES),
                "pool_per_dose": f2["pool_per_dose"],
                "slope": DF.loglog_slope(doses, f2["pool_per_dose"])["slope"],
                "amplitude_c": f2["amplitude_c_log2_per_unit_bound_fraction"]}
        if len(doses) > 2:
            f3 = DF.fit_pools(K, Y[:-1])
            sens["excluding_top_dose"] = {
                "doses": doses[:-1],
                "pool_per_dose": f3["pool_per_dose"],
                "slope": DF.loglog_slope(doses[:-1],
                                         f3["pool_per_dose"])["slope"]}

        # does the affinity model carry any signal at all here
        diag = []
        for dd in doses:
            r = spearmanr(-np.log10(K), d[f"y_{dd}"].to_numpy())
            diag.append({"dose_nM": dd,
                         "spearman_minus_log10K_vs_log2fc":
                             float(r.statistic),
                         "p": float(r.pvalue),
                         "median_log2fc": float(np.median(d[f"y_{dd}"])),
                         "mean_log2fc": float(np.mean(d[f"y_{dd}"]))})

        per_construct.append({
            "construct": c, "status": "OK",
            "cell_line": s["cell_line"], "target_gene": s["target_gene"],
            "doses_nM": doses,
            "n_transcripts_retrieved_at_every_dose": int(len(d)),
            "n_transcripts_strong_site_classes": int(len(strong)),
            "total_retrieved_abundance_molecules_per_cell": x_retrieved,
            "background_beta_bracket_high": beta_hi,
            "free_fit": free,
            "loglog_slope_pool_vs_dose": slope,
            "constrained_independent": ind,
            "constrained_equilibrium": eq,
            "aic_free_unconstrained": aic_free,
            "aic_independent": ind["aic"],
            "aic_equilibrium": eq["aic"],
            "aic_equilibrium_minus_independent": eq["aic"] - ind["aic"],
            "preferred_by_aic": ("equilibrium" if eq["aic"] < ind["aic"]
                                 else "independent"),
            "rho_inversion": rho_rows,

            "class_fit": cls,
            "class_fit_n_genes": int(len(F)),
            "class_fit_loglog_slope_pool_vs_dose": cls_slope,
            "class_fit_rho_inversion": cls_rho,
            "class_fit_model_comparison": cls_cmp,
            "class_fit_positive_control": ctrl_of.get(c, []),

            "sensitivity": sens,
            "predictor_diagnostics_per_dose": diag,
        })
        for dd, p in zip(doses, free["pool_per_dose"]):
            pooled_rows.append((c, dd, p))
        for dd, p in zip(doses, cls["pool_per_dose"]):
            pooled_rows_class.append((c, dd, p))

    # ---------------------------------------------------------- bootstrap --
    ok = [p for p in per_construct if p["status"] == "OK"]
    boot_by_construct = {p["construct"]: {"slope": [], "pool": [],
                                          "rho_zero": [], "rho_max": [],
                                          "M_slope": [], "kappa_eq": [],
                                          "aic_diff": [], "cls_slope": [],
                                          "cls_pool": [], "cls_rho": [],
                                          "cls_M_slope": []} for p in ok}
    boot_class_rho_median = []
    boot_thermo_rho_median = []
    for _ in range(N_BOOT):
        rows = []
        iter_cls_rho, iter_thermo_rho = [], []
        for p in ok:
            c = p["construct"]
            s = systems[c]
            d, doses = s["frame"], s["doses"]
            n = len(d)
            ix = rng.integers(0, n, n)
            K = d.K.to_numpy()[ix]
            X = d.x.to_numpy()[ix]
            Y = [d[f"y_{dd}"].to_numpy()[ix] for dd in doses]
            try:
                fb = DF.fit_pools(K, Y, p_init=p["free_fit"]["pool_per_dose"],
                                  restarts=(0.0,))
                eb = DF.fit_constrained(K, Y, doses, "equilibrium", x=X,
                                        beta=0.0)
                ib = DF.fit_constrained(K, Y, doses, "independent")
            except Exception:
                continue
            pools = fb["pool_per_dose"]
            b = boot_by_construct[c]
            b["slope"].append(DF.loglog_slope(doses, pools)["slope"])
            b["pool"].append(pools)
            b["kappa_eq"].append(eb["kappa_complexes_per_cell_per_nM"])
            b["aic_diff"].append(eb["aic"] - ib["aic"])
            n_mrna = s["n_mrna"]
            beta_hi = p["background_beta_bracket_high"]
            M0 = [DF.invert_to_M(q, K, X, 0.0) for q in pools]
            Mh = [DF.invert_to_M(q, K, X, beta_hi) for q in pools]
            b["rho_zero"].append([m / n_mrna for m in M0])
            b["rho_max"].append([m / n_mrna for m in Mh])
            iter_thermo_rho.extend([m / n_mrna for m in M0])
            b["M_slope"].append(DF.loglog_slope(doses, M0)["slope"])
            # the class-affinity variant, resampled on the same draw
            Fb = s["full"]
            nf = len(Fb)
            jx = rng.integers(0, nf, nf)
            cnt_b = {"6mer": Fb.n_6mer.to_numpy()[jx],
                     "7mer-A1": Fb.n_7mer_A1.to_numpy()[jx],
                     "7mer-m8": Fb.n_7mer_m8.to_numpy()[jx],
                     "8mer": Fb.n_8mer.to_numpy()[jx]}
            Yb = [Fb[f"y_{dd}"].to_numpy()[jx] for dd in doses]
            Xb = Fb.x.to_numpy()[jx]
            try:
                cb = DF.fit_class_pools(
                    cnt_b, Yb, p["class_fit"]["K_anchor_molecules_per_cell"],
                    u0=p["class_fit"]["u_hat"], shifts=(0.0,), maxiter=4000)
            except Exception:
                cb = None
            if cb is not None:
                b["cls_slope"].append(
                    DF.loglog_slope(doses, cb["pool_per_dose"])["slope"])
                b["cls_pool"].append(cb["pool_per_dose"])
                Kb = DF.class_K_vector(
                    cnt_b, cb["K_by_class_molecules_per_cell"])
                fin = np.isfinite(Kb)
                Mb = [DF.invert_to_M(q, Kb[fin], Xb[fin], 0.0)
                      for q in cb["pool_per_dose"]]
                b["cls_rho"].append([m / n_mrna for m in Mb])
                iter_cls_rho.extend([m / n_mrna for m in Mb])
                b["cls_M_slope"].append(
                    DF.loglog_slope(doses, Mb)["slope"])
            for dd, q in zip(doses, pools):
                rows.append((c, dd, q))
        # A confidence interval needs an estimand. The estimand here is the
        # MEDIAN rho over the construct-dose cells, recomputed inside each
        # resample; collecting the endpoints of separate per-dose intervals
        # and taking their extremes, as an earlier version did, is not an
        # interval for anything.
        if iter_cls_rho:
            boot_class_rho_median.append(float(np.median(iter_cls_rho)))
        if iter_thermo_rho:
            boot_thermo_rho_median.append(float(np.median(iter_thermo_rho)))
        if rows:
            try:
                boot_pooled.append(DF.pooled_slope(rows)["slope"])
            except Exception:
                pass
        rows_c = []
        for p in ok:
            b = boot_by_construct[p["construct"]]
            if b["cls_pool"]:
                for dd, q in zip(p["doses_nM"], b["cls_pool"][-1]):
                    rows_c.append((p["construct"], dd, q))
        if rows_c:
            try:
                boot_pooled_class.append(DF.pooled_slope(rows_c)["slope"])
            except Exception:
                pass

    for p in ok:
        b = boot_by_construct[p["construct"]]
        nd = len(p["doses_nM"])
        p["bootstrap"] = {
            "n_resamples": N_BOOT,
            "n_successful": len(b["slope"]),
            "slope_ci95": DF.percentile_ci(b["slope"]),
            "slope_median": float(np.median(b["slope"])) if b["slope"]
                            else float("nan"),
            "slope_sd": float(np.std(b["slope"], ddof=1))
                        if len(b["slope"]) > 1 else float("nan"),
            "M_vs_dose_slope_ci95": DF.percentile_ci(b["M_slope"]),
            "aic_equilibrium_minus_independent_ci95": DF.percentile_ci(
                b["aic_diff"]),
            "frac_resamples_preferring_equilibrium": float(np.mean(
                [q < 0 for q in b["aic_diff"]])) if b["aic_diff"] else
                float("nan"),
            "frac_resamples_slope_above_1": float(np.mean(
                [q > 1.0 for q in b["slope"]])) if b["slope"] else
                float("nan"),
            "pool_ci95_per_dose": [
                DF.percentile_ci([r[i] for r in b["pool"]])
                for i in range(nd)],
            "rho_ci95_per_dose_zero_background": [
                DF.percentile_ci([r[i] for r in b["rho_zero"]])
                for i in range(nd)],
            "rho_ci95_per_dose_max_background": [
                DF.percentile_ci([r[i] for r in b["rho_max"]])
                for i in range(nd)],
            "rho_median_per_dose_zero_background": [
                float(np.median([r[i] for r in b["rho_zero"]]))
                for i in range(nd)] if b["rho_zero"] else None,
        }
        p["class_fit_bootstrap"] = {
            "n_successful": len(b["cls_slope"]),
            "slope_ci95": DF.percentile_ci(b["cls_slope"]),
            "slope_median": float(np.median(b["cls_slope"]))
                            if b["cls_slope"] else float("nan"),
            "frac_resamples_slope_above_1": float(np.mean(
                [q > 1.0 for q in b["cls_slope"]])) if b["cls_slope"]
                else float("nan"),
            "M_vs_dose_slope_ci95": DF.percentile_ci(b["cls_M_slope"]),
            "pool_ci95_per_dose": [
                DF.percentile_ci([r[i] for r in b["cls_pool"]])
                for i in range(nd)] if b["cls_pool"] else None,
            "rho_ci95_per_dose_zero_background": [
                DF.percentile_ci([r[i] for r in b["cls_rho"]])
                for i in range(nd)] if b["cls_rho"] else None,
            "rho_median_per_dose_zero_background": [
                float(np.median([r[i] for r in b["cls_rho"]]))
                for i in range(nd)] if b["cls_rho"] else None,
        }

    pooled = DF.pooled_slope(pooled_rows) if pooled_rows else None
    all_rho_zero, all_rho_max = [], []
    for p in ok:
        for r in p["rho_inversion"]:
            (all_rho_zero if r["beta_case"] == "zero_background"
             else all_rho_max).extend(r["rho_per_dose"])
    boot_all_rho = []
    for p in ok:
        b = boot_by_construct[p["construct"]]
        for r in b["rho_zero"]:
            boot_all_rho.extend(r)

    # ---- leave-one-construct-out, and the M-vs-dose audit ---------------
    # A pooled exponent over five constructs, one of which has two dose
    # points and therefore no residual degree of freedom, can be carried by
    # that one construct. Refitting with each construct dropped in turn says
    # whether it is.
    def loco(rows):
        cons = sorted({r[0] for r in rows})
        out = []
        for drop in cons:
            keep = [r for r in rows if r[0] != drop]
            if len({r[0] for r in keep}) < 2:
                continue
            fit = DF.pooled_slope(keep)
            out.append({"construct_excluded": drop, "slope": fit["slope"],
                        "n_points": fit["n_points"],
                        "n_constructs": fit["n_constructs"],
                        "residual_df": fit["residual_df"],
                        "residual_rms_log10": fit["residual_rms_log10"]})
        return out

    loco_class = loco(pooled_rows_class) if pooled_rows_class else []
    loco_thermo = loco(pooled_rows) if pooled_rows else []
    full_class_slope = (DF.pooled_slope(pooled_rows_class)["slope"]
                        if pooled_rows_class else float("nan"))
    loco_class_range = ([min(q["slope"] for q in loco_class),
                         max(q["slope"] for q in loco_class)]
                        if loco_class else None)

    m_slope_rows = []
    for p in ok:
        cb = p.get("class_fit_bootstrap") or {}
        ri = [r for r in p["class_fit_rho_inversion"]
              if r["beta_case"] == "zero_background"][0]
        ci = cb.get("M_vs_dose_slope_ci95") or [float("nan")] * 2
        m_slope_rows.append({
            "construct": p["construct"],
            "n_doses": len(p["doses_nM"]),
            "loglog_slope_M_vs_dose": ri["loglog_slope_M_vs_dose"],
            "bootstrap_ci95": ci,
            "ci_excludes_one": bool(np.isfinite(ci[0]) and np.isfinite(ci[1])
                                    and (ci[0] > 1.0 or ci[1] < 1.0)),
        })
    n_excl = sum(1 for r in m_slope_rows if r["ci_excludes_one"])

    e5_band = [1.875e-4, 2.125]
    e5_contour = 0.0703872016148075
    return {
        "PREDICTION_DIRECTION_CORRECTION": (
            "The brief states that the equilibrium free pool grows "
            "SUBLINEARLY in dose and that a log-log slope below 1 is the "
            "signature of competition. The conservation equation says the "
            "opposite. M(f) is strictly concave in f because "
            "d2M/df2 = -sum_j 2 x_j K_j/(K_j+f)^3 < 0, so f is strictly "
            "convex in M, and with f(0)=0 this forces "
            "d log f / d log M >= 1 everywhere. Independent scoring predicts "
            "a slope of exactly 1; equilibrium predicts at least 1, and "
            "strictly more than 1 except in the deep weak-binding limit "
            "where the two models agree about everything else too. A slope "
            "of 1 is therefore not discriminating, a slope above 1 is "
            "evidence of competition, and a slope below 1 is predicted by "
            "neither model. What IS true in the brief's sense is a "
            "statement about the LEVEL of the pool, not about its exponent: "
            "M/(1 + beta + sum_j x_j/K_j) <= f(M) <= M/(1 + beta), the "
            "lower bound because f/(K_j+f) <= f/K_j and the upper because "
            "the occupancy terms are nonnegative. f is convex with f(0)=0, "
            "so it lies above its tangent at the origin, which is the lower "
            "bound; superlinear elasticity does not put f above M/(1+beta)."),
        "identifying_assumption": (
            "the amplitude c, the log2 repression of a fully occupied "
            "transcript, is shared across doses within a construct because "
            "it is a property of the silencing machinery and cannot depend "
            "on how much siRNA was pipetted on. In the weak-binding limit "
            "only the product c * pool is identified, so the ABSOLUTE pool "
            "and therefore rho rest on curvature in the data, while the "
            "SLOPE survives the degeneracy intact. Wide rho intervals "
            "alongside a tight slope are the expected signature of that, not "
            "a fitting failure."),
        "PROPORTIONAL_LOADING_ASSUMPTION": (
            "We ASSUME that the intracellular guide-specific loaded pool M "
            "is proportional to the administered guide dose. Total "
            "transfected duplex is held constant across doses by making the "
            "specific siRNA up to 25 nM with non-targeting control siRNA, "
            "and to 10 nM with AllStars for HK2-4031, as the CEL file names "
            "record. That makes the assumption more plausible, but it does "
            "not establish proportional uptake, strand selection, Argonaute "
            "loading, displacement of endogenous microRNA, or recycling. "
            "The assumption is checked, not asserted: "
            "M_vs_dose_slope_summary reports the log-log slope of the "
            "conservation-inverted M against dose for each construct, which "
            "must be 1 if the assumption holds."),
        "data_source": "GSE28786 (Caffrey et al. 2011, PMC3130022)",
        "gencode_release": 50,
        "constants_used": scale,
        "K_source": (
            "ViennaRNA duplex energy plus the pfl_fold opening cost "
            "on GENCODE v50 3'UTRs, anchored on the published seed-match Kd. "
            "K is never fitted to the expression response and is held fixed "
            "across doses, which is the whole point of the design."),
        "n_bootstrap": N_BOOT,
        "min_transcripts_required": MIN_TRANSCRIPTS,
        "constructs": constructs,
        "n_constructs_fitted": len(ok),
        "per_construct": per_construct,

        "AFFINITY_MODEL_FINDING": (
            "the purely thermodynamic K used by e4, e5 and e7 does not rank "
            "off-target transcripts against the measured response in this "
            "dataset either: the Spearman correlation between -log10 K and "
            "the measured log2 fold change is within 0.06 of zero at every "
            "dose of every construct, which reproduces on MCF-7 and Hep3B "
            "the limitation e7 already recorded on HeLa. A pool fitted "
            "through an affinity model with no discriminative power is "
            "fitted to noise, and the unstable per-construct exponents of "
            "the thermodynamic fit below are exactly that. The positive "
            "control shows the seed signal itself is present and strong, so "
            "the failure is in the affinity model and not in the data. The "
            "site-class fit is therefore reported alongside, with affinity "
            "carried by site class, one parameter per class shared across "
            "doses, the 7mer-m8 class pinned to the published seed-match Kd, "
            "and every measured gene included so that no-site transcripts "
            "pin the per-dose intercept."),
        "class_fit_pooled_slope_construct_fixed_effects": (
            DF.pooled_slope(pooled_rows_class) if pooled_rows_class
            else None),
        "class_fit_pooled_slope_bootstrap_ci95": DF.percentile_ci(
            boot_pooled_class),
        "class_fit_pooled_slope_bootstrap_median": float(
            np.median(boot_pooled_class)) if boot_pooled_class
            else float("nan"),
        "class_fit_pooled_slope_frac_resamples_above_1": float(np.mean(
            [q > 1.0 for q in boot_pooled_class])) if boot_pooled_class
            else float("nan"),
        "class_fit_n_constructs_with_sane_class_ordering": int(sum(
            p["class_fit"]["class_ordering_is_8mer_strongest"] for p in ok)),
        "class_fit_rho_all_construct_dose_zero_background": [
            q for p in ok for r in p["class_fit_rho_inversion"]
            if r["beta_case"] == "zero_background" for q in r["rho_per_dose"]],
        "class_fit_rho_median_zero_background": float(np.median([
            q for p in ok for r in p["class_fit_rho_inversion"]
            if r["beta_case"] == "zero_background"
            for q in r["rho_per_dose"]])) if ok else float("nan"),
        # The estimand is the MEDIAN rho over construct-dose cells,
        # recomputed within each bootstrap resample. The previous version
        # pooled the ENDPOINTS of separate per-dose intervals and took
        # percentiles of that, which is an interval for no quantity at all
        # and spanned eleven decades as a result.
        "class_fit_rho_median_bootstrap_ci95": DF.percentile_ci(
            boot_class_rho_median),
        "class_fit_rho_median_bootstrap_n": len(boot_class_rho_median),
        "class_fit_rho_per_dose_intervals_are_reported_separately_in":
            "per_construct[].class_fit_bootstrap."
            "rho_ci95_per_dose_zero_background",
        "class_fit_rho_point_estimate_spread_decades": (
            float(np.log10(max(q for p in ok for r in
                               p["class_fit_rho_inversion"]
                               if r["beta_case"] == "zero_background"
                               for q in r["rho_per_dose"] if q > 0)
                           / min(q for p in ok for r in
                                 p["class_fit_rho_inversion"]
                                 if r["beta_case"] == "zero_background"
                                 for q in r["rho_per_dose"] if q > 0)))
            if ok else float("nan")),

        "RHO_IS_NOT_IDENTIFIED": (
            "the point estimates of rho span "
            "class_fit_rho_point_estimate_spread_decades decades across "
            "construct-dose cells and the median carries a bootstrap "
            "interval of its own on top of that, so no single number here "
            "is a calibrated cellular estimate of the competition "
            "parameter. The median is reported as a location of a spread, "
            "not as a measurement, and it does not resolve the "
            "alpha-driven uncertainty of e5: it replaces one unmeasured "
            "quantity with a heterogeneous fit."),

        "leave_one_construct_out_class_fit": loco_class,
        "leave_one_construct_out_thermo_fit": loco_thermo,
        "class_fit_pooled_slope_all_constructs": full_class_slope,
        "class_fit_pooled_slope_loco_range": loco_class_range,
        "class_fit_pooled_slope_excluding_HK2_4031": next(
            (q["slope"] for q in loco_class
             if q["construct_excluded"] == "HK2-4031"), float("nan")),
        "LOCO_NOTE": (
            "HK2-4031 has two dose points, so its individual slope has zero "
            "residual degrees of freedom and is the line through two "
            "points. Dropping it moves the pooled exponent from "
            "class_fit_pooled_slope_all_constructs to "
            "class_fit_pooled_slope_excluding_HK2_4031, which is the "
            "sensitivity that decides whether the pooled superlinear "
            "estimate is a property of the panel or of one construct."),

        "M_vs_dose_slope_summary": {
            "per_construct": m_slope_rows,
            "n_constructs": len(m_slope_rows),
            "n_with_ci_excluding_one": n_excl,
            "test": (
                "the assumed proportionality M_d = kappa * dose_d implies a "
                "log-log slope of exactly 1 for the conservation-inverted M "
                "against dose. These are the measured slopes. A slope away "
                "from 1 whose interval excludes 1 falsifies the assumption "
                "for that construct, or the affinity model through which "
                "the inversion runs, and the two cannot be separated here."),
        },

        "class_fit_model_comparison_summary": {
            "n_constructs": len(ok),
            "preferred_by_aic": {
                p["construct"]:
                    p["class_fit_model_comparison"]["preferred_by_aic"]
                for p in ok},
            "preferred_by_heldout_gene_rmse": {
                p["construct"]:
                    p["class_fit_model_comparison"].get(
                        "preferred_by_heldout_gene_rmse")
                for p in ok},
            "n_preferring_equilibrium_by_aic": sum(
                p["class_fit_model_comparison"]["preferred_by_aic"]
                == "equilibrium" for p in ok),
            "n_preferring_equilibrium_by_heldout": sum(
                p["class_fit_model_comparison"].get(
                    "preferred_by_heldout_gene_rmse") == "equilibrium"
                for p in ok),
            "n_preferring_free_unconstrained_by_aic": sum(
                p["class_fit_model_comparison"]["preferred_by_aic"] == "free"
                for p in ok),
            "aic_equilibrium_minus_independent": {
                p["construct"]: p["class_fit_model_comparison"][
                    "aic_equilibrium_minus_independent"] for p in ok},
            "heldout_rmse_equilibrium_minus_independent": {
                p["construct"]: p["class_fit_model_comparison"].get(
                    "heldout_rmse_equilibrium_minus_independent")
                for p in ok},
            "note": (
                "three dose mechanisms in the site-class parameterisation: "
                "free pools per dose, M proportional to dose with the pool "
                "equal to M, and M proportional to dose with the pool the "
                "equilibrium free level. The class affinities are free in "
                "all three, so this compares the dose mechanism and nothing "
                "else. A preference for the FREE model says the data reject "
                "proportional loading in either mechanistic form."),
        },

        "pooled_slope_construct_fixed_effects": pooled,
        "pooled_slope_bootstrap_ci95": DF.percentile_ci(boot_pooled),
        "pooled_slope_bootstrap_median": float(np.median(boot_pooled))
                                          if boot_pooled else float("nan"),
        "pooled_slope_bootstrap_n": len(boot_pooled),
        "pooled_slope_frac_resamples_above_1": float(np.mean(
            [q > 1.0 for q in boot_pooled])) if boot_pooled else
            float("nan"),

        "rho_data_driven_zero_background_all_construct_dose": all_rho_zero,
        "rho_data_driven_max_background_all_construct_dose": all_rho_max,
        "rho_data_driven_median_zero_background": float(
            np.median(all_rho_zero)) if all_rho_zero else float("nan"),
        "rho_data_driven_median_bootstrap_ci95": DF.percentile_ci(
            boot_thermo_rho_median),
        "rho_data_driven_pooled_draw_spread_2p5_97p5": DF.percentile_ci(
            boot_all_rho),
        "rho_data_driven_spread_note": (
            "rho_data_driven_median_bootstrap_ci95 is an interval for the "
            "median rho over construct-dose cells, recomputed inside each "
            "resample. rho_data_driven_pooled_draw_spread_2p5_97p5 is the "
            "spread of the individual rho draws themselves and is a "
            "description of heterogeneity, not a confidence interval."),
        "rho_data_driven_range_zero_background": [
            float(np.min(all_rho_zero)), float(np.max(all_rho_zero))
        ] if all_rho_zero else None,

        "e5_alpha_swept_band_for_comparison": e5_band,
        "e5_alpha_swept_band_width_decades": float(
            np.log10(e5_band[1] / e5_band[0])),
        "e5_tau_0.9_contour_rho": e5_contour,
        "comparison_note": (
            "e5 could only bracket rho between "
            f"{e5_band[0]:.3e} and {e5_band[1]:.3e}, a span of "
            f"{np.log10(e5_band[1] / e5_band[0]):.2f} decades, because the "
            "loaded fraction alpha is unmeasured. The rho reported here uses "
            "no alpha and no Argonaute copy number: it is the total complex "
            "the fitted free pool implies through conservation, divided by "
            "the measured abundance total. The two are compared, not merged."),

        "POWER_LIMITATION": (
            "Three dose points per construct, two for HK2-4031. A slope from "
            "three points has one residual degree of freedom and from two "
            "points has none, so the per-construct interval is wide by "
            "construction and the bootstrap resamples transcripts, not "
            "doses: it propagates uncertainty in each fitted pool, and it "
            "cannot represent uncertainty about the dose grid itself. The "
            "pooled fit borrows strength across constructs but assumes one "
            "common exponent, which is an assumption and not a measurement. "
            "Two of the five constructs are the 2'-O-methyl modified "
            "versions of the other two rather than independent guides, and "
            "the two cell lines differ between the STAT3 and HK2 arms, so "
            "the five constructs are not five independent replications."),
        "SCALE_LIMITATION": (
            "The molecules-per-cell scale uses the same published total mRNA "
            "count per cell as e5, which was measured in neither MCF-7 nor "
            "Hep3B. rho and the implied alpha inherit that, and they are an "
            "order-of-magnitude scale rather than a calibration. The SLOPE "
            "is invariant to it: rescaling every K and x by a common factor "
            "rescales the fitted pools by the same factor and leaves the "
            "exponent untouched."),
    }


if __name__ == "__main__":
    runner.run("e9_dose_response", fn, seed=0)
