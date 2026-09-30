"""
K-head: features -> effective interaction score -> K -> equilibrium.

Deliberately small. The scientific question is whether the equilibrium
transformation of learned interactions changes therapeutic ranking, so the
neural component exists to support that experiment, not to compete on capacity.

The head predicts an EFFECTIVE INTERACTION SCORE. It is not a binding constant
and is never supervised as one. What we ask of it is rank fidelity.

Parameterisation note. The spec said K = softplus(s) + eps. We use K = exp(s)
with s clamped instead, because K spans decades: reaching K = 1e-3 through a
softplus requires driving s far negative where the gradient has already
vanished, whereas in log space the same target is an ordinary output value.
Same positivity guarantee, far better conditioned.
"""

import torch
import torch.nn as nn
from scipy.stats import spearmanr
from .equilibrium import risc_equilibrium, pairwise_occupancy

torch.manual_seed(0)
BAR = "=" * 72
D_FEAT = 12


class KHead(nn.Module):
    def __init__(self, d_in=D_FEAT, d_hid=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_in, d_hid), nn.SiLU(),
            nn.Linear(d_hid, d_hid), nn.SiLU(),
            nn.Linear(d_hid, 1),
        )

    def forward(self, z):                      # z: (B, N, D)
        s = self.net(z).squeeze(-1)            # (B, N)
        return torch.exp(s.clamp(-9.0, 9.0))


def make_world(B, N, rho, seed=0):
    """
    Synthetic ground truth. A subset of features drives log K*, the rest are
    distractors, standing in for the fact that most computed pair features do
    not carry interaction information.
    """
    g = torch.Generator().manual_seed(seed)
    z = torch.randn(B, N, D_FEAT, generator=g).double()
    w = torch.zeros(D_FEAT).double()
    w[:4] = torch.tensor([2.1, -1.4, 1.7, -0.9]).double()   # informative block
    logK = (z @ w) + 0.6 * torch.tanh(z[..., 4] * z[..., 5]) + 1.0
    Kstar = torch.exp(logK.clamp(-6, 6))
    Kstar[:, 0] *= 0.05                                     # index 0 = target

    x = (torch.rand(B, N, generator=g).double() * 30 + 1.0)
    M = (rho * x.sum(-1, keepdim=True))
    _, o = risc_equilibrium(Kstar, x, M)
    return z, Kstar, x, M, (o / x)                          # bound fraction


def train(z, x, M, r_obs, supervision, forward="equilibrium",
          steps=400, lr=3e-3, verbose=False):
    head = KHead().double()
    opt = torch.optim.Adam(head.parameters(), lr=lr)
    for i in range(steps):
        K = head(z)
        if forward == "equilibrium":
            _, o = risc_equilibrium(K, x, M)
        else:
            o = pairwise_occupancy(K, x, M)
        r = o / x
        if supervision == "target":
            loss = ((r[:, 0] - r_obs[:, 0]) ** 2).mean()
        else:
            loss = ((r - r_obs) ** 2).mean()
        opt.zero_grad()
        loss.backward()
        opt.step()
        if verbose and i % 100 == 0:
            print(f"    step {i:>4}  loss {loss.item():.3e}")
    return head


def recovery(head, z, Kstar):
    """Rank fidelity, split by target vs off-target pairs."""
    with torch.no_grad():
        K = head(z)
    a = spearmanr(K.flatten().numpy(), Kstar.flatten().numpy()).statistic
    b = spearmanr(K[:, 1:].flatten().numpy(),
                  Kstar[:, 1:].flatten().numpy()).statistic
    return a, b


def check_gradient_flow():
    print(BAR + "\n1. End-to-end gradient flow through the solver\n" + BAR)
    z, Kstar, x, M, r = make_world(8, 40, rho=0.05, seed=1)
    head = KHead().double()
    K = head(z)
    _, o = risc_equilibrium(K, x, M)
    ((o / x - r) ** 2).mean().backward()
    gs = [p.grad.abs().max().item() for p in head.parameters()]
    print(f"  layers receiving gradient    {sum(g > 0 for g in gs)}/{len(gs)}")
    print(f"  max |grad| across params     {max(gs):.3e}")
    print(f"  min |grad| across params     {min(gs):.3e}")
    print(f"  any nan                      {any(torch.isnan(p.grad).any() for p in head.parameters())}")
    assert min(gs) > 0


def identifiability():
    """
    The question the Huesken pivot rests on. Efficacy datasets observe target
    knockdown only. If off-target interaction structure is recoverable from
    that alone, training on Huesken is fine. If it is not, then no amount of
    efficacy data identifies the quantity the therapeutic objective depends on,
    and the paper has to say so.
    """
    print("\n" + BAR + "\n2. What target-only supervision can and cannot identify\n" + BAR)
    z, Kstar, x, M, r = make_world(300, 50, rho=0.02, seed=2)
    zt, Kt, xt, Mt, rt = make_world(80, 50, rho=0.02, seed=99)

    for sup, label in (("full", "full occupancy profile (RNA-seq like)"),
                       ("target", "target knockdown only (Huesken like)")):
        head = train(z, x, M, r, supervision=sup)
        a, b = recovery(head, zt, Kt)
        with torch.no_grad():
            K = head(zt)
            _, o = risc_equilibrium(K, xt, Mt)
            fit = spearmanr((o / xt)[:, 0].numpy(), rt[:, 0].numpy()).statistic
        print(f"\n  supervision: {label}")
        print(f"    held-out target knockdown, Spearman   {fit:>7.3f}")
        print(f"    rank recovery of K*, all pairs        {a:>7.3f}")
        print(f"    rank recovery of K*, off-target only  {b:>7.3f}")


def model_mismatch():
    """
    Data generated under competition. Train one head through the equilibrium
    forward model and one through independent occupancy, then ask which
    recovers the underlying interaction ranking.
    """
    print("\n" + BAR + "\n3. Recovery vs competition regime, correct and misspecified\n" + BAR)
    print(f"  {'rho':>8} {'equilibrium-trained':>21} {'pairwise-trained':>19}")
    for rho in [0.005, 0.05, 0.5, 5.0]:
        z, Ks, x, M, r = make_world(250, 40, rho=rho, seed=3)
        zt, Kt, xt, Mt, _ = make_world(60, 40, rho=rho, seed=77)
        he = train(z, x, M, r, "full", forward="equilibrium", steps=350)
        hp = train(z, x, M, r, "full", forward="pairwise", steps=350)
        _, be = recovery(he, zt, Kt)
        _, bp = recovery(hp, zt, Kt)
        print(f"  {rho:>8.3f} {be:>21.3f} {bp:>19.3f}")
    print("\n  gap between the columns is the cost of assuming independence")
    print("  when the generating process is resource limited")


if __name__ == "__main__":
    check_gradient_flow()
    identifiability()
    model_mismatch()
    print("\n" + BAR)
