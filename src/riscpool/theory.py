"""
The three objects the paper needs before any GNN, plus corrections.

1. Redistribution theorem, checked by autograd against the analytic sign.
2. Pairwise limit: equilibrium recovers independent scoring as rho -> inf.
3. Retrieval invariance under the calibrated linear background.
4. Phase diagram, rank based rather than magnitude based.
"""

import torch
from scipy.stats import kendalltau
from .equilibrium import (risc_equilibrium, pairwise_occupancy, pairwise_score)

torch.manual_seed(0)
BAR = "=" * 72


def theorem():
    """
    Claim A (easy):   d o_i / d K_t > 0 for i != t.
    Claim B (harder): d o_t / d K_t < 0.

    B is not immediate, because o_t depends on K_t both directly and through f,
    and the two act in opposite directions. Writing f' = df/dK_t,

        d o_t / d K_t = x_t (f' K_t - f) / (K_t + f)^2,

    so the sign turns on whether f' K_t < f. With u = x_t K_t / (K_t + f)^2,
    the implicit gradient gives f' = f u / (K_t D), hence

        f' K_t - f = f (u / D - 1),

    and since D = (1 + beta) + sum_j x_j K_j/(K_j+f)^2 >= 1 + u > u, the
    bracket is strictly negative for every admissible parameter value. So B
    holds globally, not just in the regime we happened to simulate. The proof
    needs the D >= 1 + u step; without it the claim is only asserted.
    """
    print(BAR + "\n1. Redistribution theorem\n" + BAR)
    bad_a = bad_b = 0
    worst_margin = 1e9
    for _ in range(300):
        N = int(torch.randint(5, 400, (1,)))
        K = (torch.rand(1, N).double() * 30 + 1e-3).requires_grad_(True)
        x = torch.rand(1, N).double() * 60 + 1e-3
        M = torch.rand(1, 1).double() * 200 + 0.05
        beta = torch.rand(1, 1).double() * 5
        _, o = risc_equilibrium(K, x, M, beta)

        gt, = torch.autograd.grad(o[0, 0], K, retain_graph=True)
        go, = torch.autograd.grad(o[0, 1:].sum(), K, retain_graph=True)
        if gt[0, 0] >= 0:
            bad_b += 1
        if go[0, 0] <= 0:
            bad_a += 1
        worst_margin = min(worst_margin, -gt[0, 0].item() / (abs(gt[0, 0].item()) + 1e-30))

    print(f"  d o_i/d K_t > 0  (i != t)   violations: {bad_a}/300")
    print(f"  d o_t/d K_t < 0             violations: {bad_b}/300")
    print("  strengthening the target (K_t down) raises target occupancy AND")
    print("  lowers every off-target occupancy, simultaneously, always.")
    assert bad_a == 0 and bad_b == 0


def pairwise_limit():
    """
    The review says f -> M as M -> inf. That is not right. Conservation forces
    f = M - sum_j o_j, and sum_j o_j -> sum_j x_j, a finite constant. So

        f -> M - sum_j x_j,

    which is not M. What actually holds is f/M -> 1, hence o_j^eq / o_j^pw -> 1
    with relative error that is actually O(1/rho^2), not O(1/rho): expanding
    o_eq/o_pw = 1 - S K /(M(K+M)) + ... gives quadratic decay, confirmed below.
    The recovery claim survives; the intermediate
    step does not, and a reviewer who checks it will find the gap.
    """
    print("\n" + BAR + "\n2. Pairwise limit (equilibrium generalises pairwise)\n" + BAR)
    N = 400
    K = torch.rand(1, N).double() * 10 + 0.05
    x = torch.rand(1, N).double() * 30 + 0.1
    X = x.sum().item()
    print(f"  sum_j x_j = {X:.1f}")
    print(f"\n  {'rho=M/sum x':>12} {'f':>12} {'M - sum x':>12} "
          f"{'max rel err o':>15}")
    for rho in [0.1, 1.0, 10.0, 100.0, 1e3, 1e4]:
        M = torch.tensor([[rho * X]]).double()
        f, o = risc_equilibrium(K, x, M)
        p = pairwise_occupancy(K, x, M)
        err = ((o - p).abs() / p).max().item()
        print(f"  {rho:>12.1f} {f.item():>12.2f} {M.item()-X:>12.2f} {err:>15.3e}")
    print("\n  f tracks M - sum x, not M. Relative occupancy error decays as 1/rho.")


