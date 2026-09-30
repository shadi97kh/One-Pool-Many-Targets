"""
Series that figures plot but that no experiment previously recorded.

Rule Zero says a plotted value is read from results/*.json at render time.
Two panels of the rebuilt Fig 1 were previously computed inside the plotting
script, which meant the figure was the only record of them. That is exactly
the failure mode the rule exists to prevent, so the curves are computed here
and written to results/ like any other measurement.

  e5b_budget_curve         total occupancy against the RISC budget M, and the
                           ratio that makes the over-allocation legible
  e2b_redistribution_curve Proposition 1 as a curve rather than a violation
                           count: sweep one transcript's affinity and watch
                           the rest of the transcriptome take up the slack
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
import torch                                                    # noqa: E402
from riscpool import calibration, runner                        # noqa: E402
from riscpool.equilibrium import (pairwise_occupancy,           # noqa: E402
                                  risc_equilibrium)
from riscpool.features import load_features, transcript_level   # noqa: E402
from riscpool.hela import load_abundance                        # noqa: E402

CONSTRUCT = "MAPK14-193_parent"
N_BUDGET = 60
RHO_LO, RHO_HI = -5.0, 2.0
K_SWEEP_DECADES = (-4.0, 6.0)
N_KSWEEP = 60
REDIST_RHOS = [0.01, 0.1875, 2.0]


def hela_system(construct=CONSTRUCT):
    """The real (K, x) system: the same one e4, e5 and e7 use."""
    feats = load_features()
    scale = calibration.build_scale(feats)
    C, n_mrna = scale["K_scale_constant_C"], scale["mrna_molecules_per_cell"]
    tx = transcript_level()
    tx = tx[(tx.construct == construct)
            & np.isfinite(tx.K_transcript) & (tx.K_transcript > 0)]
    ab = load_abundance()[["transcript_id", "x_rel"]]
    tx = tx.drop(columns=["x_rel"]).merge(ab, on="transcript_id", how="left")
    tx = tx[tx.x_rel.notna() & (tx.x_rel > 0)].reset_index(drop=True)
    K = tx.K_transcript.to_numpy() * C
    x = tx.x_rel.to_numpy() * n_mrna
    return K, x, scale, tx


def budget(seed=0):
    K, x, scale, tx = hela_system()
    n_mrna = scale["mrna_molecules_per_cell"]
    Kt = torch.tensor(K, dtype=torch.float64)[None, :]
    xt = torch.tensor(x, dtype=torch.float64)[None, :]
    rows = []
    for r in np.logspace(RHO_LO, RHO_HI, N_BUDGET):
        M = float(r * n_mrna)
        Mt = torch.tensor([[M]], dtype=torch.float64)
        _, o = risc_equilibrium(Kt, xt, Mt)
        p = pairwise_occupancy(Kt, xt, Mt)
        eq, pw = float(o.sum()), float(p.sum())
        rows.append({"rho": float(r), "M": M,
                     "independent_total_occupancy": pw,
                     "equilibrium_total_occupancy": eq,
                     "independent_over_M": pw / M,
                     "equilibrium_over_M": eq / M})
    worst = max(rows, key=lambda q: q["independent_over_M"])
    cst = calibration.load_constants()

    # Where does the counterfactual actually break the budget? The worst ratio
    # sits at a pool of well under one complex per cell, which is outside any
    # defensible range and is not a claim worth making. The honest statement is
    # a threshold on the loaded fraction alpha: at the MEASURED Argonaute copy
    # numbers with alpha = 1 there is no over-allocation at all.
    lo_a = cst["ago2_copies_per_cell"]["low"]
    hi_a = cst["ago2_copies_per_cell"]["high"]
    lm = np.log10([q["M"] for q in rows])
    lr = np.log10([q["independent_over_M"] for q in rows])
    at_lo = float(10 ** np.interp(np.log10(lo_a), lm, lr))
    at_hi = float(10 ** np.interp(np.log10(hi_a), lm, lr))
    below = np.where(np.array([q["independent_over_M"] for q in rows]) < 1)[0]
    cross = (float(10 ** np.interp(0.0, [lr[below[0]], lr[below[0] - 1]],
                                   [lm[below[0]], lm[below[0] - 1]]))
             if below.size and below[0] > 0 else float("nan"))
    return {
        "construct": CONSTRUCT,
        "n_retrieved_transcripts": int(len(K)),
        "sum_x_retrieved_molecules_per_cell": float(x.sum()),
        "total_mrna_molecules_per_cell": float(n_mrna),
        "curve": rows,
        "max_independent_over_M": worst["independent_over_M"],
        "independent_over_M_at_ago2_measured_low": at_lo,
        "independent_over_M_at_ago2_measured_high": at_hi,
        "crossover_M_where_independent_equals_budget": cross,
        "alpha_threshold_for_over_allocation_vs_ago2_low": cross / lo_a,
        "alpha_threshold_for_over_allocation_vs_ago2_high": cross / hi_a,
        "over_allocation_note": (
            "max_independent_over_M is attained at a pool of well under one "
            "complex per cell, outside any defensible range, and should not "
            "be quoted as a headline. At the measured Argonaute copy numbers "
            "with alpha = 1 the independent counterfactual allocates LESS "
            "than the budget, so the over-allocation is conditional: it "
            "occurs only when the loaded fraction falls below "
            "alpha_threshold_for_over_allocation_vs_ago2_low against the "
            "HeLa-specific measurement."),
        "max_independent_over_M_at_rho": worst["rho"],
        "max_independent_over_M_at_M": worst["M"],
        "equilibrium_plateau_equals_sum_x": bool(
            abs(rows[-1]["equilibrium_total_occupancy"] - x.sum())
            / x.sum() < 0.05),
        "ago2_measured_low_copies_per_cell":
            cst["ago2_copies_per_cell"]["low"],
        "ago2_measured_high_copies_per_cell":
            cst["ago2_copies_per_cell"]["high"],
        "ago2_measurement_note": (
            "the low value is the only HeLa-specific measurement found "
            "(Janas et al., AQUA mass spectrometry, Ago1-4); the high value "
            "is from a different cell type and method. Both are measured "
            "copy numbers and neither is a sweep, which is why the figure "
            "marks them differently from the alpha-swept band."),
        "interpretation": (
            "independent_over_M above 1 means the independent pairwise "
            "counterfactual allocates more loaded RISC than the cell "
            "contains. It is a counterfactual about what those affinities "
            "imply if transcripts are scored in isolation, not a claim about "
            "any published predictor's output."),
    }


def redistribution(seed=0):
    """
    Proposition 1 as a curve. One transcript's K is swept over decades; its
    own occupancy falls as K rises and every other transcript's rises, because
    the pool it releases has to go somewhere. The target is chosen by a stated
    rule rather than picked to look good: the transcript with median x/K among
    the retrieved set.
    """
    K, x, scale, tx = hela_system()
    n_mrna = scale["mrna_molecules_per_cell"]
    order = np.argsort(x / K)
    t = int(order[len(order) // 2])
    series = []
    for rho in REDIST_RHOS:
        M = float(rho * n_mrna)
        pts = []
        for kt in np.logspace(*K_SWEEP_DECADES, N_KSWEEP):
            Kv = K.copy()
            Kv[t] = kt
            Kt = torch.tensor(Kv, dtype=torch.float64)[None, :]
            xt = torch.tensor(x, dtype=torch.float64)[None, :]
            Mt = torch.tensor([[M]], dtype=torch.float64)
            f, o = risc_equilibrium(Kt, xt, Mt)
            o = o[0].numpy()
            pts.append({"K_target": float(kt),
                        "o_target": float(o[t]),
                        "o_others_sum": float(o.sum() - o[t]),
                        "free_pool_f": float(f.item())})
        ot = np.array([q["o_target"] for q in pts])
        oo = np.array([q["o_others_sum"] for q in pts])
        series.append({
            "rho": rho, "M": M, "points": pts,
            "o_target_is_monotone_decreasing_in_K": bool(
                np.all(np.diff(ot) <= 1e-18)),
            "o_others_is_monotone_increasing_in_K": bool(
                np.all(np.diff(oo) >= -1e-18)),
            "o_target_fold_change_over_sweep": float(ot[0] / ot[-1])
                                               if ot[-1] > 0 else float("inf"),
            "o_others_fold_change_over_sweep": float(oo[-1] / oo[0])
                                               if oo[0] > 0 else float("inf"),
        })
    return {
        "construct": CONSTRUCT,
        "n_retrieved_transcripts": int(len(K)),
        "target_selection_rule": "transcript with the median x/K in the "
                                 "retrieved set",
        "target_index": t,
        "target_transcript_id": str(tx.transcript_id.iloc[t]),
        "target_gene_symbol": str(tx.gene_symbol.iloc[t]),
        "target_K_original": float(K[t]),
        "target_x": float(x[t]),
        "K_sweep_log10_range": list(K_SWEEP_DECADES),
        "rho_values": REDIST_RHOS,
        "series": series,
        "all_series_monotone_as_proposition_requires": bool(all(
            s["o_target_is_monotone_decreasing_in_K"]
            and s["o_others_is_monotone_increasing_in_K"] for s in series)),
    }


if __name__ == "__main__":
    runner.run("e5b_budget_curve", budget, seed=0)
    runner.run("e2b_redistribution_curve", redistribution, seed=0)
