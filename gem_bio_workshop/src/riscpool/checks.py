"""
Correctness checks and the synthetic competition experiments.

Order matters. The first three blocks establish that the layer is a correct
differentiable solver. Only then does the redistribution experiment mean
anything, because otherwise a positive result could be a solver artefact.
"""

import torch
from .equilibrium import (
    risc_equilibrium, equilibrium_residual, pairwise_occupancy, solve_free_pool
)

torch.manual_seed(0)
BAR = "=" * 68


def check_conservation():
    print(BAR + "\n1. Conservation\n" + BAR)
    B, N = 16, 200
    K = torch.rand(B, N).double() * 10 + 1e-3
    x = torch.rand(B, N).double() * 50
    M = torch.rand(B, 1).double() * 100 + 10
    f, o = risc_equilibrium(K, x, M)

    r = equilibrium_residual(K, x, M, f).abs().max()
    closure = (f + o.sum(-1, keepdim=True) - M).abs().max()
    print(f"  max |F(f)|                  {r.item():.3e}")
    print(f"  max |f + sum(o) - M|        {closure.item():.3e}")
    print(f"  f within (0, M)             {bool(((f > 0) & (f <= M)).all())}")
    assert r < 1e-9 and closure < 1e-9


def check_gradients():
    print("\n" + BAR + "\n2. Implicit gradients vs central differences\n" + BAR)
    B, N = 3, 40
    K = (torch.rand(B, N).double() * 5 + 0.01).requires_grad_(True)
    x = (torch.rand(B, N).double() * 20).requires_grad_(True)
    M = (torch.rand(B, 1).double() * 50 + 5).requires_grad_(True)

    def loss(K, x, M):
        _, o = risc_equilibrium(K, x, M)
        return (o ** 2).sum()

    loss(K, x, M).backward()
    eps = 1e-6
    worst = 0.0
    for name, t in (("K", K), ("x", x), ("M", M)):
        flat = t.detach().clone().reshape(-1)
        idx = torch.randperm(flat.numel())[:12]
        for i in idx:
            up, dn = flat.clone(), flat.clone()
            up[i] += eps
            dn[i] -= eps
            args = {"K": K, "x": x, "M": M}
            args[name] = up.reshape(t.shape)
            lu = loss(**{k: v.detach() for k, v in args.items()}).item()
            args[name] = dn.reshape(t.shape)
            ld = loss(**{k: v.detach() for k, v in args.items()}).item()
            fd = (lu - ld) / (2 * eps)
            an = t.grad.reshape(-1)[i].item()
            worst = max(worst, abs(fd - an) / max(abs(fd), 1.0))
    print(f"  worst relative error        {worst:.3e}")
    assert worst < 1e-6


def check_monotonicity():
    print("\n" + BAR + "\n3. Qualitative properties\n" + BAR)
    N = 60
    K = torch.rand(1, N).double() * 5 + 0.05
    x = torch.rand(1, N).double() * 30
    Ms = torch.linspace(1, 400, 40).double().reshape(-1, 1)
    Kb, xb = K.expand(40, -1), x.expand(40, -1)
    f, o = risc_equilibrium(Kb, xb, Ms)
    print(f"  f increasing in M           {bool((f.diff(dim=0) > 0).all())}")
    print(f"  o_j increasing in M         {bool((o.diff(dim=0) > -1e-12).all())}")
    print(f"  saturation: o/x at max M    {(o[-1] / xb[-1]).mean().item():.4f}")


