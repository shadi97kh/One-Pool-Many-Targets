"""
D8 - Burchard et al. 2009 cross-species / cross-context set (the e10
substrate).

  Burchard J, Zhang C, Liu AM, Poon RTP, Lee NPY, Wong K-F, et al.
  "microRNA-like off-target transcript regulation by siRNAs is species
  specific." RNA 2009; 15(2):308-315. PMC2648714.

The article itself is not open access: Europe PMC returns 404 for its full
text and "Article with id PMC2648714 is not open access one" for its
supplementary files, and the publisher blocks XML retrieval through efetch.
Those attempts are recorded below as failures, because the route by which the
accession was found matters.

The accession was obtained from GEO rather than from the paper: NCBI's own
series record for GSE14073 carries pubmed id 19144911, which is this article.
That link is what identifies the deposit, and it is fetched and recorded here
so the identification is checkable rather than asserted.

GPL6793 is the human platform; GPL6794 is the mouse one and is downloaded
too, because the paper's claim is about species specificity and leaving half
the deposit unfetched would misrepresent what was available.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import provenance as P  # noqa: E402

GEO = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE14nnn/GSE14073"
E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

print("### D8  the accession link itself, from NCBI")
P.fetch(f"{E}/esummary.fcgi?db=gds&id=200014073&retmode=json",
        "data/lit/burchard2009/GSE14073_esummary.json", "D8_GSE14073",
        accession="GSE14073",
        note="GEO series summary; its pubmed id 19144911 is what ties this "
             "deposit to PMC2648714",
        volatile=True)

print("\n### D8  GEO GSE14073")
for gpl, what in (("GPL6793", "human platform: HUH7 and PLC/PRF/5 samples"),
                  ("GPL6794", "mouse platform: liver and Hepa1-6 samples")):
    P.fetch(f"{GEO}/matrix/GSE14073-{gpl}_series_matrix.txt.gz",
            f"data/raw/GSE14073-{gpl}_series_matrix.txt.gz", "D8_GSE14073",
            accession="GSE14073",
            note=f"series matrix for {gpl}; {what}")
P.fetch(f"{GEO}/suppl/filelist.txt", "data/raw/GSE14073_filelist.txt",
        "D8_GSE14073", accession="GSE14073", note="supplementary listing")

print("\n### D8  attempts recorded as failures (tried, blocked by the "
      "publisher)")
P.fetch("https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2648714/"
        "fullTextXML",
        "data/lit/burchard2009/PMC2648714_fulltext.xml", "D8_burchard2009",
        accession="PMC2648714",
        note="Europe PMC full text; the article is not open access and this "
             "404s, which is why the accession had to come from GEO")
P.fetch("https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2648714/"
        "supplementaryFiles",
        "data/lit/burchard2009/PMC2648714_suppl.zip", "D8_burchard2009",
        accession="PMC2648714",
        note="Europe PMC supplementary files; returns an errMsg document "
             "rather than a zip, recorded so the attempt is on record")
print("\n### downloads finished")

print("\n### D8  GPL6793 platform annotation, to map probes to gene symbols")
P.fetch("https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL6nnn/GPL6793/annot/"
        "GPL6793.annot.gz", "data/raw/GPL6793.annot.gz", "D8_GSE14073",
        accession="GPL6793",
        note="GEO curated platform annotation: probe id to gene symbol for "
             "the Rosetta/Merck Human RSTA custom array")
P.fetch("https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL6nnn/GPL6793/soft/"
        "GPL6793_family.soft.gz", "data/raw/GPL6793_family.soft.gz",
        "D8_GSE14073", accession="GPL6793",
        note="platform SOFT table, the submitter's own probe annotation; "
             "fallback if the curated .annot is not served")
