"""Per-site sequence and thermodynamic features for the D7 guides."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                    # noqa: E402
from riscpool import dose, provenance as P, runner    # noqa: E402


def fn(seed=0):
    df = dose.build_features()
    P.register_local(dose.FEAT, "D7_GSE28786_derived",
                     note="per-site features for the five D7 constructs over "
                          "the D7 candidate 3'UTRs")
    tx = dose.transcript_level(df)
    import RNA
    return {
        "n_site_rows": int(len(df)),
        "n_construct_transcript_pairs": int(len(tx)),
        "constructs": sorted(df.construct.unique()),
        "n_transcripts_per_construct": {
            k: int(v) for k, v in
            tx.groupby("construct").transcript_id.nunique().items()},
        "site_class_counts": {k: int(v) for k, v in
                              df.site_class.value_counts().items()},
        "frac_sites_with_finite_ddG": float(np.isfinite(df.ddG_kcal).mean()),
        "ddG_kcal_median": float(np.nanmedian(df.ddG_kcal)),
        "ddG_kcal_min": float(np.nanmin(df.ddG_kcal)),
        "ddG_kcal_max": float(np.nanmax(df.ddG_kcal)),
        "log10_K_transcript_uncalibrated_min": float(
            np.log10(np.nanmin(tx.K_transcript))),
        "log10_K_transcript_uncalibrated_max": float(
            np.log10(np.nanmax(tx.K_transcript))),
        "viennarna_version": RNA.__version__,
        "gencode_release": 50,
        "path": dose.FEAT,
    }


if __name__ == "__main__":
    runner.run("f4_features_d7", fn, seed=0)
