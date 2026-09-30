# Literature-sourced constants — provenance record

All numbers below were read out of a file downloaded or a web page fetched on **2026-09-04**
into `/home/shadi/GEM/data/lit/constants/`. Nothing here is quoted from memory.

Note on verbatim quotes taken from `pdftotext` output: the PDF text layer of the
Genes & Development and RNA papers renders the multiplication sign "×" as the digit
"3" and renders superscripts inline. So `1.4 3 105` in the extracted text is
`1.4 × 10^5` in the printed paper. This is flagged inline where it occurs.

---

## QUANTITY 1 — Argonaute protein copy number per cell

### 1A. PRIMARY (the paper the build brief was pointing at) — Wang et al., Genes Dev 2012

- **Value:** ~1.4 × 10^5 to 1.7 × 10^5 (140,000–170,000)
- **Units:** molecules per cell
- **What is being counted:** **TOTAL Argonaute (Ago1 + Ago2 + Ago3), not AGO2 alone.**
  This is a correction to the build brief, which attributed the figure to "AGO2".
- **Cell types:** mouse P4/P4.5 epidermis (skin keratinocytes) **and** human WM239A
  melanoma cells. **Not HeLa.**
- **Method:** absolute quantification by quantitative western blot against purified
  synthetic/recombinant His-tagged Ago1, Ago2, Ago3 standards (standard curves,
  ImageJ densitometry), assuming ~80% protein-extraction efficiency. Relative
  Ago1:Ago2:Ago3 ratios were independently determined by shotgun 2D-LC-MS/MS
  proteomics (spectral counting, IsoformResolver, 1% FDR).
- **Citation:** Wang D, Zhang Z, O'Loughlin E, Lee T, Houel S, O'Carroll D,
  Tarakhovsky A, Ahn NG, Yi R. "Quantitative functions of Argonaute proteins in
  mammalian development." *Genes Dev.* 2012;26(7):693–704.
- **DOI:** 10.1101/gad.182758.111
- **PMID:** 22474261 — **PMCID: PMC3323880** (the brief said PMC3323879; that is wrong,
  verified against the Europe PMC record)
- **URL read:** https://europepmc.org/articles/PMC3323880?pdf=render
  (Europe PMC record: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC3323880&format=json&resultType=core)
- **Local files:** `wang2012_genesdev_PMC3323880.pdf`, extracted text `wang2012.txt`
- **Verbatim, abstract (`wang2012.txt` line 26):**
  > "Finally, we measure the absolute expression of Argonaute proteins and determine
  > that their copy number is ~1.4 3 105 to 1.7 3 105 molecules per cell."
  (`3 105` = `× 10^5`)
- **Verbatim, Results (`wang2012.txt` lines 417–419):**
  > "Importantly, with the absolute quantification, we estimate (with ~80% efficiency
  > in protein extraction) that the total copy number of Argonaute proteins is
  > ~1.4 3 105 to 1.7 3 105 molecules per cell in mice and humans."
- **Verbatim, Discussion (`wang2012.txt` lines 565–570):**
  > "With an estimated 80% efficiency for protein extraction, we determined that the
  > total copy number of Argonautes is ~1.4 3 105 to 1.7 3 105 molecules per cell.
  > Because all mature miRNAs associate with Argonautes in a 1:1 manner, our estimate
  > likely represents an upper limit for the copy number of total mature miRNAs."
- **Supporting per-protein measurements, verbatim (`wang2012.txt` lines ~399–403):**
  > "We determined, for 0.5 3 106 cells, that 3.2 ng of Ago1 and 6.2 ng of Ago2 are
  > expressed in P4 epidermis and 1.7 ng of Ago1, 5.6 ng of Ago2, and 1.8 ng of Ago3
  > are expressed in WM239A cells."
  > "the ratio among Argonautes ... e.g., Ago1:Ago2 = 1.0:1.9 in the epidermis, and
  > Ago1:Ago2:Ago3 = 0.94:3.3:1.0 in WM239A cells"
- **Conversion factor given by the paper, verbatim (Materials and Methods, `wang2012.txt` line ~664):**
  > "For a half-million cells, 8 ng of Ago protein represents 1 3 105 molecules per cell."
