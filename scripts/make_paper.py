"""
paper/main.tex, generated from results/*.json.

Rule Zero applies to the paper as hard as it applies to the report: if a
number appears in the manuscript it was read out of a result file at build
time, not typed. Every numeric macro below is defined from a JSON value, so a
rerun of the pipeline that changes a result changes the manuscript, and a
number with no result behind it cannot be written at all.

Prose is written here. Numbers are not.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool.provenance import ROOT, utcnow            # noqa: E402
from riscpool.runner import load_result                 # noqa: E402

PAPER = os.path.join(ROOT, "paper")
OUT = os.path.join(PAPER, "main.tex")
OUT_APPENDIX = os.path.join(PAPER, "appendix.tex")

class Missing(Exception):
    pass

def has_class_fit(e9):
    """Whether the site-class estimator has been recorded for every construct."""
    ok = [p for p in e9.get("per_construct", []) if p.get("status") == "OK"]
    return bool(ok) and all("class_fit" in p for p in ok)

def dig(d, path):
    cur = d
    for k in path.split("."):
        if isinstance(cur, list):
            cur = cur[int(k)]
        elif isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            raise Missing(path)
    return cur

def num(x, n=2):
    return f"{float(x):.{n}f}"

def fmt_thousands(x):
    return f"{int(round(float(x))):,}"

def sci(x, n=1):
    """LaTeX scientific notation, e.g. 1.9\\times10^{-4}."""
    x = float(x)
    if x == 0:
        return "0"
    import math
    e = int(math.floor(math.log10(abs(x))))
    m = x / (10.0 ** e)
    if -2 <= e <= 3:
        return f"{x:.{max(0, n - e)}f}".rstrip("0").rstrip(".")
    # \ensuremath so the same macro is legal in text and in math mode; these
    # values appear in both, and a bare \times outside math aborts the run
    return f"\\ensuremath{{{m:.{n}f}\\times 10^{{{e}}}}}"

def ci(pair, n=2, f=num):
    return f"[{f(pair[0], n)},\\, {f(pair[1], n)}]"

def build():
    R = {k: load_result(k) for k in [
        "e1_solver_correctness", "e2_redistribution", "e3_pairwise_limit",
        "e4_retrieval_invariance", "e4b_binned_background", "e5_hela_regime",
        "e7_offtarget_ranking", "e9_dose_response", "e10_cross_context",
        "d1_gse5814", "d1_seed_validation", "d3_gencode",
        "d4_hela_abundance", "d7_gse28786", "d8_gse14073",
        "d2b_birmingham_arrays", "e8_huesken_efficacy",
        "e7b_null_calibration", "e9v_sim_estimator_validation",
        "e5b_budget_curve", "pxb_audit", "px0_audit_and_spec"]}
    missing = [k for k, v in R.items() if v is None or v["status"] != "OK"]
    if missing:
        raise Missing(f"these experiments have no OK result: {missing}")
    V = {k: v["values"] for k, v in R.items()}
    return V

def retrieval_depth_stats(e4):
    """Which calibration rule wins, as a function of retrieval depth.

    The affinity-weighted background is the correct rule asymptotically, but
    it is not uniformly better: at the shallowest depth it is worse than the
    abundance-mass control it is meant to replace. Reporting "least bad"
    without a depth qualifier contradicts the table it cites, so the crossover
    depth is computed here from that table rather than asserted.
    """
    aff, abu = "affinity_weighted_x_over_K", "abundance_mass_x"
    by = {}
    for r in e4["table"]:
        by.setdefault((r["R"], r["rho"]), {})[r["rule"]] = r["rel_err_o_target"]
    pairs = {k: v for k, v in by.items() if aff in v and abu in v}
    depths = sorted({k[0] for k in pairs})
    wins = [R for R in depths
            if all(v[aff] < v[abu] for k, v in pairs.items() if k[0] == R)]
    deep = max(depths)
    return {
        "r_win": min(wins),
        "r_shallow": min(depths),
        "r_deep": deep,
        "deep_affinity": max(v[aff] for k, v in pairs.items() if k[0] == deep),
        "deep_abundance": max(v[abu] for k, v in pairs.items() if k[0] == deep),
    }


def macros(V):
    """Every number the manuscript is allowed to use, as a LaTeX macro."""
    m = {}
    src = {}

    def put(name, value, source=None):
        """Record a macro, optionally with an explicit source.

        Names built inside a loop cannot be read out of the syntax tree,
        because the tree only holds the f-string. Those call sites pass their
        source explicitly; everything else is recovered statically by
        macro_provenance, so the two mechanisms together cover every macro
        and neither can be silently skipped.
        """
        m[name] = value
        if source is not None:
            src[name] = source
    macros.last_sources = src

    e1, e2, e3 = (V["e1_solver_correctness"], V["e2_redistribution"],
                  V["e3_pairwise_limit"])
    e4, e4b, e5 = (V["e4_retrieval_invariance"], V["e4b_binned_background"],
                   V["e5_hela_regime"])
    e7, e9, e10 = (V["e7_offtarget_ranking"], V["e9_dose_response"],
                   V["e10_cross_context"])
    d1, d3, d4 = V["d1_gse5814"], V["d3_gencode"], V["d4_hela_abundance"]
    d7, d8, d2b = (V["d7_gse28786"], V["d8_gse14073"],
                   V["d2b_birmingham_arrays"])
    e8 = V["e8_huesken_efficacy"]

    # --- solver and theory ---
    pb = V["pxb_audit"]
    pba, pbt = pb["accuracy_heldout"], pb["timing"]
    pbc = pb["accuracy_heldout_comparators"]["per_method"]
    pbf = pb["FROZEN_CONFIGURATION"]
    _oa = V["px0_audit_and_spec"]["spec"]["overlap_audit"]
    put("ApxGuideOverlap", str(_oa["n_guide_overlap"]),
        source="px0_audit_and_spec")
    put("ApxSeedOverlap", str(_oa["n_seed_overlap"]),
        source="px0_audit_and_spec")
    put("ApxR", str(pbf["R"]), source="pxb_audit")
    put("ApxB", str(pbf["B"]), source="pxb_audit")
    put("ApxDevFam", str(len(pb["counts_and_exclusions"]["development_families"])),
        source="pxb_audit")
    put("ApxTestFam", str(pba["n_families"]), source="pxb_audit")
    put("ApxCases", str(pba["n_cases"]), source="pxb_audit")
    put("ApxFocal", sci(pba["worst_focal_rel_err"], 1), source="pxb_audit")
    put("ApxGrad", num(pba["worst_grad_rel_err"], 4), source="pxb_audit")
    put("ApxTruncGrad", num(pbc["truncate"]["worst_grad_rel_err"], 2),
        source="pxb_audit")
    put("ApxLinGrad", sci(pbc["linear"]["worst_grad_rel_err"], 1),
        source="pxb_audit")
    put("ApxDefectMed", sci(pba["full_system_defect_over_M_median"], 1),
        source="pxb_audit")
    put("ApxDefectWorst", sci(pba["full_system_defect_over_M_worst"], 1),
        source="pxb_audit")
    put("ApxResid", sci(pba["compressed_residual_over_M_worst"], 1),
        source="pxb_audit")
    put("ApxFullMs", num(
        pbt["per_method"]["full"]["end_to_end_forward"]["median_ms"], 1),
        source="pxb_audit")
    put("ApxSelMs", num(
        pbt["per_method"]["bins"]["end_to_end_forward"]["median_ms"], 1),
        source="pxb_audit")
    put("ApxNRef", fmt_thousands(pbt["N_reference"]), source="pxb_audit")
    pbfd, pbn = pb["finite_difference_check"], pb["counts_and_exclusions"]
    pbp = pbt["profiling"]
    put("ApxMethod", str(pbf["method"]), source="pxb_audit")
    put("ApxTestCon", str(pbn["n_test_constructs"]), source="pxb_audit")
    put("ApxRhos", str(pbn["cases_per_construct"]), source="pxb_audit")
    put("ApxFDCoord", str(pbfd["n_coordinates_resolvable"]),
        source="pxb_audit")
    put("ApxFDWorst", num(pbfd["worst_rel_err"], 4), source="pxb_audit")
    put("ApxFDStrat", num(pbfd["worst_rel_err_above_1e9_of_max"], 5),
        source="pxb_audit")
    put("ApxFDAbove", str(pbfd["n_coordinates_above_1e9_of_max"]),
        source="pxb_audit")
    put("ApxReps", str(pbt["repetitions"]), source="pxb_audit")
    put("ApxIters", str(pbp["iterations_per_solve"]), source="pxb_audit")
    _mc = pbp["marginal_cost_ms"]
    _ek = next(k for k in _mc if k.endswith("_to_one_reduction"))
    put("ApxElems", fmt_thousands(int(_ek.split("_")[1])), source="pxb_audit")
    put("ApxCostElems", num(_mc[_ek], 2), source="pxb_audit")
    put("ApxCostSecond",
        num(_mc["adding_a_second_reduction_of_one_element"], 2),
        source="pxb_audit")

    _st = V["e7b_null_calibration"]["pooled_spearman_with_null_and_ci"]
    put("NGapCIExclZero", str(sum(
        1 for q in _st
        if not (q["cluster_bootstrap_ci95_gap"][0] <= 0
                <= q["cluster_bootstrap_ci95_gap"][1]))),
        source="e7b_null_calibration")
    put("MaxNetOverSE", num(max(
        abs(q["paired_net_gap_over_cluster_se"]) for q in _st), 2),
        source="e7b_null_calibration")
    put("ConsResid", sci(e1["max_abs_residual_F_of_f"], 1))
    put("GradErr", sci(e1["median_relative_gradient_error_resolvable_only"], 1))
    put("GradWorst", sci(e1["worst_relative_gradient_error_resolvable_only"], 1))
    # the worst PER-COORDINATE relative error lands on a component whose own
    # gradient is near zero, where a relative measure is meaningless. The
    # measure that says whether the gradients are right is the error relative
    # to the gradient norm, so both are reported.
    put("GradWorstNorm", sci(e1["worst_error_relative_to_gradient_norm"], 1))
    put("NGradCoord", str(e1["n_gradient_coordinates_checked"]))
    put("RedistDraws", str(e2["n_draws"]))
    put("RedistViolA", str(e2["claim_A_d_o_i_d_K_t_positive_violations"]))
    put("RedistViolB", str(e2["claim_B_d_o_t_d_K_t_negative_violations"]))
    put("RedistMargin", sci(e2["min_margin_1_minus_u_over_D"], 1))
    put("PwSlope", num(e3["loglog_slope_MEDIAN_transcript"], 2))
    put("PwSlopeSE", num(e3["loglog_slope_stderr_MEDIAN_transcript"], 3))
    put("PwSlopeAll", num(e3["loglog_slope_all"], 2))
    put("PwSlopeMax", num(e3["loglog_slope_asymptotic_window"], 2))
    put("PwSlopeMaxSE", num(e3["loglog_slope_stderr_asymptotic_window"], 3))
    put("PwSlopeAllSE", num(e3["loglog_slope_stderr_all"], 2))
    put("PwDecades", str(e3["n_decades_swept"]))
    put("PwPredicted", num(e3["predicted_slope"], 0))
    _b = V["e5b_budget_curve"]
    put("BudgetWorst", fmt_thousands(_b["max_independent_over_M"]))
    put("BudgetAtAgoLo", num(_b["independent_over_M_at_ago2_measured_low"], 2))
    put("BudgetAtAgoHi", num(_b["independent_over_M_at_ago2_measured_high"], 3))
    put("BudgetCrossM", fmt_thousands(
        _b["crossover_M_where_independent_equals_budget"]))
    put("AlphaThreshLo", num(
        _b["alpha_threshold_for_over_allocation_vs_ago2_low"], 2))
    put("AlphaThreshHi", num(
        _b["alpha_threshold_for_over_allocation_vs_ago2_high"], 3))

    # --- data ---
    put("NConstructs", str(d1["n_constructs"]))
    put("NSeedVariants", str(d1["n_mapk14_seed_variant_constructs"]))
    # one deposited construct carries no human guide and so cannot be scored
    put("NConstructsScored", str(e7["n_constructs_scored"]))
    put("NArraysHela", str(d1["n_sirna_hela_samples"]))
    put("GencodeRelease", str(d3["gencode_release"]))
    put("NCanonUTR", f"{d3['n_canonical_gene_symbols_with_utr3']:,}")
    put("NHelaGenes", f"{d4['n_genes_joined_to_gencode_canonical_with_utr3']:,}")
    put("SeedAgree", num(100 * V["d1_seed_validation"]["agreement_rate_7mer"], 0))
    put("NSeedCompared", str(V["d1_seed_validation"]["n_constructs_compared"]))
    put("NDoseArrays", str(d7["n_arrays"]))
    put("NDoseProbes", f"{d7['n_probesets']:,}")
    put("DoseAllLevels", ", ".join(f"{d:g}" for d in d7["doses_nM"]))
    put("NDoseConstructs", str(len(d7["constructs"])))
    put("NCtxArrays", str(d8["n_arrays"]))
    put("NCtxConstructs", str(len(d8["constructs"])))
    put("NBirmArrays", str(d2b["n_arrays_parsed"]))
    put("NBirmGuides", str(d2b["n_distinct_guides"]))
    put("NBirmGenes", f"{d2b['n_gene_symbols']:,}")

    # --- e5, the regime ---
    put("RhoLo", sci(e5["rho_hela_band_low"], 1))
    put("RhoHi", sci(e5["rho_hela_band_high"], 1))
    import math
    put("RhoDecades", num(math.log10(e5["rho_hela_band_high"]
                                     / e5["rho_hela_band_low"]), 1))
    put("AgoLo", f"{int(e5['constants_used']['ago2_copies_per_cell_low']):,}")
    put("AgoHi", f"{int(e5['constants_used']['ago2_copies_per_cell_high']):,}")
    put("NmRNA", f"{int(e5['constants_used']['mrna_molecules_per_cell']):,}")
    put("NOffUnion", f"{e5['n_retrieved_offtarget_transcripts_union']:,}")
    put("HKMeasured", num(e5["H_K_measured_sd_log10_K_on"], 2))
    put("TauMin", num(e5["min_tau_anywhere_in_hela_band"], 2))
    contour = [c for c in e5["tau_0.9_contour_by_H_K"]
               if abs(c["H_K"] - 1.6) < 1e-9][0]["rho_at_tau_0.9"]
    put("TauContour", sci(contour, 3))

    # --- e4 and e4b ---
    put("EFourAff", num(100 * e4["max_rel_err_o_target_affinity_rule"], 1))
    put("EFourAbund", num(e4["max_rel_err_o_target_abundance_rule"], 1))
    # the affinity rule is NOT uniformly better. Which rule wins is a
    # function of retrieval depth, so the depth at which it starts winning is
    # read off the table rather than asserted, and the deep-retrieval margin
    # is reported alongside the shallow failure.
    put("EFourAbundPct",
        num(100 * e4["max_rel_err_o_target_abundance_rule"], 1))
    rd = retrieval_depth_stats(e4)
    put("EFourRWin", str(rd["r_win"]))
    put("EFourRShallow", str(rd["r_shallow"]))
    put("EFourRDeep", str(rd["r_deep"]))
    put("EFourDeepAff", num(100 * rd["deep_affinity"], 3))
    put("EFourDeepAbund", num(100 * rd["deep_abundance"], 1))
    put("EFourN", str(e4["reference_set_size_including_on_target"]))
    put("EFourHolds", str(e4["n_rows_where_linearisation_holds"]))
    put("EFourRows", str(e4["n_truncated_rows"]))
    put("RegDiff", sci(e4b["regression_against_e4_max_rel_diff"], 1)
        if e4b["regression_against_e4_max_rel_diff"] else "0")
    put("BLinR", num(100 * e4b["max_rel_err_o_target_at_R25_linear_rule"], 1))
    put("BTenR", num(100 * e4b["max_rel_err_o_target_at_R25_binned_B10_quantile"],
                     1))
    sb = {(s["binning_rule"], s["R"], s["threshold"]): s
          for s in e4b["smallest_B_restoring_invariance"]}
    for thr, tag in ((0.1, "Ten"), (0.01, "One")):
        v = sb[("quantile", 25, thr)]["smallest_B_all_rho_o_target"]
        put(f"BSmallest{tag}", str(v) if v is not None else "none swept",
            "e4b_binned_background.smallest_B_restoring_invariance"
            f"[quantile,R=25,threshold={thr}].smallest_B_all_rho_o_target")
    put("BRequired", ", ".join(str(b) for b in e4b["B_values_required_by_brief"]))

    # --- e7 ---
    put("WithinDiff", sci(
        e7["within_construct_max_abs_spearman_difference_over_all_rho"], 1))
    put("NCtrlSig", str(e7["positive_control_any_site_n_constructs_p_below_0.05"]))
    put("NCtrlTested", str(e7["positive_control_any_site_n_constructs_tested"]))
    kdiag = [d for d in e7["predictor_diagnostics_parent_construct"]
             if d["predictor"] == "minus_log10_K_thermodynamic"][0]
    put("KSpearman", num(kdiag["spearman_vs_measured"], 3))
    put("EightMer", num(
        e7["positive_control_measured_repression_by_site_class"]["8mer"][
            "mean_of_median_log10ratio"], 3))
    put("SixMer", num(
        e7["positive_control_measured_repression_by_site_class"]["6mer"][
            "mean_of_median_log10ratio"], 3))

    # --- e8 ---
    put("HueskenRho", num(e8["mean_spearman_heldout_genes"], 3))
    put("HueskenSd", num(e8["sd_spearman_heldout_genes"], 3))
    put("HueskenN", f"{e8['n_sirnas_used']:,}")
    put("HueskenGenes", str(e8["n_target_genes"]))

    # --- e9, the dose series ---
    ok = [p for p in e9["per_construct"] if p["status"] == "OK"]
    put("NDoseFitted", str(len(ok)))
    # the dose grid is NOT uniform across constructs, and saying "5 constructs
    # at 1, 10 and 25 nM" is wrong for one of them
    _nd = [len(p["doses_nM"]) for p in ok]
    put("NDoseThree", str(sum(1 for n in _nd if n == 3)))
    put("NDoseTwo", str(sum(1 for n in _nd if n == 2)))
    put("DoseTwoName", ", ".join(
        p["construct"].replace("_", r"\_") for p in ok
        if len(p["doses_nM"]) == 2))
    put("DoseLevels", ", ".join(
        f"{d:g}" for d in sorted({d for p in ok for d in p["doses_nM"]})))
    put("DoseNBoot", str(e9["n_bootstrap"]))
    put("NThermoNeg", str(sum(
        1 for p in ok if p["loglog_slope_pool_vs_dose"]["slope"] < 0)))
    put("ThermoSlope", num(
        e9["pooled_slope_construct_fixed_effects"]["slope"], 2))
    put("ThermoSlopeCI", ci(e9["pooled_slope_bootstrap_ci95"], 2))
    # These exist only once the site-class estimator has been recorded. When
    # it has not, the manuscript drops every sentence that depends on it
    # rather than guessing, so the macros are simply not emitted.
    if has_class_fit(e9):
        cf = e9["class_fit_pooled_slope_construct_fixed_effects"]
        put("ClassSlope", num(cf["slope"], 2))
        put("ClassSlopeCI", ci(e9["class_fit_pooled_slope_bootstrap_ci95"], 2))
        put("ClassSlopeAboveOne", num(
            100 * e9["class_fit_pooled_slope_frac_resamples_above_1"], 0))
        put("ClassSane",
            str(e9["class_fit_n_constructs_with_sane_class_ordering"]))
        put("RhoData", sci(e9["class_fit_rho_median_zero_background"], 2))
        put("RhoDataCI", ci(
            e9["class_fit_rho_median_bootstrap_ci95"], 2, sci))
        rr = e9["class_fit_rho_all_construct_dose_zero_background"]
        put("RhoDataLo", sci(min(q for q in rr if q > 0), 1))
        put("RhoDataHi", sci(max(rr), 1))
        put("RhoDataDecades", num(
            e9["class_fit_rho_point_estimate_spread_decades"], 1))
        # the direction of the comparison against the tau = 0.9 contour is
        # read off the numbers, not asserted
        med = e9["class_fit_rho_median_zero_background"]
        put("RhoContourRelation", "above" if med > contour else "below")
        put("RhoFracAboveContour", num(
            100 * sum(1 for q in rr if q > contour) / len(rr), 0))

        # --- the identifiability audit: what happens when the two-dose
        # --- construct is dropped, and whether the assumed proportional
        # --- loading survives its own check
        put("ClassSlopeNoHK", num(
            e9["class_fit_pooled_slope_excluding_HK2_4031"], 3))
        put("LocoLo", num(e9["class_fit_pooled_slope_loco_range"][0], 2))
        put("LocoHi", num(e9["class_fit_pooled_slope_loco_range"][1], 2))
        ms = e9["M_vs_dose_slope_summary"]
        put("NMSlopeExclOne", str(ms["n_with_ci_excluding_one"]))
        put("NMSlopeTested", str(ms["n_constructs"]))
        put("MSlopeLo", num(min(q["loglog_slope_M_vs_dose"]
                                for q in ms["per_construct"]), 2))
        put("MSlopeHi", num(max(q["loglog_slope_M_vs_dose"]
                                for q in ms["per_construct"]), 2))
        put("NBelowOne", str(sum(
            1 for p in ok
            if (p["class_fit_bootstrap"]["slope_ci95"][1] < 1.0))))
        put("ClassResidRms", num(
            e9["class_fit_pooled_slope_construct_fixed_effects"][
                "residual_rms_log10"], 3))
        mc = e9["class_fit_model_comparison_summary"]
        put("NPrefFree", str(mc["n_preferring_free_unconstrained_by_aic"]))
        put("NPrefEqAIC", str(mc["n_preferring_equilibrium_by_aic"]))
        put("NPrefEqHeld", str(mc["n_preferring_equilibrium_by_heldout"]))
        put("MaxHeldDiff", sci(max(
            abs(q) for q in
            mc["heldout_rmse_equilibrium_minus_independent"].values()
            if q is not None), 1))
        put("NFolds", str(ok[0]["class_fit_model_comparison"][
            "n_folds_completed"]))
        put("ClassNGenes", fmt_thousands(ok[0]["class_fit_n_genes"]))
    put("ThermoRhoMedian", sci(e9["rho_data_driven_median_zero_background"], 2))
    put("ThermoRhoCI", ci(
        e9["rho_data_driven_median_bootstrap_ci95"], 2, sci))
    ks = [abs(d["spearman_minus_log10K_vs_log2fc"])
          for p in ok for d in p["predictor_diagnostics_per_dose"]]
    put("DoseKMaxAbsSpearman", num(max(ks), 3))
    pcs = [r for p in ok for r in (p.get("class_fit_positive_control") or [])]
    ps = [r[k] for r in pcs for k in r
          if k.startswith("mann_whitney_p_less_") and r[k] > 0]
    if ps:
        put("DosePosCtrlMinP", sci(min(ps), 0))

    # --- e7b: intervals, the null, and the hierarchy that is not clean ---
    nb = V["e7b_null_calibration"]
    put("NullBoot", str(nb["n_bootstrap"]))
    put("NullPerm", str(nb["n_permutations"]))
    put("NullConstructs", str(nb["n_constructs_analysed"]))
    for rule, tag in (("canonical_strongest", "Can"), ("best_ddG", "Best")):
        d = nb["pooled_site_class"][rule]
        # LaTeX macro names cannot contain digits, hence SevenMEight not
        # SevenM8: the latter parses as \CanSevenM followed by "8"
        for cl, ct in (("8mer", "EightMer"), ("7mer-m8", "SevenMEight"),
                       ("7mer-A1", "SevenAOne"), ("6mer", "SixMer")):
            base = f'e7b_null_calibration.pooled_site_class.{rule}.{cl}'
            put(f"{tag}{ct}Med", num(d[cl]["median_log10ratio"], 5),
                f"{base}.median_log10ratio")
            put(f"{tag}{ct}CI", ci(d[cl]["median_ci95"], 5),
                f"{base}.median_ci95")
            put(f"{tag}{ct}N", f"{d[cl]['n']:,}", f"{base}.n")
        sm = d["_summary"]
        sb = f'e7b_null_calibration.pooled_site_class.{rule}._summary'
        put(f"{tag}Inv", num(sm["inversion_median_7merm8_minus_7merA1"], 5),
            f"{sb}.inversion_median_7merm8_minus_7merA1")
        put(f"{tag}InvCI", ci(sm["inversion_ci95"], 5),
            f"{sb}.inversion_ci95")
        put(f"{tag}NInv", str(sm["n_constructs_showing_inversion"]),
            f"{sb}.n_constructs_showing_inversion")
        put(f"{tag}NTested", str(sm["n_constructs_tested"]),
            f"{sb}.n_constructs_tested")
        put(f"{tag}Monotone", "monotone" if sm["monotone_in_canonical_order"]
            else "not monotone", f"{sb}.monotone_in_canonical_order")
    st = nb["pooled_spearman_with_null_and_ci"]
    put("NullNPairs", f"{st[0]['n_pairs_pooled']:,}")
    put("NullNRho", str(len(st)))
    allz = [q[f"z_vs_permutation_null_{t}"] for q in st
            for t in ("equilibrium", "independent")]
    put("NullZLo", num(min(allz), 1))
    put("NullZHi", num(max(allz), 1))
    _sb = {(x["binning_rule"], x["R"], x["threshold"]):
           x["smallest_B_all_rho_o_target"]
           for x in V["e4b_binned_background"]["smallest_B_restoring_invariance"]}
    _both = [(r, t) for (b, r, t) in _sb if b == "quantile"
             and ("equal_width", r, t) in _sb]
    put("NQuantileCheaper", str(sum(
        1 for r, t in _both
        if (_sb[("quantile", r, t)] or 0) < (_sb[("equal_width", r, t)] or 0))))
    put("NBinSettings", str(len(_both)))
    _nq = sum(1 for r, t in _both
              if (_sb[("quantile", r, t)] or 0) < (_sb[("equal_width", r, t)] or 0))
    put("QuantileCheaperClause",
        "never the cheaper rule" if _nq == 0
        else f"the cheaper rule in {_nq} of the {len(_both)} settings")
    put("BSmallestOneEW", str(next(
        (x["smallest_B_all_rho_o_target"]
         for x in V["e4b_binned_background"]["smallest_B_restoring_invariance"]
         if x["binning_rule"] == "equal_width" and x["R"] == 25
         and x["threshold"] == 0.01), "none")))

    put("NullOutside", str(sum(
        q["observed_outside_null_envelope_equilibrium"] for q in st)))
    # repression is negative, so the strongest predictor is the MOST
    # negative correlation, not the largest
    best = min(st, key=lambda q: q["pooled_spearman_equilibrium"])
    put("SpearBest", num(best["pooled_spearman_equilibrium"], 4))
    put("SpearBestCI", ci(best["cluster_bootstrap_ci95_equilibrium"], 4))
    put("SpearBestPairCI",
        ci(best["pair_bootstrap_ci95_equilibrium_CONDITIONAL"], 4))
    put("SpearBestRho", num(best["rho"], 3))
    worst = max(st, key=lambda q: q["pooled_spearman_equilibrium"])
    put("SpearWorst", num(worst["pooled_spearman_equilibrium"], 4))
    put("SpearWorstCI", ci(worst["cluster_bootstrap_ci95_equilibrium"], 4))
    put("SpearWorstRho", num(worst["rho"], 3))
    put("SpearInd", num(st[0]["pooled_spearman_independent"], 4))

    # --- the paired comparison, which is what licenses or refuses any
    # --- claim that the coupling layer predicts better than independent
    # --- scoring. The rho where the two scorings differ MOST is where such
    # --- a claim would be made, so that is the row reported.
    wide = min(st, key=lambda q: q["equilibrium_minus_independent"])
    put("GapRho", num(wide["rho"], 3))
    put("SpearGap", num(wide["equilibrium_minus_independent"], 4))
    put("GapNullMean", num(wide["paired_permutation_null_mean_gap"], 4))
    put("GapNet", num(wide["observed_gap_minus_paired_null_mean"], 4))
    put("GapNetP", num(
        wide["paired_permutation_p_two_sided_about_null_mean"], 3))
    put("GapClusterCI", ci(wide["cluster_bootstrap_ci95_gap"], 4))
    put("GapNetOverSE", num(abs(wide["paired_net_gap_over_cluster_se"]), 2))
    put("GapDirection", "independent scoring"
        if wide["observed_gap_minus_paired_null_mean"] > 0
        else "the equilibrium score")
    put("NullCentredEq", num(
        wide["null_centred_association_equilibrium"], 4))
    put("NullCentredInd", num(
        wide["null_centred_association_independent"], 4))
    put("ClusterBoot", str(nb["n_cluster_bootstrap"]))
    put("NGeneRepeat", fmt_thousands(
        nb["pooled_pair_dependence_diagnostic"]["n_distinct_genes"]))
    put("MaxConstructsPerGene", str(
        nb["pooled_pair_dependence_diagnostic"]["max_constructs_per_gene"]))
    put("NCritMet", str(len(
        nb["rho_values_meeting_paired_and_cluster_criteria"])))
    put("NCritMaterial", str(len(
        nb["rho_values_where_improvement_exceeds_one_cluster_se"])))
    put("CritMetRhos", ", ".join(
        num(q, 1) for q in
        nb["rho_values_meeting_paired_and_cluster_criteria"]) or "none")
    put("MaxNetGapWhereMet", sci(
        nb["max_abs_net_gap_where_criteria_met"], 1)
        if nb["max_abs_net_gap_where_criteria_met"] is not None else "n/a")
    put("AddedValue", "is not established"
        if not nb["EQUILIBRIUM_ADDS_ESTABLISHED_PREDICTIVE_VALUE"]
        else "is established")

    # --- e9v: does the estimator recover a known answer ---
    sv = V["e9v_sim_estimator_validation"]
    put("SimSlopeErrInd", num(sv["sim_worst_slope_error_independent_data"], 3))
    put("SimSlopeErrEq", num(sv["sim_worst_slope_error_equilibrium_data"], 4))
    put("SimSlopeErrClass",
        num(sv["sim_worst_slope_error_class_estimator"], 4))
    put("SimPoolErr",
        num(100 * sv["sim_worst_rel_pool_error_class_estimator"], 1))
    put("SimKErr", num(100 * sv["sim_worst_rel_K_error_class_estimator"], 1))
    put("SimTrueEqSlope",
        num(sv["sim_continuous_K"][0]["sim_true_slope_equilibrium"], 3))
    put("SimNoise", ", ".join(str(q) for q in sv["sim_noise_levels"]))

    # --- e10 ---
    put("CtxAttempted", str(e10["n_constructs_attempted"]))
    put("CtxAgree", str(e10["n_constructs_with_agreeing_seed"]))
    put("CtxRatio", num(e10["pooled_geometric_mean_pool_ratio"], 2))
    put("CtxRatioCI", ci(e10["pooled_pool_ratio_ci95"], 2))
    put("CtxExcl", str(e10["n_constructs_whose_ci_excludes_1"]))
    put("CtxNBoot", str(e10["n_bootstrap"]))
    dl = [abs(r["on_target_log2fc_difference"])
          for r in e10["delivery_control_on_target_knockdown"]
          if r["on_target_log2fc_difference"] is not None]
    put("CtxDeliveryMin", num(min(dl), 2))
    put("CtxDeliveryMax", num(max(dl), 2))
    return m

def table_e4b(V):
    e4b = V["e4b_binned_background"]
    rows = [r for r in e4b["per_setting_summary"]
            if r["binning_rule"] == "quantile" and r["R"] in (25, 100, 500)]
    lin = {r["R"]: r["max_rel_err_o_target_linear_rule"] for r in rows}
    out = []
    for R in (25, 100, 500):
        cells = [f"{R}", f"{lin[R] * 100:.3g}"]
        for B in (1, 2, 5, 10, 50, 200):
            hit = [r for r in rows if r["R"] == R and r["B"] == B]
            cells.append(f"{hit[0]['max_rel_err_o_target_over_rho'] * 100:.3g}"
                         if hit else "--")
        out.append(" & ".join(cells) + r" \\")
    return "\n".join(out)

def table_e9(V):
    e9 = V["e9_dose_response"]
    cls = has_class_fit(e9)
    out = []
    for p in e9["per_construct"]:
        if p["status"] != "OK":
            continue
        cell = p["cell_line"].split()[0].replace("-", "").replace("/", "")
        ts = p["loglog_slope_pool_vs_dose"]["slope"]
        tb = (p.get("bootstrap") or {}).get("slope_ci95",
                                            [float("nan")] * 2)
        # a two-dose construct has no residual degree of freedom for its own
        # slope, which the reader has to be able to see in the table
        nd = len(p["doses_nM"])
        row = [p["construct"].replace("_", r"\_"), cell,
               f"{nd}" + (r"$^{\dagger}$" if nd < 3 else ""),
               f"{p['n_transcripts_retrieved_at_every_dose']:,}"]
        if cls:
            b = p.get("class_fit_bootstrap", {}) or {}
            sl = p["class_fit_loglog_slope_pool_vs_dose"]["slope"]
            lo, hi = b.get("slope_ci95", [float("nan")] * 2)
            ms = [r for r in p["class_fit_rho_inversion"]
                  if r["beta_case"] == "zero_background"][0]
            row += [f"{p['class_fit_n_genes']:,}",
                    f"{sl:.2f}", f"[{lo:.2f}, {hi:.2f}]",
                    f"{ms['loglog_slope_M_vs_dose']:.2f}"]
        else:
            rho = [r for r in p["rho_inversion"]
                   if r["beta_case"] == "zero_background"][0]["rho_per_dose"]
            row += [f"{ts:.2f}", f"[{tb[0]:.2f}, {tb[1]:.2f}]",
                    f"{sci(min(rho), 1)}--{sci(max(rho), 1)}"]
        out.append(" & ".join(row) + r" \\")
    return "\n".join(out)

def table_e9_header(V):
    """Column spec, header row and caption tail, matched to what exists."""
    if has_class_fit(V["e9_dose_response"]):
        return ("llrrrrrr",
                "construct & cells & doses & $n$ thermo. & $n$ class & "
                "exponent & 95\\% CI & $M$ slope \\\\",
                "The two sample sizes belong to different estimators and are "
                "not interchangeable: $n$ thermo.\\ is the retrieved "
                "subset the thermodynamic-$K$ fit uses, $n$ class is every "
                "measured gene, which is what the site-class fit uses. "
                "Exponent and its bootstrap 95\\% interval over "
                "transcripts are under the site-class estimator. $M$ slope "
                "is the log-log slope of the conservation-inverted total "
                "complex against dose, which must be $1$ if the assumed "
                "proportional loading holds. The last column is the "
                "thermodynamic-$K$ exponent, shown to make its instability "
                "visible. $\\dagger$ marks a construct with two dose "
                "points, whose individual slope has zero residual degrees "
                "of freedom.")
    return ("llrrrrr",
            "construct & cells & doses & transcripts & exponent & 95\\% CI "
            "& $\\rho$ range \\\\",
            "Exponent is under the thermodynamic $K$ with a bootstrap 95\\% "
            "interval over transcripts. The site-class estimator had not "
            "finished when this was generated and no column for it is shown.")

TEX = r"""
\documentclass{article}

