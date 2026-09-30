"""
The two proposed figures for the positive-extension report.

Every plotted value is read from results/positive_extensions/ at draw time.
Nothing is typed into a caption.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import matplotlib                                          # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                            # noqa: E402
import numpy as np                                         # noqa: E402
import pandas as pd                                        # noqa: E402
from riscpool.provenance import ROOT                       # noqa: E402

OUT = os.path.join(ROOT, "results", "positive_extensions")
FIG = os.path.join(ROOT, "figures")
OK = {"blue": "#0072B2", "orange": "#E69F00", "green": "#009E73",
      "vermillion": "#D55E00", "grey": "#999999", "black": "#000000"}
plt.rcParams.update({"font.size": 8, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.dpi": 300,
                     "savefig.bbox": "tight"})
CAP = {}


def fig_a():
    v = json.load(open(os.path.join(ROOT, "results",
                                    "pxa_affinity_correction.json")))["values"]
    per = pd.read_csv(os.path.join(OUT, "A_per_family_external.csv"))
    per = per.sort_values("paired_difference")
    boot = np.load(os.path.join(OUT, "A_bootstrap_distribution.npy"))
    fig, ax = plt.subplots(1, 2, figsize=(7.0, 2.8),
                           gridspec_kw={"width_ratios": [1.3, 1]})
    # The two models differ by ~1e-4 against absolute correlations of ~3e-2,
    # so plotting both on one absolute axis shows two overlapping dots and
    # hides the quantity of interest. The left panel therefore shows the
    # PAIRED DIFFERENCE per family, which is what the primary metric is, and
    # the absolute level is stated in the caption.
    y = np.arange(len(per))
    col = [OK["blue"] if d > 0 else OK["vermillion"]
           for d in per.paired_difference]
    SC = 1e4          # plot in units of 1e-4, see the axis labels
    ax[0].hlines(y, 0, per.paired_difference * SC, color=OK["grey"], lw=0.9)
    ax[0].scatter(per.paired_difference * SC, y, s=22, color=col, zorder=3)
    ax[0].axvline(0, color=OK["black"], lw=0.9, ls="--")
    ax[0].set_yticks(y)
    ax[0].set_yticklabels([f"{f}  ({m:.3f})" for f, m in
                           zip(per.family, per.M1)], fontsize=6.5)
    ax[0].set_xlabel("paired difference in within-guide Spearman "
                     r"($\times 10^{-4}$)", fontsize=7)
    ax[0].set_ylabel("guide family (seed), baseline in ( )", fontsize=7)
    ax[0].set_title("(a) per external family", fontsize=8, loc="left")

    ax[1].hist(boot * SC, bins=60, color=OK["blue"], alpha=0.75, lw=0)
    eff = v["primary_paired_effect_M3_minus_M1"]
    ci = v["primary_effect_ci95_family_cluster_bootstrap"]
    ax[1].axvline(0, color=OK["black"], lw=1.0, ls="--", label="no change")
    ax[1].axvline(eff * SC, color=OK["vermillion"], lw=1.4, label="observed")
    ax[1].axvspan(ci[0] * SC, ci[1] * SC, color=OK["vermillion"], alpha=0.15,
                  lw=0)
    ax[1].set_xlabel("paired effect (offsets $-$ thermodynamic) "
                     r"($\times 10^{-4}$)", fontsize=7)
    ax[1].set_ylabel("bootstrap resamples")
    ax[1].tick_params(axis="x", labelsize=6)
    ax[1].legend(frameon=False, fontsize=6.5)
    ax[1].set_title("(b) family-cluster bootstrap", fontsize=8, loc="left")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG, f"px_A_external.{ext}"))
    plt.close(fig)
    CAP["px_A_external"] = (
        "Measured data (E-MEXP-668, external). (a) Paired difference in "
        "within-guide Spearman correlation between predicted affinity score "
        "and measured repression, corrected minus uncorrected, for each of "
        f"the {len(per)} external guide families; the uncorrected baseline "
        "for each family is in brackets on the axis. The three site-class "
        "offsets were fitted on GSE5814 alone and frozen. Differences are "
        "plotted rather than the two absolute curves because the two models "
        "differ by about 1e-4 against correlations of about 3e-2 and would "
        "otherwise be indistinguishable. "
        f"{int((per.paired_difference < 0).sum())} of {len(per)} families "
        "move the wrong way. (b) The paired family-cluster "
        f"bootstrap, {len(boot)} resamples, of the equal-family mean "
        f"difference. The observed effect is {eff:.2e} with interval "
        f"{ci[0]:.2e} to {ci[1]:.2e}. The correction does not improve external "
        "ranking; the interval excludes zero on the side of no benefit and "
        "the magnitude is negligible against a baseline correlation of "
        f"{v['external_D2']['M1_thermodynamic']['equal_family_mean_spearman']:.3f}.")


def fig_b():
    """Experiment B, drawn only from audited outputs.

    Residuals come from B_audit_residuals.csv, never from B_grid's
    dimensionless_residual column: the audit showed that column used a
    double-counted definition. Only focal_rel_err is taken from B_grid, and
    only for the development families, because that is a column the
    invariance check reproduced exactly and those families are what the
    selection actually used.
    """
    ex = json.load(open(os.path.join(OUT, "B_audit_export.json")))
    res = pd.read_csv(os.path.join(OUT, "B_audit_residuals.csv"))
    fd = pd.read_csv(os.path.join(OUT, "B_audit_finite_differences.csv"))
    grid = pd.read_csv(os.path.join(OUT, "B_grid.csv"))
    dev_fams = set(ex["family_split"]["development"])
    cfg, acc, tim = (ex["frozen_configuration"], ex["accuracy_heldout"],
                     ex["timing"])
    fdc = ex["finite_difference_check"]

    fig, ax = plt.subplots(1, 4, figsize=(9.6, 2.5))
    style = {"truncate": (OK["vermillion"], "o", "top-$R$, omitted dropped"),
             "linear": (OK["orange"], "s", "top-$R$ + linear background"),
             "bins": (OK["blue"], "^", "top-$R$ + saturable bins")}

    dev = grid[(~grid.exact_no_truncation) & (grid.family.isin(dev_fams))]
    for m, (c, mk, lab) in style.items():
        g = dev[dev.method == m]
        if not len(g):
            continue
        agg = g.groupby(["R", "B"]).agg(
            occ=("focal_rel_err", lambda v: np.nanpercentile(v, 90))
        ).reset_index()
        ax[0].scatter(agg.R, np.maximum(agg.occ, 1e-17), s=14, color=c,
                      marker=mk, label=lab, alpha=0.8)
    ax[0].scatter([cfg["R"]], [max(cfg["worst_dev_focal_rel_err"], 1e-17)],
                  s=70, facecolors="none", edgecolors=OK["black"], lw=1.0,
                  zorder=5)
    ax[0].set_yscale("log")
    ax[0].set_xlabel("retrieval depth $R$")
    ax[0].set_ylabel("focal occupancy rel. error (p90)")
    ax[0].axhline(1e-2, color=OK["black"], lw=0.8, ls=":")
    ax[0].legend(frameon=False, fontsize=5.0, loc="lower left")
    ax[0].set_title("(a) development surface", fontsize=8, loc="left")

    te = res[res.split == "test"]
    parts = [te.compressed_residual_over_M.clip(lower=1e-18),
             te.full_system_defect_over_M.clip(lower=1e-18)]
    ax[1].boxplot(parts, widths=0.55, showfliers=True,
                  flierprops={"marker": ".", "markersize": 2},
                  medianprops={"color": OK["black"]})
    ax[1].set_yscale("log")
    ax[1].set_xticklabels(["solves its\nown system",
                           "satisfies the\nfull system"], fontsize=6.5)
    ax[1].set_ylabel(r"residual $/\max(M,1)$")
    ax[1].set_title("(b) two residual definitions", fontsize=8, loc="left")

    meths = ["full", "truncate", "linear", "bins"]
    prep = [tim["per_method"][m]["preparation_total"]["median_ms"]
            for m in meths]
    solv = [tim["per_method"][m]["solve_cached"]["median_ms"] for m in meths]
    xs = np.arange(len(meths))
    ax[2].bar(xs, prep, 0.62, color=OK["grey"], label="preparation")
    ax[2].bar(xs, solv, 0.62, bottom=prep, color=OK["blue"],
              label="cached solve")
    ax[2].axhline(tim["per_method"]["full"]["end_to_end_forward"]["median_ms"],
                  color=OK["vermillion"], lw=1.0, ls="--",
                  label="full reference, end to end")
    ax[2].set_xticks(xs)
    ax[2].set_xticklabels(meths, fontsize=6.5)
    ax[2].set_ylabel("time (ms)")
    ax[2].legend(frameon=False, fontsize=5.0, loc="upper left")
    ax[2].set_title("(c) forward cost", fontsize=8, loc="left")

    ok = fd[fd.status == "ok"]
    lo = min(ok.analytic.abs().min(), ok.central_difference.abs().min()) * 0.5
    hi = max(ok.analytic.abs().max(), ok.central_difference.abs().max()) * 2
    ax[3].plot([lo, hi], [lo, hi], color=OK["black"], lw=0.7, ls=":")
    ax[3].scatter(ok.analytic.abs(), ok.central_difference.abs(), s=16,
                  color=OK["green"], alpha=0.85)
    ax[3].set_xscale("log")
    ax[3].set_yscale("log")
    ax[3].set_xlabel("|analytic gradient|")
    ax[3].set_ylabel("|central difference|")
    ax[3].set_title("(d) gradient check", fontsize=8, loc="left")

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG, f"px_B_approx.{ext}"))
    plt.close(fig)

    be = tim["break_even_solves_including_preparation"]
    CAP["px_B_approx"] = (
        "Model calculation on measured inputs. Audit of the compressed "
        "equilibrium solve, drawn only from audited outputs. (a) Development "
        "selection surface: 90th-percentile focal occupancy error against the "
        "full retrieved reference over the "
        f"{len(dev_fams)} development families, for every configuration on "
        "the frozen grid; the circled point is the selected configuration "
        f"({cfg['method']}, $R={cfg['R']}$, $B={cfg['B']}$), chosen before "
        "any held-out family was scored and not reselected afterwards. "
        f"(b) On the {acc['n_cases']} held-out cases from "
        f"{acc['n_families']} independent families, the two residual "
        "definitions, each divided by $\\max(M,1)$, are separated by "
        f"{acc['separation_orders_of_magnitude_median']:.1f} orders of "
        "magnitude at the median: the compressed system is solved to "
        f"{acc['compressed_residual_over_M_worst']:.1e} at worst, but the "
        "resulting solution misses the original conservation law by a median "
        f"of {acc['full_system_defect_over_M_median']:.1e} and by up to "
        f"{acc['full_system_defect_over_M_worst']:.1e}. The second quantity "
        "is the approximation error; the first only says the bisection "
        "converged. (c) Median forward cost in milliseconds at matched "
        f"outputs on one construct with {tim['N_reference']} competitors, "
        "single-threaded float64; bin construction is part of preparation, "
        "not an addition to it. Compression does not pay for itself at this "
        "workload: the selected configuration's cached solve is "
        f"{abs(tim['cached_solve_saving_per_solve_ms']):.2f} ms "
        + ("slower" if be is None else "faster") +
        " than the full solve, so preparation never pays back; truncation is "
        "cheaper from the first solve but fails the gradient target. "
        "(d) Analytic gradients against central differences over "
        f"{int((fd.status == 'ok').sum())} coordinates, including omitted "
        "ones; worst relative error "
        f"{fdc['worst_rel_err']:.3g} overall and "
        f"{fdc['worst_rel_err_above_1e9_of_max']:.3g} over the "
        f"{fdc['n_coordinates_above_1e9_of_max']} coordinates whose gradient "
        "exceeds 1e-9. The dotted line is equality.")


def fig_b_main():
    """Main-text figure: what the compression buys and what it costs.

    Drawn only from audited outputs. Three panels, sized for the paper's
    text width: acceptance against both targets, what "accurate" means, and
    the measured cost.
    """
    ex = json.load(open(os.path.join(OUT, "B_audit_export.json")))
    res = pd.read_csv(os.path.join(OUT, "B_audit_residuals.csv"))
    grid = pd.read_csv(os.path.join(OUT, "B_grid.csv"))
    cfg, acc, tim = (ex["frozen_configuration"], ex["accuracy_heldout"],
                     ex["timing"])
    test = set(ex["family_split"]["test"])
    FULLW = 5.5

    fig, ax = plt.subplots(1, 3, figsize=(FULLW, 1.72),
                           gridspec_kw={"width_ratios": [1.25, 0.8, 1.0],
                                        "wspace": 0.62})
    style = {"truncate": (OK["vermillion"], "o", "drop omitted"),
             "linear": (OK["orange"], "s", "linear background"),
             "bins": (OK["blue"], "^", "saturable bins")}

    # (a) both targets, per held-out case
    g = grid[grid.family.isin(test) & (grid.R == cfg["R"])
             & (~grid.exact_no_truncation)]
    for m, (c, mk, lab) in style.items():
        bb = cfg["B"] if m == "bins" else 0
        gg = g[(g.method == m) & (g.B == bb)]
        if not len(gg):
            continue
        ax[0].scatter(gg.focal_rel_err.clip(lower=1e-16),
                      gg.grad_rel_l2_err.clip(lower=1e-16), s=7, color=c,
                      marker=mk, alpha=0.65, lw=0, label=lab)
    ax[0].axhline(1e-2, color=OK["black"], lw=0.7, ls=":")
    ax[0].axvline(1e-2, color=OK["black"], lw=0.7, ls=":")
    ax[0].set_xscale("log")
    ax[0].set_yscale("log")
    ax[0].set_xlabel("focal occupancy rel. err", fontsize=6.5)
    ax[0].set_ylabel("gradient rel. $L_2$ err", fontsize=6.5)
    ax[0].tick_params(labelsize=6)
    # clear a band above the data so the legend cannot sit on any point
    ylo, yhi = ax[0].get_ylim()
    ax[0].set_ylim(ylo, yhi * 3e3)
    ax[0].legend(frameon=False, fontsize=5.2, loc="upper left",
                 handletextpad=0.1, borderaxespad=0.15, labelspacing=0.25)
    ax[0].set_title("(a) both 1% targets", fontsize=7.5, loc="left")

    # (b) the two residual definitions
    te = res[res.split == "test"]
    ax[1].boxplot([te.compressed_residual_over_M.clip(lower=1e-18),
                   te.full_system_defect_over_M.clip(lower=1e-18)],
                  widths=0.5, showfliers=False,
                  medianprops={"color": OK["black"]})
    ax[1].set_yscale("log")
    ax[1].set_xticklabels(["own\nsystem", "full\nsystem"], fontsize=5.5)
    ax[1].set_ylabel(r"residual / $\max(M,1)$", fontsize=6.5)
    ax[1].tick_params(axis="y", labelsize=6)
    ax[1].set_title("(b) what error means", fontsize=7.5, loc="left")

    # (c) measured forward cost
    meths = ["full", "truncate", "linear", "bins"]
    prep = [tim["per_method"][m]["preparation_total"]["median_ms"]
            for m in meths]
    solv = [tim["per_method"][m]["solve_cached"]["median_ms"] for m in meths]
    xs = np.arange(len(meths))
    ax[2].bar(xs, prep, 0.6, color=OK["grey"], label="preparation")
    ax[2].bar(xs, solv, 0.6, bottom=prep, color=OK["blue"],
              label="cached solve")
    ax[2].axhline(tim["per_method"]["full"]["end_to_end_forward"]["median_ms"],
                  color=OK["vermillion"], lw=0.9, ls="--",
                  label="full reference")
    ax[2].set_xticks(xs)
    ax[2].set_xticklabels(["full", "trunc.", "linear", "bins"], fontsize=5.5)
    ax[2].set_ylabel("forward time (ms)", fontsize=6.5)
    ax[2].tick_params(axis="y", labelsize=6)
    ax[2].legend(frameon=False, fontsize=5.2, loc="upper left",
                 handletextpad=0.3, borderaxespad=0.15, labelspacing=0.25)
    ax[2].set_title("(c) measured cost", fontsize=7.5, loc="left")

    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG, f"fig_approx.{ext}"),
                    bbox_inches="tight")
    plt.close(fig)

    cm = ex["accuracy_heldout_comparators"]["per_method"]
    CAP["fig_approx"] = (
        "Model calculation on measured inputs. Compressing the competitor "
        f"set, on {acc['n_cases']} held-out cases from {acc['n_families']} "
        f"guide families disjoint from the {len(ex['family_split']['development'])} "
        "used to choose the configuration. (a) Relative error against the "
        f"full retrieved reference at depth $R={cfg['R']}$, one point per "
        "case; dotted lines are the 1% engineering targets, so only the "
        "lower-left quadrant passes both. (b) Two error measures for the "
        f"same solutions, each divided by $\\max(M,1)$; boxes are median and "
        "quartiles. (c) Median forward time in milliseconds over "
        f"{tim['repetitions']} repetitions on one construct with "
        f"{tim['N_reference']} competitors, single-threaded float64; bin "
        "construction is part of preparation.")


if __name__ == "__main__":
    fig_a()
    fig_b()
    fig_b_main()
    with open(os.path.join(OUT, "px_CAPTIONS.json"), "w") as fh:
        json.dump(CAP, fh, indent=1)
    print("wrote figures/px_A_external.{pdf,png}, figures/px_B_approx.{pdf,png}")