- **Derived (arithmetic on the paper's own numbers, NOT stated in the paper — use with care):**
  AGO2 alone ≈ 6.2/8 × 10^5 ≈ 7.8 × 10^4 molecules/cell (mouse P4 epidermis) and
  ≈ 5.6/8 × 10^5 ≈ 7.0 × 10^4 molecules/cell (WM239A), before the 80% extraction
  correction. The paper never states an AGO2-only copy number.
- **Shotgun-proteomics ratio, verbatim (`wang2012.txt` lines 417–419):**
  > "We determined that the ratios among individual Argonautes, based on the normalized
  > SCs, were Ago1:Ago2:Ago3 = 1.0:3.6:1.0 (22:80:22)"

### 1B. CONFLICTING PRIMARY MEASUREMENT IN HeLa — Janas et al., RNA 2012

**This is the one measured in HeLa, and it disagrees with Wang 2012 by ~10-fold.**

- **Value:** ~15,000 Ago1–4 molecules per cell (paper's headline number; text also gives
  ~202,765 miRNA molecules per HeLa cell, a 13-fold excess of miRNA over Ago)
- **Units:** molecules per cell
- **Cell type:** **HeLa**
- **Method:** AQUA (absolute quantification) by tandem mass spectrometry, with known
  amounts of synthetic stable-isotope-labeled (heavy) tryptic peptide standards
  (YTPVGR covering all Agos; AVQVHQDTLR covering Ago1 + both Ago2 isoforms;
  DHQALAK specific to the two Ago2 isoforms) spiked into a gel-slice trypsin digest
  (85–110 kDa band).
- **Citation:** Janas MM, Wang B, Harris AS, Aguiar M, Shaffer JM, Subrahmanyam YVBK,
  Behlke MA, Wucherpfennig KW, Gygi SP, Gagnon E, Novina CD. "Alternative RISC
  assembly: binding and repression of microRNA–mRNA duplexes by human Ago proteins."
  *RNA.* 2012;18(11):2041–2055.
- **DOI:** 10.1261/rna.035675.112 — **PMID:** 23019594 — **PMCID:** PMC3479394
- **URL read:** https://europepmc.org/articles/PMC3479394?pdf=render
- **Local files:** `janas2012_PMC3479394.pdf`, extracted text `janas2012.txt`
- **Verbatim (`janas2012.txt` lines ~151–153):**
  > "Based on the integrated peak areas around the m/z of each light (endogenous Ago)
  > and heavy (spiked control) peptide, we determined that there are approximately
  > 15,000 Ago1–4 molecules per HeLa cell based on the YTPVGR peptide standard (Fig. 1D)."
- **Verbatim (`janas2012.txt` lines ~150–153):**
  > "Together, these absolute quantitations of miRNAs and Ago1–4 on a per cell basis
  > demonstrate that there is about a 13-fold excess of miRNA molecules (about 202,000)
  > relative to Ago 1–4 molecules (about 15,000) in a HeLa cell."
- **Verbatim (Discussion, `janas2012.txt` line ~579):**
  > "We determined the absolute number of miRNA molecules per HeLa cell to be 202,765,
  > demonstrating a 13-fold excess over Ago1–4 molecules."
- **Verbatim, Ago composition in HeLa (`janas2012.txt` line ~146):**
  > "Virtually the entire Ago population in a HeLa cell consists of Ago1 and Ago2 based
  > on the AVQVHQDTLR peptide standard, with ~40% representing Ago2 based on the
  > DHQALAK peptide standard (Fig. 1D)."
  → implies AGO2 in HeLa ≈ 0.4 × 15,000 ≈ 6,000 molecules/cell (derived arithmetic,
  not stated in the paper).

### 1C. PUBLISHED ERRATUM that resolves how the two papers relate

Janas 2012 as printed **misquoted Wang 2012 by a factor of 10**, and RNA published a
correction. This matters: anyone reading Janas 2012 alone will see "14,000–17,000" for
Wang, which is wrong.

- **Citation:** ERRATA. *RNA.* 2012;18(12):2345. (correcting RNA 18:2041–2055, 2012)
- **PMCID:** PMC3504684
- **URL read:** https://europepmc.org/articles/PMC3504684?pdf=render
- **Local files:** `rna_errata_PMC3504684.pdf`, text `rna_errata.txt`
- **Verbatim (whole relevant erratum):**
  > "In this article (page 2043), the authors incorrectly stated that Wang et al. (2012)
  > found 14,000–17,000 Ago1–4 molecules per cell in mouse melanocytes and human
  > melanoma cells when in fact they found 140,000–170,000 molecules per cell.
  > The authors apologize for any confusion this error may have caused but note this
  > does not change their results or the interpretation of their data."

**→ Net position for QUANTITY 1: the literature does NOT agree.** Total Ago is
140,000–170,000/cell in mouse epidermis and human WM239A melanoma (Wang 2012, western
blot vs. recombinant standards) but ~15,000/cell in HeLa (Janas 2012, AQUA MS). Both are
real primary measurements in different cell types by different methods. If the model is
HeLa-based, Janas 2012 (~1.5 × 10^4 total Ago, ~6 × 10^3 AGO2) is the cell-type-matched
number; the 1.4–1.7 × 10^5 figure is not a HeLa number.

### 1D. Cross-checks performed

- **Stalder L, Heusermann W, et al. EMBO J 2013;32(8):1115–1127** (DOI 10.1038/emboj.2013.52,
  PMCID PMC3630355; local `stalder2013_PMC3630355.xml`, text `stalder2013.txt`;
  URL https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3630355/fullTextXML).
  Does **not** independently measure Ago copy number. It cites Janas. Verbatim:
  > "Interestingly however, a recent publication (Janas et al, 2012) reports a conclusion
  > perfectly consistent with our quantitative data. Based on an absolute quantification
  > of Ago proteins and total miRNA copies per cell, the authors come to the conclusion
  > that there is a 13-fold excess of miRNA over Argonaute molecules in HeLa cells."
  What Stalder does measure (verbatim): "the IC50 of SSB mRNA knockdown is as little as
  35–40 molecules of siRISC per cell" and "for all of these siRNAs we find equally low
  numbers at IC50 ranging from 10 to 110 siRISC molecules per cell."
- **Bosson AD, Zamudio JR, Sharp PA. Mol Cell 2014;56(3):347–359** (DOI 10.1016/j.molcel.2014.09.018,
  PMCID PMC5048918; local `bosson2014_PMC5048918.html`, text `bosson2014.txt`;
  URL https://pmc.ncbi.nlm.nih.gov/articles/PMC5048918/).
  **Does NOT report an AGO protein copy number per cell.** The brief's expectation here is
  not supported. It reports miRNA and mRNA copies per cell (see Quantity 2 below) and
  "Total Ago Occupancy" as a normalized iCLIP ratio, not a molecule count.
- **BioNumbers**: searched "Argonaute copies per cell" at
  https://bionumbers.hms.harvard.edu/search.aspx?task=searchbytrmorid&trm=Argonaute+copies+per+cell
  — **no BNID exists for Argonaute/Ago protein copies per cell.** NOT AVAILABLE.
- **"Schmidt MF et al."** — could not be resolved to a specific paper from the brief's
  partial citation. **NOT CHECKED.**

---

## QUANTITY 2 — Total mRNA molecules per human cell

### THE ~360,000 FIGURE IS NOT TRACEABLE TO A PRIMARY SOURCE — DO NOT CITE IT AS ONE

- **Where it actually comes from:** a QIAGEN FAQ / RNA handbook page, which gives **no
  citation at all**, and which says "mammalian cell", not HeLa.
- **URL read:** https://www.qiagen.com/us/resources/faq?id=06a192c2-e72d-42e8-9b40-3171e1eb4cb8&lang=en
- **Local file:** `qiagen_faq_rna_per_cell.html`
- **Verbatim:**
  > "mRNA accounts for only 1–5% of the total cellular RNA although the actual amount
  > depends on the cell type and physiological state. Approximately 360,000 mRNA
  > molecules are present in a single mammalian cell, made up of approximately 12,000
  > different transcripts with a typical length of around 2 kb. Some mRNAs comprise 3%
  > of the mRNA pool whereas others account for less than 0.1%."
  > (same page: "a typical mammalian cell contains 10–30 pg total RNA")
- **Status: NOT VERIFIED as a primary measurement, and NOT HeLa-specific.** It is a
  vendor-handbook order-of-magnitude figure. It is *within* the range of the primary
  literature below, so it is not wrong, but it should not be cited as a measurement.

### The answer supported by primary literature is a RANGE, ~5 × 10^4 to ~1 × 10^6 mRNA/cell

No primary, HeLa-specific total-mRNA-per-cell measurement was found. Searches run:
BioNumbers ("mRNA molecules per cell HeLa", "mRNA per HeLa cell", "number of mRNA
molecules HeLa cell", "total mRNA molecules mammalian cell"), Europe PMC full-text
search, and web search. **HeLa-specific: NOT VERIFIED.**

| Value | Units | Cell type | Method | Source |
|---|---|---|---|---|
| ~80,000 mean; <50,000 to ~300,000 across single cells; 50,000–100,000 in pool/splits | mRNAs/cell | human GM12878 lymphoblastoid | SMART-seq scRNA-seq with spike-in standards; total from bulk RNA mass per known cell number + mean human mRNA length | Marinov 2014 (below) |
| 158,000 | protein-coding mRNA copies per cell (cpc) | mouse embryonic stem cells (TT-FHAgo2 ESC) | poly-A RNA-seq with synthetic spike-in RNAs, Cufflinks isoform quantification | Bosson 2014 (below) |
| 300,000 | molecules/cell | human, cell type unspecified | SAGE | Velculescu 1999 via BNID 104330 |
| 200,000 | mRNAs/cell | "typical mammalian cell" | review/secondary | Shapiro 2013 via BNID 109916 |
| ~100,000 – 1,000,000 | mRNAs/cell | "typical single mammalian cell" | review/secondary | Islam 2014 via BNID 111220 |
| 10^5 – 10^6 | mRNA/cell | mammalian cell of 3000 µm^3 | back-of-envelope estimate | Cell Biology by the Numbers (below) |

#### 2A. Marinov GK et al., Genome Res 2014 — GM12878, spike-in calibrated (best primary human number)

- **Citation:** Marinov GK, Williams BA, McCue K, Schroth GP, Gertz J, Myers RM,
  Wold BJ. "From single-cell to cell-pool transcriptomes: stochasticity in gene
  expression and RNA splicing." *Genome Res.* 2014;24(3):496–510.
- **DOI:** 10.1101/gr.161034.113 — **PMID:** 24299736 — **PMCID:** PMC3941114
- **URL read:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3941114/fullTextXML
- **Local files:** `marinov2014_PMC3941114.xml`, text `marinov2014.txt`
- **Verbatim (abstract):**
  > "By using spike-in quantification standards, we estimate the absolute number of RNA
  > molecules per cell for each gene and find significant variation in total mRNA
  > content: between 50,000 and 300,000 transcripts per cell."
- **Verbatim (Results, p.501):**
  > "Based on the average mass of RNA in each cell (derived from bulk RNA samples from a
  > known number of cells) and the average length of mRNAs in the human genome, we
  > estimated that each GM12878 cell contains, on average, ~80,000 mRNAs. However, we
  > observed striking cell-to-cell differences in the total transcript number of single
  > cells, with some cells expressing <50,000 mRNAs and others almost 300,000. In
  > contrast, pool/split experiments exhibited remarkable uniformity (between 50,000 and
  > 100,000 transcripts) and agree well with prior expectations."
- **Verbatim (caveat stated by the authors themselves):**
  > "The average total number of mRNA molecules in a single cell is not known for most
  > cell types, but it is expected to vary with cell size, metabolic status, and even
  > cell cycle phase."
- **BioNumbers entry for this:** BNID 111775, https://bionumbers.hms.harvard.edu/bionumber.aspx?id=111775
  (local `bn_111775.html`), value "~80,000 (from below 50,000 - to almost 300,000)
  mRNA molecules/cell".

#### 2B. Bosson AD et al., Mol Cell 2014 — mouse ESC, spike-in calibrated

- **Citation:** Bosson AD, Zamudio JR, Sharp PA. "Endogenous miRNA and target
  concentrations determine susceptibility to potential ceRNA competition."
  *Mol Cell.* 2014;56(3):347–359.
- **DOI:** 10.1016/j.molcel.2014.09.018 — **PMID:** 25449132 — **PMCID:** PMC5048918
- **URL read:** https://pmc.ncbi.nlm.nih.gov/articles/PMC5048918/
- **Local files:** `bosson2014_PMC5048918.html`, text `bosson2014.txt`
- **Verbatim:**
  > "To measure global target RNA concentrations, we performed poly-A RNA-seq with
  > synthetic spike-in RNAs and used transcript isoform levels estimated with Cufflinks
  > (Trapnell et al., 2010) because isoforms may differ in miRNA seed match content.
  > The total protein-coding mRNA content for ESCs was calculated at 158,000 cpc
  > (Figure S1B)."

#### 2C. BioNumbers entries (secondary; recorded because the brief asked for BNIDs)

- **BNID 104330** — "Number of mRNA molecules in cell", Human, **300000 molecules/cell**.
  URL https://bionumbers.hms.harvard.edu/bionumber.aspx?id=104330 (local `bn_104330.html`).
  Reference recorded there: Velculescu VE, Madden SL, Zhang L, et al. "Analysis of human
  transcriptomes." *Nat Genet.* 1999 Dec;23(4):387–8, p.387 right column bottom paragraph.
  PMID 10581018. **Note: this is Nat Genet 1999, NOT the Cell 1997 paper named in the
  brief.** BioNumbers' own caveat, verbatim:
  > "According to author, Cell lines were grown in standard tissue culture conditions
  > (personal communication). No specific cell type is mentioned, value is given in the
  > context of the development of the SAGE method that enables good coverage of transcripts."
- **BNID 109916** — "Number of mRNA molecules in a typical single mammalian cell",
  **200000 mRNAs/cell**. https://bionumbers.hms.harvard.edu/bionumber.aspx?id=109916
  (local `bn_109916.html`). Reference: Shapiro E, Biezuner T, Linnarsson S.
  *Nat Rev Genet.* 2013;14(9):618–30, p.623 box, top paragraph. PMID 23897237.
  Verbatim comment: "a fairly typical single mammalian cell [contains] 200,000 mRNA molecules."
  **This is a review, i.e. secondary.**
- **BNID 111220** — "Number of mRNA molecules in a typical single cell", Mammals,
  **~100,000 – 1,000,000 mRNAs/cell**. https://bionumbers.hms.harvard.edu/bionumber.aspx?id=111220
  (local `bn_111220.html`). Reference: Islam S. et al. "Quantitative single-cell RNA-seq
  with unique molecular identifiers." *Nat Methods.* 2014;11(2):163–6.
  DOI 10.1038/nmeth.2772, p.163 right column 2nd paragraph. PMID 24363023.
  Verbatim comment: "Approximately 10^5–10^6 mRNA molecules are present in a typical
  single mammalian cell, and up to 10,000 different genes may be expressed."
- **No BioNumbers entry exists for total mRNA per HeLa cell.** Searched
  https://bionumbers.hms.harvard.edu/search.aspx?task=searchbytrmorid&trm=mRNA+per+HeLa+cell
  and three other phrasings. NOT AVAILABLE.

#### 2D. Cell Biology by the Numbers (Milo & Phillips) — textbook estimate

- **URL read:** http://book.bionumbers.org/how-many-mrnas-are-in-a-cell/
- **Local file:** `cbbn_mrna.html`
- **Verbatim:**
  > "As shown in this back of the envelope calculation we can derive an estimate for
  > rapidly dividing cells of 10^3-10^4 mRNA per bacterial cell and 10^5-10^6 mRNA per
  > the 3000 μm^3 characteristic size of a mammalian cell."
  > "For 'typical' mammalian cells a quoted value of 200,000 mRNA per cell (BNID 109916)
  > is in line with our simple estimate above and shows that scaling the number of mRNA
  > proportionally with size and growth rate seems to be a useful first guess."

**→ Recommended constant for QUANTITY 2:** report the range **5 × 10^4 – 3 × 10^5
mRNA/cell** if you want a spike-in-calibrated human measurement (Marinov 2014, GM12878),
or **10^5 – 10^6 mRNA/cell** for the broader mammalian range (Islam 2014 / CBBN). A
single point value of 360,000 for HeLa is **NOT VERIFIED** against any primary source.

---

## QUANTITY 3 — Kd of Ago2-RISC for seed-matched vs. fully complementary targets

### PRIMARY SOURCE — Wee, Flores-Jasso, Salomon & Zamore, Cell 2012

- **Citation:** Wee LM, Flores-Jasso CF, Salomon WE, Zamore PD. "Argonaute divides its
  RNA guide into domains with distinct functions and RNA-binding properties."
  *Cell.* 2012;151(5):1055–1067.
- **DOI:** 10.1016/j.cell.2012.10.036 — **PMID:** 23178124 — **PMCID:** PMC3595543
- **URL read:** https://pmc.ncbi.nlm.nih.gov/articles/PMC3595543/
- **Local files:** `wee2012_PMC3595543.html`, text `wee2012.txt`
- **Guide:** let-7 siRNA. **Temperature: 25 °C.**
- **Preparations:** mouse AGO2-RISC assembled in S100 from immortalized Ago2−/− MEFs
  expressing mouse AGO2; fly Ago2-RISC assembled in 0–2 hr Drosophila embryo lysate.
- **Method verbatim (Experimental Procedures):**
  > "Ago2-RISC was assembled with let-7 siRNA in 0–2 hr embryo lysate or S100 from
  > immortalized Ago2−/− MEFs expressing mouse AGO2 (O'Carroll et al., 2007). Binding
  > reactions were at 25°C for 1 hr; protein-RNA complexes were captured on
  > nitrocellulose and unbound RNA on Nylon membranes under vacuum and washed with
  > ice-cold buffer. Competition reactions were at 25°C for 1 hr (mouse) or 6 hr (fly)."

**Mouse AGO2-RISC (the mammalian numbers — use these):**

| Target | K_D | Source sentence |
|---|---|---|
| seed-matching (g2–g8, 7-mer seed pairing only) | **26 ± 2 pM** | direct binding assay, Figure 6C |
| seed + 3′ supplementary pairing | **13 ± 1 pM** | direct binding assay, Figure 6C |
| fully complementary | **20 ± 10 pM** (ΔG_25°C ≈ −15 kcal mol⁻¹) | direct binding assay, Figures 3D/6C |

- **Verbatim (mouse):**
  > "Moreover, direct binding assays found no substantive difference in affinity between
  > a seed-matching (K D = 26 ± 2 pM) and a fully complementary target (20 ± 10 pM;
  > Figure 6C). We did observe a small but significant (p value = 3.2 × 10−4) increase
  > in affinity for a target with seed and 3′ supplementary pairing (k D = 13 ± 1 pM),
  > compared to the affinity of a target with seed pairing alone."
- **Verbatim (fully complementary, both species):**
  > "the binding affinity of fly Ago2-RISC (k D = 3.7 ± 0.9 pM, mean ± S.D.;
  > Δ G 25°C − 16 kcal mol−1) and mouse AGO2-RISC (k D = 20 ± 10 pM, mean ± S.D.;
  > Δ G 25°C − 15 kcal mol−1; see below) for a fully complementary target was comparable
  > to that of a 10 bp RNA:RNA helix."
- **Verbatim (the paper's own summary of seed-only K_D for both species, Discussion):**
  > "Both miRNAs are present at a concentration greater than the K D we measured for seed
  > matched targets for fly (~210 pM) or mouse (~26 pM) Ago2-RISC."

**Fly Ago2-RISC (for contrast — do NOT use for a mammalian model):**
- fully complementary: **3.7 ± 0.9 pM**
- seed-only: **~210 pM**; verbatim: "a target complementary only to the seed bound 80
  times less tightly" (than the fully complementary target)
- g4g5 seed mismatch: K_D 2.3 ± 0.6 nM by equilibrium competition (5.2 nM from k_on/k_off)

**Important caveats read out of the paper:**
- K_M is NOT K_D here. Verbatim: "The K D measured in our binding assay (3.7 ± 0.9 pM)
  was ~270-fold smaller than the K M (1.0 ± 0.2 nM) determined with purified fly Ago2."
  For mouse: "the K D for mouse AGO2 (20 ± 10 pM) was only ~5-fold smaller than the K M
  (0.10 ± 0.06 nM)".
- These K_D values are for a **fully accessible, unstructured, modified oligo target in
  lysate at 25 °C**, not an mRNA in a cell. Applying them directly as an absolute
  in-cell scale will overestimate affinity.
- This article carries a published correction: the PMC record states "This article has
  been corrected. See the correction in volume 152 on page 366." The content of that
  correction was **NOT retrieved** (Europe PMC has no indexed record for it). Check
  Cell 2013;152(1–2):366 before relying on any single value here.

### Cross-check — Salomon et al., Cell 2015 (PARTIAL / NOT VERIFIED for K_D)

- **Citation:** Salomon WE, Jolly SM, Moore MJ, Zamore PD, Serebrov V. "Single-Molecule
  Imaging Reveals that Argonaute Reshapes the Binding Properties of Its Nucleic Acid
  Guides." *Cell.* 2015;162(1):84–95.
- **DOI:** 10.1016/j.cell.2015.06.029 — **PMID:** 26140592 — **PMCID:** PMC4503223
  (note: the brief gave PMC4503223, which resolves correctly)
- **URL read:** https://pmc.ncbi.nlm.nih.gov/articles/PMC4503223/
- **Local files:** `salomon2015_PMC4503223.html`, text `salomon2015.txt`
- **What was verified verbatim:** ensemble K_M and k_cat for mouse AGO2 + let-7a:
  > "standard ensemble experiments found similar K M (1.7 ± 0.1 nM vs. 1.2 ± 0.2 nM) and
  > k cat (7.8 ± 0.2 × 10−2 sec−1 vs. 6.6 ± 0.4 × 10−2 sec−1) values for unmodified and
  > 3′ Alexa555-labeled guides"
- **Also verified verbatim (protein-free RNA:RNA reference points, for the ΔG scale):**
  > "a fully base-paired double-stranded RNA composed of let-7a and its complement is
  > predicted to have a K D = 6.3 × 10−7 nM, implying a k off = 5.7 × 10−9 s−1
  > (τ = ~5.6 years). In contrast, an 8-bp duplex formed with just the let-7a seed
  > sequence is unstable: the predicted K D = 56 μM implies a k off = 52 s−1 (τ = ~20 msec)."
- **A seed-match K_D value could NOT be found in the retrieved body text of this paper.**
  Salomon 2015 reports single-molecule k_on/k_off; any K_D is in figures/tables not
  present in the HTML text layer. **NOT VERIFIED.**
- **Chandradoss SD et al., Cell 2015;162(1):96–107 — NOT CHECKED.**

---

## QUANTITY 4 — HeLa cell volume

**Answer is a range: ~1,200 – 5,000 µm³ (≈ 1.2 – 5.0 pL) whole cell, with most-cited
central values 2,400–3,700 µm³ (2.4 – 3.7 pL).** Sources genuinely disagree, largely
by method and by whether the cell is rounded (trypsinized) or spread.

Note unit identity: 1 µm³ = 1 fL = 10⁻³ pL, so 3,000 µm³ = 3 pL.

| Value | Units | Method | BNID | Primary source |
|---|---|---|---|---|
| 4,400–5,000 | µm³ | Coulter counter + electronic particle size analyser, log-phase monolayer | 103719 | Cohen & Studzinski 1967 |
| 2,425 (range 1,198–4,290); also 2,600 quoted in-text | µm³ | light-microscope radius 10.5 ± 2.2 µm (n = 24), half-sphere on microbeads | 103725 | Zhao et al. 2008 |
| 3,700 ± 1,500 (human serum); 5,000 ± 1,900 (porcine serum) | µm³ | microscopic diameter of trypsinized rounded live cells, ≥20 cells | 105879 | Puck, Marcus & Cieciura 1956 |
| 2,600 | µm³ | typical 3-day-old HeLa | 109386 | Luciani et al. 2001 (via Finka & Goloubinoff 2013) |
| median 1.6 ± 0.7 pL; max 4.4 pL | pL (cytoplasmic only) | FluidFM single-cell extraction | 112928 | Guillaume-Gentil et al. 2016 |

Details, each read from its BioNumbers page:

- **BNID 103719** — https://bionumbers.hms.harvard.edu/bionumber.aspx?id=103719
  (local `bn_103719.html`). "HeLa cell volume — Range 4400-5000 µm^3".
  Ref: Cohen LS, Studzinski GP. *J Cell Physiol.* 1967 Jun;69(3):331–9, p.336 table 3.
  PMID 4230858. Method verbatim: "Cell number was obtained with a Coulter counter, while
  cell sizing was performed with the automatic particle size distribution analyser Model
  J Electronic Co., Hialeah, Fla."
- **BNID 103725** — https://bionumbers.hms.harvard.edu/bionumber.aspx?id=103725
  (local `bn_103725.html`). "HeLa cell volume — Value 2425 µm^3, Range: 1198-4290 µm^3".
  Ref: Zhao L, Kroenke CD, Song J, Piwnica-Worms D, Ackerman JJ, Neil JJ. *NMR Biomed.*
  2008 Feb;21(2):159–64. PMID 17461436. Comment verbatim: "Researchers measured 24 cells
  and got a radius of 10.5±2.2 µm (mean ±SD), personal communication with author (Jeff
  Neil). The cells are a half sphere in culture, so the radius can be used to calculate a
  volume (mean 2,425µm^3 range 1,198-4,290µm^3). For value of 2600 µm^3 see ref p.6 4th
  paragraph: 'The HeLa cell volume is 2.6 × 10^3 μm^3 as estimated from the cell diameter
  measured under the light microscope.'"
- **BNID 105879** — https://bionumbers.hms.harvard.edu/bionumber.aspx?id=105879
  (local `bn_105879.html`). "Volume of HeLa cell — Value 3700 µm^3, Range: ±1,500 µm^3".
  Ref: Puck TT, Marcus PI, Cieciura SJ. *J Exp Med.* 1956 Feb 1;103(2):273–83, p.280
  table I. PMID 13286432. Method verbatim: "Cell volumes were determined by microscopic
  measurement of the diameters of the spherical cells resulting from mild trypsinization.
  Living cells were employed in all these determinations, and measurements were repeated
  on at least 20 different cells of each type." Comment verbatim: "Volume for cells in
  human serum. Volume of cell in porcine serum was 5,000±1,900µm^3."
- **BNID 109386** — https://bionumbers.hms.harvard.edu/bionumber.aspx?id=109386
  (local `bn_109386.html`). "Average volume of typical 3 day old HeLa cell — 2600 μm^3".
  Reference: Finka A, Goloubinoff P. *Cell Stress Chaperones.* 2013, p.3 right column
  2nd paragraph (PMID 23430704); **primary source**: Luciani AM, Rosi A, Matarrese P,
  Arancia G, Guidoni L, Viti V. *Eur J Cell Biol.* 2001 Feb;80(2):187–95, PMID 11302524.
  Comment verbatim: "...an average volume of 2,600 µm^3 for typical 3-day-old HeLa cells
  was from primary source."
- **BNID 112928** — https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112928
  (local `bn_112928.html`). "Native cytoplasmic volume in HeLa cell — maximum 4.4 pL:
  median 1.6±0.7 pL". Ref: Guillaume-Gentil O et al. "Tunable Single-Cell Extraction for
  Molecular Analyses." *Cell.* 2016 Jul 14;166(2):506–16, doi 10.1016/j.cell.2016.06.025,
  p.508 right column 3rd paragraph. PMID 27419874. Comment verbatim: "Considering the
  native cytoplasmic volumes measured in the pool of HeLa cells (maximum 4.4 pl median
  1.6 ± 0.7 pl Figure 3A), the observed loss in viability after extraction was most
  likely related to the complete removal of the cytoplasmic content."
  **This is cytoplasmic volume, not whole-cell volume** — it is the right number if the
  Kd conversion is meant to apply to a cytoplasmic concentration.

Cross-check from an independent paper already in this collection — **Wee et al. Cell 2012**
uses 5,000 µm³ for HeLa, verbatim (`wee2012.txt`):
  > "Consider two abundant miRNAs in a cultured HeLa cell (~5,000 μm 3; Cohen and
  > Studzinski, 1967; Milo et al., 2010)"

**Recommended for QUANTITY 4:** use **~3 pL (3,000 µm³) whole-cell** as a central value
with an explicit **1.2 – 5.0 pL** uncertainty range, or **~1.6 pL cytoplasmic** if the
relevant compartment is the cytoplasm. The "2–3 pL" figure in the brief is consistent
with the central values but the full literature range is wider on both sides.

Useful conversion, for the record: 1 molecule in 3 pL = 1/(6.022e23 × 3e-12 L)
= 5.5 × 10⁻¹³ M ≈ 0.55 pM. So a mouse AGO2 seed-match K_D of 26 pM corresponds to
about 47 molecules per 3 pL HeLa cell. (Arithmetic performed here, not quoted from
any source.)

---

## Files retrieved into this directory

| File | What it is |
|---|---|
| `wang2012_genesdev_PMC3323880.pdf` / `wang2012.txt` | Wang et al. Genes Dev 2012 (Q1 primary) |
| `janas2012_PMC3479394.pdf` / `janas2012.txt` | Janas et al. RNA 2012 (Q1, HeLa) |
| `rna_errata_PMC3504684.pdf` / `rna_errata.txt` | RNA 2012 erratum reconciling Janas vs Wang |
| `stalder2013_PMC3630355.xml` / `stalder2013.txt` | Stalder et al. EMBO J 2013 (Q1 cross-check) |
| `bosson2014_PMC5048918.html` / `bosson2014.txt` | Bosson et al. Mol Cell 2014 (Q1 negative, Q2 ESC mRNA) |
| `marinov2014_PMC3941114.xml` / `marinov2014.txt` | Marinov et al. Genome Res 2014 (Q2 primary) |
| `qiagen_faq_rna_per_cell.html` | QIAGEN FAQ — the actual origin of "360,000 mRNA/cell" |
| `cbbn_mrna.html` | Cell Biology by the Numbers, "How many mRNAs are in a cell?" |
| `wee2012_PMC3595543.html` / `wee2012.txt` | Wee et al. Cell 2012 (Q3 primary) |
| `salomon2015_PMC4503223.html` / `salomon2015.txt` | Salomon et al. Cell 2015 (Q3 cross-check) |
| `bn_104330.html`, `bn_109916.html`, `bn_111220.html`, `bn_111775.html` | BioNumbers, mRNA per cell |
| `bn_103719.html`, `bn_103725.html`, `bn_105879.html`, `bn_109386.html`, `bn_112928.html` | BioNumbers, HeLa cell volume |
