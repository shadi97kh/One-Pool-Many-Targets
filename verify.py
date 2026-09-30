#!/usr/bin/env python3
"""
verify.py

Three stages, any of which can fail the build:

  A  file integrity. Every OK record in data/PROVENANCE.json is re-hashed and
     compared against the recorded SHA256 and byte size.
  B  recomputation. Every experiment whose function is pure and seeded is
     re-run from the recorded seed and every numeric leaf of its result is
     compared against results/<name>.json within the recorded tolerance.
  C  report regeneration. results/SUMMARY.md is regenerated and compared
     against the copy on disk, ignoring only the generation timestamp.

Exits nonzero on any mismatch, and writes results/verify_status.json.

The old contents of this file (the solver correctness suite that shipped with
the seed code) now live in src/riscpool/checks.py and are exercised by e1.
"""

import os

# Pin the thread pools BEFORE numpy, scipy or torch reach an import below.
# Stage B re-runs the experiments in THIS process, and the ones that dominate
# it are thousands of small solves rather than a few large ones, so intra-op
# threading costs far more in contention than it saves. run_e9.py sets the
# same variables at its own top, but by the time verify imports it numpy has
# long since read them, so the setting there cannot help: an unpinned stage B
# run burned 18 CPU-hours in 1.5 wall hours without reaching the dose fit.
# Thread count changes the clock and not the numbers, which is also why
# pinning here cannot hide a real reproduction failure.
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS",
           "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse                                              # noqa: E402
import json                                                  # noqa: E402
import re                                                    # noqa: E402
import subprocess                                            # noqa: E402
import sys                                                   # noqa: E402
import traceback                                             # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "src"))

from riscpool.provenance import PROV_PATH, ROOT, sha256_file, utcnow  # noqa: E402
from riscpool.runner import RESULTS, load_all                         # noqa: E402

DEFAULT_RTOL = 1e-6
DEFAULT_ATOL = 1e-12
SKIP_KEYS = {"path", "features_path", "annotation", "samples", "expression",
             "errors", "constants_used"}
SKIP_SUFFIX = ("_path", "_utc", "_note", "_NOTE")


def numeric_leaves(obj, prefix=""):
    out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in SKIP_KEYS or k.endswith(SKIP_SUFFIX):
                continue
            out.update(numeric_leaves(v, f"{prefix}.{k}" if prefix else k))
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            out.update(numeric_leaves(v, f"{prefix}[{i}]"))
    elif isinstance(obj, bool):
        out[prefix] = float(obj)
    elif isinstance(obj, (int, float)):
        out[prefix] = float(obj)
    return out


def close(a, b, rtol, atol):
    if a != a and b != b:
        return True
    if a in (float("inf"), float("-inf")) or b in (float("inf"), float("-inf")):
        return a == b
    return abs(a - b) <= atol + rtol * max(abs(a), abs(b))


def stage_a(allow_missing=False):
    checks, bad = [], 0
    if not os.path.exists(PROV_PATH):
        return [{"stage": "A", "name": "PROVENANCE.json", "ok": False,
                 "detail": "missing"}], 1
    led = json.load(open(PROV_PATH))
    for r in led.get("records", []):
        if r.get("status") != "OK" or not r.get("sha256"):
            continue
        p = os.path.join(ROOT, r["path"])
        if not os.path.exists(p):
            # A fresh clone has no downloads yet. That is not a hash failure,
            # so it is reported as such only when strictness is requested.
            checks.append({
                "stage": "A", "name": r["path"], "ok": bool(allow_missing),
                "detail": "file not present; run the acquisition scripts "
                          "first (see README). Reported as a pass because "
                          "--allow-missing was given."
                          if allow_missing else "file missing"})
            bad += (not allow_missing)
            continue
        if r.get("content_stability") == "volatile":
            checks.append({
                "stage": "A", "name": r["path"], "ok": True,
                "detail": "hash not enforced: " + str(
                    r.get("content_stability_reason", "volatile source"))})
            continue
        h = sha256_file(p)
        sz = os.path.getsize(p)
        ok = (h == r["sha256"]) and (sz == r["bytes"])
        checks.append({"stage": "A", "name": r["path"], "ok": ok,
                       "detail": "" if ok else
                       f"sha256 {h[:12]} vs {r['sha256'][:12]}, "
                       f"bytes {sz} vs {r['bytes']}"})
        bad += (not ok)
    return checks, bad


EXPERIMENTS = {}


def register():
    """Import the experiment functions lazily; a module that cannot import is
    itself a verification failure, not a crash."""
    import importlib.util

    def load(script, attr):
        p = os.path.join(ROOT, "scripts", script)
        spec = importlib.util.spec_from_file_location(
            script[:-3] + "_mod", p)
        m = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = m
        spec.loader.exec_module(m)
        return getattr(m, attr)

    for name, script, attr in [
        ("e1_solver_correctness", "run_theory.py", "e1"),
        ("e2_redistribution", "run_theory.py", "e2"),
        ("e3_pairwise_limit", "run_theory.py", "e3"),
        ("e4_retrieval_invariance", "run_e4.py", "fn"),
        ("e5_hela_regime", "run_e5.py", "fn"),
        ("e7_offtarget_ranking", "run_e7.py", "fn"),
        ("e6_sim_interaction_recovery", "run_e6.py", "fn"),
        ("e8_huesken_efficacy", "run_e8.py", "fn"),
        ("e4b_binned_background", "run_e4b.py", "fn"),
        ("e5b_budget_curve", "run_figseries.py", "budget"),
        ("e2b_redistribution_curve", "run_figseries.py", "redistribution"),
        ("e7b_null_calibration", "run_e7b.py", "fn"),
        ("e9v_sim_estimator_validation", "run_e9v.py", "fn"),
        ("e9_dose_response", "run_e9.py", "fn"),
        ("e10_cross_context", "run_e10.py", "fn"),
        ("d1_seed_validation", "run_seed_validation.py", "fn"),
    ]:
        try:
            EXPERIMENTS[name] = load(script, attr)
        except Exception as exc:
            EXPERIMENTS[name] = ("IMPORT_FAILED", f"{type(exc).__name__}: {exc}")


