"""
Sequence and thermodynamic features on the real transcriptome.

Everything here is computed from actual sequence: the guide strands from the
Garcia 2011 supplementary table, the 3'UTR and CDS from GENCODE v50, the
thermodynamics from ViennaRNA. No feature is imputed.

Site conventions. With the guide written 5'-g1 g2 ... g19-3', the target site
in the mRNA reads 5'-[t8][t7..t2][t1]-3', so

    6mer      = revcomp(g2..g7)                     core
    7mer-m8   = revcomp(g2..g8)                     core + t8 pairing g8
    7mer-A1   = revcomp(g2..g7) followed by A       core + t1 = A
    8mer      = revcomp(g2..g8) followed by A       both

Affinity. K is not fitted to the expression response anywhere in the real-data
experiments; it comes from thermodynamics alone, so that any difference
between equilibrium and independent scoring is attributable to the coupling
layer and not to a fitted nuisance. Per site,

    dG_eff = dG_duplex - RT * ln(P_unpaired)   [= dG_duplex + dG_open]

which is the duplex energy PLUS the free-energy cost of opening the site,
since binding has to pay that cost, and K_site = exp(dG_eff / RT) up to an
arbitrary common scale. The sign matters: subtracting the opening cost makes
an inaccessible site score as the strongest binder. Sites on one
transcript combine as parallel binding opportunities, 1/K_tx = sum_s 1/K_site.
"""

import os

import numpy as np
import pandas as pd

from . import kmers
from .provenance import DATA

RT = 0.0019872 * 310.15          # kcal/mol at 37 C
FEAT = os.path.join(DATA, "features.parquet")
FLANK = 12                       # nt either side of the site for duplexfold
AU_WIN = 30


def _comp(b):
    return {"A": "T", "C": "G", "G": "C", "T": "A"}.get(b, "N")


def site_strings(guide):
    """(6mer core, t8 base, 8mer) for a DNA guide string."""
    core = kmers.revcomp(guide[1:7])
    t8 = _comp(guide[7])
    return core, t8


def find_sites(guide, seq):
    """All seed sites in seq. Returns list of (core_start, site_class)."""
    core, t8 = site_strings(guide)
    out = []
    n, m = len(seq), len(core)
    start = 0
    while True:
        i = seq.find(core, start)
        if i < 0:
            break
        start = i + 1
        has_m8 = i - 1 >= 0 and seq[i - 1] == t8
        has_a1 = i + m < n and seq[i + m] == "A"
        if has_m8 and has_a1:
            cls = "8mer"
        elif has_m8:
            cls = "7mer-m8"
        elif has_a1:
            cls = "7mer-A1"
        else:
            cls = "6mer"
        out.append((i, cls))
    return out


def guide_features(guide):
    import RNA
    g = guide.upper().replace("T", "U")
    def dg(a):
        return RNA.duplexfold(a, kmers.revcomp(a.replace("U", "T"))
                              .replace("T", "U")).energy
    five, three = dg(g[:5]), dg(g[-5:])
    seed = g[1:8]
    return {
        "guide_gc": float(sum(c in "GC" for c in g) / len(g)),
        "guide_dg5_kcal": float(five),
        "guide_dg3_kcal": float(three),
        "guide_asymmetry_kcal": float(five - three),
        "seed_pairing_stability_kcal": float(
            RNA.duplexfold(seed, kmers.revcomp(seed.replace("U", "T"))
                           .replace("T", "U")).energy),
    }


def _pair_features(args):
    """Features for one (construct, transcript). Runs in a worker process."""
    import RNA
    (construct, guide_rna, guide_dna, tid, symbol, utr3, cds, acc15,
     x_rel) = args
    sites = find_sites(guide_dna, utr3)
    if not sites:
        return None
    n = len(utr3)
    rows = []
    inv_K = 0.0
    for i, cls in sites:
        lo, hi = max(0, i - 1 - FLANK), min(n, i + 6 + 1 + FLANK)
        win = utr3[lo:hi].replace("T", "U")
        try:
            d = RNA.duplexfold(guide_rna, win)
            dgd = float(d.energy)
        except Exception:
            dgd = np.nan
        end = min(n - 1, i + 6)
        p = float(acc15[end]) if acc15 is not None and end < len(acc15) else np.nan
        p = min(max(p, 1e-12), 1.0) if np.isfinite(p) else np.nan
        # Binding must PAY the cost of opening the site, so the opening
        # free energy dG_open = -RT ln P_unpaired >= 0 is ADDED to the
        # duplex energy. Adding RT ln P_unpaired instead subtracts that
        # cost and makes an inaccessible site look like the strongest
        # binder, which is the opposite of the intended physics.
        ddg = dgd - RT * np.log(p) if np.isfinite(p) and np.isfinite(dgd) else np.nan
        a, b = max(0, i - AU_WIN), min(n, i + 6 + AU_WIN)
        loc = utr3[a:b]
        au = float(sum(c in "AT" for c in loc) / max(1, len(loc)))
        if np.isfinite(ddg):
            inv_K += np.exp(-ddg / RT)
        rows.append({
            "construct": construct, "transcript_id": tid,
            "gene_symbol": symbol, "site_start": int(i), "site_class": cls,
            "dg_duplex_kcal": dgd, "p_unpaired_15": p,
            "ddG_kcal": ddg,
            "rel_pos_in_utr3": float(i / max(1, n)),
            "dist_to_utr3_start": int(i),
            "dist_to_utr3_end": int(n - i - 6),
            "local_au_content": au, "utr3_len": int(n),
            "cds_len": int(len(cds)), "x_rel": float(x_rel),
        })
    K = 1.0 / inv_K if inv_K > 0 else np.nan
    for r in rows:
        r["K_transcript"] = K
        r["n_sites"] = len(rows)
    return rows


