"""
Literature acquisition. Closes the reproduction loop.

The repository does not redistribute publisher PDFs, supplementary
spreadsheets or archives. It records where each one came from and fetches it
on demand. This script is what turns data/lit/SOURCES.txt and
data/lit/constants/CONSTANTS_SOURCES.md from documentation into something a
reader can re-run.

One file is REQUIRED, because sirna.py reads it: the Garcia et al. 2011
supplementary table that lists the guide-strand sequence of every GSE5814
array by GEO accession. Everything else is evidence for a number quoted in
data/constants.json, and a failure to fetch it is recorded rather than raised.

Every fetch goes through provenance.fetch, so a URL that has rotted is written
into data/PROVENANCE.json as a FAILED record with its HTTP status. That is the
point: link rot is a fact about the world and belongs in the ledger.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import provenance as P  # noqa: E402

SPRINGER = "https://media.springernature.com/original/springer-static/esm"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"

REQUIRED = [
    (f"{SPRINGER}/art%3A10.1038%2Fnsmb.2115/MediaObjects/"
     "41594_2011_BFnsmb2115_MOESM7_ESM.xlsx",
     "data/lit/garcia2011/nsmb2115_MOESM7.xlsx",
     "D1_sirna_sequences",
     "Garcia DM, Baek D, Shin C, Bell GW, Grimson A, Bartel DP. Nat Struct "
     "Mol Biol 2011;18:1139-1146. doi:10.1038/nsmb.2115. Supplementary table "
     "MOESM7, sheet '175 microarrays analyzed': guide-strand sequence, seed "
     "2-8 and 7mer-m8 site per GEO array accession. 66 rows are GSE5814. "
     "REQUIRED: src/riscpool/sirna.py reads this file."),
]

EVIDENCE = [
    (f"{SPRINGER}/art%3A10.1038%2Fnbt831/MediaObjects/"
     "41587_2003_BFnbt831_MOESM2_ESM.pdf",
     "data/lit/jackson2003/nbt831_MOESM2.pdf", "D1_sirna_sequences",
     "Jackson AL et al. Nat Biotechnol 2003;21:635-637. Supplementary Table "
     "1, MAPK14 sense strands. Corroborates the MAPK14-193 sense strand as "
     "the reverse complement of the Garcia guide strand."),
    (f"{EPMC}/PMC3361704/supplementaryFiles",
     "data/lit/PMC3361704_suppl.zip", "D1_sirna_sequences",
     "Sigoillot FD et al. Sci Rep 2012;2:428. Supplementary Dataset 1, an "
     "independent source of the PIK3CB siRNA sense strands with GEO mapping."),
    ("https://europepmc.org/articles/PMC3323880?pdf=render",
     "data/lit/constants/wang2012_genesdev_PMC3323880.pdf", "D6_constants",
     "Wang D et al. Genes Dev 2012;26:693-704. Source of the 1.4e5-1.7e5 "
     "TOTAL Argonaute copy number, in mouse epidermis and WM239A melanoma."),
    ("https://europepmc.org/articles/PMC3479394?pdf=render",
     "data/lit/constants/janas2012_PMC3479394.pdf", "D6_constants",
     "Janas MM et al. RNA 2012;18:2041-2055. The HeLa measurement, ~15,000 "
     "Ago1-4 per cell by AQUA mass spectrometry."),
    ("https://europepmc.org/articles/PMC3504684?pdf=render",
     "data/lit/constants/rna_errata_PMC3504684.pdf", "D6_constants",
     "ERRATA. RNA 2012;18:2345. Confirms Janas misquoted Wang tenfold as "
     "printed, and that both measurements are real."),
    (f"{EPMC}/PMC3941114/fullTextXML",
     "data/lit/constants/marinov2014_PMC3941114.xml", "D6_constants",
     "Marinov GK et al. Genome Res 2014;24:496-510. Spike-in calibrated "
     "50,000-300,000 mRNA molecules per cell."),
    ("https://pmc.ncbi.nlm.nih.gov/articles/PMC3595543/",
     "data/lit/constants/wee2012_PMC3595543.html", "D6_constants",
     "Wee LM, Flores-Jasso CF, Salomon WE, Zamore PD. Cell 2012;151:1055-"
     "1067. Seed-match Kd 26 pM and fully complementary Kd 20 pM for mouse "
     "AGO2-RISC; anchors the absolute affinity scale."),
    ("https://www.qiagen.com/us/resources/faq"
     "?id=06a192c2-e72d-42e8-9b40-3171e1eb4cb8&lang=en",
     "data/lit/constants/qiagen_faq_rna_per_cell.html", "D6_constants",
     "The actual origin of the widely repeated '360,000 mRNA per cell' "
     "figure: a vendor FAQ with no citation. Recorded because the repository "
     "REJECTS this number, and the rejection needs evidence too."),
    ("https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/suppl/"
     "GSE5814_RAW.tar", "data/lit/GSE5814_RAW.tar", "D1_sirna_sequences",
     "GEO supplementary archive for GSE5814. Inspected and found to contain "
     "only GPL3992_feature_ids_locations.txt.gz. Recorded to document that "
     "the deposit contains NO siRNA sequences."),
]


# Sources measured to be NOT byte-stable. Re-fetched during the build; the
# server returned different bytes for the same URL. Their SHA256 is recorded
# but not enforced, and the durable record of what they said is the verbatim
# quotation in data/lit/constants/CONSTANTS_SOURCES.md. Europe PMC has no
# fullTextXML and no PDF render for PMC3595543, so no stable form exists.
VOLATILE = [
    ("data/lit/constants/wee2012_PMC3595543.html",
     "server-side rendering of a PMC article page; re-fetching the same URL "
     "during this build returned different bytes. Europe PMC returns 404 for "
     "both fullTextXML and pdf=render for PMC3595543, so no byte-stable form "
     "of this source exists. The verbatim Kd sentences quoted in "
     "data/lit/constants/CONSTANTS_SOURCES.md are the durable record."),
]


def main():
    ok = fail = 0
    print("### required")
    for url, dest, ds, note in REQUIRED:
        p = P.fetch(url, dest, ds, note=note)
        if p is None:
            print("\nFATAL: the required Garcia 2011 supplementary table "
                  "could not be fetched. src/riscpool/sirna.py cannot run "
                  "without it and no substitute exists. The failure is "
                  "recorded in data/PROVENANCE.json.")
            return 1
        ok += 1
    print("\n### evidence")
    for url, dest, ds, note in EVIDENCE:
        if P.fetch(url, dest, ds, note=note) is None:
            fail += 1
        else:
            ok += 1
    print("\n### stability annotation")
    for path, reason in VOLATILE:
        n = P.set_stability(path, "volatile", reason)
        print(f"[prov] volatile  {path}  ({n} record(s))")
    print(f"\n{ok} fetched, {fail} failed (failures recorded in "
          f"data/PROVENANCE.json)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
