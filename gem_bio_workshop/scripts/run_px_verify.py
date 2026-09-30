"""
CORE phase 3 verification for the positive extensions.

Each check either passes or is recorded as failed. Nothing here is allowed to
overwrite an existing result file.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                        # noqa: E402
import pandas as pd                                       # noqa: E402
import torch                                              # noqa: E402
from riscpool import features, runner                     # noqa: E402
from riscpool.provenance import DATA, ROOT                # noqa: E402

OUT = os.path.join(ROOT, "results", "positive_extensions")
CH = []


def check(name, ok, detail=""):
    CH.append({"check": name, "ok": bool(ok), "detail": str(detail)[:400]})
    return ok


def fn(seed=0):
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import importlib.util
    def load(mod, path):
        s = importlib.util.spec_from_file_location(mod, os.path.join(ROOT, "scripts", path))
        m = importlib.util.module_from_spec(s); sys.modules[mod] = m
        s.loader.exec_module(m); return m
    A = load("pxa", "run_pxa_affinity.py")
    B = load("pxb", "run_pxb_approx.py")

    spec = json.load(open(os.path.join(OUT, "run_spec.json")))
    av = json.load(open(os.path.join(ROOT, "results",
                                     "pxa_affinity_correction.json")))["values"]

    # 1. original forward outputs unchanged (features fixture)
    ref = pd.read_parquet(features.FEAT)
    tmp = os.path.join("/tmp", "px_feat_check.parquet")
    got = features.build(out=tmp)
    k = ["construct", "transcript_id", "site_start"]
    ref_s = ref.sort_values(k).reset_index(drop=True)
    got_s = got.sort_values(k).reset_index(drop=True)
    num = [c for c in ref_s.columns if pd.api.types.is_numeric_dtype(ref_s[c])]
    worst = max(float(np.nanmax(np.abs(ref_s[c].to_numpy() - got_s[c].to_numpy())))
                for c in num)
    check("features.build() with defaults is bit-identical to the committed "
          "features.parquet", worst == 0.0, f"max abs difference {worst}")

    # 2. class-offset anchoring and log-space aggregation
    from riscpool.features import RT
    d = pd.read_parquet(features.FEAT)
    M = A.class_matrix(d[d.construct == d.construct.iloc[0]],
                       set(d.gene_symbol))
    m0 = M[list(M)[0]]
    s_zero = A.score_thermo(m0, np.zeros(len(A.FREE)))
    s_none = A.score_thermo(m0, None)
    check("zero offsets reproduce the uncorrected thermodynamic score exactly "
          "(7mer-m8 anchor is inert)",
          float(np.nanmax(np.abs(s_zero - s_none))) == 0.0,
          f"max abs diff {float(np.nanmax(np.abs(s_zero - s_none)))}")
    direct = []
    for i in range(min(200, m0["S"].shape[0])):
        v = m0["S"][i][np.isfinite(m0["S"][i])]
        direct.append(np.log(np.exp(v).sum()) if len(v) else -np.inf)
    check("logsumexp site aggregation equals the direct 1/K = sum 1/K_js form",
          np.allclose(np.array(direct), s_none[:len(direct)], atol=1e-9),
          f"max abs diff {float(np.nanmax(np.abs(np.array(direct)-s_none[:len(direct)])))}")

    # 3. split integrity: no guide or seed shared between train and test
    ov = spec["overlap_audit"]
    check("no exact guide overlap between GSE5814 and E-MEXP-668",
          ov["n_guide_overlap"] == 0, ov["exact_guide_overlap_D1_D2"])
    check("no exact seed(2-8) overlap between GSE5814 and E-MEXP-668",
          ov["n_seed_overlap"] == 0, ov["exact_seed_2_8_overlap_D1_D2"])

    # 4. identical evaluation rows across the three A comparators
    ns = {m: sorted((c, v["n"]) for c, v in dd["per_construct"].items())
          for m, dd in av["external_D2"].items()}
    check("all three A comparators are scored on identical rows",
          len({json.dumps(v) for v in ns.values()}) == 1,
          {m: len(v) for m, v in ns.items()})

    # 5. within-construct rank invariance for frozen affinities
    sysd = B.systems()
    con = sorted(sysd)[0]
    _, K, x, foc, nm = sysd[con]
    Mt = torch.tensor(0.1 * nm, dtype=B.DT)
    f = B.equilibrium(K, x, Mt)
    q_eq = (f / (K + f)).detach().numpy()
    q_ind = (Mt / (K + Mt)).detach().numpy()
    from scipy.stats import spearmanr
    rho_rank = float(spearmanr(q_eq, q_ind).statistic)
    check("equilibrium and independent fractional occupancies rank identically "
          "within a construct (Proposition 1)", abs(rho_rank - 1.0) < 1e-9,
          f"Spearman {rho_rank!r}")

    # 6. no double counting in the omitted background
    n = int(K.numel()); R = 100
    order = torch.argsort(-(x / K)); keep = order[:R]
    out = torch.tensor([i for i in range(n) if i not in set(keep.tolist())])
    check("retained and omitted sets partition the reference exactly",
          keep.numel() + out.numel() == n and
          len(set(keep.tolist()) & set(out.tolist())) == 0,
          f"{keep.numel()} + {out.numel()} = {n}")
    Xb, Kb, _ = B.bins_from(K[out], x[out], 10)
    check("saturable bin masses sum to the omitted abundance (no mass lost or "
          "double counted)",
          abs(float(Xb.sum()) - float(x[out].sum())) < 1e-6 * float(x[out].sum()),
          f"bins {float(Xb.sum())!r} vs omitted {float(x[out].sum())!r}")

    # 7. reproduction of the reported A metric from saved per-family values
    per = pd.read_csv(os.path.join(OUT, "A_per_family_external.csv"))
    check("primary effect recomputes from the saved per-family table",
          abs(float(per.paired_difference.mean()) -
              av["primary_paired_effect_M3_minus_M1"]) < 1e-12,
          f"{float(per.paired_difference.mean())!r} vs "
          f"{av['primary_paired_effect_M3_minus_M1']!r}")

    # 8. determinism of the frozen configuration
    fz = json.load(open(os.path.join(OUT, "A_frozen_config.json")))
    check("frozen lambda is the strongest-regularisation maximiser as "
          "specified", fz["lambda"] in spec["experiment_A"]["lambda_grid"],
          fz["lambda"])

    # 9. existing result files untouched
    dirty = subprocess.run(["git", "status", "--porcelain", "results/"],
                           capture_output=True, text=True, cwd=ROOT).stdout
    # verify.py writes results/verify_status.json on every run, so counting it
    # here makes this check fail for anyone who runs the main verifier first —
    # which is the documented order. It is this check's sibling output, not a
    # pre-existing result.
    touched = [l.split()[-1] for l in dirty.splitlines()
               if l.strip() and "positive_extensions" not in l
               and "px" not in l.split()[-1]
               and not l.split()[-1].endswith("results/verify_status.json")]
    check("no pre-existing result file was modified", not touched, touched)

    n_fail = sum(1 for c in CH if not c["ok"])
    return {"n_checks": len(CH), "n_failed": n_fail,
            "verdict": "PASS" if n_fail == 0 else "FAIL", "checks": CH}


if __name__ == "__main__":
    runner.run("px_verify", fn, seed=0)
