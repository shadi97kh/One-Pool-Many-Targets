"""
Bounded retry of the Jackson et al. 2006 full text, PMC1484447.

The paper states it is freely available through the journal's open access
option, so the PMC open-access web service and its FTP package were retried.
Every attempt is recorded with its HTTP status whether it worked or not.
This affects only the sequence cross-check, which already succeeded by
another route through the Garcia 2011 supplementary table, so nothing
downstream depends on the outcome.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import provenance as P, runner  # noqa: E402

ATTEMPTS = [
    ("https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC1484447",
     "data/lit/jackson2006/oa_fcgi_PMC1484447.xml",
     "PMC open-access web service, the route the retry was asked to try"),
    ("https://pmc.ncbi.nlm.nih.gov/utils/oa/oa.fcgi?id=PMC1484447",
     "data/lit/jackson2006/oa_fcgi_new_host_PMC1484447.xml",
     "the same service on the current PMC host"),
    ("https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/"
     "fullTextXML",
     "data/lit/jackson2006/PMC1484447_fulltext_retry.xml",
     "Europe PMC full text, retried; returned 404 on the earlier pass"),
    ("https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/"
     "supplementaryFiles",
     "data/lit/jackson2006/PMC1484447_suppl_retry.zip",
     "Europe PMC supplementary files, retried"),
    ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
     "db=pmc&id=1484447&retmode=xml",
     "data/lit/jackson2006/efetch_PMC1484447.xml",
     "NCBI efetch against the PMC database"),
]


def fn(seed=0):
    rows = []
    for url, dest, note in ATTEMPTS:
        p = P.fetch(url, dest, "jackson2006_oa_retry", accession="PMC1484447",
                    note=note, volatile=True)
        ok = False
        detail = "not downloaded"
        if p and os.path.exists(p):
            head = open(p, "rb").read(4000).decode("utf8", "replace")
            has_body = ("<body" in head or "<sec" in head
                        or "<abstract" in head)
            blocked = ("does not allow downloading" in head
                       or "not open access" in head or "<error" in head
                       or "errMsg" in head)
            ok = bool(has_body and not blocked)
            detail = head[:400].replace("\n", " ")
        rows.append({"url": url, "downloaded": p is not None,
                     "full_text_usable": ok, "first_bytes": detail,
                     "note": note})
    usable = [r for r in rows if r["full_text_usable"]]
    return {
        "target": "Jackson AL et al. RNA 2006;12:1179-1187, PMC1484447",
        "attempts": rows,
        "n_attempts": len(rows),
        "n_usable": len(usable),
        "full_text_obtained": bool(usable),
        "consequence": (
            "none for any downstream number. The siRNA sequences this "
            "article would have supplied were already obtained from the "
            "Garcia et al. 2011 supplementary table joined on GSM accession, "
            "and independently corroborated by recovering the same 7mer-m8 "
            "sites from the measured response; see results/"
            "d1_seed_validation.json."),
    }


if __name__ == "__main__":
    runner.run("d9_jackson_oa_retry", fn, seed=0)
