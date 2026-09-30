"""
e5 - where HeLa actually sits.

rho = M / sum_j x_j with M = alpha * (Argonaute copies per cell). Because the
abundance vector is normalised to the total mRNA count, rho collapses to

    rho = alpha * Ago2_copies / mRNA_copies

so only alpha, the loaded fraction, is unmeasured, and it is swept.

The background term beta is not measured either. Transcripts with no seed
match still bind Argonaute nonspecifically, and no number in this repository
says how well. It is therefore BRACKETED rather than chosen: beta = 0 (no
background binding at all, which understates competition) up to the value
obtained if every non-retrieved transcript bound as well as the weakest
retrieved seed site (which overstates it). Both ends are reported.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
import torch                                                    # noqa: E402
from scipy.stats import kendalltau                              # noqa: E402
from riscpool import calibration, real_experiments as R, runner  # noqa: E402
from riscpool.equilibrium import (pairwise_occupancy,            # noqa: E402
                                 risc_equilibrium)
from riscpool.features import RT, load_features  # noqa: E402
from riscpool.hela import load_abundance                         # noqa: E402
from riscpool.sirna import per_construct                         # noqa: E402

ALPHAS = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0]
RHOS = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0]
HKS = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6, 3.2]


def tau_row(K_off, x_off, K_on, x_on, rho, total_x, beta):
    C, N = K_off.shape
    K = torch.tensor(np.concatenate([K_on.reshape(C, 1), K_off], 1),
                     dtype=torch.float64)
    x = torch.tensor(np.concatenate([[x_on], x_off]),
                     dtype=torch.float64).expand(C, -1).contiguous()
    M = torch.full((C, 1), float(rho * total_x), dtype=torch.float64)
    b = torch.full((C, 1), float(beta), dtype=torch.float64)
    f, o = risc_equilibrium(K, x, M, b)
    p = pairwise_occupancy(K, x, M)
    eq = o[:, 1:].sum(-1).numpy()
    pw = p[:, 1:].sum(-1).numpy()
    return (float(kendalltau(eq, pw).statistic), eq, pw,
            f[:, 0].numpy(), o[:, 0].numpy())


def fn(seed=0):
    feats = load_features()
    scale = calibration.build_scale(feats)
    C = scale["K_scale_constant_C"]
    n_mrna = scale["mrna_molecules_per_cell"]

    ab = load_abundance()[["transcript_id", "x_rel"]]
    pc = per_construct()
    constructs = sorted(c for c in pc.construct if c.startswith("MAPK14-193"))

    asm = R.assemble(constructs, target_gene="MAPK14")
    K_off = asm["K_off"] * C                       # molecules per cell
    x_off = asm["x_off"] * n_mrna                  # molecules per cell
    total_x = float(n_mrna)                        # whole-cell mRNA count

    # on-target affinity, anchored on the published full-complementarity Kd
    ont, site = R.on_target_affinity(pc[pc.construct.isin(constructs)])
    cst = calibration.load_constants()
    kd_full = calibration.kd_molar_to_molecules_per_cell(
        cst["kd_full_complementarity_molar"]["central"],
        cst["hela_cell_volume_litres"]["central"])
    parent_dg = float(ont.loc[ont.construct == "MAPK14-193_parent",
                              "dg_on_target_kcal"].iloc[0])
    ont = ont.set_index("construct").loc[constructs].reset_index()
    K_on = kd_full * np.exp((ont.dg_on_target_kcal.to_numpy() - parent_dg) / RT)
    log10K_on = np.log10(K_on)
    H_K_measured = float(np.std(log10K_on, ddof=1))

    ab_full = load_abundance()[["transcript_id", "gene_symbol", "x_rel"]]
    x_on = float(ab_full.query("gene_symbol=='MAPK14'").x_rel.iloc[0] * n_mrna)

    # background bracket. Not measured, so bracketed at both ends: no
    # background binding at all, and every non-retrieved transcript binding
    # with the published seed-MISmatched dissociation constant.
    retrieved = set(asm["transcripts"])
    x_rest = float(n_mrna
                   * ab_full[~ab_full.transcript_id.isin(retrieved)].x_rel.sum())
    K_nonspecific = calibration.kd_molar_to_molecules_per_cell(
        cst["kd_seed_mismatched_molar"]["central"],
        cst["hela_cell_volume_litres"]["central"])
    beta_hi = x_rest / K_nonspecific
    betas = [0.0, beta_hi]

    # rho estimate for HeLa
    rho_rows = []
    for a in ALPHAS:
        lo, hi = calibration.rho_from_alpha(a, scale)
        rho_rows.append({"alpha_loaded_fraction": a, "rho_low": lo,
                         "rho_high": hi})
    rho_lo_all = min(r["rho_low"] for r in rho_rows)
    rho_hi_all = max(r["rho_high"] for r in rho_rows)

    # phase grid at beta = 0
    grid = {}
    mu, dev = log10K_on.mean(), log10K_on - log10K_on.mean()
    sd0 = dev.std(ddof=1)
    contours = []
    for h in HKS:
        s = h / sd0 if sd0 > 0 else 0.0
        Kon_h = 10.0 ** (mu + dev * s)
        row = []
        for r in RHOS:
            t, *_ = tau_row(K_off, x_off, Kon_h, x_on, r, total_x, 0.0)
            row.append(t)
        grid[f"H_K={h}"] = row
        contours.append({"H_K": h,
                         "rho_at_tau_0.9": R.contour_rho_at_tau(RHOS, row,
                                                                0.9),
                         "min_tau": float(np.min(row)),
                         "max_tau": float(np.max(row))})

    # the measured H_K row, and the background bracket at the HeLa rho band
    row_meas = [tau_row(K_off, x_off, K_on, x_on, r, total_x, 0.0)[0]
                for r in RHOS]
    band = []
    for lab, r in (("rho_low_end", rho_lo_all), ("rho_high_end", rho_hi_all)):
        for bi, b in enumerate(betas):
            t, eq, pw, f, o_on = tau_row(K_off, x_off, K_on, x_on, r,
                                         total_x, b)
            band.append({
                "which": lab, "rho": r,
                "beta": b,
                "beta_case": "zero_background" if bi == 0 else
                             "max_background_bracket",
                "kendall_tau_eq_vs_independent": t,
                "mean_free_pool_f": float(np.mean(f)),
                "mean_f_over_M": float(np.mean(f) / (r * total_x)),
                "mean_offtarget_load_equilibrium": float(np.mean(eq)),
                "mean_offtarget_load_independent": float(np.mean(pw)),
                "load_ratio_eq_over_independent": float(np.mean(eq)
                                                        / np.mean(pw)),
            })

    tau_at_band = [b["kendall_tau_eq_vs_independent"] for b in band]
    return {
        "normalisation_LIMITATION": (
            "Microarray intensities are relative, not absolute. They are put "
            "on a molecules-per-cell scale by assuming the measured relative "
            "abundances partition a published total mRNA count per cell. "
            "Array intensity is not linear in transcript number across the "
            "full dynamic range, probe affinities differ, and only "
            f"{len(ab)} gene symbols were measured, so the resulting "
            "molecule counts are an order-of-magnitude scale, not a "
            "calibration. rho depends on this only through the total, which "
            "is the best-constrained part of it."),
        "constants_used": scale,
        "kd_full_complementarity_molecules_per_cell": kd_full,
        "n_candidate_constructs": len(constructs),
        "candidate_constructs": constructs,
        "n_retrieved_offtarget_transcripts_union": int(K_off.shape[1]),
        "total_mrna_molecules_per_cell": total_x,
        "x_on_target_MAPK14_molecules_per_cell": x_on,
        "H_K_measured_sd_log10_K_on": H_K_measured,
        "dg_on_target_kcal_parent": parent_dg,
        "dg_on_target_kcal_range": [float(ont.dg_on_target_kcal.min()),
                                    float(ont.dg_on_target_kcal.max())],
        "on_target_site_sequence_dna": site.replace("U", "T"),
        "alpha_swept": ALPHAS,
        "rho_estimates_by_alpha": rho_rows,
        "rho_hela_band_low": rho_lo_all,
        "rho_hela_band_high": rho_hi_all,
        "rho_grid": RHOS,
        "H_K_grid": HKS,
        "tau_grid_beta_zero": grid,
        "tau_row_at_measured_H_K": row_meas,
        "tau_0.9_contour_by_H_K": contours,
        "background_beta_bracket": {
            "low": 0.0, "high": beta_hi,
            "x_not_retrieved_molecules_per_cell": x_rest,
            "K_nonspecific_molecules_per_cell": K_nonspecific,
            "K_nonspecific_source": "Wee et al. Cell 2012, g4g5 seed-mismatched "
                                    "target, 2.3 nM; fly Ago2, species caveat "
                                    "recorded in data/constants.json"},
        "hela_band_detail": band,
        "min_tau_anywhere_in_hela_band": float(np.min(tau_at_band)),
        "max_tau_anywhere_in_hela_band": float(np.max(tau_at_band)),
        "answer_does_hela_fall_in_the_regime_where_equilibrium_reorders":
            bool(np.min(tau_at_band) < 0.9),
        "criterion": "tau < 0.9 between equilibrium and independent candidate "
                     "ranking is the threshold used throughout; tau = 1 means "
                     "the layer changes no decision",
    }


if __name__ == "__main__":
    runner.run("e5_hela_regime", fn, seed=0)