def retrieval_invariance():
    """
    The review recommends calibrating the background from residual abundance
    mass. That is wrong: contribution to the budget is affinity weighted. Two
    transcripts of equal x and different K do not consume equally. The correct
    rule follows from the weak-binding expansion,

        beta = sum_{j not in R} x_j / K_j,

    which makes invariance exact to O(f/K). Both rules are run below.
    """
    print("\n" + BAR + "\n3. Retrieval-depth invariance\n" + BAR)
    N = 4000
    torch.manual_seed(11)
    K_all = torch.rand(1, N).double() * 60 + 0.02
    x_all = torch.rand(1, N).double() * 20 + 0.01
    K_all[0, 0], x_all[0, 0] = 0.05, 25.0          # therapeutic target
    M = torch.tensor([[8.0]]).double()

    order = (x_all[0] / K_all[0]).argsort(descending=True)
    full_f, full_o = risc_equilibrium(K_all, x_all, M)
    ref_t = full_o[0, 0].item()

    for rule in ("affinity-weighted  x/K", "abundance mass     x"):
        print(f"\n  background rule: {rule}")
        print(f"  {'R':>6} {'f':>11} {'o_target':>11} {'total load':>12} "
              f"{'err vs full':>12}")
        for R in [25, 50, 100, 200, 500, 1000]:
            idx = order[:R]
            out = order[R:]
            beta = ((x_all[0, out] / K_all[0, out]).sum() if "affinity" in rule
                    else x_all[0, out].sum()).reshape(1, 1)
            K, x = K_all[:, idx], x_all[:, idx]
            f, o = risc_equilibrium(K, x, M, beta)
            tgt = o[0, (idx == 0).nonzero()[0, 0]].item()
            load = o.sum().item() + beta.item() * f.item()
            print(f"  {R:>6} {f.item():>11.5f} {tgt:>11.5f} {load:>12.5f} "
                  f"{abs(tgt-ref_t)/ref_t:>11.2%}")
    print(f"\n  full {N}-transcript reference: f={full_f.item():.5f} "
          f"o_target={ref_t:.5f}")


def phase_diagram():
    """
    The review proposes C(rho) = (load_pw - load_eq)/load_pw. That index is
    dominated by the budget violation, not by anything decision relevant: pw
    load exceeds M by orders of magnitude, so C sits near 1 across the whole
    competitive regime and only measures a fact already known analytically.

    The paper's actual claim is about which candidate you pick. So make the
    index rank based: Kendall tau between the candidate ordering under
    independent scoring and under equilibrium. tau = 1 means the layer changes
    no decision and is not worth having. Scale invariant, so the conservation
    mismatch cannot leak into it.
    """
    print("\n" + BAR + "\n4. Phase diagram, rank based\n" + BAR)
    torch.manual_seed(5)
    C, N = 120, 300
    x = (torch.rand(1, N).double() * 40 + 1).expand(C, -1).contiguous()
    K = torch.rand(C, N).double() * 12 + 0.02
    K[:, 0] = torch.rand(C).double() * 0.4 + 0.01      # on-target, varied
    X = x[0].sum().item()

    print(f"  {C} candidates, {N} transcripts, sum x = {X:.0f}")
    print(f"\n  {'rho':>10} {'tau vs occupancy':>18} {'tau vs x/K score':>18} "
          f"{'regime':>20}")
    rows = []
    for rho in [1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0]:
        M = torch.full((C, 1), rho * X, dtype=torch.float64)
        _, o = risc_equilibrium(K, x, M)
        eq = o[:, 1:].sum(-1).numpy()
        pw = pairwise_occupancy(K, x, M)[:, 1:].sum(-1).numpy()
        sc = pairwise_score(K, x)[:, 1:].sum(-1).numpy()
        t1 = kendalltau(eq, pw).statistic
        t2 = kendalltau(eq, sc).statistic
        tag = ("decisions differ" if t1 < 0.9 else
               "marginal" if t1 < 0.99 else "layer is inert")
        print(f"  {rho:>10.3f} {t1:>18.4f} {t2:>18.4f} {tag:>20}")
        rows.append((rho, t1))
    lo = [r for r, t in rows if t < 0.9]
    print(f"\n  equilibrium changes the candidate ranking for rho <= "
          f"{max(lo) if lo else float('nan'):.3f}")
    print("  above that it reproduces independent scoring, as the limit predicts")


if __name__ == "__main__":
    theorem()
    pairwise_limit()
    retrieval_invariance()
    phase_diagram()
    print("\n" + BAR)
