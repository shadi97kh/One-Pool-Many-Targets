"""
e4 - retrieval-depth invariance on the real human transcriptome.

The full retrieved competitor set for a real siRNA on GENCODE v50 3'UTRs with
measured HeLa abundances is the reference. Truncating to the top R competitors
and absorbing the remainder into the linear background should leave the
answer unchanged IF the background is calibrated correctly. Two rules:

    affinity weighted   beta = sum_{j not in R} x_j / K_j     (correct)
    abundance mass      beta = sum_{j not in R} x_j           (control)

The second is the rule a reviewer is likely to propose. It is run so that the
difference is measured rather than asserted.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
import torch                                                    # noqa: E402
from riscpool import calibration, runner                         # noqa: E402
from riscpool.equilibrium import risc_equilibrium                # noqa: E402
from riscpool.features import load_features, transcript_level  # noqa: E402
from riscpool.hela import load_abundance                         # noqa: E402
from riscpool.sirna import per_construct                         # noqa: E402

RS = [25, 50, 100, 200, 500, 1000, 2000, 5000]
RHOS = [0.01, 0.5, 10.0]
CONSTRUCT = "MAPK14-193_parent"


def solve(K, x, M, beta):
    Kt = torch.tensor(K, dtype=torch.float64)[None, :]
    xt = torch.tensor(x, dtype=torch.float64)[None, :]
    Mt = torch.tensor([[float(M)]], dtype=torch.float64)
    bt = torch.tensor([[float(beta)]], dtype=torch.float64)
    f, o = risc_equilibrium(Kt, xt, Mt, bt)
    return float(f.item()), o[0].numpy()


def fn(seed=0, construct=CONSTRUCT):
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

    # the on-target sits in the same vector, index 0 after sorting
    pc = per_construct()
    ont_dg = None
    import RNA
    from riscpool import kmers
    parent = pc.loc[pc.construct == CONSTRUCT, "guide_5to3_dna"].iloc[0]
    site = kmers.revcomp(parent).replace("T", "U")
    ont_dg = float(RNA.duplexfold(parent.replace("T", "U"), site).energy)
    kd_full = calibration.kd_molar_to_molecules_per_cell(
        cst["kd_full_complementarity_molar"]["central"],
        cst["hela_cell_volume_litres"]["central"])
    x_on = float(ab.query("gene_symbol=='MAPK14'").x_rel.iloc[0] * n_mrna)

    K_all = np.concatenate([[kd_full], tx.K.to_numpy()])
    x_all = np.concatenate([[x_on], tx.x.to_numpy()])
    N = len(K_all)
    order = np.argsort(-(x_all / K_all))          # strongest competitors first
    total_x = float(n_mrna)

    rows = []
    for rho in RHOS:
        M = rho * total_x
        f_full, o_full = solve(K_all, x_all, M, 0.0)
        ref_t = float(o_full[0])
        ref_load = float(o_full.sum())
        rows.append({"rho": rho, "R": N, "rule": "full reference",
                     "f": f_full, "o_target": ref_t,
                     "total_load": ref_load, "rel_err_o_target": 0.0,
                     "rel_err_total_load": 0.0, "converged": True})
        for rule in ("affinity_weighted_x_over_K", "abundance_mass_x"):
            for Rr in RS:
                if Rr >= N:
                    continue
                idx, out = order[:Rr], order[Rr:]
                if 0 not in idx:                  # keep the target retrieved
                    idx = np.concatenate([[0], idx[:-1]])
                    out = np.setdiff1d(order, idx, assume_unique=False)
                beta = (float((x_all[out] / K_all[out]).sum())
                        if rule.startswith("affinity")
                        else float(x_all[out].sum()))
                f, o = solve(K_all[idx], x_all[idx], M, beta)
                tpos = int(np.where(idx == 0)[0][0])
                tgt = float(o[tpos])
                load = float(o.sum() + beta * f)
                Kout = K_all[out]
                rows.append({
                    "rho": rho, "R": Rr, "rule": rule, "beta": beta, "f": f,
                    "o_target": tgt, "total_load": load,
                    "frac_omitted_with_K_below_f": float((Kout < f).mean()),
                    "median_K_omitted_over_f": float(np.median(Kout) / f)
                                               if f > 0 else float("inf"),
                    "linearisation_assumption_K_bg_much_greater_than_f":
                        bool((Kout > 10 * f).mean() > 0.95),
                    "rel_err_o_target": abs(tgt - ref_t) / abs(ref_t),
                    "rel_err_total_load": abs(load - ref_load)
                                          / abs(ref_load),
                    "converged": bool(np.isfinite(f) and f > 0),
                })

    aff = [r for r in rows if r.get("rule") == "affinity_weighted_x_over_K"]
    mas = [r for r in rows if r.get("rule") == "abundance_mass_x"]
    a25 = [r for r in aff if r["R"] == 25]
    m25 = [r for r in mas if r["R"] == 25]
    return {
        "construct": construct,
        "reference_set_size_including_on_target": int(N),
        "gencode_release": 50,
        "rho_values": RHOS,
        "R_values": RS,
        "on_target_dg_kcal": ont_dg,
        "on_target_kd_molecules_per_cell": kd_full,
        "total_mrna_molecules_per_cell": total_x,
        "table": rows,
        "max_rel_err_o_target_affinity_rule": float(
            max(r["rel_err_o_target"] for r in aff)),
        "max_rel_err_o_target_abundance_rule": float(
            max(r["rel_err_o_target"] for r in mas)),
        "mean_rel_err_o_target_affinity_rule": float(
            np.mean([r["rel_err_o_target"] for r in aff])),
        "mean_rel_err_o_target_abundance_rule": float(
            np.mean([r["rel_err_o_target"] for r in mas])),
        "rel_err_at_R25_affinity_rule": [r["rel_err_o_target"] for r in a25],
        "rel_err_at_R25_abundance_rule": [r["rel_err_o_target"] for r in m25],
        "assumption_diagnostic": (
            "The linear background (1+beta)f replaces X_bg f/(K_bg+f) and is "
            "valid only where K_bg >> f. frac_omitted_with_K_below_f measures "
            "directly how often that fails at each truncation depth. The "
            "affinity-weighted rule cannot rescue a truncation that removed "
            "transcripts whose K is comparable to or below the free pool, "
            "because those are not in the weak-binding tail at all. Ordering "
            "by x/K does not guarantee they are."),
        "n_rows_where_linearisation_holds": int(sum(
            1 for r in rows if r.get(
                "linearisation_assumption_K_bg_much_greater_than_f"))),
        "n_truncated_rows": int(sum(1 for r in rows if "rule" in r
                                    and r["rule"] != "full reference")),
        "K_calibrated_log10_min": float(np.log10(K_all.min())),
        "K_calibrated_log10_max": float(np.log10(K_all.max())),
        "synthetic_pilot_for_comparison": {
            "affinity_rule_at_R25_vs_4000_reference": 0.0004,
            "abundance_rule": "86% and non-converging",
            "note": "pilot figures quoted from the build brief for "
                    "comparison only; the measured values above supersede "
                    "them and were computed on the real transcriptome"},
    }


if __name__ == "__main__":
    runner.run("e4_retrieval_invariance", fn, seed=0)
