"""
CORE phase 0: audit the current implementation, then FREEZE the specification
for the two new experiments.

This runs before any held-out outcome is looked at. It records what the
existing code actually does, so the new work can be checked against it rather
than against a remembered version of it, and it writes a machine-readable run
specification that fixes seeds, splits, metrics, exclusions and tolerances.

Freezing here does not make the historical study preregistered. It fixes the
NEW analysis only.
"""
import hashlib
import json
import os
import platform
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                        # noqa: E402
import pandas as pd                                       # noqa: E402
from riscpool import features, kmers, runner              # noqa: E402
from riscpool.provenance import DATA, ROOT                # noqa: E402

OUT = os.path.join(ROOT, "results", "positive_extensions")


def sh(c):
    try:
        return subprocess.run(c, shell=True, capture_output=True, text=True,
                              cwd=ROOT, timeout=60).stdout.strip()
    except Exception as e:
        return f"<unavailable: {e}>"


def sha(path, n=16):
    if not os.path.exists(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()[:n]


def fn(seed=0):
    from riscpool.offtarget import load_candidates
    from riscpool.sirna import per_construct

    cand = load_candidates()
    d1 = per_construct()
    d2_sir = pd.read_parquet(os.path.join(DATA, "birmingham_sirna.parquet"))
    d2_sir = d2_sir[d2_sir.guide_5to3_dna.notna()]
    d2_resp = pd.read_parquet(os.path.join(DATA, "birmingham_response.parquet"))

    # ---- exact guide and seed overlap, response-independent ---------------
    d1g = {r.construct: r.guide_5to3_dna for _, r in d1.iterrows()}
    d1seed = {c: g[1:8] for c, g in d1g.items()}
    d2g = (d2_sir[["construct", "guide_5to3_dna", "seed_2_8_dna"]]
           .drop_duplicates("guide_5to3_dna"))
    guide_overlap = sorted({g for g in d2g.guide_5to3_dna} & set(d1g.values()))
    seed_overlap = sorted({s for s in d2g.seed_2_8_dna} & set(d1seed.values()))

    # ---- family definition, fixed here, before any outcome is scored ------
    # D1: the deposited series is one MAPK14 guide plus 19 single-position
    # seed variants of it, and four further guides against two genes. Seed
    # variants of one guide are not independent of it, and two guides against
    # one gene share that gene's biology, so the family is the TARGET GENE.
    d1_fam = {c: (d1.set_index("construct").loc[c, "target_gene"])
              for c in d1g}
    # D2: twelve distinct guides with twelve distinct seeds and no
    # parent/variant series, so each seed is its own family. The map must
    # cover EVERY construct, including the same guide assayed at a second
    # dose, which is exactly why the family is the seed and not the construct.
    d2_fam = {r.construct: r.seed_2_8_dna
              for _, r in d2_sir[["construct", "seed_2_8_dna"]]
              .drop_duplicates().iterrows()}

    spec = {
        "spec_version": 1,
        "frozen_utc": runner.utcnow(),
        "purpose": ("freezes the NEW analysis only; the historical archival "
                    "study is not preregistered by this file"),
        "datasets_by_accession": {
            "D1_training": "GSE5814",
            "D2_external": "E-MEXP-668",
            "note": "resolved by accession, not by repository D-number",
        },
        "rho_convention": {
            "definition": "rho = M / N_mRNA_whole_cell",
            "denominator": "total cellular mRNA count, NOT the retrieved "
                           "competitor abundance sum",
            "verified_in": ["scripts/run_e5.py:total_x = float(n_mrna)",
                            "src/riscpool/calibration.py:rho_from_alpha",
                            "src/riscpool/real_experiments.py:score_construct"],
        },
        "physics_preserved": {
            "dG_open": "-R*T*log(P_unpaired) >= 0",
            "dG_eff": "dG_duplex + dG_open",
            "K_site": "K_ref*exp((dG_eff-dG_ref)/(R*T))",
            "RT_kcal_per_mol": features.RT,
            "temperature_K": 310.15,
            "energy_units": "kcal/mol",
            "p_unpaired_floor": 1e-12,
            "aggregation": "1/K_j = sum_s 1/K_js (mutually exclusive sites)",
            "no_site_transcripts": "zero binding capacity, represented "
                                   "explicitly rather than as infinite K",
        },
        "experiment_A": {
            "model": "log K_js_corrected = log K_js_thermo + delta[class]",
            "anchor_class": "7mer-m8", "anchor_value": 0.0,
            "free_classes": ["8mer", "7mer-A1", "6mer"],
            "init": 0.0, "bounds": [-3.0, 3.0],
            "score": "score_j = -log K_j = logsumexp_s(-log K_js_corrected)",
            "loss": "within-guide pairwise softplus(-t_jk*(score_j-score_k))",
            "y": "-log(expression ratio); larger y = stronger repression",
            "pairs_per_guide": 4096, "pair_seed": 1729,
            "drop_exact_ties": True,
            "balance": "equal weight per guide within family, then per family",
            "lambda_grid": [0.0, 0.01, 0.1, 1.0],
            "lambda_selection": "leave-one-family-out on D1 only; equal-family "
                                "average of per-guide Spearman; ties to "
                                "stronger regularisation",
            "dtype": "float64",
            "comparators": ["thermodynamic (current corrected baseline)",
                            "class-only (no thermodynamic energy)",
                            "thermodynamic + 3 class offsets"],
            "primary_comparison": "model 3 minus model 1",
            "primary_metric": "equal-family average of within-guide Spearman "
                              "between score_j and y_j",
            "bootstrap": {"n": 5000, "seed": 1730,
                          "unit": "family cluster, paired, retaining all "
                                  "guides of a sampled family",
                          "targets": "sampling variation across THIS set of "
                                     "families"},
            "sign_randomisation": {"unit": "family", "exact_if_families_le":
                                   20, "draws_otherwise": 10000,
                                   "null": "family-level exchangeability and "
                                           "symmetry of the paired difference"},
            "eligible_population": "measured guide-gene pairs with a valid "
                                   "canonical UTR and >=1 canonical site "
                                   "under the shared response-independent "
                                   "pipeline; identical rows for all models",
            "external_exclusion_rule": "D2 families whose guide OR seed(2-8) "
                                       "exactly matches any D1 guide are "
                                       "removed from the primary external "
                                       "analysis and reported separately",
        },
        "experiment_B": {
            "reference": "the construct's full retrieved competitor set, "
                         "which is a site-filtered universe and is NOT the "
                         "whole transcriptome",
            "methods": ["full reference", "top-R truncation (omitted dropped)",
                        "top-R + linear beta_omit = sum x_j/K_j",
                        "top-R + saturable affinity-quantile bins"],
            "bins": {"X_b": "sum_{j in b} x_j",
                     "K_b": "X_b / sum_{j in b}(x_j/K_j)",
                     "background_b": "X_b*f/(K_b+f)",
                     "skip_zero_mass_bins": True},
            "rho_grid": [0.001, 0.01, 0.1, 0.5, 1.0, 10.0],
            "R_grid": [25, 50, 100, 200, 500],
            "B_grid": [1, 5, 10, 25, 50, 100, 200],
            "retrieval_order": "by x/K (weighted load), the project's existing "
                               "rule; response-independent",
            "downstream_loss": {
                "definition": "L = q_focal + 0.5 * mean_j q_j over the "
                              "retained explicitly represented transcripts",
                "why": "dimensionless, O(1), and touches both the focal "
                       "target and the retained outputs, so a gradient error "
                       "cannot hide in either alone",
                "frozen_before_any_B_evaluation": True,
                "gradients_wrt": ["log K", "log x (positive x only)", "log M"],
                "membership": "retrieval and bin membership are treated as "
                              "piecewise constant; no gradient is claimed "
                              "through a discrete sorting boundary",
            },
            "constructs": "GSE5814 and E-MEXP-668 constructs, family split "
                          "balanced by dataset of origin",
            "tolerances": {"rel_focal_occupancy": 0.01,
                           "rel_L2_gradient": 0.01,
                           "near_zero_occupancy_abs": 1e-12,
                           "near_zero_gradient_abs": 1e-12},
            "timing": {"warmup": 10, "repetitions": 50,
                       "note": "repetitions are not independent biological "
                               "samples"},
            "split": "deterministic family-level development/test split over "
                     "usable constructs, defined before configuration choice",
        },
        "families": {
            "D1_rule": "target gene",
            "D1_families": sorted(set(d1_fam.values())),
            "D1_construct_to_family": d1_fam,
            "D2_rule": "distinct seed (guide positions 2-8)",
            "D2_families": sorted(set(d2_fam.values())),
            "D2_construct_to_family": d2_fam,
        },
        "overlap_audit": {
            "exact_guide_overlap_D1_D2": guide_overlap,
            "exact_seed_2_8_overlap_D1_D2": seed_overlap,
            "n_guide_overlap": len(guide_overlap),
            "n_seed_overlap": len(seed_overlap),
        },
        "outputs": "results/positive_extensions/",
    }

    audit = {
        "git_commit": sh("git rev-parse HEAD"),
        "git_dirty": bool(sh("git status --porcelain")),
        "python": platform.python_version(),
        "numpy": np.__version__, "pandas": pd.__version__,
        "input_checksums": {
            "data/features.parquet": sha(features.FEAT),
            "data/accessibility_u8_u15.npz": sha(
                os.path.join(DATA, "accessibility_u8_u15.npz")),
            "data/birmingham_response.parquet": sha(
                os.path.join(DATA, "birmingham_response.parquet")),
            "data/birmingham_sirna.parquet": sha(
                os.path.join(DATA, "birmingham_sirna.parquet")),
        },
        "D2_used_for_model_selection_before": False,
        "D2_use_evidence": ("no experiment in results/ consumes the D2 "
                            "response: d2_birmingham records acquisition and "
                            "d2b_birmingham_arrays records parsing only. The "
                            "manuscript states D2 is an acquisition and that "
                            "no experiment consumes it."),
        "candidate_universe": {
            "n_transcripts": int(len(cand)),
            "n_genes": int(cand.gene_symbol.nunique()),
            "source": "GENCODE v50 canonical 3'UTRs, HeLa-expressed",
            "is_whole_transcriptome": False,
        },
        "D1": {"n_constructs": int(len(d1)),
               "n_families": len(set(d1_fam.values()))},
        "D2": {"n_constructs_with_guide":
               int(d2_sir.construct.nunique()),
               "n_distinct_guides": int(d2_sir.guide_5to3_dna.nunique()),
               "n_genes_measured": int(d2_resp.gene_symbol.nunique()),
               "n_genes_measured_with_canonical_utr":
               int(len(set(cand.gene_symbol) & set(d2_resp.gene_symbol))),
               "response_definition":
               "log10(siRNA channel / mock channel), negative is repression"},
    }
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "run_spec.json"), "w") as fh:
        json.dump(spec, fh, indent=1)
    return {"audit": audit, "frozen_spec_path":
            "results/positive_extensions/run_spec.json", "spec": spec}


if __name__ == "__main__":
    runner.run("px0_audit_and_spec", fn, seed=0)