def build(out=FEAT, nproc=None, constructs=None, cand=None, guides=None,
          acc=None):
    """Per-site features for every (guide, transcript) pair with a seed site.

    cand, guides and acc default to the D1 candidate set, the D1 siRNA table
    and the cached D1 accessibility array, so calling build() with no
    arguments reproduces the original behaviour exactly. They are parameters
    so that a second dataset can be scored through this same code path rather
    than through a copy of it: the accessibility array is guide-independent
    and both GSE5814 and E-MEXP-668 are HeLa, so the cached array is reusable
    and only the duplex energies have to be recomputed per guide.
    """
    from multiprocessing import Pool
    from .accessibility import Accessibility
    from .offtarget import load_candidates
    from .sirna import per_construct

    cand = load_candidates() if cand is None else cand
    acc = Accessibility() if acc is None else acc
    pc = per_construct() if guides is None else guides
    if constructs is not None:
        pc = pc[pc.construct.isin(constructs)]

    cache = {t: acc.get(t, 15) for t in cand.transcript_id}
    jobs = []
    for _, s in pc.iterrows():
        g_dna = s.guide_5to3_dna
        g_rna = g_dna.replace("T", "U")
        core = kmers.revcomp(g_dna[1:7])
        for tid, sym, utr3, cds, x in zip(cand.transcript_id, cand.gene_symbol,
                                          cand.utr3_seq, cand.cds_seq,
                                          cand.x_rel):
            if core in utr3:
                jobs.append((s.construct, g_rna, g_dna, tid, sym, utr3, cds,
                             cache.get(tid), x))
    nproc = nproc or max(1, (os.cpu_count() or 4) - 2)
    rows = []
    with Pool(nproc) as p:
        for r in p.imap_unordered(_pair_features, jobs, chunksize=64):
            if r:
                rows.extend(r)
    df = pd.DataFrame(rows)

    gf = pd.DataFrame([dict(construct=s.construct, **guide_features(
        s.guide_5to3_dna)) for _, s in pc.iterrows()])
    df = df.merge(gf, on="construct", how="left")
    df.to_parquet(out, index=False, compression="zstd")
    return df


def load_features():
    return pd.read_parquet(FEAT)


def transcript_level(df=None):
    """Collapse sites to one row per (construct, transcript): the object the
    equilibrium layer consumes."""
    if df is None:
        df = load_features()
    best = (df.sort_values("ddG_kcal")
              .groupby(["construct", "transcript_id"], as_index=False).first())
    agg = (df.groupby(["construct", "transcript_id"])
             .agg(n_sites=("site_start", "size"),
                  n_8mer=("site_class", lambda s: int((s == "8mer").sum())),
                  n_7mer_m8=("site_class", lambda s: int((s == "7mer-m8").sum())),
                  n_7mer_A1=("site_class", lambda s: int((s == "7mer-A1").sum())),
                  n_6mer=("site_class", lambda s: int((s == "6mer").sum())),
                  best_ddG=("ddG_kcal", "min"),
                  mean_p_unpaired=("p_unpaired_15", "mean"))
             .reset_index())
    cols = ["construct", "transcript_id", "gene_symbol", "K_transcript",
            "x_rel", "utr3_len", "cds_len", "site_class", "dg_duplex_kcal",
            "p_unpaired_15", "rel_pos_in_utr3", "local_au_content",
            "guide_gc", "guide_asymmetry_kcal", "seed_pairing_stability_kcal"]
    return best[cols].merge(agg, on=["construct", "transcript_id"], how="left")
