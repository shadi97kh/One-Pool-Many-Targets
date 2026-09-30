"""
D2, second stage: fetch the E-MEXP-668 arrays and build a per-gene response.

The first stage established that the deposit is the right one. This stage
downloads every array data file the SDRF names, parses the Agilent Feature
Extraction FEATURES block, and collapses probes to gene symbols, producing
the machine-readable per-transcript table the earlier attempt concluded did
not exist. Every file is recorded in the provenance ledger with its own hash.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np                                          # noqa: E402
from riscpool import birmingham as B, provenance as P, runner  # noqa: E402


def fn(seed=0):
    ident = B.identify()
    if not ident["identified"]:
        raise RuntimeError(
            "E-MEXP-668 IDF does not name the expected PubMed id; refusing "
            f"to treat it as D2. {ident}")
    sdrf = B.parse_sdrf()
    files, failed = [], []
    for name in sorted(sdrf.array_data_file.unique()):
        dest = os.path.join("data", "raw", "birmingham", name)
        p = P.fetch(f"{B.BASE}/{name}", dest, "D2_birmingham_arrays",
                    accession=B.ACCESSION,
                    note="Agilent Feature Extraction output; per-feature "
                         "log10(Cy5/Cy3) = log10(siRNA/mock) with gene names")
        (files if p else failed).append(p or name)
    if not files:
        raise RuntimeError("no array data files could be downloaded")

    resp = B.build_response(files, sdrf)
    P.register_local(B.RESP, "D2_birmingham_derived",
                     note="per-gene median log10(siRNA/mock) per construct")
    sdrf.to_parquet(B.SIRNA, index=False, compression="zstd")
    P.register_local(B.SIRNA, "D2_birmingham_derived",
                     note="array to siRNA mapping, with guide strands "
                          "derived from the SDRF sense sequences")

    guides = sdrf[sdrf.guide_5to3_dna.notna()]
    per = (resp.groupby("construct")
               .agg(n_genes=("gene_symbol", "nunique"),
                    median_log10ratio=("value", "median"),
                    mean_log10ratio=("value", "mean"))
               .reset_index())
    return {
        "accession": B.ACCESSION,
        "identification_from_idf": ident,
        "route": (
            "found by searching the ArrayExpress collection for the article "
            "title phrase, not by guessing an accession; the IDF's PubMed id "
            "is checked in code before the deposit is accepted"),
        "n_array_files_named_by_sdrf": int(sdrf.array_data_file.nunique()),
        "n_array_files_downloaded": len(files),
        "n_array_files_failed": len(failed),
        "n_arrays_parsed": int(resp.array_data_file.nunique()),
        "n_constructs": int(resp.construct.nunique()),
        "constructs": sorted(resp.construct.unique()),
        "n_distinct_guides": int(guides.guide_5to3_dna.nunique()),
        "doses_nM": sorted(set(float(d) for d in guides.dose if d)),
        "cell_line": sorted(set(sdrf.cell_line.dropna())),
        "n_gene_symbols": int(resp.gene_symbol.nunique()),
        "n_rows": int(len(resp)),
        "median_probes_per_gene": float(resp.n_probes.median()),
        "value_definition": (
            "log10 of the siRNA channel over the mock channel, per gene, "
            "median over probes. Negative is repression. Same sign "
            "convention as the GSE5814 pipeline."),
        "guides": guides[["construct", "sense_5to3_dna", "guide_5to3_dna",
                          "seed_2_8_dna", "site_7mer_m8_dna", "dose"]]
                  .drop_duplicates().to_dict("records"),
        "per_construct": per.to_dict("records"),
        "overall_median_log10ratio": float(np.median(resp.value)),
        "supersedes": (
            "the earlier FAILED record for D2. That record was correct that "
            "no GEO deposit exists and that the van Dongen archive carries "
            "no table; it was wrong that the data was unobtainable, because "
            "it was deposited in ArrayExpress instead."),
        "paths": {"response": B.RESP, "sirna": B.SIRNA},
    }


if __name__ == "__main__":
    runner.run("d2b_birmingham_arrays", fn, seed=0)
