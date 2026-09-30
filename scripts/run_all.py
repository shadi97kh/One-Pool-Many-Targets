#!/usr/bin/env python3
"""
Run the whole build, in the staging order the project requires.

    D1, D3, D4  ->  e5, e7  ->  e4  ->  e2, e3, e1  ->  D5, e8  ->  e6, D2

The order is not cosmetic. Partial completion must still yield a submission,
so the data acquisition and the two experiments that carry the argument come
first, and e6 and e8 are not started until e7 has produced a result. That
dependency is enforced here, not left to the operator.

A stage that fails does not stop the run. Its experiment writes a FAILED
result and the build continues, because a failed experiment is a real result
and the report has to say so.

    python3 scripts/run_all.py              # everything
    python3 scripts/run_all.py --from e5    # resume from a stage
    python3 scripts/run_all.py --list       # show the plan and exit
"""
import argparse
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))

# (stage name, script, what it does, produces which results)
PLAN = [
    ("d1_d3", "download_d1_d3.py",
     "D1 GSE5814 and D3 GENCODE v50 downloads", []),
    ("lit", "download_lit.py",
     "literature supplementary files, incl. the required siRNA sequences", []),
    ("refseq", "fetch_refseq.py",
     "reference mRNAs for the three transfection target genes", []),
    ("data", "run_data.py",
     "parse D1, extract D3 3'UTR/CDS, build D4 HeLa abundance",
     ["d1_gse5814", "d3_gencode", "d4_hela_abundance"]),
    ("provenance", "register_lit_provenance.py",
     "hash and record the literature files", []),
    ("constants", "write_constants.py",
     "D6 literature constants with citations", []),
    ("seeds", "run_seed_validation.py",
     "recover each seed from measured response; compare with the published "
     "sequences", ["d1_seed_validation"]),
    ("accessibility", "run_accessibility.py",
     "ViennaRNA local accessibility over every candidate 3'UTR",
     ["f1_accessibility"]),
    ("features", "run_features.py",
     "per-site sequence and thermodynamic features", ["f2_features"]),
    ("e5", "run_e5.py", "where HeLa sits: rho, the tau grid, the contour",
     ["e5_hela_regime"]),
    ("e7", "run_e7.py", "real off-target ranking, equilibrium vs independent",
     ["e7_offtarget_ranking"]),
    ("e4", "run_e4.py", "retrieval invariance on the real transcriptome",
     ["e4_retrieval_invariance"]),
    ("theory", "run_theory.py", "e1 solver correctness, e2 redistribution, "
     "e3 pairwise limit", ["e1_solver_correctness", "e2_redistribution",
                           "e3_pairwise_limit"]),
    ("d5", "download_d5.py", "D5 Huesken efficacy set", []),
    ("e8", "run_e8.py", "Huesken efficacy, target-gene split",
     ["e8_huesken_efficacy"]),
    ("e6", "run_e6.py", "SIMULATION: interaction recovery under known truth",
     ["e6_sim_interaction_recovery"]),
    ("d2", "run_d2.py", "D2 Birmingham: identify the ArrayExpress deposit",
     ["d2_birmingham"]),
    ("d2_arrays", "run_d2_arrays.py",
     "D2 Birmingham: fetch and parse the 29 Agilent arrays",
     ["d2b_birmingham_arrays"]),
    ("jackson", "retry_jackson_oa.py",
     "bounded retry of the Jackson 2006 full text",
     ["d9_jackson_oa_retry"]),
    ("e4b", "run_e4b.py",
     "binned background at shallow retrieval depth",
     ["e4b_binned_background"]),
    ("figseries", "run_figseries.py",
     "budget and redistribution curves the figures plot",
     ["e5b_budget_curve", "e2b_redistribution_curve"]),
    ("e7b", "run_e7b.py",
     "site-class CIs, permutation null, bootstrap pooled Spearman",
     ["e7b_null_calibration"]),
    ("e9v", "run_e9v.py",
     "SIMULATION: do the dose estimators recover a known answer",
     ["e9v_sim_estimator_validation"]),
    ("d7", "download_d7.py", "D7 Caffrey dose series downloads", []),
    ("d7_data", "run_data_d7.py", "parse GSE28786, build its candidate set",
     ["d7_gse28786", "d7_candidates"]),
    ("d7_acc", "run_accessibility_d7.py",
     "ViennaRNA accessibility over the D7 candidates",
     ["f3_accessibility_d7"]),
    ("d7_feat", "run_features_d7.py", "features for the D7 guides",
     ["f4_features_d7"]),
    ("e9", "run_e9.py", "dose series: pool per dose, exponent, data-driven "
     "rho", ["e9_dose_response"]),
    ("d8", "download_d8.py", "D8 Burchard cross-context downloads", []),
    ("d8_data", "run_data_d8.py",
     "parse GSE14073, candidates and accessibility",
     ["d8_gse14073", "d8_candidates", "f5_accessibility_d8"]),
    ("e10", "run_e10.py", "same guide, different transcriptome",
     ["e10_cross_context"]),
    ("figures", "make_figures.py",
     "fig1-fig4 plus appendix figures, vector PDF and 300 dpi PNG", []),
    ("manifest", "make_manifest.py", "MANIFEST.json", []),
    ("summary", "make_summary.py", "results/SUMMARY.md", []),
]

