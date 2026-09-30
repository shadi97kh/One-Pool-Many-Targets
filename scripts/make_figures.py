"""
Figures. Every plotted value is read from results/*.json at render time.
Nothing is recomputed here and no number is typed into a caption.

If a panel's source result is missing or FAILED the panel is SKIPPED and the
omission is printed and recorded in the caption, rather than drawn from
something else. That is the whole point of the rule: a figure is a claim, and
a claim needs a file behind it.

Palette is Okabe-Ito, which is colourblind safe. Vector PDF plus 300 dpi PNG.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import matplotlib                                               # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                 # noqa: E402
import numpy as np                                              # noqa: E402
from riscpool import provenance as P                           # noqa: E402
from riscpool.provenance import FIGURES                         # noqa: E402
from riscpool.runner import load_result                         # noqa: E402

OK = {"blue": "#0072B2", "orange": "#E69F00", "green": "#009E73",
      "vermillion": "#D55E00", "purple": "#CC79A7", "sky": "#56B4E9",
      "yellow": "#F0E442", "black": "#000000", "grey": "#999999",
      "lightgrey": "#D9D9D9"}

plt.rcParams.update({
    "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8,
    "legend.fontsize": 7, "xtick.labelsize": 7, "ytick.labelsize": 7,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 300, "savefig.bbox": "tight", "pdf.fonttype": 42,
    "legend.handlelength": 1.6, "legend.borderpad": 0.3,
    "legend.labelspacing": 0.25,
})

# NeurIPS text width is 5.5in. Authoring wider than that and then including
# the figure at \textwidth scales everything DOWN on the page, which shrinks
# the fonts below their nominal size. Author at the final width instead.
FULL, HALF = 5.5, 3.4
CAPTIONS = {}
SKIPPED = []


def val(name):
    """Values of an OK result, or None. A FAILED result is not a source."""
    r = load_result(name)
    if r is None or r.get("status") != "OK":
        return None
    return r["values"]


def need(panel, **sources):
    """Return the sources, or None and record the skip."""
    missing = [k for k, v in sources.items() if v is None]
    if missing:
        SKIPPED.append({"panel": panel, "missing_results": missing})
        print(f"  SKIP {panel}: missing or FAILED {missing}")
        return False
    return True


def panel_label(ax, letter, dx=-0.20, dy=1.16):
    """Bold letter above the axes, clear of long y-axis labels."""
    ax.text(dx, dy, f"({letter})", transform=ax.transAxes,
            fontsize=9, fontweight="bold", va="top", ha="left")


def save(fig, name, caption):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGURES, f"{name}.{ext}"),
                    dpi=300 if ext == "png" else None)
    plt.close(fig)
    CAPTIONS[name] = caption
    print(f"wrote figures/{name}.pdf and .png")


def fmt(x, n=3):
    """Format a number for a caption. Reads from JSON, never typed."""
    x = float(x)
    a = abs(x)
    if a != 0 and (a < 1e-3 or a >= 1e4):
        return f"{x:.{n}e}"
    return f"{x:.{n}g}"


# ------------------------------------------------------------------ fig 1 --

def fig1():
    """Mechanism and theory: budget violation, redistribution, high-rho limit."""
    b = val("e5b_budget_curve")
    r = val("e2b_redistribution_curve")
    p = val("e3_pairwise_limit")
    e5 = val("e5_hela_regime")
    if not need("fig1", e5b_budget_curve=b, e2b_redistribution_curve=r,
                e3_pairwise_limit=p, e5_hela_regime=e5):
        return
    # three panels across one text width left every panel too narrow; (a) is
    # the busiest so it gets the full width and the other two share a row
    # the budget panel carries the claim the body needs and is the one that
    # needs the width; the two theory panels are confirmations of proved
    # statements and go to the appendix as figA3
    fig = plt.figure(figsize=(FULL, 2.45))
    gs = fig.add_gridspec(1, 1)
    axes = [fig.add_subplot(gs[0, 0]), None, None]
    figB = plt.figure(figsize=(FULL, 2.5))
    gsB = figB.add_gridspec(1, 2, wspace=0.85)
    axes[1] = figB.add_subplot(gsB[0, 0])
    axes[2] = figB.add_subplot(gsB[0, 1])

    # ---- (a) budget ----
    # Everything in this panel used to land in one narrow horizontal strip
    # around sum_x: two dotted reference lines, both curves, the markers and
    # three text labels. The declutter is: markers go to the top axis rail,
    # curves are labelled where they are actually separated (low M), and the
    # only in-strip element left is the sum_x line itself.
    ax = axes[0]
    M = np.array([q["M"] for q in b["curve"]])
    ind = np.array([q["independent_total_occupancy"] for q in b["curve"]])
    eq = np.array([q["equilibrium_total_occupancy"] for q in b["curve"]])
    ratio = np.array([q["independent_over_M"] for q in b["curve"]])
    sx = b["sum_x_retrieved_molecules_per_cell"]
    nm = b["total_mrna_molecules_per_cell"]
    lo = e5["rho_hela_band_low"] * nm
    hi = e5["rho_hela_band_high"] * nm

    ax.axvspan(lo, hi, color=OK["grey"], alpha=0.16, lw=0, zorder=0)
    ax.plot(M, M, color=OK["lightgrey"], lw=3.4, solid_capstyle="round",
            zorder=1)
    ax.plot(M, ind, color=OK["vermillion"], lw=1.6, zorder=3)
    ax.plot(M, eq, color=OK["blue"], lw=1.1, zorder=4)
    ax.axhline(sx, color=OK["black"], lw=0.7, ls=":", zorder=2)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(M[0], M[-1])
    ax.set_ylim(min(eq.min(), M[0]) * 0.4, max(ind.max(), M[-1]) * 3)
    ax.set_xlabel(r"RISC pool $M$ (molecules/cell)")
    ax.set_ylabel("bound transcript (mol/cell)")

    # labels where the curves are far apart, not where they converge
    ax.annotate("independent", xy=(M[3], ind[3]), textcoords="offset points",
                xytext=(3, 6), fontsize=6.5, color=OK["vermillion"],
                ha="left", va="bottom")
    ax.annotate(r"equilibrium $\approx M$", xy=(M[11], M[11]),
                textcoords="offset points", xytext=(7, -3), fontsize=6.5,
                color=OK["blue"], ha="left", va="top")
    # spell out that this is the retrieved sum, not the whole-cell mRNA
    # total that the competition parameter is divided by
    ax.annotate(r"$\sum_j x_j$ (retrieved)", xy=(M[-1], sx),
                textcoords="offset points",
                xytext=(-2, 3), fontsize=6.5, ha="right", va="bottom")

    # measured Argonaute copy numbers on the top rail, clear of the data
    for a in (b["ago2_measured_low_copies_per_cell"],
              b["ago2_measured_high_copies_per_cell"]):
        ax.axvline(a, color=OK["green"], lw=0.8, ls=(0, (2, 2)), zorder=2,
                   alpha=0.9)
        ax.plot([a], [1.0], marker="v", ms=4, color=OK["green"],
                transform=ax.get_xaxis_transform(), clip_on=False, zorder=7)
    ax.annotate("total Ago, published", xy=(np.sqrt(
        b["ago2_measured_low_copies_per_cell"]
        * b["ago2_measured_high_copies_per_cell"]), 1.04),
        xycoords=ax.get_xaxis_transform(), fontsize=6, color=OK["green"],
        ha="center", va="bottom")
    ax.annotate(r"$\alpha$-swept band", xy=(lo, 0.015),
                xycoords=ax.get_xaxis_transform(), fontsize=6,
                color="#6f6f6f", ha="left", va="bottom")

    ax2 = ax.twinx()
    ax2.spines["right"].set_visible(True)
    ax2.plot(M, ratio, color=OK["purple"], lw=1.2, ls=(0, (4, 2)), zorder=5)
    ax2.axhline(1.0, color=OK["purple"], lw=0.6, ls=":", alpha=0.55)
    ax2.set_yscale("log")
    ax2.set_ylabel("independent / $M$", color=OK["purple"], fontsize=7)
    ax2.tick_params(axis="y", colors=OK["purple"], labelsize=6)

    # ---- (b) redistribution ----
    # the series whose redistribution is largest, so the effect is legible;
    # one transcript out of many moves the sum by only a few per cent, which
    # the caption states in absolute terms
    ax = axes[1]
    s = max(r["series"], key=lambda q: q["o_others_fold_change_over_sweep"])
    kk = np.array([q["K_target"] for q in s["points"]])
    ot = np.array([q["o_target"] for q in s["points"]])
    oo = np.array([q["o_others_sum"] for q in s["points"]])
    ax.plot(kk, ot, color=OK["vermillion"], lw=1.5)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$K_t$ of one transcript (molecules/cell)")
    ax.set_ylabel(r"$o_t$ (mol/cell)", color=OK["vermillion"])
    ax.tick_params(axis="y", colors=OK["vermillion"])
    axb = ax.twinx()
    axb.spines["right"].set_visible(True)
    axb.plot(kk, 100.0 * (oo / oo[0] - 1.0), color=OK["blue"], lw=1.5)
    axb.set_ylabel(r"$\sum_{i\neq t} o_i$: change (%)", color=OK["blue"],
                   fontsize=7.5)
    axb.tick_params(axis="y", colors=OK["blue"], labelsize=6.5)

    # ---- (c) high-resource limit ----
    ax = axes[2]
    sw = p["sweep"]
    rho = np.array([q["rho"] for q in sw])
    med = np.array([q["median_rel_occupancy_error"] for q in sw])
    mx = np.array([q["max_rel_occupancy_error"] for q in sw])
    # a ratio that has reached float64 resolution is stored as exactly zero;
    # plotting it on a log axis draws a spike to the axis floor that looks
    # like a result. Mask those points and mark where resolution ran out.
    med_m = np.where(med > 0, med, np.nan)
    mx_m = np.where(mx > 0, mx, np.nan)
    # the note goes in the legend rather than next to the last point, where
    # it would sit on the series it is describing
    lost = int(np.sum(~(med > 0)))
    med_lab = ("median transcript" if not lost else
               "median transcript\n(ends at float64 resolution)")
    ax.plot(rho, med_m, "o-", color=OK["blue"], ms=3, lw=1.3, label=med_lab)
    ax.plot(rho, mx_m, "s-", color=OK["orange"], ms=3, lw=1.0,
            label="worst transcript")
    ref = med[len(med) // 2] * (rho / rho[len(rho) // 2]) ** (-2.0)
    ax.plot(rho, ref, color=OK["black"], lw=0.8, ls="--",
            label=r"slope $-2$")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$M / \sum_j x_j$ (modelled set)")
    ax.set_ylabel(r"$|o^{\mathrm{eq}}/o^{\mathrm{pw}} - 1|$")
    ax.legend(frameon=False, loc="lower left", fontsize=6)

    panel_label(axes[1], "a", dx=-0.30)
    panel_label(axes[2], "b", dx=-0.30)
    save(figB, "figA3_theory",
         "Model calculation on measured inputs (abundances from the GEO GSE5814 mock channel, structure "
         "from GENCODE v50 3'UTRs; siRNA "
         f"MAPK14-193 parent). (a) Redistribution at rho = {fmt(s['rho'])}: "
         "raising one transcript's affinity constant lowers its own occupancy "
         f"{fmt(s['o_target_fold_change_over_sweep'])}-fold and raises the "
         "rest of the transcriptome's by "
         f"{fmt(s['o_others_fold_change_over_sweep'])}-fold, monotonically, "
         "as the proposition requires. The swept transcript is "
         f"{r['target_gene_symbol']}, chosen by the stated rule "
         f"({r['target_selection_rule']}). (b) The relative gap between the "
         "two scorings decays as the pool grows, with a fitted log-log "
         f"exponent of {fmt(p['loglog_slope_MEDIAN_transcript'])} +/- "
         f"{fmt(p['loglog_slope_stderr_MEDIAN_transcript'])} for the median "
         f"transcript against a predicted {fmt(p['predicted_slope'])}: "
         "equilibrium contains independent scoring as its high-resource "
         "limit.")
    save(fig, "fig1_mechanism",
         "Model calculation on measured inputs (abundances from the GEO GSE5814 mock channel, structure "
         "from GENCODE v50 3'UTRs; siRNA "
         f"MAPK14-193 parent, {b['n_retrieved_transcripts']} retrieved "
         "transcripts). Total bound transcript against the loaded RISC pool. "
         "The independent pairwise counterfactual scores every transcript as "
         "though it saw the whole pool; the ratio of what it allocates to the "
         "budget is the dashed purple curve on the right axis. That ratio "
         "exceeds one only below M = "
         f"{fmt(b['crossover_M_where_independent_equals_budget'])} complexes "
         "per cell. At the published Argonaute copy numbers, which count total "
         "Ago rather than AGO2 alone, with the loaded "
         "fraction alpha set to 1 it is "
         f"{fmt(b['independent_over_M_at_ago2_measured_low'])} against the "
         "HeLa-specific count and "
         f"{fmt(b['independent_over_M_at_ago2_measured_high'])} against the "
         "higher non-HeLa one, so there is no over-allocation there at all; "
         "the violation is conditional on alpha falling below "
         f"{fmt(b['alpha_threshold_for_over_allocation_vs_ago2_low'])}. "
         "Equilibrium is constrained to the budget by construction and "
         "plateaus at the retrieved abundance "
         f"{fmt(b['sum_x_retrieved_molecules_per_cell'])} molecules/cell. "
         "Green triangles are published total-Argonaute copy numbers; the grey band "
         "is the swept loaded fraction, which is not measured. This is a "
         "counterfactual about what these affinities imply under independent "
         "scoring, not a claim about any published predictor's output.")


# ------------------------------------------------------------------ fig 2 --

def fig2():
    """Where real cells sit: tau against rho, with the H_K spread as a band.

    The 2-D grid this replaces is essentially one-dimensional: the contours
    run near-vertical because H_K carries almost no variation. Drawing it as a
    band makes that flatness visible instead of asserting it.
    """
    e5 = val("e5_hela_regime")
    if not need("fig2", e5_hela_regime=e5):
        return
    e9 = val("e9_dose_response")

    rho = np.array(e5["rho_grid"], dtype=float)
    G = np.array([e5["tau_grid_beta_zero"][f"H_K={h}"]
                  for h in e5["H_K_grid"]], dtype=float)
    meas = np.array(e5["tau_row_at_measured_H_K"], dtype=float)

    fig, ax = plt.subplots(figsize=(HALF, 2.6))
    ax.fill_between(rho, G.min(axis=0), G.max(axis=0), color=OK["sky"],
                    alpha=0.30, lw=0,
                    label=r"range over $H_K$")
    ax.plot(rho, meas, color=OK["blue"], lw=1.6,
            label=r"measured $H_K$")
    ax.axhline(0.9, color=OK["vermillion"], lw=1.0, ls="--",
               label=r"$\tau = 0.9$")

    lo, hi = e5["rho_hela_band_low"], e5["rho_hela_band_high"]
    ax.axvspan(lo, hi, color=OK["grey"], alpha=0.20, lw=0,
               label=r"$\alpha$-swept band")
    # the Argonaute-anchored point: alpha = 1 with the HeLa total-Ago count,
    # i.e. the upper bound the copy number alone permits
    anchor = [q for q in e5["rho_estimates_by_alpha"]
              if abs(q["alpha_loaded_fraction"] - 1.0) < 1e-12]
    if anchor:
        ax.axvline(anchor[0]["rho_low"], color=OK["green"], lw=1.2,
                   label=r"total Ago, $\alpha=1$")
    # The dose series does NOT deliver a calibrated rho. Its point estimates
    # span several decades across construct-dose cells, three of five
    # construct-level exponent intervals fall entirely below the value both
    # models permit, and the pooled figure moves substantially when the
    # two-dose construct is dropped. Plotting the median as a marker on this
    # axis presented an unstable location as a measurement, so it is gone.
    # The spread is reported in the dose section, where its caveats are.

    ax.set_xscale("log")
    ax.set_xlabel(r"$\rho = M / N_{\mathrm{mRNA}}$ (whole-cell mRNA)")
    ax.set_ylabel(r"Kendall $\tau$ (equilibrium vs independent)",
                  fontsize=7.5)
    ax.set_ylim(0, 1.05)
    ax.legend(frameon=False, loc="lower right", fontsize=6, ncol=1)
    fig.tight_layout()
    c = [q for q in e5["tau_0.9_contour_by_H_K"]
         if abs(q["H_K"] - e5["H_K_grid"][-2]) < 1e-9]
    save(fig, "fig2_regime",
         "Model calculation on measured inputs (GEO GSE5814 HeLa abundances; MAPK14-193 "
         "seed-variant series, "
         f"{e5['n_candidate_constructs']} constructs, "
         f"{e5['n_retrieved_offtarget_transcripts_union']} retrieved "
         "off-target transcripts). Kendall tau between candidate rankings "
         "under equilibrium and under independent scoring, against the "
         "competition parameter. The band is the full range over the swept "
         "on-target affinity spread $H_K$; it is narrow, which is why this "
         "is drawn as a line with an envelope rather than as a 2-D grid "
         "(the grid is in the appendix). Below tau = 0.9 the two scorings "
         "order candidates differently. The alpha-swept band spans "
         f"{fmt(e5['rho_hela_band_low'])} to {fmt(e5['rho_hela_band_high'])} "
         "because the guide-loaded fraction is unmeasured; the contour it "
         "has to be compared against sits at rho = "
         f"{fmt(c[0]['rho_at_tau_0.9']) if c else 'n/a'}, inside the band, "
         "which is the identifiability problem the dose series sets out to "
         "address and does not resolve. No data-driven rho is marked on this "
         "axis: the dose fits do not deliver a stable estimate of it.")


# ------------------------------------------------------------------ fig 3 --

CLASS_ORDER = ["8mer", "7mer-m8", "7mer-A1", "6mer"]


def fig3():
    """Three distinct results figures.

    The old single figure carried three unrelated claims. They are now
    separate: the equilibrium-versus-independent comparison (main text), the
    dose exponent (main text) and the site-class diagnostic (appendix).
    """
    nb = val("e7b_null_calibration")
    e9 = val("e9_dose_response")
    if not need("fig3", e7b_null_calibration=nb):
        return
    _fig_assoc(nb)
    _fig_hier(nb)
    if e9 is not None:
        _fig_dose(e9)
    else:
        SKIPPED.append({"panel": "fig_dose",
                        "missing_results": ["e9_dose_response"]})


def _fig_assoc(nb):
    """Primary comparison: does the coupling add anything over independent."""
    st = nb["pooled_spearman_with_null_and_ci"]
    rho = np.array([q["rho"] for q in st], dtype=float)
    fig, axes = plt.subplots(1, 2, figsize=(FULL, 2.05))
    fig.subplots_adjust(wspace=0.34)

    # ---- (a) each scoring net of its OWN null ----
    ax = axes[0]
    for tag, col, lab in (("equilibrium", OK["blue"], "equilibrium"),
                          ("independent", OK["vermillion"], "independent")):
        y = np.array([q[f"null_centred_association_{tag}"] for q in st])
        mu = np.array([q[f"permutation_null_mean_{tag}"] for q in st])
        ci = np.array([q[f"cluster_bootstrap_ci95_{tag}"] for q in st])
        ax.fill_between(rho, ci[:, 0] - mu, ci[:, 1] - mu, color=col,
                        alpha=0.16, lw=0)
        ax.plot(rho, y, "o-", ms=3, lw=1.3, color=col, label=lab)
    ax.axhline(0.0, color=OK["black"], lw=0.8, ls=":")
    ax.annotate("no association", xy=(0.98, 0.0),
                xycoords=("axes fraction", "data"), ha="right", va="bottom",
                fontsize=5.5, color="#555555")
    ylo, yhi = ax.get_ylim()
    span = max(yhi, 0.0) - min(0.0, ylo)
    ax.set_ylim(min(0.0, ylo) - 0.06 * span, max(yhi, 0.0) + 0.24 * span)
    ax.set_xscale("log")
    ax.set_xlabel(r"$\rho$")
    ax.set_ylabel("association net of null", fontsize=7)
    ax.legend(frameon=False, loc="upper left", fontsize=5.5,
              handletextpad=0.4, borderaxespad=0.2)
    panel_label(ax, "a", dx=-0.26)

    # ---- (b) the paired test: what survives the shared null ----
    ax = axes[1]
    raw = np.array([q["equilibrium_minus_independent"] for q in st])
    net = np.array([q["paired_net_gap"] for q in st])
    gci = np.array([q["cluster_bootstrap_ci95_gap"] for q in st])
    ax.fill_between(rho, gci[:, 0], gci[:, 1], color=OK["grey"], alpha=0.25,
                    lw=0, label="cluster 95% CI")
    ax.plot(rho, raw, "o-", ms=3, lw=1.3, color=OK["black"],
            label="raw gap")
    ax.plot(rho, net, "s--", ms=3, lw=1.3, color=OK["orange"],
            label="net of paired null")
    ax.axhline(0.0, color=OK["black"], lw=0.8, ls=":")
    ax.set_xscale("log")
    ax.set_xlabel(r"$\rho$")
    ax.set_ylabel("equilibrium $-$ independent", fontsize=7)
    ax.legend(frameon=False, loc="lower left", fontsize=5.2,
              handletextpad=0.4, borderaxespad=0.2, labelspacing=0.25)
    panel_label(ax, "b", dx=-0.30)

    save(fig, "fig_assoc",
         "Model calculation against measured repression, GSE5814. Whether the "
         "shared-pool coupling adds anything over independent scoring. "
         f"(a) Pooled Spearman over {nb['n_constructs_analysed']} constructs "
         "between predicted bound fraction and measured log ratio, each "
         "scoring shown net of its OWN within-construct permutation null; "
         "bands are construct-cluster 95% intervals. Repression is negative, "
         "so below zero is the working direction. (b) The difference between "
         "the two scorings. The raw gap is reliably nonzero: its "
         "construct-cluster interval excludes zero at "
         f"{sum(1 for q in st if not (q['cluster_bootstrap_ci95_gap'][0] <= 0 <= q['cluster_bootstrap_ci95_gap'][1]))} "
         f"of {len(st)} values of rho. It is nevertheless not evidence for "
         "the coupling: under a paired permutation null, one shuffle applied "
         "to both models, what survives is at most "
         f"{max(abs(q['paired_net_gap_over_cluster_se']) for q in st):.2f} of "
         "one cluster standard error. The two scorings have different null "
         "baselines because pooling constructs leaves a between-construct "
         "correlation a within-construct shuffle cannot remove.")


def _fig_dose(e9):
    """The dose identifiability audit, as its own figure."""
    ok = [p for p in e9["per_construct"] if p["status"] == "OK"]
    fig, ax = plt.subplots(1, 1, figsize=(FULL * 0.85, 1.42))
    y = np.arange(len(ok))
    ax.axvspan(-1e4, 1.0, color=OK["vermillion"], alpha=0.10, lw=0)
    ax.annotate("incompatible under proportional loading", xy=(0.02, 1.03),
                xycoords="axes fraction", fontsize=5.5,
                color=OK["vermillion"], va="bottom")
    series = [("class_fit_loglog_slope_pool_vs_dose", "class_fit_bootstrap",
               OK["blue"], "s", "site-class $K$"),
              ("loglog_slope_pool_vs_dose", "bootstrap", OK["grey"], "o",
               "thermodynamic $K$")]
    lim = [1.0, 1.0]
    for j, (skey, bkey, col, mk, lab) in enumerate(series):
        if not all(skey in p for p in ok):
            continue
        sl = np.array([p[skey]["slope"] for p in ok], dtype=float)
        b = [(p.get(bkey) or {}).get("slope_ci95", [np.nan, np.nan])
             for p in ok]
        lo = np.array([q[0] for q in b], dtype=float)
        hi = np.array([q[1] for q in b], dtype=float)
        ax.errorbar(sl, y + (0.5 - j) * 0.2,
                    xerr=[np.abs(sl - lo), np.abs(hi - sl)], fmt=mk, ms=3.5,
                    lw=1.0, capsize=2, color=col, label=lab)
        lim = [min(lim[0], np.nanmin(lo)), max(lim[1], np.nanmax(hi))]
    ax.axvline(1.0, color=OK["black"], lw=1.0, ls="--")
    ax.set_yticks(y)
    ax.set_yticklabels([p["construct"] for p in ok], fontsize=5.5)
    ax.set_xlabel(r"$\mathrm{d}\log(\mathrm{pool})/"
                  r"\mathrm{d}\log(\mathrm{dose})$")
    if not np.isfinite(lim[0]) or not np.isfinite(lim[1]) \
            or lim[1] - lim[0] < 1e-6:
        lim = [0.0, 2.0]
    pad = 0.06 * (lim[1] - lim[0])
    ax.set_xlim(lim[0] - pad, lim[1] + pad)
    ax.set_ylim(-0.6, len(ok) - 0.4)
    ax.legend(frameon=False, loc="lower right", fontsize=5.5,
              handletextpad=0.4, borderaxespad=0.2)
    save(fig, "fig_dose",
         "Fitted dose exponent per construct on GSE28786, both estimators, "
         "with 95% bootstrap intervals. Conservation makes the pool convex in "
         "the loaded amount, so under the proportional-loading assumption the "
         "exponent cannot fall below 1; the shaded region therefore indicts "
         "the combined specification rather than equilibrium alone. The "
         "constructs are variants of one another, which is why the audit "
         "cannot separate the mechanism from the assumption.")


def _fig_hier(nb):
    """Appendix: the measured site-class order is not the canonical one."""
    fig, ax = plt.subplots(1, 1, figsize=(HALF, 2.1))
    rules = [("canonical_strongest", OK["blue"], "o", "strongest class"),
             ("best_ddG", OK["orange"], "s",
              r"lowest-$\Delta G_{\mathrm{eff}}$ site")]
    xs = np.arange(len(CLASS_ORDER))
    for j, (rule, col, mk, lab) in enumerate(rules):
        d = nb["pooled_site_class"][rule]
        med = np.array([d[c]["median_log10ratio"] for c in CLASS_ORDER])
        cis = np.array([d[c]["median_ci95"] for c in CLASS_ORDER])
        ax.errorbar(xs + (j - 0.5) * 0.18, med,
                    yerr=[med - cis[:, 0], cis[:, 1] - med],
                    fmt=mk, ms=3.5, lw=1.1, capsize=2, color=col, label=lab)
        if j == 0:
            for k, c in enumerate(CLASS_ORDER):
                n = d[c]["n"]
                ax.annotate(f"{n / 1000:.1f}k" if n >= 1000 else str(n),
                            (xs[k], 1.02), xycoords=ax.get_xaxis_transform(),
                            ha="center", va="bottom", fontsize=5.5,
                            color="#555555")
            ax.annotate("n:", (-0.5, 1.02),
                        xycoords=ax.get_xaxis_transform(), ha="right",
                        va="bottom", fontsize=5.5, color="#555555")
    ax.axhline(0.0, color=OK["black"], lw=0.6, ls=":")
    ax.set_xticks(xs)
    ax.set_xticklabels(CLASS_ORDER, fontsize=6.5, rotation=22, ha="right")
    ax.set_xlim(-0.55, len(CLASS_ORDER) - 0.45)
    ax.set_ylabel(r"median measured $\log_{10}$ ratio")
    ax.legend(frameon=False, loc="lower right", fontsize=5.5)
    save(fig, "fig_hier",
         "Measured repression by seed site class over "
         f"{nb['n_constructs_analysed']} GSE5814 constructs, under both site "
         "assignment rules, with bootstrap 95% intervals on the median and "
         "pair counts above each pair. The two 7mer classes are exchanged "
         "relative to the canonical order under both rules.")


# ------------------------------------------------------------------ fig 4 --

def fig4():
    """Appendix: retrieval invariance on the real transcriptome."""
    e4 = val("e4_retrieval_invariance")
    if not need("fig4", e4_retrieval_invariance=e4):
        return
    e5, e9 = val("e5_hela_regime"), val("e9_dose_response")
    rows = e4["table"]
    rhos = e4["rho_values"]
    Rs = [R for R in e4["R_values"] if R <= 500]
    fig, axes = plt.subplots(1, len(rhos), figsize=(FULL, 2.6), sharey=True)
    for i, rho in enumerate(rhos):
        ax = axes[i]
        for rule, col, mk, lab in (
                ("affinity_weighted_x_over_K", OK["blue"], "o",
                 r"affinity weighted $\sum x_j/K_j$"),
                ("abundance_mass_x", OK["vermillion"], "s",
                 r"abundance mass $\sum x_j$")):
            pts = [(q["R"], q["rel_err_o_target"]) for q in rows
                   if q.get("rule") == rule and q["rho"] == rho
                   and q["R"] in Rs]
            pts.sort()
            if pts:
                ax.plot([q[0] for q in pts], [max(q[1], 1e-12) for q in pts],
                        mk + "-", ms=3.5, lw=1.2, color=col, label=lab)
        ax.axhline(0.01, color=OK["grey"], lw=0.9, ls=":")
        ax.annotate("1% error", xy=(Rs[0], 0.012), fontsize=5.5,
                    color=OK["grey"], va="bottom")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xticks(Rs)
        ax.set_xticklabels([str(R) for R in Rs], fontsize=6.5)
        ax.minorticks_off()
        ax.set_xlabel("retrieval depth $R$")
        ax.set_title(rf"$\rho = {rho:g}$", fontsize=7.5)
        panel_label(ax, "abc"[i], dx=-0.12)
    axes[0].set_ylabel(r"relative error in $o_{\mathrm{target}}$")
    axes[1].legend(frameon=False, loc="upper center", fontsize=6.5,
                   bbox_to_anchor=(0.5, -0.22), ncol=2)

    # No panel is marked as "the" relevant one. Which rho a real cell sits at
    # is exactly what is not identified: the alpha-swept scenario range spans
    # decades and the dose fits do not narrow it, so singling out a panel
    # would assert a calibration this project does not have.
    note = ""
    if e5 is not None:
        note = (" Which panel a transfected cell corresponds to is not "
                "determined here: the scenario range for the competition "
                f"parameter spans {fmt(e5['rho_hela_band_low'])} to "
                f"{fmt(e5['rho_hela_band_high'])} because the guide-loaded "
                "fraction is unmeasured, and it covers all three panels.")
    save(fig, "fig4_retrieval",
         "Model calculation on measured inputs (GEO GSE5814 abundances, GENCODE v50 3'UTRs; siRNA "
         f"MAPK14-193 parent against the full "
         f"{e4['reference_set_size_including_on_target']}-transcript "
         "reference). Relative error in on-target occupancy when the "
         "competitor set is truncated to the top R and the remainder is "
         "folded into a linear background, under the affinity-weighted "
         "calibration rule and the abundance-mass control. Each panel is one "
         "value of the competition parameter. The affinity-weighted rule is "
         "the correct one and is better everywhere, but neither rule is "
         "reliable at shallow depth: the linearisation assumes the omitted "
         "transcripts are weakly binding, which held in only "
         f"{e4['n_rows_where_linearisation_holds']} of "
         f"{e4['n_truncated_rows']} truncated rows." + note)


# ----------------------------------------------------------- appendix figs --

def figA1():
    """Appendix: the 2-D phase grid the main text replaces with Fig 2."""
    e5 = val("e5_hela_regime")
    if not need("figA1", e5_hela_regime=e5):
        return
    rho = np.array(e5["rho_grid"], dtype=float)
    hks = np.array(e5["H_K_grid"], dtype=float)
    G = np.array([e5["tau_grid_beta_zero"][f"H_K={h}"]
                  for h in e5["H_K_grid"]], dtype=float)
    fig, ax = plt.subplots(figsize=(HALF, 2.6))
    # clip the colour range to what the data occupies, rather than 0..1
    m = ax.pcolormesh(rho, hks, G, shading="nearest", cmap="viridis",
                      vmin=float(G.min()), vmax=float(G.max()))
    ax.contour(rho, hks, G, levels=[0.9], colors=[OK["vermillion"]],
               linewidths=1.6)
    lo, hi = e5["rho_hela_band_low"], e5["rho_hela_band_high"]
    # an outlined region, not hatching: hatching over a colormap is unreadable,
    # and it was covering the contour label, so the contour is named in the
    # legend instead of being labelled in place
    ax.axvline(lo, color="white", lw=1.4, ls="--")
    ax.axvline(hi, color="white", lw=1.4, ls="--")
    ax.plot([], [], color=OK["vermillion"], lw=1.6, label=r"$\tau = 0.9$")
    ax.plot([], [], color="white", lw=1.4, ls="--",
            label=r"$\alpha$-swept HeLa band")
    ax.legend(frameon=True, framealpha=0.75, edgecolor="none",
              loc="lower left", fontsize=6)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$\rho = M / N_{\mathrm{mRNA}}$ (whole-cell mRNA)")
    ax.set_ylabel(r"$H_K$ (sd of $\log_{10} K$ on target)")
    cb = fig.colorbar(m, ax=ax)
    cb.set_label(r"Kendall $\tau$", fontsize=7.5)
    cb.ax.tick_params(labelsize=6.5)
    fig.tight_layout()
    save(fig, "figA1_phase_2d",
         "Model calculation on measured inputs (GEO GSE5814 HeLa abundances). The two-dimensional form "
         "of Fig 2, "
         "kept for completeness. The colour range is clipped to the range the "
         "data occupies, "
         f"{fmt(float(G.min()))} to {fmt(float(G.max()))}, rather than to "
         "0-1. The contours run near-vertical, which is the reason the main "
         "text shows this as a one-dimensional curve with an envelope: the "
         "second axis carries almost no variation.")


def figA2():
    """Appendix: the dose fit in detail, both estimators, pools normalised."""
    e9 = val("e9_dose_response")
    if not need("figA2", e9_dose_response=e9):
        return
    ok = [p for p in e9["per_construct"] if p["status"] == "OK"]
    if not ok:
        SKIPPED.append({"panel": "figA2", "missing_results":
                        ["e9_dose_response has no fitted construct"]})
        return
    has_class = all("class_fit" in p for p in ok)
    ncol = 2 if has_class else 1
    fig, axes = plt.subplots(1, ncol, figsize=(FULL * 0.75 if ncol == 2
                                               else HALF, 2.5), squeeze=False,
                             sharey=True)
    cols = [OK["blue"], OK["orange"], OK["green"], OK["vermillion"],
            OK["purple"]]
    panels = [("free_fit", r"thermodynamic $K$")]
    if has_class:
        panels.append(("class_fit", r"site-class $K$"))
    for j, (key, title) in enumerate(panels):
        ax = axes[0][j]
        for i, p in enumerate(ok):
            d = np.array(p["doses_nM"], dtype=float)
            f = np.array(p[key]["pool_per_dose"], dtype=float)
            # normalised to the lowest dose: the constructs differ by a
            # constant factor that has nothing to do with dose, and without
            # this the y-axis spans the whole diverged range
            ax.plot(d / d[0], f / f[0], "o-", ms=3, lw=1.2,
                    color=cols[i % len(cols)], label=p["construct"])
        xs = np.array([1.0, max(np.array(p["doses_nM"]).max()
                                / np.array(p["doses_nM"]).min()
                                for p in ok)])
        ax.plot(xs, xs, color=OK["black"], lw=1.0, ls="--",
                label="slope 1 (independent)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("dose / lowest dose")
        if j == 0:
            ax.set_ylabel("pool / pool at lowest dose")
        ax.set_title(title, fontsize=7.5)
        panel_label(ax, "ab"[j], dx=-0.22)
        if j == ncol - 1:
            ax.legend(frameon=False, loc="center left",
                      bbox_to_anchor=(1.02, 0.5))
    fig.tight_layout(w_pad=1.6)
    pooled = e9.get("class_fit_pooled_slope_construct_fixed_effects") or {}
    msl = e9["M_vs_dose_slope_summary"]["per_construct"]
    n_excl = e9["M_vs_dose_slope_summary"]["n_with_ci_excluding_one"]
    save(fig, "figA2_dose_detail",
         "Model fitted to measured data (GEO GSE28786; STAT3-1676 and "
         "STAT3-1676M in MCF-7, "
         "HK2-3581, HK2-3581M and HK2-4031 in Hep3B, each against zero-dose "
         "arrays made up to the same total duplex with non-targeting control "
         "siRNA). Fitted effective pool against dose, each construct "
         "normalised to its own lowest dose so the curves are comparable. "
         "The dashed line is the slope-1 null that independent scoring "
         "predicts, since its effective pool is M and M is ASSUMED "
         "proportional to dose. Holding total transfected duplex constant "
         "makes that assumption more plausible but does not establish it, "
         "and it is checked separately: the conservation-inverted M has a "
         f"log-log slope against dose of "
         f"{fmt(min(q['loglog_slope_M_vs_dose'] for q in msl))} to "
         f"{fmt(max(q['loglog_slope_M_vs_dose'] for q in msl))} across "
         f"constructs, and {n_excl} of {len(msl)} bootstrap intervals "
         "exclude the value of 1 the assumption requires. "
         + ("Panel (a) uses the thermodynamic affinity model and panel (b) "
            "the site-class model; the contrast between them is the "
            "argument, because the thermodynamic model does not rank "
            "transcripts and its fits diverge. "
            if has_class else "")
         + (f"The pooled exponent under the site-class model is "
            f"{fmt(pooled['slope'])} with bootstrap interval "
            f"{fmt((e9.get('class_fit_pooled_slope_bootstrap_ci95') or [float('nan')])[0])}"
            f" to {fmt((e9.get('class_fit_pooled_slope_bootstrap_ci95') or [float('nan'), float('nan')])[1])}, "
            f"which contains 1; dropping HK2-4031, the construct with only "
            f"two dose points, moves it to "
            f"{fmt(e9['class_fit_pooled_slope_excluding_HK2_4031'])}, so the "
            f"pooled superlinear estimate is not robust."
            if pooled.get("slope") is not None else ""))


def main():
    fig1()
    fig2()
    fig3()
    fig4()
    figA1()
    figA2()
    with open(os.path.join(FIGURES, "CAPTIONS.json"), "w") as fh:
        json.dump({"captions": CAPTIONS, "skipped_panels": SKIPPED}, fh,
                  indent=2)
    # the caption files are derived artifacts like any other. They were in
    # the ledger but nothing refreshed them, so their recorded hashes went
    # stale on every figure rebuild and stage A reported it as a data
    # integrity failure. Registering them here keeps the record current.
    with open(os.path.join(FIGURES, "CAPTIONS.md"), "w") as fh:
        fh.write("# Figure captions\n\nGenerated by scripts/make_figures.py "
                 "from results/*.json. No number here was typed by hand.\n\n")
        for k, v in CAPTIONS.items():
            fh.write(f"## {k}\n\n{v}\n\n")
        if SKIPPED:
            fh.write("## Panels skipped\n\nA panel whose source result is "
                     "missing or FAILED is omitted rather than drawn from "
                     "another source.\n\n")
            for s in SKIPPED:
                fh.write(f"- `{s['panel']}`: {s['missing_results']}\n")
    for fn in ("CAPTIONS.json", "CAPTIONS.md"):
        P.register_local(os.path.join(FIGURES, fn), "figures",
                         note="figure captions generated from results/*.json")
    print(f"wrote figures/CAPTIONS.json and CAPTIONS.md "
          f"({len(CAPTIONS)} figures, {len(SKIPPED)} skipped panels)")


if __name__ == "__main__":
    main()
