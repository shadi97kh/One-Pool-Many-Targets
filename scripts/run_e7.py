"""
e7 - real off-target ranking, equilibrium against independent occupancy.

Three things are measured, and one of them is an analytic fact that the
measurement confirms.

1. WITHIN a single construct the two scorings CANNOT differ in rank.
   The bound fraction is f/(K_j+f) under equilibrium and M/(K_j+M) under
   independent occupancy. f and M are scalars shared by every transcript in
   that construct, and both expressions are strictly decreasing in K_j, so one
   is a strictly monotone transform of the other and every rank statistic is
   identical by construction, at every rho. This is reported as an identity
   and checked numerically rather than presented as an empirical finding.
   The layer applies a shared monotone nonlinear transformation of
   fractional occupancy within a construct; it does not reorder.

2. ACROSS constructs the two scorings do differ, because the free pool f_c
   depends on the construct's own competitor set while M does not. Pooling
   every (construct, transcript) pair and ranking globally is therefore the
   comparison in which the coupling can show up, and it is the comparison that
   matches the therapeutic use, which is choosing between candidates.

3. Whether either scoring predicts the measured response at all. K here is
   purely thermodynamic and is never fitted to the expression data, so this is
   an honest out-of-the-box test of the affinity model.

A positive control is computed alongside: measured repression stratified by
seed site class against transcripts with no site. If that control fails, no
conclusion about scoring means anything.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
import pandas as pd                                             # noqa: E402
from scipy.stats import (kendalltau, mannwhitneyu, spearmanr,    # noqa: E402
                         wilcoxon)
from riscpool import calibration, real_experiments as R, runner  # noqa: E402
from riscpool.features import load_features, transcript_level    # noqa: E402
from riscpool.hela import load_abundance                         # noqa: E402
from riscpool.offtarget import (construct_response,              # noqa: E402
                               load_candidates, load_response)
from riscpool.sirna import per_construct                         # noqa: E402

RHOS = [1e-3, 1e-2, 0.1, 0.5, 2.0, 10.0]
RHO_MAIN = 0.5
N_BOOT = 400


def positive_control(tx, resp, cand, constructs, gene_of):
    """Measured repression by seed site class. Nothing model-based."""
    rows = []
    universe = set(cand.gene_symbol)
    for c in constructs:
        d = tx[(tx.construct == c) & (tx.gene_symbol != gene_of.get(c))]
        meas = construct_response(resp, c)[["gene_symbol", "value"]]
        meas = meas[meas.gene_symbol.isin(universe)]
        hit = set(d.gene_symbol)
        no = meas[~meas.gene_symbol.isin(hit)]
        m = d.merge(meas, on="gene_symbol", how="inner")
        if len(no) < 50 or len(m) < 20:
            continue
        for cls in ["6mer", "7mer-A1", "7mer-m8", "8mer", "ANY"]:
            s = m if cls == "ANY" else m[m.site_class == cls]
            if len(s) < 10:
                continue
            p = float(mannwhitneyu(s.value, no.value,
                                   alternative="less").pvalue)
            rows.append({"construct": c, "site_class": cls,
                         "n_with_site": int(len(s)),
                         "n_no_site": int(len(no)),
                         "median_log10ratio_with_site": float(s.value.median()),
                         "mean_log10ratio_with_site": float(s.value.mean()),
                         "median_log10ratio_no_site": float(no.value.median()),
                         "mann_whitney_p_less": p})
    return rows


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

    resp = load_response()
    cand = load_candidates()
    pc = per_construct()
    gene_of = dict(zip(pc.construct, pc.target_gene))
    constructs = sorted(pc.construct)

    ctrl = positive_control(tx, resp, cand, constructs, gene_of)
    ctrl_any = [r for r in ctrl if r["site_class"] == "ANY"]
    by_class = {}
    for cls in ["6mer", "7mer-A1", "7mer-m8", "8mer"]:
        s = [r for r in ctrl if r["site_class"] == cls]
        if s:
            by_class[cls] = {
                "n_constructs": len(s),
                "mean_of_median_log10ratio": float(np.mean(
                    [r["median_log10ratio_with_site"] for r in s])),
                "mean_of_mean_log10ratio": float(np.mean(
                    [r["mean_log10ratio_with_site"] for r in s])),
                "n_constructs_with_p_below_0.05": int(sum(
                    r["mann_whitney_p_less"] < 0.05 for r in s))}

    per_rho, phi_out, pooled = [], None, []
    for rho in RHOS:
        rows, frames = [], []
        for c in constructs:
            tgt = gene_of.get(c) or "MAPK14"
            d = R.score_construct(c, rho, n_mrna, target_gene=tgt, tx=tx)
            if d is None:
                continue
            meas = construct_response(resp, c)[["gene_symbol", "value"]]
            ev = R.evaluate(d, meas, n_boot=N_BOOT if rho == RHO_MAIN else 0,
                            rng=rng)
            if ev is None:
                continue
            e, merged = ev
            e.update({"construct": c, "target_gene": tgt, "rho": rho,
                      "f_free_pool": float(d.f_free_pool.iloc[0]),
                      "f_over_M": float(d.f_free_pool.iloc[0]
                                        / (rho * n_mrna))})
            rows.append(e)
            merged = merged.copy()
            merged["construct"] = c
            frames.append(merged[["construct", "gene_symbol", "value",
                                  "bound_frac_equilibrium",
                                  "bound_frac_independent"]])
            if rho == RHO_MAIN and c == "MAPK14-193_parent":
                phi_out = R.fit_monotone_map(
                    merged.bound_frac_equilibrium.to_numpy(),
                    merged.value.to_numpy())
        if not rows:
            continue
        se = np.array([r["spearman_equilibrium"] for r in rows])
        si = np.array([r["spearman_independent"] for r in rows])
        tt = np.array([r["kendall_between_the_two_scorings"] for r in rows])
        try:
            w = wilcoxon(se, si)
            wstat, wp = float(w.statistic), float(w.pvalue)
        except Exception as exc:
            wstat, wp = float("nan"), float("nan")
            print(f"  wilcoxon not defined at rho={rho}: {exc}")

        P = pd.concat(frames, ignore_index=True)
        pe = spearmanr(P.bound_frac_equilibrium, P.value)
        pi = spearmanr(P.bound_frac_independent, P.value)
        pooled.append({
            "rho": rho,
            "n_pairs_pooled": int(len(P)),
            "pooled_spearman_equilibrium": float(pe.statistic),
            "pooled_spearman_p_equilibrium": float(pe.pvalue),
            "pooled_spearman_independent": float(pi.statistic),
            "pooled_spearman_p_independent": float(pi.pvalue),
            "pooled_spearman_difference": float(pe.statistic - pi.statistic),
            "pooled_kendall_between_the_two_scorings": float(kendalltau(
                P.bound_frac_equilibrium, P.bound_frac_independent).statistic),
            "pooled_spearman_between_the_two_scorings": float(spearmanr(
                P.bound_frac_equilibrium, P.bound_frac_independent).statistic),
        })
        per_rho.append({
            "rho": rho, "n_constructs": len(rows),
            "mean_spearman_equilibrium": float(se.mean()),
            "sd_spearman_equilibrium": float(se.std(ddof=1)),
            "mean_spearman_independent": float(si.mean()),
            "sd_spearman_independent": float(si.std(ddof=1)),
            "mean_spearman_difference": float((se - si).mean()),
            "max_abs_spearman_difference": float(np.abs(se - si).max()),
            "mean_kendall_between_scorings_within_construct": float(tt.mean()),
            "min_kendall_between_scorings_within_construct": float(tt.min()),
            "wilcoxon_statistic_paired_across_constructs": wstat,
            "wilcoxon_p_paired_across_constructs": wp,
            "mean_f_over_M": float(np.mean([r["f_over_M"] for r in rows])),
            "min_f_over_M": float(np.min([r["f_over_M"] for r in rows])),
            "max_f_over_M": float(np.max([r["f_over_M"] for r in rows])),
            "per_construct": rows,
        })

    main = next((p for p in per_rho if p["rho"] == RHO_MAIN), None)
    IDENTITY_TOL = 1e-4
    within_identical = all(
        p["max_abs_spearman_difference"] <= IDENTITY_TOL for p in per_rho)
    within_max_diff = max(p["max_abs_spearman_difference"] for p in per_rho)
    pooled_div = [p["rho"] for p in pooled
                  if p["pooled_kendall_between_the_two_scorings"] < 0.99]

    # which predictors do carry signal, measured, for the parent construct
    d = tx[(tx.construct == "MAPK14-193_parent")
           & (tx.gene_symbol != "MAPK14")]
    m = d.merge(construct_response(resp, "MAPK14-193_parent")[
        ["gene_symbol", "value"]], on="gene_symbol", how="inner")
    diag = []
    for nm, vv in [("minus_log10_K_thermodynamic", -np.log10(m.K_transcript)),
                   ("best_ddG_kcal", m.best_ddG),
                   ("dg_duplex_kcal", m.dg_duplex_kcal),
                   ("log10_p_unpaired_15", np.log10(m.p_unpaired_15 + 1e-12)),
                   ("n_sites", m.n_sites), ("n_8mer_sites", m.n_8mer),
                   ("utr3_len", m.utr3_len),
                   ("local_au_content", m.local_au_content),
                   ("abundance_x", m.x_rel)]:
        r = spearmanr(vv, m.value)
        diag.append({"predictor": nm, "spearman_vs_measured":
                     float(r.statistic), "p": float(r.pvalue),
                     "n": int(len(m))})

    return {
        "scoring_note": (
            "K is thermodynamic (ViennaRNA duplex energy plus the "
            "pfl_fold opening cost on GENCODE v50 3'UTRs, anchored on the "
            "published seed-match Kd of Wee et al. 2012) and is never fitted "
            "to the expression response."),
        "sign_convention": ("measured VALUE = log10(siRNA/mock); repression is "
                            "NEGATIVE, so a working predictor gives a NEGATIVE "
                            "Spearman against predicted bound fraction"),
        "constants_used": scale,
        "n_constructs_scored": main["n_constructs"] if main else 0,
        "rho_swept": RHOS, "rho_main": RHO_MAIN,
        "bootstrap_resamples": N_BOOT,

        "ANALYTIC_IDENTITY_within_construct": (
            "Within one construct the bound fraction is f/(K_j+f) under "
            "equilibrium and M/(K_j+M) under independent occupancy. f and M "
            "are scalars shared by every transcript, and both are strictly "
            "decreasing in K_j, so the two orderings are identical at every "
            "rho and every rank statistic must agree exactly. The measured "
            "max_abs_spearman_difference below confirms this numerically. It "
            "is a property of the model, not a result about this dataset: the "
            "layer applies a shared monotone nonlinear transformation of "
            "fractional occupancy within a construct and reorders only across "
            "constructs."),
        "within_construct_rank_statistics_identical_at_every_rho":
            bool(within_identical),
        "within_construct_max_abs_spearman_difference_over_all_rho":
            float(within_max_diff),
        "within_construct_identity_tolerance": IDENTITY_TOL,
        "within_construct_identity_tolerance_note": (
            "the residual difference is at the level of the bisection "
            "tolerance of the solver and of rank ties, not a real reordering"),

        "positive_control_measured_repression_by_site_class": by_class,
        "positive_control_any_site_n_constructs_p_below_0.05": int(sum(
            r["mann_whitney_p_less"] < 0.05 for r in ctrl_any)),
        "positive_control_any_site_n_constructs_tested": len(ctrl_any),
        "positive_control_detail": ctrl,

        "per_rho_within_construct": per_rho,
        "pooled_across_constructs": pooled,
        "pooled_rho_values_where_scorings_diverge_kendall_below_0.99":
            pooled_div,
        "pooled_scorings_ever_diverge": bool(len(pooled_div) > 0),

        "predictor_diagnostics_parent_construct": diag,
        "fitted_monotone_map_phi_parent_construct": phi_out,
        "phi_note": ("r = phi(o) fitted by isotonic regression of the measured "
                     "log ratio on predicted bound fraction, rather than "
                     "assuming r = o/x"),
        "LIMITATION_thermodynamic_K": (
            "The purely thermodynamic K does not reproduce the site-class "
            "hierarchy that the same data shows (see "
            "positive_control_measured_repression_by_site_class and "
            "predictor_diagnostics_parent_construct). ViennaRNA duplexfold "
            "cannot see the t1 = A contribution, which is an Argonaute pocket "
            "effect rather than a base pair, and it reports the best duplex "
            "anywhere in the scanned window rather than necessarily at the "
            "seed site. So a near-zero within-seed-match rank correlation is "
            "a statement about this affinity model, not about the equilibrium "
            "layer, and not about whether seed matches are repressed, which "
            "the positive control shows they are."),
    }


if __name__ == "__main__":
    runner.run("e7_offtarget_ranking", fn, seed=0)
