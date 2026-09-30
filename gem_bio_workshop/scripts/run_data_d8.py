"""D8: parse GSE14073, build its candidate universe and accessibility."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import crosscontext as CC, dose, provenance as P, runner  # noqa: E402


def fn_parse(seed=0):
    out = CC.build()
    for k, v in out["paths"].items():
        P.register_local(v, "D8_GSE14073_derived", note=f"derived table: {k}")
    return out


def fn_candidates(seed=0):
    df = CC.build_candidates()
    P.register_local(CC.CAND, "D8_GSE14073_derived",
                     note="retrieval universe: GPL6793 genes with a GENCODE "
                          "canonical 3'UTR of at least 10 nt")
    return {"n_candidate_transcripts": int(len(df)),
            "total_utr3_nucleotides": int(df.utr3_len.sum()),
            "gencode_release": 50, "path": CC.CAND}


def fn_acc(seed=0):
    out = CC.build_accessibility(reuse=(dose.ACC,))
    P.register_local(CC.ACC, "D8_GSE14073_derived",
                     note="pfl_fold unpaired probabilities over the D8 "
                          "candidate 3'UTRs")
    return out


if __name__ == "__main__":
    runner.run("d8_gse14073", fn_parse, seed=0)
    runner.run("d8_candidates", fn_candidates, seed=0)
    runner.run("f5_accessibility_d8", fn_acc, seed=0)
