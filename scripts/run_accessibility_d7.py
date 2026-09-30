"""ViennaRNA local accessibility over the D7 (GSE28786) candidate 3'UTRs."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import dose, provenance as P, runner  # noqa: E402


def fn(seed=0):
    out = dose.build_accessibility()
    P.register_local(dose.ACC, "D7_GSE28786_derived",
                     note="pfl_fold unpaired probabilities, u=8 and u=15, "
                          "over the D7 candidate 3'UTRs")
    return out


if __name__ == "__main__":
    runner.run("f3_accessibility_d7", fn, seed=0)
