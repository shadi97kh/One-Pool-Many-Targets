"""
results/SUMMARY.md, generated from the JSONs.

Nothing in this file is typed by hand. Every number is read out of
results/*.json, data/PROVENANCE.json or MANIFEST.json at run time.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool.provenance import ROOT, PROV_PATH, utcnow    # noqa: E402
from riscpool.runner import RESULTS, load_all              # noqa: E402

ORDER = ["d1_gse5814", "d1_sirna_sequences", "d1_seed_validation",
         "d2_birmingham", "d2b_birmingham_arrays", "d3_gencode",
         "d4_hela_abundance", "d5_huesken", "d6_ago2_abundance",
         "d7_gse28786", "d7_candidates", "d8_gse14073", "d8_candidates",
         "d9_jackson_oa_retry",
         "f1_accessibility", "f2_features", "f3_accessibility_d7",
         "f4_features_d7", "f5_accessibility_d8",
         "e5_hela_regime", "e5b_budget_curve", "e2b_redistribution_curve",
         "e7_offtarget_ranking", "e7b_null_calibration",
         "e4_retrieval_invariance",
         "e4b_binned_background", "e9_dose_response",
         "e9v_sim_estimator_validation", "e10_cross_context",
         "e2_redistribution", "e3_pairwise_limit", "e1_solver_correctness",
         "e8_huesken_efficacy", "e6_sim_interaction_recovery"]


def fmt(v, depth=0):
    if isinstance(v, float):
        if v != v:
            return "NaN"
        a = abs(v)
        if a != 0 and (a < 1e-3 or a >= 1e6):
            return f"{v:.4e}"
        return f"{v:.6g}"
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "null"
    if isinstance(v, (int, str)):
        return str(v)
    return json.dumps(v)


def scalar_table(values):
    rows = [(k, v) for k, v in values.items()
            if isinstance(v, (int, float, str, bool)) or v is None]
    if not rows:
        return ""
    out = ["| quantity | value |", "|---|---|"]
    for k, v in rows:
        s = fmt(v)
        if len(s) > 300:
            s = s[:297] + "..."
        out.append(f"| `{k}` | {s} |")
    return "\n".join(out)


def listdict_table(name, rows):
    if not rows or not isinstance(rows[0], dict):
        return ""
    cols = list(rows[0].keys())
    out = [f"\n**`{name}`**\n", "| " + " | ".join(cols) + " |",
           "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows[:80]:
        out.append("| " + " | ".join(fmt(r.get(c)) for c in cols) + " |")
    if len(rows) > 80:
        out.append(f"\n_{len(rows)} rows total, first 80 shown; "
                   f"full data in the JSON._")
    return "\n".join(out)


def main():
    res = load_all()
    prov = json.load(open(PROV_PATH)) if os.path.exists(PROV_PATH) else \
        {"records": []}
    man_p = os.path.join(ROOT, "MANIFEST.json")
    man = json.load(open(man_p)) if os.path.exists(man_p) else {}

    names = [n for n in ORDER if n in res] + \
            [n for n in sorted(res) if n not in ORDER]
    failed = [n for n in names if res[n]["status"] == "FAILED"]

    L = []
    A = L.append
    A("# riscpool build report")
    A("")
    A("Generated programmatically from `results/*.json`, "
      "`data/PROVENANCE.json` and `MANIFEST.json`. No number in this file "
      "was typed by hand.")
    A("")
    A(f"- generated: `{utcnow()}`")
    A(f"- git commit: `{man.get('git_commit', 'n/a')}`")
    A(f"- python: `{man.get('python_version_short', 'n/a')}`")
    A(f"- experiments recorded: **{len(names)}**, "
      f"failed: **{len(failed)}**")
    A("")

    A("## 1. Experiment status and wall clock")
    A("")
    A("| experiment | status | seed | wall clock (s) |")
    A("|---|---|---|---|")
    for n in names:
        r = res[n]
        A(f"| `{n}` | **{r['status']}** | {fmt(r.get('seed'))} | "
          f"{fmt(r.get('elapsed_s'))} |")
    tot = sum(r.get("elapsed_s", 0) or 0 for r in res.values())
    A(f"| **total** |  |  | **{tot:.2f}** |")
    A("")

    A("## 2. Failed experiments")
    A("")
    if not failed:
        A("None. Every experiment that was started produced a result.")
    else:
        for n in failed:
            A(f"### `{n}` — FAILED")
            A("")
            tb = res[n].get("traceback") or ""
            A("```")
            A(tb.strip()[-3000:])
            A("```")
            A("")
    A("")

    A("## 3. Results, per experiment")
    A("")
    for n in names:
        r = res[n]
        A(f"### `{n}`  ({r['status']})")
        A("")
        A(f"seed `{fmt(r.get('seed'))}`, wall clock "
          f"`{fmt(r.get('elapsed_s'))}` s, recorded "
          f"`{r.get('timestamp_utc')}`")
        A("")
        v = r.get("values") or {}
        t = scalar_table(v)
        if t:
            A(t)
            A("")
        for k, val in v.items():
            if isinstance(val, list) and val and isinstance(val[0], dict):
                A(listdict_table(k, val))
                A("")
            elif isinstance(val, dict):
                A(f"\n**`{k}`**\n")
                A("```json")
                A(json.dumps(val, indent=2)[:4000])
                A("```")
                A("")
            elif isinstance(val, list):
                A(f"\n**`{k}`**: `{json.dumps(val)[:1500]}`\n")
        A("")

    A("## 3b. Mean +/- sd, per experiment")
    A("")
    A("Every `mean_*` value in a result JSON, paired with its `sd_*` "
      "counterpart where one exists. Read from the JSONs, not typed.")
    A("")
    A("| experiment | quantity | mean | sd | n |")
    A("|---|---|---|---|---|")
    nrows = 0
    for n in names:
        v = res[n].get("values") or {}
        flat = {}

        def walk(o, pre=""):
            if isinstance(o, dict):
                for k, x in o.items():
                    walk(x, f"{pre}.{k}" if pre else k)
            elif isinstance(o, list):
                for i, x in enumerate(o):
                    walk(x, f"{pre}[{i}]")
            else:
                flat[pre] = o

        walk(v)
        for k, val in flat.items():
            base = None
            for tag in ("mean_of_", "mean_", "sim_mean_"):
                if k.rsplit(".", 1)[-1].startswith(tag):
                    base = (k, tag)
                    break
            if base is None or not isinstance(val, (int, float)):
                continue
            kk, tag = base
            sd_key = kk.replace(tag, tag.replace("mean", "sd"), 1)
            sd = flat.get(sd_key)
            cnt = None
            for cand in (kk.rsplit(".", 1)[0] + ".n_seeds",
                         kk.rsplit(".", 1)[0] + ".n_constructs",
                         kk.rsplit(".", 1)[0] + ".n_transcripts",
                         "n_constructs_scored", "n_splits"):
                if cand in flat and isinstance(flat[cand], (int, float)):
                    cnt = flat[cand]
                    break
            A(f"| `{n}` | `{kk}` | {fmt(val)} | "
              f"{fmt(sd) if sd is not None else '-'} | "
              f"{fmt(cnt) if cnt is not None else '-'} |")
            nrows += 1
    if nrows == 0:
        A("| - | no mean/sd pairs found | - | - | - |")
    A("")

    A("## 4. Data provenance")
    A("")
    recs = prov.get("records", [])
    ok = [r for r in recs if r.get("status") == "OK"]
    bad = [r for r in recs if r.get("status") != "OK"]
    A(f"{len(recs)} records: {len(ok)} OK, {len(bad)} FAILED.")
    A("")
    A("| dataset | status | path | bytes | sha256 (first 16) | url |")
    A("|---|---|---|---|---|---|")
    for r in recs:
        u = r.get("url") or ""
        if len(u) > 110:
            u = u[:107] + "..."
        sh = (r.get("sha256") or "")[:16]
        A(f"| {r.get('dataset')} | {r.get('status')} | "
          f"`{r.get('path')}` | {fmt(r.get('bytes'))} | `{sh}` | {u} |")
    A("")

    A("## 5. Manifest")
    A("")
    if man:
        keys = ["generated_utc", "git_commit", "git_branch",
                "python_version_short", "platform", "cpu_count",
                "n_experiments", "n_failed",
                "total_experiment_wall_clock_seconds"]
        A("| key | value |")
        A("|---|---|")
        for k in keys:
            A(f"| `{k}` | {fmt(man.get(k))} |")
        A("")
        A(f"`pip freeze` has {len(man.get('pip_freeze', []))} entries; "
          f"full list in `MANIFEST.json`.")
    else:
        A("`MANIFEST.json` not present.")
    A("")

    A("## 6. verify.py")
    A("")
    vp = os.path.join(RESULTS, "verify_status.json")
    if os.path.exists(vp):
        vs = json.load(open(vp))
        A("| key | value |")
        A("|---|---|")
        for k, val in vs.items():
            if isinstance(val, (int, float, str, bool)) or val is None:
                A(f"| `{k}` | {fmt(val)} |")
        A("")
        if vs.get("checks"):
            A(listdict_table("checks", vs["checks"]))
    else:
        A("`verify.py` has not been run, or wrote no status file.")
    A("")

    out = os.path.join(RESULTS, "SUMMARY.md")
    with open(out, "w") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"wrote {out}  ({len(L)} lines)")


if __name__ == "__main__":
    main()