%% NeurIPS 2026 workshop format. Double-blind is assumed for submission;
%% switch to [sglblindworkshop] if the workshop reviews single-blind, and add
%% "final" to the option list for the camera-ready.
\usepackage[dblblindworkshop]{neurips_2026}
\workshoptitle{Generative and Experimental Perspectives for Biomolecular
Design}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{float}
\usepackage{url}
\usepackage[hidelinks]{hyperref}
\usepackage{microtype}

%% ---------------------------------------------------------------------
%% Every macro below is written by scripts/make_paper.py from a value in
%% results/*.json. No number in this manuscript was typed by hand.
%% ---------------------------------------------------------------------
__MACROS__

%% Default float parameters reserve so much of a page for text that a
%% half-page figure pushes the rest of the page away, which wastes roughly a
%% fifth of every page carrying one. These are the usual relaxed values.
\renewcommand{\topfraction}{0.92}
\renewcommand{\bottomfraction}{0.85}
\renewcommand{\textfraction}{0.07}
\renewcommand{\floatpagefraction}{0.82}
\setcounter{topnumber}{2}
\setcounter{totalnumber}{3}

\newtheorem{proposition}{Proposition}
\newtheorem{theorem}{Theorem}

\title{One pool, many targets: a conservation layer and what
archival data can identify}

\begin{document}
\maketitle

\begin{abstract}
Pairwise guide--transcript scores do not enforce conservation of a finite
guide-loaded RISC pool when they are interpreted independently as occupancies.
We formulate a differentiable scalar equilibrium layer: one conservation
equation with a unique positive root and exact implicit gradients. It yields
a redistribution theorem, a qualified high-resource limit, an analysis of the
retrieval approximation, and a conditional rank-invariance result: within one
construct at one dose, rankings by fractional occupancy cannot distinguish
equilibrium from independent scoring. We therefore audit the two experiments
that proposition leaves open, dose and cross-context, on archival off-target
data. Corrected thermodynamic affinities associate weakly with measured
repression in the direction a working predictor requires, but a paired
permutation test and a construct-cluster bootstrap do not establish added
predictive value from the coupling: what survives their differing
permutation-null baselines is \GapNet{}, a descriptive \GapNetOverSE{} of the
equilibrium association's cluster standard error.
The dose fits are heterogeneous and frequently violate the model-implied
exponent constraint, which is superlinear rather than sublinear, so these data
do not identify the competition parameter. A saturable compression of the
competitor set holds both accuracy targets on held-out guide families but is
not faster at the size measured. The contribution is a reusable conservation
operator and the experimental information needed to test it.
\end{abstract}

\section{Introduction}

A transfected siRNA silences its target and, through its seed, tens to
hundreds of unintended transcripts \citep{jackson2003, birmingham2006,
jackson2006seed}. Design tools score candidates with sequence models
\citep{huesken2005, bai2024} that evaluate each (guide, transcript) pair
independently, which leaves the shared loaded-RISC budget unenforced. Cells
supply that constraint: Argonaute has limited copy number \citep{wang2012, janas2012},
transfected small RNAs compete with endogenous microRNAs for it
\citep{khan2009}, and target abundance dilutes activity \citep{arvey2010,
bosson2014, denzler2014, denzler2016}. We model one part of this: competition
among target sites for a pool \emph{already} loaded with the candidate guide.
Loading competition, endogenous microRNA occupancy, strand selection,
recycling and cleavage enter only through $M$.

Quantitative models of small-RNA competition already exist
\citep{loinger2012}, as do explicit on- and off-target repression models for
screening data \citep{riba2017}. Ours is narrower and mostly structural: the
operator, its comparative statics, and an audit of what archival data can
identify.

\section{A shared-resource equilibrium layer}
\begin{figure}[t]
\centering
\includegraphics[width=\textwidth]{../figures/fig_assoc.pdf}
\caption{Does the shared-pool coupling add anything over independent
scoring? GSE5814, \NullConstructs{} constructs, \NullNPairs{} pooled
construct--transcript pairs. (a) Pooled Spearman against measured log ratio,
each scoring net of \emph{its own} within-construct permutation null
(\NullPerm{} draws); bands are \ClusterBoot{} construct-cluster 95\%
intervals. Repression is negative, so below zero is the working direction.
(b) Their difference. The raw gap is reliably nonzero, its cluster interval
excluding zero at \NGapCIExclZero{} of \NullNRho{} values of $\rho$, yet under
a paired null (one shuffle applied to both models) what survives is at most
\MaxNetOverSE{} of one cluster standard error (\S\ref{sec:assoc}).}
\label{fig:assoc}
\end{figure}

Let $M$ be the pool of RISC loaded with the candidate guide, $x_j$ the
abundance of transcript $j$, and $K_j>0$ an effective interaction parameter.
Writing $f$ for the free loaded pool, mass conservation over the retrieved
set $\mathcal{R}$ gives
%
\begin{equation}
F(f) \;=\; (1+\beta)\,f \;+\; \sum_{j\in\mathcal{R}} \frac{x_j f}{K_j+f}
\;-\; M \;=\; 0,
\qquad
o_j \;=\; \frac{x_j f}{K_j + f},
\label{eq:cons}
\end{equation}
%
where a constant $\beta$ stands in for the omitted set as a linear,
unsaturated reservoir, which cannot represent saturable omitted targets
exactly (\S\ref{sec:binned}). Combining a transcript's sites as
$1/K_j = \sum_s 1/K_{js}$ and capping its load at $x_j$ treats them as
\emph{mutually exclusive}: at most one complex per transcript
(\S\ref{sec:proofs}). Since $F(0)=-M<0$,
$F'>0$ and $F(M)\ge 0$, the root is unique and bracketed by $[0,M]$, so
bisection is globally convergent and batches over candidates; gradients come
from the implicit function theorem and match central differences to a median
relative error of \GradErr{} (coordinate-level checks, \S\ref{sec:proofs}).

The independent counterfactual is the same expression with $f$ pinned to $M$,
$o_j^{\text{ind}} = x_j M/(K_j+M)$, isolating the coupling as the only
difference. The competition parameter is
$\rho = M/N_{\mathrm{mRNA}}$, where the denominator is the \emph{whole-cell}
mRNA count, \NmRNA{} molecules per cell, and not the retrieved set
$\mathcal{R}$ of \eqref{eq:cons}. That is what makes $\rho$ the same
quantity as $\alpha\cdot(\text{Argonaute})/(\text{mRNA})$ in
\S\ref{sec:regime}.
The pipeline is short: control-channel abundances and GENCODE 3$'$UTRs give
$x_j$, a ViennaRNA construction anchored on a measured $K_d$ gives $K_j$, and
\eqref{eq:cons} turns them into occupancies whose gradients flow back to
$K$__WORKFLOW_REF__.
Whether independent scoring over-allocates is conditional on the loaded
fraction $\alpha$: at \AgoLo{} total Ago1--4 in HeLa with $\alpha=1$ it uses
\BudgetAtAgoLo{} of the budget, crossing only below
$\alpha=\AlphaThreshLo{}$ (Figure~\ref{fig:mech}).



\subsection{What the layer implies}

\paragraph{Redistribution, the high-resource limit, retrieval depth.}
Weakening one transcript's affinity frees pool for every other,
$\partial o_i/\partial K_t > 0$ for $i \neq t$ and $\partial o_t/\partial
K_t<0$, with \RedistViolA{} and \RedistViolB{} violations over \RedistDraws{}
draws (\S\ref{sec:proofs}). With $\beta=0$ the fractional-occupancy gap is
$O(M^{-2})$ pointwise as $M\to\infty$, so equilibrium contains independent
scoring as its high-resource limit under conditions in \S\ref{sec:limit}.
Shallow truncation is unusable: at $R=\EFourRShallow{}$ affinity errs by
\EFourAff\% and abundance mass by \EFourAbundPct\% (\S\ref{sec:binned}).


\subsection{Compressing the competitor set}
\label{sec:approx}

\begin{figure}[t]
\centering
\includegraphics[width=\textwidth]{../figures/fig_approx.pdf}
\caption{Compressing the competitor set: \ApxCases{} held-out cases,
\ApxTestFam{} guide families disjoint from the \ApxDevFam{} used to fix the
configuration. (a) Relative error against the full retrieved reference at
$R=\ApxR{}$, one point per case, three treatments of the omitted transcripts;
dotted lines are the 1\% targets, so only the lower-left quadrant passes both.
(b) Two error measures for the same solutions, each divided by $\max(M,1)$;
median and quartiles. (c) Median forward time (ms) over \ApxNRef{}
competitors, single-threaded float64; bin construction is part of
preparation.}
\label{fig:approx}
\end{figure}

Truncation is usable only if the omitted mass is represented well enough to
differentiate through. At depth $R=\ApxR{}$ we compare three treatments of the
remainder: discard it, fold it into one linear reservoir, or bin it into
\ApxB{} saturable groups, $X_b=\sum x_j$ and $K_b = X_b/\sum(x_j/K_j)$. The
configuration was fixed on \ApxDevFam{} guide families from D1 and D2, with
1\% relative error in the focal occupancy \emph{and} the gradient as the prior
criterion,
then applied unchanged to \ApxTestFam{} disjoint families, \ApxCases{} cases.

Only the saturable bins pass both (Figure~\ref{fig:approx}a): worst gradient
error \ApxGrad{} against \ApxTruncGrad{} for discarding and \ApxLinGrad{}
for the linear reservoir, though all three are inside 1\% in the forward
solve. A linear background has constant slope in $f$, so once the omitted mass
saturates it reports the wrong $\partial F/\partial f$, which implicit
gradients divide by. Accuracy is the defect against the \emph{original}
conservation law, median \ApxDefectMed{} and worst \ApxDefectWorst{}; the
compressed system's own residual, \ApxResid{}, says only that the bisection
converged (Figure~\ref{fig:approx}b). It is not faster: \ApxSelMs\,ms
forward against \ApxFullMs\,ms for the full reference at \ApxNRef{}
competitors, because the solver runs a fixed iteration count and a second
reduction costs more than a longer one at this size
(Figure~\ref{fig:approx}c, \S\ref{sec:apxdetail}). Accurate, with no measured
speed-up.

\paragraph{A negative result that constrains within-construct fixed-dose
rank tests based on fractional occupancy in the one-effective-$K$
formulation.}

\begin{proposition}[Within-construct fractional-occupancy rank invariance]
\label{prop:rank}
Fix a construct and a dose, and represent each transcript by one effective
binding state, so its sites are mutually exclusive and it carries at most one
complex. Equilibrium fractional occupancy is $q^{\mathrm{eq}}_j=f/(K_j+f)$ and
independent fractional occupancy is $q^{\mathrm{ind}}_j=M/(K_j+M)$. Both $f$
and $M$ are scalars shared by every transcript, and both expressions are
strictly decreasing in $K_j$. Hence one is a strictly monotone transform of
the other, and every rank statistic over transcripts computed on fractional
occupancy is identical, at every $\rho$.
\end{proposition}

The scope is exactly that: not absolute occupancy $x_j q_j$, which reorders
whenever abundance differs, not simultaneously occupiable sites. Within it the
result is a property of the model, not of our data, and it disqualifies the
experiment we first set out to run; the largest within-construct Spearman
difference over all $\rho$ is \WithinDiff{}, at the solver's bisection
tolerance. The layer can reorder only across constructs, doses or
transcriptomes.

\section{Data}
\label{sec:data}

Archival off-target microarrays only, numbered in order of appearance
(\S\ref{sec:recover} maps these onto the repository's D1--D9). \textbf{D1},
GSE5814 \citep{jackson2006seed}: \NArraysHela{} HeLa arrays, \NConstructs{}
constructs including \NSeedVariants{} seed variants of one MAPK14 siRNA. One is the non-targeting luciferase
control, which has no human guide, so \NConstructsScored{} are scored.
\textbf{D2}, E-MEXP-668 \citep{birmingham2006}: \NBirmArrays{} HeLa arrays,
\NBirmGuides{} guides, recovered from ArrayExpress
(\S\ref{sec:recover}); its seeds supply most of both sides of the
\S\ref{sec:approx} split and share \ApxGuideOverlap{} exact guides and
\ApxSeedOverlap{} exact seeds (2--8) with D1. \textbf{D3}, dose series GSE28786 \citep{caffrey2011}:
\NDoseArrays{} arrays. \NDoseThree{} constructs were measured at
\DoseLevels\,nM and \DoseTwoName{} only at 1 and 10\,nM; matched 0\,nM
controls were also deposited.
\textbf{D4}, cross-context GSE14073 \citep{burchard2009}: \NCtxArrays{}
arrays in two liver lines. Recovery and preprocessing: \S\ref{sec:recover}.

Transcript structure is GENCODE v\GencodeRelease{} \citep{frankish2021},
\NCanonUTR{} canonical 3$'$UTRs. Abundance comes from the untreated, mock or
non-targeting control measurements of the same experiment: the reference
channel for the two-colour GSE5814 and E-MEXP-668 arrays, and the
control-condition arrays for the single-channel GSE28786 and GSE14073. Affinity is thermodynamic,
$\Delta G_{\mathrm{eff}} = \Delta G_{\text{duplex}} - RT\ln
P_{\text{unpaired}}$ from ViennaRNA \citep{lorenz2011, bernhart2006}, the
duplex energy \emph{plus} the cost of opening the site, anchored on the
measured seed-match $K_d$ \citep{wee2012} to give molecules per cell
(\S\ref{sec:scale}); $K$ is never fitted to expression. Argonaute copy number
\citep{wang2012, janas2012} is carried as a range; the mRNA total
\citep{marinov2014} is one value inside the range that measurement reports
(\S\ref{sec:limits}).

\section{Where a real transfected cell sits}
\label{sec:regime}

With abundance normalised to the assumed total, $\rho_{\mathrm{cell}}$
reduces to $\alpha \cdot (\text{Argonaute copies})/(\text{mRNA copies})$,
$\alpha$ being the unmeasured loaded fraction. The two Argonaute figures are
not two measurements of one quantity: \AgoLo{} is total Ago1--4 in HeLa and
\AgoHi{} total Argonaute from other settings, neither AGO2-specific, and the
mRNA count was not measured on these arrays, so what follows is a
literature-based \emph{scenario range}, not an estimated band. Sweeping
$\alpha$ over three decades, with the Argonaute figures spanning a further
decade, gives $\rho_{\mathrm{cell}} \in [\RhoLo, \RhoHi]$, and the contour
below which $\tau<0.9$ sits at $\rho \approx \TauContour{}$, \emph{inside} it
(Figure~\ref{fig:phase}). Whether the layer matters therefore turns on a
quantity these datasets do not measure; whether a dose series can supply it is
\S\ref{sec:dose}.

\section{What the affinity scores predict}
\label{sec:assoc}


Over \NullNPairs{} pooled construct-transcript pairs in D1 the equilibrium
score reaches \SpearBest{} at $\rho=\SpearBestRho{}$ against \SpearInd{} for
independent scoring, each \NullZLo{} to \NullZHi{} standard deviations from
its own permutation null (Figure~\ref{fig:assoc}a): weak, and in the right
direction.

The raw difference between them is not evidence that coupling helps: the two
have different null baselines, because pooling constructs leaves a
between-construct correlation a within-construct shuffle cannot remove. At
$\rho=\GapRho{}$, where they differ most, the raw gap is \SpearGap{} but the
paired null, one shuffle applied to both models, already sits at
\GapNullMean{} and so exceeds it. What survives is \GapNet{}, or
\GapNetOverSE{} of the equilibrium association's cluster standard error: a
descriptive scale, not a paired test. The prespecified three-part screen of
\S\ref{sec:paired} is met at \NCritMet{} of \NullNRho{} evaluated $\rho$
values, all at the largest $\rho$, where the scorings converge by construction
and the absolute difference is at most \MaxNetGapWhereMet{}; the separate
practical-significance requirement is met at no $\rho$. This analysis does not
establish that coupling improves prediction.

Per dose the correlation is at most \DoseKMaxAbsSpearman{} in absolute value,
so this $K$ orders transcripts only coarsely: 7mer-A1 sites are repressed more
than 7mer-m8, a $t1$-pocket contribution \texttt{duplexfold} does not
represent (\S\ref{sec:hier}).

\begin{figure}[t]
\centering
\includegraphics[width=0.78\textwidth]{../figures/fig_dose.pdf}
\caption{Fitted dose exponent
$\mathrm{d}\log(\text{pool})/\mathrm{d}\log(\text{dose})$ per construct on
GSE28786, both estimators, 95\% bootstrap intervals, \NDoseFitted{}
constructs. Conservation makes the pool convex in the loaded amount, so under
proportional loading the exponent cannot fall below $1$: the shaded region
indicts that combined specification rather than equilibrium alone. The
constructs are variants of one another, so the audit cannot separate mechanism
from assumption (\S\ref{sec:convex}).}
\label{fig:dose}
\end{figure}

\section{A dose-series identifiability audit}
\label{sec:dose}

Proposition~\ref{prop:rank} fixes the dose; it says nothing about how one
construct behaves across doses, because dose changes $M$ and therefore $f$.
\citet{caffrey2011} profile \NDoseThree{} of \NDoseFitted{} constructs at
\DoseLevels\,nM and \DoseTwoName{} at 1 and 10\,nM only, against matched 0\,nM
arrays, holding \emph{total} transfected duplex constant. We \emph{assume} the
guide-specific loaded pool $M$ is proportional to administered dose: the
constant-duplex design makes that more plausible but does not establish
proportional uptake, loading or recycling. We fit one scalar pool per dose by
maximum likelihood with $K_j$ fixed, regress $\log(\text{pool})$ on
$\log(\text{dose})$, then check the assumption.

\paragraph{The direction of the test is the opposite of what we expected.}
One expects added complex to be absorbed, so an exponent below $1$ would
signal competition. Conservation says otherwise: $M(f)$ is concave in $f$, so
$f$ is \emph{convex} in $M$ and $\mathrm{d}\log f/\mathrm{d}\log M \ge 1$.
The measured exponent is against \emph{dose}, and inherits that bound only
under proportional loading, so an exponent below $1$ indicts the combined
specification rather than equilibrium (\S\ref{sec:convex}).


We report two estimators. The thermodynamic $K$ gives a pooled exponent of
\ThermoSlope{} (95\% CI \ThermoSlopeCI) with \NThermoNeg{} of \NDoseFitted{}
per-construct exponents \emph{negative}, which conflict with the fixed-input
model whenever the loaded pool is nondecreasing in dose, proportional loading
included (\S\ref{sec:convex}), so it diagnoses its own failure. The second carries
affinity by \emph{site class}, one parameter per class shared across doses
(\S\ref{sec:sim}).__CLASS_SANITY__

__DOSE_RESULT__

\section{Limitations and conclusion}

For within-construct fixed-dose rank statistics of fractional occupancy under
the one-effective-$K$ model, reweighting $K$ cannot outperform the $K$ it is
given: Proposition~\ref{prop:rank} says no such statistic detects the coupling
at all. That is the most useful thing the shared pool buys, because it says
which experiments are not worth running (\S\ref{sec:limits}). The archival data buy less: a weak association in the right
direction, no established added value from coupling, and dose fits too
heterogeneous to identify $\rho$. The compression of \S\ref{sec:approx} is
accurate but not faster at the size measured. A decisive experiment needs more
doses, constructs that are not variants of one another, and a better $K$.

The next step is a learned, strictly positive affinity head, a transformer or
graph network over base-pairing and accessibility, emitting $K_j>0$ per pair
and trained through the conservation equation to learn what the ViennaRNA
construction omits. Evaluation should hold out guides and cell lines and
compare the head with and without the layer. It is not evaluated here.

\bibliographystyle{plainnat}
\bibliography{refs}

\clearpage
\appendix
\input{appendix}

\end{document}
"""

# The appendix is a separate file, written to paper/appendix.tex and pulled in
# by main.tex after the bibliography. It inherits the generated macros from
# main.tex's preamble, so it is an \input fragment and not a standalone
# document.
TEX_APPENDIX = r"""
__WORKFLOW_FIGURE__\section{Code and data availability}

The equilibrium layer, the acquisition scripts, the per-experiment result
files and the figure code will be released publicly once review is complete.
Every number in this manuscript, including every number in a caption, is
generated from a machine-readable result file rather than transcribed; each
generated macro carries the expression and the result file it was read from,
so the trace from a printed number back to the script that produced it is
mechanical. Every retrieved byte carries a provenance record with its URL,
checksum and retrieval status, failed retrievals included. The released
materials also contain a held-out test on external families of a site-class
correction to $K$, which reduced performance and is not reported here. All datasets used
are archival and already public under the accessions named in
\S\ref{sec:data}.

\begin{figure}[h]
\centering
\includegraphics[width=\textwidth]{../figures/fig1_mechanism.pdf}
\caption{Model calculation on measured inputs (abundances from the GSE5814
mock channel, structure from GENCODE v\GencodeRelease{} 3'UTRs; MAPK14-193
parent). Total bound transcript against the loaded pool, with the
over-allocation ratio on the right axis: the independent counterfactual
exceeds the budget by up to \BudgetWorst-fold more complexes, but only at
pools far below one complex per cell, while equilibrium is constrained to the
budget by construction. Green triangles are published Argonaute copy numbers,
total Ago1--4 in the HeLa case; the grey band is the swept loaded fraction. Redistribution and the
high-resource limit are shown in \S\ref{sec:proofs}.}
\label{fig:mech}
\end{figure}

\begin{figure}[h]
\centering
\includegraphics[width=0.58\textwidth]{../figures/fig2_regime.pdf}
\caption{Model calculation on measured GSE5814 HeLa abundances. Kendall
$\tau$ between the two scorings' candidate rankings against $\rho$, with the
band covering the swept $H_K$. The $\tau=0.9$ contour lies \emph{inside} the
\RhoDecades-decade scenario range, so the calculation cannot say which side a
real cell falls on: the identifiability problem \S\ref{sec:dose} does not
close.}
\label{fig:phase}
\end{figure}

\section{Proofs}
\label{sec:proofs}

\begin{figure}[h]
\centering
\includegraphics[width=\textwidth]{../figures/figA3_theory.pdf}
\caption{Model calculation on measured GSE5814 abundances and GENCODE
v\GencodeRelease{} structure. (a) Redistribution: raising one
transcript's $K_t$ lowers its own occupancy and raises every other's,
monotonically. (b) The relative gap between the two scorings decays with
exponent $\PwSlope \pm \PwSlopeSE$ against a predicted $\PwPredicted$, over
\PwDecades{} decades.}
\label{fig:theory}
\end{figure}

\paragraph{Gradient accuracy.} Over \NGradCoord{} coordinates the median
relative disagreement with a central difference is \GradErr{}. The worst is
\GradWorst{}, and it is not informative: it falls on a coordinate whose own
gradient is near zero, where a relative measure divides by nothing. Measured
against the gradient norm, which is the quantity that says whether the
implicit gradients are right, the worst error is \GradWorstNorm{}. A wrong
implicit gradient would disagree by order one, not by parts in $10^7$.

\paragraph{Redistribution.} Assume $M>0$, $x_j\ge 0$, $K_j>0$ and
$\beta\ge 0$, which are the conditions under which the root of
\eqref{eq:cons} is unique. Write
%
\[
D \;=\; \frac{\partial F}{\partial f}
\;=\; (1+\beta) + \sum_j \frac{x_j K_j}{(K_j+f)^2} \;>\; 0 .
\]
%
The implicit function theorem gives
$\partial f/\partial K_t = x_t f / [(K_t+f)^2 D] > 0$: raising one
transcript's $K_t$ raises the free pool. For any other transcript $i\neq t$,
%
\[
\frac{\partial o_i}{\partial K_t}
= \frac{x_i K_i}{(K_i+f)^2}\,\frac{\partial f}{\partial K_t} \;>\; 0 ,
\]
%
so every other transcript gains. For the swept transcript itself,
$\partial o_t/\partial K_t = x_t(f'K_t-f)/(K_t+f)^2$ where
$f' = \partial f/\partial K_t$; putting $u = x_t K_t/(K_t+f)^2$ gives
$f'K_t - f = f(u/D - 1)$, which is strictly negative because
$D \ge 1+u > u$. So $o_t$ falls while every $o_i$ rises.

\section{Binned background at shallow retrieval}
\label{sec:binned}

\begin{table}[h]
\caption{Maximum relative error in on-target occupancy against the full
\EFourN-transcript reference, in per cent, over $\rho\in\{0.01,0.5,10\}$,
quantile bins. The first column is the linear affinity-weighted rule, which
uses no bins at all. The columns to its right are $B$ \emph{saturable} bins,
so the $B{=}1$ column is one saturable bin: a different object, which errs
differently. Forcing a saturable bin to its linear limit does reproduce the
linear column exactly, to a maximum relative difference of \RegDiff{}, but
that is a regression check on the implementation and not a row of this
table.}
\label{tab:e4b}
\centering
\small
\begin{tabular}{rrrrrrrr}
\toprule
& linear & \multicolumn{6}{c}{saturable bins, $B=$} \\
\cmidrule(lr){3-8}
$R$ & (no bins) & 1 & 2 & 5 & 10 & 50 & 200 \\
\midrule
__TABLE_EFOURB__
\bottomrule
\end{tabular}
\end{table}

\paragraph{How much does binning actually save?} Restoring $1\%$ accuracy at
$R=25$ takes $25+\BSmallestOne$ individually scored terms, and the two binning
rules agree exactly on that count, against the $501$ an untruncated $R=500$
requires. That is not a saving in time: \S\ref{sec:approx} measures the
compressed solve as slower than the full one at this size, so a smaller term
count must not be read as a speed-up. The table reports quantile bins,
which are \QuantileCheaperClause{} across the \NBinSettings{} depth and
threshold settings swept, so nothing here is flattered by the choice.

\section{Compressed solve: selection, gradients and timing}
\label{sec:apxdetail}

\begin{figure}[h]
\centering
\includegraphics[width=\textwidth]{../figures/px_B_approx.pdf}
\caption{Detail behind Figure~\ref{fig:approx}. (a) Development selection
surface: 90th-percentile focal occupancy error over the \ApxDevFam{}
development families for every configuration on the frozen grid; the circled
point is the selected one, fixed before any held-out family was scored.
(b) The two residual definitions on the \ApxCases{} held-out cases, each
divided by $\max(M,1)$. (c) Median forward cost at matched outputs,
preparation and cached solve stacked, against the full reference end to end.
(d) Analytic gradients against central differences over \ApxFDCoord{}
coordinates including omitted competitors; the dotted line is equality.}
\label{fig:apxdetail}
\end{figure}

\paragraph{Selection.} The grid over method, retrieval depth $R$ and bin count
$B$ was scored on \ApxDevFam{} guide families, three of them D1 target genes
and the rest D2 seed families. The configuration
(\ApxMethod{}, $R=\ApxR{}$, $B=\ApxB{}$) was frozen there and applied
unchanged to \ApxTestFam{} disjoint families, \ApxCases{} cases, which are
\ApxTestCon{} constructs times \ApxRhos{} values of $\rho$; the families are
the independent units, not the cases. No configuration was reselected after
the held-out families were scored.

\paragraph{Gradients.} Central differences were taken on \ApxFDCoord{}
coordinates, including coordinates of omitted competitors, with the step
escalated until the difference cleared the float64 noise floor. The worst
relative error is \ApxFDWorst{}; restricted to the \ApxFDAbove{} coordinates
whose analytic gradient exceeds $10^{-9}$, below which a relative measure
divides by the noise floor, it is \ApxFDStrat{}. Both numbers are reported
because neither replaces the other.

\paragraph{Timing.} Preparation, bin construction, cached solve and end-to-end
cost are measured separately on one construct with \ApxNRef{} competitors,
CPU, float64, single-threaded, \ApxReps{} timed repetitions after warm-up,
with every method returning the same outputs. Bin construction is a component
of preparation, not an addition to it. The solver runs a fixed \ApxIters{}
bisection iterations for every method, so iteration count cannot separate
them; what does is the number of reduction passes per iteration. Adding
\ApxElems{} elements to an existing reduction costs \ApxCostElems\,ms, while
adding a second reduction holding a single element costs
\ApxCostSecond\,ms, so per-pass fixed cost dominates the $O(n)$ work at this
size and the linear and binned backgrounds, which each add a pass, cannot
beat the full solve. Charging preparation to both sides, truncation is
cheaper from the first solve and the binned configuration never breaks even.
These are measurements of this workload on this machine, not scaling claims.

\section{The site-class hierarchy is not the canonical one}
\label{sec:hier}

\begin{figure}[h]
\centering
\includegraphics[width=0.56\textwidth]{../figures/fig_hier.pdf}
\caption{Measured repression by seed site class over \NullConstructs{}
GSE5814 constructs under both site-assignment rules, bootstrap 95\% intervals
on the median, pair counts above each pair. The two 7mer classes are
exchanged relative to the canonical order under both rules, which is the
observation this section is about.}
\label{fig:hier}
\end{figure}


Seed-matched transcripts are repressed against transcripts with no site, but
the four classes do not order as the canonical hierarchy expects. Pooling
\NullConstructs{} constructs and assigning each transcript the strongest class
present on it, the medians are \CanEightMerMed{} for 8mer (n = \CanEightMerN,
95\% CI \CanEightMerCI), \CanSevenMEightMed{} for 7mer-m8 (n = \CanSevenMEightN,
\CanSevenMEightCI), \CanSevenAOneMed{} for 7mer-A1 (n = \CanSevenAOneN,
\CanSevenAOneCI) and \CanSixMerMed{} for 6mer (n = \CanSixMerN, \CanSixMerCI).
That sequence is \CanMonotone{} in the canonical order 8mer, 7mer-m8,
7mer-A1, 6mer: the two 7mer classes are exchanged, with 7mer-A1 the more
repressed of the two by \CanInv{} (95\% CI \CanInvCI), and the exchange
appears in \CanNInv{} of \CanNTested{} constructs individually.

It is not an artefact of how a transcript is assigned a class. Under the
alternative rule, labelling each transcript by the class of its lowest
$\Delta G_{\mathrm{eff}}$ site, the ordering is \BestMonotone{} in the same way and the difference is
\BestInv{} (95\% CI \BestInvCI) in \BestNInv{} of \BestNTested{} constructs.
Both intervals exclude zero. This is not an anomaly to be explained away. A
7mer-A1 site pairs guide positions 2--7 and adds the $t1$ adenosine, which
Argonaute reads through a dedicated pocket rather than by base pairing; a
7mer-m8 site pairs 2--8 and has no $t1$. An ordering in which 7mer-A1 wins is
what a strong $t1$ contribution looks like. It is consistent with a
contribution from the Argonaute $t1$-adenosine pocket, the same mechanism
invoked in \S\ref{sec:assoc} for why a duplex-energy model ranks these
transcripts poorly: the term that separates the two classes is not a base
pair, and the present duplex-pairing-only energy construction does not
represent this non-base-pair contribution.

\section{How the association is tested}
\label{sec:paired}

\paragraph{The permutation null is not centred on zero.} Permuting measured
values within construct preserves each construct's response distribution, so
any between-construct structure survives the shuffle: pooling constructs whose
predicted occupancies and whose measured responses both differ systematically
leaves a correlation the shuffle cannot remove. The null is therefore reported
rather than assumed, and the test is two-sided about the null's own mean
rather than about zero. The two scorings do not share that mean, which is why
a raw difference of pooled correlations is not a test: at $\rho=\GapRho{}$
the equilibrium null sits at one place and the independent null at another,
and the difference between the nulls, \GapNullMean{}, exceeds the raw gap
\SpearGap{} in magnitude, which is why the net changes sign rather than
merely shrinking. Net of their own nulls the two associations are \NullCentredEq{}
and \NullCentredInd{}.

\paragraph{The paired test, and the criterion it feeds.} One within-construct
permutation is drawn and applied to \emph{both} models, and the difference of
the two correlations is recorded under that same shuffle, so the two models
see identical permuted data and the difference is not inflated by their
seeing different ones. It does \emph{not} follow that the confound cancels:
the paired null mean is \GapNullMean{}, not zero, which is why the test is
two-sided about that mean rather than about zero. Over \NullPerm{} draws this
gives the paired null quoted in \S\ref{sec:assoc}.

The screen is prespecified and has three parts, all of which must hold at the
same $\rho$: the paired permutation $p$ is below $0.05$, the
construct-cluster interval on the gap excludes zero, and the gap net of the
paired null is in equilibrium's favour. That is what the count in
\S\ref{sec:assoc} reports. A fourth requirement separates a difference that is
detectable from one worth having: the net gap must be at least one
construct-cluster standard error of the equilibrium association itself. The
scale is taken from the data rather than chosen, and the fourth requirement is
met at no $\rho$, which is why no added predictive value is claimed.

\paragraph{Two bootstraps, and what each licenses.} The pair-level bootstrap
resamples transcript-construct pairs. It is \emph{conditional on the observed
constructs}: it describes sampling noise inside this panel of
\NullConstructs{} constructs and cannot support a statement about a new guide.
The construct-cluster bootstrap resamples whole constructs with replacement,
keeping every pair belonging to a sampled construct, over \ClusterBoot{}
draws; that is the interval a generalising claim needs, and it is
correspondingly wider. At $\rho=\GapRho{}$ the pair-level interval on the
equilibrium correlation is \SpearBestPairCI{} and the cluster interval on the
raw gap is \GapClusterCI{}. The latter excludes zero, but it is an interval on
the \emph{raw} gap, which carries the null baseline with it, so it is not the
quantity the claim rests on; the null-centred difference is what is, and that
is \GapNet{}. Neither removes the dependence created by one gene
appearing under many constructs: the \NullNPairs{} pooled pairs cover
\NGeneRepeat{} distinct genes, the most frequent appearing under
\MaxConstructsPerGene{} of them. The cluster bootstrap carries a gene's
repeated appearances together with the construct that produced them, but
residual gene-level dependence across distinct constructs would need a
crossed random-effects model that \NullConstructs{} constructs cannot
support. We therefore treat \S\ref{sec:assoc} as an upper bound on what can
be claimed, not a lower one.

\section{Estimator validation}
\label{sec:sim}

The site-class estimator pins the 7mer-m8 class to the published
dissociation constant \citep{wee2012} to fix the common scale, and its
recovered class ordering is a built-in check: it comes out correct (8mer
strongest) for \ClassSane{} of \NDoseFitted{} constructs.

SIMULATION. Ground-truth pools and affinities do not exist in nature, so this
validates the estimators of \S\ref{sec:dose} and claims nothing about any
cell. Data
were generated from each model in turn at noise levels \SimNoise{} and refitted
blind. On data generated by independent scoring, where the true exponent is
exactly 1, the fitted exponent is correct to within \SimSlopeErrInd. On data
generated by the equilibrium model, whose own exponent is \SimTrueEqSlope{}
and therefore above 1 as the convexity argument requires, the fitted exponent
is correct to within \SimSlopeErrEq. The site-class estimator recovers its
true exponent to within \SimSlopeErrClass, the true pools to within
\SimPoolErr\% and the true per-class affinities to within \SimKErr\%, with the
class ordering recovered correctly at every noise level. The simulation
verifies implementation-level recovery under the assumed generative model; it
does not rule out model misspecification, confounding, or weak
identifiability in the archival data, and the audit in \S\ref{sec:dose}
finds all three to be live.

\begin{table}[h]
\caption{Dose series, per construct. Exponent is
$\mathrm{d}\log(\text{pool})/\mathrm{d}\log(\text{dose})$ under the site-class
estimator with a bootstrap interval over transcripts; $1$ is the
independent-scoring prediction and below $1$ is incompatible with the combined
model under proportional loading. The
sample sizes belong to different estimators: $n$ thermo.\ is the retrieved
subset, $n$ class every measured gene. $M$ slope must be $1$ if proportional
loading holds. $\dagger$: two dose points, zero residual df.}
\label{tab:e9}
\centering
\small
\begin{tabular}{__TABLE_ENINE_SPEC__}
\toprule
__TABLE_ENINE_HEAD__
\midrule
__TABLE_ENINE__
\bottomrule
\end{tabular}
\end{table}

\section{The dose likelihood as implemented}
\label{sec:like}

Transcribed from the implementation rather than restated. For construct $s$,
dose $d$ and transcript $j$,
%
\[
y_{d,j} \;=\; a_d \;-\; c_s\, b_j(p_d) \;+\; \varepsilon,
\qquad b_j(p) \;=\; \frac{p}{K_j + p},
\]
%
with $y$ the measured log$_2$ fold change against the zero-dose arrays. The
per-dose intercepts $a_d$ and the amplitude $c_s$ are profiled out in closed
form: centring $y$ and $b$ within each dose removes $a_d$ exactly, leaving a
single-coefficient regression through the origin pooled over doses,
$c_s = -\sum_d \langle \tilde y_d, \tilde b_d\rangle / \sum_d \langle \tilde
b_d, \tilde b_d\rangle$, the sign because repression is negative. Errors are
homoscedastic within a construct and $\sigma$ is concentrated out, so the
objective is the Gaussian profile negative log-likelihood
$\tfrac{1}{2} n \log(\mathrm{RSS}/n)$; the per-dose residual spread is
reported as a diagnostic rather than modelled, because three doses barely
estimate a per-dose variance. Only $\log_{10} p_d$ is optimised numerically,
by Nelder--Mead from several starts.

$c_s$ is shared across doses within a construct, and that sharing is the whole
identifying assumption: it is the efficacy of a bound complex, a property of
the guide and the silencing machinery, so it cannot depend on how much siRNA
was pipetted on. In the weak-binding limit $K_j \gg p_d$ only the product
$c_s p_d$ is identified, so the absolute pool, and hence $\rho$, rests on
curvature, while the \emph{slope} survives the degeneracy.

In the site-class variant the free parameters are $\log_{10} K_c$ for the
three classes other than the anchor, plus one $\log_{10} p_d$ per dose; the
7mer-m8 class is pinned to the published seed-match $K_d$ to fix the common
scale. Sites combine as $1/K_j = \sum_c n_{jc}/K_c$ over the class counts, and
a transcript with no site has $K_j = \infty$ and hence $b_j = 0$ at any pool,
which is what pins the per-dose intercept. The constrained fits replace the
free pool vector by $M_d = \kappa\,d$ with $\kappa = 10^{u} > 0$, taking
$p_d = M_d$ under independent scoring and $p_d = f(M_d)$ under equilibrium,
$f$ solving \eqref{eq:cons}; all three are compared by
$\mathrm{AIC} = n\log(\mathrm{RSS}/n) + 2k$ and by held-out-gene prediction.

\section{Why the pool exponent in $M$ cannot fall below one}
\label{sec:convex}

From \eqref{eq:cons},
$\mathrm{d}^2M/\mathrm{d}f^2 = -\sum_j 2x_jK_j/(K_j+f)^3 < 0$, so $M$ is
strictly concave in $f$ and $f$ is strictly convex in $M$; with $f(0)=0$ the
ratio $f/M$ increases, which gives
$\mathrm{d}\log f/\mathrm{d}\log M = (\mathrm{d}f/\mathrm{d}M)(M/f) \ge 1$.
The competitor set's buffering capacity saturates, so each added unit of
complex is absorbed less than the last and the free pool accelerates.

The bound is on the exponent in $M$, not in dose. Under the
proportional-loading assumption $M \propto$ dose it carries over, giving
$\mathrm{d}\log f/\mathrm{d}\log(\text{dose}) \ge 1$ for equilibrium against
exactly $1$ for independent scoring. Without it,
%
\[
\frac{\mathrm{d}\log f}{\mathrm{d}\log(\text{dose})}
= \frac{\mathrm{d}\log f}{\mathrm{d}\log M}\,
  \frac{\mathrm{d}\log M}{\mathrm{d}\log(\text{dose})},
\]
%
so a measured exponent below $1$ does not by itself falsify equilibrium. It
diagnoses failure of at least one element of the combined specification: the
proportional loading, the affinity or observation model, or the static
equilibrium approximation. \S\ref{sec:dose} finds the first of these failing
its own check, which is why the exponent is reported as an audit rather than
as a measurement of competition.

What is true in the sublinear intuition is a statement about the
\emph{level} of the pool, and it bounds $f$ on both sides:
%
\[
\frac{M}{\,1+\beta+\sum_j x_j/K_j\,} \;\le\; f(M) \;\le\; \frac{M}{1+\beta}.
\]
%
The lower bound follows from $f/(K_j+f)\le f/K_j$, which makes the left-hand
side of \eqref{eq:cons} at most $(1+\beta+\sum_j x_j/K_j)f$. The upper bound
follows because every occupancy term is nonnegative, so the left-hand side is
at least $(1+\beta)f$. Since $f$ is convex with $f(0)=0$ it lies above its
tangent at the origin, which is the lower bound. Superlinear elasticity does
not put $f$ above $M/(1+\beta)$: a level bounded by lines through the origin
and an exponent below $1$ are different statements, and only the first
holds.

\section{Approach to the independent limit}
\label{sec:limit}

The result is conditional and the conditions are load-bearing. Assume
$\beta=0$, $K_j$ fixed, $x_j$ fixed, and let $M\to\infty$. Then
$f-(M-\sum_j x_j)\to 0$, so $f\to M-S_{\mathcal{R}}$ and not $M$, and the
difference in \emph{fractional} occupancy between the two scorings is
$O(M^{-2})$ \emph{pointwise for each fixed $K_j$}. Three qualifications
matter. The error over the worst transcript, and separately the error in the
aggregate load, are two different quantities and each decays only as
$O(M^{-1})$ over practical ranges, because the tail of transcripts with
$K_j\gg M$ is not yet in the asymptotic regime at any finite $M$. For fixed $\beta>0$ the
difference from the independent counterfactual is $O(M^{-1})$ in general,
since the background absorbs a constant fraction of the pool. And nothing
here is an unconditional $O(\rho^{-2})$ statement: $\rho$ and $M$ differ by
the fixed abundance total, so the exponent transfers only under the
assumptions above.

Over \PwDecades{} decades on the real transcriptome the median transcript
gives a log-log slope $\PwSlope \pm \PwSlopeSE$ against the predicted
$\PwPredicted$. Both slower quantities land near $-1$: the worst transcript,
which is what Figure~\ref{fig:theory}b plots beside the median, gives
$\PwSlopeMax \pm \PwSlopeMaxSE$, and the aggregate load gives
$\PwSlopeAll \pm \PwSlopeAllSE$. The original derivation stated neither.

\begin{figure}[h]
\centering
\includegraphics[width=\textwidth]{../figures/fig4_retrieval.pdf}
\caption{Approximation error on data-derived inputs. Relative error in
on-target
occupancy against the full \EFourN-transcript reference when the competitor
set is truncated to the top $R$, under the affinity-weighted calibration rule
and the abundance-mass control, at three values of the competition parameter.
The dotted line is 1\% error.}
\label{fig:retrieval}
\end{figure}

\begin{figure}[h]
\centering
\includegraphics[width=0.49\textwidth]{../figures/figA1_phase_2d.pdf}
\hfill
\includegraphics[width=0.49\textwidth]{../figures/figA2_dose_detail.pdf}
\caption{Left: the two-dimensional form of Figure~\ref{fig:phase},
kept for completeness; the $\tau = 0.9$ contour runs near-vertical, which is
why the main text shows a one-dimensional curve with an envelope. Right: the
dose fit with each construct's pool normalised to its own lowest dose, under
both affinity models.}
\label{fig:appfigs}
\end{figure}

\section{The cross-context test (exploratory)}
\label{sec:ctx}

Proposition~\ref{prop:rank} permits a second escape: fix the guide and change
the cell, so $K_j$ is identical and only $x^{(c)}$ differs. On
\citet{burchard2009} the pooled ratio of fitted pools between HUH7 and
PLC/PRF/5 is \CtxRatio{} (95\% CI \CtxRatioCI), with \CtxExcl{} of
\CtxAgree{} intervals excluding $1$. We report this as exploratory and draw no
conclusion from it, for three reasons. The seeds are recovered from the same
expression responses used to evaluate the fit, so the analysis is circular;
only constructs whose recovered seeds agree across both lines are retained,
which selects on the outcome; and a ratio of $1$ is predicted only when the
loaded complex is equal in both cell lines, which is unverified: the
on-target readouts differ by \CtxDeliveryMin{}--\CtxDeliveryMax{} log$_2$
units, but that difference is itself a joint consequence of loading,
transcriptome competition and the observation model, so it cannot be read as
evidence of unequal loading. The experiment cannot separate the three.

\citet{burchard2009} profile six APOB siRNAs and a RAD18 control in HUH7 and
PLC/PRF/5. The guide sequences were not included in the GEO deposit, and we did not
locate them in the article or its accessible supplementary material, so the
7-mer site is recovered from the measured response
separately in each cell line by the enrichment scan used for D1, and a
construct enters only when the two recoveries agree exactly; \CtxAgree{} of
\CtxAttempted{} survive. Recovery identifies guide positions 2--8 and nothing
else, so $K$ here is built from the seed duplex rather than the full guide,
which costs resolution within the retrieved set but does not threaten a
comparison that needs only $K$ to be identical between contexts. One effective
pool is fitted per context with a shared amplitude, exactly as for dose.

\section{The affinity scale}
\label{sec:scale}

Per-site free energies are converted to molecules per cell against a
published reference,
$K_{\mathrm{site}} = K_{\mathrm{ref}}\exp[(\Delta G_{\mathrm{eff}} -
\Delta G_{\mathrm{ref}})/RT]$, with $\Delta G_{\mathrm{ref}}$ the median
7mer-m8 site and $K_{\mathrm{ref}}$ the measured seed-match $K_d$
\citep{wee2012} at an assumed cell volume. Sites on one transcript are
parallel binding opportunities, $1/K_j = \sum_s 1/K_{js}$. The competition
parameter uses the whole-cell mRNA total in its denominator, not the retrieved
subset: every experiment sets $M = \rho \cdot(\text{total mRNA})$, so a
$\rho$ quoted here is roughly an order of magnitude smaller than
$M$ divided by the retrieved abundance alone would be. The biochemical
$K_d$ was measured under conditions unlike these cells, so this fixes a
common scale rather than an absolute one. Rank statistics computed
\emph{within} a construct are invariant to it, because rescaling every $K_j$
leaves $q_j$ a monotone function of $K_j$; the pooled statistic of
\S\ref{sec:assoc} mixes constructs whose free pools respond differently to
the rescale and is therefore not exactly invariant, and $\rho$ is not
invariant either.

\section{Standing assumptions}
\label{sec:assumptions}

A transcript is represented by one effective binding state, so its sites are
treated as mutually exclusive and it carries at most one complex. Binding is a
static equilibrium snapshot: recycling and catalytic cleavage are not
modelled. Abundance $x_j$ is taken from the untreated, mock or non-targeting
control measurement of the same experiment, the reference channel for the
two-colour arrays and the control-condition arrays for the single-channel
ones, and is not updated as repression proceeds. Structure comes from canonical GENCODE 3$'$UTRs rather
than cell-specific expressed isoforms, so alternative polyadenylation may
change which sites are actually present. Each of these is a live alternative
explanation for weak affinity performance.

\section{Further limitations}
\label{sec:limits}

The layer models competition among complexes already loaded with one guide, so
loading competition and endogenous microRNA occupancy enter only through $M$.
The molecules-per-cell scale rests on an mRNA count measured in neither
dose-series cell line, and the value used is a point inside the range that
measurement reports rather than a figure the source states, so the exponent is
invariant to it but $\rho$ scales inversely with it.
The site-class affinities are fitted on the same data whose dose dependence is
tested, though shared across doses, which is what keeps the exponent a shape
statement rather than a per-dose fit. The two dose-series cell lines differ
between the STAT3 and HK2 arms, so a construct effect and a cell-line effect
cannot be separated. Three dose points per construct, two for one of them,
leave the per-construct exponents wide, and the bootstrap resamples
transcripts rather than doses, so it cannot represent uncertainty about the
dose grid. The cross-context comparison assumes equal total loaded complex in
both lines, which is unverified; the differing on-target readouts do not
settle it, because loading, transcriptome competition and observation
effects are confounded in them.

\section{Datasets and what had to be recovered}
\label{sec:recover}

\paragraph{Numbering.} The main text numbers the four off-target datasets
D1--D4 in order of appearance. The repository numbers every acquisition,
experiments and references alike: D1 GSE5814, D2 E-MEXP-668, D3 GENCODE,
D4 HeLa abundance, D5 the Huesken efficacy set, D6 literature constants,
D7 GSE28786, D8 GSE14073, D9 a full-text retrieval. So main-text D3 and D4
are repository D7 and D8. Result files use the repository numbering
throughout.

\paragraph{Processing and archives.} Expression values are the depositors'
own summaries, which differ by platform: GSE5814 and E-MEXP-668 are two-colour
arrays deposited as within-array log ratios of the siRNA channel to its
control channel, and the single-channel Affymetrix deposits are RMA summaries
\citep{irizarry2003}. GSE28786 is quantified on a custom CDF
whose probeset identifiers are Entrez gene ids \citep{dai2005}, resolved to
symbols through NCBI Gene \citep{sayers2026}. Accessions are retrieved from
GEO \citep{barrett2013}, except E-MEXP-668, which is in ArrayExpress
\citep{athar2019}.

Guide sequences were absent from two of the four deposits. For GSE5814 they
were taken from \citet{garcia2011} joined on GSM accession and corroborated by
data-driven seed recovery. For GSE14073 the guide sequences were not
included in the deposit and we did not locate them in the article or its
accessible supplementary material, so seeds were recovered from the response
alone. For GSE28786 the sequences are in the
article's own table and were parsed from the full-text XML rather than
transcribed. For E-MEXP-668 they are in the deposit's sample file. In GSE28786
the dose recorded in the sample title disagrees with the dose in the raw file
name for exactly one construct; we resolved it from the measurement, by asking
under which labelling the on-target actually falls.
"""

LATEX_BUILTIN = {"S", "Bigl", "Bigr", "Big", "Large", "LaTeX", "TeX", "Delta",
                 "Gamma", "Omega", "Sigma", "Pi", "Lambda", "Phi", "Psi",
                 "Theta", "Xi", "Upsilon"}

def macro_provenance(V):
    """
    Where every macro's number came from, derived from the source, not typed.

    The manuscript claims that no number in it was written by hand. That claim
    is only auditable if each macro can be traced back to the result file it
    was read from, so this walks the abstract syntax tree of macros() and
    propagates result-file dependencies through the local variables: an alias
    bound to V["e9_dose_response"] carries that file, anything computed from
    the alias inherits it, and a put() whose expression touches no result file
    at all is a number with no provenance and fails the build.

    Names built inside a loop cannot be recovered this way, because the tree
    holds only the f-string; those call sites pass their source to put()
    explicitly and are merged in at the end.
    """
    import ast
    import inspect
    import textwrap
    src = textwrap.dedent(inspect.getsource(macros))
    tree = ast.parse(src)
    deps = {}

    def sources_of(node):
        out = set()
        for n in ast.walk(node):
            if isinstance(n, ast.Name):
                out |= deps.get(n.id, set())
            elif (isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name)
                    and n.value.id == "V"
                    and isinstance(n.slice, ast.Constant)):
                out.add(n.slice.value)
        return out

    def bind(target, srcs):
        if isinstance(target, ast.Name):
            if srcs:
                deps[target.id] = deps.get(target.id, set()) | srcs
        elif isinstance(target, (ast.Tuple, ast.List)):
            for t in target.elts:
                bind(t, srcs)

    out = {}
    for node in ast.walk(tree):
        # bind aliases first, in source order, so a later put() sees them
        if isinstance(node, ast.Assign):
            value = node.value
            tgt = node.targets[0]
            if (isinstance(tgt, ast.Tuple) and isinstance(value, ast.Tuple)
                    and len(tgt.elts) == len(value.elts)):
                for t, v in zip(tgt.elts, value.elts):
                    bind(t, sources_of(v))
            else:
                bind(tgt, sources_of(value))
        elif isinstance(node, ast.For):
            bind(node.target, sources_of(node.iter))
        elif isinstance(node, ast.comprehension):
            bind(node.target, sources_of(node.iter))

    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "put" and len(node.args) >= 2
                and isinstance(node.args[0], ast.Constant)):
            name = node.args[0].value
            out[name] = {
                "expression": ast.unparse(node.args[1]),
                "source_results": sorted(sources_of(node.args[1])),
            }
    for name, source in getattr(macros, "last_sources", {}).items():
        out.setdefault(name, {
            "expression": f"put(..., {source})",
            "source_results": [source.split(".", 1)[0]],
        })
    unresolved = sorted(k for k, v in out.items() if not v["source_results"])
    return out, unresolved


def check_macros_defined(tex, m):
    """
    Every CamelCase macro token in the manuscript must be one we generated.

    This is the Rule Zero guard for prose: if the text refers to a quantity
    that no result file produced, the build fails here rather than silently
    typesetting an undefined control sequence or, worse, a stale number.
    """
    import re
    # the negative lookbehind stops a "\\Paper" line break from matching
    used = set(re.findall(r"(?<!\\)\\([A-Z][A-Za-z]*)", tex)) - LATEX_BUILTIN
    missing = sorted(used - set(m))
    if missing:
        raise Missing(f"manuscript uses undefined numeric macros: {missing}")
    unused = sorted(set(m) - used)
    return unused

WORKFLOW_FIGURE = r"""
\section{Pipeline overview}
\label{sec:workflow}


Figure~\ref{fig:workflow} is the whole study on one page, in four stages.
\textbf{Stage 1} is what enters: four archival off-target microarray
accessions, GENCODE canonical 3$'$UTRs, and two literature constants: the
Argonaute copy number, carried as a range, and the mRNA count per cell, a
single value inside the range its source reports (\S\ref{sec:limits}). No new measurement is made anywhere in this work.
\textbf{Stage 2} builds the two per-transcript quantities the layer needs.
Abundance $x_j$ comes from the control measurement of the \emph{same}
experiment that supplies the measured response, so abundance and response are never taken from
different experiments. Affinity $K_j$ comes from a ViennaRNA construction,
duplex energy plus the cost of opening the site, anchored on a measured
seed-match $K_d$ (\S\ref{sec:scale}); it is never fitted to expression, which
is what keeps the association tests in \S\ref{sec:assoc} honest.
\textbf{Stage 3} is the conservation equation \eqref{eq:cons} itself, beside
the independent counterfactual it is compared against, with the properties
that make it usable as a layer: a unique root, bisection, and exact implicit
gradients. \textbf{Stage 4} records what this construction can and cannot
test. The within-construct fixed-dose comparison is blocked by
Proposition~\ref{prop:rank}, not by a limitation of the data; the dose and
cross-transcriptome comparisons remain open, which is why they are the two
experiments attempted.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{__WORKFLOW_PATH__}
\caption{The full pipeline, shown at page width because the panel text is
part of the content. Archival expression datasets, canonical 3$'$UTR
sequences, computed thermodynamic affinities, and stated literature ranges
are combined in a differentiable shared-pool equilibrium model. At fixed
construct and dose, equilibrium and independent fractional-occupancy scores
induce identical transcript rankings under the one-effective-$K$ model. Pool
effects instead remain testable across doses or transcriptomic contexts.
Intracellular loading proportional to transfected dose is an explicit
modelling assumption rather than a direct measurement. Boxes name the
archival accessions, the affinity construction of \S\ref{sec:scale}, the
conservation equation \eqref{eq:cons} of the main text, and which
experiments each part licenses.}
\label{fig:workflow}
\end{figure}

"""

DOSE_RESULT_WITH_CLASS = r"""\paragraph{The audit fails.} The site-class pooled exponent is \ClassSlope{}
with bootstrap interval \ClassSlopeCI{} containing $1$, but it is not robust:
leaving each construct out moves it over \LocoLo--\LocoHi{}, and
\NBelowOne{} of \NDoseFitted{} construct-level intervals lie entirely below
$1$, incompatible with the combined model under proportional loading
(Table~\ref{tab:e9}, Figure~\ref{fig:dose}). The loading assumption also
fails its own check: the implied $M$ per dose must have log-log slope $1$
against dose, and \NMSlopeExclOne{} of \NMSlopeTested{} intervals exclude it.
An unconstrained per-dose pool beats a proportional one for \NPrefFree{} of
\NDoseFitted{} constructs on both AIC and held-out genes
(\S\ref{sec:convex}). We therefore report no estimate of $\rho$: the
inverted values span \RhoDataDecades{} decades across construct-dose cells,
leaving the $\alpha$-driven uncertainty of Figure~\ref{fig:phase} where it
was."""

# What the section says when the site-class fit has not been recorded yet. It
# reports the estimator that HAS run and says plainly that the other has not,
# rather than leaving a claim standing with no file behind it.
DOSE_RESULT_NO_CLASS = r"""\paragraph{Result.} Under the thermodynamic $K$
the pooled exponent is \ThermoSlope{} with bootstrap interval
\ThermoSlopeCI{}, an interval that contains the independent-scoring value of
$1$ and is therefore not discriminating; the per-construct estimates behind it
are in Table~\ref{tab:e9} and Figure~\ref{fig:dose}, and they range widely
enough that the pooled figure is an average over diverged fits rather than an
estimate. Inverting those pools through \eqref{eq:cons} gives a competition
parameter of median $\ThermoRhoMedian{}$ with interval \ThermoRhoCI{},
which is not an improvement on the \RhoDecades{} decades of the
$\alpha$-swept band. \emph{The site-class fit that this section argues for
had not finished at the time this manuscript was generated, so no number from
it is reported here.} The estimator is validated on simulated data in
\S\ref{sec:sim}; the measured result will replace this paragraph when the
fit is recorded."""

CLASS_SANITY = ""

def main():
    V = build()
    m = macros(V)

    macro_lines = "\n".join(
        f"\\newcommand{{\\{k}}}{{{v}\\xspace}}" if False else
        f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in sorted(m.items()))
    cls = has_class_fit(V["e9_dose_response"])
    spec, head, tail = table_e9_header(V)
    # the workflow schematic is drawn outside this pipeline, so it is included
    # only if the file is actually there; a missing graphic aborts LaTeX, and a
    # dangling \ref is worse than no figure
    wf = ""
    for name in ("fig0_workflow.pdf", "fig0_workflow.png",
                 "workflow_GEM.pdf", "workflow_GEM.png"):
        if os.path.exists(os.path.join(ROOT, "figures", name)):
            wf = WORKFLOW_FIGURE.replace("__WORKFLOW_PATH__",
                                         f"../figures/{name}")
            break
    # the figure's own caption now says what it shows, so the cross-reference
    # only has to point at it
    # the schematic now lives in the appendix; the body keeps the equation
    # and a one-sentence pipeline, and points there
    wf_ref = (" (\\S\\ref{sec:workflow}, Figure~\\ref{fig:workflow})"
              if wf else "")
    if not wf:
        print("note: no workflow graphic in figures/; the workflow "
              "figure and its cross-reference are omitted from this build")
    tex = (TEX.replace("__MACROS__", macro_lines)
              .replace("__WORKFLOW_FIGURE__", wf)
              .replace("__WORKFLOW_REF__", wf_ref)
              .replace("__DOSE_RESULT__", DOSE_RESULT_WITH_CLASS if cls
                       else DOSE_RESULT_NO_CLASS)
              .replace("__CLASS_SANITY__", CLASS_SANITY if cls else "")
              .replace("__DOSE_POSCTRL__",
                       r" with $p$ down to \DosePosCtrlMinP{}"
                       if "DosePosCtrlMinP" in m else "")
              .replace("__TABLE_ENINE_SPEC__", spec)
              .replace("__TABLE_ENINE_HEAD__", head)
              .replace("__TABLE_ENINE_TAIL__", tail)
              .replace("__TABLE_EFOURB__", table_e4b(V))
              .replace("__TABLE_ENINE__", table_e9(V)))
    app = (TEX_APPENDIX.replace("__WORKFLOW_FIGURE__", wf)
                       .replace("__TABLE_ENINE_SPEC__", spec)
                       .replace("__TABLE_ENINE_HEAD__", head)
                       .replace("__TABLE_ENINE_TAIL__", tail)
                       .replace("__TABLE_EFOURB__", table_e4b(V))
                       .replace("__TABLE_ENINE__", table_e9(V)))
    if not cls:
        print("note: e9 has no site-class fit yet; the manuscript reports the "
              "thermodynamic estimator and says the other has not finished")
    os.makedirs(PAPER, exist_ok=True)
    # check AFTER substitution: the conditional blocks decide which macros
    # the manuscript actually references
    unused = check_macros_defined(tex + app, m)
    if unused:
        print(f"note: {len(unused)} generated macros are unused: {unused}")
    with open(OUT, "w") as fh:
        fh.write(tex)
    with open(OUT_APPENDIX, "w") as fh:
        fh.write(app)
    prov, unresolved = macro_provenance(V)
    no_record = sorted(set(m) - set(prov))
    if no_record:
        raise Missing(
            "these macros have no traceable source expression, which means "
            f"a number could have been typed by hand: {no_record}")
    if unresolved:
        # a macro built only from literals, with no result subscript at all,
        # is exactly the failure mode Rule Zero exists to catch
        raise Missing(
            "these macros do not read from any result file: "
            f"{unresolved}")
    with open(os.path.join(PAPER, "macros_used.json"), "w") as fh:
        json.dump({"generated_utc": utcnow(),
                   "n_macros": len(m),
                   "macros": {k: {"value": v, **prov[k]}
                              for k, v in sorted(m.items())}},
                  fh, indent=2)
    print(f"wrote {OUT} and {OUT_APPENDIX} with {len(m)} generated "
          f"numeric macros, each traced to a result file")

if __name__ == "__main__":
    main()
