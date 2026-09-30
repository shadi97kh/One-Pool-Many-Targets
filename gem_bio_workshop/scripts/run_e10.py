"""
e10 - the same guide in two transcriptomes.

The construct is fixed and the cell line changes, so K_j is identical between
the two contexts by construction and only the abundance vector x^(c) differs.
Independent scoring says the bound fraction M/(K_j+M) cannot notice that.
Equilibrium says the free pool must satisfy conservation against x^(c), so a
context carrying more high-affinity competitor mass leaves less free pool and
a weaker off-target signature.

The estimator is the one e9 uses for dose, applied to context: one effective
pool per context, one amplitude shared between them, K held fixed. The
observed ratio of the two fitted pools is then compared against 1, which is
the independent prediction, and against the ratio conservation predicts from
the two measured abundance vectors at a common total complex.

THE CONFOUND, STATED UP FRONT. Independent scoring predicts a pool ratio of 1
only if the total loaded complex M is the same in both cell lines. It is not
measured. Two cell lines transfected with the same nominal 10 nM can differ
in uptake, in Argonaute abundance and in loading. So a pool ratio away from 1
is evidence for competition OR for unequal delivery, and this experiment
cannot separate them on its own. What it can do is report the on-target
knockdown in each context as a delivery readout, which is done below, and
report the size of the competitive effect the transcriptomes would have to
produce. That is weaker than the brief implies and it is reported as weaker.

THE SEED IS RECOVERED, NOT ASSUMED. The guide sequences were never deposited
and the article is closed; both failures are in the ledger. The 7-mer site is
recovered from the measured response independently in EACH cell line and a
construct is analysed only if the two recoveries agree exactly. Constructs
that fail that test are reported with their disagreeing top hits rather than
being quietly dropped.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
from riscpool import calibration, crosscontext as CC            # noqa: E402
from riscpool import dosefit as DF, runner                      # noqa: E402

CELLS = ("HUH7", "PLC/PRF/5")
HOURS = [6.0, 12.0, 48.0]
RHO_GRID = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0]
N_BOOT = 300
MIN_TRANSCRIPTS = 100


def fn(seed=0):
    rng = np.random.default_rng(seed)
    cand = CC.load_candidates()
    resp_all = CC.load_response()
    resp = resp_all[resp_all.hours.isin(HOURS)]
    ab_all = CC.load_abundance()

    # ---- seed recovery, independently per cell line -----------------------
    G = None
    recovery, seeds = [], {}
    for c in sorted(CC.TARGET_OF):
        tops = {}
        for cell in CELLS:
            top, n_used, G = CC.recover_seed(resp, c, cell, cand, G=G)
            tops[cell] = top
        a, b = tops[CELLS[0]][0], tops[CELLS[1]][0]
        agree = a["site_kmer"] == b["site_kmer"]
        rec = {
            "construct": c, "agree_exact_7mer": bool(agree),
            "top_site_HUH7": a["site_kmer"],
            "welch_t_HUH7": a["welch_t"],
            "delta_mean_log2fc_HUH7": a["delta_mean_log2fc"],
            "top_site_PLC": b["site_kmer"],
            "welch_t_PLC": b["welch_t"],
            "delta_mean_log2fc_PLC": b["delta_mean_log2fc"],
            "n_transcripts_with_site": a["n_transcripts_with_site"],
            "share_a_6mer": bool(
                len(set([a["site_kmer"][:6], a["site_kmer"][1:]])
                    & set([b["site_kmer"][:6], b["site_kmer"][1:]])) > 0),
            "top10_HUH7": [x["site_kmer"] for x in tops[CELLS[0]]],
            "top10_PLC": [x["site_kmer"] for x in tops[CELLS[1]]],
        }
        recovery.append(rec)
        if agree:
            seeds[c] = a["site_kmer"]

    if not seeds:
        raise RuntimeError("seed recovery agreed in both cell lines for no "
                           "construct; the cross-context test cannot be run "
                           "because K would not be the same object in the "
                           "two contexts")

    if not os.path.exists(CC.FEAT):
        CC.build_features(seeds)
    feats = CC.load_features()
    if set(feats.construct.unique()) != set(seeds):
        CC.build_features(seeds)
        feats = CC.load_features()
    scale = calibration.build_scale(feats)
    Cs = scale["K_scale_constant_C"]
    n_mrna = scale["mrna_molecules_per_cell"]
    tx = CC.transcript_level(feats)

    ab = {cell: ab_all[ab_all.cell_line == cell][["gene_symbol", "x_rel"]]
          for cell in CELLS}

    # ---- delivery control: on-target knockdown in each context ------------
    delivery = []
    for c in sorted(CC.TARGET_OF):
        tgt = CC.TARGET_OF[c]
        row = {"construct": c, "on_target_gene": tgt}
        for cell in CELLS:
            d = resp[(resp.construct == c) & (resp.cell_line == cell)
                     & (resp.gene_symbol == tgt)]
            row[f"on_target_log2fc_{cell}"] = (float(d.log2fc.median())
                                               if len(d) else None)
        a = row.get(f"on_target_log2fc_{CELLS[0]}")
        b = row.get(f"on_target_log2fc_{CELLS[1]}")
        row["on_target_log2fc_difference"] = (float(a - b) if
                                              a is not None and b is not None
                                              else None)
        delivery.append(row)

    # ---- per construct ----------------------------------------------------
    per_construct, boot_log_ratio_pooled = [], []
    for c in sorted(seeds):
        tgt = CC.TARGET_OF[c]
        d = tx[(tx.construct == c) & (tx.gene_symbol != tgt)].copy()
        d = d[np.isfinite(d.K_transcript) & (d.K_transcript > 0)]
        d["K"] = d.K_transcript * Cs
        d = d.drop(columns=[q for q in ("x_rel",) if q in d.columns])
        for cell in CELLS:
            d = d.merge(ab[cell].rename(
                columns={"x_rel": f"x_rel_{cell}"}), on="gene_symbol",
                how="inner")
            y = (resp[(resp.construct == c) & (resp.cell_line == cell)]
                 .groupby("gene_symbol", as_index=False)
                 .agg(**{f"y_{cell}": ("log2fc", "median")}))
            d = d.merge(y, on="gene_symbol", how="inner")
        d = d.drop_duplicates(subset=["gene_symbol"]).reset_index(drop=True)
        for cell in CELLS:
            d = d[np.isfinite(d[f"y_{cell}"]) & (d[f"x_rel_{cell}"] > 0)]
        if len(d) < MIN_TRANSCRIPTS:
            per_construct.append({"construct": c, "status": "SKIPPED",
                                  "reason": "fewer than "
                                            f"{MIN_TRANSCRIPTS} transcripts "
                                            "shared by both contexts"})
            continue
        K = d.K.to_numpy()
        Xc = {cell: d[f"x_rel_{cell}"].to_numpy() * n_mrna for cell in CELLS}
        Y = [d[f"y_{cell}"].to_numpy() for cell in CELLS]

        fit = DF.fit_pools(K, Y)
        p0, p1 = fit["pool_per_dose"]
        obs_ratio = p0 / p1

        # equilibrium prediction across rho, at a common M in both contexts
        pred = []
        for rho in RHO_GRID:
            M = rho * n_mrna
            f0 = float(DF.free_pool_from_M(M, K, Xc[CELLS[0]])[0])
            f1 = float(DF.free_pool_from_M(M, K, Xc[CELLS[1]])[0])
            pred.append({
                "rho": rho, "M_molecules_per_cell": M,
                "f_HUH7": f0, "f_PLC": f1,
                "predicted_pool_ratio_equilibrium": (f0 / f1 if f1 > 0
                                                     else float("nan")),
                "predicted_pool_ratio_independent": 1.0,
            })

        boot = {"ratio": [], "p0": [], "p1": []}
        n = len(d)
        for _ in range(N_BOOT):
            ix = rng.integers(0, n, n)
            try:
                fb = DF.fit_pools(K[ix], [y[ix] for y in Y],
                                  p_init=fit["pool_per_dose"],
                                  restarts=(0.0,))
            except Exception:
                continue
            q0, q1 = fb["pool_per_dose"]
            boot["ratio"].append(q0 / q1)
            boot["p0"].append(q0)
            boot["p1"].append(q1)
        ci = DF.percentile_ci(boot["ratio"])
        logs = [np.log10(q) for q in boot["ratio"] if q > 0]
        boot_log_ratio_pooled.append(logs)

        # the rho at which the equilibrium prediction meets the observation
        rr = [p["predicted_pool_ratio_equilibrium"] for p in pred]
        rho_match = None
        for i in range(len(rr) - 1):
            lo, hi = sorted((rr[i], rr[i + 1]))
            if lo <= obs_ratio <= hi and rr[i] != rr[i + 1]:
                w = (obs_ratio - rr[i]) / (rr[i + 1] - rr[i])
                rho_match = float(10 ** (np.log10(RHO_GRID[i]) + w * (
                    np.log10(RHO_GRID[i + 1]) - np.log10(RHO_GRID[i]))))
                break

        per_construct.append({
            "construct": c, "status": "OK",
            "recovered_site_7mer": seeds[c],
            "on_target_gene": tgt,
            "n_transcripts_shared_by_both_contexts": int(len(d)),
            "total_retrieved_abundance_HUH7": float(Xc[CELLS[0]].sum()),
            "total_retrieved_abundance_PLC": float(Xc[CELLS[1]].sum()),
            "retrieved_abundance_ratio_HUH7_over_PLC": float(
                Xc[CELLS[0]].sum() / Xc[CELLS[1]].sum()),
            "mean_log2fc_HUH7": float(np.mean(Y[0])),
            "mean_log2fc_PLC": float(np.mean(Y[1])),
            "fit": fit,
            "observed_pool_ratio_HUH7_over_PLC": float(obs_ratio),
            "observed_pool_ratio_ci95": ci,
            "observed_ratio_ci_excludes_1": bool(
                (ci[0] > 1.0) or (ci[1] < 1.0)),
            "bootstrap_n_successful": len(boot["ratio"]),
            "predicted_ratio_by_rho": pred,
            "rho_at_which_equilibrium_matches_observed_ratio": rho_match,
            "independent_prediction_pool_ratio": 1.0,
        })

    ok = [p for p in per_construct if p["status"] == "OK"]
    ratios = [p["observed_pool_ratio_HUH7_over_PLC"] for p in ok]
    pooled_boot = []
    if boot_log_ratio_pooled:
        m = min(len(v) for v in boot_log_ratio_pooled)
        for i in range(m):
            pooled_boot.append(10 ** np.mean([v[i] for v in
                                              boot_log_ratio_pooled]))
    pooled_ci = DF.percentile_ci(pooled_boot)

    return {
        "data_source": "GSE14073 (Burchard et al. 2009, PMC2648714)",
        "contexts": list(CELLS),
        "timepoints_hours_used": HOURS,
        "gencode_release": 50,
        "constants_used": scale,
        "n_bootstrap": N_BOOT,
        "rho_grid": RHO_GRID,

        "SEED_RECOVERY_NOTE": (
            "the guide sequences are not in the deposit and the article is "
            "not open access, both recorded as failures in "
            "data/PROVENANCE.json. The 7-mer site is recovered from the "
            "measured response separately in each cell line by the "
            "enrichment scan of riscpool.kmers, and a construct enters the "
            "analysis only when the two recoveries agree exactly, so that K "
            "is literally the same object in both contexts."),
        "AFFINITY_MODEL_LIMITATION": (
            "recovery identifies guide positions 2-8 and nothing else, so K "
            "here is built from the SEED duplex rather than from the full "
            "19-mer as in the HeLa pipeline. That costs resolution within "
            "the retrieved set. It does not threaten the cross-context "
            "comparison, which requires only that K be identical between "
            "contexts."),
        "DELIVERY_CONFOUND": (
            "the independent-scoring prediction of a pool ratio of exactly 1 "
            "holds only if the total loaded complex M is equal in the two "
            "cell lines. M is not measured. Different uptake, different "
            "Argonaute abundance or different loading would move the ratio "
            "away from 1 with no competition involved, so a ratio away from "
            "1 is not by itself evidence for the equilibrium layer. The "
            "on-target knockdown in each context is reported below as the "
            "only available delivery readout."),

        "seed_recovery": recovery,
        "n_constructs_attempted": len(CC.TARGET_OF),
        "n_constructs_with_agreeing_seed": len(seeds),
        "constructs_with_agreeing_seed": sorted(seeds),
        "constructs_excluded_for_seed_disagreement": sorted(
            c for c in CC.TARGET_OF if c not in seeds),
        "recovered_seeds": seeds,

        "delivery_control_on_target_knockdown": delivery,
        "per_construct": per_construct,
        "n_constructs_fitted": len(ok),
        "observed_pool_ratios": ratios,
        "pooled_geometric_mean_pool_ratio": float(
            10 ** np.mean(np.log10(ratios))) if ratios else float("nan"),
        "pooled_pool_ratio_ci95": pooled_ci,
        "pooled_ratio_ci_excludes_1": bool(
            pooled_ci[0] > 1.0 or pooled_ci[1] < 1.0)
        if np.isfinite(pooled_ci[0]) else None,
        "n_constructs_whose_ci_excludes_1": int(sum(
            p["observed_ratio_ci_excludes_1"] for p in ok)),
        "POWER_LIMITATION": (
            "three constructs survive the seed-agreement requirement out of "
            "seven attempted, two contexts each, and the bootstrap resamples "
            "transcripts rather than cell lines, so it propagates "
            "uncertainty in each fitted pool and says nothing about "
            "between-context variability beyond the one pair observed. Two "
            "of the three surviving constructs target the same gene."),
    }


if __name__ == "__main__":
    runner.run("e10_cross_context", fn, seed=0)
