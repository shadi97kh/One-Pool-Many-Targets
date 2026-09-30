"""
e5 and e7: the two experiments that run on measured human data.

Nothing in here fits K to the expression response. K comes from ViennaRNA
thermodynamics on real sequences (features.py), x comes from the mock channel
of the same arrays (hela.py), and M comes from published Argonaute copy number
(constants.py). The only free quantity is alpha, the fraction of the Argonaute
pool loaded with the transfected guide, which is not measured and is therefore
swept rather than chosen.
"""

import numpy as np
import pandas as pd
import torch
from scipy.stats import kendalltau, spearmanr

from . import kmers
from .equilibrium import pairwise_occupancy, risc_equilibrium
from .features import RT, transcript_level
from .hela import load_abundance

BIG_K = 1e12          # transcripts with no seed site: effectively no binding


def on_target_site(parent_guide_dna):
    """The perfectly complementary site is the reverse complement of the
    parent guide. Derived, never typed in."""
    return kmers.revcomp(parent_guide_dna)


def on_target_affinity(pc, parent_construct="MAPK14-193_parent"):
    """Duplex free energy of each guide against the parent on-target site.
    The mutants differ from the parent by one base, so this really is the
    spread of on-target affinity across the candidate set."""
    import RNA
    parent = pc.loc[pc.construct == parent_construct,
                    "guide_5to3_dna"].iloc[0]
    site = on_target_site(parent).replace("T", "U")
    rows = []
    for _, s in pc.iterrows():
        d = RNA.duplexfold(s.guide_5to3_dna.replace("T", "U"), site)
        dg = float(d.energy)
        rows.append({"construct": s.construct, "dg_on_target_kcal": dg,
                     "K_on_target": float(np.exp(dg / RT))})
    out = pd.DataFrame(rows)
    out["log10_K_on"] = np.log10(out.K_on_target)
    return out, site


def assemble(constructs, target_gene="MAPK14"):
    """
    Build the (C x N) affinity matrix and the N-vector of abundances over the
    union of every construct's retrieved off-target set, plus the on-target
    column. Returns numpy arrays and bookkeeping.
    """
    tx = transcript_level()
    tx = tx[tx.construct.isin(constructs)]
    ab = load_abundance()[["gene_symbol", "transcript_id", "x_rel"]]

    off = tx[tx.gene_symbol != target_gene]
    union = sorted(off.transcript_id.unique())
    pos = {t: i for i, t in enumerate(union)}
    N = len(union)
    C = len(constructs)
    K = np.full((C, N), BIG_K, dtype=np.float64)
    for ci, c in enumerate(constructs):
        d = off[off.construct == c]
        idx = np.array([pos[t] for t in d.transcript_id])
        kk = d.K_transcript.to_numpy()
        good = np.isfinite(kk) & (kk > 0)
        K[ci, idx[good]] = kk[good]
    xmap = ab.set_index("transcript_id").x_rel
    x = xmap.reindex(union).fillna(0.0).to_numpy()
    return {"constructs": list(constructs), "transcripts": union,
            "K_off": K, "x_off": x, "n_transcripts": N,
            "n_sites_per_construct": off.groupby("construct").size().to_dict()}


def _tau_at(K_off, x_off, K_on, x_on, rho, total_x):
    """Kendall tau between candidate ranking by off-target load under
    equilibrium and under independent pairwise occupancy."""
    C, N = K_off.shape
    K = np.concatenate([K_on.reshape(C, 1), K_off], axis=1)
    x = np.concatenate([[x_on], x_off])
    Kt = torch.tensor(K, dtype=torch.float64)
    xt = torch.tensor(x, dtype=torch.float64).expand(C, -1).contiguous()
    M = torch.full((C, 1), float(rho * total_x), dtype=torch.float64)
    _, o = risc_equilibrium(Kt, xt, M)
    p = pairwise_occupancy(Kt, xt, M)
    eq = o[:, 1:].sum(-1).numpy()
    pw = p[:, 1:].sum(-1).numpy()
    return float(kendalltau(eq, pw).statistic), eq, pw


def phase_grid(K_off, x_off, log10K_on, x_on, total_x, rhos, hks):
    """tau(rho, H_K). H_K rescales the spread of on-target affinity about its
    own mean, so H_K equal to the measured spread reproduces the real data."""
    mu = log10K_on.mean()
    dev = log10K_on - mu
    sd0 = dev.std(ddof=1)
    grid = np.zeros((len(hks), len(rhos)))
    for i, h in enumerate(hks):
        s = h / sd0 if sd0 > 0 else 0.0
        Kon = 10.0 ** (mu + dev * s)
        for j, r in enumerate(rhos):
            grid[i, j] = _tau_at(K_off, x_off, Kon, x_on, r, total_x)[0]
    return grid


def contour_rho_at_tau(rhos, taus, level=0.9):
    """Largest rho at which tau crosses below `level`, by linear interpolation
    in log rho. NaN if the row never crosses."""
    t = np.asarray(taus, dtype=float)
    lr = np.log10(np.asarray(rhos, dtype=float))
    below = t < level
    if not below.any() or below.all():
        return float("nan")
    idx = np.where(below)[0].max()
    if idx + 1 >= len(t):
        return float("nan")
    t0, t1 = t[idx], t[idx + 1]
    if t1 == t0:
        return float(10 ** lr[idx])
    w = (level - t0) / (t1 - t0)
    return float(10 ** (lr[idx] + w * (lr[idx + 1] - lr[idx])))


# ----------------------------------------------------------------- e7 -----

