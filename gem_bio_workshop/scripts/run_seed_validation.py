"""
Independent corroboration of the siRNA sequences.

seeds.py recovers each construct's 7mer-m8 site from the measured expression
response alone, never reading a sequence file. sirna.py reads the published
guide strands, never reading the expression data. This experiment compares
them. Agreement is a joint check on the sequence table, on the construct
assignment parsed out of the GEO labels, and on the claim that guide positions
2-8 are the functional seed.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import runner, seeds, sirna, provenance as P   # noqa: E402


def fn(seed=0):
    rec, meta = seeds.build()
    P.register_local(seeds.OUT, "D1_seed_recovery",
                     note="7mer-m8 sites recovered from measured log ratios")
    seqs = sirna.build()
    P.register_local(sirna.OUT, "D1_sirna_sequences",
                     note="published guide strands joined by GSM accession")
    pub = sirna.per_construct()[["construct", "site_7mer_m8_dna",
                                 "site_6mer_dna", "guide_5to3_dna"]]
    m = rec.merge(pub, on="construct", how="inner")
    m["site_agrees"] = m.recovered_site == m.site_7mer_m8_dna
    m["core6_agrees"] = m.recovered_site.str[1:] == m.site_6mer_dna

    inseed = m[m.in_seed_by_definition]
    outseed = m[~m.in_seed_by_definition]
    return {
        "parent_site_recovered_from_expression": meta["parent_site"],
        "parent_site_published": str(
            pub.loc[pub.construct == "MAPK14-193_parent",
                    "site_7mer_m8_dna"].iloc[0]),
        "parent_site_welch_t": meta["parent_site_t"],
        "parent_scan_top10_kmers": meta["parent_top10"],
        "n_constructs_compared": int(len(m)),
        "n_sites_exactly_agreeing": int(m.site_agrees.sum()),
        "n_6mer_cores_agreeing": int(m.core6_agrees.sum()),
        "agreement_rate_7mer": float(m.site_agrees.mean()),
        "agreement_rate_6mer_core": float(m.core6_agrees.mean()),
        "n_seed_altering_constructs": int(len(inseed)),
        "n_seed_altering_with_predicted_index_confirmed": int(
            inseed.prediction_confirmed.sum()),
        "mean_t_parent_site_seed_preserving": float(
            outseed.t_parent_site.mean()),
        "mean_t_parent_site_seed_altering": float(
            inseed.t_parent_site.mean()),
        "median_rank_parent_site_seed_preserving_of_16384": float(
            outseed.rank_parent_site.median()),
        "median_rank_parent_site_seed_altering_of_16384": float(
            inseed.rank_parent_site.median()),
        "per_construct": m[["construct", "mut_position",
                            "in_seed_by_definition", "recovered_site",
                            "site_7mer_m8_dna", "site_agrees",
                            "core6_agrees", "recovered_site_t",
                            "t_parent_site", "rank_parent_site"]]
                        .to_dict("records"),
        "interpretation_is_not_asserted_here": (
            "Counts and statistics only. The parent site was defined from the "
            "expression contrast without reading any sequence file; the "
            "published sites were read without touching the expression data."),
        # constructs the response data covers but for which no published
        # guide strand exists, so the comparison could not be made. The
        # previous expression carried two unexplained constants and returned
        # a negative count, which is impossible.
        "n_constructs_recovered_from_expression": int(len(rec)),
        "n_constructs_with_published_sequence": int(
            seqs.construct.dropna().nunique()),
        "n_constructs_without_published_sequence": int(len(
            set(rec.construct) - set(seqs.construct.dropna()))),
    }


if __name__ == "__main__":
    runner.run("d1_seed_validation", fn, seed=0)
