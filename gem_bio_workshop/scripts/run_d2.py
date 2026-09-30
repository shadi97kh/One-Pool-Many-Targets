"""
D2 - Birmingham et al. 2006 off-target set.

Attempted per the build brief. Every URL tried is recorded with its HTTP
status, including the ones that failed on the earlier pass, because the route
by which a dataset was eventually found is part of the record.

The earlier pass marked this FAILED and its reasoning was sound as far as it
went: no PMC identifier, no GEO series linked to the PMID, and the van Dongen
supplementary archive contains only images. What it missed is that the data
was deposited in ArrayExpress, not GEO. Searching the ArrayExpress collection
for the article's own title phrase returns exactly one study, E-MEXP-668,
whose IDF carries PubMed ID 16489337. That identification is checked in code
against the IDF rather than asserted; see riscpool.birmingham.identify.

So D2 is no longer FAILED. The deposit gives 29 two-colour Agilent arrays
with per-feature log10 ratios and gene names, and the SDRF gives the sense
strand sequence of every siRNA, from which the guide strands follow by
reverse complement.
"""
import os
import sys
import zipfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import birmingham as B, provenance as P, runner  # noqa: E402

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
CANDIDATES = [
    (f"{EPMC}/PMC2635553/supplementaryFiles",
     "data/raw/d2_vandongen_PMC2635553_suppl.zip",
     "van Dongen S, Abreu-Goodger C, Enright AJ. Nat Methods 2008;5:1023-5. "
     "PMC2635553. Supplementary files, which reprocess the Birmingham and "
     "Jackson off-target datasets."),
    (f"{EPMC}/PMC1804340/supplementaryFiles",
     "data/raw/d2_pmc1804340_suppl.zip",
     "candidate PMC record for a Birmingham-related deposit"),
    ("https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5291/soft/"
     "GSE5291_family.soft.gz",
     "data/raw/d2_GSE5291_family.soft.gz",
     "GSE5291, the GEO series that Garcia et al. 2011 lists alongside "
     "GSE5814 and which corresponds to a Dharmacon/Birmingham off-target "
     "experiment"),
    ("https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5769/soft/"
     "GSE5769_family.soft.gz",
     "data/raw/d2_GSE5769_family.soft.gz",
     "GSE5769, a further off-target series listed by Garcia et al. 2011"),
    (f"{B.BASE}/{B.ACCESSION}.idf.txt",
     os.path.join("data", "raw", "birmingham", f"{B.ACCESSION}.idf.txt"),
     "ArrayExpress E-MEXP-668 investigation description; found by searching "
     "the ArrayExpress collection for the article title phrase, and the file "
     "that carries PubMed ID 16489337 and so identifies the deposit"),
    (f"{B.BASE}/{B.ACCESSION}.sdrf.txt",
     os.path.join("data", "raw", "birmingham", f"{B.ACCESSION}.sdrf.txt"),
     "ArrayExpress E-MEXP-668 sample and data relationship file; names every "
     "array data file and gives the sense strand sequence of every siRNA as "
     "its compound factor value"),
]


def machine_readable(path):
    """A downloaded file only counts if something can actually be parsed out
    of it. A zip of scanned page images is not machine readable."""
    if path is None or not os.path.exists(path):
        return False, "not downloaded"
    if path.endswith(".gz"):
        import gzip
        try:
            with gzip.open(path, "rt", errors="replace") as fh:
                head = fh.read(4000)
            return ("!Sample_title" in head or "^SAMPLE" in head or
                    "!Series_title" in head), "SOFT header parsed"
        except Exception as exc:
            return False, f"{type(exc).__name__}: {exc}"
    if path.endswith(".zip"):
        try:
            z = zipfile.ZipFile(path)
            names = z.namelist()
            tabular = [n for n in names
                       if n.lower().endswith((".txt", ".csv", ".tsv", ".xls",
                                              ".xlsx"))]
            return bool(tabular), f"members={names[:20]} tabular={tabular[:10]}"
        except Exception as exc:
            return False, f"{type(exc).__name__}: {exc}"
    return os.path.getsize(path) > 0, "non-archive file present"


def fn(seed=0):
    attempts = []
    usable = []
    for url, dest, note in CANDIDATES:
        p = P.fetch(url, dest, "D2_birmingham", note=note)
        ok, detail = machine_readable(p)
        attempts.append({"url": url, "downloaded": p is not None,
                         "machine_readable": bool(ok), "detail": detail[:600],
                         "note": note})
        if ok:
            usable.append(url)
    # A download only counts as D2 if it actually IS the Birmingham dataset.
    # It is not enough for some file to parse.
    identified = []
    for a in attempts:
        u = a["url"]
        if not a["machine_readable"]:
            continue
        if "GSE5291" in u:
            a["is_birmingham"] = False
            a["what_it_actually_is"] = (
                "GSE5291 = Schwarz et al., 'Designing siRNA that distinguish "
                "between genes that differ by a single nucleotide', PMID "
                "16965178. SOD1 allele-specific siRNAs in HeLa. A different "
                "study; retrieved and recorded, but it is NOT D2.")
        elif "GSE5769" in u:
            a["is_birmingham"] = False
            a["what_it_actually_is"] = (
                "GSE5769 = Jackson et al., 'Position-specific chemical "
                "modification of siRNAs reduces off-target transcript "
                "silencing', PMID 16682562. A different study; retrieved and "
                "recorded, but it is NOT D2.")
        elif "E-MEXP-668" in u:
            ident = B.identify()
            a["is_birmingham"] = bool(ident["identified"])
            a["identification"] = ident
            a["what_it_actually_is"] = (
                "ArrayExpress E-MEXP-668. The IDF names PubMed ID "
                f"{ident.get('pubmed_id_in_idf')}, which is Birmingham et "
                "al. 2006, so this IS D2." if ident["identified"] else
                "E-MEXP-668 was retrieved but its IDF does not name the "
                "expected PMID, so it is not accepted as D2.")
        elif "PMC2635553" in u:
            a["is_birmingham"] = False
            a["what_it_actually_is"] = (
                "van Dongen 2008 supplementary archive contains only figure "
                "images and a scanned PDF. No siRNA table, no processed "
                "Birmingham matrix.")
        else:
            a["is_birmingham"] = False
        if a.get("is_birmingham"):
            identified.append(u)
    usable = identified

    if not usable:
        raise RuntimeError(
            "D2 FAILED. The Birmingham et al. 2006 (Nat Methods 3:199-204, "
            "PMID 16489337) off-target set could not be obtained in "
            "machine-readable form. The paper has no PMC identifier and "
            "NCBI elink returns no GEO series for its PMID, so there is no "
            "deposited matrix to fetch. The van Dongen 2008 supplementary "
            "archive that reprocesses it contains only figure images and a "
            "scanned PDF, no table. Two adjacent HeLa off-target series "
            "(GSE5291, GSE5769) were retrieved and are recorded in "
            "data/PROVENANCE.json, but they are different studies and are "
            "NOT D2. Substituting one of them would put a different "
            "experiment behind the D2 label, so D2 is marked FAILED and the "
            "analysis proceeds on D1 alone.\n"
            + "\n".join(f"  {a['url']} -> downloaded={a['downloaded']} "
                        f"machine_readable={a['machine_readable']} "
                        f"({a['detail'][:200]})" for a in attempts))
    return {"attempts": attempts, "usable_sources": usable,
            "n_usable": len(usable),
            "status_note": "D2 obtained; see attempts for what was tried"}


if __name__ == "__main__":
    runner.run("d2_birmingham", fn, seed=0)
