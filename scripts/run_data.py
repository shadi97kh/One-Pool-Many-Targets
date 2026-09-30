"""Stage 1: D1, D3, D4. Each writes results/<name>.json through the harness."""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import runner, provenance as P            # noqa: E402
from riscpool import data_gse5814, data_gencode, hela   # noqa: E402
import pandas as pd                                    # noqa: E402


def d1(seed=0):
    info = data_gse5814.build()
    s = pd.read_csv(info["samples"], sep="\t")
    sir = s[s.is_sirna_hela]
    per = (sir.groupby("construct").size().sort_index())
    P.register_local(info["expression"], "D1_GSE5814",
                     note="parsed per-probe VALUE/INTENSITY tables, 68 GSMs")
    P.register_local(info["annotation"], "D1_GSE5814",
                     note="probe -> gene symbol / accession, 3 platforms")
    info = dict(info)
    info.update({
        "n_mapk14_seed_variant_constructs": int(
            sir[(sir.target_gene == "MAPK14")
                & (sir.variant != "parent")].construct.nunique()),
        "n_seed_altering_constructs_pos2to8": int(
            sir[sir.seed_altered == True].construct.nunique()),   # noqa: E712
        "n_seed_preserving_constructs": int(
            sir[sir.seed_altered == False].construct.nunique()),  # noqa: E712
        "target_genes": sorted(sir.target_gene.dropna().unique().tolist()),
        "arrays_per_construct": {k: int(v) for k, v in per.items()},
        "channel_convention": "CH1=Cy3=mock control, CH2=Cy5=siRNA; "
                              "VALUE=log10(CH2/CH1), negative = repressed",
        "note_construct_count": (
            "The build brief anticipated 27 constructs. The series as "
            "deposited contains the number reported in n_constructs; that "
            "measured count is reported rather than the anticipated one."),
    })
    return info


def d3(seed=0):
    tx = data_gencode.build_transcripts()
    tg = data_gencode.build_gtf_tags()
    can = data_gencode.canonical_by_symbol()
    can.to_parquet(os.path.join(P.DATA, "gencode_canonical_by_symbol.parquet"),
                   index=False, compression="zstd")
    for f in ("gencode_transcripts.parquet", "gencode_tx_tags.parquet",
              "gencode_canonical_by_symbol.parquet"):
        P.register_local(os.path.join(P.DATA, f), "D3_GENCODE",
                         note=f"derived from GENCODE release "
                              f"{data_gencode.RELEASE}")
    return {
        "gencode_release": data_gencode.RELEASE,
        "n_pc_transcripts": int(len(tx)),
        "n_gtf_transcript_records": int(len(tg)),
        "n_transcripts_with_utr3": int((tx.utr3_len > 0).sum()),
        "n_transcripts_with_cds": int((tx.cds_len > 0).sum()),
        "median_utr3_len": float(tx.loc[tx.utr3_len > 0, "utr3_len"].median()),
        "mean_utr3_len": float(tx.loc[tx.utr3_len > 0, "utr3_len"].mean()),
        "total_utr3_nt": int(tx.utr3_len.sum()),
        "total_cds_nt": int(tx.cds_len.sum()),
        "n_canonical_gene_symbols_with_utr3": int(len(can)),
        "n_canonical_mane_select": int(can.mane_select.sum()),
    }


def d4(seed=0):
    info = hela.build()
    P.register_local(info["path"], "D4_abundance",
                     note="relative HeLa abundance from GSE5814 mock Cy3 "
                          "channel, collapsed to GENCODE canonical "
                          "transcripts")
    d = hela.load_abundance()
    info = dict(info)
    info.update({
        "source": "GSE5814 INTENSITY1 (raw Cy3, CH1 = mock control channel)",
        "top10_genes_by_relative_abundance":
            d.head(10)[["gene_symbol", "x_rel"]].to_dict("records"),
        "sum_x_rel": float(d.x_rel.sum()),
        "median_x_rel": float(d.x_rel.median()),
    })
    return info


if __name__ == "__main__":
    runner.run("d1_gse5814", d1, seed=0)
    runner.run("d3_gencode", d3, seed=0)
    runner.run("d4_hela_abundance", d4, seed=0)
    print("\nstage 1 (D1,D3,D4) complete")