def score_construct(construct, rho, total_x, target_gene="MAPK14",
                    tx=None, ab=None):
    """
    Occupancies for one construct's retrieved off-target set at a given rho.
    Returns a DataFrame with both scorings joined to the measured log ratio.
    """
    if tx is None:
        tx = transcript_level()
    d = tx[(tx.construct == construct) & (tx.gene_symbol != target_gene)].copy()
    d = d[np.isfinite(d.K_transcript) & (d.K_transcript > 0)]
    if len(d) < 20:
        return None
    K = torch.tensor(d.K_transcript.to_numpy(), dtype=torch.float64)[None, :]
    x = torch.tensor(d.x_rel.to_numpy(), dtype=torch.float64)[None, :]
    M = torch.tensor([[float(rho * total_x)]], dtype=torch.float64)
    f, o = risc_equilibrium(K, x, M)
    p = pairwise_occupancy(K, x, M)
    d["o_equilibrium"] = o[0].numpy()
    d["o_independent"] = p[0].numpy()
    d["bound_frac_equilibrium"] = (o[0] / x[0]).numpy()
    d["bound_frac_independent"] = (p[0] / x[0]).numpy()
    d["f_free_pool"] = float(f.item())
    return d


def evaluate(d, measured, n_boot=0, rng=None):
    """
    Rank agreement between predicted occupancy and measured repression.
    Measured log ratio is negative when repressed, so a correct predictor has
    NEGATIVE correlation with bound fraction. Sign is reported as measured.
    """
    m = d.merge(measured, on="gene_symbol", how="inner")
    m = m[np.isfinite(m.value)]
    if len(m) < 20:
        return None
    out = {"n_transcripts": int(len(m))}
    for tag, col in (("equilibrium", "bound_frac_equilibrium"),
                     ("independent", "bound_frac_independent")):
        s = spearmanr(m[col], m.value)
        k = kendalltau(m[col], m.value)
        out[f"spearman_{tag}"] = float(s.statistic)
        out[f"spearman_p_{tag}"] = float(s.pvalue)
        out[f"kendall_{tag}"] = float(k.statistic)
    out["spearman_difference_eq_minus_ind"] = (out["spearman_equilibrium"]
                                               - out["spearman_independent"])
    out["kendall_between_the_two_scorings"] = float(
        kendalltau(m.bound_frac_equilibrium,
                   m.bound_frac_independent).statistic)
    out["pairwise_ranking_accuracy_equilibrium"] = _pra(
        m.bound_frac_equilibrium.to_numpy(), m.value.to_numpy())
    out["pairwise_ranking_accuracy_independent"] = _pra(
        m.bound_frac_independent.to_numpy(), m.value.to_numpy())
    if n_boot:
        rng = rng or np.random.default_rng(0)
        de, di = [], []
        v = m.value.to_numpy()
        a = m.bound_frac_equilibrium.to_numpy()
        b = m.bound_frac_independent.to_numpy()
        for _ in range(n_boot):
            ix = rng.integers(0, len(m), len(m))
            de.append(spearmanr(a[ix], v[ix]).statistic)
            di.append(spearmanr(b[ix], v[ix]).statistic)
        de, di = np.array(de), np.array(di)
        out["spearman_equilibrium_ci95"] = [float(np.nanpercentile(de, 2.5)),
                                            float(np.nanpercentile(de, 97.5))]
        out["spearman_independent_ci95"] = [float(np.nanpercentile(di, 2.5)),
                                            float(np.nanpercentile(di, 97.5))]
        out["bootstrap_n"] = int(n_boot)
    return out, m


def _pra(pred, obs, n_pairs=200000, seed=0):
    """Fraction of transcript pairs ordered consistently: higher predicted
    bound fraction should go with more negative measured log ratio."""
    rng = np.random.default_rng(seed)
    n = len(pred)
    i = rng.integers(0, n, n_pairs)
    j = rng.integers(0, n, n_pairs)
    ok = (pred[i] != pred[j]) & (obs[i] != obs[j])
    i, j = i[ok], j[ok]
    if len(i) == 0:
        return float("nan")
    agree = ((pred[i] > pred[j]) & (obs[i] < obs[j])) | \
            ((pred[i] < pred[j]) & (obs[i] > obs[j]))
    return float(agree.mean())


def fit_monotone_map(occ, obs, n_bins=25):
    """
    r = phi(o), fitted rather than assumed. Isotonic regression of measured
    log ratio on predicted bound fraction (decreasing), reported as a binned
    table so the paper can plot it without rerunning anything.
    """
    from sklearn.isotonic import IsotonicRegression
    o = np.asarray(occ, dtype=float)
    y = np.asarray(obs, dtype=float)
    good = np.isfinite(o) & np.isfinite(y)
    o, y = o[good], y[good]
    ir = IsotonicRegression(increasing=False, out_of_bounds="clip")
    yhat = ir.fit_transform(o, y)
    qs = np.quantile(o, np.linspace(0, 1, n_bins + 1))
    qs = np.unique(qs)
    b = np.clip(np.digitize(o, qs[1:-1]), 0, len(qs) - 2)
    tab = []
    for k in range(len(qs) - 1):
        m = b == k
        if m.sum() < 5:
            continue
        tab.append({"bin": k, "n": int(m.sum()),
                    "occupancy_mid": float(np.median(o[m])),
                    "phi_fitted_log10ratio": float(np.median(yhat[m])),
                    "observed_median_log10ratio": float(np.median(y[m]))})
    resid = y - yhat
    return {"table": tab,
            "spearman_fit_vs_observed": float(
                spearmanr(yhat, y).statistic),
            "residual_sd": float(np.std(resid)),
            "r2_isotonic": float(1 - np.var(resid) / np.var(y))}
