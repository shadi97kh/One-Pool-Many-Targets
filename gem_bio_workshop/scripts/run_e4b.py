"""
e4b - binned background at shallow retrieval depth.

e4 measured the failure: at R = 25 the linearised background is wrong by
tens of percent to tens of times, because it assumes K_j >> f for every
omitted transcript and that held in only 4 of 30 truncated rows. The
diagnosis was not that the affinity weighting is wrong but that a LINEAR
term cannot represent a saturable one when the omitted set is not weak.

This experiment replaces the single linear term with B saturable bins over
log K (riscpool/background.py) and asks how many bins are needed before the
truncated answer matches the full-transcriptome reference again.

Three things are reported and none is asserted:

  * the relative error against the full reference for every (B, R, rho),
    under both quantile and equal-width binning, so the binning choice is
    visible rather than hidden;
  * the smallest B that restores invariance at R = 25, at several stated
    error thresholds, because "restores invariance" is a threshold statement
    and the threshold is ours;
  * the fraction of omitted transcripts satisfying K >> f at each setting,
    which is the assumption that failed in the first place.

The B = 1 linear case is not a new number. It is the e4 rule recomputed and
compared against results/e4_retrieval_invariance.json, and the comparison is
reported as a pass or a fail.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
from riscpool import background as bg                           # noqa: E402
from riscpool import calibration, runner                        # noqa: E402
from riscpool.equilibrium import risc_equilibrium               # noqa: E402
from riscpool.features import load_features, transcript_level   # noqa: E402
from riscpool.hela import load_abundance                        # noqa: E402
from riscpool.provenance import ROOT                            # noqa: E402
from riscpool.sirna import per_construct                        # noqa: E402

import torch                                                    # noqa: E402

BS_REQUIRED = [1, 2, 3, 5, 10]      # the sweep the brief asks for
BS = BS_REQUIRED + [20, 50, 100, 200, 500]
RS = [25, 50, 100, 200, 500]
RHOS = [0.01, 0.5, 10.0]              # identical to e4, so rows line up
RULES = ["quantile", "equal_width"]
CONSTRUCT = "MAPK14-193_parent"
THRESHOLDS = [0.5, 0.1, 0.01, 0.001]
E4_PATH = os.path.join(ROOT, "results", "e4_retrieval_invariance.json")


def build_system(construct=CONSTRUCT):
    """
    The same K and x vectors e4 built, on the same construct. Rebuilt here
    rather than imported because e4's setup lives inside its own experiment
    function; the regression check against the stored e4 reference values is
    what guarantees the two constructions agree.
    """
    feats = load_features()
    scale = calibration.build_scale(feats)
    Cs = scale["K_scale_constant_C"]
    n_mrna = scale["mrna_molecules_per_cell"]
    cst = calibration.load_constants()

    tx = transcript_level()
    tx = tx[(tx.construct == construct)
            & np.isfinite(tx.K_transcript) & (tx.K_transcript > 0)].copy()
    tx["K"] = tx.K_transcript * Cs
    ab = load_abundance()[["transcript_id", "x_rel", "gene_symbol"]]
    tx = tx.drop(columns=["x_rel"]).merge(
        ab[["transcript_id", "x_rel"]], on="transcript_id", how="left")
    tx["x"] = tx.x_rel.fillna(0.0) * n_mrna
    tx = tx[tx.x > 0].reset_index(drop=True)

    kd_full = calibration.kd_molar_to_molecules_per_cell(
        cst["kd_full_complementarity_molar"]["central"],
        cst["hela_cell_volume_litres"]["central"])
    x_on = float(ab.query("gene_symbol=='MAPK14'").x_rel.iloc[0] * n_mrna)

    K_all = np.concatenate([[kd_full], tx.K.to_numpy()])
    x_all = np.concatenate([[x_on], tx.x.to_numpy()])
    order = np.argsort(-(x_all / K_all))
    return K_all, x_all, order, float(n_mrna)


def split(order, R, N):
    """Top-R retained, remainder omitted, with the on-target kept retained -
    exactly the rule e4 used."""
    idx, out = order[:R], order[R:]
    if 0 not in idx:
        idx = np.concatenate([[0], idx[:-1]])
        out = np.setdiff1d(order, idx, assume_unique=False)
    return idx, out


def weak_limit_diagnostics(K_out, f, X_bins, K_bins):
    d = {
        "frac_omitted_with_K_below_f": float((K_out < f).mean()),
        "frac_omitted_with_K_above_10f": float((K_out > 10 * f).mean()),
        "median_K_omitted_over_f": (float(np.median(K_out) / f) if f > 0
                                    else float("inf")),
        "linearisation_assumption_K_bg_much_greater_than_f":
            bool((K_out > 10 * f).mean() > 0.95),
    }
    if len(K_bins):
        Kb = np.asarray(K_bins, dtype=np.float64)
        d["frac_bins_with_K_b_above_10f"] = float((Kb > 10 * f).mean())
        d["min_K_b_over_f"] = float(Kb.min() / f) if f > 0 else float("inf")
    return d


def fn(seed=0, construct=CONSTRUCT):
    K_all, x_all, order, n_mrna = build_system(construct)
    N = len(K_all)
    total_x = n_mrna

    stored_e4 = None
    if os.path.exists(E4_PATH):
        with open(E4_PATH) as fh:
            j = json.load(fh)
        if j.get("status") == "OK":
            stored_e4 = j["values"]

    rows, refs = [], {}
    for rho in RHOS:
        M = rho * total_x
        Kt = torch.tensor(K_all, dtype=torch.float64)[None, :]
        xt = torch.tensor(x_all, dtype=torch.float64)[None, :]
        Mt = torch.tensor([[M]], dtype=torch.float64)
        f_full, o_full = risc_equilibrium(Kt, xt, Mt,
                                          torch.zeros_like(Mt))
        f_full = float(f_full.item())
        o_full = o_full[0].numpy()
        refs[rho] = {"f": f_full, "o_target": float(o_full[0]),
                     "total_load": float(o_full.sum())}
        rows.append({"rho": rho, "R": N, "B": None, "binning_rule":
                     "full reference", "background": "none", "f": f_full,
                     "o_target": float(o_full[0]),
                     "total_load": float(o_full.sum()),
                     "rel_err_o_target": 0.0, "rel_err_total_load": 0.0,
                     "rel_err_f": 0.0})

    regression = []
    for rho in RHOS:
        M = rho * total_x
        ref = refs[rho]
        for R in RS:
            if R >= N:
                continue
            idx, out = split(order, R, N)
            K_in, x_in = K_all[idx], x_all[idx]
            K_out, x_out = K_all[out], x_all[out]
            tpos = int(np.where(idx == 0)[0][0])

            # --- B = 1 linearised: the e4 rule, recomputed for regression ---
            beta = float((x_out / K_out).sum())
            f_lin, o_lin = bg.solve_linear(K_in, x_in, beta, M)
            tgt = float(o_lin[tpos])
            load = float(o_lin.sum() + beta * f_lin)
            lin_row = {
                "rho": rho, "R": R, "B": 1, "binning_rule": "n/a",
                "background": "linear_affinity_weighted_e4_rule",
                "beta": beta, "f": f_lin, "o_target": tgt,
                "total_load": load,
                "rel_err_o_target": abs(tgt - ref["o_target"])
                                    / abs(ref["o_target"]),
                "rel_err_total_load": abs(load - ref["total_load"])
                                      / abs(ref["total_load"]),
                "rel_err_f": abs(f_lin - ref["f"]) / abs(ref["f"]),
                "dF_df": bg.dF_df(f_lin, K_in, x_in, beta=beta),
            }
            lin_row.update(weak_limit_diagnostics(K_out, f_lin, [], []))
            rows.append(lin_row)

            if stored_e4 is not None:
                match = [r for r in stored_e4["table"]
                         if r.get("rule") == "affinity_weighted_x_over_K"
                         and r.get("R") == R and r.get("rho") == rho]
                if match:
                    m = match[0]
                    regression.append({
                        "rho": rho, "R": R,
                        "e4_stored_o_target": m["o_target"],
                        "e4b_recomputed_o_target": tgt,
                        "abs_diff_o_target": abs(m["o_target"] - tgt),
                        "e4_stored_f": m["f"],
                        "e4b_recomputed_f": f_lin,
                        "abs_diff_f": abs(m["f"] - f_lin),
                        "e4_stored_beta": m["beta"],
                        "e4b_recomputed_beta": beta,
                        "abs_diff_beta": abs(m["beta"] - beta),
                    })

            # --- binned saturable background ---
            for rule in RULES:
                for B in BS:
                    X_b, K_b, det = bg.bin_omitted(K_out, x_out, B, rule)
                    f_b, o_ret, o_bin = bg.solve_binned(K_in, x_in, X_b, K_b,
                                                        M)
                    tgt = float(o_ret[tpos])
                    load = float(o_ret.sum() + o_bin.sum())
                    row = {
                        "rho": rho, "R": R, "B": B, "binning_rule": rule,
                        "background": "binned_michaelis",
                        "n_bins_used": det["n_bins_used"],
                        "n_omitted": det["n_omitted"],
                        "f": f_b, "o_target": tgt, "total_load": load,
                        "rel_err_o_target": abs(tgt - ref["o_target"])
                                            / abs(ref["o_target"]),
                        "rel_err_total_load": abs(load - ref["total_load"])
                                              / abs(ref["total_load"]),
                        "rel_err_f": abs(f_b - ref["f"]) / abs(ref["f"]),
                        "dF_df": bg.dF_df(f_b, K_in, x_in, X_b, K_b, 0.0),
                        "bin_K_harmonic_log10":
                            [float(np.log10(k)) for k in K_b],
                        "bin_abundance_mass": det["bin_abundance_mass"],
                        "bin_n_transcripts": det["bin_n_transcripts"],
                    }
                    row.update(weak_limit_diagnostics(K_out, f_b, X_b, K_b))
                    rows.append(row)

    binned = [r for r in rows if r["background"] == "binned_michaelis"]
    linear = [r for r in rows if r["background"].startswith("linear")]

    def smallest_B(rule, R, thr, key="rel_err_o_target"):
        """Smallest B whose error is below thr at EVERY rho tested."""
        for B in BS:
            s = [r for r in binned if r["binning_rule"] == rule
                 and r["R"] == R and r["B"] == B]
            if len(s) == len(RHOS) and all(r[key] < thr for r in s):
                return B
        return None

    def smallest_B_required(rule, R, thr, key="rel_err_o_target"):
        b = smallest_B(rule, R, thr, key)
        return b if (b is not None and b in BS_REQUIRED) else None

    def smallest_B_at_rho(rule, R, rho, thr, key="rel_err_o_target"):
        for B in BS:
            s = [r for r in binned if r["binning_rule"] == rule
                 and r["R"] == R and r["B"] == B and r["rho"] == rho]
            if s and all(r[key] < thr for r in s):
                return B
        return None

    smallest = []
    for rule in RULES:
        for R in RS:
            for thr in THRESHOLDS:
                row = {
                    "binning_rule": rule, "R": R, "threshold": thr,
                    "smallest_B_all_rho_o_target": smallest_B(rule, R, thr),
                    "smallest_B_all_rho_total_load":
                        smallest_B(rule, R, thr, "rel_err_total_load"),
                    "smallest_B_within_required_sweep_o_target":
                        smallest_B_required(rule, R, thr),
                }
                for rho in RHOS:
                    row[f"smallest_B_at_rho_{rho}"] = smallest_B_at_rho(
                        rule, R, rho, thr)
                smallest.append(row)

    per_setting = []
    for rule in RULES:
        for R in RS:
            for B in BS:
                s = [r for r in binned if r["binning_rule"] == rule
                     and r["R"] == R and r["B"] == B]
                if not s:
                    continue
                lin = [r for r in linear if r["R"] == R]
                per_setting.append({
                    "binning_rule": rule, "R": R, "B": B,
                    "max_rel_err_o_target_over_rho": float(
                        max(r["rel_err_o_target"] for r in s)),
                    "mean_rel_err_o_target_over_rho": float(
                        np.mean([r["rel_err_o_target"] for r in s])),
                    "max_rel_err_total_load_over_rho": float(
                        max(r["rel_err_total_load"] for r in s)),
                    "max_rel_err_o_target_linear_rule": float(
                        max(r["rel_err_o_target"] for r in lin)) if lin
                        else None,
                    "mean_n_bins_used": float(
                        np.mean([r["n_bins_used"] for r in s])),
                    "mean_frac_omitted_with_K_above_10f": float(
                        np.mean([r["frac_omitted_with_K_above_10f"]
                                 for r in s])),
                    "n_rows_where_linearisation_holds": int(sum(
                        r["linearisation_assumption_K_bg_much_greater_than_f"]
                        for r in s)),
                    "n_rows": len(s),
                })

    reg_ok = None
    reg_max = None
    if regression:
        reg_max = float(max(
            max(r["abs_diff_o_target"] / max(abs(r["e4_stored_o_target"]),
                                             1e-300),
                r["abs_diff_f"] / max(abs(r["e4_stored_f"]), 1e-300))
            for r in regression))
        reg_ok = bool(reg_max <= 1e-12)

    at25 = [r for r in binned if r["R"] == 25]
    return {
        "construct": construct,
        "reference_set_size_including_on_target": int(N),
        "gencode_release": 50,
        "rho_values": RHOS, "R_values": RS, "B_values": BS,
        "B_values_required_by_brief": BS_REQUIRED,
        "B_sweep_extension_note": (
            "The brief asks for B in {1,2,3,5,10}. No B in that set restores "
            "invariance at R = 25, so the sweep was extended upward until the "
            "convergence is visible and the smallest sufficient B can be "
            "reported rather than merely bounded below. Both answers are "
            "given: smallest_B_within_required_sweep_o_target is restricted "
            "to the requested set and is null where none of them suffices."),
        "binning_rules": RULES,
        "error_thresholds_for_invariance": THRESHOLDS,
        "total_mrna_molecules_per_cell": total_x,
        "reference_by_rho": {str(k): v for k, v in refs.items()},

        "invariance_criterion": (
            "invariance is 'restored' at a given (rule, R, threshold) when "
            "the relative error of the on-target occupancy against the "
            "full-transcriptome reference is below the threshold at EVERY "
            "rho in rho_values, not merely on average. The threshold is a "
            "choice of ours and several are reported rather than one."),
        "smallest_B_restoring_invariance": smallest,
        "smallest_B_at_R25_quantile_threshold_0.01": next(
            (s["smallest_B_all_rho_o_target"] for s in smallest
             if s["binning_rule"] == "quantile" and s["R"] == 25
             and s["threshold"] == 0.01), None),
        "smallest_B_at_R25_quantile_threshold_0.1": next(
            (s["smallest_B_all_rho_o_target"] for s in smallest
             if s["binning_rule"] == "quantile" and s["R"] == 25
             and s["threshold"] == 0.1), None),
        "smallest_B_at_R25_equal_width_threshold_0.01": next(
            (s["smallest_B_all_rho_o_target"] for s in smallest
             if s["binning_rule"] == "equal_width" and s["R"] == 25
             and s["threshold"] == 0.01), None),

        "max_rel_err_o_target_at_R25_linear_rule": float(max(
            r["rel_err_o_target"] for r in linear if r["R"] == 25)),
        "max_rel_err_o_target_at_R25_binned_B10_quantile": float(max(
            r["rel_err_o_target"] for r in at25
            if r["B"] == 10 and r["binning_rule"] == "quantile")),
        "max_rel_err_o_target_binned_B10_quantile_all_R": float(max(
            r["rel_err_o_target"] for r in binned
            if r["B"] == 10 and r["binning_rule"] == "quantile")),

        "regression_against_e4": regression,
        "regression_against_e4_max_rel_diff": reg_max,
        "regression_against_e4_passes_at_1e-12": reg_ok,
        "regression_note": (
            "B = 1 with the omitted mass collapsed to a single LINEAR term is "
            "the affinity-weighted rule of e4. It is recomputed here through "
            "riscpool.background and compared row by row against the stored "
            "results/e4_retrieval_invariance.json. A mismatch would mean the "
            "two experiments no longer describe the same system and would "
            "invalidate the comparison, so it is checked rather than assumed."),

        "per_setting_summary": per_setting,
        "table": rows,
        "n_rows": len(rows),
        "weak_limit_note": (
            "frac_omitted_with_K_above_10f is the fraction of OMITTED "
            "transcripts in the weak-binding regime at the solved free pool. "
            "It is a property of the truncation, not of the background rule, "
            "so it is nearly the same for the linear and binned backgrounds "
            "at a given R; what changes is whether the background rule needs "
            "the assumption. The binned form does not, which is the point."),
    }


if __name__ == "__main__":
    runner.run("e4b_binned_background", fn, seed=0)
