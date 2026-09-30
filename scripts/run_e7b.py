"""
e7b - how big is the signal really, and how big is nothing?

e7 reported point estimates: a site-class hierarchy and a pooled Spearman
against the measured response. Neither came with an uncertainty, and a pooled
Spearman of 0.036 looks meaningful only until you ask what a shuffled dataset
would have produced. This experiment supplies the three missing things.

  1. Site-class medians with bootstrap intervals and n, pooled and per
     construct, under TWO class-assignment rules. e7 labels a transcript by
     the class of its lowest-ddG site, which is a thermodynamic choice; the
     canonical alternative labels it by the strongest class present
     (8mer > 7mer-m8 > 7mer-A1 > 6mer). If the reported inversion of the two
     7mer classes is an artefact of the first rule it will not survive the
     second, and that is worth knowing before anything is said about it.

  2. A permutation null for the pooled Spearman. Measured values are shuffled
     WITHIN construct, which destroys the transcript-level association while
     preserving each construct's own response distribution and the pooling
     structure. Anything inside that envelope is indistinguishable from no
     signal at all.

  3. Bootstrap intervals on the pooled Spearman at every rho, so the dip that
     e7 recorded can be judged rather than eyeballed.

  4. A PAIRED comparison of the two scorings. A raw difference of two pooled
     Spearman correlations is not evidence that one model predicts better
     than the other, because the two have different permutation-null
     baselines: pooling constructs leaves a between-construct correlation
     that survives a within-construct shuffle, and it is not the same for
     equilibrium and for independent scoring. The paired test applies the
     SAME within-construct permutation of the measured response to both
     models and takes the difference of the two correlations under that one
     shuffle, so the shared between-construct confound cancels draw by draw.

  5. A construct-cluster bootstrap. The pair-level bootstrap resamples
     transcript-construct pairs, so its interval is conditional on the 24
     constructs actually observed and says nothing about a new guide. The
     cluster bootstrap resamples CONSTRUCTS with replacement, keeping every
     pair belonging to a sampled construct, which is the interval that
     supports a claim about constructs in general. Both are reported and
     labelled, and only the cluster interval is allowed to carry a
     generalising claim.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
import pandas as pd                                             # noqa: E402
from scipy.stats import mannwhitneyu, rankdata, spearmanr                 # noqa: E402
from riscpool import calibration, real_experiments as R, runner  # noqa: E402
from riscpool.features import load_features, transcript_level    # noqa: E402
from riscpool.hela import load_abundance                         # noqa: E402
from riscpool.offtarget import (construct_response,              # noqa: E402
                                load_candidates, load_response)
from riscpool.sirna import per_construct                         # noqa: E402

RHOS = [1e-3, 1e-2, 0.1, 0.5, 2.0, 10.0]
CLASSES = ["6mer", "7mer-A1", "7mer-m8", "8mer"]
CANONICAL_ORDER = ["8mer", "7mer-m8", "7mer-A1", "6mer"]   # strongest first
N_BOOT = 2000
N_PERM = 1000
N_CLUSTER_BOOT = 2000
MIN_N = 10


def median_ci(v, rng, n_boot=N_BOOT):
    v = np.asarray(v, dtype=float)
    v = v[np.isfinite(v)]
    if v.size < 3:
        return float("nan"), [float("nan")] * 2
    idx = rng.integers(0, v.size, (n_boot, v.size))
    meds = np.median(v[idx], axis=1)
    return float(np.median(v)), [float(np.percentile(meds, 2.5)),
                                 float(np.percentile(meds, 97.5))]


def diff_ci(a, b, rng, n_boot=N_BOOT):
    """Bootstrap interval for median(a) - median(b), resampled independently."""
    a = np.asarray(a, float)[np.isfinite(a)]
    b = np.asarray(b, float)[np.isfinite(b)]
    if a.size < 3 or b.size < 3:
        return float("nan"), [float("nan")] * 2
    ia = rng.integers(0, a.size, (n_boot, a.size))
    ib = rng.integers(0, b.size, (n_boot, b.size))
    d = np.median(a[ia], axis=1) - np.median(b[ib], axis=1)
    return float(np.median(a) - np.median(b)), [
        float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))]


def strongest_class(row):
    for c, col in (("8mer", "n_8mer"), ("7mer-m8", "n_7mer_m8"),
                   ("7mer-A1", "n_7mer_A1"), ("6mer", "n_6mer")):
        if row.get(col, 0) > 0:
            return c
    return "none"


def fn(seed=0):
    rng = np.random.default_rng(seed)
    feats = load_features()
    scale = calibration.build_scale(feats)
    Cs = scale["K_scale_constant_C"]
    n_mrna = scale["mrna_molecules_per_cell"]

    tx = transcript_level()
    tx = tx[np.isfinite(tx.K_transcript) & (tx.K_transcript > 0)].copy()
    tx["K_transcript"] = tx.K_transcript * Cs
    ab = load_abundance()[["transcript_id", "x_rel"]]
    tx = tx.drop(columns=["x_rel"]).merge(ab, on="transcript_id", how="left")
    tx["x_rel"] = tx.x_rel.fillna(0.0) * n_mrna
    tx = tx[tx.x_rel > 0]
    tx["strongest_class"] = tx.apply(strongest_class, axis=1)

    resp = load_response()
    cand = load_candidates()
    pc = per_construct()
    gene_of = dict(zip(pc.construct, pc.target_gene))
    constructs = sorted(pc.construct)
    universe = set(cand.gene_symbol)

    # ---------------- 1. site-class medians, two assignment rules ----------
    frames, per_construct_rows = [], []
    for c in constructs:
        d = tx[(tx.construct == c) & (tx.gene_symbol != gene_of.get(c))]
        meas = construct_response(resp, c)[["gene_symbol", "value"]]
        meas = meas[meas.gene_symbol.isin(universe)]
        hit = set(d.gene_symbol)
        no = meas[~meas.gene_symbol.isin(hit)]
        m = d.merge(meas, on="gene_symbol", how="inner")
        if len(no) < 50 or len(m) < 20:
            continue
        m = m.assign(construct=c)
        frames.append(m[["construct", "gene_symbol", "value", "site_class",
                         "strongest_class"]])
        row = {"construct": c, "n_no_site": int(len(no)),
               "median_no_site": float(no.value.median())}
        for rule, col in (("best_ddG", "site_class"),
                          ("canonical_strongest", "strongest_class")):
            for cl in CLASSES:
                s = m.loc[m[col] == cl, "value"]
                if len(s) < MIN_N:
                    continue
                med, ci = median_ci(s.to_numpy(), rng, 500)
                row[f"{rule}.{cl}.n"] = int(len(s))
                row[f"{rule}.{cl}.median"] = med
                row[f"{rule}.{cl}.ci95"] = ci
                row[f"{rule}.{cl}.p_mw_less"] = float(mannwhitneyu(
                    s, no.value, alternative="less").pvalue)
            a = m.loc[m[col] == "7mer-A1", "value"].to_numpy()
            b = m.loc[m[col] == "7mer-m8", "value"].to_numpy()
            if len(a) >= MIN_N and len(b) >= MIN_N:
                dd, dci = diff_ci(b, a, rng, 500)
                row[f"{rule}.inversion_m8_minus_A1"] = dd
                row[f"{rule}.inversion_ci95"] = dci
                row[f"{rule}.inverted"] = bool(dd > 0)
        per_construct_rows.append(row)
    P = pd.concat(frames, ignore_index=True)

    pooled_classes = {}
    for rule, col in (("best_ddG", "site_class"),
                      ("canonical_strongest", "strongest_class")):
        out = {}
        for cl in CLASSES:
            v = P.loc[P[col] == cl, "value"].to_numpy()
            med, ci = median_ci(v, rng)
            out[cl] = {"n": int(v.size), "median_log10ratio": med,
                       "median_ci95": ci,
                       "mean_log10ratio": float(np.mean(v)) if v.size else
                       float("nan")}
        obs = [out[c]["median_log10ratio"] for c in CANONICAL_ORDER]
        a = P.loc[P[col] == "7mer-A1", "value"].to_numpy()
        b = P.loc[P[col] == "7mer-m8", "value"].to_numpy()
        dd, dci = diff_ci(b, a, rng)
        n_inv = sum(1 for r in per_construct_rows
                    if r.get(f"{rule}.inverted") is True)
        n_test = sum(1 for r in per_construct_rows
                     if f"{rule}.inverted" in r)
        out["_summary"] = {
            "assignment_rule": rule,
            "canonical_order_checked": CANONICAL_ORDER,
            "medians_in_canonical_order": obs,
            "monotone_in_canonical_order": bool(
                all(obs[i] <= obs[i + 1] for i in range(len(obs) - 1))),
            "inversion_median_7merm8_minus_7merA1": dd,
            "inversion_ci95": dci,
            "inversion_significant_at_95": bool(dci[0] > 0 or dci[1] < 0),
            "inversion_direction": ("7mer-A1 more repressed than 7mer-m8"
                                    if dd > 0 else
                                    "canonical: 7mer-m8 more repressed"),
            "n_constructs_showing_inversion": n_inv,
            "n_constructs_tested": n_test,
        }
        pooled_classes[rule] = out

    # ------------- 2-5. null, bootstrap, paired test, cluster bootstrap ----
    pooled_stats = []
    dependence = None
    for rho in RHOS:
        parts = []
        for c in constructs:
            tgt = gene_of.get(c) or "MAPK14"
            d = R.score_construct(c, rho, n_mrna, target_gene=tgt, tx=tx)
            if d is None:
                continue
            meas = construct_response(resp, c)[["gene_symbol", "value"]]
            m = d.merge(meas, on="gene_symbol", how="inner")
            m = m[np.isfinite(m.value)]
            if len(m) < 20:
                continue
            parts.append(m[["gene_symbol", "value",
                            "bound_frac_equilibrium",
                            "bound_frac_independent"]].assign(construct=c))
        if not parts:
            continue
        Q = pd.concat(parts, ignore_index=True)
        y = Q.value.to_numpy()
        cons_arr = Q.construct.to_numpy()
        uniq = list(pd.unique(cons_arr))
        groups = [np.where(cons_arr == c)[0] for c in uniq]
        A = {"equilibrium": Q.bound_frac_equilibrium.to_numpy(),
             "independent": Q.bound_frac_independent.to_numpy()}
        row = {"rho": rho, "n_pairs_pooled": int(len(Q)),
               "n_constructs": len(groups)}

        if dependence is None:
            # the same gene appears under many constructs, so the pooled
            # pairs are not independent observations even before the
            # construct-level clustering is considered. Reported as a
            # diagnostic: it is the reason the cluster bootstrap, which
            # resamples whole constructs and therefore carries a gene's
            # repeated appearances together, is the interval to trust.
            vc = Q.gene_symbol.value_counts()
            dependence = {
                "n_pairs": int(len(Q)),
                "n_distinct_genes": int(vc.size),
                "mean_constructs_per_gene": float(vc.mean()),
                "max_constructs_per_gene": int(vc.max()),
                "frac_pairs_whose_gene_appears_more_than_once": float(
                    (vc[vc > 1].sum()) / len(Q)),
                "note": (
                    "pooled pairs are clustered twice over: by construct, "
                    "and by gene, because one gene is measured under many "
                    "constructs. The pair-level bootstrap ignores both. The "
                    "construct-cluster bootstrap resamples whole constructs "
                    "and so respects the construct clustering and carries "
                    "each gene's repeated appearances together with the "
                    "construct that produced them; it does not remove the "
                    "residual gene-level dependence ACROSS distinct "
                    "constructs, which would need a crossed random-effects "
                    "model that 24 constructs cannot support."),
            }

        # ---- observed, pair-level bootstrap (CONDITIONAL), per-model null --
        # ranks are computed once: permuting y within a construct permutes
        # the pooled ranks of that construct's rows among themselves, so a
        # Spearman under permutation is a Pearson correlation of fixed
        # predictor ranks against permuted response ranks.
        ry = rankdata(y)
        rA = {t: rankdata(v) for t, v in A.items()}
        ry_c = ry - ry.mean()
        den_y = float(np.sqrt(ry_c @ ry_c))
        rA_c = {t: (v - v.mean()) for t, v in rA.items()}
        den_A = {t: float(np.sqrt(v @ v)) for t, v in rA_c.items()}

        for tag in ("equilibrium", "independent"):
            a = A[tag]
            row[f"pooled_spearman_{tag}"] = float(spearmanr(a, y).statistic)
            # the permutation loop below computes Spearman as a Pearson
            # correlation of precomputed ranks, which is the same statistic
            # only if the tie handling agrees. Checked here rather than
            # assumed, on the unpermuted data, and recorded.
            row[f"rank_pearson_identity_abs_err_{tag}"] = abs(
                float(rA_c[tag] @ ry_c) / (den_A[tag] * den_y)
                - row[f"pooled_spearman_{tag}"])
            bs = np.empty(N_BOOT)
            n = len(Q)
            for i in range(N_BOOT):
                ix = rng.integers(0, n, n)
                bs[i] = spearmanr(a[ix], y[ix]).statistic
            row[f"pair_bootstrap_ci95_{tag}_CONDITIONAL"] = [
                float(np.nanpercentile(bs, 2.5)),
                float(np.nanpercentile(bs, 97.5))]
            row[f"pair_bootstrap_sd_{tag}_CONDITIONAL"] = float(
                np.nanstd(bs, ddof=1))

        # ---- the paired permutation: ONE shuffle, both models -------------
        perm = {"equilibrium": np.empty(N_PERM),
                "independent": np.empty(N_PERM)}
        perm_delta = np.empty(N_PERM)
        for i in range(N_PERM):
            rp = ry.copy()
            for g in groups:               # shuffle within construct
                rp[g] = rng.permutation(rp[g])
            rp = rp - rp.mean()
            dp = float(np.sqrt(rp @ rp))
            for tag in ("equilibrium", "independent"):
                perm[tag][i] = float(rA_c[tag] @ rp) / (den_A[tag] * dp)
            perm_delta[i] = perm["equilibrium"][i] - perm["independent"][i]

        for tag in ("equilibrium", "independent"):
            pv = perm[tag]
            lo, hi = (float(np.nanpercentile(pv, 2.5)),
                      float(np.nanpercentile(pv, 97.5)))
            mu = float(np.nanmean(pv))
            sd = float(np.nanstd(pv, ddof=1))
            obs = row[f"pooled_spearman_{tag}"]
            row[f"permutation_null_ci95_{tag}"] = [lo, hi]
            row[f"permutation_null_mean_{tag}"] = mu
            row[f"permutation_null_sd_{tag}"] = sd
            row[f"observed_outside_null_envelope_{tag}"] = bool(
                obs < lo or obs > hi)
            # The null is NOT centred on zero. Permuting within construct
            # keeps each construct's own response distribution, so any
            # between-construct structure survives the shuffle and shows up
            # as a non-zero expected pooled correlation. A two-sided p built
            # on |perm| >= |obs| would silently assume a zero-centred null
            # and is meaningless here; the test has to be about the null's
            # own centre.
            row[f"permutation_p_two_sided_about_null_mean_{tag}"] = float(
                (np.sum(np.abs(pv - mu) >= abs(obs - mu)) + 1)
                / (N_PERM + 1))
            row[f"z_vs_permutation_null_{tag}"] = float((obs - mu) / sd) \
                if sd > 0 else float("nan")
            # the association net of its own baseline, which is the only
            # quantity comparable between two models with different nulls
            row[f"null_centred_association_{tag}"] = obs - mu

        gap = (row["pooled_spearman_equilibrium"]
               - row["pooled_spearman_independent"])
        row["equilibrium_minus_independent"] = gap
        mu_d = float(np.nanmean(perm_delta))
        sd_d = float(np.nanstd(perm_delta, ddof=1))
        row["paired_permutation_null_mean_gap"] = mu_d
        row["paired_permutation_null_sd_gap"] = sd_d
        row["paired_permutation_null_ci95_gap"] = [
            float(np.nanpercentile(perm_delta, 2.5)),
            float(np.nanpercentile(perm_delta, 97.5))]
        row["observed_gap_minus_paired_null_mean"] = gap - mu_d
        row["paired_permutation_p_two_sided_about_null_mean"] = float(
            (np.sum(np.abs(perm_delta - mu_d) >= abs(gap - mu_d)) + 1)
            / (N_PERM + 1))
        row["paired_z_vs_permutation_null"] = (
            float((gap - mu_d) / sd_d) if sd_d > 0 else float("nan"))
        row["paired_observed_outside_null_envelope"] = bool(
            gap < row["paired_permutation_null_ci95_gap"][0]
            or gap > row["paired_permutation_null_ci95_gap"][1])
        row["null_centred_difference"] = (
            row["null_centred_association_equilibrium"]
            - row["null_centred_association_independent"])

        # ---- construct-cluster bootstrap ---------------------------------
        cb = {"equilibrium": np.empty(N_CLUSTER_BOOT),
              "independent": np.empty(N_CLUSTER_BOOT)}
        cb_delta = np.empty(N_CLUSTER_BOOT)
        ng = len(groups)
        for i in range(N_CLUSTER_BOOT):
            pick = rng.integers(0, ng, ng)
            ix = np.concatenate([groups[k] for k in pick])
            yy = y[ix]
            for tag in ("equilibrium", "independent"):
                cb[tag][i] = spearmanr(A[tag][ix], yy).statistic
            cb_delta[i] = cb["equilibrium"][i] - cb["independent"][i]
        for tag in ("equilibrium", "independent"):
            row[f"cluster_bootstrap_ci95_{tag}"] = [
                float(np.nanpercentile(cb[tag], 2.5)),
                float(np.nanpercentile(cb[tag], 97.5))]
            row[f"cluster_bootstrap_sd_{tag}"] = float(
                np.nanstd(cb[tag], ddof=1))
        row["cluster_bootstrap_ci95_gap"] = [
            float(np.nanpercentile(cb_delta, 2.5)),
            float(np.nanpercentile(cb_delta, 97.5))]
        row["cluster_bootstrap_median_gap"] = float(np.nanmedian(cb_delta))
        row["cluster_bootstrap_gap_excludes_zero"] = bool(
            np.nanpercentile(cb_delta, 2.5) > 0
            or np.nanpercentile(cb_delta, 97.5) < 0)
        row["cluster_bootstrap_n_resamples"] = N_CLUSTER_BOOT

        # Two flags, because they answer two different questions and at
        # some rho they disagree.
        #
        # The first is the significance criterion alone: a paired
        # permutation p below 0.05, a construct-cluster interval on the gap
        # that excludes zero, and a gap in the direction of better
        # prediction. It says the difference is not attributable to sampling
        # or to the shared between-construct baseline.
        #
        # The second additionally asks whether the difference is large
        # enough to be worth anything. The scale it is measured against is
        # not invented: it is the construct-cluster standard error of the
        # equilibrium association itself, so the requirement is that
        # coupling move the association by at least as much as the
        # association is itself uncertain across constructs. Without that,
        # a difference of 1e-4 in Spearman passes the significance criterion
        # at high rho purely because the paired null has almost no spread
        # there, which is the regime where the limit theorem says the two
        # models coincide and a vanishing difference is expected.
        net = gap - mu_d
        row["paired_net_gap"] = net
        row["cluster_se_equilibrium_association"] = row[
            "cluster_bootstrap_sd_equilibrium"]
        row["paired_net_gap_over_cluster_se"] = (
            net / row["cluster_bootstrap_sd_equilibrium"]
            if row["cluster_bootstrap_sd_equilibrium"] > 0 else float("nan"))
        row["paired_and_cluster_criteria_met"] = bool(
            row["paired_permutation_p_two_sided_about_null_mean"] < 0.05
            and row["cluster_bootstrap_gap_excludes_zero"]
            and net < 0)
        row["improvement_exceeds_one_cluster_se"] = bool(
            row["paired_and_cluster_criteria_met"]
            and abs(net) >= row["cluster_bootstrap_sd_equilibrium"])
        pooled_stats.append(row)

    met = [q["rho"] for q in pooled_stats
           if q["paired_and_cluster_criteria_met"]]
    material = [q["rho"] for q in pooled_stats
                if q["improvement_exceeds_one_cluster_se"]]
    # where the two scorings differ most is where an improvement, if there
    # were one, would be visible; the sign of the net gap there is the
    # single most informative number in this block
    widest = min(pooled_stats, key=lambda q: q["equilibrium_minus_independent"])

    return {
        "sign_convention": ("measured VALUE = log10(siRNA/mock); repression "
                            "is NEGATIVE, so a working predictor of bound "
                            "fraction gives a NEGATIVE Spearman"),
        "n_bootstrap": N_BOOT, "n_permutations": N_PERM,
        "min_n_per_class": MIN_N,
        "rho_values": RHOS,
        "class_assignment_rules": {
            "best_ddG": "the class of the transcript's lowest-ddG site, which "
                        "is what e7 used",
            "canonical_strongest": "the strongest class present on the "
                                   "transcript, 8mer > 7mer-m8 > 7mer-A1 > "
                                   "6mer"},
        "pooled_site_class": pooled_classes,
        "per_construct_site_class": per_construct_rows,
        "n_constructs_analysed": len(per_construct_rows),
        "n_cluster_bootstrap": N_CLUSTER_BOOT,
        "pooled_spearman_with_null_and_ci": pooled_stats,
        "pooled_pair_dependence_diagnostic": dependence,
        "rho_values_meeting_paired_and_cluster_criteria": met,
        "rho_values_where_improvement_exceeds_one_cluster_se": material,
        "EQUILIBRIUM_ADDS_ESTABLISHED_PREDICTIVE_VALUE": bool(material),
        "max_abs_net_gap_where_criteria_met": (
            max(abs(q["paired_net_gap"]) for q in pooled_stats
                if q["paired_and_cluster_criteria_met"]) if met else None),
        "rho_where_scorings_differ_most": widest["rho"],
        "net_gap_where_scorings_differ_most": widest["paired_net_gap"],
        "net_gap_sign_where_scorings_differ_most": (
            "independent better" if widest["paired_net_gap"] > 0
            else "equilibrium better"),
        "effect_size_note": (
            "the criteria in rho_values_meeting_paired_and_cluster_criteria "
            "are the significance criteria alone. They are met only at the "
            "large rho values where the limit theorem makes the two scorings "
            "converge, so the difference they certify is tiny, and the "
            "paired null has almost no spread there, which is why a "
            "negligible difference reaches a small p. "
            "EQUILIBRIUM_ADDS_ESTABLISHED_PREDICTIVE_VALUE additionally "
            "requires the difference to be at least one construct-cluster "
            "standard error of the equilibrium association itself. At the "
            "rho where the two scorings differ most, the net gap after "
            "removing the paired baseline is reported above with its sign; a "
            "positive value there means independent scoring predicts "
            "better, not worse."),
        "paired_test_note": (
            "the raw difference of two pooled Spearman correlations is not a "
            "test. The two models have different permutation-null baselines "
            "because pooling constructs leaves a between-construct "
            "correlation that a within-construct shuffle cannot remove, and "
            "that baseline is not the same for the two scorings, so most of "
            "a raw gap can be baseline rather than skill. The paired test "
            "applies ONE within-construct permutation to both models and "
            "differences the two correlations under that same shuffle, so "
            "the shared confound cancels. "
            "EQUILIBRIUM_IMPROVES_PREDICTION_AT_ANY_RHO is true only if, at "
            "some rho, the paired permutation p is below 0.05, the "
            "construct-cluster interval on the gap excludes zero, and the "
            "gap is in the direction of better prediction (more negative, "
            "since repression is negative). Anything less than all three is "
            "reported as no established improvement."),
        "bootstrap_scope_note": (
            "two bootstraps are reported and they answer different "
            "questions. pair_bootstrap_* resamples transcript-construct "
            "pairs and is CONDITIONAL ON THE OBSERVED CONSTRUCTS: it "
            "describes sampling noise within this construct panel and must "
            "not be used to claim anything about a new guide. "
            "cluster_bootstrap_* resamples whole constructs with "
            "replacement, keeping every pair of a sampled construct, and is "
            "the interval that supports a statement about constructs in "
            "general. With 24 constructs it is wide, and that width is the "
            "honest one."),
        "permutation_null_note": (
            "measured values are permuted WITHIN construct, so the null "
            "keeps each construct's response distribution and the pooling "
            "structure and destroys only the transcript-level association. "
            "An observed correlation inside this envelope is not "
            "distinguishable from no association. Note the null is not "
            "centred on zero: pooling constructs whose predicted bound "
            "fractions and whose measured responses both differ "
            "systematically leaves a between-construct correlation that the "
            "shuffle cannot remove. That is a real confound in the pooled "
            "statistic, it is why the null is reported rather than assumed, "
            "and it is why the p-value here is two-sided about the null "
            "mean rather than about zero."),
    }


if __name__ == "__main__":
    runner.run("e7b_null_calibration", fn, seed=0)
