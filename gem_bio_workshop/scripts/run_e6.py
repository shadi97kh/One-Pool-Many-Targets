"""
e6 - SIMULATION. Interaction recovery under known ground truth.

Every artifact of this experiment is prefixed sim_. Ground-truth K* does not
exist in nature, so this is methods validation, not observation, and nothing
here is evidence about HeLa, about siRNA off-targeting, or about any measured
quantity. It answers one question only: if the generating process really were
resource limited, would training through the equilibrium forward model recover
the interaction ranking better than training through independent occupancy?

K* -> equilibrium -> bound fractions -> train two heads -> Spearman recovery
of K* on held-out draws, off-target pairs only, swept over rho, five seeds.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
import torch                                                    # noqa: E402
from riscpool import runner                                      # noqa: E402
from riscpool.khead import make_world, recovery, train           # noqa: E402

RHOS = [0.005, 0.05, 0.5, 5.0]
SEEDS = [0, 1, 2, 3, 4]
STEPS = 350


def fn(seed=0):
    rows = []
    for rho in RHOS:
        for s in SEEDS:
            torch.manual_seed(seed * 1000 + s)
            z, Ks, x, M, r = make_world(250, 40, rho=rho, seed=100 + s)
            zt, Kt, xt, Mt, _ = make_world(60, 40, rho=rho, seed=900 + s)
            he = train(z, x, M, r, "full", forward="equilibrium", steps=STEPS)
            hp = train(z, x, M, r, "full", forward="pairwise", steps=STEPS)
            ae, be = recovery(he, zt, Kt)
            ap, bp = recovery(hp, zt, Kt)
            rows.append({
                "rho": rho, "seed": s,
                "sim_spearman_offtarget_equilibrium_trained": float(be),
                "sim_spearman_offtarget_pairwise_trained": float(bp),
                "sim_spearman_allpairs_equilibrium_trained": float(ae),
                "sim_spearman_allpairs_pairwise_trained": float(ap),
                "sim_gap_equilibrium_minus_pairwise": float(be - bp),
            })
            print(f"  rho={rho:<7g} seed={s}  eq={be:.4f}  pw={bp:.4f}",
                  flush=True)
    summary = []
    for rho in RHOS:
        g = [r for r in rows if r["rho"] == rho]
        e = np.array([r["sim_spearman_offtarget_equilibrium_trained"]
                      for r in g])
        p = np.array([r["sim_spearman_offtarget_pairwise_trained"] for r in g])
        summary.append({
            "rho": rho, "n_seeds": len(g),
            "sim_mean_spearman_equilibrium_trained": float(e.mean()),
            "sim_sd_spearman_equilibrium_trained": float(e.std(ddof=1)),
            "sim_mean_spearman_pairwise_trained": float(p.mean()),
            "sim_sd_spearman_pairwise_trained": float(p.std(ddof=1)),
            "sim_mean_gap": float((e - p).mean()),
            "sim_sd_gap": float((e - p).std(ddof=1)),
            "sim_gap_positive_in_all_seeds": bool((e - p > 0).all()),
        })
    return {
        "SIMULATION_ONLY": (
            "Ground-truth K* is generated, not measured. Nothing in this "
            "experiment is evidence about any real cell, transcript or "
            "siRNA. It validates the training method under a known "
            "generating process and nothing else."),
        "sim_n_rho": len(RHOS), "sim_rho_values": RHOS,
        "sim_seeds": SEEDS, "sim_training_steps": STEPS,
        "sim_batch_train": 250, "sim_batch_test": 60,
        "sim_n_transcripts": 40,
        "sim_per_run": rows,
        "sim_summary_by_rho": summary,
        "sim_pilot_for_comparison": {
            "rho_0.005": {"equilibrium": 0.954, "pairwise": 0.547},
            "rho_5.0": {"equilibrium": 0.990, "pairwise": 0.976},
            "note": "pilot figures quoted from the build brief for "
                    "comparison; the measured values above supersede them"},
    }


if __name__ == "__main__":
    runner.run("e6_sim_interaction_recovery", fn, seed=0)
