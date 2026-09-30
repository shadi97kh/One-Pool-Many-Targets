"""D7: parse GSE28786 into the tables e9 consumes, and build its candidate
3'UTR universe. Provenance-registered, runner-recorded."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import dose, provenance as P, runner  # noqa: E402


def fn_parse(seed=0):
    g = dose.guides_from_table1()
    out = dose.build()
    out["n_guides_parsed_from_table1"] = int(len(g))
    out["guides"] = g.drop(columns=["table_row_label"]).to_dict("records")
    out["all_passengers_are_revcomp_of_guide"] = bool(
        g.passenger_is_revcomp_of_guide.all())
    out["all_underlined_seeds_match_positions_2_7"] = bool(
        g.underlined_seed_matches_positions_2_7.dropna().all())
    out["guide_source"] = (
        "Table 1 of PMC3130022, parsed from the recorded full-text XML at "
        "data/lit/caffrey2011/PMC3130022_fulltext.xml. Not typed in. The "
        "3' overhang is the lowercase suffix the table itself uses and the "
        "seed is the table's own <underline> span; both are checked against "
        "the guide body rather than assumed.")
    for k, v in out["paths"].items():
        P.register_local(v, "D7_GSE28786_derived",
                         note=f"derived table: {k}")
    return out


def fn_candidates(seed=0):
    df = dose.build_candidates()
    P.register_local(dose.CAND, "D7_GSE28786_derived",
                     note="retrieval universe: GPL9324 genes with a GENCODE "
                          "canonical 3'UTR of at least 10 nt")
    return {
        "n_candidate_transcripts": int(len(df)),
        "total_utr3_nucleotides": int(df.utr3_len.sum()),
        "median_utr3_len": float(df.utr3_len.median()),
        "gencode_release": 50,
        "path": dose.CAND,
        "note": ("both cell lines were run on the same array, so the "
                 "retrieval universe is shared and only the abundance "
                 "vector differs between them"),
    }


if __name__ == "__main__":
    runner.run("d7_gse28786", fn_parse, seed=0)
    runner.run("d7_candidates", fn_candidates, seed=0)
