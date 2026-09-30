"""
Per-construct seed recovery from measured response, with an internal test.

The GSE5814 submitters deposited no siRNA sequences and the publisher releases
no machine-readable full text, so the seeds are MEASURED rather than assumed.

Procedure, and the reason each step is not circular:

 1. The model defines the seed as guide positions 2-8. That is a definition,
    not a fact fitted to this data.
 2. Parent site. Contrast the parent construct's response against the mean
    response of the constructs whose mutation falls inside 2-8. Shared effects
    (on-target MAPK14 knockdown, downstream p38 signalling, transfection
    stress, array AU bias) cancel; what survives is specific to the parent
    seed. The argmin 7-mer over all 16384 is the parent site.
 3. Mutant sites. For a construct mutated at guide position p in 2..8, the
    7mer-m8 site is the reverse complement of guide 2..8, so site index 8-p is
    the one that must change and no other. Testing only the three single-base
    variants at that index is a sharp, falsifiable prediction: it can fail.
 4. The seed-preserving constructs (p = 1 and p = 9..19) must retain the parent
    site. They are not used to define it, so this is a held-out check.

Everything reported here is a statistic computed on measured log ratios.
"""

import os

import numpy as np
import pandas as pd

from . import kmers
from .offtarget import load_candidates, load_response
from .provenance import DATA

OUT = os.path.join(DATA, "recovered_seeds.parquet")
K = 7
BACKBONE = "MAPK14-193"
SEED_POSITIONS = list(range(2, 9))          # model definition of the seed


def construct_list():
    return [f"{BACKBONE}_parent"] + [f"{BACKBONE}_pos{n:02d}mut"
                                     for n in range(1, 20)]


def _wide(resp, syms, arrays=None):
    d = resp if arrays is None else resp[resp.geo_accession.isin(arrays)]
    return (d.groupby(["gene_symbol", "construct"])["value"].median()
             .unstack().reindex(syms))


def _scan(G, y, min_n=15):
    m = np.isfinite(y)
    d, t, n1 = kmers.enrichment_scan(G[np.where(m)[0]], y[m], min_n=min_n)
    return d, t, n1, int(m.sum())


def recover(arrays=None, min_n=15):
    cand = load_candidates()
    resp = load_response()
    syms = cand.gene_symbol.tolist()
    G = kmers.incidence(cand.utr3_seq.tolist(), k=K)
    w = _wide(resp, syms, arrays=arrays)

    cons = [c for c in construct_list() if c in w.columns]
    altered = [f"{BACKBONE}_pos{n:02d}mut" for n in SEED_POSITIONS
               if f"{BACKBONE}_pos{n:02d}mut" in w.columns]
    preserved = [c for c in cons if c not in altered]

    # ---- step 2: parent site -------------------------------------------
    ref_alt = w[altered].mean(axis=1).to_numpy()
    y = w[f"{BACKBONE}_parent"].to_numpy() - ref_alt
    d, t, n1, ngenes = _scan(G, y, min_n)
    order = np.argsort(np.where(np.isnan(t), np.inf, t))
    parent_site = kmers.index_to_kmer(int(order[0]), K)
    parent_t = float(t[order[0]])
    parent_top10 = [kmers.index_to_kmer(int(i), K) for i in order[:10]]

    # ---- step 4: held-out retention in seed-preserving constructs -------
    ip = kmers.kmer_index(parent_site)
    ref_pres = w[preserved].mean(axis=1).to_numpy()
    rows = []
    for con in cons:
        p = 0 if con.endswith("parent") else int(con[-5:-3])
        in_seed = p in SEED_POSITIONS
        ref = ref_alt if not in_seed else ref_pres
        yy = w[con].to_numpy() - ref
        dd, tt, nn, ng = _scan(G, yy, min_n)
        ordr = np.argsort(np.where(np.isnan(tt), np.inf, tt))
        rank_parent = int(np.where(ordr == ip)[0][0])
        rec = {"construct": con, "mut_position": p,
               "in_seed_by_definition": in_seed,
               "n_genes": ng,
               "t_parent_site": float(tt[ip]),
               "delta_parent_site": float(dd[ip]),
               "rank_parent_site": rank_parent,
               "global_top_kmer": kmers.index_to_kmer(int(ordr[0]), K),
               "global_top_t": float(tt[ordr[0]])}

        # ---- step 3: sharp test at the predicted index ------------------
        if in_seed:
            si = 8 - p
            best_k, best_t = None, np.inf
            var = {}
            for b in "ACGT":
                if b == parent_site[si]:
                    continue
                km = parent_site[:si] + b + parent_site[si + 1:]
                j = kmers.kmer_index(km)
                var[km] = float(tt[j])
                if tt[j] < best_t:
                    best_k, best_t = km, float(tt[j])
            # is the winner among the predicted-index variants also the best
            # single-base variant anywhere in the 7-mer?
            all_var = {}
            for q in range(K):
                for b in "ACGT":
                    if b == parent_site[q]:
                        continue
                    km = parent_site[:q] + b + parent_site[q + 1:]
                    all_var[km] = float(tt[kmers.kmer_index(km)])
            gk = min(all_var, key=all_var.get)
            rec.update({
                "predicted_variable_site_index": si,
                "recovered_site": best_k,
                "recovered_site_t": best_t,
                "variants_at_predicted_index": var,
                "best_single_base_variant_anywhere": gk,
                "best_single_base_variant_t": all_var[gk],
                "prediction_confirmed": bool(gk == best_k),
            })
        else:
            rec.update({"predicted_variable_site_index": None,
                        "recovered_site": parent_site,
                        "recovered_site_t": float(tt[ip]),
                        "variants_at_predicted_index": None,
                        "best_single_base_variant_anywhere": None,
                        "best_single_base_variant_t": None,
                        "prediction_confirmed": None})
        rows.append(rec)

    df = pd.DataFrame(rows)
    df["seed_guide_2_8"] = df.recovered_site.map(kmers.revcomp)
    df["parent_site"] = parent_site
    df["site_kmer"] = df.recovered_site
    return df, {"parent_site": parent_site, "parent_site_t": parent_t,
                "parent_top10": parent_top10, "n_genes": ngenes,
                "n_altered": len(altered), "n_preserved": len(preserved)}


def build(out=OUT):
    df, meta = recover()
    df.to_parquet(out, index=False, compression="zstd")
    return df, meta


def load_seeds():
    return pd.read_parquet(OUT)
