"""
D7 - Caffrey et al. 2011 dose series (the e9 substrate).

  Caffrey DR, Zhao J, Song Z, Schaffer ME, Haney SA, Subramanian RR,
  Seymour AB, Hughes JD. "siRNA off-target effects can be reduced at
  concentrations that match their individual potency." PLoS ONE 2011;
  6(7):e21503. PMC3130022.

The accession is not guessed. The paper's Methods state, verbatim:

  "Off-targets were assessed using the Affymetrix gene expression platform
   and all data is MIAME compliant and available at GEO (GSE28786)."

read from https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3130022/fullTextXML
which is fetched and recorded here so the claim is checkable from the ledger
rather than from this docstring.

Every URL attempted is recorded with its HTTP status, successes and failures
alike, including the ones known to fail: the PMC OA service does not serve
this ID, and GEO's human-facing accession page is behind a CAPTCHA. Both are
recorded because "we tried and it 404ed" is a fact about the world.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import provenance as P  # noqa: E402

GEO = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE28nnn/GSE28786"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
PLOS = ("https://journals.plos.org/plosone/article/file"
        "?id=10.1371/journal.pone.0021503.s{n}&type=supplementary")

print("### D7  paper full text (the accession statement itself)")
P.fetch(f"{EPMC}/PMC3130022/fullTextXML",
        "data/lit/caffrey2011/PMC3130022_fulltext.xml", "D7_caffrey2011",
        accession="PMC3130022",
        note="Europe PMC full text; the Methods sentence naming GSE28786 is "
             "the sole accession statement in the article",
        volatile=True)

print("\n### D7  GEO GSE28786 (the deposited matrix)")
P.fetch(f"{GEO}/matrix/GSE28786_series_matrix.txt.gz",
        "data/raw/GSE28786_series_matrix.txt.gz", "D7_GSE28786",
        accession="GSE28786",
        note="normalised log2 expression matrix, 54 samples on GPL9324 "
             "(Affymetrix HG-U133 Plus 2.0 with the Brainarray v11 "
             "hgu133plus2hsentrezg custom CDF); sample titles carry construct "
             "and dose")
P.fetch(f"{GEO}/suppl/filelist.txt", "data/raw/GSE28786_filelist.txt",
        "D7_GSE28786", accession="GSE28786",
        note="supplementary file listing for the series")
P.fetch(f"{GEO}/soft/GSE28786_family.soft.gz",
        "data/raw/GSE28786_family.soft.gz", "D7_GSE28786",
        accession="GSE28786",
        note="SOFT family: platform table for GPL9324 plus every sample "
             "characteristic; the source for dose and construct assignment")

print("\n### D7  Entrez gene id -> symbol, to join the custom CDF to GENCODE")
P.fetch("https://ftp.ncbi.nlm.nih.gov/gene/DATA/GENE_INFO/Mammalia/"
        "Homo_sapiens.gene_info.gz",
        "data/raw/Homo_sapiens.gene_info.gz", "D7_entrez_gene_info",
        note="NCBI Gene: GeneID to official symbol. The GPL9324 probeset "
             "identifiers are Entrez gene ids, so this is what maps the "
             "matrix onto the GENCODE symbols the rest of the pipeline uses")

print("\n### D7  supplementary tables (recorded as the fallback the brief "
      "allows, and as evidence of what the article itself publishes)")
for n, what in (("014", "Table S1: STAT3-1676 immune-response off-targets, "
                        "log2 fold change at 25, 10 and 1 nM"),
                ("016", "Table S3: HK2-3581 immune-response off-targets, "
                        "log2 fold change at 25, 10 and 1 nM"),
                ("018", "Table S5: HK2-3581 cell-cycle off-targets, "
                        "log fold change at 25, 10 and 1 nM"),
                ("020", "Table S7: HK2-3581M cell-cycle off-targets, "
                        "log fold change at 25, 10 and 1 nM")):
    P.fetch(PLOS.format(n=n), f"data/lit/caffrey2011/pone.0021503.s{n}.doc",
            "D7_caffrey2011_suppl", accession="PMC3130022", note=what)

print("\n### D7  attempts recorded as failures (tried, did not work)")
P.fetch("https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC3130022",
        "data/lit/caffrey2011/oa_fcgi_PMC3130022.xml", "D7_caffrey2011",
        accession="PMC3130022",
        note="PMC open-access web service; recorded because it does not "
             "serve this identifier and the failure belongs in the ledger")
print("\n### downloads finished")
