"""Hash and record every literature-derived file the sequence table rests on."""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool import provenance as P  # noqa: E402

REC = [
 ("data/lit/garcia2011/nsmb2115_MOESM7.xlsx",
  "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnsmb.2115/MediaObjects/41594_2011_BFnsmb2115_MOESM7_ESM.xlsx",
  "Garcia DM et al., Nat Struct Mol Biol 2011;18:1139-1146, "
  "doi:10.1038/nsmb.2115, Supplementary Table (MOESM7). Sheet '175 "
  "microarrays analyzed' gives guide-strand sequence, seed 2-8 and "
  "7mer-m8 site per GEO array accession; 66 rows are GSE5814. PRIMARY "
  "SOURCE OF siRNA SEQUENCES."),
 ("data/lit/jackson2003/nbt831_MOESM2.pdf",
  "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnbt831/MediaObjects/41587_2003_BFnbt831_MOESM2_ESM.pdf",
  "Jackson AL et al., Nat Biotechnol 2003;21:635-637, "
  "doi:10.1038/nbt831, Supplementary Table 1: MAPK14 and IGF1R siRNA "
  "sense strands, plus the luciferase control duplex. Corroborates the "
  "MAPK14-193 sense strand as the reverse complement of the Garcia "
  "guide strand."),
 ("data/lit/sigoillot/srep00428-s1.xls",
  "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3361704/supplementaryFiles",
  "Sigoillot FD et al., Sci Rep 2012;2:428, PMC3361704, Supplementary "
  "Dataset 1. Independent source of PIK3CB siRNA sense strands with GEO "
  "mapping."),
 ("data/lit/GSE5814_RAW.tar",
  "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/suppl/GSE5814_RAW.tar",
  "GEO supplementary archive for GSE5814. Inspected: contains only "
  "GPL3992_feature_ids_locations.txt.gz. NO siRNA sequences."),
]
for path, url, note in REC:
    ab = os.path.join(P.ROOT, path)
    if os.path.exists(ab):
        P.record({"dataset": "D1_sirna_sequences", "status": "OK",
                  "kind": "literature_supplementary", "url": url,
                  "path": path, "bytes": os.path.getsize(ab),
                  "sha256": P.sha256_file(ab), "note": note})
        print("recorded", path)
    else:
        P.record({"dataset": "D1_sirna_sequences", "status": "FAILED",
                  "url": url, "path": path, "bytes": None, "sha256": None,
                  "note": note, "error": "file not present on disk"})
        print("MISSING", path)

FAILS = [
 ("https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/fullTextXML", 404,
  "Jackson 2006 RNA full text, the paper GSE5814 accompanies."),
 ("https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/supplementaryFiles", 200,
  "returned errorBean 'not open access'; no supplementary retrieved"),
 ("https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC1484447", 404,
  "not in the PMC open-access subset"),
 ("https://rnajournal.cshlp.org/content/12/7/1179/suppl/DC1", 403,
  "publisher supplementary blocked by Cloudflare"),
 ("https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/matrix/"
  "GSE5814_series_matrix.txt.gz", 404,
  "no combined series matrix; per-platform matrices used instead"),
]
for url, code, note in FAILS:
    P.record({"dataset": "D1_sirna_sequences", "status": "FAILED", "url": url,
              "http_status": code, "path": None, "bytes": None,
              "sha256": None, "note": note,
              "error": f"HTTP {code} / no machine-readable content",
              "consequence":
                  "siRNA sequences could not be obtained from the primary "
                  "publication; the Garcia 2011 supplementary table was used "
                  "instead and is independently corroborated by seeds.py"})
print("recorded failures")
