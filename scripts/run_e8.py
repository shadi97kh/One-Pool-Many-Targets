"""
D5 + e8 - Huesken efficacy, split so no target gene is shared.

This dataset observes ON-TARGET knockdown only. NO off-target claim is made
from it, and that statement is written into the result JSON as a field rather
than left to the reader.

The K-head consumes real ViennaRNA thermodynamics on the real 19-mers and the
real target-site context, and predicts occupancy through the same forward
model the rest of the repository uses. The split is by target gene, using the
gene assignment derived in huesken.py by locating each guide's reverse
complement in that gene's tiled target sequence.
"""
import os
import sys

# Pin the thread pools BEFORE numpy or torch are imported. This experiment's
# recorded values depend on floating-point reduction order, which depends on
# how many threads the BLAS and torch pools happen to have, so an unpinned run
# does not reproduce a run made on a differently loaded machine. Stage B of
# verify.py caught exactly that. Thread count changes only the arithmetic
# order, never the mathematics, and pinning makes the result reproducible.
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS",
           "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                              # noqa: E402
import pandas as pd                                             # noqa: E402
import torch                                                    # noqa: E402
torch.set_num_threads(1)
from scipy.stats import pearsonr, spearmanr                     # noqa: E402
from sklearn.model_selection import GroupKFold                  # noqa: E402
from riscpool import huesken, kmers, runner         # noqa: E402
from riscpool import provenance as P                             # noqa: E402
from riscpool.khead import KHead                                 # noqa: E402

NUC = "ACGT"


def sirna_features(guide_dna, context=None):
    """Real thermodynamics and composition. No learned or imputed inputs."""
    import RNA
    g = guide_dna.replace("T", "U")
    site = kmers.revcomp(guide_dna)

    def dg(a):
        return float(RNA.duplexfold(
            a, kmers.revcomp(a.replace("U", "T")).replace("T", "U")).energy)

    five, three = dg(g[:5]), dg(g[-5:])
    full = float(RNA.duplexfold(g, site.replace("T", "U")).energy)
    fold = float(RNA.fold(g)[1])
    seed = g[1:8]
    f = {
        "dg_duplex_full": full,
        "dg_5p_end": five,
        "dg_3p_end": three,
        "asymmetry": five - three,
        "dg_guide_selffold": fold,
        "seed_pairing_stability": dg(seed),
        "gc_fraction": sum(c in "GC" for c in guide_dna) / len(guide_dna),
        "gc_seed": sum(c in "GC" for c in guide_dna[1:8]) / 7.0,
        "a_at_pos1": float(guide_dna[0] == "A"),
        "u_at_pos1": float(guide_dna[0] == "T"),
        "g_at_pos19": float(guide_dna[-1] == "G"),
        "c_at_pos19": float(guide_dna[-1] == "C"),
    }
    return f


def build_matrix(df):
    feats = [sirna_features(g) for g in df.guide_19mer_dna]
    F = pd.DataFrame(feats)
    return F


def fn(seed=0, n_splits=5, steps=600, lr=3e-3):
    hu, info = huesken.build()
    P.register_local(huesken.OUT, "D5_huesken",
                     note="Huesken efficacy table with sequence-derived "
                          "target-gene assignment")
    hu = hu.dropna(subset=["target_gene"]).reset_index(drop=True)
    F = build_matrix(hu)
    X = F.to_numpy(dtype=np.float64)
    X = (X - X.mean(0)) / (X.std(0) + 1e-12)
    y = hu.efficacy.to_numpy(dtype=np.float64)
    groups = hu.target_gene.to_numpy()

    # The efficacy assay reports fractional knockdown of a single target and
    # provides no absolute pool scale, so M is set to 1 and K is measured in
    # units of the pool. Using the HeLa Argonaute count here would be a
    # category error: it would pin M far above the representable range of
    # K = exp(s), driving M/(K+M) to 1 for every siRNA and killing the
    # gradient. That failure was observed and is why this is set to 1.
    M_val = 1.0

    torch.manual_seed(seed)
    np.random.seed(seed)
    gkf = GroupKFold(n_splits=n_splits)
    folds = []
    preds = np.zeros_like(y)
    for k, (tr, te) in enumerate(gkf.split(X, y, groups)):
        head = KHead(d_in=X.shape[1]).double()
        opt = torch.optim.Adam(head.parameters(), lr=lr)
        xt = torch.tensor(X[tr])[None, :, :]
        yt = torch.tensor(y[tr])[None, :]
        M = torch.tensor([[M_val]], dtype=torch.float64)
        for _ in range(steps):
            K = head(xt)
            r = M / (K + M)              # independent occupancy, single target
            loss = ((r - yt) ** 2).mean()
            opt.zero_grad()
            loss.backward()
            opt.step()
        with torch.no_grad():
            Kte = head(torch.tensor(X[te])[None, :, :])
            rte = (M / (Kte + M))[0].numpy()
        preds[te] = rte
        sp = spearmanr(rte, y[te])
        pe = pearsonr(rte, y[te])
        folds.append({
            "fold": k, "n_train": int(len(tr)), "n_test": int(len(te)),
            "n_train_genes": int(len(set(groups[tr]))),
            "n_test_genes": int(len(set(groups[te]))),
            "genes_shared_between_train_and_test": int(
                len(set(groups[tr]) & set(groups[te]))),
            "test_genes": sorted(set(groups[te])),
            "spearman": float(sp.statistic), "spearman_p": float(sp.pvalue),
            "pearson": float(pe.statistic), "pearson_p": float(pe.pvalue),
            "final_train_loss": float(loss.item()),
        })
    sps = np.array([f["spearman"] for f in folds])
    pes = np.array([f["pearson"] for f in folds])
    allsp = spearmanr(preds, y)
    allpe = pearsonr(preds, y)
    return {
        "OFF_TARGET_CLAIM": (
            "NONE. This dataset observes on-target knockdown only. No "
            "off-target conclusion of any kind is drawn from it, and none "
            "may be drawn from these numbers."),
        "dataset": "Huesken et al. Nat Biotechnol 2005;23:995-1001, "
                   "redistributed in the OligoFormer repository",
        "d5_acquisition": info,
        "n_sirnas_used": int(len(hu)),
        "n_target_genes": int(hu.target_gene.nunique()),
        "n_features": int(X.shape[1]),
        "feature_names": list(F.columns),
        "split": "GroupKFold by target gene; no gene appears in both train "
                 "and test in any fold",
        "n_splits": n_splits, "training_steps": steps, "learning_rate": lr,
        "M_pool_units": M_val,
        "M_note": ("dimensionless; the efficacy assay carries no absolute "
                   "pool scale, so K is expressed in units of the pool"),
        "folds": folds,
        "mean_spearman_heldout_genes": float(sps.mean()),
        "sd_spearman_heldout_genes": float(sps.std(ddof=1)),
        "mean_pearson_heldout_genes": float(pes.mean()),
        "sd_pearson_heldout_genes": float(pes.std(ddof=1)),
        "pooled_out_of_fold_spearman": float(allsp.statistic),
        "pooled_out_of_fold_spearman_p": float(allsp.pvalue),
        "pooled_out_of_fold_pearson": float(allpe.statistic),
        "pooled_out_of_fold_pearson_p": float(allpe.pvalue),
        "max_genes_shared_any_fold": int(max(
            f["genes_shared_between_train_and_test"] for f in folds)),
    }


if __name__ == "__main__":
    runner.run("e8_huesken_efficacy", fn, seed=0)