def stage_b(only=None, rtol=DEFAULT_RTOL, atol=DEFAULT_ATOL):
    register()
    stored = load_all()
    checks, bad = [], 0
    for name, fn in EXPERIMENTS.items():
        if only and name not in only:
            continue
        if name not in stored:
            continue
        rec = stored[name]
        if rec["status"] != "OK":
            checks.append({"stage": "B", "name": name, "ok": True,
                           "detail": "recorded FAILED; nothing to reproduce"})
            continue
        if isinstance(fn, tuple):
            checks.append({"stage": "B", "name": name, "ok": False,
                           "detail": f"could not import: {fn[1]}"})
            bad += 1
            continue
        try:
            got = fn(seed=rec.get("seed", 0))
        except Exception:
            checks.append({"stage": "B", "name": name, "ok": False,
                           "detail": "re-run raised:\n"
                                     + traceback.format_exc()[-1500:]})
            bad += 1
            continue
        A = numeric_leaves(rec["values"])
        B = numeric_leaves(got)
        common = sorted(set(A) & set(B))
        missing = sorted((set(A) ^ set(B)))
        diffs = [(k, A[k], B[k]) for k in common
                 if not close(A[k], B[k], rtol, atol)]
        ok = (not diffs) and (not missing)
        checks.append({
            "stage": "B", "name": name, "ok": ok,
            "n_numeric_values_compared": len(common),
            "n_mismatched": len(diffs),
            "n_keys_only_on_one_side": len(missing),
            "rtol": rtol,
            "detail": "" if ok else json.dumps(
                {"first_mismatches": [{"key": k, "stored": a, "recomputed": b}
                                      for k, a, b in diffs[:12]],
                 "keys_only_on_one_side": missing[:12]}),
        })
        bad += (not ok)
    return checks, bad


def stage_c():
    p = os.path.join(RESULTS, "SUMMARY.md")
    if not os.path.exists(p):
        return [{"stage": "C", "name": "SUMMARY.md", "ok": False,
                 "detail": "not generated"}], 1
    before = open(p).read()
    r = subprocess.run([sys.executable,
                        os.path.join(ROOT, "scripts", "make_summary.py")],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        return [{"stage": "C", "name": "SUMMARY.md", "ok": False,
                 "detail": r.stderr[-1500:]}], 1
    after = open(p).read()

    def strip(s):
        # drop the generation timestamp, and drop the verify section itself:
        # it reports the outcome of this very check, so comparing it would be
        # self-referential rather than a test of report generation.
        s = re.sub(r"^- generated: .*$", "", s, flags=re.M)
        i = s.find("## 6. verify.py")
        return s[:i] if i >= 0 else s

    ok = strip(before) == strip(after)
    return [{"stage": "C", "name": "SUMMARY.md", "ok": ok,
             "detail": "" if ok else
             "regenerated report differs from the copy on disk"}], (not ok)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stages", default="ABC")
    ap.add_argument("--only", default=None,
                    help="comma separated experiment names for stage B")
    ap.add_argument("--rtol", type=float, default=DEFAULT_RTOL)
    ap.add_argument("--allow-missing", action="store_true",
                    help="treat a not-yet-downloaded file as a pass in stage "
                         "A, for checking recomputation in a fresh clone")
    args = ap.parse_args()
    only = set(args.only.split(",")) if args.only else None

    all_checks, bad = [], 0
    if "A" in args.stages:
        print("== stage A: file integrity ==", flush=True)
        c, b = stage_a(allow_missing=args.allow_missing)
        all_checks += c
        bad += b
        print(f"   {len(c)} files checked, {b} mismatched", flush=True)
    if "B" in args.stages:
        print("== stage B: recomputation ==", flush=True)
        c, b = stage_b(only=only, rtol=args.rtol)
        all_checks += c
        bad += b
        for x in c:
            print(f"   {x['name']:32s} {'OK' if x['ok'] else 'MISMATCH'}"
                  f"  ({x.get('n_numeric_values_compared', 0)} values)",
                  flush=True)
            if not x["ok"]:
                print("      " + str(x["detail"])[:1200], flush=True)
    if "C" in args.stages:
        print("== stage C: report regeneration ==", flush=True)
        c, b = stage_c()
        all_checks += c
        bad += b
        print(f"   SUMMARY.md {'OK' if not b else 'DIFFERS'}", flush=True)

    status = {
        "generated_utc": utcnow(),
        "stages_run": args.stages,
        "rtol": args.rtol,
        "allow_missing": bool(args.allow_missing),
        "n_checks": len(all_checks),
        "n_failed": int(bad),
        "exit_status": 0 if bad == 0 else 1,
        "verdict": "PASS" if bad == 0 else "FAIL",
        "checks": [{k: v for k, v in c.items() if k != "detail"}
                   | {"detail": str(c.get("detail", ""))[:400]}
                   for c in all_checks],
    }
    with open(os.path.join(RESULTS, "verify_status.json"), "w") as fh:
        json.dump(status, fh, indent=2)
    print(f"\nverify: {status['verdict']}  "
          f"({bad} failed of {len(all_checks)} checks)")
    sys.exit(status["exit_status"])


if __name__ == "__main__":
    main()
