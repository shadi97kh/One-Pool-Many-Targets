# Submission 101: figure and experiment map

Reference: *One pool, many targets: a conservation layer and what archival data can identify*,
GEM bio workshop. Figure numbers below follow the uploaded submission, not the
historical figure filenames. Its extracted text matches the saved workshop PDF
exactly. The source snapshot is `bd7850d3cac09b9564ea4b394fbdad111d399f3e` (September 7, 2026).

| Submission figure | Subject | Saved figure | Experiment results | Plot source |
|---|---|---|---|---|
| 1 | Coupling versus independent scoring | [fig_assoc.pdf](figures/fig_assoc.pdf) | [e7_offtarget_ranking.json](results/e7_offtarget_ranking.json)<br>[e7b_null_calibration.json](results/e7b_null_calibration.json) | [make_figures.py](scripts/make_figures.py) |
| 2 | Held-out competitor compression | [fig_approx.pdf](figures/fig_approx.pdf) | [pxb_approximation_cost.json](results/pxb_approximation_cost.json)<br>[pxb_audit.json](results/pxb_audit.json) | [make_px_figures.py](scripts/make_px_figures.py) |
| 3 | Dose exponent by construct | [fig_dose.pdf](figures/fig_dose.pdf) | [e9_dose_response.json](results/e9_dose_response.json) | [make_figures.py](scripts/make_figures.py) |
| 4 | Workflow schematic | [workflow_GEM.png](figures/workflow_GEM.png) | Schematic; no numeric result | Supplied artwork |
| 5 | Loaded-pool budget | [fig1_mechanism.pdf](figures/fig1_mechanism.pdf) | [e5b_budget_curve.json](results/e5b_budget_curve.json) | [make_figures.py](scripts/make_figures.py) |
| 6 | Competition regime | [fig2_regime.pdf](figures/fig2_regime.pdf) | [e5_hela_regime.json](results/e5_hela_regime.json) | [make_figures.py](scripts/make_figures.py) |
| 7 | Redistribution and high-resource limit | [figA3_theory.pdf](figures/figA3_theory.pdf) | [e2b_redistribution_curve.json](results/e2b_redistribution_curve.json)<br>[e3_pairwise_limit.json](results/e3_pairwise_limit.json) | [make_figures.py](scripts/make_figures.py) |
| 8 | Compression selection, timing and gradient audit | [px_B_approx.pdf](figures/px_B_approx.pdf) | [pxb_approximation_cost.json](results/pxb_approximation_cost.json)<br>[pxb_audit.json](results/pxb_audit.json) | [make_px_figures.py](scripts/make_px_figures.py) |
| 9 | Measured seed-class repression | [fig_hier.pdf](figures/fig_hier.pdf) | [e7b_null_calibration.json](results/e7b_null_calibration.json) | [make_figures.py](scripts/make_figures.py) |
| 10 | Retrieval-depth approximation error | [fig4_retrieval.pdf](figures/fig4_retrieval.pdf) | [e4_retrieval_invariance.json](results/e4_retrieval_invariance.json) | [make_figures.py](scripts/make_figures.py) |
| 11 | Regime surface and dose-fit detail | [figA1_phase_2d.pdf](figures/figA1_phase_2d.pdf)<br>[figA2_dose_detail.pdf](figures/figA2_dose_detail.pdf) | [e5_hela_regime.json](results/e5_hela_regime.json)<br>[e9_dose_response.json](results/e9_dose_response.json) | [make_figures.py](scripts/make_figures.py) |

The machine-readable [figure_map.json](figure_map.json) also lists each experiment runner.
Figure 11 combines two saved assets. Figure 4 is supplied artwork; its editable
drawing source was not present in the workshop snapshot. Both the corrected
`workflow_GEM.png` used in the paper and its original image are preserved.

## Tables and experiments without a dedicated main-text figure

| Submission material | Saved results | Source |
|---|---|---|
| Table 1: shallow retrieval with saturable bins | `results/e4b_binned_background.json` | `scripts/run_e4b.py`, `src/riscpool/background.py` |
| Table 2: dose fits and intervals | `results/e9_dose_response.json` | `scripts/run_e9.py`, `src/riscpool/dosefit.py` |
| Solver correctness and implicit gradients | `results/e1_solver_correctness.json` | `scripts/run_theory.py`, `src/riscpool/equilibrium.py`, `src/riscpool/checks.py` |
| Redistribution signs and high-resource limit | `results/e2_redistribution.json`, `results/e3_pairwise_limit.json` | `scripts/run_theory.py`, `src/riscpool/theory.py` |
| Cross-context audit, GSE14073 | `results/e10_cross_context.json` | `scripts/run_e10.py`, `src/riscpool/crosscontext.py`, `src/riscpool/dosefit.py` |
| Simulated dose-estimator validation | `results/e9v_sim_estimator_validation.json` | `scripts/run_e9v.py` |
| Simulated interaction recovery | `results/e6_sim_interaction_recovery.json` | `scripts/run_e6.py` |
| Huesken efficacy control | `results/e8_huesken_efficacy.json` | `scripts/run_e8.py`, `src/riscpool/huesken.py` |
| External affinity correction, disclosed in appendix B | `results/pxa_affinity_correction.json`, `results/positive_extensions/A_*`, `figures/px_A_external.*` | `scripts/run_pxa_affinity.py`, `scripts/make_px_figures.py` |
| Frozen family split and extension audits | `results/px0_audit_and_spec.json`, `results/px_verify.json`, `results/positive_extensions/run_spec.json` | `scripts/run_px_audit.py`, `scripts/run_px_verify.py` |

The negative external affinity-correction result remains included: the submission
explicitly discloses it even though it has no numbered figure in the paper.
Compression figures use the audited residual/timing exports, including
`B_audit_residuals.csv`, `B_audit_finite_differences.csv`, and `B_audit_export.json`.
The older grid's own-system residual must not be read as the full-system defect.

## Dataset numbering

| Submission | Repository identifier | Dataset or input |
|---|---|---|
| D1 | D1 | GSE5814, Jackson off-target arrays |
| D2 | D2 | E-MEXP-668, Birmingham off-target arrays |
| D3 | D7 | GSE28786, Caffrey dose series |
| D4 | D8 | GSE14073, Burchard cross-context data |
| Reference inputs | D3 / D4 / D5 / D6 / D9 | GENCODE v50 / HeLa abundance / Huesken efficacy / literature constants / full-text retrieval |

Acquisition and feature results are preserved as `results/d*.json` and
`results/f*.json`. Their runners are listed by `python3 scripts/run_all.py --list`.
`data/PROVENANCE.json` records the source URLs and hashes.
