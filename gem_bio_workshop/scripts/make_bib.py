"""
paper/refs.bib, built by looking every reference up rather than typing it.

Rule Zero is about numbers, but a citation invented from memory is the same
failure mode: a plausible-looking string with nothing behind it. So every
entry here is fetched from Europe PMC or Crossref, and each lookup declares in
advance a phrase that must appear in the returned title. If the phrase is
absent the entry is REJECTED and reported, never written to the bib. The
lookup log is written next to the bib so a reader can see what was asked and
what came back.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool.provenance import ROOT, utcnow          # noqa: E402

OUT_BIB = os.path.join(ROOT, "paper", "refs.bib")
OUT_LOG = os.path.join(ROOT, "paper", "refs_lookup.json")
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
CROSSREF = "https://api.crossref.org/works/"
UA = {"User-Agent": "riscpool-build/1.0 (research)"}

# (bibkey, europepmc query, phrase that MUST appear in the returned title)
REFS = [
    # --- the datasets ---
    ("jackson2003", "EXT_ID:12754523",
     "Expression profiling reveals off-target gene regulation by RNAi"),
    ("jackson2006seed", "EXT_ID:16682560",
     "seed region sequence complementarity"),
    ("jackson2006chem", "EXT_ID:16682562",
     "Position-specific chemical modification"),
    ("birmingham2006", "EXT_ID:16489337",
     "seed matches, but not overall identity"),
    ("anderson2008", "PMCID:PMC2327361", "seed complement frequency"),
    ("caffrey2011", "PMCID:PMC3130022",
     "Concentrations That Match Their Individual Potency"),
    ("burchard2009", "EXT_ID:19144911", "species specific"),
    ("garcia2011", 'DOI:"10.1038/nsmb.2115"', "Weak seed-pairing stability"),
    ("huesken2005", 'TITLE:"Design of a genome-wide siRNA library using an '
                    'artificial neural network"',
     "genome-wide siRNA library using an artificial neural network"),
    ("sigoillot2012", "PMCID:PMC3361704", "off-target"),
    ("vandongen2008", "PMCID:PMC2635553", "Detecting microRNA binding and "
                                          "siRNA off-target effects"),
    ("schwarz2006", "EXT_ID:16965178", "single nucleotide"),
    # --- the biophysics the calibration rests on ---
    ("wee2012", "PMCID:PMC3595543",
     "Argonaute divides its RNA guide into domains"),
    ("salomon2015", "PMCID:PMC4503223",
     "Single-Molecule Imaging Reveals that Argonaute"),
    ("wang2012", "PMCID:PMC3323880", "Quantitative functions of Argonaute"),
    ("janas2012", "PMCID:PMC3479394",
     "binding and repression of microRNA-mRNA duplexes by human Ago"),
    ("marinov2014", "PMCID:PMC3941114",
     "From single-cell to cell-pool transcriptomes"),
    ("bosson2014", "PMCID:PMC5048918",
     "Endogenous miRNA and target concentrations determine"),
    ("stalder2013", "PMCID:PMC3630355",
     "central nucleation site of siRNA-mediated RNA silencing"),
    ("denzler2014", 'TITLE:"Assessing the ceRNA hypothesis with quantitative '
                    'measurements of miRNA and target abundance"',
     "ceRNA hypothesis"),
    ("denzler2016", 'TITLE:"Impact of MicroRNA Levels, Target-Site '
                    'Complementarity, and Cooperativity on Competing '
                    'Endogenous RNA-Regulated Gene Expression"',
     "Competing Endogenous RNA"),
    ("khan2009", "PMCID:PMC2782465",
     "Transfection of small RNAs globally perturbs gene regulation"),
    ("arvey2010", 'TITLE:"Target mRNA abundance dilutes microRNA and siRNA '
                  'activity"', "dilutes microRNA and siRNA activity"),
    ("grimson2007", 'TITLE:"MicroRNA targeting specificity in mammals: '
                    'determinants beyond seed pairing"',
     "determinants beyond seed pairing"),
    ("bartel2018", 'TITLE:"Metazoan MicroRNAs"', "Metazoan MicroRNAs"),
    # --- tools and resources ---
    ("lorenz2011", 'TITLE:"ViennaRNA Package 2.0"', "ViennaRNA Package 2.0"),
    ("bernhart2006", 'TITLE:"Local RNA base pairing probabilities in large '
                     'sequences"', "Local RNA base pairing probabilities"),
    ("frankish2021", 'TITLE:"GENCODE 2021"', "GENCODE"),
    ("barrett2013", 'TITLE:"NCBI GEO: archive for functional genomics data '
                    'sets--update"', "NCBI GEO"),
    ("athar2019", 'TITLE:"ArrayExpress update - from bulk to single-cell '
                  'expression data"', "ArrayExpress"),
    ("sayers2026", 'TITLE:"Database resources of the national center for '
                   'biotechnology information"', "national center for "
                   "biotechnology information"),
    ("irizarry2003", 'TITLE:"Exploration, normalization, and summaries of '
                     'high density oligonucleotide array probe level data"',
     "high density oligonucleotide array probe level data"),
    ("dai2005", 'TITLE:"Evolving gene/transcript definitions significantly '
                'alter the interpretation of GeneChip data"',
     "alter the interpretation of GeneChip data"),
    ("bai2024", 'TITLE:"OligoFormer"', "OligoFormer"),
    # --- prior quantitative competition / off-target models -----------------
    ("loinger2012", 'TITLE:"Competition between small RNAs: a quantitative '
                    'view"', "Competition between small RNAs"),
    ("riba2017", 'TITLE:"Explicit Modeling of siRNA-Dependent On- and '
                 'Off-Target Repression Improves the Interpretation of '
                 'Screening Results"', "Off-Target Repression"),
]

# DOIs resolved through Crossref because they are not indexed in Europe PMC.
# Deliberately empty: the only candidate was the PyTorch paper, whose arXiv
# DOI Crossref does not serve and whose NeurIPS proceedings entry is not
# registered there either. Rather than write an entry that no lookup returned,
# the software is named in the text with the exact version from MANIFEST.json
# and carries no bibliography entry.
CROSSREF_REFS = []


def get_json(url, attempts=4):
    """Retry transient transport failures. A reference must be rejected for
    being wrong, not for a dropped TLS connection."""
    import time
    last = None
    for i in range(attempts):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.loads(r.read().decode("utf8", "replace")), \
                    getattr(r, "status", 200)
        except urllib.error.HTTPError:
            raise
        except Exception as exc:
            last = exc
            time.sleep(2 * (i + 1))
    raise last


def surname_first(a):
    """Europe PMC returns "Huesken D"; BibTeX needs "Huesken, D".

    Without the comma BibTeX reads "Huesken" as a given name and "D" as the
    surname, and the citation renders as "D et al.". The comma is the whole
    fix, but it has to be applied at the source or every citation in the
    paper is wrong in a way that is easy to miss.
    """
    a = a.strip()
    parts = a.split()
    if len(parts) < 2:
        return a
    return f"{' '.join(parts[:-1])}, {parts[-1]}"


def dedupe_authors(people):
    """Drop repeated names, keeping the first occurrence and the order.

    Europe PMC author strings occasionally repeat a name, which BibTeX
    faithfully typesets twice. It is a source-data defect rather than a
    formatting choice, so it is removed here, at the one place author lists
    are built, rather than by hand-editing the generated .bib.
    """
    seen, out = set(), []
    for a in people:
        k = re.sub(r"[^a-z]", "", a.lower())
        if k and k in seen:
            continue
        seen.add(k)
        out.append(a)
    return out


def norm(s):
    return re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower())


def epmc(query):
    u = (f"{EPMC}?query={urllib.parse.quote(query)}"
         f"&resultType=core&format=json&pageSize=5")
    d, status = get_json(u)
    hits = d.get("resultList", {}).get("result", [])
    return hits, u, status


def bib_from_epmc(key, r):
    authors = r.get("authorString", "").rstrip(".")
    people = dedupe_authors(
        [surname_first(a) for a in authors.split(",") if a.strip()])
    fields = {
        "author": " and ".join(people),
        "title": r.get("title", "").rstrip("."),
        "journal": r.get("journalInfo", {}).get("journal", {}).get("title")
                   or r.get("journalTitle", ""),
        "year": r.get("pubYear", ""),
        "volume": r.get("journalInfo", {}).get("volume", ""),
        "number": r.get("journalInfo", {}).get("issue", ""),
        "pages": r.get("pageInfo", ""),
        "doi": r.get("doi", ""),
    }
    return fields


def bib_from_crossref(key, doi):
    d, status = get_json(CROSSREF + urllib.parse.quote(doi))
    m = d["message"]
    people = [f"{a.get('given','')} {a.get('family','')}".strip()
              for a in m.get("author", [])]
    people = dedupe_authors(people)
    year = ""
    for k in ("published-print", "published-online", "created", "issued"):
        if k in m and m[k].get("date-parts"):
            year = str(m[k]["date-parts"][0][0])
            break
    fields = {
        "author": " and ".join(people),
        "title": (m.get("title") or [""])[0],
        "journal": (m.get("container-title") or [m.get("publisher", "")])[0],
        "year": year,
        "volume": m.get("volume", ""),
        "number": m.get("issue", ""),
        "pages": m.get("page", ""),
        "doi": m.get("DOI", ""),
    }
    return fields, CROSSREF + doi, status


SPECIALS = {"&": "\\&", "%": "\\%", "#": "\\#", "_": "\\_",
            "$": "\\$"}


def tex_escape(v):
    """Journal names carry ampersands ("Genes & Development") and titles carry
    per cent signs. Left raw they abort the LaTeX run inside the .bbl, which is
    a confusing place to debug, so they are escaped here at the source."""
    out = []
    for ch in str(v):
        out.append(SPECIALS.get(ch, ch))
    return "".join(out)


def emit(key, f):
    body = ",\n".join(f"  {k} = {{{tex_escape(v)}}}"
                       for k, v in f.items() if v)
    return f"@article{{{key},\n{body}\n}}\n"


def main():
    log, entries, rejected = [], [], []
    for key, query, expect in REFS:
        try:
            hits, url, status = epmc(query)
        except Exception as exc:
            log.append({"key": key, "query": query, "status": "ERROR",
                        "error": f"{type(exc).__name__}: {exc}"})
            rejected.append(key)
            continue
        chosen = None
        for h in hits:
            if norm(expect) in norm(h.get("title", "")):
                chosen = h
                break
        rec = {"key": key, "query": query, "url": url,
               "http_status": status, "n_hits": len(hits),
               "expected_title_phrase": expect,
               "returned_titles": [h.get("title", "") for h in hits[:3]]}
        if chosen is None:
            rec["status"] = "REJECTED_TITLE_MISMATCH"
            rejected.append(key)
            log.append(rec)
            continue
        f = bib_from_epmc(key, chosen)
        rec.update({"status": "OK", "matched_title": f["title"],
                    "pmid": chosen.get("pmid"), "pmcid": chosen.get("pmcid"),
                    "doi": f["doi"]})
        log.append(rec)
        entries.append(emit(key, f))

    for key, doi, expect in CROSSREF_REFS:
        try:
            f, url, status = bib_from_crossref(key, doi)
        except Exception as exc:
            log.append({"key": key, "doi": doi, "status": "ERROR",
                        "error": f"{type(exc).__name__}: {exc}"})
            rejected.append(key)
            continue
        rec = {"key": key, "query": doi, "url": url, "http_status": status,
               "expected_title_phrase": expect, "matched_title": f["title"]}
        if norm(expect) not in norm(f["title"]):
            rec["status"] = "REJECTED_TITLE_MISMATCH"
            rejected.append(key)
            log.append(rec)
            continue
        rec["status"] = "OK"
        log.append(rec)
        entries.append(emit(key, f))

    os.makedirs(os.path.dirname(OUT_BIB), exist_ok=True)
    with open(OUT_BIB, "w") as fh:
        fh.write("% Generated by scripts/make_bib.py. Every entry was fetched\n"
                 "% and its title checked against a phrase declared in advance.\n"
                 f"% Generated {utcnow()}. Lookup log: paper/refs_lookup.json\n\n")
        fh.write("\n".join(entries))
    with open(OUT_LOG, "w") as fh:
        json.dump({"generated_utc": utcnow(), "n_requested":
                   len(REFS) + len(CROSSREF_REFS), "n_written": len(entries),
                   "n_rejected": len(rejected), "rejected_keys": rejected,
                   "lookups": log}, fh, indent=2)
    print(f"wrote {OUT_BIB}: {len(entries)} entries, "
          f"{len(rejected)} rejected {rejected}")


if __name__ == "__main__":
    main()
