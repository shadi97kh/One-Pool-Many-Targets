import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import accessibility, runner, provenance as P
def fn(seed=0):
    info = accessibility.build()
    P.register_local(info["path"], "features_accessibility",
                     note="ViennaRNA pfl_fold_up unpaired probabilities over "
                          "GENCODE v50 3'UTRs of the HeLa-expressed candidate set")
    info = dict(info)
    info["errors"] = dict(list(info["errors"].items())[:20])
    return info
runner.run("f1_accessibility", fn, seed=0)
