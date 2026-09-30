import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
from riscpool import features, runner, provenance as P

def fn(seed=0):
    df = features.build()
    P.register_local(features.FEAT, "features",
                     note="per-site sequence and ViennaRNA thermodynamic "
                          "features for every retrieved (siRNA, transcript) "
                          "pair on GENCODE v50 3'UTRs")
    tx = features.transcript_level(df)
    import RNA
    from riscpool import data_gencode
    per_class = df.site_class.value_counts().to_dict()
    return {
        "gencode_release": data_gencode.RELEASE,
        "viennarna_version": RNA.__version__,
        "RT_kcal_per_mol": features.RT,
        "duplexfold_flank_nt": features.FLANK,
        "local_au_window_nt": features.AU_WIN,
        "n_sites": int(len(df)),
        "n_construct_transcript_pairs": int(len(tx)),
        "n_constructs": int(df.construct.nunique()),
        "n_transcripts_hit": int(df.transcript_id.nunique()),
        "sites_by_class": {k: int(v) for k, v in per_class.items()},
        "median_sites_per_construct": float(
            df.groupby("construct").size().median()),
        "median_pairs_per_construct": float(
            tx.groupby("construct").size().median()),
        "dg_duplex_kcal_mean": float(np.nanmean(df.dg_duplex_kcal)),
        "dg_duplex_kcal_sd": float(np.nanstd(df.dg_duplex_kcal)),
        "p_unpaired_15_median": float(np.nanmedian(df.p_unpaired_15)),
        "ddG_kcal_mean": float(np.nanmean(df.ddG_kcal)),
        "ddG_kcal_sd": float(np.nanstd(df.ddG_kcal)),
        "n_sites_with_nan_ddG": int((~np.isfinite(df.ddG_kcal)).sum()),
        "log10_K_transcript_min": float(np.log10(np.nanmin(tx.K_transcript))),
        "log10_K_transcript_max": float(np.log10(np.nanmax(tx.K_transcript))),
        "log10_K_transcript_sd": float(np.nanstd(np.log10(tx.K_transcript))),
        "features_path": features.FEAT,
    }

runner.run("f2_features", fn, seed=0)