# e6 and e8 must not start until e7 has produced a result.
GATED = {"e6": "e7_offtarget_ranking", "e8": "e7_offtarget_ranking"}


def result_exists(name):
    return os.path.exists(os.path.join(ROOT, "results", f"{name}.json"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="start", default=None,
                    help="resume from this stage name")
    ap.add_argument("--only", default=None,
                    help="comma separated stage names")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--no-verify", action="store_true",
                    help="skip the final verify.py run")
    args = ap.parse_args()

    if args.list:
        w = max(len(s[0]) for s in PLAN)
        for name, script, what, _ in PLAN:
            gate = f"  [gated on {GATED[name]}]" if name in GATED else ""
            print(f"  {name:<{w}}  {script:<26} {what}{gate}")
        return 0

    plan = PLAN
    if args.start:
        names = [p[0] for p in PLAN]
        if args.start not in names:
            print(f"unknown stage {args.start!r}; try --list")
            return 2
        plan = PLAN[names.index(args.start):]
    if args.only:
        want = set(args.only.split(","))
        plan = [p for p in PLAN if p[0] in want]

    started = time.time()
    outcomes = []
    for name, script, what, produces in plan:
        gate = GATED.get(name)
        if gate and not result_exists(gate):
            print(f"\n[skip] {name}: gated on {gate}, which has not produced "
                  f"a result yet")
            outcomes.append((name, "SKIPPED_GATE", 0.0))
            continue
        bar = "=" * 72
        print(f"\n{bar}\n[stage] {name}  ({script})\n         {what}\n{bar}",
              flush=True)
        t0 = time.time()
        r = subprocess.run([sys.executable, os.path.join(HERE, script)],
                           cwd=ROOT)
        el = time.time() - t0
        outcomes.append((name, "ok" if r.returncode == 0 else
                         f"exit {r.returncode}", el))

    print("\n" + "=" * 72)
    print(f"{'stage':<16}{'outcome':<18}{'seconds':>10}")
    print("=" * 72)
    for name, out, el in outcomes:
        print(f"{name:<16}{out:<18}{el:>10.1f}")
    print(f"\ntotal {time.time() - started:.1f} s")

    res_dir = os.path.join(ROOT, "results")
    if os.path.isdir(res_dir):
        failed = []
        for fn in sorted(os.listdir(res_dir)):
            if fn.endswith(".json") and not fn.startswith("verify_"):
                with open(os.path.join(res_dir, fn)) as fh:
                    d = json.load(fh)
                if d.get("status") == "FAILED":
                    failed.append(fn[:-5])
        print(f"\nexperiments recorded FAILED: "
              f"{', '.join(failed) if failed else 'none'}")

    if not args.no_verify:
        print("\n" + "=" * 72 + "\n[verify]\n" + "=" * 72, flush=True)
        r = subprocess.run([sys.executable, os.path.join(ROOT, "verify.py")],
                           cwd=ROOT)
        return r.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