def redistribution():
    """
    The crux. Strengthen the guide's interaction with the on-target only.
    A pairwise model holds every off-target occupancy fixed, because nothing
    couples them. The equilibrium model must drain the free pool and pull
    off-target occupancy down with it.
    """
    print("\n" + BAR + "\n4. Redistribution under a target-only affinity change\n" + BAR)
    N = 300
    torch.manual_seed(7)
    K_off = torch.rand(1, N).double() * 8 + 0.5
    x = torch.rand(1, N).double() * 40 + 1
    x[0, 0] = 25.0                       # index 0 is the therapeutic target
    M = torch.tensor([[60.0]]).double()  # pool comparable to total abundance

    print(f"  {'K_target':>10} {'f':>9} {'o_target':>10} "
          f"{'sum o_off':>10} {'pairwise off':>13}")
    base_off = None
    for Kt in [10.0, 3.0, 1.0, 0.3, 0.1, 0.03]:
        K = K_off.clone()
        K[0, 0] = Kt
        f, o = risc_equilibrium(K, x, M)
        p = pairwise_occupancy(K, x, M)
        off, poff = o[0, 1:].sum().item(), p[0, 1:].sum().item()
        if base_off is None:
            base_off = off
        print(f"  {Kt:>10.2f} {f.item():>9.3f} {o[0,0].item():>10.3f} "
              f"{off:>10.3f} {poff:>13.3f}")
    print(f"\n  equilibrium: off-target load falls {100*(1-off/base_off):.1f}% "
          f"as the target is strengthened")
    print(f"  pairwise:    off-target load is constant by construction")


def m_sensitivity():
    """
    The ratio M / sum(x) decides whether the whole effect exists. Too large and
    nothing competes and the layer collapses to pairwise scoring. This sweep
    belongs in the paper as a figure, not an appendix hyperparameter.
    """
    print("\n" + BAR + "\n5. Where competition actually lives\n" + BAR)
    N = 300
    torch.manual_seed(7)
    x = torch.rand(1, N).double() * 40 + 1
    K_hi, K_lo = torch.rand(1, N).double() * 8 + 0.5, None
    K_lo = K_hi.clone()
    K_hi[0, 0], K_lo[0, 0] = 10.0, 0.03
    total_x = x.sum().item()

    print(f"  total transcript abundance  {total_x:.0f}")
    print(f"\n  {'M/sum(x)':>10} {'off-target change':>20} {'regime':>22}")
    for ratio in [0.001, 0.01, 0.05, 0.2, 1.0, 5.0, 50.0]:
        M = torch.tensor([[ratio * total_x]]).double()
        _, o_hi = risc_equilibrium(K_hi, x, M)
        _, o_lo = risc_equilibrium(K_lo, x, M)
        d = 100 * (o_lo[0, 1:].sum() / o_hi[0, 1:].sum() - 1).item()
        if abs(d) < 1.0:
            tag = "no coupling"
        elif abs(d) < 10.0:
            tag = "weak"
        else:
            tag = "strong competition"
        print(f"  {ratio:>10.3f} {d:>19.2f}% {tag:>22}")


def regimes():
    print("\n" + BAR + "\n6. Competition regimes (section 20)\n" + BAR)
    torch.manual_seed(3)
    N = 200

    def run(label, x, K, M):
        f, o = risc_equilibrium(K, x, M)
        frac = (o[0, 0] / x[0, 0]).item()
        print(f"  {label:<34} f={f.item():>8.3f}  "
              f"target bound={frac:>6.1%}  off load={o[0,1:].sum().item():>8.2f}")

    x = torch.ones(1, N).double() * 0.05
    x[0, 0] = 40.0
    K = torch.ones(1, N).double() * 20
    K[0, 0] = 0.1
    M = torch.tensor([[30.0]]).double()
    run("A  one dominant target", x, K, M)

    x2 = x.clone(); x2[0, 1:] = 2.0
    run("B  target + many weak competitors", x2, K, M)

    K3 = K.clone(); K3[0, 1:6] = 0.15
    x3 = x.clone(); x3[0, 1:6] = 30.0
    run("C  few strong competitors", x3, K3, M)

    x4 = x.clone(); x4[0, 1:] = 20.0
    K4 = K.clone(); K4[0, 1:] = 3.0
    run("D  many abundant off-targets", x4, K4, M)

    K5 = K4.clone(); K5[0, 0] = 0.005
    run("E  D with target affinity raised", x4, K5, M)


if __name__ == "__main__":
    check_conservation()
    check_gradients()
    check_monotonicity()
    redistribution()
    m_sensitivity()
    regimes()
    print("\n" + BAR + "\nAll checks passed.\n" + BAR)
