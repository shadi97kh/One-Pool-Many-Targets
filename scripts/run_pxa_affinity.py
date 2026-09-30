"""
Positive extension A: a low-dimensional affinity correction, evaluated
externally on E-MEXP-668.

QUESTION. Does a three-parameter correction to the per-site thermodynamic
affinities improve transcript repression ranking on independent guides?

WHAT THIS IS NOT. It is not a test of conservation coupling. For fixed
affinities the equilibrium and independent fractional occupancies are strictly
monotone transforms of one another within a construct, so they induce the same
within-construct ranking and neither can win this comparison. This experiment
is about K, not about the layer that consumes K.

MODEL. In log space, with the 7mer-m8 class anchored at zero,

    log K_js_corrected = log K_js_thermo + delta[class(js)]
    score_j = -log K_j = logsumexp_s(-log K_js_corrected)

Three free offsets, for 8mer, 7mer-A1 and 6mer, initialised at zero and bounded
to [-3, 3]. The sign of the 7mer-A1 offset is NOT constrained: the training
data decide whether A1 sites bind better or worse than m8, which is the whole
point of fitting it rather than asserting it.

Because sites of one class enter only through their logsumexp, the score can be
written exactly as

    score_j = logsumexp_c ( S_jc - delta_c ),   S_jc = logsumexp_{s in c}(-log K_js)

so the fit needs a (transcript x 4) matrix per guide and never touches
individual sites again. That is an algebraic identity, not an approximation.

EVALUATION. Offsets and the ridge weight are chosen on GSE5814 alone, by
leave-one-family-out over target genes. The chosen configuration is frozen and
then applied unchanged to E-MEXP-668, whose responses are used for nothing
except the final score.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                            # noqa: E402
import pandas as pd                                           # noqa: E402
from scipy.optimize import minimize                           # noqa: E402
from scipy.special import logsumexp                           # noqa: E402
from scipy.stats import spearmanr                             # noqa: E402
from riscpool import features, runner                         # noqa: E402
from riscpool import provenance as P                          # noqa: E402
from riscpool.provenance import DATA, ROOT                    # noqa: E402

OUT = os.path.join(ROOT, "results", "positive_extensions")
D2_FEAT = os.path.join(DATA, "features_emexp668.parquet")
CLASSES = ["6mer", "7mer-A1", "7mer-m8", "8mer"]
ANCHOR = "7mer-m8"
FREE = [c for c in CLASSES if c != ANCHOR]
PAIR_SEED, BOOT_SEED = 1729, 1730
N_PAIRS, N_BOOT = 4096, 5000
LAMBDAS = [0.0, 0.01, 0.1, 1.0]
BOUNDS = [(-3.0, 3.0)] * len(FREE)


# --------------------------------------------------------------- features --
def build_d2_features():
    """E-MEXP-668 guides scored through the SAME code path as GSE5814.

    The accessibility array is guide-independent and both series are HeLa, so
    the cached array is reused and only the duplex energies are recomputed.
    """
    if os.path.exists(D2_FEAT):
        return pd.read_parquet(D2_FEAT)
    sir = pd.read_parquet(os.path.join(DATA, "birmingham_sirna.parquet"))
    sir = (sir[sir.guide_5to3_dna.notna()][["construct", "guide_5to3_dna"]]
           .drop_duplicates("construct").reset_index(drop=True))
    df = features.build(out=D2_FEAT, guides=sir)
    P.register_local(D2_FEAT, "D2_EMEXP668_derived",
                     note="per-site ViennaRNA features for the E-MEXP-668 "
                          "guides over the same canonical 3'UTR set and the "
                          "same cached accessibility array as GSE5814")
    return df


# ------------------------------------------------------------- score model --
def class_matrix(feat, resp_genes):
    """Per (construct, gene): S[:, c] = logsumexp over class-c sites of
    -log K_js, and N[:, c] = the number of class-c sites.

    -log K_js is -ddG/RT up to the common reference constant that cancels in
    every rank statistic used here.
    """
    from riscpool.features import RT
    d = feat[np.isfinite(feat.ddG_kcal)].copy()
    d = d[d.gene_symbol.isin(resp_genes)]
    d["v"] = -d.ddG_kcal.to_numpy() / RT
    out = {}
    for con, g in d.groupby("construct", sort=True):
        genes = np.sort(g.gene_symbol.unique())
        gi = {s: i for i, s in enumerate(genes)}
        S = np.full((len(genes), len(CLASSES)), -np.inf)
        N = np.zeros((len(genes), len(CLASSES)))
        ci = {c: i for i, c in enumerate(CLASSES)}
        gidx = g.gene_symbol.map(gi).to_numpy()
        cidx = g.site_class.map(ci).to_numpy()
        vals = g.v.to_numpy()
        ok = np.isfinite(gidx.astype(float)) & np.isfinite(cidx.astype(float))
        for a, b, v in zip(gidx[ok], cidx[ok], vals[ok]):
            S[a, b] = np.logaddexp(S[a, b], v)
            N[a, b] += 1
        out[con] = {"genes": genes, "S": S, "N": N}
    return out


def score_thermo(M, delta=None):
    """score_j = logsumexp_c (S_jc - delta_c). delta=None gives the
    uncorrected thermodynamic score."""
    S = M["S"]
    if delta is None:
        return logsumexp(S, axis=1)
    d = np.zeros(len(CLASSES))
    for k, c in enumerate(FREE):
        d[CLASSES.index(c)] = delta[k]
    return logsumexp(S - d[None, :], axis=1)


def score_class_only(M, const):
    """Class-only comparator: log K_js = c[class], no thermodynamic energy.
    1/K_j = sum_c n_jc exp(-c_c), so score_j = logsumexp_c(log n_jc - c_c)."""
    N = M["N"]
    c = np.zeros(len(CLASSES))
    for k, cl in enumerate(FREE):
        c[CLASSES.index(cl)] = const[k]
    with np.errstate(divide="ignore"):
        logN = np.where(N > 0, np.log(np.maximum(N, 1e-300)), -np.inf)
    return logsumexp(logN - c[None, :], axis=1)


# ---------------------------------------------------------------- training --
def make_pairs(y, rng, n_pairs=N_PAIRS):
    """Deterministic eligible unordered pairs, exact ties dropped.

    Sampled without materialising the O(n^2) table: draw index pairs and keep
    the ones whose responses differ.
    """
    n = len(y)
    if n < 2:
        return np.empty(0, int), np.empty(0, int), 0
    want = n_pairs
    a = rng.integers(0, n, want * 3)
    b = rng.integers(0, n, want * 3)
    keep = (a != b) & (y[a] != y[b])
    n_tied = int(((a != b) & (y[a] == y[b])).sum())
    a, b = a[keep][:want], b[keep][:want]
    return a, b, n_tied


def pair_loss(score, y, a, b):
    t = np.sign(y[a] - y[b])
    z = -t * (score[a] - score[b])
    return np.mean(np.logaddexp(0.0, z))          # softplus, stable


def fit(train, scorer, x0, lam, rng_seed=PAIR_SEED):
    """Balanced within-guide pairwise fit. Equal weight per guide within a
    family, then equal weight per family."""
    rng = np.random.default_rng(rng_seed)
    prepared, ties = [], 0
    for fam, cons in train.items():
        for con, (M, y) in cons.items():
            a, b, nt = make_pairs(y, rng)
            ties += nt
            if len(a):
                prepared.append((fam, M, y, a, b))
    fams = sorted({p[0] for p in prepared})

    def obj(theta):
        per_fam = {f: [] for f in fams}
        for fam, M, y, a, b in prepared:
            per_fam[fam].append(pair_loss(scorer(M, theta), y, a, b))
        L = np.mean([np.mean(v) for v in per_fam.values() if v])
        return L + lam * float(np.dot(theta, theta))

    r = minimize(obj, np.asarray(x0, float), method="L-BFGS-B",
                 bounds=BOUNDS, options={"maxiter": 500, "ftol": 1e-12})
    return r, ties


# -------------------------------------------------------------- evaluation --
def per_construct_spearman(data, scorer, theta):
    out = {}
    for fam, cons in data.items():
        for con, (M, y) in cons.items():
            s = scorer(M, theta)
            ok = np.isfinite(s) & np.isfinite(y)
            out[con] = (fam, float(spearmanr(s[ok], y[ok]).statistic)
                        if ok.sum() > 2 else np.nan, int(ok.sum()))
    return out


def equal_family_mean(per_con):
    fam = {}
    for con, (f, r, n) in per_con.items():
        if np.isfinite(r):
            fam.setdefault(f, []).append(r)
    if not fam:
        return np.nan, {}
    fam_mean = {f: float(np.mean(v)) for f, v in fam.items()}
    return float(np.mean(list(fam_mean.values()))), fam_mean


# ------------------------------------------------------------------- data --
def assemble(feat, resp, fam_of, value_col="value"):
    """{family: {construct: (class_matrix, y)}} with y = -log ratio."""
    genes = set(resp.gene_symbol)
    M = class_matrix(feat, genes)
    out = {}
    for con, m in M.items():
        r = resp[resp.construct == con]
        if r.empty:
            continue
        med = r.groupby("gene_symbol")[value_col].median()
        y = med.reindex(m["genes"]).to_numpy()
        ok = np.isfinite(y)
        if ok.sum() < 20:
            continue
        mm = {"genes": m["genes"][ok], "S": m["S"][ok], "N": m["N"][ok]}
        out.setdefault(fam_of[con], {})[con] = (mm, -y[ok])   # y = -log ratio
    return out


def fn(seed=0):
    spec = json.load(open(os.path.join(OUT, "run_spec.json")))
    fam1 = spec["families"]["D1_construct_to_family"]
    fam2 = spec["families"]["D2_construct_to_family"]

    from riscpool.offtarget import load_response
    d1_feat = features.load_features()
    d1_resp = load_response()
    d2_feat = build_d2_features()
    d2_resp = pd.read_parquet(os.path.join(DATA, "birmingham_response.parquet"))

    D1 = assemble(d1_feat, d1_resp, fam1)
    D2 = assemble(d2_feat, d2_resp, fam2)

    def n_rows(D):
        return int(sum(len(y) for c in D.values() for _, y in c.values()))
    elig = {"D1_families": sorted(D1), "D1_constructs":
            sorted(c for f in D1.values() for c in f),
            "D1_eligible_pairs": n_rows(D1),
            "D2_families": sorted(D2), "D2_constructs":
            sorted(c for f in D2.values() for c in f),
            "D2_eligible_pairs": n_rows(D2)}

    # ---- lambda by leave-one-family-out on D1 ONLY ---------------------
    loo = []
    for lam in LAMBDAS:
        scores = []
        for held in sorted(D1):
            tr = {f: v for f, v in D1.items() if f != held}
            r, _ = fit(tr, lambda M, t: score_thermo(M, t),
                       np.zeros(len(FREE)), lam)
            pc = per_construct_spearman({held: D1[held]},
                                        lambda M, t: score_thermo(M, t), r.x)
            m, _ = equal_family_mean(pc)
            scores.append(m)
        # diagnostic only: the offsets a full-D1 refit produces at this
        # lambda. Reported so that a null result can be told apart from a fit
        # that never moved. Does not enter lambda selection.
        rfull, _ = fit(D1, lambda M, t: score_thermo(M, t),
                       np.zeros(len(FREE)), lam)
        loo.append({"lambda": lam,
                    "loo_equal_family_mean_spearman": float(np.mean(scores)),
                    "per_held_out_family": dict(zip(sorted(D1), map(float, scores))),
                    "offsets_if_selected": dict(zip(FREE, map(float, rfull.x))),
                    "offset_max_abs": float(np.max(np.abs(rfull.x)))})
    # ties break toward stronger regularisation: scan the grid descending
    best = max(sorted(loo, key=lambda d: -d["lambda"]),
               key=lambda d: d["loo_equal_family_mean_spearman"])
    lam_star = best["lambda"]

    # baseline reference: the uncorrected thermodynamic score on the same
    # held-out D1 families, so the lambda table can be read against it
    m1_loo = []
    for held in sorted(D1):
        pc = per_construct_spearman({held: D1[held]},
                                    lambda M, t: score_thermo(M, None), None)
        m1_loo.append(equal_family_mean(pc)[0])
    m1_reference = float(np.mean(m1_loo))

    # ---- refit on ALL of D1, then freeze -------------------------------
    r3, n_ties = fit(D1, lambda M, t: score_thermo(M, t),
                     np.zeros(len(FREE)), lam_star)
    delta = r3.x.copy()
    r2, _ = fit(D1, lambda M, t: score_class_only(M, t),
                np.zeros(len(FREE)), lam_star)
    const = r2.x.copy()

    frozen = {"lambda": lam_star,
              "offsets_thermo_plus_class": dict(zip(FREE, map(float, delta))),
              "anchor": {ANCHOR: 0.0},
              "class_only_constants": dict(zip(FREE, map(float, const))),
              "optimiser_success": bool(r3.success), "n_iter": int(r3.nit),
              "final_objective": float(r3.fun),
              "training_pairs_with_exact_response_ties_dropped": int(n_ties)}
    with open(os.path.join(OUT, "A_frozen_config.json"), "w") as fh:
        json.dump(frozen, fh, indent=1)

    # ---- external evaluation on D2, identical rows for all models -------
    models = {
        "M1_thermodynamic": (lambda M, t: score_thermo(M, None), None),
        "M2_class_only": (lambda M, t: score_class_only(M, t), const),
        "M3_thermo_plus_offsets": (lambda M, t: score_thermo(M, t), delta),
    }
    ext, fam_means = {}, {}
    for name, (sc, th) in models.items():
        pc = per_construct_spearman(D2, sc, th)
        m, fm = equal_family_mean(pc)
        ext[name] = {"equal_family_mean_spearman": m,
                     "per_construct": {k: {"family": v[0], "spearman": v[1],
                                           "n": v[2]} for k, v in pc.items()},
                     "per_family": fm}
        fam_means[name] = fm

    fams = sorted(set(fam_means["M1_thermodynamic"]) &
                  set(fam_means["M3_thermo_plus_offsets"]))
    d1v = np.array([fam_means["M3_thermo_plus_offsets"][f] -
                    fam_means["M1_thermodynamic"][f] for f in fams])
    effect = float(np.mean(d1v))

    # paired family-cluster bootstrap
    rng = np.random.default_rng(BOOT_SEED)
    idx = rng.integers(0, len(fams), (N_BOOT, len(fams)))
    boot = d1v[idx].mean(axis=1)
    ci = [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))]
    idx0 = idx

    # exact paired sign randomisation over families
    from itertools import product
    if len(fams) <= 20:
        signs = np.array(list(product([-1, 1], repeat=len(fams))))
        null = (signs * d1v[None, :]).mean(axis=1)
        p = float((np.abs(null) >= abs(effect)).mean())
        p_mode = f"exact enumeration over 2^{len(fams)} sign flips"
    else:
        s = np.random.default_rng(BOOT_SEED).choice([-1, 1], (10000, len(fams)))
        null = (s * d1v[None, :]).mean(axis=1)
        p = float((np.abs(null) >= abs(effect)).mean())
        p_mode = "10000 fixed-seed sign flips"

    # prespecified SECONDARY comparator: does the thermodynamic energy add
    # anything beyond site class? Same families, same rows, same bootstrap.
    d2v = np.array([fam_means["M2_class_only"][f] -
                    fam_means["M1_thermodynamic"][f] for f in fams])
    eff2 = float(np.mean(d2v))
    boot2 = d2v[idx0].mean(axis=1)
    ci2 = [float(np.percentile(boot2, 2.5)), float(np.percentile(boot2, 97.5))]

    pd.DataFrame({"family": fams, "M1": [fam_means["M1_thermodynamic"][f] for f in fams],
                  "M3": [fam_means["M3_thermo_plus_offsets"][f] for f in fams],
                  "paired_difference": d1v}).to_csv(
        os.path.join(OUT, "A_per_family_external.csv"), index=False)
    np.save(os.path.join(OUT, "A_bootstrap_distribution.npy"), boot)

    return {
        "WHAT_THIS_TESTS": (
            "whether a three-parameter correction to per-site thermodynamic "
            "affinities improves within-guide repression ranking on guides "
            "that were never used to fit it. It does NOT test conservation "
            "coupling: for fixed affinities the equilibrium and independent "
            "fractional occupancies induce identical within-construct "
            "rankings, so neither can win this comparison."),
        "frozen_before_external_evaluation": frozen,
        "lambda_selection_D1_leave_one_family_out": loo,
        "D1_baseline_M1_equal_family_mean_spearman": m1_reference,
        "fit_movement_diagnostic": (
            "offsets_if_selected at each lambda shows how far the fit moves "
            "from zero. If the selected offsets are near zero the corrected "
            "model is numerically almost the baseline, and a null external "
            "effect means the correction did not move rather than that it "
            "moved and failed."),
        "eligibility": elig,
        "external_D2": ext,
        "secondary_paired_effect_M2_minus_M1": eff2,
        "secondary_effect_ci95_family_cluster_bootstrap": ci2,
        "secondary_interpretation": (
            "M2 uses site class alone and no thermodynamic energy. A positive "
            "M2 minus M1 means the ViennaRNA energies are not adding usable "
            "ranking information beyond the site class on these guides."),
        "primary_paired_effect_M3_minus_M1": effect,
        "primary_effect_ci95_family_cluster_bootstrap": ci,
        "bootstrap_n": N_BOOT, "bootstrap_seed": BOOT_SEED,
        "bootstrap_targets": ("sampling variation across THIS set of "
                              f"{len(fams)} guide families, not across guides "
                              "in general"),
        "sign_randomisation_p": p, "sign_randomisation_mode": p_mode,
        "sign_randomisation_null": ("family-level exchangeability and "
                                    "symmetry of the paired difference"),
        "n_independent_families_external": len(fams),
        "per_family_paired_difference": dict(zip(fams, map(float, d1v))),
        "supported_positive_result": bool(effect > 0 and ci[0] > 0),
        "CLAIM_SCOPE": ("a positive result here supports better AFFINITIES, "
                        "not added predictive value from coupling and not an "
                        "identified rho"),
        "LIMITATION_family_count": (
            f"{len(fams)} independent guide families support the external "
            "interval. Thousands of genes do not increase that number, and "
            "the interval is correspondingly unstable."),
    }


if __name__ == "__main__":
    runner.run("pxa_affinity_correction", fn, seed=0)
