# riscpool build report

Generated programmatically from `results/*.json`, `data/PROVENANCE.json` and `MANIFEST.json`. No number in this file was typed by hand.

- generated: `2026-09-06T19:41:07Z`
- git commit: `0da907be5184eea8732e44cd580e9efe431b8b0b`
- python: `3.13.12`
- experiments recorded: **35**, failed: **0**

## 1. Experiment status and wall clock

| experiment | status | seed | wall clock (s) |
|---|---|---|---|
| `d1_gse5814` | **OK** | 0 | 4.9466 |
| `d1_seed_validation` | **OK** | 0 | 4.6777 |
| `d2_birmingham` | **OK** | 0 | 7.116 |
| `d2b_birmingham_arrays` | **OK** | 0 | 9.1155 |
| `d3_gencode` | **OK** | 0 | 28.6898 |
| `d4_hela_abundance` | **OK** | 0 | 2.9504 |
| `d7_gse28786` | **OK** | 0 | 1.1244 |
| `d7_candidates` | **OK** | 0 | 3.2891 |
| `d8_gse14073` | **OK** | 0 | 2.2863 |
| `d8_candidates` | **OK** | 0 | 3.3208 |
| `d9_jackson_oa_retry` | **OK** | 0 | 2.2498 |
| `f1_accessibility` | **OK** | 0 | 295.489 |
| `f2_features` | **OK** | 0 | 23.6534 |
| `f3_accessibility_d7` | **OK** | 0 | 398.195 |
| `f4_features_d7` | **OK** | 0 | 16.708 |
| `f5_accessibility_d8` | **OK** | 0 | 31.934 |
| `e5_hela_regime` | **OK** | 0 | 20.8686 |
| `e5b_budget_curve` | **OK** | 0 | 18.6449 |
| `e2b_redistribution_curve` | **OK** | 0 | 18.9288 |
| `e7_offtarget_ranking` | **OK** | 0 | 38.1648 |
| `e7b_null_calibration` | **OK** | 0 | 412.43 |
| `e4_retrieval_invariance` | **OK** | 0 | 18.6872 |
| `e4b_binned_background` | **OK** | 0 | 19.428 |
| `e9_dose_response` | **OK** | 0 | 1651.67 |
| `e9v_sim_estimator_validation` | **OK** | 0 | 5.7055 |
| `e10_cross_context` | **OK** | 0 | 33.8669 |
| `e2_redistribution` | **OK** | 0 | 22.0555 |
| `e3_pairwise_limit` | **OK** | 0 | 18.3421 |
| `e1_solver_correctness` | **OK** | 0 | 18.9688 |
| `e8_huesken_efficacy` | **OK** | 0 | 9.312 |
| `e6_sim_interaction_recovery` | **OK** | 0 | 172.464 |
| `px0_audit_and_spec` | **OK** | 0 | 0.6527 |
| `px_verify` | **OK** | 0 | 47.5714 |
| `pxa_affinity_correction` | **OK** | 0 | 5.441 |
| `pxb_approximation_cost` | **OK** | 0 | 311.754 |
| **total** |  |  | **3680.70** |

## 2. Failed experiments

None. Every experiment that was started produced a result.

## 3. Results, per experiment

### `d1_gse5814`  (OK)

seed `0`, wall clock `4.9466` s, recorded `2026-09-04T07:40:42Z`

| quantity | value |
|---|---|
| `annotation` | data/gse5814_probe_annotation.parquet |
| `samples` | data/gse5814_samples.tsv |
| `expression` | data/gse5814_expression.parquet |
| `n_platforms` | 3 |
| `n_samples` | 68 |
| `n_expr_rows` | 1608535 |
| `n_sirna_hela_samples` | 67 |
| `n_constructs` | 25 |
| `n_mapk14_seed_variant_constructs` | 19 |
| `n_seed_altering_constructs_pos2to8` | 7 |
| `n_seed_preserving_constructs` | 18 |
| `channel_convention` | CH1=Cy3=mock control, CH2=Cy5=siRNA; VALUE=log10(CH2/CH1), negative = repressed |
| `note_construct_count` | The build brief anticipated 27 constructs. The series as deposited contains the number reported in n_constructs; that measured count is reported rather than the anticipated one. |


**`target_genes`**: `["LUC_CONTROL", "MAPK14", "PIK3CB", "PLK1"]`


**`arrays_per_construct`**

```json
{
  "Luc_control": 1,
  "MAPK14-193_parent": 4,
  "MAPK14-193_pos01mut": 4,
  "MAPK14-193_pos02mut": 4,
  "MAPK14-193_pos03mut": 3,
  "MAPK14-193_pos04mut": 3,
  "MAPK14-193_pos05mut": 2,
  "MAPK14-193_pos06mut": 3,
  "MAPK14-193_pos07mut": 3,
  "MAPK14-193_pos08mut": 3,
  "MAPK14-193_pos09mut": 3,
  "MAPK14-193_pos10mut": 3,
  "MAPK14-193_pos11mut": 3,
  "MAPK14-193_pos12mut": 3,
  "MAPK14-193_pos13mut": 3,
  "MAPK14-193_pos14mut": 3,
  "MAPK14-193_pos15mut": 3,
  "MAPK14-193_pos16mut": 3,
  "MAPK14-193_pos17mut": 3,
  "MAPK14-193_pos18mut": 3,
  "MAPK14-193_pos19mut": 3,
  "PIK3CB-6338_parent": 1,
  "PIK3CB-6340_parent": 1,
  "PLK1-319_parent": 1,
  "PLK1-772_parent": 1
}
```


### `d1_seed_validation`  (OK)

seed `0`, wall clock `4.6777` s, recorded `2026-09-04T19:42:20Z`

| quantity | value |
|---|---|
| `parent_site_recovered_from_expression` | CTGCGGT |
| `parent_site_published` | CTGCGGT |
| `parent_site_welch_t` | -6.38984 |
| `n_constructs_compared` | 20 |
| `n_sites_exactly_agreeing` | 19 |
| `n_6mer_cores_agreeing` | 19 |
| `agreement_rate_7mer` | 0.95 |
| `agreement_rate_6mer_core` | 0.95 |
| `n_seed_altering_constructs` | 7 |
| `n_seed_altering_with_predicted_index_confirmed` | 4 |
| `mean_t_parent_site_seed_preserving` | -5.15803 |
| `mean_t_parent_site_seed_altering` | 4.65812 |
| `median_rank_parent_site_seed_preserving_of_16384` | 7 |
| `median_rank_parent_site_seed_altering_of_16384` | 14770 |
| `interpretation_is_not_asserted_here` | Counts and statistics only. The parent site was defined from the expression contrast without reading any sequence file; the published sites were read without touching the expression data. |
| `n_constructs_recovered_from_expression` | 20 |
| `n_constructs_with_published_sequence` | 24 |
| `n_constructs_without_published_sequence` | 0 |


**`parent_scan_top10_kmers`**: `["CTGCGGT", "TGCGGTT", "ATGCGGT", "TGCGGTA", "TTGCGGT", "TGCGGTC", "GCGGTTT", "CCCGCGA", "CCGCGCC", "TGGGTCC"]`


**`per_construct`**

| construct | mut_position | in_seed_by_definition | recovered_site | site_7mer_m8_dna | site_agrees | core6_agrees | recovered_site_t | t_parent_site | rank_parent_site |
|---|---|---|---|---|---|---|---|---|---|
| MAPK14-193_parent | 0 | false | CTGCGGT | CTGCGGT | true | true | -6.38984 | -6.38984 | 0 |
| MAPK14-193_pos01mut | 1 | false | CTGCGGT | CTGCGGT | true | true | -5.71697 | -5.71697 | 7 |
| MAPK14-193_pos02mut | 2 | true | CTGCGGA | CTGCGGA | true | true | -8.56354 | 3.16925 | 10762 |
| MAPK14-193_pos03mut | 3 | true | CTGCGAT | CTGCGAT | true | true | -4.56241 | 7.09554 | 16382 |
| MAPK14-193_pos04mut | 4 | true | CTGCAGT | CTGCAGT | true | true | -8.69489 | 5.27872 | 14770 |
| MAPK14-193_pos05mut | 5 | true | CTGAGGT | CTGAGGT | true | true | -7.40061 | 5.97844 | 16380 |
| MAPK14-193_pos06mut | 6 | true | CTACGGT | CTACGGT | true | true | -4.43095 | 3.8415 | 12407 |
| MAPK14-193_pos07mut | 7 | true | CAGCGGT | CGGCGGT | false | false | -1.9582 | 3.95019 | 16382 |
| MAPK14-193_pos08mut | 8 | true | ATGCGGT | ATGCGGT | true | true | -2.88116 | 3.29323 | 9568 |
| MAPK14-193_pos09mut | 9 | false | CTGCGGT | CTGCGGT | true | true | -2.80968 | -2.80968 | 4675 |
| MAPK14-193_pos10mut | 10 | false | CTGCGGT | CTGCGGT | true | true | -6.13437 | -6.13437 | 3 |
| MAPK14-193_pos11mut | 11 | false | CTGCGGT | CTGCGGT | true | true | -4.42461 | -4.42461 | 1019 |
| MAPK14-193_pos12mut | 12 | false | CTGCGGT | CTGCGGT | true | true | -5.9776 | -5.9776 | 0 |
| MAPK14-193_pos13mut | 13 | false | CTGCGGT | CTGCGGT | true | true | -5.67167 | -5.67167 | 400 |
| MAPK14-193_pos14mut | 14 | false | CTGCGGT | CTGCGGT | true | true | -2.10003 | -2.10003 | 8269 |
| MAPK14-193_pos15mut | 15 | false | CTGCGGT | CTGCGGT | true | true | -6.80094 | -6.80094 | 0 |
| MAPK14-193_pos16mut | 16 | false | CTGCGGT | CTGCGGT | true | true | -3.39849 | -3.39849 | 119 |
| MAPK14-193_pos17mut | 17 | false | CTGCGGT | CTGCGGT | true | true | -5.44262 | -5.44262 | 0 |
| MAPK14-193_pos18mut | 18 | false | CTGCGGT | CTGCGGT | true | true | -5.36199 | -5.36199 | 567 |
| MAPK14-193_pos19mut | 19 | false | CTGCGGT | CTGCGGT | true | true | -6.82553 | -6.82553 | 2 |


### `d2_birmingham`  (OK)

seed `0`, wall clock `7.116` s, recorded `2026-09-04T16:29:41Z`

| quantity | value |
|---|---|
| `n_usable` | 2 |
| `status_note` | D2 obtained; see attempts for what was tried |


**`attempts`**

| url | downloaded | machine_readable | detail | note |
|---|---|---|---|---|
| https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2635553/supplementaryFiles | true | false | members=['ukmss-2618-f0002.jpg', 'NIHMS2618-supplement-1.pdf', 'ukmss-2618-f0002.gif', 'ukmss-2618-f0001.gif', 'ukmss-2618-f0001.jpg'] tabular=[] | van Dongen S, Abreu-Goodger C, Enright AJ. Nat Methods 2008;5:1023-5. PMC2635553. Supplementary files, which reprocess the Birmingham and Jackson off-target datasets. |
| https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1804340/supplementaryFiles | false | false | not downloaded | candidate PMC record for a Birmingham-related deposit |
| https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5291/soft/GSE5291_family.soft.gz | true | true | SOFT header parsed | GSE5291, the GEO series that Garcia et al. 2011 lists alongside GSE5814 and which corresponds to a Dharmacon/Birmingham off-target experiment |
| https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5769/soft/GSE5769_family.soft.gz | true | true | SOFT header parsed | GSE5769, a further off-target series listed by Garcia et al. 2011 |
| https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/E-MEXP-668.idf.txt | true | true | non-archive file present | ArrayExpress E-MEXP-668 investigation description; found by searching the ArrayExpress collection for the article title phrase, and the file that carries PubMed ID 16489337 and so identifies the deposit |
| https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/E-MEXP-668.sdrf.txt | true | true | non-archive file present | ArrayExpress E-MEXP-668 sample and data relationship file; names every array data file and gives the sense strand sequence of every siRNA as its compound factor value |


**`usable_sources`**: `["https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/E-MEXP-668.idf.txt", "https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/E-MEXP-668.sdrf.txt"]`


### `d2b_birmingham_arrays`  (OK)

seed `0`, wall clock `9.1155` s, recorded `2026-09-04T16:33:12Z`

| quantity | value |
|---|---|
| `accession` | E-MEXP-668 |
| `route` | found by searching the ArrayExpress collection for the article title phrase, not by guessing an accession; the IDF's PubMed id is checked in code before the deposit is accepted |
| `n_array_files_named_by_sdrf` | 29 |
| `n_array_files_downloaded` | 29 |
| `n_array_files_failed` | 0 |
| `n_arrays_parsed` | 24 |
| `n_constructs` | 15 |
| `n_distinct_guides` | 12 |
| `n_gene_symbols` | 19780 |
| `n_rows` | 474720 |
| `median_probes_per_gene` | 1 |
| `value_definition` | log10 of the siRNA channel over the mock channel, per gene, median over probes. Negative is repression. Same sign convention as the GSE5814 pipeline. |
| `overall_median_log10ratio` | 0 |
| `supersedes` | the earlier FAILED record for D2. That record was correct that no GEO deposit exists and that the van Dongen archive carries no table; it was wrong that the data was unobtainable, because it was deposited in ArrayExpress instead. |


**`identification_from_idf`**

```json
{
  "identified": true,
  "pubmed_id_in_idf": "16489337",
  "expected_pubmed_id": "16489337",
  "publication_title_in_idf": "3' UTR seed matches, but not overall identity, are associated with RNAi off-targets",
  "investigation_title_in_idf": "Transcription profiling of human HeLa cells treated with various functional siRNAs to investigate RNAi off-targets",
  "author_list_in_idf": "Amanda Birmingham; Emily Anderson; Angela Reynolds; Diane Ilsley-Tyree; Devin Leake; Yuriy Fedorov; Scott Baskerville; Elena Maksimova; Kathryn Robinson; Jon Karpilow; William Marshall; Anastasia Khvorova"
}
```


**`constructs`**: `["BIRM-ACAGCAAA-100nM", "BIRM-CAGGGCGG-100nM", "BIRM-GAAAGAGC-100nM", "BIRM-GAAAGGAT-100nM", "BIRM-GAGCAGAT-100nM", "BIRM-GAGGTTCT-100nM", "BIRM-GCACATGG-100nM", "BIRM-GCAGAGAG-100nM", "BIRM-GGAAAGAC-100nM", "BIRM-GGCCTTAG-100nM", "BIRM-GGCCTTAG-50nM", "BIRM-GTATGACA-100nM", "BIRM-GTATGACA-50nM", "BIRM-TGGTTTAC-100nM", "BIRM-TGGTTTAC-50nM"]`


**`doses_nM`**: `[50.0, 100.0]`


**`cell_line`**: `["HeLa"]`


**`guides`**

| construct | sense_5to3_dna | guide_5to3_dna | seed_2_8_dna | site_7mer_m8_dna | dose |
|---|---|---|---|---|---|
| BIRM-GAGCAGAT-100nM | GAGCAGATTTGAAGCAACT | AGTTGCTTCAAATCTGCTC | GTTGCTT | AAGCAAC | 100 |
| BIRM-GAGGTTCT-100nM | GAGGTTCTCTGGATCAAGT | ACTTGATCCAGAGAACCTC | CTTGATC | GATCAAG | 100 |
| BIRM-GCAGAGAG-100nM | GCAGAGAGAGCAGATTTGA | TCAAATCTGCTCTCTCTGC | CAAATCT | AGATTTG | 100 |
| BIRM-GCACATGG-100nM | GCACATGGATGGAGGTTCT | AGAACCTCCATCCATGTGC | GAACCTC | GAGGTTC | 100 |
| BIRM-GAAAGAGC-100nM | GAAAGAGCATCTACGGTGA | TCACCGTAGATGCTCTTTC | CACCGTA | TACGGTG | 100 |
| BIRM-GAAAGGAT-100nM | GAAAGGATTTGGCTACAAA | TTTGTAGCCAAATCCTTTC | TTGTAGC | GCTACAA | 100 |
| BIRM-ACAGCAAA-100nM | ACAGCAAATTCCATCGTGT | ACACGATGGAATTTGCTGT | CACGATG | CATCGTG | 100 |
| BIRM-GGAAAGAC-100nM | GGAAAGACTGTTCCAAAAA | TTTTTGGAACAGTCTTTCC | TTTTGGA | TCCAAAA | 100 |
| BIRM-CAGGGCGG-100nM | CAGGGCGGAGACTTCACCA | TGGTGAAGTCTCCGCCCTG | GGTGAAG | CTTCACC | 100 |
| BIRM-TGGTTTAC-100nM | TGGTTTACATGTTCCAATA | TATTGGAACATGTAAACCA | ATTGGAA | TTCCAAT | 100 |
| BIRM-TGGTTTAC-50nM | TGGTTTACATGTTCCAATA | TATTGGAACATGTAAACCA | ATTGGAA | TTCCAAT | 50 |
| BIRM-GTATGACA-100nM | GTATGACAACAGCCTCAAG | CTTGAGGCTGTTGTCATAC | TTGAGGC | GCCTCAA | 100 |
| BIRM-GTATGACA-50nM | GTATGACAACAGCCTCAAG | CTTGAGGCTGTTGTCATAC | TTGAGGC | GCCTCAA | 50 |
| BIRM-GGCCTTAG-100nM | GGCCTTAGCTACAGGAGAG | CTCTCCTGTAGCTAAGGCC | TCTCCTG | CAGGAGA | 100 |
| BIRM-GGCCTTAG-50nM | GGCCTTAGCTACAGGAGAG | CTCTCCTGTAGCTAAGGCC | TCTCCTG | CAGGAGA | 50 |


**`per_construct`**

| construct | n_genes | median_log10ratio | mean_log10ratio |
|---|---|---|---|
| BIRM-ACAGCAAA-100nM | 19780 | 0 | 0.00115597 |
| BIRM-CAGGGCGG-100nM | 19780 | 0 | -0.00128878 |
| BIRM-GAAAGAGC-100nM | 19780 | 0 | 7.0588e-04 |
| BIRM-GAAAGGAT-100nM | 19780 | 0 | -0.00100274 |
| BIRM-GAGCAGAT-100nM | 19780 | 0 | 0.00716054 |
| BIRM-GAGGTTCT-100nM | 19780 | 0 | 0.0123815 |
| BIRM-GCACATGG-100nM | 19780 | 0 | 0.00598467 |
| BIRM-GCAGAGAG-100nM | 19780 | 0 | 0.0101787 |
| BIRM-GGAAAGAC-100nM | 19780 | 3.5737e-04 | 0.00215458 |
| BIRM-GGCCTTAG-100nM | 19780 | 0 | 0.00236332 |
| BIRM-GGCCTTAG-50nM | 19780 | 0 | 0.00494147 |
| BIRM-GTATGACA-100nM | 19780 | 0 | 0.00114668 |
| BIRM-GTATGACA-50nM | 19780 | 0 | 1.9346e-04 |
| BIRM-TGGTTTAC-100nM | 19780 | 0 | -0.00164846 |
| BIRM-TGGTTTAC-50nM | 19780 | 0 | 6.5874e-04 |


**`paths`**

```json
{
  "response": "data/birmingham_response.parquet",
  "sirna": "data/birmingham_sirna.parquet"
}
```


### `d3_gencode`  (OK)

seed `0`, wall clock `28.6898` s, recorded `2026-09-04T07:41:10Z`

| quantity | value |
|---|---|
| `gencode_release` | 50 |
| `n_pc_transcripts` | 382428 |
| `n_gtf_transcript_records` | 644292 |
| `n_transcripts_with_utr3` | 357575 |
| `n_transcripts_with_cds` | 382428 |
| `median_utr3_len` | 1134 |
| `mean_utr3_len` | 1663.64 |
| `total_utr3_nt` | 594874861 |
| `total_cds_nt` | 471142060 |
| `n_canonical_gene_symbols_with_utr3` | 19786 |
| `n_canonical_mane_select` | 18892 |


### `d4_hela_abundance`  (OK)

seed `0`, wall clock `2.9504` s, recorded `2026-09-04T07:41:13Z`

| quantity | value |
|---|---|
| `n_expr_rows_before_quality_filter` | 1585182 |
| `n_expr_rows_after` | 1575964 |
| `n_mock_arrays_used` | 67 |
| `n_probes_with_signal` | 35672 |
| `n_gene_symbols` | 16839 |
| `n_genes_joined_to_gencode_canonical_with_utr3` | 11306 |
| `abundance_gini_like_top1pct_share` | 0.195569 |
| `abundance_dynamic_range_log10` | 4.11142 |
| `path` | data/hela_abundance.parquet |
| `source` | GSE5814 INTENSITY1 (raw Cy3, CH1 = mock control channel) |
| `sum_x_rel` | 1 |
| `median_x_rel` | 8.9345e-06 |


**`top10_genes_by_relative_abundance`**

| gene_symbol | x_rel |
|---|---|
| RPS27A | 0.0021522 |
| RPS17 | 0.0020637 |
| RPS29 | 0.00203788 |
| RPL32 | 0.00200294 |
| ALDOA | 0.00199197 |
| NCL | 0.00199077 |
| MYL6 | 0.00195841 |
| IFITM3 | 0.00194205 |
| ARF1 | 0.00193324 |
| PARK7 | 0.0019311 |


### `d7_gse28786`  (OK)

seed `0`, wall clock `1.1244` s, recorded `2026-09-04T16:07:41Z`

| quantity | value |
|---|---|
| `n_probesets` | 17788 |
| `n_arrays` | 54 |
| `n_probesets_unmapped_to_ncbi_gene` | 470 |
| `n_gene_symbols` | 17318 |
| `n_arrays_with_conflicting_dose_labels` | 6 |
| `dose_label_resolution` | the GEO characteristics labelling is used throughout. It is the labelling under which the on-target transcript falls when its own siRNA is added, for every construct including STAT3-1676; the CEL-filename labelling would require STAT3 to be silenced by zero nanomolar of STAT3 siRNA. |
| `abundance_note` | x_rel is the mean linear-scale RMA intensity over the zero-dose arrays of that cell line, collapsed probeset to symbol by median and normalised to sum to one. Zero dose is not untreated: it carries the same total duplex made up with non-targeting control siRNA. |
| `response_note` | log2fc is the mean log2 RMA level at the dose minus the mean over the zero-dose arrays of the same construct. Negative is repression. |
| `n_guides_parsed_from_table1` | 7 |
| `all_passengers_are_revcomp_of_guide` | true |
| `all_underlined_seeds_match_positions_2_7` | true |
| `guide_source` | Table 1 of PMC3130022, parsed from the recorded full-text XML at data/lit/caffrey2011/PMC3130022_fulltext.xml. Not typed in. The 3' overhang is the lowercase suffix the table itself uses and the seed is the table's own <underline> span; both are checked against the guide body rather than assumed. |


**`cell_lines`**: `["Hep3B liver cancer cells", "MCF-7 breast cancer cells"]`


**`constructs`**: `["HK2-3581", "HK2-3581M", "HK2-4031", "STAT3-1676", "STAT3-1676M"]`


**`doses_nM`**: `[0.0, 1.0, 10.0, 25.0]`


**`constructs_with_conflicting_dose_labels`**: `["STAT3-1676"]`


**`dose_label_audit`**

| construct | cell_line | on_target_gene | probeset | n_arrays | n_arrays_where_labels_agree | on_target_log2_at_zero_characteristics | on_target_log2_at_top_dose_characteristics | on_target_log2fc_top_minus_zero_characteristics | silencing_observed_characteristics | on_target_log2_at_zero_cel_filename | on_target_log2_at_top_dose_cel_filename | on_target_log2fc_top_minus_zero_cel_filename | silencing_observed_cel_filename |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HK2-3581 | Hep3B liver cancer cells | HK2 | 3099_at | 12 | 12 | 11.2697 | 9.20469 | -2.06501 | true | 11.2697 | 9.20469 | -2.06501 | true |
| HK2-3581M | Hep3B liver cancer cells | HK2 | 3099_at | 12 | 12 | 11.5043 | 10.2086 | -1.29572 | true | 11.5043 | 10.2086 | -1.29572 | true |
| HK2-4031 | Hep3B liver cancer cells | HK2 | 3099_at | 6 | 6 | 9.62773 | 7.39571 | -2.23202 | true | 9.62773 | 7.39571 | -2.23202 | true |
| STAT3-1676 | MCF-7 breast cancer cells | STAT3 | 6774_at | 12 | 6 | 7.977 | 6.86938 | -1.10762 | true | 6.86938 | 7.977 | 1.10762 | false |
| STAT3-1676M | MCF-7 breast cancer cells | STAT3 | 6774_at | 12 | 12 | 9.06322 | 7.12104 | -1.94219 | true | 9.06322 | 7.12104 | -1.94219 | true |


**`paths`**

```json
{
  "expression": "data/gse28786_expression.parquet",
  "samples": "data/gse28786_samples.parquet",
  "abundance": "data/gse28786_abundance.parquet",
  "response": "data/gse28786_response.parquet"
}
```


**`guides`**

| guide_with_overhang_rna | guide_5to3_rna | guide_5to3_dna | guide_len | overhang_rna | passenger_5to3_rna | seed_underlined_in_table_rna | seed_positions_2_7_from_guide_rna | seed_2_8_dna | site_7mer_m8_dna | site_6mer_dna | passenger_is_revcomp_of_guide | underlined_seed_matches_positions_2_7 | construct | is_2ome_modified | target_gene |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UUUGUAAUCGUCGAUACCC | UUUGUAAUCGUCGAUACCC | TTTGTAATCGTCGATACCC | 19 |  | GGGUAUCGACGAUUACAAA |  | UUGUAA | TTGTAAT | ATTACAA | TTACAA | true | null | AllStars negative control | false | null |
| UUGUUGUGCAUCUCCACUCuu | UUGUUGUGCAUCUCCACUC | TTGTTGTGCATCTCCACTC | 19 | uu | GAGUGGAGAUGCACAACAA | UGUUGU | UGUUGU | TGTTGTG | CACAACA | ACAACA | true | true | HK2-3581 | false | HK2 |
| UUGUUGUGCAUCUCCACUCuu | UUGUUGUGCAUCUCCACUC | TTGTTGTGCATCTCCACTC | 19 | uu | GAGUGGAGAUGCACAACAA | UGUUGU | UGUUGU | TGTTGTG | CACAACA | ACAACA | true | true | HK2-3581M | true | HK2 |
| UCCAUGUUCACACACAUCCuu | UCCAUGUUCACACACAUCC | TCCATGTTCACACACATCC | 19 | uu | GGAUGUGUGUGAACAUGGA | CCAUGU | CCAUGU | CCATGTT | AACATGG | ACATGG | true | true | HK2-4031 | false | HK2 |
| GUAUCUCUUCAUAGCCUUA | GUAUCUCUUCAUAGCCUUA | GTATCTCTTCATAGCCTTA | 19 |  | UAAGGCUAUGAAGAGAUAC | UAUCUC | UAUCUC | TATCTCT | AGAGATA | GAGATA | true | true | siGenome2 non-targeting control | false | null |
| UUGGUCAGCAUGUUGUACCuu | UUGGUCAGCAUGUUGUACC | TTGGTCAGCATGTTGTACC | 19 | uu | GGUACAACAUGCUGACCAA | UGGUCA | UGGUCA | TGGTCAG | CTGACCA | TGACCA | true | true | STAT3-1676 | false | STAT3 |
| UUGGUCAGCAUGUUGUACCuu | UUGGUCAGCAUGUUGUACC | TTGGTCAGCATGTTGTACC | 19 | uu | GGUACAACAUGCUGACCAA | UGGUCA | UGGUCA | TGGTCAG | CTGACCA | TGACCA | true | true | STAT3-1676M | true | STAT3 |


### `d7_candidates`  (OK)

seed `0`, wall clock `3.2891` s, recorded `2026-09-04T16:07:45Z`

| quantity | value |
|---|---|
| `n_candidate_transcripts` | 16492 |
| `total_utr3_nucleotides` | 30493209 |
| `median_utr3_len` | 1149 |
| `gencode_release` | 50 |
| `path` | data/candidate_utr3_gse28786.parquet |
| `note` | both cell lines were run on the same array, so the retrieval universe is shared and only the abundance vector differs between them |


### `d8_gse14073`  (OK)

seed `0`, wall clock `2.2863` s, recorded `2026-09-04T16:21:01Z`

| quantity | value |
|---|---|
| `n_probes` | 43483 |
| `n_arrays` | 56 |
| `n_probes_without_platform_annotation` | 16674 |
| `n_gene_symbols` | 18503 |
| `value_scale_note` | the deposited matrix carries linear RMA intensities, not log ratios; log2fc is formed here against the mock arrays of the same cell line at the same timepoint |


**`cell_lines`**: `["HUH7", "PLC/PRF/5"]`


**`constructs`**: `["APOB-Hs1", "APOB-Hs2", "APOB-Hs3", "APOB-Hs4", "Apob-Mm1", "Apob-Mm2", "RAD18"]`


**`hours`**: `[6.0, 12.0, 24.0, 48.0]`


**`n_mock_arrays_per_cell_line`**

```json
{
  "HUH7": 4,
  "PLC/PRF/5": 3
}
```


**`timepoints_shared_by_both_cell_lines`**: `[6.0, 12.0, 48.0]`


**`paths`**

```json
{
  "expression": "data/gse14073_expression.parquet",
  "samples": "data/gse14073_samples.parquet",
  "abundance": "data/gse14073_abundance.parquet",
  "response": "data/gse14073_response.parquet"
}
```


### `d8_candidates`  (OK)

seed `0`, wall clock `3.3208` s, recorded `2026-09-04T16:21:04Z`

| quantity | value |
|---|---|
| `n_candidate_transcripts` | 14576 |
| `total_utr3_nucleotides` | 26954037 |
| `gencode_release` | 50 |
| `path` | data/candidate_utr3_gse14073.parquet |


### `d9_jackson_oa_retry`  (OK)

seed `0`, wall clock `2.2498` s, recorded `2026-09-04T16:33:47Z`

| quantity | value |
|---|---|
| `target` | Jackson AL et al. RNA 2006;12:1179-1187, PMC1484447 |
| `n_attempts` | 5 |
| `n_usable` | 0 |
| `full_text_obtained` | false |
| `consequence` | none for any downstream number. The siRNA sequences this article would have supplied were already obtained from the Garcia et al. 2011 supplementary table joined on GSM accession, and independently corroborated by recovering the same 7mer-m8 sites from the measured response; see results/d1_seed_v... |


**`attempts`**

| url | downloaded | full_text_usable | first_bytes | note |
|---|---|---|---|---|
| https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC1484447 | false | false | not downloaded | PMC open-access web service, the route the retry was asked to try |
| https://pmc.ncbi.nlm.nih.gov/utils/oa/oa.fcgi?id=PMC1484447 | false | false | not downloaded | the same service on the current PMC host |
| https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/fullTextXML | false | false | not downloaded | Europe PMC full text, retried; returned 404 on the earlier pass |
| https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/supplementaryFiles | true | false | <?xml version="1.0" encoding="UTF-8" standalone="yes"?><errorBean><errCode>0</errCode><errMsg>Article with id PMC1484447 is not open access one</errMsg></errorBean> | Europe PMC supplementary files, retried |
| https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=1484447&retmode=xml | true | false | <?xml version="1.0"  ?><!DOCTYPE pmc-articleset PUBLIC "-//NLM//DTD ARTICLE SET 2.0//EN" "https://dtd.nlm.nih.gov/ncbi/pmc/articleset/nlm-articleset-2.0.dtd"><pmc-articleset><article article-type="research-article" xml:lang="EN" dtd-version="1.4"><!--The publisher of this article does not allow downloading of the full text in XML form.--><front><journal-meta><journal-id journal-id-type="nlm-ta">RN | NCBI efetch against the PMC database |


### `f1_accessibility`  (OK)

seed `0`, wall clock `295.489` s, recorded `2026-09-04T07:54:21Z`

| quantity | value |
|---|---|
| `n_transcripts` | 11304 |
| `n_errors` | 0 |
| `total_positions` | 21496942 |
| `pfl_fold_W` | 80 |
| `pfl_fold_L` | 40 |
| `pfl_fold_u_max` | 15 |
| `path` | data/accessibility_u8_u15.npz |


**`errors`**

```json
{}
```


**`stretch_lengths_kept`**: `[8, 15]`


### `f2_features`  (OK)

seed `0`, wall clock `23.6534` s, recorded `2026-09-04T19:42:44Z`

| quantity | value |
|---|---|
| `gencode_release` | 50 |
| `viennarna_version` | 2.6.4 |
| `RT_kcal_per_mol` | 0.61633 |
| `duplexfold_flank_nt` | 12 |
| `local_au_window_nt` | 30 |
| `n_sites` | 50708 |
| `n_construct_transcript_pairs` | 34953 |
| `n_constructs` | 24 |
| `n_transcripts_hit` | 8100 |
| `median_sites_per_construct` | 1085 |
| `median_pairs_per_construct` | 951 |
| `dg_duplex_kcal_mean` | -13.7997 |
| `dg_duplex_kcal_sd` | 3.36448 |
| `p_unpaired_15_median` | 9.0570e-04 |
| `ddG_kcal_mean` | -9.22901 |
| `ddG_kcal_sd` | 3.35033 |
| `n_sites_with_nan_ddG` | 0 |
| `log10_K_transcript_min` | -18.7281 |
| `log10_K_transcript_max` | 7.56073 |
| `log10_K_transcript_sd` | 2.43565 |
| `features_path` | data/features.parquet |


**`sites_by_class`**

```json
{
  "6mer": 29568,
  "7mer-m8": 11938,
  "7mer-A1": 6717,
  "8mer": 2485
}
```


### `f3_accessibility_d7`  (OK)

seed `0`, wall clock `398.195` s, recorded `2026-09-04T16:14:52Z`

| quantity | value |
|---|---|
| `n_transcripts` | 16492 |
| `n_errors` | 0 |
| `total_positions` | 30493209 |
| `pfl_fold_W` | 80 |
| `pfl_fold_L` | 40 |
| `pfl_fold_u_max` | 15 |
| `path` | data/accessibility_gse28786_u8_u15.npz |


**`errors`**

```json
{}
```


**`stretch_lengths_kept`**: `[8, 15]`


### `f4_features_d7`  (OK)

seed `0`, wall clock `16.708` s, recorded `2026-09-04T19:43:01Z`

| quantity | value |
|---|---|
| `n_site_rows` | 40796 |
| `n_construct_transcript_pairs` | 25076 |
| `frac_sites_with_finite_ddG` | 1 |
| `ddG_kcal_median` | -7.68152 |
| `ddG_kcal_min` | -22.3839 |
| `ddG_kcal_max` | 11.1298 |
| `log10_K_transcript_uncalibrated_min` | -15.7727 |
| `log10_K_transcript_uncalibrated_max` | 7.84259 |
| `viennarna_version` | 2.6.4 |
| `gencode_release` | 50 |
| `path` | data/features_gse28786.parquet |


**`constructs`**: `["HK2-3581", "HK2-3581M", "HK2-4031", "STAT3-1676", "STAT3-1676M"]`


**`n_transcripts_per_construct`**

```json
{
  "HK2-3581": 4634,
  "HK2-3581M": 4634,
  "HK2-4031": 5626,
  "STAT3-1676": 5091,
  "STAT3-1676M": 5091
}
```


**`site_class_counts`**

```json
{
  "6mer": 19975,
  "7mer-m8": 8746,
  "7mer-A1": 8743,
  "8mer": 3332
}
```


### `f5_accessibility_d8`  (OK)

seed `0`, wall clock `31.934` s, recorded `2026-09-04T16:21:36Z`

| quantity | value |
|---|---|
| `n_transcripts` | 14576 |
| `n_reused_from_existing_caches` | 13349 |
| `n_computed_here` | 1227 |
| `n_errors` | 0 |
| `total_positions` | 26954037 |
| `pfl_fold_W` | 80 |
| `pfl_fold_L` | 40 |
| `pfl_fold_u_max` | 15 |
| `path` | data/accessibility_gse14073_u8_u15.npz |


**`errors`**

```json
{}
```


**`reused_from`**: `["data/accessibility_gse28786_u8_u15.npz"]`


### `e5_hela_regime`  (OK)

seed `0`, wall clock `20.8686` s, recorded `2026-09-04T19:45:07Z`

| quantity | value |
|---|---|
| `normalisation_LIMITATION` | Microarray intensities are relative, not absolute. They are put on a molecules-per-cell scale by assuming the measured relative abundances partition a published total mRNA count per cell. Array intensity is not linear in transcript number across the full dynamic range, probe affinities differ, an... |
| `kd_full_complementarity_molecules_per_cell` | 36.1328 |
| `n_candidate_constructs` | 20 |
| `n_retrieved_offtarget_transcripts_union` | 6814 |
| `total_mrna_molecules_per_cell` | 80000 |
| `x_on_target_MAPK14_molecules_per_cell` | 28.8352 |
| `H_K_measured_sd_log10_K_on` | 1.28026 |
| `dg_on_target_kcal_parent` | -34.9 |
| `on_target_site_sequence_dna` | CCTACAGAGAACTGCGGTT |
| `rho_hela_band_low` | 1.8750e-04 |
| `rho_hela_band_high` | 2.125 |
| `min_tau_anywhere_in_hela_band` | 0.705263 |
| `max_tau_anywhere_in_hela_band` | 1 |
| `answer_does_hela_fall_in_the_regime_where_equilibrium_reorders` | true |
| `criterion` | tau < 0.9 between equilibrium and independent candidate ranking is the threshold used throughout; tau = 1 means the layer changes no decision |


**`constants_used`**

```json
{
  "kd_seed_match_molar": 2.6e-11,
  "kd_seed_match_molecules_per_cell": 46.972697928,
  "hela_cell_volume_litres": 3e-12,
  "anchor_site_class": "7mer-m8",
  "median_boltzmann_factor_anchor_class": 3.380290220755692e-08,
  "K_scale_constant_C": 1389605473.5057297,
  "mrna_molecules_per_cell": 80000.0,
  "ago2_copies_per_cell_low": 15000.0,
  "ago2_copies_per_cell_high": 170000.0
}
```


**`candidate_constructs`**: `["MAPK14-193_parent", "MAPK14-193_pos01mut", "MAPK14-193_pos02mut", "MAPK14-193_pos03mut", "MAPK14-193_pos04mut", "MAPK14-193_pos05mut", "MAPK14-193_pos06mut", "MAPK14-193_pos07mut", "MAPK14-193_pos08mut", "MAPK14-193_pos09mut", "MAPK14-193_pos10mut", "MAPK14-193_pos11mut", "MAPK14-193_pos12mut", "MAPK14-193_pos13mut", "MAPK14-193_pos14mut", "MAPK14-193_pos15mut", "MAPK14-193_pos16mut", "MAPK14-193_pos17mut", "MAPK14-193_pos18mut", "MAPK14-193_pos19mut"]`


**`dg_on_target_kcal_range`**: `[-34.9, -28.7]`


**`alpha_swept`**: `[0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0]`


**`rho_estimates_by_alpha`**

| alpha_loaded_fraction | rho_low | rho_high |
|---|---|---|
| 0.001 | 1.8750e-04 | 0.002125 |
| 0.003 | 5.6250e-04 | 0.006375 |
| 0.01 | 0.001875 | 0.02125 |
| 0.03 | 0.005625 | 0.06375 |
| 0.1 | 0.01875 | 0.2125 |
| 0.3 | 0.05625 | 0.6375 |
| 1 | 0.1875 | 2.125 |


**`rho_grid`**: `[0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0]`


**`H_K_grid`**: `[0.05, 0.1, 0.2, 0.4, 0.8, 1.6, 3.2]`


**`tau_grid_beta_zero`**

```json
{
  "H_K=0.05": [
    0.7473684210526316,
    0.7578947368421053,
    0.6947368421052632,
    0.7263157894736842,
    0.7999999999999999,
    0.8421052631578948,
    0.9789473684210527,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0
  ],
  "H_K=0.1": [
    0.7473684210526316,
    0.7578947368421053,
    0.6947368421052632,
    0.7263157894736842,
    0.7999999999999999,
    0.8421052631578948,
    0.9789473684210527,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0
  ],
  "H_K=0.2": [
    0.7473684210526316,
    0.7578947368421053,
    0.6947368421052632,
    0.7263157894736842,
    0.7999999999999999,
    0.8421052631578948,
    0.9789473684210527,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0
  ],
  "H_K=0.4": [
    0.7473684210526316,
    0.7578947368421053,
    0.6947368421052632,
    0.7263157894736842,
    0.7999999999999999,
    0.8526315789473685,
    0.9789473684210527,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0
  ],
  "H_K=0.8": [
    0.7473684210526316,
    0.7578947368421053,
    0.6947368421052632,
    0.7263157894736842,
    0.7894736842105264,
    0.8526315789473685,
    0.9789473684210527,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0
  ],
  "H_K=1.6": [
    0.7052631578947369,
    0.7052631578947369,
    0.6631578947368422,
    0.6631578947368422,
    0.768421052631579,
    0.8631578947368421,
    0.9789473684210527,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0
  ],
  "H_K=3.2": [
    0.5684210526315789,
    0.5894736842105264,
    0.5368421052631579,
    0.5684210526315789,
    0.7157894736842105,
    0.8526315789473685,
    0.9789473684210527,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0
  ]
}
```


**`tau_row_at_measured_H_K`**: `[0.7368421052631579, 0.7368421052631579, 0.6736842105263158, 0.7157894736842105, 0.7999999999999999, 0.8631578947368421, 0.9789473684210527, 1.0, 1.0, 1.0, 1.0, 1.0]`


**`tau_0.9_contour_by_H_K`**

| H_K | rho_at_tau_0.9 | min_tau | max_tau |
|---|---|---|---|
| 0.05 | 0.0499274 | 0.694737 | 1 |
| 0.1 | 0.0499274 | 0.694737 | 1 |
| 0.2 | 0.0499274 | 0.694737 | 1 |
| 0.4 | 0.0471195 | 0.694737 | 1 |
| 0.8 | 0.0471195 | 0.694737 | 1 |
| 1.6 | 0.044004 | 0.663158 | 1 |
| 3.2 | 0.0471195 | 0.536842 | 1 |


**`background_beta_bracket`**

```json
{
  "low": 0.0,
  "high": 9.61641287818848,
  "x_not_retrieved_molecules_per_cell": 39958.86045152216,
  "K_nonspecific_molecules_per_cell": 4155.2771244000005,
  "K_nonspecific_source": "Wee et al. Cell 2012, g4g5 seed-mismatched target, 2.3 nM; fly Ago2, species caveat recorded in data/constants.json"
}
```


**`hela_band_detail`**

| which | rho | beta | beta_case | kendall_tau_eq_vs_independent | mean_free_pool_f | mean_f_over_M | mean_offtarget_load_equilibrium | mean_offtarget_load_independent | load_ratio_eq_over_independent |
|---|---|---|---|---|---|---|---|---|---|
| rho_low_end | 1.8750e-04 | 0 | zero_background | 0.705263 | 9.5714e-05 | 6.3810e-06 | 14.9999 | 2517.94 | 0.00595721 |
| rho_low_end | 1.8750e-04 | 9.61641 | max_background_bracket | 0.726316 | 9.5649e-05 | 6.3766e-06 | 14.999 | 2517.94 | 0.00595684 |
| rho_high_end | 2.125 | 0 | zero_background | 1 | 163626 | 0.962507 | 6351.94 | 6366.49 | 0.997715 |
| rho_high_end | 2.125 | 9.61641 | max_background_bracket | 0.968421 | 15479.7 | 0.091057 | 5646.87 | 6366.49 | 0.886968 |


### `e5b_budget_curve`  (OK)

seed `0`, wall clock `18.6449` s, recorded `2026-09-04T19:45:27Z`

| quantity | value |
|---|---|
| `construct` | MAPK14-193_parent |
| `n_retrieved_transcripts` | 951 |
| `sum_x_retrieved_molecules_per_cell` | 5437.12 |
| `total_mrna_molecules_per_cell` | 80000 |
| `max_independent_over_M` | 1491.14 |
| `independent_over_M_at_ago2_measured_low` | 0.291129 |
| `independent_over_M_at_ago2_measured_high` | 0.0294098 |
| `crossover_M_where_independent_equals_budget` | 3950.29 |
| `alpha_threshold_for_over_allocation_vs_ago2_low` | 0.263353 |
| `alpha_threshold_for_over_allocation_vs_ago2_high` | 0.023237 |
| `over_allocation_note` | max_independent_over_M is attained at a pool of well under one complex per cell, outside any defensible range, and should not be quoted as a headline. At the measured Argonaute copy numbers with alpha = 1 the independent counterfactual allocates LESS than the budget, so the over-allocation is con... |
| `max_independent_over_M_at_rho` | 1.0000e-05 |
| `max_independent_over_M_at_M` | 0.8 |
| `equilibrium_plateau_equals_sum_x` | true |
| `ago2_measured_low_copies_per_cell` | 15000 |
| `ago2_measured_high_copies_per_cell` | 170000 |
| `ago2_measurement_note` | the low value is the only HeLa-specific measurement found (Janas et al., AQUA mass spectrometry, Ago1-4); the high value is from a different cell type and method. Both are measured copy numbers and neither is a sweep, which is why the figure marks them differently from the alpha-swept band. |
| `interpretation` | independent_over_M above 1 means the independent pairwise counterfactual allocates more loaded RISC than the cell contains. It is a counterfactual about what those affinities imply if transcripts are scored in isolation, not a claim about any published predictor's output. |


**`curve`**

| rho | M | independent_total_occupancy | equilibrium_total_occupancy | independent_over_M | equilibrium_over_M |
|---|---|---|---|---|---|
| 1.0000e-05 | 0.8 | 1192.91 | 0.8 | 1491.14 | 1 |
| 1.3141e-05 | 1.05132 | 1259.31 | 1.05132 | 1197.84 | 1 |
| 1.7270e-05 | 1.38159 | 1326.86 | 1.38159 | 960.387 | 1 |
| 2.2695e-05 | 1.81561 | 1395.44 | 1.81561 | 768.582 | 1 |
| 2.9825e-05 | 2.38598 | 1465.15 | 2.38598 | 614.065 | 1 |
| 3.9194e-05 | 3.13553 | 1536.19 | 3.13552 | 489.931 | 1 |
| 5.1507e-05 | 4.12054 | 1608.9 | 4.12054 | 390.459 | 1 |
| 6.7688e-05 | 5.415 | 1683.63 | 5.415 | 310.919 | 0.999999 |
| 8.8951e-05 | 7.11611 | 1760.67 | 7.1161 | 247.421 | 0.999999 |
| 1.1690e-04 | 9.35161 | 1840.28 | 9.35161 | 196.788 | 0.999999 |
| 1.5362e-04 | 12.2894 | 1922.65 | 12.2894 | 156.448 | 0.999999 |
| 2.0188e-04 | 16.1501 | 2007.92 | 16.1501 | 124.328 | 0.999999 |
| 2.6529e-04 | 21.2236 | 2096.16 | 21.2236 | 98.7656 | 0.999999 |
| 3.4864e-04 | 27.8909 | 2187.44 | 27.8909 | 78.4283 | 0.999999 |
| 4.5816e-04 | 36.6528 | 2281.72 | 36.6527 | 62.2523 | 0.999999 |
| 6.0209e-04 | 48.1672 | 2378.88 | 48.1671 | 49.388 | 0.999999 |
| 7.9123e-04 | 63.2987 | 2478.63 | 63.2987 | 39.1577 | 0.999999 |
| 0.0010398 | 83.1839 | 2580.56 | 83.1837 | 31.0223 | 0.999998 |
| 0.00136645 | 109.316 | 2684.1 | 109.316 | 24.5536 | 0.999998 |
| 0.00179571 | 143.657 | 2788.62 | 143.657 | 19.4116 | 0.999998 |
| 0.00235983 | 188.787 | 2893.4 | 188.786 | 15.3263 | 0.999997 |
| 0.00310117 | 248.094 | 2997.74 | 248.093 | 12.0831 | 0.999996 |
| 0.00407539 | 326.031 | 3100.98 | 326.029 | 9.51128 | 0.999994 |
| 0.00535567 | 428.453 | 3202.53 | 428.448 | 7.47464 | 0.999988 |
| 0.00703814 | 563.051 | 3301.97 | 563.031 | 5.86443 | 0.999965 |
| 0.00924915 | 739.932 | 3399.03 | 739.848 | 4.59371 | 0.999887 |
| 0.0121547 | 972.379 | 3493.65 | 972.076 | 3.59289 | 0.999688 |
| 0.0159731 | 1277.85 | 3585.97 | 1276.72 | 2.80625 | 0.999117 |
| 0.020991 | 1679.28 | 3676.28 | 1674.05 | 2.18919 | 0.996885 |
| 0.0275853 | 2206.83 | 3764.95 | 2179.57 | 1.70605 | 0.987651 |
| 0.0362512 | 2900.09 | 3852.43 | 2765.01 | 1.32838 | 0.953422 |
| 0.0476394 | 3811.15 | 3939.09 | 3280.56 | 1.03357 | 0.860778 |
| 0.0626052 | 5008.41 | 4025.24 | 3614.83 | 0.803696 | 0.721752 |
| 0.0822724 | 6581.79 | 4111.06 | 3835.1 | 0.624611 | 0.582683 |
| 0.108118 | 8649.45 | 4196.54 | 4001.71 | 0.48518 | 0.462655 |
| 0.142083 | 11366.6 | 4281.52 | 4140.33 | 0.376674 | 0.364253 |
| 0.186718 | 14937.4 | 4365.68 | 4262.06 | 0.292264 | 0.285327 |
| 0.245375 | 19630 | 4448.57 | 4372.17 | 0.226621 | 0.222729 |
| 0.322459 | 25796.7 | 4529.69 | 4473.35 | 0.175592 | 0.173408 |
| 0.423759 | 33900.7 | 4608.5 | 4567.08 | 0.135941 | 0.134719 |
| 0.556881 | 44550.5 | 4684.46 | 4654.16 | 0.105149 | 0.104469 |
| 0.731824 | 58545.9 | 4757.04 | 4735.02 | 0.0812531 | 0.0808771 |
| 0.961725 | 76938 | 4825.78 | 4809.91 | 0.062723 | 0.0625167 |
| 1.26385 | 101108 | 4890.25 | 4878.91 | 0.0483667 | 0.0482545 |
| 1.66088 | 132871 | 4950.1 | 4942.09 | 0.0372551 | 0.0371947 |
| 2.18264 | 174612 | 5005.08 | 4999.47 | 0.0286641 | 0.028632 |
| 2.86832 | 229465 | 5055.04 | 5051.16 | 0.0220297 | 0.0220127 |
| 3.76939 | 301551 | 5099.98 | 5097.32 | 0.0169125 | 0.0169037 |
| 4.95354 | 396283 | 5140.03 | 5138.23 | 0.0129706 | 0.0129661 |
| 6.50968 | 520774 | 5175.44 | 5174.22 | 0.00993797 | 0.00993563 |
| 8.55467 | 684374 | 5206.54 | 5205.73 | 0.00760774 | 0.00760655 |
| 11.2421 | 899368 | 5233.75 | 5233.21 | 0.00581937 | 0.00581876 |
| 14.7738 | 1.1819e+06 | 5257.51 | 5257.15 | 0.00444835 | 0.00444804 |
| 19.4149 | 1.5532e+06 | 5278.23 | 5277.99 | 0.00339831 | 0.00339816 |
| 25.5141 | 2.0411e+06 | 5296.32 | 5296.16 | 0.0025948 | 0.00259472 |
| 33.5292 | 2.6823e+06 | 5312.1 | 5311.99 | 0.0019804 | 0.00198036 |
| 44.0624 | 3.5250e+06 | 5325.86 | 5325.79 | 0.00151089 | 0.00151087 |
| 57.9044 | 4.6324e+06 | 5337.83 | 5337.78 | 0.00115229 | 0.00115228 |
| 76.095 | 6.0876e+06 | 5348.19 | 5348.16 | 8.7854e-04 | 8.7853e-04 |
| 100 | 8.0000e+06 | 5357.08 | 5357.06 | 6.6964e-04 | 6.6963e-04 |


### `e2b_redistribution_curve`  (OK)

seed `0`, wall clock `18.9288` s, recorded `2026-09-04T19:45:46Z`

| quantity | value |
|---|---|
| `construct` | MAPK14-193_parent |
| `n_retrieved_transcripts` | 951 |
| `target_selection_rule` | transcript with the median x/K in the retrieved set |
| `target_index` | 183 |
| `target_transcript_id` | ENST00000271915.9 |
| `target_gene_symbol` | KCNN3 |
| `target_K_original` | 17.0396 |
| `target_x` | 0.0959742 |
| `all_series_monotone_as_proposition_requires` | false |


**`K_sweep_log10_range`**: `[-4.0, 6.0]`


**`rho_values`**: `[0.01, 0.1875, 2.0]`


**`series`**

| rho | M | points | o_target_is_monotone_decreasing_in_K | o_others_is_monotone_increasing_in_K | o_target_fold_change_over_sweep | o_others_fold_change_over_sweep |
|---|---|---|---|---|---|---|
| 0.01 | 800 | [{"K_target": 0.0001, "o_target": 0.095895954603926, "o_others_sum": 799.7816225889583, "free_pool_f": 0.1224814564377987}, {"K_target": 0.00014773776525985112, "o_target": 0.09585862372648742, "o_others_sum": 799.7816598925833, "free_pool_f": 0.12248148369020873}, {"K_target": 0.00021826447283974872, "o_target": 0.09580352511089354, "o_others_sum": 799.7817149509755, "free_pool_f": 0.1224815239134891}, {"K_target": 0.00032245905452963947, "o_target": 0.0957222395285553, "o_others_sum": 799.7817961772176, "free_pool_f": 0.12248158325388592}, {"K_target": 0.00047639380104013405, "o_target": 0.09560240227602787, "o_others_sum": 799.7819159269861, "free_pool_f": 0.12248167073795}, {"K_target": 0.0007038135554931555, "o_target": 0.09542590579737843, "o_others_sum": 799.7820922946179, "free_pool_f": 0.12248179958468586}, {"K_target": 0.00103979841848149, "o_target": 0.09516634384776076, "o_others_sum": 799.7823516670808, "free_pool_f": 0.12248198907141511}, {"K_target": 0.0015361749466718281, "o_target": 0.09478544795907312, "o_others_sum": 799.7827322849055, "free_pool_f": 0.12248226713533339}, {"K_target": 0.0022695105366946685, "o_target": 0.09422827087096113, "o_others_sum": 799.7832890552392, "free_pool_f": 0.1224826738899159}, {"K_target": 0.0033529241492495565, "o_target": 0.09341700062306332, "o_others_sum": 799.7840997332355, "free_pool_f": 0.12248326614118057}, {"K_target": 0.00495353520895917, "o_target": 0.0922437046253485, "o_others_sum": 799.785272172689, "free_pool_f": 0.12248412268549957}, {"K_target": 0.007318242219076174, "o_target": 0.09056328303120176, "o_others_sum": 799.7869513675133, "free_pool_f": 0.12248534945535175}, {"K_target": 0.010811807510766078, "o_target": 0.088189824652808, "o_others_sum": 799.789323093165, "free_pool_f": 0.1224870821823491}, {"K_target": 0.01597312280060254, "o_target": 0.08490260634861115, "o_others_sum": 799.7926079116295, "free_pool_f": 0.12248948202191048}, {"K_target": 0.02359833466782194, "o_target": 0.08047136613309178, "o_others_sum": 799.797035916758, "free_pool_f": 0.12249271710890569}, {"K_target": 0.03486365227678084, "o_target": 0.07471089977005148, "o_others_sum": 799.8027921775249, "free_pool_f": 0.12249692270508414}, {"K_target": 0.05150678076168122, "o_target": 0.06756579375892219, "o_others_sum": 799.8099320669024, "free_pool_f": 0.12250213933850437}, {"K_target": 0.07609496685459875, "o_target": 0.05920164496838539, "o_others_sum": 799.81829010884, "free_pool_f": 0.12250824619162604}, {"K_target": 0.11242100350620862, "o_target": 0.05004887146974832, "o_others_sum": 799.827436199448, "free_pool_f": 0.12251492908212183}, {"K_target": 0.1660882782627715, "o_target": 0.040743322569339345, "o_others_sum": 799.8367349536468, "free_pool_f": 0.1225217237836643}, {"K_target": 0.24537511066398168, "o_target": 0.03196369111203031, "o_others_sum": 799.8455081741732, "free_pool_f": 0.12252813471456497}, {"K_target": 0.36251170499885316, "o_target": 0.024245327927261317, "o_others_sum": 799.8532209011764, "free_pool_f": 0.12253377089644851}, {"K_target": 0.5355666917706896, "o_target": 0.01787029624392308, "o_others_sum": 799.8595912774817, "free_pool_f": 0.12253842627426575}, {"K_target": 0.7912342618981318, "o_target": 0.012870637293745307, "o_others_sum": 799.8645872853357, "free_pool_f": 0.12254207737060796}, {"K_target": 1.1689518164985777, "o_target": 0.009106603344113059, "o_others_sum": 799.8683485704772, "free_pool_f": 0.1225448261785787}, {"K_target": 1.7269832906594325, "o_target": 0.0063590963280658105, "o_others_sum": 799.8710940710098, "free_pool_f": 0.12254683266207389}, {"K_target": 2.5514065200312874, "o_target": 0.004398532727586196, "o_others_sum": 799.8730532028113, "free_pool_f": 0.12254826446086525}, {"K_target": 3.7693909753883634, "o_target": 0.0030220335797495326, "o_others_sum": 799.8744286966955, "free_pool_f": 0.12254926972464}, {"K_target": 5.568813990945267, "o_target": 0.002066576863769794, "o_others_sum": 799.8753834556338, "free_pool_f": 0.12254996750255659}, {"K_target": 8.227241341700458, "o_target": 0.0014086204174752906, "o_others_sum": 799.8760409315673, "free_pool_f": 0.12255044801519427}, {"K_target": 12.15474250076286, "o_target": 0.0009580058498702383, "o_others_sum": 799.8764912170454, "free_pool_f": 0.12255077710460038}, {"K_target": 17.957144943716408, "o_target": 0.0006505496755209149, "o_others_sum": 799.8767984486803, "free_pool_f": 0.12255100164401275}, {"K_target": 26.529484644318945, "o_target": 0.00044130793931140003, "o_others_sum": 799.8770075376043, "free_pool_f": 0.12255115445625456}, {"K_target": 39.19406774847213, "o_target": 0.0002991550458215114, "o_others_sum": 799.8771495866815, "free_pool_f": 0.12255125827262828}, {"K_target": 57.90443980602483, "o_target": 0.00020269484065155323, "o_others_sum": 799.8772459764405, "free_pool_f": 0.12255132871898691}, {"K_target": 85.54672535565685, "o_target": 0.00013729281668206406, "o_others_sum": 799.8773113307003, "free_pool_f": 0.12255137648309833}, {"K_target": 126.38482029342971, "o_target": 9.297307543300825e-05, "o_others_sum": 799.8773556180739, "free_pool_f": 0.1225514088504994}, {"K_target": 186.71810912919167, "o_target": 6.295086669656986e-05, "o_others_sum": 799.877385618357, "free_pool_f": 0.12255143077619204}, {"K_target": 275.85316176291815, "o_target": 4.261890586226935e-05, "o_others_sum": 799.8774059354691, "free_pool_f": 0.12255144562494535}, {"K_target": 407.5392965871778, "o_target": 2.885181422527283e-05, "o_others_sum": 799.8774196925062, "free_pool_f": 0.12255145567927123}, {"K_target": 602.0894493336125, "o_target": 1.9530970064076302e-05, "o_others_sum": 799.8774290065436, "free_pool_f": 0.12255146248643248}, {"K_target": 889.5134973108218, "o_target": 1.3220895239368841e-05, "o_others_sum": 799.87743531201, "free_pool_f": 0.12255146709478074}, {"K_target": 1314.1473626117554, "o_target": 8.949292055945583e-06, "o_others_sum": 799.8774395804935, "free_pool_f": 0.1225514702144008}, {"K_target": 1941.4919457438816, "o_target": 6.0577346950175825e-06, "o_others_sum": 799.8774424699391, "free_pool_f": 0.12255147232615149}, {"K_target": 2868.316813342009, "o_target": 4.100412853622533e-06, "o_others_sum": 799.8774444258314, "free_pool_f": 0.12255147375561487}, {"K_target": 4237.587160604055, "o_target": 2.7755052925563788e-06, "o_others_sum": 799.8774457497715, "free_pool_f": 0.12255147472321606}, {"K_target": 6260.516572014815, "o_target": 1.8786877130356869e-06, "o_others_sum": 799.8774466459341, "free_pool_f": 0.12255147537817637}, {"K_target": 9249.147277217335, "o_target": 1.2716447954748376e-06, "o_others_sum": 799.8774472525336, "free_pool_f": 0.12255147582150941}, {"K_target": 13664.483492953244, "o_target": 8.607482594198445e-07, "o_others_sum": 799.8774476631299, "free_pool_f": 0.12255147612159376}, {"K_target": 20187.60254679035, "o_target": 5.826206682844482e-07, "o_others_sum": 799.8774479410545, "free_pool_f": 0.12255147632471486}, {"K_target": 29824.71286216882, "o_target": 3.9436213940376e-07, "o_others_sum": 799.8774481291755, "free_pool_f": 0.12255147646220299}, {"K_target": 44062.36427773573, "o_target": 2.6693422810226055e-07, "o_others_sum": 799.8774482565105, "free_pool_f": 0.12255147655526571}, {"K_target": 65096.75230458164, "o_target": 1.8068126837232937e-07, "o_others_sum": 799.8774483427004, "free_pool_f": 0.1225514766182576}, {"K_target": 96172.48711152945, "o_target": 1.2229870813918263e-07, "o_others_sum": 799.8774484010402, "free_pool_f": 0.12255147666089525}, {"K_target": 142083.08325339237, "o_target": 8.278097229226734e-08, "o_others_sum": 799.8774484405293, "free_pool_f": 0.12255147668975575}, {"K_target": 209910.37201085544, "o_target": 5.603238632412259e-08, "o_others_sum": 799.8774484672583, "free_pool_f": 0.12255147670929062}, {"K_target": 310116.8926574775, "o_target": 3.792692870511566e-08, "o_others_sum": 799.8774484853504, "free_pool_f": 0.1225514767225134}, {"K_target": 458159.76690544817, "o_target": 2.5671793183104634e-08, "o_others_sum": 799.8774484975968, "free_pool_f": 0.12255147673146355}, {"K_target": 676875.0009458513, "o_target": 1.7376596537839975e-08, "o_others_sum": 799.8774485058857, "free_pool_f": 0.12255147673752159}, {"K_target": 1000000.0, "o_target": 1.1761784486483168e-08, "o_others_sum": 799.8774485114965, "free_pool_f": 0.12255147674162217}] | true | true | 8.1532e+06 | 1.00012 |
| 0.1875 | 15000 | [{"K_target": 0.0001, "o_target": 0.09597424797378812, "o_others_sum": 4263.729089560424, "free_pool_f": 10736.1749361916}, {"K_target": 0.00014773776525985112, "o_target": 0.09597424754704433, "o_others_sum": 4263.729089560436, "free_pool_f": 10736.174936192016}, {"K_target": 0.00021826447283974872, "o_target": 0.09597424691658257, "o_others_sum": 4263.729089560454, "free_pool_f": 10736.174936192627}, {"K_target": 0.00032245905452963947, "o_target": 0.09597424598515249, "o_others_sum": 4263.729089560479, "free_pool_f": 10736.174936193533}, {"K_target": 0.00047639380104013405, "o_target": 0.09597424460907857, "o_others_sum": 4263.729089560518, "free_pool_f": 10736.174936194871}, {"K_target": 0.0007038135554931555, "o_target": 0.09597424257609774, "o_others_sum": 4263.729089560576, "free_pool_f": 10736.174936196847}, {"K_target": 0.00103979841848149, "o_target": 0.09597423957261747, "o_others_sum": 4263.72908956066, "free_pool_f": 10736.174936199764}, {"K_target": 0.0015361749466718281, "o_target": 0.09597423513534317, "o_others_sum": 4263.729089560785, "free_pool_f": 10736.17493620408}, {"K_target": 0.0022695105366946685, "o_target": 0.09597422857981407, "o_others_sum": 4263.729089560969, "free_pool_f": 10736.17493621045}, {"K_target": 0.0033529241492495565, "o_target": 0.09597421889482347, "o_others_sum": 4263.7290895612405, "free_pool_f": 10736.174936219864}, {"K_target": 0.00495353520895917, "o_target": 0.09597420458643839, "o_others_sum": 4263.729089561643, "free_pool_f": 10736.174936233769}, {"K_target": 0.007318242219076174, "o_target": 0.09597418344755783, "o_others_sum": 4263.729089562237, "free_pool_f": 10736.174936254316}, {"K_target": 0.010811807510766078, "o_target": 0.0959741522174651, "o_others_sum": 4263.729089563115, "free_pool_f": 10736.174936284668}, {"K_target": 0.01597312280060254, "o_target": 0.09597410607886125, "o_others_sum": 4263.729089564411, "free_pool_f": 10736.17493632951}, {"K_target": 0.02359833466782194, "o_target": 0.09597403791480018, "o_others_sum": 4263.729089566326, "free_pool_f": 10736.174936395757}, {"K_target": 0.03486365227678084, "o_target": 0.09597393721091685, "o_others_sum": 4263.729089569156, "free_pool_f": 10736.174936493633}, {"K_target": 0.05150678076168122, "o_target": 0.09597378843363681, "o_others_sum": 4263.729089573337, "free_pool_f": 10736.174936638228}, {"K_target": 0.07609496685459875, "o_target": 0.09597356863425217, "o_others_sum": 4263.729089579511, "free_pool_f": 10736.174936851854}, {"K_target": 0.11242100350620862, "o_target": 0.09597324390939568, "o_others_sum": 4263.729089588635, "free_pool_f": 10736.174937167452}, {"K_target": 0.1660882782627715, "o_target": 0.09597276417217075, "o_others_sum": 4263.729089602116, "free_pool_f": 10736.17493763371}, {"K_target": 0.24537511066398168, "o_target": 0.09597205542789243, "o_others_sum": 4263.72908962203, "free_pool_f": 10736.17493832254}, {"K_target": 0.36251170499885316, "o_target": 0.0959710083640906, "o_others_sum": 4263.72908965145, "free_pool_f": 10736.174939340184}, {"K_target": 0.5355666917706896, "o_target": 0.0959694614972391, "o_others_sum": 4263.7290896949135, "free_pool_f": 10736.174940843586}, {"K_target": 0.7912342618981318, "o_target": 0.09596717628197332, "o_others_sum": 4263.729089759123, "free_pool_f": 10736.174943064594}, {"K_target": 1.1689518164985777, "o_target": 0.09596380035516426, "o_others_sum": 4263.7290898539795, "free_pool_f": 10736.174946345665}, {"K_target": 1.7269832906594325, "o_target": 0.09595881327097833, "o_others_sum": 4263.729089994106, "free_pool_f": 10736.174951192621}, {"K_target": 2.5514065200312874, "o_target": 0.09595144641275649, "o_others_sum": 4263.729090201098, "free_pool_f": 10736.174958352487}, {"K_target": 3.7693909753883634, "o_target": 0.09594056485080027, "o_others_sum": 4263.729090506848, "free_pool_f": 10736.174968928302}, {"K_target": 5.568813990945267, "o_target": 0.09592449319025521, "o_others_sum": 4263.729090958427, "free_pool_f": 10736.174984548383}, {"K_target": 8.227241341700458, "o_target": 0.09590075912955572, "o_others_sum": 4263.729091625303, "free_pool_f": 10736.175007615566}, {"K_target": 12.15474250076286, "o_target": 0.0958657164440691, "o_others_sum": 4263.729092609927, "free_pool_f": 10736.175041673629}, {"K_target": 17.957144943716408, "o_target": 0.09581399200460886, "o_others_sum": 4263.729094063272, "free_pool_f": 10736.175091944722}, {"K_target": 26.529484644318945, "o_target": 0.09573767753698195, "o_others_sum": 4263.729096207545, "free_pool_f": 10736.175166114917}, {"K_target": 39.19406774847213, "o_target": 0.09562515445690246, "o_others_sum": 4263.729099369201, "free_pool_f": 10736.17527547634}, {"K_target": 57.90443980602483, "o_target": 0.09545939858125566, "o_others_sum": 4263.7291040265845, "free_pool_f": 10736.175436574831}, {"K_target": 85.54672535565685, "o_target": 0.09521556347491135, "o_others_sum": 4263.729110877827, "free_pool_f": 10736.175673558697}, {"K_target": 126.38482029342971, "o_target": 0.09485759798100671, "o_others_sum": 4263.729120935886, "free_pool_f": 10736.17602146613}, {"K_target": 186.71810912919167, "o_target": 0.09433364618275754, "o_others_sum": 4263.729135657804, "free_pool_f": 10736.176530696011}, {"K_target": 275.85316176291815, "o_target": 0.09357007825129594, "o_others_sum": 4263.729157112418, "free_pool_f": 10736.177272809331}, {"K_target": 407.5392965871778, "o_target": 0.09246435395442835, "o_others_sum": 4263.729188180884, "free_pool_f": 10736.17834746516}, {"K_target": 602.0894493336125, "o_target": 0.09087778476686545, "o_others_sum": 4263.729232760051, "free_pool_f": 10736.179889455183}, {"K_target": 889.5134973108218, "o_target": 0.08863099880195303, "o_others_sum": 4263.729295889871, "free_pool_f": 10736.182073111326}, {"K_target": 1314.1473626117554, "o_target": 0.08550779025922721, "o_others_sum": 4263.729383645247, "free_pool_f": 10736.185108564492}, {"K_target": 1941.4919457438816, "o_target": 0.08127651126686043, "o_others_sum": 4263.729502534955, "free_pool_f": 10736.189220953776}, {"K_target": 2868.316813342009, "o_target": 0.07573945003798206, "o_others_sum": 4263.7296581142255, "free_pool_f": 10736.194602435735}, {"K_target": 4237.587160604055, "o_target": 0.06881350428373927, "o_others_sum": 4263.729852717994, "free_pool_f": 10736.20133377772}, {"K_target": 6260.516572014815, "o_target": 0.06062341834490753, "o_others_sum": 4263.730082841149, "free_pool_f": 10736.209293740503}, {"K_target": 9249.147277217335, "o_target": 0.05155774981278115, "o_others_sum": 4263.730337566024, "free_pool_f": 10736.218104684162}, {"K_target": 13664.483492953244, "o_target": 0.04222833312736383, "o_others_sum": 4263.730599701411, "free_pool_f": 10736.22717196546}, {"K_target": 20187.60254679035, "o_target": 0.03332064269825162, "o_others_sum": 4263.73084998704, "free_pool_f": 10736.23582937026}, {"K_target": 29824.71286216882, "o_target": 0.02540381193306911, "o_others_sum": 4263.731072431621, "free_pool_f": 10736.243523756446}, {"K_target": 44062.36427773573, "o_target": 0.0188034595081108, "o_others_sum": 4263.731257886091, "free_pool_f": 10736.2499386544}, {"K_target": 65096.75230458164, "o_target": 0.013587803603492345, "o_others_sum": 4263.731404433749, "free_pool_f": 10736.255007762647}, {"K_target": 96172.48711152945, "o_target": 0.00963816729119789, "o_others_sum": 4263.731515409189, "free_pool_f": 10736.25884642352}, {"K_target": 142083.08325339237, "o_target": 0.006742632283258354, "o_others_sum": 4263.73159676685, "free_pool_f": 10736.261660600867}, {"K_target": 209910.37201085544, "o_target": 0.0046699322591381345, "o_others_sum": 4263.731655004787, "free_pool_f": 10736.263675062954}, {"K_target": 310116.8926574775, "o_target": 0.0032114534422195457, "o_others_sum": 4263.731695984565, "free_pool_f": 10736.265092561993}, {"K_target": 458159.76690544817, "o_target": 0.0021975128813206714, "o_others_sum": 4263.731724473874, "free_pool_f": 10736.266078013243}, {"K_target": 676875.0009458513, "o_target": 0.001498528581596263, "o_others_sum": 4263.731744113662, "free_pool_f": 10736.266757357756}, {"K_target": 1000000.0, "o_target": 0.0010194599875181516, "o_others_sum": 4263.731757574344, "free_pool_f": 10736.267222965667}] | true | true | 94.1422 | 1 |
| 2 | 160000 | [{"K_target": 0.0001, "o_target": 0.09597424880580988, "o_others_sum": 4981.64270712769, "free_pool_f": 155018.2613186235}, {"K_target": 0.00014773776525985112, "o_target": 0.09597424877625468, "o_others_sum": 4981.642707127689, "free_pool_f": 155018.2613186235}, {"K_target": 0.00021826447283974872, "o_target": 0.0959742487325905, "o_others_sum": 4981.642707127689, "free_pool_f": 155018.26131862355}, {"K_target": 0.00032245905452963947, "o_target": 0.09597424866808198, "o_others_sum": 4981.642707127689, "free_pool_f": 155018.2613186236}, {"K_target": 0.00047639380104013405, "o_target": 0.09597424857277856, "o_others_sum": 4981.64270712769, "free_pool_f": 155018.26131862373}, {"K_target": 0.0007038135554931555, "o_target": 0.0959742484319794, "o_others_sum": 4981.64270712769, "free_pool_f": 155018.26131862384}, {"K_target": 0.00103979841848149, "o_target": 0.09597424822396587, "o_others_sum": 4981.64270712769, "free_pool_f": 155018.26131862408}, {"K_target": 0.0015361749466718281, "o_target": 0.09597424791665135, "o_others_sum": 4981.642707127691, "free_pool_f": 155018.26131862437}, {"K_target": 0.0022695105366946685, "o_target": 0.09597424746263174, "o_others_sum": 4981.642707127692, "free_pool_f": 155018.26131862483}, {"K_target": 0.0033529241492495565, "o_target": 0.09597424679187332, "o_others_sum": 4981.642707127692, "free_pool_f": 155018.26131862547}, {"K_target": 0.00495353520895917, "o_target": 0.09597424580090984, "o_others_sum": 4981.642707127694, "free_pool_f": 155018.26131862646}, {"K_target": 0.007318242219076174, "o_target": 0.09597424433688258, "o_others_sum": 4981.642707127697, "free_pool_f": 155018.26131862798}, {"K_target": 0.010811807510766078, "o_target": 0.0959742421739615, "o_others_sum": 4981.6427071276985, "free_pool_f": 155018.26131863013}, {"K_target": 0.01597312280060254, "o_target": 0.0959742389785104, "o_others_sum": 4981.642707127703, "free_pool_f": 155018.26131863333}, {"K_target": 0.02359833466782194, "o_target": 0.09597423425762275, "o_others_sum": 4981.642707127709, "free_pool_f": 155018.26131863805}, {"K_target": 0.03486365227678084, "o_target": 0.0959742272830897, "o_others_sum": 4981.642707127717, "free_pool_f": 155018.26131864497}, {"K_target": 0.05150678076168122, "o_target": 0.09597421697907227, "o_others_sum": 4981.642707127731, "free_pool_f": 155018.26131865528}, {"K_target": 0.07609496685459875, "o_target": 0.09597420175615126, "o_others_sum": 4981.64270712775, "free_pool_f": 155018.26131867047}, {"K_target": 0.11242100350620862, "o_target": 0.09597417926615676, "o_others_sum": 4981.64270712778, "free_pool_f": 155018.26131869294}, {"K_target": 0.1660882782627715, "o_target": 0.0959741460399608, "o_others_sum": 4981.642707127822, "free_pool_f": 155018.26131872612}, {"K_target": 0.24537511066398168, "o_target": 0.0959740969523635, "o_others_sum": 4981.642707127886, "free_pool_f": 155018.26131877513}, {"K_target": 0.36251170499885316, "o_target": 0.09597402443153609, "o_others_sum": 4981.642707127979, "free_pool_f": 155018.2613188476}, {"K_target": 0.5355666917706896, "o_target": 0.09597391729108692, "o_others_sum": 4981.642707128117, "free_pool_f": 155018.26131895458}, {"K_target": 0.7912342618981318, "o_target": 0.0959737590046194, "o_others_sum": 4981.6427071283215, "free_pool_f": 155018.26131911267}, {"K_target": 1.1689518164985777, "o_target": 0.095973525156685, "o_others_sum": 4981.642707128623, "free_pool_f": 155018.2613193462}, {"K_target": 1.7269832906594325, "o_target": 0.0959731796770581, "o_others_sum": 4981.642707129067, "free_pool_f": 155018.26131969126}, {"K_target": 2.5514065200312874, "o_target": 0.09597266927772957, "o_others_sum": 4981.642707129726, "free_pool_f": 155018.26132020098}, {"K_target": 3.7693909753883634, "o_target": 0.09597191523510235, "o_others_sum": 4981.642707130698, "free_pool_f": 155018.26132095407}, {"K_target": 5.568813990945267, "o_target": 0.09597080125105895, "o_others_sum": 4981.642707132133, "free_pool_f": 155018.2613220666}, {"K_target": 8.227241341700458, "o_target": 0.09596915552325283, "o_others_sum": 4981.642707134255, "free_pool_f": 155018.2613237102}, {"K_target": 12.15474250076286, "o_target": 0.09596672426505784, "o_others_sum": 4981.642707137389, "free_pool_f": 155018.26132613834}, {"K_target": 17.957144943716408, "o_target": 0.09596313260395589, "o_others_sum": 4981.64270714202, "free_pool_f": 155018.26132972538}, {"K_target": 26.529484644318945, "o_target": 0.09595782685606839, "o_others_sum": 4981.64270714886, "free_pool_f": 155018.26133502426}, {"K_target": 39.19406774847213, "o_target": 0.09594998933629637, "o_others_sum": 4981.642707158962, "free_pool_f": 155018.26134285168}, {"K_target": 57.90443980602483, "o_target": 0.09593841270238923, "o_others_sum": 4981.642707173885, "free_pool_f": 155018.2613544134}, {"K_target": 85.54672535565685, "o_target": 0.0959213147534025, "o_others_sum": 4981.642707195927, "free_pool_f": 155018.26137148932}, {"K_target": 126.38482029342971, "o_target": 0.0958960657754156, "o_others_sum": 4981.642707228475, "free_pool_f": 155018.26139670576}, {"K_target": 186.71810912919167, "o_target": 0.0958587878153349, "o_others_sum": 4981.642707276532, "free_pool_f": 155018.26143393567}, {"K_target": 275.85316176291815, "o_target": 0.09580376719777835, "o_others_sum": 4981.642707347458, "free_pool_f": 155018.26148888533}, {"K_target": 407.5392965871778, "o_target": 0.09572259645444152, "o_others_sum": 4981.642707452094, "free_pool_f": 155018.26156995143}, {"K_target": 602.0894493336125, "o_target": 0.0956029280075119, "o_others_sum": 4981.642707606359, "free_pool_f": 155018.2616894656}, {"K_target": 889.5134973108218, "o_target": 0.09542667906523117, "o_others_sum": 4981.642707833562, "free_pool_f": 155018.26186548738}, {"K_target": 1314.1473626117554, "o_target": 0.09516747881637982, "o_others_sum": 4981.642708167697, "free_pool_f": 155018.2621243535}, {"K_target": 1941.4919457438816, "o_target": 0.0947871086875622, "o_others_sum": 4981.642708658032, "free_pool_f": 155018.26250423328}, {"K_target": 2868.316813342009, "o_target": 0.0942306899667933, "o_others_sum": 4981.64270937531, "free_pool_f": 155018.26305993472}, {"K_target": 4237.587160604055, "o_target": 0.09342050128406332, "o_others_sum": 4981.642710419725, "free_pool_f": 155018.263869079}, {"K_target": 6260.516572014815, "o_target": 0.09224872236311948, "o_others_sum": 4981.6427119302625, "free_pool_f": 155018.26503934735}, {"K_target": 9249.147277217335, "o_target": 0.09057037757626091, "o_others_sum": 4981.642714093816, "free_pool_f": 155018.26671552862}, {"K_target": 13664.483492953244, "o_target": 0.08819966302907974, "o_others_sum": 4981.642717149902, "free_pool_f": 155018.26908318704}, {"K_target": 20187.60254679035, "o_target": 0.08491588685863438, "o_others_sum": 4981.642721383015, "free_pool_f": 155018.27236273012}, {"K_target": 29824.71286216882, "o_target": 0.08048864987304287, "o_others_sum": 4981.642727090162, "free_pool_f": 155018.27678425994}, {"K_target": 44062.36427773573, "o_target": 0.07473234322478452, "o_others_sum": 4981.64273451061, "free_pool_f": 155018.28253314615}, {"K_target": 65096.75230458164, "o_target": 0.06759085511941251, "o_others_sum": 4981.642743716696, "free_pool_f": 155018.28966542816}, {"K_target": 96172.48711152945, "o_target": 0.05922894307331128, "o_others_sum": 4981.642754496026, "free_pool_f": 155018.2980165609}, {"K_target": 142083.08325339237, "o_target": 0.05007639166414615, "o_others_sum": 4981.642766294568, "free_pool_f": 155018.30715731374}, {"K_target": 209910.37201085544, "o_target": 0.04076896926061908, "o_others_sum": 4981.642778292755, "free_pool_f": 155018.31645273796}, {"K_target": 310116.8926574775, "o_target": 0.03198589733088714, "o_others_sum": 4981.642789615, "free_pool_f": 155018.32522448763}, {"K_target": 458159.76690544817, "o_target": 0.024263371552542184, "o_others_sum": 4981.642799570095, "free_pool_f": 155018.33293705835}, {"K_target": 676875.0009458513, "o_target": 0.017884226205327487, "o_others_sum": 4981.642807793441, "free_pool_f": 155018.33930798032}, {"K_target": 1000000.0, "o_target": 0.012880980833532887, "o_others_sum": 4981.642814243116, "free_pool_f": 155018.34430477605}] | true | false | 7.45085 | 1 |


### `e7_offtarget_ranking`  (OK)

seed `0`, wall clock `38.1648` s, recorded `2026-09-05T03:39:18Z`

| quantity | value |
|---|---|
| `scoring_note` | K is thermodynamic (ViennaRNA duplex energy plus the pfl_fold opening cost on GENCODE v50 3'UTRs, anchored on the published seed-match Kd of Wee et al. 2012) and is never fitted to the expression response. |
| `sign_convention` | measured VALUE = log10(siRNA/mock); repression is NEGATIVE, so a working predictor gives a NEGATIVE Spearman against predicted bound fraction |
| `n_constructs_scored` | 24 |
| `rho_main` | 0.5 |
| `bootstrap_resamples` | 400 |
| `ANALYTIC_IDENTITY_within_construct` | Within one construct the bound fraction is f/(K_j+f) under equilibrium and M/(K_j+M) under independent occupancy. f and M are scalars shared by every transcript, and both are strictly decreasing in K_j, so the two orderings are identical at every rho and every rank statistic must agree exactly. T... |
| `within_construct_rank_statistics_identical_at_every_rho` | true |
| `within_construct_max_abs_spearman_difference_over_all_rho` | 1.6501e-05 |
| `within_construct_identity_tolerance` | 1.0000e-04 |
| `within_construct_identity_tolerance_note` | the residual difference is at the level of the bisection tolerance of the solver and of rank ties, not a real reordering |
| `positive_control_any_site_n_constructs_p_below_0.05` | 24 |
| `positive_control_any_site_n_constructs_tested` | 24 |
| `pooled_scorings_ever_diverge` | true |
| `phi_note` | r = phi(o) fitted by isotonic regression of the measured log ratio on predicted bound fraction, rather than assuming r = o/x |
| `LIMITATION_thermodynamic_K` | The purely thermodynamic K does not reproduce the site-class hierarchy that the same data shows (see positive_control_measured_repression_by_site_class and predictor_diagnostics_parent_construct). ViennaRNA duplexfold cannot see the t1 = A contribution, which is an Argonaute pocket effect rather ... |


**`constants_used`**

```json
{
  "kd_seed_match_molar": 2.6e-11,
  "kd_seed_match_molecules_per_cell": 46.972697928,
  "hela_cell_volume_litres": 3e-12,
  "anchor_site_class": "7mer-m8",
  "median_boltzmann_factor_anchor_class": 3.380290220755692e-08,
  "K_scale_constant_C": 1389605473.5057297,
  "mrna_molecules_per_cell": 80000.0,
  "ago2_copies_per_cell_low": 15000.0,
  "ago2_copies_per_cell_high": 170000.0
}
```


**`rho_swept`**: `[0.001, 0.01, 0.1, 0.5, 2.0, 10.0]`


**`positive_control_measured_repression_by_site_class`**

```json
{
  "6mer": {
    "n_constructs": 24,
    "mean_of_median_log10ratio": -0.005248958333333334,
    "mean_of_mean_log10ratio": -0.011317618290383814,
    "n_constructs_with_p_below_0.05": 22
  },
  "7mer-A1": {
    "n_constructs": 24,
    "mean_of_median_log10ratio": -0.013808854166666667,
    "mean_of_mean_log10ratio": -0.029863745963492765,
    "n_constructs_with_p_below_0.05": 22
  },
  "7mer-m8": {
    "n_constructs": 24,
    "mean_of_median_log10ratio": -0.009256770833333332,
    "mean_of_mean_log10ratio": -0.021828892213300838,
    "n_constructs_with_p_below_0.05": 22
  },
  "8mer": {
    "n_constructs": 23,
    "mean_of_median_log10ratio": -0.025564130434782607,
    "mean_of_mean_log10ratio": -0.053262008517335604,
    "n_constructs_with_p_below_0.05": 22
  }
}
```


**`positive_control_detail`**

| construct | site_class | n_with_site | n_no_site | median_log10ratio_with_site | mean_log10ratio_with_site | median_log10ratio_no_site | mann_whitney_p_less |
|---|---|---|---|---|---|---|---|
| MAPK14-193_parent | 6mer | 573 | 10320 | -0.0028 | -0.00916545 | 0.0012 | 1.9405e-04 |
| MAPK14-193_parent | 7mer-A1 | 81 | 10320 | -0.0229 | -0.0320083 | 0.0012 | 2.9437e-05 |
| MAPK14-193_parent | 7mer-m8 | 267 | 10320 | -0.01045 | -0.0215201 | 0.0012 | 3.6112e-07 |
| MAPK14-193_parent | 8mer | 28 | 10320 | -0.013775 | -0.0555652 | 0.0012 | 0.0215038 |
| MAPK14-193_parent | ANY | 949 | 10320 | -0.006375 | -0.0159601 | 0.0012 | 9.1555e-12 |
| MAPK14-193_pos01mut | 6mer | 571 | 10338 | -0.006375 | -0.0094581 | 0.0025 | 8.4515e-06 |
| MAPK14-193_pos01mut | 7mer-A1 | 84 | 10338 | -0.0119875 | -0.0263006 | 0.0025 | 1.0201e-04 |
| MAPK14-193_pos01mut | 7mer-m8 | 267 | 10338 | -0.0073 | -0.018832 | 0.0025 | 2.3344e-05 |
| MAPK14-193_pos01mut | 8mer | 28 | 10338 | -0.00645 | -0.0460036 | 0.0025 | 0.0349951 |
| MAPK14-193_pos01mut | ANY | 950 | 10338 | -0.007325 | -0.014659 | 0.0025 | 8.4524e-12 |
| MAPK14-193_pos02mut | 6mer | 315 | 10522 | -0.00935 | -0.0140429 | -9.7500e-04 | 2.2996e-04 |
| MAPK14-193_pos02mut | 7mer-A1 | 108 | 10522 | -0.01705 | -0.0277887 | -9.7500e-04 | 5.0827e-05 |
| MAPK14-193_pos02mut | 7mer-m8 | 236 | 10522 | -0.0119875 | -0.0238589 | -9.7500e-04 | 8.6124e-06 |
| MAPK14-193_pos02mut | 8mer | 84 | 10522 | -0.026475 | -0.0417762 | -9.7500e-04 | 1.8795e-06 |
| MAPK14-193_pos02mut | ANY | 743 | 10522 | -0.01355 | -0.0222942 | -9.7500e-04 | 2.1341e-14 |
| MAPK14-193_pos03mut | 6mer | 438 | 10569 | -0.0016 | -0.0061766 | 0.00635 | 0.00147047 |
| MAPK14-193_pos03mut | 7mer-A1 | 86 | 10569 | -0.025675 | -0.0494916 | 0.00635 | 2.8833e-07 |
| MAPK14-193_pos03mut | 7mer-m8 | 163 | 10569 | 0.0076 | -0.0143379 | 0.00635 | 0.192779 |
| MAPK14-193_pos03mut | 8mer | 31 | 10569 | -0.0492 | -0.0949984 | 0.00635 | 5.3847e-05 |
| MAPK14-193_pos03mut | ANY | 718 | 10569 | -0.002375 | -0.0170524 | 0.00635 | 1.2507e-07 |
| MAPK14-193_pos04mut | 6mer | 2667 | 6361 | 0.0027 | 6.2123e-04 | 0.005 | 0.00446309 |
| MAPK14-193_pos04mut | 7mer-A1 | 535 | 6361 | -0.0061 | -0.0208332 | 0.005 | 1.6036e-11 |
| MAPK14-193_pos04mut | 7mer-m8 | 1432 | 6361 | -0.0033 | -0.0120651 | 0.005 | 2.0111e-15 |
| MAPK14-193_pos04mut | 8mer | 269 | 6361 | -0.0167 | -0.0380117 | 0.005 | 1.2756e-14 |
| MAPK14-193_pos04mut | ANY | 4903 | 6361 | -9.0000e-04 | -0.00754464 | 0.005 | 3.6550e-17 |
| MAPK14-193_pos05mut | 6mer | 1843 | 7312 | -0.0015 | -0.00769811 | 0.00305 | 1.6404e-08 |
| MAPK14-193_pos05mut | 7mer-A1 | 407 | 7312 | -0.01115 | -0.0216015 | 0.00305 | 7.8385e-11 |
| MAPK14-193_pos05mut | 7mer-m8 | 1335 | 7312 | -0.00405 | -0.00587375 | 0.00305 | 4.4183e-06 |
| MAPK14-193_pos05mut | 8mer | 224 | 7312 | -0.010675 | -0.0219288 | 0.00305 | 3.7433e-05 |
| MAPK14-193_pos05mut | ANY | 3809 | 7312 | -0.003925 | -0.00938119 | 0.00305 | 3.6986e-17 |
| MAPK14-193_pos06mut | 6mer | 367 | 10688 | -0.0078 | -0.0162271 | -0.0012 | 8.9543e-08 |
| MAPK14-193_pos06mut | 7mer-A1 | 109 | 10688 | -0.02785 | -0.0502073 | -0.0012 | 1.4124e-11 |
| MAPK14-193_pos06mut | 7mer-m8 | 79 | 10688 | -0.0102 | -0.0306475 | -0.0012 | 4.0760e-04 |
| MAPK14-193_pos06mut | 8mer | 26 | 10688 | -0.034375 | -0.0628663 | -0.0012 | 5.3275e-07 |
| MAPK14-193_pos06mut | ANY | 581 | 10688 | -0.01215 | -0.02665 | -0.0012 | 3.0162e-20 |
| MAPK14-193_pos07mut | 6mer | 599 | 10548 | -0.0081 | -0.0237634 | 7.0000e-04 | 3.5456e-05 |
| MAPK14-193_pos07mut | 7mer-A1 | 85 | 10548 | -0.0076 | -0.0233694 | 7.0000e-04 | 0.23096 |
| MAPK14-193_pos07mut | 7mer-m8 | 62 | 10548 | 1.0000e-04 | -0.0189427 | 7.0000e-04 | 0.361284 |
| MAPK14-193_pos07mut | ANY | 752 | 10548 | -0.00755 | -0.0234373 | 7.0000e-04 | 4.1047e-05 |
| MAPK14-193_pos08mut | 6mer | 693 | 10347 | -0.0064 | -0.010907 | 8.0000e-04 | 1.1621e-05 |
| MAPK14-193_pos08mut | 7mer-A1 | 82 | 10347 | -0.0135 | -0.033597 | 8.0000e-04 | 0.00109374 |
| MAPK14-193_pos08mut | 7mer-m8 | 147 | 10347 | -0.0144 | -0.0339495 | 8.0000e-04 | 6.0754e-06 |
| MAPK14-193_pos08mut | 8mer | 29 | 10347 | -0.0139 | -0.037406 | 8.0000e-04 | 0.0102022 |
| MAPK14-193_pos08mut | ANY | 951 | 10347 | -0.0084 | -0.0172333 | 8.0000e-04 | 4.5699e-11 |
| MAPK14-193_pos09mut | 6mer | 574 | 10343 | -0.0072 | -0.0330601 | 4.0000e-04 | 9.6324e-04 |
| MAPK14-193_pos09mut | 7mer-A1 | 83 | 10343 | -0.01715 | -0.0610087 | 4.0000e-04 | 0.0013587 |
| MAPK14-193_pos09mut | 7mer-m8 | 267 | 10343 | -0.0103 | -0.0291487 | 4.0000e-04 | 0.00327513 |
| MAPK14-193_pos09mut | 8mer | 27 | 10343 | -0.056 | -0.136544 | 4.0000e-04 | 0.00300596 |
| MAPK14-193_pos09mut | ANY | 951 | 10343 | -0.00935 | -0.0373393 | 4.0000e-04 | 2.0989e-07 |
| MAPK14-193_pos10mut | 6mer | 573 | 10343 | -0.0035 | -0.0115928 | 0.0042 | 8.1101e-06 |
| MAPK14-193_pos10mut | 7mer-A1 | 82 | 10343 | -0.02025 | -0.0328512 | 0.0042 | 7.5559e-04 |
| MAPK14-193_pos10mut | 7mer-m8 | 267 | 10343 | -0.0112 | -0.0245204 | 0.0042 | 1.5433e-06 |
| MAPK14-193_pos10mut | 8mer | 28 | 10343 | -0.034175 | -0.0597268 | 0.0042 | 0.0014269 |
| MAPK14-193_pos10mut | ANY | 950 | 10343 | -0.0074 | -0.0184798 | 0.0042 | 7.4438e-13 |
| MAPK14-193_pos11mut | 6mer | 574 | 10336 | -0.00655 | -0.00872409 | 0.0028 | 4.3474e-04 |
| MAPK14-193_pos11mut | 7mer-A1 | 80 | 10336 | -0.01595 | -0.0304744 | 0.0028 | 0.00180922 |
| MAPK14-193_pos11mut | 7mer-m8 | 269 | 10336 | -0.0064 | -0.0194705 | 0.0028 | 6.2778e-04 |
| MAPK14-193_pos11mut | 8mer | 27 | 10336 | -0.01985 | -0.0527519 | 0.0028 | 0.0208764 |
| MAPK14-193_pos11mut | ANY | 950 | 10336 | -0.00725 | -0.0148499 | 0.0028 | 4.4268e-08 |
| MAPK14-193_pos12mut | 6mer | 574 | 10335 | -0.010575 | -0.0107943 | -0.004825 | 0.00374004 |
| MAPK14-193_pos12mut | 7mer-A1 | 81 | 10335 | -0.0133 | -0.0336392 | -0.004825 | 0.00116446 |
| MAPK14-193_pos12mut | 7mer-m8 | 266 | 10335 | -0.020225 | -0.0237406 | -0.004825 | 1.0570e-06 |
| MAPK14-193_pos12mut | 8mer | 28 | 10335 | -0.0385 | -0.0648964 | -0.004825 | 6.3200e-04 |
| MAPK14-193_pos12mut | ANY | 949 | 10335 | -0.01245 | -0.0179692 | -0.004825 | 2.2571e-09 |
| MAPK14-193_pos13mut | 6mer | 568 | 10325 | -0.00625 | -0.0124925 | 0.0034 | 2.5577e-06 |
| MAPK14-193_pos13mut | 7mer-A1 | 83 | 10325 | -0.0135 | -0.0406184 | 0.0034 | 1.4689e-04 |
| MAPK14-193_pos13mut | 7mer-m8 | 269 | 10325 | -0.009 | -0.0218882 | 0.0034 | 3.9833e-05 |
| MAPK14-193_pos13mut | 8mer | 28 | 10325 | -0.02535 | -0.0571946 | 0.0034 | 0.00486944 |
| MAPK14-193_pos13mut | ANY | 948 | 10325 | -0.007725 | -0.0189414 | 0.0034 | 1.6743e-12 |
| MAPK14-193_pos14mut | 6mer | 572 | 10327 | -0.00645 | -0.0224626 | 0.0088 | 3.1790e-05 |
| MAPK14-193_pos14mut | 7mer-A1 | 80 | 10327 | -0.00815 | -0.0398212 | 0.0088 | 0.0164254 |
| MAPK14-193_pos14mut | 7mer-m8 | 269 | 10327 | -0.0044 | -0.0177581 | 0.0088 | 0.0253639 |
| MAPK14-193_pos14mut | 8mer | 27 | 10327 | -0.04875 | -0.0692704 | 0.0088 | 0.0110965 |
| MAPK14-193_pos14mut | ANY | 948 | 10327 | -0.00715 | -0.0239257 | 0.0088 | 2.4712e-07 |
| MAPK14-193_pos15mut | 6mer | 569 | 10311 | -0.0054 | -0.012673 | 0.00205 | 5.1625e-04 |
| MAPK14-193_pos15mut | 7mer-A1 | 85 | 10311 | -0.0104 | -0.0314903 | 0.00205 | 0.00918918 |
| MAPK14-193_pos15mut | 7mer-m8 | 268 | 10311 | -0.01275 | -0.0317716 | 0.00205 | 2.2452e-07 |
| MAPK14-193_pos15mut | 8mer | 27 | 10311 | -0.0265 | -0.0785852 | 0.00205 | 0.00280244 |
| MAPK14-193_pos15mut | ANY | 949 | 10311 | -0.00895 | -0.0216272 | 0.00205 | 2.4366e-10 |
| MAPK14-193_pos16mut | 6mer | 567 | 10325 | -0.001 | -0.00136301 | 0.002 | 0.131692 |

_119 rows total, first 80 shown; full data in the JSON._


**`per_rho_within_construct`**

| rho | n_constructs | mean_spearman_equilibrium | sd_spearman_equilibrium | mean_spearman_independent | sd_spearman_independent | mean_spearman_difference | max_abs_spearman_difference | mean_kendall_between_scorings_within_construct | min_kendall_between_scorings_within_construct | wilcoxon_statistic_paired_across_constructs | wilcoxon_p_paired_across_constructs | mean_f_over_M | min_f_over_M | max_f_over_M | per_construct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.001 | 24 | -0.0656005 | 0.0431399 | -0.0655998 | 0.0431395 | -7.5280e-07 | 1.3288e-05 | 0.999996 | 0.999983 | 79 | 0.777118 | 5.9200e-05 | 2.4090e-08 | 7.9819e-04 | [{"n_transcripts": 949, "spearman_equilibrium": -0.08307691482541965, "spearman_p_equilibrium": 0.010457931382571636, "kendall_equilibrium": -0.056674833502767585, "spearman_independent": -0.08306953331357741, "spearman_p_independent": 0.010464803488803345, "kendall_independent": -0.0566726732569599, "spearman_difference_eq_minus_ind": -7.38151184223601e-06, "kendall_between_the_two_scorings": 0.9999833268314151, "pairwise_ranking_accuracy_equilibrium": 0.5277043533982138, "pairwise_ranking_accuracy_independent": 0.5277043533982138, "construct": "MAPK14-193_parent", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.00012587095680657498, "f_over_M": 1.5733869600821874e-06}, {"n_transcripts": 950, "spearman_equilibrium": -0.0927578144297314, "spearman_p_equilibrium": 0.004217816240869713, "kendall_equilibrium": -0.06330789061807642, "spearman_independent": -0.09274452598526292, "spearman_p_independent": 0.004223297300441577, "kendall_independent": -0.06329471986878236, "spearman_difference_eq_minus_ind": -1.3288444468476102e-05, "kendall_between_the_two_scorings": 0.9999911263565235, "pairwise_ranking_accuracy_equilibrium": 0.530385938211838, "pairwise_ranking_accuracy_independent": 0.530385938211838, "construct": "MAPK14-193_pos01mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.00010950974926316221, "f_over_M": 1.3688718657895277e-06}, {"n_transcripts": 743, "spearman_equilibrium": -0.11277689287573685, "spearman_p_equilibrium": 0.0020788726492119917, "kendall_equilibrium": -0.0752725037638355, "spearman_independent": -0.11277813708270523, "spearman_p_independent": 0.0020786341423314, "kendall_independent": -0.0752762682459009, "spearman_difference_eq_minus_ind": 1.2442069683843426e-06, "kendall_between_the_two_scorings": 0.9999981861236648, "pairwise_ranking_accuracy_equilibrium": 0.5385728592889334, "pairwise_ranking_accuracy_independent": 0.5385728592889334, "construct": "MAPK14-193_pos02mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.0001437660288187728, "f_over_M": 1.7970753602346602e-06}, {"n_transcripts": 718, "spearman_equilibrium": -0.035454868170593165, "spearman_p_equilibrium": 0.34278608766977836, "kendall_equilibrium": -0.023779041618543797, "spearman_independent": -0.035454868170593165, "spearman_p_independent": 0.34278608766977836, "kendall_independent": -0.023779041618543797, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.5105482484698528, "pairwise_ranking_accuracy_independent": 0.5105482484698528, "construct": "MAPK14-193_pos03mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.013015048757182839, "f_over_M": 0.0001626881094647855}, {"n_transcripts": 4903, "spearman_equilibrium": -0.05050935271753931, "spearman_p_equilibrium": 0.0004030274744785883, "kendall_equilibrium": -0.033708064763731026, "spearman_independent": -0.0505092465551706, "spearman_p_independent": 0.00040303884019337363, "kendall_independent": -0.03370814939292792, "spearman_difference_eq_minus_ind": -1.0616236871541229e-07, "kendall_between_the_two_scorings": 0.9999997919657602, "pairwise_ranking_accuracy_equilibrium": 0.5181601696950292, "pairwise_ranking_accuracy_independent": 0.5181601696950292, "construct": "MAPK14-193_pos04mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 4.4554870101574755e-05, "f_over_M": 5.569358762696844e-07}, {"n_transcripts": 3809, "spearman_equilibrium": 0.028091360126263263, "spearman_p_equilibrium": 0.08300857524584336, "kendall_equilibrium": 0.018871894861059085, "spearman_independent": 0.028091307197346687, "spearman_p_independent": 0.08300915551493411, "kendall_independent": 0.018871619073091102, "spearman_difference_eq_minus_ind": 5.2928916575989415e-08, "kendall_between_the_two_scorings": 0.9999995863400665, "pairwise_ranking_accuracy_equilibrium": 0.49036023465514395, "pairwise_ranking_accuracy_independent": 0.49036023465514395, "construct": "MAPK14-193_pos05mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 1.9271822671214477e-06, "f_over_M": 2.4089778339018096e-08}, {"n_transcripts": 581, "spearman_equilibrium": -0.08951259872803471, "spearman_p_equilibrium": 0.0309829251876887, "kendall_equilibrium": -0.059984032818233245, "spearman_independent": -0.08951259872803471, "spearman_p_independent": 0.0309829251876887, "kendall_independent": -0.059984032818233245, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999999, "pairwise_ranking_accuracy_equilibrium": 0.5296950079918228, "pairwise_ranking_accuracy_independent": 0.5296950079918228, "construct": "MAPK14-193_pos06mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.029107317083142188, "f_over_M": 0.00036384146353927733}, {"n_transcripts": 752, "spearman_equilibrium": 0.026952184067538253, "spearman_p_equilibrium": 0.46051199996351344, "kendall_equilibrium": 0.015598215038033235, "spearman_independent": 0.026952184067538253, "spearman_p_independent": 0.46051199996351344, "kendall_independent": 0.015598215038033235, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4912066340838074, "pairwise_ranking_accuracy_independent": 0.4912066340838074, "construct": "MAPK14-193_pos07mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.00011937129785595196, "f_over_M": 1.4921412231993994e-06}, {"n_transcripts": 951, "spearman_equilibrium": -0.03504310516763995, "spearman_p_equilibrium": 0.2803294066446322, "kendall_equilibrium": -0.023132931592382538, "spearman_independent": -0.035045092612376996, "spearman_p_independent": 0.28030211332594746, "kendall_independent": -0.02313949705862236, "spearman_difference_eq_minus_ind": 1.9874447370477055e-06, "kendall_between_the_two_scorings": 0.9999966793680838, "pairwise_ranking_accuracy_equilibrium": 0.5123342128584232, "pairwise_ranking_accuracy_independent": 0.5123342128584232, "construct": "MAPK14-193_pos08mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.0012259442915006189, "f_over_M": 1.5324303643757735e-05}, {"n_transcripts": 951, "spearman_equilibrium": -0.07516245461047316, "spearman_p_equilibrium": 0.02044320148874819, "kendall_equilibrium": -0.049639400002518874, "spearman_independent": -0.07515627843617632, "spearman_p_independent": 0.020453582691637134, "kendall_independent": -0.0496346973662164, "spearman_difference_eq_minus_ind": -6.176174296837478e-06, "kendall_between_the_two_scorings": 0.9999944656318506, "pairwise_ranking_accuracy_equilibrium": 0.5253331864742813, "pairwise_ranking_accuracy_independent": 0.5253305563760707, "construct": "MAPK14-193_pos09mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 5.737683301868198e-06, "f_over_M": 7.172104127335247e-08}, {"n_transcripts": 950, "spearman_equilibrium": -0.036741772542910715, "spearman_p_equilibrium": 0.25790843442281874, "kendall_equilibrium": -0.0246140877181472, "spearman_independent": -0.03674174416476396, "spearman_p_independent": 0.2579088023115762, "kendall_independent": -0.0246140331140329, "spearman_difference_eq_minus_ind": -2.837814675610284e-08, "kendall_between_the_two_scorings": 0.9999977815909764, "pairwise_ranking_accuracy_equilibrium": 0.5109928350048317, "pairwise_ranking_accuracy_independent": 0.5109928350048317, "construct": "MAPK14-193_pos10mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 3.4271708529866262e-06, "f_over_M": 4.2839635662332825e-08}, {"n_transcripts": 950, "spearman_equilibrium": -0.09966220442276137, "spearman_p_equilibrium": 0.0021021283640688514, "kendall_equilibrium": -0.06707062807130494, "spearman_independent": -0.09966505335358392, "spearman_p_independent": 0.0021015056425839813, "kendall_independent": -0.0670773587273438, "spearman_difference_eq_minus_ind": 2.8489308225437826e-06, "kendall_between_the_two_scorings": 0.9999966723796977, "pairwise_ranking_accuracy_equilibrium": 0.5339455789125798, "pairwise_ranking_accuracy_independent": 0.5339455789125798, "construct": "MAPK14-193_pos11mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.002079827454670783, "f_over_M": 2.599784318338479e-05}, {"n_transcripts": 949, "spearman_equilibrium": -0.061621942231316854, "spearman_p_equilibrium": 0.05774647706183021, "kendall_equilibrium": -0.041453404276838725, "spearman_independent": -0.06162253587608544, "spearman_p_independent": 0.05774406259046985, "kendall_independent": -0.04145567377469735, "spearman_difference_eq_minus_ind": 5.936447685858659e-07, "kendall_between_the_two_scorings": 0.9999966653593639, "pairwise_ranking_accuracy_equilibrium": 0.5196108863700084, "pairwise_ranking_accuracy_independent": 0.5196108863700084, "construct": "MAPK14-193_pos12mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 5.093307497769583e-05, "f_over_M": 6.366634372211978e-07}, {"n_transcripts": 948, "spearman_equilibrium": -0.10518915157463257, "spearman_p_equilibrium": 0.0011808669161306495, "kendall_equilibrium": -0.0703893806552248, "spearman_independent": -0.10518915157463257, "spearman_p_independent": 0.0011808669161306495, "kendall_independent": -0.0703893806552248, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.5358541201445981, "pairwise_ranking_accuracy_independent": 0.5358541201445981, "construct": "MAPK14-193_pos13mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.00027877147286450637, "f_over_M": 3.48464341080633e-06}, {"n_transcripts": 948, "spearman_equilibrium": -0.049328975819381435, "spearman_p_equilibrium": 0.12907995212128123, "kendall_equilibrium": -0.03314328757820535, "spearman_independent": -0.0493285643542312, "spearman_p_independent": 0.12908314877469765, "kendall_independent": -0.03314336141446414, "spearman_difference_eq_minus_ind": -4.114651502365452e-07, "kendall_between_the_two_scorings": 0.9999844054953124, "pairwise_ranking_accuracy_equilibrium": 0.5173484048278175, "pairwise_ranking_accuracy_independent": 0.5173484048278175, "construct": "MAPK14-193_pos14mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 4.302101912969596e-05, "f_over_M": 5.377627391211995e-07}, {"n_transcripts": 949, "spearman_equilibrium": -0.1206148179009185, "spearman_p_equilibrium": 0.00019582017639808777, "kendall_equilibrium": -0.0812022595681529, "spearman_independent": -0.12061488895029344, "spearman_p_independent": 0.00019581846111970384, "kendall_independent": -0.08120457327101006, "spearman_difference_eq_minus_ind": 7.104937493895847e-08, "kendall_between_the_two_scorings": 0.9999966653593639, "pairwise_ranking_accuracy_equilibrium": 0.5393981875531968, "pairwise_ranking_accuracy_independent": 0.5393981875531968, "construct": "MAPK14-193_pos15mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.0009665708502170694, "f_over_M": 1.2082135627713367e-05}, {"n_transcripts": 948, "spearman_equilibrium": -0.03897837444676544, "spearman_p_equilibrium": 0.2305275015352339, "kendall_equilibrium": -0.02611882969401851, "spearman_independent": -0.03897645060837396, "spearman_p_independent": 0.23055053071489837, "kendall_independent": -0.026116456049541763, "spearman_difference_eq_minus_ind": -1.9238383914821355e-06, "kendall_between_the_two_scorings": 0.9999944305300518, "pairwise_ranking_accuracy_equilibrium": 0.512632685760064, "pairwise_ranking_accuracy_independent": 0.512632685760064, "construct": "MAPK14-193_pos16mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 7.703746537955756e-06, "f_over_M": 9.629683172444695e-08}, {"n_transcripts": 949, "spearman_equilibrium": -0.0681817787726281, "spearman_p_equilibrium": 0.03572240624343837, "kendall_equilibrium": -0.046302936227652684, "spearman_independent": -0.06818674209818035, "spearman_p_independent": 0.03570893103786658, "kendall_independent": -0.04630738308827479, "spearman_difference_eq_minus_ind": 4.963325552248543e-06, "kendall_between_the_two_scorings": 0.9999955538067196, "pairwise_ranking_accuracy_equilibrium": 0.5231207505982958, "pairwise_ranking_accuracy_independent": 0.5231207505982958, "construct": "MAPK14-193_pos17mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.00031920238646576617, "f_over_M": 3.990029830822077e-06}, {"n_transcripts": 949, "spearman_equilibrium": -0.11537478404798163, "spearman_p_equilibrium": 0.00036883702678958775, "kendall_equilibrium": -0.07758539292441914, "spearman_independent": -0.11537478404798163, "spearman_p_independent": 0.00036883702678958775, "kendall_independent": -0.07758539292441914, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999998, "pairwise_ranking_accuracy_equilibrium": 0.538647947688333, "pairwise_ranking_accuracy_independent": 0.538647947688333, "construct": "MAPK14-193_pos18mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.0008073774999655891, "f_over_M": 1.0092218749569864e-05}, {"n_transcripts": 949, "spearman_equilibrium": -0.11946186549163465, "spearman_p_equilibrium": 0.00022558948424371302, "kendall_equilibrium": -0.08024583058619343, "spearman_independent": -0.11946307633160502, "spearman_p_independent": 0.0002255561060300945, "kendall_independent": -0.08024618737625253, "spearman_difference_eq_minus_ind": 1.2108399703725237e-06, "kendall_between_the_two_scorings": 0.9999955538067193, "pairwise_ranking_accuracy_equilibrium": 0.5389788244012598, "pairwise_ranking_accuracy_independent": 0.5389788244012598, "construct": "MAPK14-193_pos19mut", "target_gene": "MAPK14", "rho": 0.001, "f_free_pool": 0.00015901550332460572, "f_over_M": 1.9876937915575714e-06}, {"n_transcripts": 3400, "spearman_equilibrium": -0.05323610732121125, "spearman_p_equilibrium": 0.0019012959141750804, "kendall_equilibrium": -0.03546882692254531, "spearman_independent": -0.05323589071819482, "spearman_p_independent": 0.0019013772500249388, "kendall_independent": -0.03546865689109966, "spearman_difference_eq_minus_ind": -2.1660301643272595e-07, "kendall_between_the_two_scorings": 0.9999985289777149, "pairwise_ranking_accuracy_equilibrium": 0.5177451878092837, "pairwise_ranking_accuracy_independent": 0.5177451878092837, "construct": "PIK3CB-6338_parent", "target_gene": "PIK3CB", "rho": 0.001, "f_free_pool": 0.0010371309415816033, "f_over_M": 1.2964136769770041e-05}, {"n_transcripts": 2638, "spearman_equilibrium": -0.09037915074377158, "spearman_p_equilibrium": 3.3302659623882974e-06, "kendall_equilibrium": -0.06047255636133446, "spearman_independent": -0.09037934339757642, "spearman_p_independent": 3.330105300616815e-06, "kendall_independent": -0.06047283522608301, "spearman_difference_eq_minus_ind": 1.9265380483968197e-07, "kendall_between_the_two_scorings": 0.9999998562475979, "pairwise_ranking_accuracy_equilibrium": 0.5300505429615173, "pairwise_ranking_accuracy_independent": 0.5300505429615173, "construct": "PIK3CB-6340_parent", "target_gene": "PIK3CB", "rho": 0.001, "f_free_pool": 0.0638551553555671, "f_over_M": 0.0007981894419445887}, {"n_transcripts": 3141, "spearman_equilibrium": -0.09881162673524846, "spearman_p_equilibrium": 2.869128101035479e-08, "kendall_equilibrium": -0.06630882732871807, "spearman_independent": -0.09880992711317516, "spearman_p_independent": 2.8707025109766435e-08, "kendall_independent": -0.06630880043591125, "spearman_difference_eq_minus_ind": -1.6996220733034306e-06, "kendall_between_the_two_scorings": 0.999994930386172, "pairwise_ranking_accuracy_equilibrium": 0.5346326086412649, "pairwise_ranking_accuracy_independent": 0.5346326086412649, "construct": "PLK1-319_parent", "target_gene": "PLK1", "rho": 0.001, "f_free_pool": 3.821430222741048e-06, "f_over_M": 4.77678777842631e-08}, {"n_transcripts": 701, "spearman_equilibrium": 0.002419988018328926, "spearman_p_equilibrium": 0.9490034070272506, "kendall_equilibrium": 0.0012881765153668566, "spearman_independent": 0.002419988018328926, "spearman_p_independent": 0.9490034070272506, "kendall_independent": 0.0012881765153668566, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4990132139171901, "pairwise_ranking_accuracy_independent": 0.4990132139171901, "construct": "PLK1-772_parent", "target_gene": "PLK1", "rho": 0.001, "f_free_pool": 0.00015315903239739514, "f_over_M": 1.9144879049674393e-06}] |
| 0.01 | 24 | -0.0656012 | 0.0431405 | -0.0655996 | 0.0431396 | -1.5732e-06 | 9.3650e-06 | 0.999996 | 0.999987 | 29 | 0.00790774 | 0.00385797 | 1.7528e-06 | 0.0474923 | [{"n_transcripts": 949, "spearman_equilibrium": -0.08307670801935858, "spearman_p_equilibrium": 0.010458123862142465, "kendall_equilibrium": -0.056681566226754264, "spearman_independent": -0.08306734299243876, "spearman_p_independent": 0.010466843425230167, "kendall_independent": -0.05666822677206273, "spearman_difference_eq_minus_ind": -9.36502691982477e-06, "kendall_between_the_two_scorings": 0.9999911076332075, "pairwise_ranking_accuracy_equilibrium": 0.5277043533982138, "pairwise_ranking_accuracy_independent": 0.5277043533982138, "construct": "MAPK14-193_parent", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.12255097624331332, "f_over_M": 0.00015318872030414165}, {"n_transcripts": 950, "spearman_equilibrium": -0.09275586292966731, "spearman_p_equilibrium": 0.004218620768641382, "kendall_equilibrium": -0.06330359399704998, "spearman_independent": -0.09275597489948859, "spearman_p_independent": 0.0042185746040697865, "kendall_independent": -0.0633080310611838, "spearman_difference_eq_minus_ind": 1.119698212759257e-07, "kendall_between_the_two_scorings": 0.9999911263343775, "pairwise_ranking_accuracy_equilibrium": 0.530385938211838, "pairwise_ranking_accuracy_independent": 0.530385938211838, "construct": "MAPK14-193_pos01mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.0795160104656901, "f_over_M": 9.939501308211262e-05}, {"n_transcripts": 743, "spearman_equilibrium": -0.11277813708270523, "spearman_p_equilibrium": 0.0020786341423314, "kendall_equilibrium": -0.0752762682459009, "spearman_independent": -0.11277689287573685, "spearman_p_independent": 0.0020788726492119917, "kendall_independent": -0.0752725037638355, "spearman_difference_eq_minus_ind": -1.2442069683843426e-06, "kendall_between_the_two_scorings": 0.9999981861236646, "pairwise_ranking_accuracy_equilibrium": 0.5385728592889334, "pairwise_ranking_accuracy_independent": 0.5385728592889334, "construct": "MAPK14-193_pos02mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.2031225639500197, "f_over_M": 0.0002539032049375246}, {"n_transcripts": 718, "spearman_equilibrium": -0.035458061511352716, "spearman_p_equilibrium": 0.3427425912596375, "kendall_equilibrium": -0.023786812547177308, "spearman_independent": -0.03545646512834478, "spearman_p_independent": 0.3427643351103264, "kendall_independent": -0.02378297328083878, "spearman_difference_eq_minus_ind": -1.5963830079374075e-06, "kendall_between_the_two_scorings": 0.9999980575188105, "pairwise_ranking_accuracy_equilibrium": 0.5105482484698528, "pairwise_ranking_accuracy_independent": 0.5105482484698528, "construct": "MAPK14-193_pos03mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 37.9938665032703, "f_over_M": 0.04749233312908787}, {"n_transcripts": 4903, "spearman_equilibrium": -0.050509243705741926, "spearman_p_equilibrium": 0.0004030391452565694, "kendall_equilibrium": -0.033708067568703926, "spearman_independent": -0.050509243705741926, "spearman_p_independent": 0.0004030391452565694, "kendall_independent": -0.033708067568703926, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.5181601696950292, "pairwise_ranking_accuracy_independent": 0.5181601696950292, "construct": "MAPK14-193_pos04mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.0030180693265159783, "f_over_M": 3.772586658144973e-06}, {"n_transcripts": 3809, "spearman_equilibrium": 0.028091386889294925, "spearman_p_equilibrium": 0.0830082818392359, "kendall_equilibrium": 0.018871619073091102, "spearman_independent": 0.02809148145562587, "spearman_p_independent": 0.08300724510294076, "kendall_independent": 0.018871894861059085, "spearman_difference_eq_minus_ind": -9.456633094304112e-08, "kendall_between_the_two_scorings": 0.999999724226711, "pairwise_ranking_accuracy_equilibrium": 0.49036023465514395, "pairwise_ranking_accuracy_independent": 0.49036023465514395, "construct": "MAPK14-193_pos05mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.0014022169256543522, "f_over_M": 1.7527711570679401e-06}, {"n_transcripts": 581, "spearman_equilibrium": -0.08951259872803471, "spearman_p_equilibrium": 0.0309829251876887, "kendall_equilibrium": -0.059984032818233245, "spearman_independent": -0.08951259872803471, "spearman_p_independent": 0.0309829251876887, "kendall_independent": -0.059984032818233245, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999999, "pairwise_ranking_accuracy_equilibrium": 0.5296950079918228, "pairwise_ranking_accuracy_independent": 0.5296950079918228, "construct": "MAPK14-193_pos06mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 19.771146640272974, "f_over_M": 0.024713933300341218}, {"n_transcripts": 752, "spearman_equilibrium": 0.026952184067538253, "spearman_p_equilibrium": 0.46051199996351344, "kendall_equilibrium": 0.015598215038033235, "spearman_independent": 0.026952184067538253, "spearman_p_independent": 0.46051199996351344, "kendall_independent": 0.015598215038033235, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4912066340838074, "pairwise_ranking_accuracy_independent": 0.4912066340838074, "construct": "MAPK14-193_pos07mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.08359497366997387, "f_over_M": 0.00010449371708746734}, {"n_transcripts": 951, "spearman_equilibrium": -0.03504548327193848, "spearman_p_equilibrium": 0.28029674866123655, "kendall_equilibrium": -0.02313949705862236, "spearman_independent": -0.035040725596564626, "spearman_p_independent": 0.2803620873539564, "kendall_independent": -0.023126212494240794, "spearman_difference_eq_minus_ind": -4.75767537385513e-06, "kendall_between_the_two_scorings": 0.999986717494388, "pairwise_ranking_accuracy_equilibrium": 0.5123366544835528, "pairwise_ranking_accuracy_independent": 0.512331647724428, "construct": "MAPK14-193_pos08mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 1.8656474042688944, "f_over_M": 0.002332059255336118}, {"n_transcripts": 951, "spearman_equilibrium": -0.07516245461047316, "spearman_p_equilibrium": 0.02044320148874819, "kendall_equilibrium": -0.049639400002518874, "spearman_independent": -0.07515627843617632, "spearman_p_independent": 0.020453582691637134, "kendall_independent": -0.0496346973662164, "spearman_difference_eq_minus_ind": -6.176174296837478e-06, "kendall_between_the_two_scorings": 0.9999944656318506, "pairwise_ranking_accuracy_equilibrium": 0.5253331864742813, "pairwise_ranking_accuracy_independent": 0.5253305563760707, "construct": "MAPK14-193_pos09mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.02369774923623056, "f_over_M": 2.96221865452882e-05}, {"n_transcripts": 950, "spearman_equilibrium": -0.03674146462582355, "spearman_p_equilibrium": 0.25791242621927285, "kendall_equilibrium": -0.0246140877181472, "spearman_independent": -0.03674174416476396, "spearman_p_independent": 0.2579088023115762, "kendall_independent": -0.0246140331140329, "spearman_difference_eq_minus_ind": 2.795389404119941e-07, "kendall_between_the_two_scorings": 0.9999977815909764, "pairwise_ranking_accuracy_equilibrium": 0.5109928350048317, "pairwise_ranking_accuracy_independent": 0.5109928350048317, "construct": "MAPK14-193_pos10mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.027850000034960208, "f_over_M": 3.481250004370026e-05}, {"n_transcripts": 950, "spearman_equilibrium": -0.09966652295802814, "spearman_p_equilibrium": 0.002101184481363075, "kendall_equilibrium": -0.06708179623453667, "spearman_independent": -0.0996612033434029, "spearman_p_independent": 0.002102347220877917, "kendall_independent": -0.06706833492762859, "spearman_difference_eq_minus_ind": -5.319614625243219e-06, "kendall_between_the_two_scorings": 0.9999889079450394, "pairwise_ranking_accuracy_equilibrium": 0.5339455789125798, "pairwise_ranking_accuracy_independent": 0.5339455789125798, "construct": "MAPK14-193_pos11mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.3506634944852647, "f_over_M": 0.00043832936810658086}, {"n_transcripts": 949, "spearman_equilibrium": -0.06162012090584499, "spearman_p_equilibrium": 0.05775388527769502, "kendall_equilibrium": -0.04144678009300796, "spearman_independent": -0.0616198611561389, "spearman_p_independent": 0.05775494187025168, "kendall_independent": -0.04144678009300796, "spearman_difference_eq_minus_ind": -2.5974970609132786e-07, "kendall_between_the_two_scorings": 0.9999955538067196, "pairwise_ranking_accuracy_equilibrium": 0.5196108863700084, "pairwise_ranking_accuracy_independent": 0.5196108863700084, "construct": "MAPK14-193_pos12mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.05914090447812824, "f_over_M": 7.39261305976603e-05}, {"n_transcripts": 948, "spearman_equilibrium": -0.10519544757163557, "spearman_p_equilibrium": 0.001180057959604051, "kendall_equilibrium": -0.07039383694851437, "spearman_independent": -0.10519437229128627, "spearman_p_independent": 0.0011801960834103475, "kendall_independent": -0.07039184402981156, "spearman_difference_eq_minus_ind": -1.0752803493024876e-06, "kendall_between_the_two_scorings": 0.9999966583068642, "pairwise_ranking_accuracy_equilibrium": 0.5358541201445981, "pairwise_ranking_accuracy_independent": 0.5358541201445981, "construct": "MAPK14-193_pos13mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.33916444114971356, "f_over_M": 0.00042395555143714194}, {"n_transcripts": 948, "spearman_equilibrium": -0.04932977883807354, "spearman_p_equilibrium": 0.12907371368363652, "kendall_equilibrium": -0.03314555246914858, "spearman_independent": -0.04932691958310024, "spearman_p_independent": 0.12909592753758756, "kendall_independent": -0.033136640577646495, "spearman_difference_eq_minus_ind": -2.859254973300307e-06, "kendall_between_the_two_scorings": 0.9999910888530463, "pairwise_ranking_accuracy_equilibrium": 0.5173484048278175, "pairwise_ranking_accuracy_independent": 0.5173484048278175, "construct": "MAPK14-193_pos14mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.0843978447577263, "f_over_M": 0.00010549730594715788}, {"n_transcripts": 949, "spearman_equilibrium": -0.12061613855706659, "spearman_p_equilibrium": 0.00019578829534006972, "kendall_equilibrium": -0.08120457327101006, "spearman_independent": -0.12061488895029344, "spearman_p_independent": 0.00019581846111970384, "kendall_independent": -0.08120457327101006, "spearman_difference_eq_minus_ind": -1.2496067731404548e-06, "kendall_between_the_two_scorings": 0.9999955538067196, "pairwise_ranking_accuracy_equilibrium": 0.5393981875531968, "pairwise_ranking_accuracy_independent": 0.5393981875531968, "construct": "MAPK14-193_pos15mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.9893624807617711, "f_over_M": 0.0012367031009522138}, {"n_transcripts": 948, "spearman_equilibrium": -0.03897837444676544, "spearman_p_equilibrium": 0.2305275015352339, "kendall_equilibrium": -0.02611882969401851, "spearman_independent": -0.03898327479306902, "spearman_p_independent": 0.23046884964086867, "kendall_independent": -0.026120912402421134, "spearman_difference_eq_minus_ind": 4.900346303578218e-06, "kendall_between_the_two_scorings": 0.9999944305300518, "pairwise_ranking_accuracy_equilibrium": 0.512632685760064, "pairwise_ranking_accuracy_independent": 0.512632685760064, "construct": "MAPK14-193_pos16mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.019008216204385038, "f_over_M": 2.3760270255481296e-05}, {"n_transcripts": 949, "spearman_equilibrium": -0.06817713837914857, "spearman_p_equilibrium": 0.03573500861964168, "kendall_equilibrium": -0.046302936227652684, "spearman_independent": -0.06817713837914857, "spearman_p_independent": 0.03573500861964168, "kendall_independent": -0.046302936227652684, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.5231207505982958, "pairwise_ranking_accuracy_independent": 0.5231207505982958, "construct": "MAPK14-193_pos17mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.15184405614914082, "f_over_M": 0.000189805070186426}, {"n_transcripts": 949, "spearman_equilibrium": -0.11537887794077872, "spearman_p_equilibrium": 0.0003686583150209769, "kendall_equilibrium": -0.07759180436910319, "spearman_independent": -0.11537478404798163, "spearman_p_independent": 0.00036883702678958775, "kendall_independent": -0.07758539292441914, "spearman_difference_eq_minus_ind": -4.093892797096821e-06, "kendall_between_the_two_scorings": 0.9999966653494795, "pairwise_ranking_accuracy_equilibrium": 0.538647947688333, "pairwise_ranking_accuracy_independent": 0.538647947688333, "construct": "MAPK14-193_pos18mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.33729852233560575, "f_over_M": 0.0004216231529195072}, {"n_transcripts": 949, "spearman_equilibrium": -0.11946517905601123, "spearman_p_equilibrium": 0.00022549815298090147, "kendall_equilibrium": -0.08025027757043207, "spearman_independent": -0.11946307633160502, "spearman_p_independent": 0.0002255561060300945, "kendall_independent": -0.08024618737625253, "spearman_difference_eq_minus_ind": -2.102724406205514e-06, "kendall_between_the_two_scorings": 0.9999955538067193, "pairwise_ranking_accuracy_equilibrium": 0.5389788244012598, "pairwise_ranking_accuracy_independent": 0.5389788244012598, "construct": "MAPK14-193_pos19mut", "target_gene": "MAPK14", "rho": 0.01, "f_free_pool": 0.2188881976158097, "f_over_M": 0.0002736102470197621}, {"n_transcripts": 3400, "spearman_equilibrium": -0.053236618358446335, "spearman_p_equilibrium": 0.0019011040290071812, "kendall_equilibrium": -0.035469179262040844, "spearman_independent": -0.05323687929998675, "spearman_p_independent": 0.0019010060570710543, "kendall_independent": -0.03546899695396181, "spearman_difference_eq_minus_ind": 2.6094154041700346e-07, "kendall_between_the_two_scorings": 0.9999990481620823, "pairwise_ranking_accuracy_equilibrium": 0.5177451878092837, "pairwise_ranking_accuracy_independent": 0.5177451878092837, "construct": "PIK3CB-6338_parent", "target_gene": "PIK3CB", "rho": 0.01, "f_free_pool": 0.2089551293614888, "f_over_M": 0.000261193911701861}, {"n_transcripts": 2638, "spearman_equilibrium": -0.09037934339757642, "spearman_p_equilibrium": 3.330105300616815e-06, "kendall_equilibrium": -0.06047283522608301, "spearman_independent": -0.09037915074377158, "spearman_p_independent": 3.3302659623882974e-06, "kendall_independent": -0.06047255636133446, "spearman_difference_eq_minus_ind": -1.9265380483968197e-07, "kendall_between_the_two_scorings": 0.9999998562475979, "pairwise_ranking_accuracy_equilibrium": 0.5300505429615173, "pairwise_ranking_accuracy_independent": 0.5300505429615173, "construct": "PIK3CB-6340_parent", "target_gene": "PIK3CB", "rho": 0.01, "f_free_pool": 10.976077662554228, "f_over_M": 0.013720097078192786}, {"n_transcripts": 3141, "spearman_equilibrium": -0.09880862371407152, "spearman_p_equilibrium": 2.8719104555254903e-08, "kendall_equilibrium": -0.06630730675013298, "spearman_independent": -0.09880570190068245, "spearman_p_independent": 2.8746200809475012e-08, "kendall_independent": -0.06630463649355836, "spearman_difference_eq_minus_ind": -2.9218133890673847e-06, "kendall_between_the_two_scorings": 0.99999340952276, "pairwise_ranking_accuracy_equilibrium": 0.5346326086412649, "pairwise_ranking_accuracy_independent": 0.5346326086412649, "construct": "PLK1-319_parent", "target_gene": "PLK1", "rho": 0.01, "f_free_pool": 0.001848136802461034, "f_over_M": 2.3101710030762926e-06}, {"n_transcripts": 701, "spearman_equilibrium": 0.002419988018328926, "spearman_p_equilibrium": 0.9490034070272506, "kendall_equilibrium": 0.0012881765153668566, "spearman_independent": 0.002419988018328926, "spearman_p_independent": 0.9490034070272506, "kendall_independent": 0.0012881765153668566, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4990132139171901, "pairwise_ranking_accuracy_independent": 0.4990132139171901, "construct": "PLK1-772_parent", "target_gene": "PLK1", "rho": 0.01, "f_free_pool": 0.16095735201569433, "f_over_M": 0.00020119669001961792}] |
| 0.1 | 24 | -0.0656014 | 0.0431406 | -0.0656008 | 0.0431407 | -5.3993e-07 | 1.0260e-05 | 0.999993 | 0.999978 | 104 | 0.465099 | 0.445944 | 4.4347e-04 | 0.758906 | [{"n_transcripts": 949, "spearman_equilibrium": -0.08306644761770716, "spearman_p_equilibrium": 0.010467677426354132, "kendall_equilibrium": -0.05666594054285816, "spearman_independent": -0.08307670801935858, "spearman_p_independent": 0.010458123862142465, "kendall_independent": -0.056681566226754264, "spearman_difference_eq_minus_ind": 1.0260401651418505e-05, "kendall_between_the_two_scorings": 0.9999833268314151, "pairwise_ranking_accuracy_equilibrium": 0.5277043533982138, "pairwise_ranking_accuracy_independent": 0.5277043533982138, "construct": "MAPK14-193_parent", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4042.307580216997, "f_over_M": 0.5052884475271247}, {"n_transcripts": 950, "spearman_equilibrium": -0.09274940269699619, "spearman_p_equilibrium": 0.004221285063588662, "kendall_equilibrium": -0.06330345356378583, "spearman_independent": -0.09275203398776861, "spearman_p_independent": 0.004220199696705247, "kendall_independent": -0.06329901650949525, "spearman_difference_eq_minus_ind": 2.6312907724229673e-06, "kendall_between_the_two_scorings": 0.9999778159343706, "pairwise_ranking_accuracy_equilibrium": 0.530385938211838, "pairwise_ranking_accuracy_independent": 0.530385938211838, "construct": "MAPK14-193_pos01mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4014.1442062854485, "f_over_M": 0.501768025785681}, {"n_transcripts": 743, "spearman_equilibrium": -0.11277813708270523, "spearman_p_equilibrium": 0.0020786341423314, "kendall_equilibrium": -0.0752762682459009, "spearman_independent": -0.11277689287573685, "spearman_p_independent": 0.0020788726492119917, "kendall_independent": -0.0752725037638355, "spearman_difference_eq_minus_ind": -1.2442069683843426e-06, "kendall_between_the_two_scorings": 0.9999981861236646, "pairwise_ranking_accuracy_equilibrium": 0.5385728592889334, "pairwise_ranking_accuracy_independent": 0.5385728592889334, "construct": "MAPK14-193_pos02mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4736.929508257663, "f_over_M": 0.5921161885322078}, {"n_transcripts": 718, "spearman_equilibrium": -0.035458061511352716, "spearman_p_equilibrium": 0.3427425912596375, "kendall_equilibrium": -0.023786812547177308, "spearman_independent": -0.035454868170593165, "spearman_p_independent": 0.34278608766977836, "kendall_independent": -0.023779041618543797, "spearman_difference_eq_minus_ind": -3.1933407595510777e-06, "kendall_between_the_two_scorings": 0.9999922300827885, "pairwise_ranking_accuracy_equilibrium": 0.5105482484698528, "pairwise_ranking_accuracy_independent": 0.5105482484698528, "construct": "MAPK14-193_pos03mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 5813.94677710313, "f_over_M": 0.7267433471378913}, {"n_transcripts": 4903, "spearman_equilibrium": -0.05050920969950734, "spearman_p_equilibrium": 0.0004030427860208176, "kendall_equilibrium": -0.03370798293950686, "spearman_independent": -0.05050938387177401, "spearman_p_independent": 0.00040302413917136853, "kendall_independent": -0.033708064763731026, "spearman_difference_eq_minus_ind": 1.7417226667176822e-07, "kendall_between_the_two_scorings": 0.9999996255383675, "pairwise_ranking_accuracy_equilibrium": 0.5181601696950292, "pairwise_ranking_accuracy_independent": 0.5181601696950292, "construct": "MAPK14-193_pos04mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 3.5477779537947587, "f_over_M": 0.00044347224422434483}, {"n_transcripts": 3809, "spearman_equilibrium": 0.028091386889294925, "spearman_p_equilibrium": 0.0830082818392359, "kendall_equilibrium": 0.018871619073091102, "spearman_independent": 0.0280911652408031, "spearman_p_independent": 0.0830107118258965, "kendall_independent": 0.018871482480169854, "spearman_difference_eq_minus_ind": 2.2164849182437774e-07, "kendall_between_the_two_scorings": 0.9999996552833673, "pairwise_ranking_accuracy_equilibrium": 0.49036023465514395, "pairwise_ranking_accuracy_independent": 0.49036023465514395, "construct": "MAPK14-193_pos05mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 31.44544602398757, "f_over_M": 0.003930680752998446}, {"n_transcripts": 581, "spearman_equilibrium": -0.08951259872803471, "spearman_p_equilibrium": 0.0309829251876887, "kendall_equilibrium": -0.059984032818233245, "spearman_independent": -0.08951259872803471, "spearman_p_independent": 0.0309829251876887, "kendall_independent": -0.059984032818233245, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999999, "pairwise_ranking_accuracy_equilibrium": 0.5296950079918228, "pairwise_ranking_accuracy_independent": 0.5296950079918228, "construct": "MAPK14-193_pos06mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 6071.24596362691, "f_over_M": 0.7589057454533638}, {"n_transcripts": 752, "spearman_equilibrium": 0.026952184067538253, "spearman_p_equilibrium": 0.46051199996351344, "kendall_equilibrium": 0.015598215038033235, "spearman_independent": 0.02696091739902728, "spearman_p_independent": 0.46036664324726106, "kendall_independent": 0.015601729241181481, "spearman_difference_eq_minus_ind": -8.733331489027552e-06, "kendall_between_the_two_scorings": 0.9999982293097053, "pairwise_ranking_accuracy_equilibrium": 0.4912066340838074, "pairwise_ranking_accuracy_independent": 0.4912066340838074, "construct": "MAPK14-193_pos07mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4416.145707949074, "f_over_M": 0.5520182134936342}, {"n_transcripts": 951, "spearman_equilibrium": -0.03504111625612612, "spearman_p_equilibrium": 0.28035672191076955, "kendall_equilibrium": -0.023126212494240794, "spearman_independent": -0.03504349484934753, "spearman_p_independent": 0.2803240550546451, "kendall_independent": -0.02313282917128464, "spearman_difference_eq_minus_ind": 2.3785932214137606e-06, "kendall_between_the_two_scorings": 0.9999966793778851, "pairwise_ranking_accuracy_equilibrium": 0.5123342128584232, "pairwise_ranking_accuracy_independent": 0.5123366544835528, "construct": "MAPK14-193_pos08mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4267.317619474354, "f_over_M": 0.5334147024342942}, {"n_transcripts": 951, "spearman_equilibrium": -0.07516685144453047, "spearman_p_equilibrium": 0.02043581388042471, "kendall_equilibrium": -0.04964366309173334, "spearman_independent": -0.07516394512819866, "spearman_p_independent": 0.020440696844160146, "kendall_independent": -0.04963912527980455, "spearman_difference_eq_minus_ind": -2.9063163318188145e-06, "kendall_between_the_two_scorings": 0.9999955725103811, "pairwise_ranking_accuracy_equilibrium": 0.525335562909597, "pairwise_ranking_accuracy_independent": 0.525335562909597, "construct": "MAPK14-193_pos09mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 3541.9916505197098, "f_over_M": 0.4427489563149637}, {"n_transcripts": 950, "spearman_equilibrium": -0.036739701100687965, "spearman_p_equilibrium": 0.25793528915037, "kendall_equilibrium": -0.02460521297947111, "spearman_independent": -0.036742492963127156, "spearman_p_independent": 0.25789909515740517, "kendall_independent": -0.0246140331140329, "spearman_difference_eq_minus_ind": 2.791862439191495e-06, "kendall_between_the_two_scorings": 0.9999889079450394, "pairwise_ranking_accuracy_equilibrium": 0.5109928350048317, "pairwise_ranking_accuracy_independent": 0.5109928350048317, "construct": "MAPK14-193_pos10mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 3689.375524714558, "f_over_M": 0.46117194058931976}, {"n_transcripts": 950, "spearman_equilibrium": -0.09966530423957083, "spearman_p_equilibrium": 0.002101450811825994, "kendall_equilibrium": -0.06707720992232592, "spearman_independent": -0.09967052588060948, "spearman_p_independent": 0.002100309927285572, "kendall_independent": -0.06708623374172953, "spearman_difference_eq_minus_ind": 5.221641038652414e-06, "kendall_between_the_two_scorings": 0.9999911263565235, "pairwise_ranking_accuracy_equilibrium": 0.5339455789125798, "pairwise_ranking_accuracy_independent": 0.5339455789125798, "construct": "MAPK14-193_pos11mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4219.821218414483, "f_over_M": 0.5274776523018104}, {"n_transcripts": 949, "spearman_equilibrium": -0.061623950026328256, "spearman_p_equilibrium": 0.057738311297646394, "kendall_equilibrium": -0.04145785111274056, "spearman_independent": -0.06162440261693557, "spearman_p_independent": 0.057736470730064625, "kendall_independent": -0.041460028445994564, "spearman_difference_eq_minus_ind": 4.5259060731106526e-07, "kendall_between_the_two_scorings": 0.9999899960990961, "pairwise_ranking_accuracy_equilibrium": 0.5196108863700084, "pairwise_ranking_accuracy_independent": 0.5196108863700084, "construct": "MAPK14-193_pos12mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 3720.3766674747794, "f_over_M": 0.4650470834343474}, {"n_transcripts": 948, "spearman_equilibrium": -0.10519329256594998, "spearman_p_equilibrium": 0.0011803347931991278, "kendall_equilibrium": -0.0703893806552248, "spearman_independent": -0.10519544757163557, "spearman_p_independent": 0.001180057959604051, "kendall_independent": -0.07039383694851437, "spearman_difference_eq_minus_ind": 2.1550056855945687e-06, "kendall_between_the_two_scorings": 0.9999866332497912, "pairwise_ranking_accuracy_equilibrium": 0.5358541201445981, "pairwise_ranking_accuracy_independent": 0.5358541201445981, "construct": "MAPK14-193_pos13mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4443.023561331045, "f_over_M": 0.5553779451663806}, {"n_transcripts": 948, "spearman_equilibrium": -0.04932786010423281, "spearman_p_equilibrium": 0.12908862020231826, "kendall_equilibrium": -0.03313890546374963, "spearman_independent": -0.04932735956565222, "spearman_p_independent": 0.12909250907364442, "kendall_independent": -0.03313883163741775, "spearman_difference_eq_minus_ind": -5.005385805903484e-07, "kendall_between_the_two_scorings": 0.9999977722157432, "pairwise_ranking_accuracy_equilibrium": 0.5173484048278175, "pairwise_ranking_accuracy_independent": 0.5173484048278175, "construct": "MAPK14-193_pos14mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 3883.972730029921, "f_over_M": 0.4854965912537401}, {"n_transcripts": 949, "spearman_equilibrium": -0.12061915727005788, "spearman_p_equilibrium": 0.00019571544093700095, "kendall_equilibrium": -0.0812090201563543, "spearman_independent": -0.1206148179009185, "spearman_p_independent": 0.00019582017639808777, "kendall_independent": -0.0812022595681529, "spearman_difference_eq_minus_ind": -4.3393691393778244e-06, "kendall_between_the_two_scorings": 0.9999966653593639, "pairwise_ranking_accuracy_equilibrium": 0.5393981875531968, "pairwise_ranking_accuracy_independent": 0.5393981875531968, "construct": "MAPK14-193_pos15mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4548.525080802729, "f_over_M": 0.5685656351003411}, {"n_transcripts": 948, "spearman_equilibrium": -0.03898064793972407, "spearman_p_equilibrium": 0.2305002889434849, "kendall_equilibrium": -0.0261253687553005, "spearman_independent": -0.03898391918202629, "spearman_p_independent": 0.23046113778354652, "kendall_independent": -0.0261253687553005, "spearman_difference_eq_minus_ind": 3.2712423022190906e-06, "kendall_between_the_two_scorings": 0.9999888610911227, "pairwise_ranking_accuracy_equilibrium": 0.512632685760064, "pairwise_ranking_accuracy_independent": 0.512632685760064, "construct": "MAPK14-193_pos16mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 3482.1592188924324, "f_over_M": 0.43526990236155405}, {"n_transcripts": 949, "spearman_equilibrium": -0.06819069753735466, "spearman_p_equilibrium": 0.03569819529820546, "kendall_equilibrium": -0.046314001898985546, "spearman_independent": -0.06818472728285715, "spearman_p_independent": 0.03571440064877774, "kendall_independent": -0.0463118299488969, "spearman_difference_eq_minus_ind": -5.970254497500438e-06, "kendall_between_the_two_scorings": 0.9999877729826873, "pairwise_ranking_accuracy_equilibrium": 0.5231207505982958, "pairwise_ranking_accuracy_independent": 0.5231207505982958, "construct": "MAPK14-193_pos17mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 3813.725468963983, "f_over_M": 0.4767156836204979}, {"n_transcripts": 949, "spearman_equilibrium": -0.11537850586691066, "spearman_p_equilibrium": 0.00036867455391867925, "kendall_equilibrium": -0.07759180436910319, "spearman_independent": -0.11537550700023234, "spearman_p_independent": 0.0003688054616885743, "kendall_independent": -0.07758718510891444, "spearman_difference_eq_minus_ind": -2.998866678316503e-06, "kendall_between_the_two_scorings": 0.9999911076356787, "pairwise_ranking_accuracy_equilibrium": 0.538647947688333, "pairwise_ranking_accuracy_independent": 0.538647947688333, "construct": "MAPK14-193_pos18mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4236.503771728907, "f_over_M": 0.5295629714661134}, {"n_transcripts": 949, "spearman_equilibrium": -0.11946671733240709, "spearman_p_equilibrium": 0.00022545576548499592, "kendall_equilibrium": -0.08025259026703455, "spearman_independent": -0.11945851289649394, "spearman_p_independent": 0.00022568192658617021, "kendall_independent": -0.08023462394118323, "spearman_difference_eq_minus_ind": -8.204435913150565e-06, "kendall_between_the_two_scorings": 0.9999844383605845, "pairwise_ranking_accuracy_equilibrium": 0.5389788244012598, "pairwise_ranking_accuracy_independent": 0.5389788244012598, "construct": "MAPK14-193_pos19mut", "target_gene": "MAPK14", "rho": 0.1, "f_free_pool": 4144.790130089472, "f_over_M": 0.518098766261184}, {"n_transcripts": 3400, "spearman_equilibrium": -0.053236613143751894, "spearman_p_equilibrium": 0.0019011059869401237, "kendall_equilibrium": -0.03546934315507993, "spearman_independent": -0.05323637561463413, "spearman_p_independent": 0.0019011951726677573, "kendall_independent": -0.035469173123693395, "spearman_difference_eq_minus_ind": -2.3752911776364627e-07, "kendall_between_the_two_scorings": 0.9999981828551379, "pairwise_ranking_accuracy_equilibrium": 0.5177451878092837, "pairwise_ranking_accuracy_independent": 0.5177451878092837, "construct": "PIK3CB-6338_parent", "target_gene": "PIK3CB", "rho": 0.1, "f_free_pool": 329.9805859595234, "f_over_M": 0.041247573244940425}, {"n_transcripts": 2638, "spearman_equilibrium": -0.09037895806042781, "spearman_p_equilibrium": 3.330426656224455e-06, "kendall_equilibrium": -0.060472260110435445, "spearman_independent": -0.09037915074377158, "spearman_p_independent": 3.3302659623882974e-06, "kendall_independent": -0.06047255636133446, "spearman_difference_eq_minus_ind": 1.9268334376654206e-07, "kendall_between_the_two_scorings": 0.9999998562475979, "pairwise_ranking_accuracy_equilibrium": 0.5300505429615173, "pairwise_ranking_accuracy_independent": 0.5300505429615173, "construct": "PIK3CB-6340_parent", "target_gene": "PIK3CB", "rho": 0.1, "f_free_pool": 2898.431983354174, "f_over_M": 0.36230399791927176}, {"n_transcripts": 3141, "spearman_equilibrium": -0.0988134056320023, "spearman_p_equilibrium": 2.8674811535275982e-08, "kendall_equilibrium": -0.06631081517812551, "spearman_independent": -0.09880902429495068, "spearman_p_independent": 2.8715391587660135e-08, "kendall_independent": -0.06630740087276976, "spearman_difference_eq_minus_ind": -4.381337051620471e-06, "kendall_between_the_two_scorings": 0.9999974651939443, "pairwise_ranking_accuracy_equilibrium": 0.5346326086412649, "pairwise_ranking_accuracy_independent": 0.5346326086412649, "construct": "PLK1-319_parent", "target_gene": "PLK1", "rho": 0.1, "f_free_pool": 22.84498929301403, "f_over_M": 0.0028556236616267537}, {"n_transcripts": 701, "spearman_equilibrium": 0.002419988018328926, "spearman_p_equilibrium": 0.9490034070272506, "kendall_equilibrium": 0.0012881765153668566, "spearman_independent": 0.002419988018328926, "spearman_p_independent": 0.9490034070272506, "kendall_independent": 0.0012881765153668566, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4990132139171901, "pairwise_ranking_accuracy_independent": 0.4990132139171901, "construct": "PLK1-772_parent", "target_gene": "PLK1", "rho": 0.1, "f_free_pool": 5248.729187314337, "f_over_M": 0.6560911484142921}] |
| 0.5 | 24 | -0.0656017 | 0.0431407 | -0.0656008 | 0.0431406 | -8.9008e-07 | 1.0399e-05 | 0.999995 | 0.999988 | 77 | 0.295878 | 0.836401 | 0.410949 | 0.944587 | [{"n_transcripts": 949, "spearman_equilibrium": -0.08307278076704751, "spearman_p_equilibrium": 0.010461779651373805, "kendall_equilibrium": -0.05667051300641982, "spearman_independent": -0.08307048514199182, "spearman_p_independent": 0.010463917121821069, "kendall_independent": -0.05667051300641982, "spearman_difference_eq_minus_ind": -2.295625055687145e-06, "kendall_between_the_two_scorings": 0.9999955538067196, "pairwise_ranking_accuracy_equilibrium": 0.5277043533982138, "pairwise_ranking_accuracy_independent": 0.5277043533982138, "spearman_equilibrium_ci95": [-0.14833894104824993, -0.019989549947645104], "spearman_independent_ci95": [-0.14833290516611003, -0.01999014551281442], "bootstrap_n": 400, "construct": "MAPK14-193_parent", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35379.42653613251, "f_over_M": 0.8844856634033127}, {"n_transcripts": 950, "spearman_equilibrium": -0.09275586292966731, "spearman_p_equilibrium": 0.004218620768641382, "kendall_equilibrium": -0.06330359399704998, "spearman_independent": -0.09274546373251612, "spearman_p_independent": 0.0042229102981756195, "kendall_independent": -0.06329471986878236, "spearman_difference_eq_minus_ind": -1.0399197151192419e-05, "kendall_between_the_two_scorings": 0.9999955631671889, "pairwise_ranking_accuracy_equilibrium": 0.530385938211838, "pairwise_ranking_accuracy_independent": 0.530385938211838, "spearman_equilibrium_ci95": [-0.15466086109424904, -0.024694480400360506], "spearman_independent_ci95": [-0.15466086109424904, -0.02468070553470879], "bootstrap_n": 400, "construct": "MAPK14-193_pos01mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35264.52285874967, "f_over_M": 0.8816130714687417}, {"n_transcripts": 743, "spearman_equilibrium": -0.11277813708270523, "spearman_p_equilibrium": 0.0020786341423314, "kendall_equilibrium": -0.0752762682459009, "spearman_independent": -0.11277813708270523, "spearman_p_independent": 0.0020786341423314, "kendall_independent": -0.0752762682459009, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.5385728592889334, "pairwise_ranking_accuracy_independent": 0.5385728592889334, "spearman_equilibrium_ci95": [-0.18303055143950764, -0.05007730508434172], "spearman_independent_ci95": [-0.18303055143950764, -0.05007730508434172], "bootstrap_n": 400, "construct": "MAPK14-193_pos02mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 36393.63661407391, "f_over_M": 0.9098409153518477}, {"n_transcripts": 718, "spearman_equilibrium": -0.035458061511352716, "spearman_p_equilibrium": 0.3427425912596375, "kendall_equilibrium": -0.023786812547177308, "spearman_independent": -0.035454868170593165, "spearman_p_independent": 0.34278608766977836, "kendall_independent": -0.023779041618543797, "spearman_difference_eq_minus_ind": -3.1933407595510777e-06, "kendall_between_the_two_scorings": 0.9999922300827885, "pairwise_ranking_accuracy_equilibrium": 0.5105482484698528, "pairwise_ranking_accuracy_independent": 0.5105482484698528, "spearman_equilibrium_ci95": [-0.09763155034415993, 0.034312225726384454], "spearman_independent_ci95": [-0.09763155034415993, 0.034312225726384454], "bootstrap_n": 400, "construct": "MAPK14-193_pos03mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 37070.30235920014, "f_over_M": 0.9267575589800036}, {"n_transcripts": 4903, "spearman_equilibrium": -0.05050920685007866, "spearman_p_equilibrium": 0.00040304309108680434, "kendall_equilibrium": -0.03370790111527594, "spearman_independent": -0.050509243705741926, "spearman_p_independent": 0.0004030391452565694, "kendall_independent": -0.033708067568703926, "spearman_difference_eq_minus_ind": 3.685566326433465e-08, "kendall_between_the_two_scorings": 0.9999998335725867, "pairwise_ranking_accuracy_equilibrium": 0.5181601696950292, "pairwise_ranking_accuracy_independent": 0.5181601696950292, "spearman_equilibrium_ci95": [-0.07913392344371657, -0.023380127443993506], "spearman_independent_ci95": [-0.07913392344371657, -0.023380127443993506], "bootstrap_n": 400, "construct": "MAPK14-193_pos04mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 16437.9551438914, "f_over_M": 0.41094887859728496}, {"n_transcripts": 3809, "spearman_equilibrium": 0.028091299708919198, "spearman_p_equilibrium": 0.08300923761215677, "kendall_equilibrium": 0.01887162167523587, "spearman_independent": 0.028091454801166343, "spearman_p_independent": 0.08300753731630005, "kendall_independent": 0.018871894861059085, "spearman_difference_eq_minus_ind": -1.5509224714563286e-07, "kendall_between_the_two_scorings": 0.999999862113346, "pairwise_ranking_accuracy_equilibrium": 0.49036023465514395, "pairwise_ranking_accuracy_independent": 0.49036023465514395, "spearman_equilibrium_ci95": [-0.0032880705266497626, 0.05568587139757043], "spearman_independent_ci95": [-0.003288059159090166, 0.055685890131466034], "bootstrap_n": 400, "construct": "MAPK14-193_pos05mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 23694.387721022453, "f_over_M": 0.5923596930255614}, {"n_transcripts": 581, "spearman_equilibrium": -0.08951259872803471, "spearman_p_equilibrium": 0.0309829251876887, "kendall_equilibrium": -0.059984032818233245, "spearman_independent": -0.08951259872803471, "spearman_p_independent": 0.0309829251876887, "kendall_independent": -0.059984032818233245, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999999, "pairwise_ranking_accuracy_equilibrium": 0.5296950079918228, "pairwise_ranking_accuracy_independent": 0.5296950079918228, "spearman_equilibrium_ci95": [-0.16847579121890258, -0.017019534656291937], "spearman_independent_ci95": [-0.16847579121890258, -0.017019534656291937], "bootstrap_n": 400, "construct": "MAPK14-193_pos06mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 37783.48325477779, "f_over_M": 0.9445870813694448}, {"n_transcripts": 752, "spearman_equilibrium": 0.026952184067538253, "spearman_p_equilibrium": 0.46051199996351344, "kendall_equilibrium": 0.015598215038033235, "spearman_independent": 0.026952184067538253, "spearman_p_independent": 0.46051199996351344, "kendall_independent": 0.015598215038033235, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4912066340838074, "pairwise_ranking_accuracy_independent": 0.4912066340838074, "spearman_equilibrium_ci95": [-0.041315008843826106, 0.0906303758774121], "spearman_independent_ci95": [-0.041315008843826106, 0.0906303758774121], "bootstrap_n": 400, "construct": "MAPK14-193_pos07mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 36203.64819016018, "f_over_M": 0.9050912047540045}, {"n_transcripts": 951, "spearman_equilibrium": -0.03504310516763995, "spearman_p_equilibrium": 0.2803294066446322, "kendall_equilibrium": -0.023132931592382538, "spearman_independent": -0.035044213628363644, "spearman_p_independent": 0.2803141840761665, "kendall_independent": -0.02313506887049517, "spearman_difference_eq_minus_ind": 1.1084607236949706e-06, "kendall_between_the_two_scorings": 0.9999966793680838, "pairwise_ranking_accuracy_equilibrium": 0.5123342128584232, "pairwise_ranking_accuracy_independent": 0.5123366544835528, "spearman_equilibrium_ci95": [-0.08937403524272058, 0.029534805093061552], "spearman_independent_ci95": [-0.08937403524272058, 0.029533715178004724], "bootstrap_n": 400, "construct": "MAPK14-193_pos08mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35531.751979158056, "f_over_M": 0.8882937994789514}, {"n_transcripts": 951, "spearman_equilibrium": -0.07516685144453047, "spearman_p_equilibrium": 0.02043581388042471, "kendall_equilibrium": -0.04964366309173334, "spearman_independent": -0.07515861969140854, "spearman_p_independent": 0.02044964686010401, "kendall_independent": -0.04963702120664771, "spearman_difference_eq_minus_ind": -8.231753121937246e-06, "kendall_between_the_two_scorings": 0.9999911449962587, "pairwise_ranking_accuracy_equilibrium": 0.525335562909597, "pairwise_ranking_accuracy_independent": 0.5253305563760707, "spearman_equilibrium_ci95": [-0.13984924907359506, -0.009122778568480396], "spearman_independent_ci95": [-0.13984721714178697, -0.00911248490135273], "bootstrap_n": 400, "construct": "MAPK14-193_pos09mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35024.44557744873, "f_over_M": 0.8756111394362183}, {"n_transcripts": 950, "spearman_equilibrium": -0.036741674312169695, "spearman_p_equilibrium": 0.2579097078685261, "kendall_equilibrium": -0.024611841733836584, "spearman_independent": -0.03674146462582355, "spearman_p_independent": 0.25791242621927285, "kendall_independent": -0.0246140877181472, "spearman_difference_eq_minus_ind": -2.096863461475973e-07, "kendall_between_the_two_scorings": 0.999987798723918, "pairwise_ranking_accuracy_equilibrium": 0.5109928350048317, "pairwise_ranking_accuracy_independent": 0.5109928350048317, "spearman_equilibrium_ci95": [-0.10281488095529645, 0.023868833606000096], "spearman_independent_ci95": [-0.10280566509173811, 0.023868833606000096], "bootstrap_n": 400, "construct": "MAPK14-193_pos10mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35126.89380283674, "f_over_M": 0.8781723450709186}, {"n_transcripts": 950, "spearman_equilibrium": -0.09966220442276137, "spearman_p_equilibrium": 0.0021021283640688514, "kendall_equilibrium": -0.06707062807130494, "spearman_independent": -0.09966652295802814, "spearman_p_independent": 0.002101184481363075, "kendall_independent": -0.06708179623453667, "spearman_difference_eq_minus_ind": 4.318535266764623e-06, "kendall_between_the_two_scorings": 0.999987798723918, "pairwise_ranking_accuracy_equilibrium": 0.5339455789125798, "pairwise_ranking_accuracy_independent": 0.5339455789125798, "spearman_equilibrium_ci95": [-0.16030116471513023, -0.032261202442517636], "spearman_independent_ci95": [-0.1603040562593841, -0.03226797415317628], "bootstrap_n": 400, "construct": "MAPK14-193_pos11mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35455.867911552676, "f_over_M": 0.8863966977888169}, {"n_transcripts": 949, "spearman_equilibrium": -0.06162253587608544, "spearman_p_equilibrium": 0.05774406259046985, "kendall_equilibrium": -0.04145567377469735, "spearman_independent": -0.06162220371143633, "spearman_p_independent": 0.05774541355984653, "kendall_independent": -0.04145358858750575, "spearman_difference_eq_minus_ind": -3.3216464911250965e-07, "kendall_between_the_two_scorings": 0.9999966653494795, "pairwise_ranking_accuracy_equilibrium": 0.5196108863700084, "pairwise_ranking_accuracy_independent": 0.5196108863700084, "spearman_equilibrium_ci95": [-0.12904887251310365, 0.0008671246031928095], "spearman_independent_ci95": [-0.12904801382366532, 0.0008775153561667033], "bootstrap_n": 400, "construct": "MAPK14-193_pos12mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35072.38089901149, "f_over_M": 0.8768095224752873}, {"n_transcripts": 948, "spearman_equilibrium": -0.10520001111308738, "spearman_p_equilibrium": 0.00117947192147119, "kendall_equilibrium": -0.07039829324180391, "spearman_independent": -0.10519437229128627, "spearman_p_independent": 0.0011801960834103475, "kendall_independent": -0.07039184402981156, "spearman_difference_eq_minus_ind": -5.638821801115523e-06, "kendall_between_the_two_scorings": 0.9999966583068642, "pairwise_ranking_accuracy_equilibrium": 0.5358541201445981, "pairwise_ranking_accuracy_independent": 0.5358541201445981, "spearman_equilibrium_ci95": [-0.16036950244612716, -0.047002552495495765], "spearman_independent_ci95": [-0.1603689089568693, -0.04700235163980373], "bootstrap_n": 400, "construct": "MAPK14-193_pos13mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35729.36100000728, "f_over_M": 0.893234025000182}, {"n_transcripts": 948, "spearman_equilibrium": -0.0493285643542312, "spearman_p_equilibrium": 0.12908314877469765, "kendall_equilibrium": -0.03314336141446414, "spearman_independent": -0.04933071935922625, "spearman_p_independent": 0.12906640732345576, "kendall_independent": -0.03314781736517864, "spearman_difference_eq_minus_ind": 2.155004995049725e-06, "kendall_between_the_two_scorings": 0.9999910888331942, "pairwise_ranking_accuracy_equilibrium": 0.5173484048278175, "pairwise_ranking_accuracy_independent": 0.5173484048278175, "spearman_equilibrium_ci95": [-0.11100980670818827, 0.004606520185936777], "spearman_independent_ci95": [-0.11101192799693033, 0.00460553458957408], "bootstrap_n": 400, "construct": "MAPK14-193_pos14mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35206.62762860161, "f_over_M": 0.8801656907150401}, {"n_transcripts": 949, "spearman_equilibrium": -0.12062751362263166, "spearman_p_equilibrium": 0.00019551389918059074, "kendall_equilibrium": -0.08122218024783169, "spearman_independent": -0.12062606520862403, "spearman_p_independent": 0.00019554881863658322, "kendall_independent": -0.08121791392704276, "spearman_difference_eq_minus_ind": -1.4484140076348462e-06, "kendall_between_the_two_scorings": 0.9999977769107731, "pairwise_ranking_accuracy_equilibrium": 0.5393981875531968, "pairwise_ranking_accuracy_independent": 0.5393981875531968, "spearman_equilibrium_ci95": [-0.18921632910578806, -0.0555259713794178], "spearman_independent_ci95": [-0.18921628756036218, -0.0555259713794178], "bootstrap_n": 400, "construct": "MAPK14-193_pos15mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35836.43960803439, "f_over_M": 0.8959109902008596}, {"n_transcripts": 948, "spearman_equilibrium": -0.03898235615832314, "spearman_p_equilibrium": 0.2304798439077155, "kendall_equilibrium": -0.026125426957115384, "spearman_independent": -0.03897467983077289, "spearman_p_independent": 0.23057172913352747, "kendall_independent": -0.026112057868693837, "spearman_difference_eq_minus_ind": -7.67632755024894e-06, "kendall_between_the_two_scorings": 0.9999910888331942, "pairwise_ranking_accuracy_equilibrium": 0.512632685760064, "pairwise_ranking_accuracy_independent": 0.512632685760064, "spearman_equilibrium_ci95": [-0.10566776964723867, 0.02556563326607339], "spearman_independent_ci95": [-0.10565858919512383, 0.025565908184476748], "bootstrap_n": 400, "construct": "MAPK14-193_pos16mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 34958.56131525409, "f_over_M": 0.8739640328813523}, {"n_transcripts": 949, "spearman_equilibrium": -0.06818472728285715, "spearman_p_equilibrium": 0.03571440064877774, "kendall_equilibrium": -0.0463118299488969, "spearman_independent": -0.06819069753735466, "spearman_p_independent": 0.03569819529820546, "kendall_independent": -0.046314001898985546, "spearman_difference_eq_minus_ind": 5.970254497500438e-06, "kendall_between_the_two_scorings": 0.9999877729826873, "pairwise_ranking_accuracy_equilibrium": 0.5231207505982958, "pairwise_ranking_accuracy_independent": 0.5231207505982958, "spearman_equilibrium_ci95": [-0.1417172291710421, -0.006403064370984893], "spearman_independent_ci95": [-0.1417289806186463, -0.006409722769993862], "bootstrap_n": 400, "construct": "MAPK14-193_pos17mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35283.28093327746, "f_over_M": 0.8820820233319365}, {"n_transcripts": 949, "spearman_equilibrium": -0.11537478404798163, "spearman_p_equilibrium": 0.00036883702678958775, "kendall_equilibrium": -0.07758539292441914, "spearman_independent": -0.1153724531864417, "spearman_p_independent": 0.00036893881261940706, "kendall_independent": -0.07758273834223006, "spearman_difference_eq_minus_ind": -2.3308615399314503e-06, "kendall_between_the_two_scorings": 0.9999944422676659, "pairwise_ranking_accuracy_equilibrium": 0.538647947688333, "pairwise_ranking_accuracy_independent": 0.538647947688333, "spearman_equilibrium_ci95": [-0.17732397712139333, -0.048289981780821806], "spearman_independent_ci95": [-0.17732329977936556, -0.04828956373069914], "bootstrap_n": 400, "construct": "MAPK14-193_pos18mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35543.89885696229, "f_over_M": 0.8885974714240572}, {"n_transcripts": 949, "spearman_equilibrium": -0.1194627438632327, "spearman_p_equilibrium": 0.00022556527044691123, "kendall_equilibrium": -0.08024369628867122, "spearman_independent": -0.11946787441785131, "spearman_p_independent": 0.0002254238866984875, "kendall_independent": -0.08025685883766132, "spearman_difference_eq_minus_ind": 5.130554618607008e-06, "kendall_between_the_two_scorings": 0.9999888845439807, "pairwise_ranking_accuracy_equilibrium": 0.5389788244012598, "pairwise_ranking_accuracy_independent": 0.5389788244012598, "spearman_equilibrium_ci95": [-0.18808086739136515, -0.049714464530544455], "spearman_independent_ci95": [-0.18808613888721684, -0.04972673178224707], "bootstrap_n": 400, "construct": "MAPK14-193_pos19mut", "target_gene": "MAPK14", "rho": 0.5, "f_free_pool": 35491.14662972056, "f_over_M": 0.8872786657430141}, {"n_transcripts": 3400, "spearman_equilibrium": -0.05323693883593833, "spearman_p_equilibrium": 0.0019009837046200804, "kendall_equilibrium": -0.03546899695396181, "spearman_independent": -0.053237204686860606, "spearman_p_independent": 0.0019008838952735173, "kendall_independent": -0.035470035557316176, "spearman_difference_eq_minus_ind": 2.658509222763783e-07, "kendall_between_the_two_scorings": 0.9999987885701943, "pairwise_ranking_accuracy_equilibrium": 0.5177451878092837, "pairwise_ranking_accuracy_independent": 0.5177451878092837, "spearman_equilibrium_ci95": [-0.08543426915302832, -0.01979259729702229], "spearman_independent_ci95": [-0.08543427137990298, -0.019792880856642], "bootstrap_n": 400, "construct": "PIK3CB-6338_parent", "target_gene": "PIK3CB", "rho": 0.5, "f_free_pool": 25708.445155339607, "f_over_M": 0.6427111288834901}, {"n_transcripts": 2638, "spearman_equilibrium": -0.09037934339757642, "spearman_p_equilibrium": 3.330105300616815e-06, "kendall_equilibrium": -0.06047283522608301, "spearman_independent": -0.09037895806042781, "spearman_p_independent": 3.330426656224455e-06, "kendall_independent": -0.060472260110435445, "spearman_difference_eq_minus_ind": -3.8533714860622403e-07, "kendall_between_the_two_scorings": 0.9999994249904332, "pairwise_ranking_accuracy_equilibrium": 0.5300505429615173, "pairwise_ranking_accuracy_independent": 0.5300505429615173, "spearman_equilibrium_ci95": [-0.1262123113700062, -0.056116501204850816], "spearman_independent_ci95": [-0.12621228477387814, -0.05611493424753746], "bootstrap_n": 400, "construct": "PIK3CB-6340_parent", "target_gene": "PIK3CB", "rho": 0.5, "f_free_pool": 31795.794989557224, "f_over_M": 0.7948948747389306}, {"n_transcripts": 3141, "spearman_equilibrium": -0.09880491329264812, "spearman_p_equilibrium": 2.875351843468968e-08, "kendall_equilibrium": -0.0663043653110717, "spearman_independent": -0.09880686258240927, "spearman_p_independent": 2.8735433935690795e-08, "kendall_independent": -0.06630554188775147, "spearman_difference_eq_minus_ind": 1.949289761146722e-06, "kendall_between_the_two_scorings": 0.9999941192492416, "pairwise_ranking_accuracy_equilibrium": 0.5346326086412649, "pairwise_ranking_accuracy_independent": 0.5346326086412649, "spearman_equilibrium_ci95": [-0.1325647448773721, -0.06417295326666354], "spearman_independent_ci95": [-0.13256040285419088, -0.06417115182113123], "bootstrap_n": 400, "construct": "PLK1-319_parent", "target_gene": "PLK1", "rho": 0.5, "f_free_pool": 25949.745847117265, "f_over_M": 0.6487436461779317}, {"n_transcripts": 701, "spearman_equilibrium": 0.002419988018328926, "spearman_p_equilibrium": 0.9490034070272506, "kendall_equilibrium": 0.0012881765153668566, "spearman_independent": 0.002419988018328926, "spearman_p_independent": 0.9490034070272506, "kendall_independent": 0.0012881765153668566, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4990132139171901, "pairwise_ranking_accuracy_independent": 0.4990132139171901, "spearman_equilibrium_ci95": [-0.07248457154216703, 0.07957260780807121], "spearman_independent_ci95": [-0.07248457154216703, 0.07957260780807121], "bootstrap_n": 400, "construct": "PLK1-772_parent", "target_gene": "PLK1", "rho": 0.5, "f_free_pool": 37003.29131145803, "f_over_M": 0.9250822827864508}] |
| 2 | 24 | -0.0656001 | 0.0431401 | -0.0656001 | 0.0431409 | 6.5270e-08 | 8.7333e-06 | 0.999997 | 0.999988 | 92 | 0.627446 | 0.955494 | 0.839686 | 0.98507 | [{"n_transcripts": 949, "spearman_equilibrium": -0.08307153379610267, "spearman_p_equilibrium": 0.01046294066547962, "kendall_equilibrium": -0.05667038702281287, "spearman_independent": -0.08307412456365657, "spearman_p_independent": 0.010460528614151688, "kendall_independent": -0.0566726732569599, "spearman_difference_eq_minus_ind": 2.5907675538922037e-06, "kendall_between_the_two_scorings": 0.9999899960990962, "pairwise_ranking_accuracy_equilibrium": 0.5277043533982138, "pairwise_ranking_accuracy_independent": 0.5277043533982138, "construct": "MAPK14-193_parent", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 155018.26132915815, "f_over_M": 0.9688641333072384}, {"n_transcripts": 950, "spearman_equilibrium": -0.0927455757023374, "spearman_p_equilibrium": 0.004222864091096164, "kendall_equilibrium": -0.06329915693291618, "spearman_independent": -0.0927465134495906, "spearman_p_independent": 0.004222477124780412, "kendall_independent": -0.06329915693291618, "spearman_difference_eq_minus_ind": 9.377472532101638e-07, "kendall_between_the_two_scorings": 0.9999955631671889, "pairwise_ranking_accuracy_equilibrium": 0.530385938211838, "pairwise_ranking_accuracy_independent": 0.530385938211838, "construct": "MAPK14-193_pos01mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 154937.56684996106, "f_over_M": 0.9683597928122566}, {"n_transcripts": 743, "spearman_equilibrium": -0.11277813708270523, "spearman_p_equilibrium": 0.0020786341423314, "kendall_equilibrium": -0.0752762682459009, "spearman_independent": -0.11277813708270523, "spearman_p_independent": 0.0020786341423314, "kendall_independent": -0.0752762682459009, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.5385728592889334, "pairwise_ranking_accuracy_independent": 0.5385728592889334, "construct": "MAPK14-193_pos02mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 156229.9993794436, "f_over_M": 0.9764374961215224}, {"n_transcripts": 718, "spearman_equilibrium": -0.035454868170593165, "spearman_p_equilibrium": 0.34278608766977836, "kendall_equilibrium": -0.023779041618543797, "spearman_independent": -0.03545646512834478, "spearman_p_independent": 0.3427643351103264, "kendall_independent": -0.02378297328083878, "spearman_difference_eq_minus_ind": 1.5969577516136702e-06, "kendall_between_the_two_scorings": 0.9999980575188105, "pairwise_ranking_accuracy_equilibrium": 0.5105482484698528, "pairwise_ranking_accuracy_independent": 0.5105482484698528, "construct": "MAPK14-193_pos03mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 156572.25780266424, "f_over_M": 0.9785766112666515}, {"n_transcripts": 4903, "spearman_equilibrium": -0.050509243705741926, "spearman_p_equilibrium": 0.0004030391452565694, "kendall_equilibrium": -0.033708067568703926, "spearman_independent": -0.05050937114665655, "spearman_p_independent": 0.00040302550149272126, "kendall_independent": -0.03370814939292792, "spearman_difference_eq_minus_ind": 1.274409146267974e-07, "kendall_between_the_two_scorings": 0.9999998751794461, "pairwise_ranking_accuracy_equilibrium": 0.5181601696950292, "pairwise_ranking_accuracy_independent": 0.5181601696950292, "construct": "MAPK14-193_pos04mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 134349.8345026945, "f_over_M": 0.8396864656418406}, {"n_transcripts": 3809, "spearman_equilibrium": 0.02809122001087111, "spearman_p_equilibrium": 0.08301011136287738, "kendall_equilibrium": 0.018871616470947407, "spearman_independent": 0.028091434173985366, "spearman_p_independent": 0.08300776345305905, "kendall_independent": 0.01887175826815685, "spearman_difference_eq_minus_ind": -2.1416311425659362e-07, "kendall_between_the_two_scorings": 0.9999995173967989, "pairwise_ranking_accuracy_equilibrium": 0.49036023465514395, "pairwise_ranking_accuracy_independent": 0.49036023465514395, "construct": "MAPK14-193_pos05mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 142044.56963684858, "f_over_M": 0.8877785602303037}, {"n_transcripts": 581, "spearman_equilibrium": -0.08951259872803471, "spearman_p_equilibrium": 0.0309829251876887, "kendall_equilibrium": -0.059984032818233245, "spearman_independent": -0.08951259872803471, "spearman_p_independent": 0.0309829251876887, "kendall_independent": -0.059984032818233245, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999999, "pairwise_ranking_accuracy_equilibrium": 0.5296950079918228, "pairwise_ranking_accuracy_independent": 0.5296950079918228, "construct": "MAPK14-193_pos06mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 157611.14935670904, "f_over_M": 0.9850696834794315}, {"n_transcripts": 752, "spearman_equilibrium": 0.026952184067538253, "spearman_p_equilibrium": 0.46051199996351344, "kendall_equilibrium": 0.015598215038033235, "spearman_independent": 0.02696091739902728, "spearman_p_independent": 0.46036664324726106, "kendall_independent": 0.015601729241181481, "spearman_difference_eq_minus_ind": -8.733331489027552e-06, "kendall_between_the_two_scorings": 0.9999982293097053, "pairwise_ranking_accuracy_equilibrium": 0.4912066340838074, "pairwise_ranking_accuracy_independent": 0.4912066340838074, "construct": "MAPK14-193_pos07mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 156111.94777159003, "f_over_M": 0.9756996735724377}, {"n_transcripts": 951, "spearman_equilibrium": -0.03504310516763995, "spearman_p_equilibrium": 0.2803294066446322, "kendall_equilibrium": -0.023132931592382538, "spearman_independent": -0.03504271353023001, "spearman_p_independent": 0.2803347851625511, "kendall_independent": -0.02313282917128464, "spearman_difference_eq_minus_ind": -3.9163740993969354e-07, "kendall_between_the_two_scorings": 0.9999955724981294, "pairwise_ranking_accuracy_equilibrium": 0.5123342128584232, "pairwise_ranking_accuracy_independent": 0.512331647724428, "construct": "MAPK14-193_pos08mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 155180.15632778348, "f_over_M": 0.9698759770486467}, {"n_transcripts": 951, "spearman_equilibrium": -0.07515805463038915, "spearman_p_equilibrium": 0.020450596711095802, "kendall_equilibrium": -0.0496348072449525, "spearman_independent": -0.07516301757413751, "spearman_p_independent": 0.020442255461282276, "kendall_independent": -0.04964139418322714, "spearman_difference_eq_minus_ind": 4.962943748368365e-06, "kendall_between_the_two_scorings": 0.9999966793778851, "pairwise_ranking_accuracy_equilibrium": 0.5253305563760707, "pairwise_ranking_accuracy_independent": 0.5253305563760707, "construct": "MAPK14-193_pos09mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 154814.69655575935, "f_over_M": 0.967591853473496}, {"n_transcripts": 950, "spearman_equilibrium": -0.036742688910362385, "spearman_p_equilibrium": 0.2578965550092918, "kendall_equilibrium": -0.02461847047352705, "spearman_independent": -0.03673979881719735, "spearman_p_independent": 0.2579340222840588, "kendall_independent": -0.024607404369420494, "spearman_difference_eq_minus_ind": -2.8900931650366335e-06, "kendall_between_the_two_scorings": 0.9999900171600089, "pairwise_ranking_accuracy_equilibrium": 0.5109928350048317, "pairwise_ranking_accuracy_independent": 0.5109928350048317, "construct": "MAPK14-193_pos10mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 154855.45062301768, "f_over_M": 0.9678465663938605}, {"n_transcripts": 950, "spearman_equilibrium": -0.0996663130145361, "spearman_p_equilibrium": 0.002101230358785706, "kendall_equilibrium": -0.0670773587273438, "spearman_independent": -0.09966642007871264, "spearman_p_independent": 0.0021012069627161824, "kendall_independent": -0.06707980069770715, "spearman_difference_eq_minus_ind": 1.0706417653827405e-07, "kendall_between_the_two_scorings": 0.9999966723698551, "pairwise_ranking_accuracy_equilibrium": 0.5339455789125798, "pairwise_ranking_accuracy_independent": 0.5339455789125798, "construct": "MAPK14-193_pos11mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 155061.9551624593, "f_over_M": 0.9691372197653705}, {"n_transcripts": 949, "spearman_equilibrium": -0.06162253587608544, "spearman_p_equilibrium": 0.05774406259046985, "kendall_equilibrium": -0.04145567377469735, "spearman_independent": -0.06162069591846597, "spearman_p_independent": 0.057751546336711965, "kendall_independent": -0.04145113478407662, "spearman_difference_eq_minus_ind": -1.8399576194663703e-06, "kendall_between_the_two_scorings": 0.9999977769107731, "pairwise_ranking_accuracy_equilibrium": 0.5196108863700084, "pairwise_ranking_accuracy_independent": 0.5196108863700084, "construct": "MAPK14-193_pos12mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 154833.82065668644, "f_over_M": 0.9677113791042903}, {"n_transcripts": 948, "spearman_equilibrium": -0.10518568555237529, "spearman_p_equilibrium": 0.0011813124747632998, "kendall_equilibrium": -0.07038476755950882, "spearman_independent": -0.10518964695984372, "spearman_p_independent": 0.001180803246815551, "kendall_independent": -0.0703892238428707, "spearman_difference_eq_minus_ind": 3.9614074684307665e-06, "kendall_between_the_two_scorings": 0.9999977722182245, "pairwise_ranking_accuracy_equilibrium": 0.5358541201445981, "pairwise_ranking_accuracy_independent": 0.5358541201445981, "construct": "MAPK14-193_pos13mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 155295.04127875465, "f_over_M": 0.9705940079922166}, {"n_transcripts": 948, "spearman_equilibrium": -0.049329229523078666, "spearman_p_equilibrium": 0.12907798113977945, "kendall_equilibrium": -0.03314555246914858, "spearman_independent": -0.049331148951725266, "spearman_p_independent": 0.12906307017665683, "kendall_independent": -0.03315227331589314, "spearman_difference_eq_minus_ind": 1.919428646600385e-06, "kendall_between_the_two_scorings": 0.9999877471599107, "pairwise_ranking_accuracy_equilibrium": 0.5173484048278175, "pairwise_ranking_accuracy_independent": 0.5173484048278175, "construct": "MAPK14-193_pos14mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 154879.47611693165, "f_over_M": 0.9679967257308228}, {"n_transcripts": 949, "spearman_equilibrium": -0.1206247445524063, "spearman_p_equilibrium": 0.00019558066311120014, "kendall_equilibrium": -0.08121560020935684, "spearman_independent": -0.12062613456442507, "spearman_p_independent": 0.00019554714642131427, "kendall_independent": -0.08122004708975815, "spearman_difference_eq_minus_ind": 1.3900120187787524e-06, "kendall_between_the_two_scorings": 0.9999911076332075, "pairwise_ranking_accuracy_equilibrium": 0.5393981875531968, "pairwise_ranking_accuracy_independent": 0.5393981875531968, "construct": "MAPK14-193_pos15mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 155424.00085059938, "f_over_M": 0.9714000053162462}, {"n_transcripts": 948, "spearman_equilibrium": -0.03897525027346241, "spearman_p_equilibrium": 0.23056490007133432, "kendall_equilibrium": -0.026116514231501017, "spearman_independent": -0.03898235615832314, "spearman_p_independent": 0.2304798439077155, "kendall_independent": -0.026125426957115384, "spearman_difference_eq_minus_ind": 7.105884860733602e-06, "kendall_between_the_two_scorings": 0.9999955444165972, "pairwise_ranking_accuracy_equilibrium": 0.512632685760064, "pairwise_ranking_accuracy_independent": 0.512632685760064, "construct": "MAPK14-193_pos16mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 154763.09090694744, "f_over_M": 0.9672693181684215}, {"n_transcripts": 949, "spearman_equilibrium": -0.06818573612656324, "spearman_p_equilibrium": 0.03571166185572163, "kendall_equilibrium": -0.046309760945454276, "spearman_independent": -0.06817814530818195, "spearman_p_independent": 0.03573227368113704, "kendall_independent": -0.046300661331947914, "spearman_difference_eq_minus_ind": -7.59081838129505e-06, "kendall_between_the_two_scorings": 0.9999955538067193, "pairwise_ranking_accuracy_equilibrium": 0.5231207505982958, "pairwise_ranking_accuracy_independent": 0.5231207505982958, "construct": "MAPK14-193_pos17mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 154982.38512887992, "f_over_M": 0.9686399070554995}, {"n_transcripts": 949, "spearman_equilibrium": -0.11537887794077872, "spearman_p_equilibrium": 0.0003686583150209769, "kendall_equilibrium": -0.07759180436910319, "spearman_independent": -0.11537478404798163, "spearman_p_independent": 0.00036883702678958775, "kendall_independent": -0.07758539292441914, "spearman_difference_eq_minus_ind": -4.093892797096821e-06, "kendall_between_the_two_scorings": 0.9999966653494795, "pairwise_ranking_accuracy_equilibrium": 0.538647947688333, "pairwise_ranking_accuracy_independent": 0.538647947688333, "construct": "MAPK14-193_pos18mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 155161.98582573183, "f_over_M": 0.9697624114108239}, {"n_transcripts": 949, "spearman_equilibrium": -0.11946307633160502, "spearman_p_equilibrium": 0.0002255561060300945, "kendall_equilibrium": -0.08024618737625253, "spearman_independent": -0.11946307633160502, "spearman_p_independent": 0.0002255561060300945, "kendall_independent": -0.08024618737625253, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999998, "pairwise_ranking_accuracy_equilibrium": 0.5389788244012598, "pairwise_ranking_accuracy_independent": 0.5389788244012598, "construct": "MAPK14-193_pos19mut", "target_gene": "MAPK14", "rho": 2.0, "f_free_pool": 155131.16738957114, "f_over_M": 0.9695697961848196}, {"n_transcripts": 3400, "spearman_equilibrium": -0.05323547877926993, "spearman_p_equilibrium": 0.001901531944600454, "kendall_equilibrium": -0.03546814065841686, "spearman_independent": -0.053236712242062334, "spearman_p_independent": 0.0019010687793535187, "kendall_independent": -0.035469179262040844, "spearman_difference_eq_minus_ind": 1.2334627924048824e-06, "kendall_between_the_two_scorings": 0.9999994808155283, "pairwise_ranking_accuracy_equilibrium": 0.5177451878092837, "pairwise_ranking_accuracy_independent": 0.5177451878092837, "construct": "PIK3CB-6338_parent", "target_gene": "PIK3CB", "rho": 2.0, "f_free_pool": 143842.44240381446, "f_over_M": 0.8990152650238404}, {"n_transcripts": 2638, "spearman_equilibrium": -0.09037915074377158, "spearman_p_equilibrium": 3.3302659623882974e-06, "kendall_equilibrium": -0.06047255636133446, "spearman_independent": -0.09037895806042781, "spearman_p_independent": 3.330426656224455e-06, "kendall_independent": -0.060472260110435445, "spearman_difference_eq_minus_ind": -1.9268334376654206e-07, "kendall_between_the_two_scorings": 0.9999998562475979, "pairwise_ranking_accuracy_equilibrium": 0.5300505429615173, "pairwise_ranking_accuracy_independent": 0.5300505429615173, "construct": "PIK3CB-6340_parent", "target_gene": "PIK3CB", "rho": 2.0, "f_free_pool": 150076.06386465242, "f_over_M": 0.9379753991540776}, {"n_transcripts": 3141, "spearman_equilibrium": -0.098802814411746, "spearman_p_equilibrium": 2.8773003103366163e-08, "kendall_equilibrium": -0.06630308117097045, "spearman_independent": -0.09880439434141491, "spearman_p_independent": 2.8758334855074905e-08, "kendall_independent": -0.06630470372119672, "spearman_difference_eq_minus_ind": 1.5799296689128495e-06, "kendall_between_the_two_scorings": 0.9999943220416317, "pairwise_ranking_accuracy_equilibrium": 0.5346326086412649, "pairwise_ranking_accuracy_independent": 0.5346326086412649, "construct": "PLK1-319_parent", "target_gene": "PLK1", "rho": 2.0, "f_free_pool": 145048.4667637839, "f_over_M": 0.9065529172736493}, {"n_transcripts": 701, "spearman_equilibrium": 0.002419988018328926, "spearman_p_equilibrium": 0.9490034070272506, "kendall_equilibrium": 0.0012881765153668566, "spearman_independent": 0.002419988018328926, "spearman_p_independent": 0.9490034070272506, "kendall_independent": 0.0012881765153668566, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4990132139171901, "pairwise_ranking_accuracy_independent": 0.4990132139171901, "construct": "PLK1-772_parent", "target_gene": "PLK1", "rho": 2.0, "f_free_pool": 156872.68192789675, "f_over_M": 0.9804542620493547}] |
| 10 | 24 | -0.0656005 | 0.0431403 | -0.0656005 | 0.0431406 | 3.0500e-08 | 1.6501e-05 | 0.999995 | 0.999988 | 98 | 0.543016 | 0.990613 | 0.966664 | 0.996816 | [{"n_transcripts": 949, "spearman_equilibrium": -0.08306953331357741, "spearman_p_equilibrium": 0.010464803488803345, "kendall_equilibrium": -0.0566726732569599, "spearman_independent": -0.08306734299243876, "spearman_p_independent": 0.010466843425230167, "kendall_independent": -0.05666822677206273, "spearman_difference_eq_minus_ind": -2.1903211386564703e-06, "kendall_between_the_two_scorings": 0.9999911076332075, "pairwise_ranking_accuracy_equilibrium": 0.5277043533982138, "pairwise_ranking_accuracy_independent": 0.5277043533982138, "construct": "MAPK14-193_parent", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794778.1078042747, "f_over_M": 0.9934726347553433}, {"n_transcripts": 950, "spearman_equilibrium": -0.09275597489948859, "spearman_p_equilibrium": 0.0042185746040697865, "kendall_equilibrium": -0.0633080310611838, "spearman_independent": -0.09274452598526292, "spearman_p_independent": 0.004223297300441577, "kendall_independent": -0.06329471986878236, "spearman_difference_eq_minus_ind": -1.144891422566463e-05, "kendall_between_the_two_scorings": 0.9999911263343775, "pairwise_ranking_accuracy_equilibrium": 0.530385938211838, "pairwise_ranking_accuracy_independent": 0.530385938211838, "construct": "MAPK14-193_pos01mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794747.8193974316, "f_over_M": 0.9934347742467895}, {"n_transcripts": 743, "spearman_equilibrium": -0.11277937963995259, "spearman_p_equilibrium": 0.0020783959766919723, "kendall_equilibrium": -0.07527975964428314, "spearman_independent": -0.11277689287573685, "spearman_p_independent": 0.0020788726492119917, "kendall_independent": -0.0752725037638355, "spearman_difference_eq_minus_ind": -2.486764215742232e-06, "kendall_between_the_two_scorings": 0.9999927445012391, "pairwise_ranking_accuracy_equilibrium": 0.5385728592889334, "pairwise_ranking_accuracy_independent": 0.5385728592889334, "construct": "MAPK14-193_pos02mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 796083.1536750062, "f_over_M": 0.9951039420937577}, {"n_transcripts": 718, "spearman_equilibrium": -0.03545646512834478, "spearman_p_equilibrium": 0.3427643351103264, "kendall_equilibrium": -0.02378297328083878, "spearman_independent": -0.03545646512834478, "spearman_p_independent": 0.3427643351103264, "kendall_independent": -0.02378297328083878, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999999, "pairwise_ranking_accuracy_equilibrium": 0.5105482484698528, "pairwise_ranking_accuracy_independent": 0.5105482484698528, "construct": "MAPK14-193_pos03mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 796186.3684186775, "f_over_M": 0.9952329605233469}, {"n_transcripts": 4903, "spearman_equilibrium": -0.05050922242719601, "spearman_p_equilibrium": 0.0004030414233696224, "kendall_equilibrium": -0.03370790111527594, "spearman_independent": -0.050509349868110634, "spearman_p_independent": 0.00040302777953375106, "kendall_independent": -0.03370798293950686, "spearman_difference_eq_minus_ind": 1.274409146267974e-07, "kendall_between_the_two_scorings": 0.9999998751794461, "pairwise_ranking_accuracy_equilibrium": 0.5181601696950292, "pairwise_ranking_accuracy_independent": 0.5181601696950292, "construct": "MAPK14-193_pos04mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 773331.2237807373, "f_over_M": 0.9666640297259216}, {"n_transcripts": 3809, "spearman_equilibrium": 0.028091312844622754, "spearman_p_equilibrium": 0.08300909360268942, "kendall_equilibrium": 0.01887175826815685, "spearman_independent": 0.02809132033610018, "spearman_p_independent": 0.08300901147214503, "kendall_independent": 0.01887175826815685, "spearman_difference_eq_minus_ind": -7.491477424514947e-09, "kendall_between_the_two_scorings": 0.9999998621133366, "pairwise_ranking_accuracy_equilibrium": 0.49036023465514395, "pairwise_ranking_accuracy_independent": 0.49036023465514395, "construct": "MAPK14-193_pos05mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 780835.491711216, "f_over_M": 0.9760443646390201}, {"n_transcripts": 581, "spearman_equilibrium": -0.08951259872803471, "spearman_p_equilibrium": 0.0309829251876887, "kendall_equilibrium": -0.059984032818233245, "spearman_independent": -0.08951259872803471, "spearman_p_independent": 0.0309829251876887, "kendall_independent": -0.059984032818233245, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 0.9999999999999999, "pairwise_ranking_accuracy_equilibrium": 0.5296950079918228, "pairwise_ranking_accuracy_independent": 0.5296950079918228, "construct": "MAPK14-193_pos06mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 797452.6851135932, "f_over_M": 0.9968158563919916}, {"n_transcripts": 752, "spearman_equilibrium": 0.026952184067538253, "spearman_p_equilibrium": 0.46051199996351344, "kendall_equilibrium": 0.015598215038033235, "spearman_independent": 0.02696091739902728, "spearman_p_independent": 0.46036664324726106, "kendall_independent": 0.015601729241181481, "spearman_difference_eq_minus_ind": -8.733331489027552e-06, "kendall_between_the_two_scorings": 0.9999982293097053, "pairwise_ranking_accuracy_equilibrium": 0.4912066340838074, "pairwise_ranking_accuracy_independent": 0.4912066340838074, "construct": "MAPK14-193_pos07mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 795987.746296857, "f_over_M": 0.9949846828710712}, {"n_transcripts": 951, "spearman_equilibrium": -0.03504349484934753, "spearman_p_equilibrium": 0.2803240550546451, "kendall_equilibrium": -0.02313282917128464, "spearman_independent": -0.035040725596564626, "spearman_p_independent": 0.2803620873539564, "kendall_independent": -0.023126212494240794, "spearman_difference_eq_minus_ind": -2.769252782905407e-06, "kendall_between_the_two_scorings": 0.9999878243839452, "pairwise_ranking_accuracy_equilibrium": 0.5123366544835528, "pairwise_ranking_accuracy_independent": 0.512331647724428, "construct": "MAPK14-193_pos08mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794947.4660681935, "f_over_M": 0.9936843325852419}, {"n_transcripts": 951, "spearman_equilibrium": -0.07515627843617632, "spearman_p_equilibrium": 0.020453582691637134, "kendall_equilibrium": -0.0496346973662164, "spearman_independent": -0.07516245461047316, "spearman_p_independent": 0.02044320148874819, "kendall_independent": -0.049639400002518874, "spearman_difference_eq_minus_ind": 6.176174296837478e-06, "kendall_between_the_two_scorings": 0.9999944656318505, "pairwise_ranking_accuracy_equilibrium": 0.5253305563760707, "pairwise_ranking_accuracy_independent": 0.5253331864742813, "construct": "MAPK14-193_pos09mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794680.974469444, "f_over_M": 0.993351218086805}, {"n_transcripts": 950, "spearman_equilibrium": -0.036739959645300246, "spearman_p_equilibrium": 0.2579319372035535, "kendall_equilibrium": -0.024609595754538752, "spearman_independent": -0.036741367423565596, "spearman_p_independent": 0.2579136863453921, "kendall_independent": -0.024611950932948032, "spearman_difference_eq_minus_ind": 1.4077782653498794e-06, "kendall_between_the_two_scorings": 0.9999944539682135, "pairwise_ranking_accuracy_equilibrium": 0.5109928350048317, "pairwise_ranking_accuracy_independent": 0.5109928350048317, "construct": "MAPK14-193_pos10mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794692.5904741078, "f_over_M": 0.9933657380926347}, {"n_transcripts": 950, "spearman_equilibrium": -0.09967052833340932, "spearman_p_equilibrium": 0.002100309391502791, "kendall_equilibrium": -0.06708608491702324, "spearman_independent": -0.09966767694974865, "spearman_p_independent": 0.00210093232433168, "kendall_independent": -0.06707950307584644, "spearman_difference_eq_minus_ind": -2.8513836606708365e-06, "kendall_between_the_two_scorings": 0.9999922355690326, "pairwise_ranking_accuracy_equilibrium": 0.5339455789125798, "pairwise_ranking_accuracy_independent": 0.5339455789125798, "construct": "MAPK14-193_pos11mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794804.043026272, "f_over_M": 0.9935050537828399}, {"n_transcripts": 949, "spearman_equilibrium": -0.061623950026328256, "spearman_p_equilibrium": 0.057738311297646394, "kendall_equilibrium": -0.04145785111274056, "spearman_independent": -0.06162220371143633, "spearman_p_independent": 0.05774541355984653, "kendall_independent": -0.04145358858750575, "spearman_difference_eq_minus_ind": -1.7463148919288907e-06, "kendall_between_the_two_scorings": 0.9999955538067193, "pairwise_ranking_accuracy_equilibrium": 0.5196108863700084, "pairwise_ranking_accuracy_independent": 0.5196108863700084, "construct": "MAPK14-193_pos12mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794700.0863683892, "f_over_M": 0.9933751079604864}, {"n_transcripts": 948, "spearman_equilibrium": -0.10518350978958328, "spearman_p_equilibrium": 0.0011815922492241068, "kendall_equilibrium": -0.07038261781642817, "spearman_independent": -0.10520001111308738, "spearman_p_independent": 0.00117947192147119, "kendall_independent": -0.07039829324180391, "spearman_difference_eq_minus_ind": 1.6501323504100607e-05, "kendall_between_the_two_scorings": 0.9999877471599107, "pairwise_ranking_accuracy_equilibrium": 0.5358541201445981, "pairwise_ranking_accuracy_independent": 0.5358541201445981, "construct": "MAPK14-193_pos13mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794960.7693687067, "f_over_M": 0.9937009617108834}, {"n_transcripts": 948, "spearman_equilibrium": -0.04932977883807354, "spearman_p_equilibrium": 0.12907371368363652, "kendall_equilibrium": -0.03314555246914858, "spearman_independent": -0.04932907458808011, "spearman_p_independent": 0.1290791848010405, "kendall_independent": -0.03314109652339754, "spearman_difference_eq_minus_ind": -7.042499934259427e-07, "kendall_between_the_two_scorings": 0.9999910888530463, "pairwise_ranking_accuracy_equilibrium": 0.5173484048278175, "pairwise_ranking_accuracy_independent": 0.5173484048278175, "construct": "MAPK14-193_pos14mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794690.5234689056, "f_over_M": 0.993363154336132}, {"n_transcripts": 949, "spearman_equilibrium": -0.1206247445524063, "spearman_p_equilibrium": 0.00019558066311120014, "kendall_equilibrium": -0.08121560020935684, "spearman_independent": -0.1206148179009185, "spearman_p_independent": 0.00019582017639808777, "kendall_independent": -0.0812022595681529, "spearman_difference_eq_minus_ind": -9.926651487787708e-06, "kendall_between_the_two_scorings": 0.9999911076332075, "pairwise_ranking_accuracy_equilibrium": 0.5393981875531968, "pairwise_ranking_accuracy_independent": 0.5393981875531968, "construct": "MAPK14-193_pos15mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 795073.1245545016, "f_over_M": 0.9938414056931271}, {"n_transcripts": 948, "spearman_equilibrium": -0.03897525027346241, "spearman_p_equilibrium": 0.23056490007133432, "kendall_equilibrium": -0.026116514231501017, "spearman_independent": -0.03898547923355562, "spearman_p_independent": 0.23044246830460235, "kendall_independent": -0.026127626035080953, "spearman_difference_eq_minus_ind": 1.0228960093214279e-05, "kendall_between_the_two_scorings": 0.9999877471599108, "pairwise_ranking_accuracy_equilibrium": 0.512632685760064, "pairwise_ranking_accuracy_independent": 0.512632685760064, "construct": "MAPK14-193_pos16mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794655.4472518303, "f_over_M": 0.9933193090647878}, {"n_transcripts": 949, "spearman_equilibrium": -0.06818573612656324, "spearman_p_equilibrium": 0.03571166185572163, "kendall_equilibrium": -0.046309760945454276, "spearman_independent": -0.06819332311549256, "spearman_p_independent": 0.03569107054722144, "kendall_independent": -0.04631844875466476, "spearman_difference_eq_minus_ind": 7.5869889293173065e-06, "kendall_between_the_two_scorings": 0.9999955538067193, "pairwise_ranking_accuracy_equilibrium": 0.5231207505982958, "pairwise_ranking_accuracy_independent": 0.5231207505982958, "construct": "MAPK14-193_pos17mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794766.9413584191, "f_over_M": 0.9934586766980239}, {"n_transcripts": 949, "spearman_equilibrium": -0.11537128201766088, "spearman_p_equilibrium": 0.00036898996600242303, "kendall_equilibrium": -0.07758291081596329, "spearman_independent": -0.11537478404798163, "spearman_p_independent": 0.00036883702678958775, "kendall_independent": -0.07758539292441914, "spearman_difference_eq_minus_ind": 3.5020303207483616e-06, "kendall_between_the_two_scorings": 0.9999966653494795, "pairwise_ranking_accuracy_equilibrium": 0.538647947688333, "pairwise_ranking_accuracy_independent": 0.538647947688333, "construct": "MAPK14-193_pos18mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794876.6041140612, "f_over_M": 0.9935957551425765}, {"n_transcripts": 949, "spearman_equilibrium": -0.1194646112533394, "spearman_p_equilibrium": 0.00022551380077755624, "kendall_equilibrium": -0.08024814327785287, "spearman_independent": -0.11946307633160502, "spearman_p_independent": 0.0002255561060300945, "kendall_independent": -0.08024618737625253, "spearman_difference_eq_minus_ind": -1.5349217343807453e-06, "kendall_between_the_two_scorings": 0.9999966653494795, "pairwise_ranking_accuracy_equilibrium": 0.5389788244012598, "pairwise_ranking_accuracy_independent": 0.5389788244012598, "construct": "MAPK14-193_pos19mut", "target_gene": "MAPK14", "rho": 10.0, "f_free_pool": 794853.8499255136, "f_over_M": 0.993567312406892}, {"n_transcripts": 3400, "spearman_equilibrium": -0.053235974192739545, "spearman_p_equilibrium": 0.0019013459044089525, "kendall_equilibrium": -0.03546916698534914, "spearman_independent": -0.05323655955326857, "spearman_p_independent": 0.0019011261083744931, "kendall_independent": -0.03546916698534914, "spearman_difference_eq_minus_ind": 5.853605290276342e-07, "kendall_between_the_two_scorings": 0.999998961631775, "pairwise_ranking_accuracy_equilibrium": 0.5177451878092837, "pairwise_ranking_accuracy_independent": 0.5177451878092837, "construct": "PIK3CB-6338_parent", "target_gene": "PIK3CB", "rho": 10.0, "f_free_pool": 782578.9715607814, "f_over_M": 0.9782237144509767}, {"n_transcripts": 2638, "spearman_equilibrium": -0.09037934339757642, "spearman_p_equilibrium": 3.330105300616815e-06, "kendall_equilibrium": -0.06047283522608301, "spearman_independent": -0.09037895806042781, "spearman_p_independent": 3.330426656224455e-06, "kendall_independent": -0.060472260110435445, "spearman_difference_eq_minus_ind": -3.8533714860622403e-07, "kendall_between_the_two_scorings": 0.9999994249904332, "pairwise_ranking_accuracy_equilibrium": 0.5300505429615173, "pairwise_ranking_accuracy_independent": 0.5300505429615173, "construct": "PIK3CB-6340_parent", "target_gene": "PIK3CB", "rho": 10.0, "f_free_pool": 788819.8260447704, "f_over_M": 0.986024782555963}, {"n_transcripts": 3141, "spearman_equilibrium": -0.09880804347554112, "spearman_p_equilibrium": 2.8724483587847018e-08, "kendall_equilibrium": -0.06630652236724313, "spearman_independent": -0.09880744434845296, "spearman_p_independent": 2.8730038749858458e-08, "kendall_independent": -0.06630657615096533, "spearman_difference_eq_minus_ind": -5.991270881633426e-07, "kendall_between_the_two_scorings": 0.9999973638037685, "pairwise_ranking_accuracy_equilibrium": 0.5346326086412649, "pairwise_ranking_accuracy_independent": 0.5346326086412649, "construct": "PLK1-319_parent", "target_gene": "PLK1", "rho": 10.0, "f_free_pool": 784461.3211747815, "f_over_M": 0.980576651468477}, {"n_transcripts": 701, "spearman_equilibrium": 0.002419988018328926, "spearman_p_equilibrium": 0.9490034070272506, "kendall_equilibrium": 0.0012881765153668566, "spearman_independent": 0.002419988018328926, "spearman_p_independent": 0.9490034070272506, "kendall_independent": 0.0012881765153668566, "spearman_difference_eq_minus_ind": 0.0, "kendall_between_the_two_scorings": 1.0, "pairwise_ranking_accuracy_equilibrium": 0.4990132139171901, "pairwise_ranking_accuracy_independent": 0.4990132139171901, "construct": "PLK1-772_parent", "target_gene": "PLK1", "rho": 10.0, "f_free_pool": 796803.9792776708, "f_over_M": 0.9960049740970885}] |


**`pooled_across_constructs`**

| rho | n_pairs_pooled | pooled_spearman_equilibrium | pooled_spearman_p_equilibrium | pooled_spearman_independent | pooled_spearman_p_independent | pooled_spearman_difference | pooled_kendall_between_the_two_scorings | pooled_spearman_between_the_two_scorings |
|---|---|---|---|---|---|---|---|---|
| 0.001 | 34676 | -0.061921 | 8.1709e-31 | -0.0529612 | 5.6876e-23 | -0.00895978 | 0.64612 | 0.831358 |
| 0.01 | 34676 | -0.071026 | 4.9957e-40 | -0.0529612 | 5.6880e-23 | -0.0180649 | 0.655291 | 0.838606 |
| 0.1 | 34676 | -0.0745539 | 6.1690e-44 | -0.0529612 | 5.6873e-23 | -0.0215926 | 0.704897 | 0.866194 |
| 0.5 | 34676 | -0.0559441 | 1.8983e-25 | -0.0529612 | 5.6878e-23 | -0.00298291 | 0.969939 | 0.998579 |
| 2 | 34676 | -0.0535443 | 1.9113e-23 | -0.0529612 | 5.6879e-23 | -5.8313e-04 | 0.994 | 0.999946 |
| 10 | 34676 | -0.053075 | 4.6014e-23 | -0.0529612 | 5.6877e-23 | -1.1383e-04 | 0.998818 | 0.999998 |


**`pooled_rho_values_where_scorings_diverge_kendall_below_0.99`**: `[0.001, 0.01, 0.1, 0.5]`


**`predictor_diagnostics_parent_construct`**

| predictor | spearman_vs_measured | p | n |
|---|---|---|---|
| minus_log10_K_thermodynamic | -0.0830718 | 0.0104627 | 949 |
| best_ddG_kcal | 0.0826515 | 0.0108606 | 949 |
| dg_duplex_kcal | 0.00114819 | 0.971821 | 949 |
| log10_p_unpaired_15 | -0.130473 | 5.5474e-05 | 949 |
| n_sites | -0.0584612 | 0.0718429 | 949 |
| n_8mer_sites | -0.0270843 | 0.404615 | 949 |
| utr3_len | 0.0603746 | 0.0630081 | 949 |
| local_au_content | -0.175449 | 5.3286e-08 | 949 |
| abundance_x | -0.129462 | 6.3405e-05 | 949 |


**`fitted_monotone_map_phi_parent_construct`**

```json
{
  "table": [
    {
      "bin": 0,
      "n": 38,
      "occupancy_mid": 0.012429180901646453,
      "phi_fitted_log10ratio": 0.0035904320348114395,
      "observed_median_log10ratio": -0.00545
    },
    {
      "bin": 1,
      "n": 38,
      "occupancy_mid": 0.1145462605013852,
      "phi_fitted_log10ratio": 0.003421653543307088,
      "observed_median_log10ratio": 0.0034999999999999996
    },
    {
      "bin": 2,
      "n": 38,
      "occupancy_mid": 0.2630306177844257,
      "phi_fitted_log10ratio": 0.003421653543307088,
      "observed_median_log10ratio": 0.004274999999999999
    },
    {
      "bin": 3,
      "n": 38,
      "occupancy_mid": 0.5074522923886546,
      "phi_fitted_log10ratio": 0.003421653543307088,
      "observed_median_log10ratio": 0.003275
    },
    {
      "bin": 4,
      "n": 38,
      "occupancy_mid": 0.7113475174471362,
      "phi_fitted_log10ratio": -0.0060141566265060255,
      "observed_median_log10ratio": 0.003400000000000001
    },
    {
      "bin": 5,
      "n": 38,
      "occupancy_mid": 0.8250717119903812,
      "phi_fitted_log10ratio": -0.0060141566265060255,
      "observed_median_log10ratio": -0.002849999999999999
    },
    {
      "bin": 6,
      "n": 38,
      "occupancy_mid": 0.8806698789003872,
      "phi_fitted_log10ratio": -0.0060141566265060255,
      "observed_median_log10ratio": -0.00165
    },
    {
      "bin": 7,
      "n": 38,
      "occupancy_mid": 0.9308365653394706,
      "phi_fitted_log10ratio": -0.016311764705882352,
      "observed_median_log10ratio": -0.0058874999999999995
    },
    {
      "bin": 8,
      "n": 38,
      "occupancy_mid": 0.964673787416171,
      "phi_fitted_log10ratio": -0.016311764705882352,
      "observed_median_log10ratio": -0.012525
    },
    {
      "bin": 9,
      "n": 38,
      "occupancy_mid": 0.978948560226059,
      "phi_fitted_log10ratio": -0.016311764705882352,
      "observed_median_log10ratio": -0.0045
    },
    {
      "bin": 10,
      "n": 38,
      "occupancy_mid": 0.9886623509642612,
      "phi_fitted_log10ratio": -0.020689867424242423,
      "observed_median_log10ratio": -0.0367625
    },
    {
      "bin": 11,
      "n": 38,
      "occupancy_mid": 0.9930546981030989,
      "phi_fitted_log10ratio": -0.020689867424242423,
      "observed_median_log10ratio": -0.006225000000000002
    },
    {
      "bin": 12,
      "n": 37,
      "occupancy_mid": 0.9959080789239615,
      "phi_fitted_log10ratio": -0.020689867424242423,
      "observed_median_log10ratio": -0.019975
    },
    {
      "bin": 13,
      "n": 38,
      "occupancy_mid": 0.9977701846229661,
      "phi_fitted_log10ratio": -0.020689867424242423,
      "observed_median_log10ratio": -0.0036
    },
    {
      "bin": 14,
      "n": 38,
      "occupancy_mid": 0.9988129491798712,
      "phi_fitted_log10ratio": -0.020689867424242423,
      "observed_median_log10ratio": -0.006225
    },
    {
      "bin": 15,
      "n": 38,
      "occupancy_mid": 0.9993174165524821,
      "phi_fitted_log10ratio": -0.020689867424242423,
      "observed_median_log10ratio": -0.022350000000000002
    },
    {
      "bin": 16,
      "n": 38,
      "occupancy_mid": 0.9995781616676842,
      "phi_fitted_log10ratio": -0.020689867424242423,
      "observed_median_log10ratio": -0.009125000000000001
    },
    {
      "bin": 17,
      "n": 38,
      "occupancy_mid": 0.9997601298648444,
      "phi_fitted_log10ratio": -0.021291193181818182,
      "observed_median_log10ratio": -0.01625
    },
    {
      "bin": 18,
      "n": 38,
      "occupancy_mid": 0.9998717066094236,
      "phi_fitted_log10ratio": -0.021291193181818182,
      "observed_median_log10ratio": -0.01325
    },
    {
      "bin": 19,
      "n": 38,
      "occupancy_mid": 0.999948539070693,
      "phi_fitted_log10ratio": -0.021291193181818182,
      "observed_median_log10ratio": -0.0083
    },
    {
      "bin": 20,
      "n": 38,
      "occupancy_mid": 0.9999761706279737,
      "phi_fitted_log10ratio": -0.021291193181818182,
      "observed_
```


### `e7b_null_calibration`  (OK)

seed `0`, wall clock `412.43` s, recorded `2026-09-05T03:35:16Z`

| quantity | value |
|---|---|
| `sign_convention` | measured VALUE = log10(siRNA/mock); repression is NEGATIVE, so a working predictor of bound fraction gives a NEGATIVE Spearman |
| `n_bootstrap` | 2000 |
| `n_permutations` | 1000 |
| `min_n_per_class` | 10 |
| `n_constructs_analysed` | 24 |
| `n_cluster_bootstrap` | 2000 |
| `EQUILIBRIUM_ADDS_ESTABLISHED_PREDICTIVE_VALUE` | false |
| `max_abs_net_gap_where_criteria_met` | 3.9934e-04 |
| `rho_where_scorings_differ_most` | 0.1 |
| `net_gap_where_scorings_differ_most` | 0.0026482 |
| `net_gap_sign_where_scorings_differ_most` | independent better |
| `effect_size_note` | the criteria in rho_values_meeting_paired_and_cluster_criteria are the significance criteria alone. They are met only at the large rho values where the limit theorem makes the two scorings converge, so the difference they certify is tiny, and the paired null has almost no spread there, which is w... |
| `paired_test_note` | the raw difference of two pooled Spearman correlations is not a test. The two models have different permutation-null baselines because pooling constructs leaves a between-construct correlation that a within-construct shuffle cannot remove, and that baseline is not the same for the two scorings, s... |
| `bootstrap_scope_note` | two bootstraps are reported and they answer different questions. pair_bootstrap_* resamples transcript-construct pairs and is CONDITIONAL ON THE OBSERVED CONSTRUCTS: it describes sampling noise within this construct panel and must not be used to claim anything about a new guide. cluster_bootstrap... |
| `permutation_null_note` | measured values are permuted WITHIN construct, so the null keeps each construct's response distribution and the pooling structure and destroys only the transcript-level association. An observed correlation inside this envelope is not distinguishable from no association. Note the null is not centr... |


**`rho_values`**: `[0.001, 0.01, 0.1, 0.5, 2.0, 10.0]`


**`class_assignment_rules`**

```json
{
  "best_ddG": "the class of the transcript's lowest-ddG site, which is what e7 used",
  "canonical_strongest": "the strongest class present on the transcript, 8mer > 7mer-m8 > 7mer-A1 > 6mer"
}
```


**`pooled_site_class`**

```json
{
  "best_ddG": {
    "6mer": {
      "n": 19380,
      "median_log10ratio": -0.0034999999999999996,
      "median_ci95": [
        -0.004313125,
        -0.0026500000000000004
      ],
      "mean_log10ratio": -0.008340672084623323
    },
    "7mer-A1": {
      "n": 4465,
      "median_log10ratio": -0.010700000000000001,
      "median_ci95": [
        -0.012049999999999998,
        -0.0093
      ],
      "mean_log10ratio": -0.023751030235162375
    },
    "7mer-m8": {
      "n": 8884,
      "median_log10ratio": -0.0079,
      "median_ci95": [
        -0.009300000000000001,
        -0.00675
      ],
      "mean_log10ratio": -0.01794356990094552
    },
    "8mer": {
      "n": 1947,
      "median_log10ratio": -0.018000000000000002,
      "median_ci95": [
        -0.02105,
        -0.0156
      ],
      "mean_log10ratio": -0.03906765536723164
    },
    "_summary": {
      "assignment_rule": "best_ddG",
      "canonical_order_checked": [
        "8mer",
        "7mer-m8",
        "7mer-A1",
        "6mer"
      ],
      "medians_in_canonical_order": [
        -0.018000000000000002,
        -0.0079,
        -0.010700000000000001,
        -0.0034999999999999996
      ],
      "monotone_in_canonical_order": false,
      "inversion_median_7merm8_minus_7merA1": 0.0028000000000000004,
      "inversion_ci95": [
        0.0008000000000000004,
        0.004699999999999999
      ],
      "inversion_significant_at_95": true,
      "inversion_direction": "7mer-A1 more repressed than 7mer-m8",
      "n_constructs_showing_inversion": 17,
      "n_constructs_tested": 24
    }
  },
  "canonical_strongest": {
    "6mer": {
      "n": 17504,
      "median_log10ratio": -0.00315,
      "median_ci95": [
        -0.0041,
        -0.0024
      ],
      "mean_log10ratio": -0.0070502627970749545
    },
    "7mer-A1": {
      "n": 4860,
      "median_log10ratio": -0.010499999999999999,
      "median_ci95": [
        -0.0119,
        -0.00915
      ],
      "mean_log10ratio": -0.024079022633744857
    },
    "7mer-m8": {
      "n": 9955,
      "median_log10ratio": -0.00745,
      "median_ci95": [
        -0.0086,
        -0.0064
      ],
      "mean_log10ratio": -0.017464753892516324
    },
    "8mer": {
      "n": 2357,
      "median_log10ratio": -0.0172,
      "median_ci95": [
        -0.0196,
        -0.0142
      ],
      "mean_log10ratio": -0.037705770046669494
    },
    "_summary": {
      "assignment_rule": "canonical_strongest",
      "canonical_order_checked": [
        "8mer",
        "7mer-m8",
        "7mer-A1",
        "6mer"
      ],
      "medians_in_canonical_order": [
        -0.0172,
        -0.00745,
        -0.010499999999999999,
        -0.00315
      ],
      "monotone_in_canonical_order": false,
      "inversion_median_7merm8_minus_7merA1": 0.003049999999999999,
      "inversion_ci95": [
        0.0011500000000000017,
        0.004775624999999996
      ],
      "inversion_significant_at_95": true,
      "inversion_direction": "7mer-A1 more repressed than 7mer-m8",
      "n_constructs_showing_inversion": 16,
      "n_constructs_tested": 24
    }
  }
}
```


**`per_construct_site_class`**

| construct | n_no_site | median_no_site | best_ddG.6mer.n | best_ddG.6mer.median | best_ddG.6mer.ci95 | best_ddG.6mer.p_mw_less | best_ddG.7mer-A1.n | best_ddG.7mer-A1.median | best_ddG.7mer-A1.ci95 | best_ddG.7mer-A1.p_mw_less | best_ddG.7mer-m8.n | best_ddG.7mer-m8.median | best_ddG.7mer-m8.ci95 | best_ddG.7mer-m8.p_mw_less | best_ddG.8mer.n | best_ddG.8mer.median | best_ddG.8mer.ci95 | best_ddG.8mer.p_mw_less | best_ddG.inversion_m8_minus_A1 | best_ddG.inversion_ci95 | best_ddG.inverted | canonical_strongest.6mer.n | canonical_strongest.6mer.median | canonical_strongest.6mer.ci95 | canonical_strongest.6mer.p_mw_less | canonical_strongest.7mer-A1.n | canonical_strongest.7mer-A1.median | canonical_strongest.7mer-A1.ci95 | canonical_strongest.7mer-A1.p_mw_less | canonical_strongest.7mer-m8.n | canonical_strongest.7mer-m8.median | canonical_strongest.7mer-m8.ci95 | canonical_strongest.7mer-m8.p_mw_less | canonical_strongest.8mer.n | canonical_strongest.8mer.median | canonical_strongest.8mer.ci95 | canonical_strongest.8mer.p_mw_less | canonical_strongest.inversion_m8_minus_A1 | canonical_strongest.inversion_ci95 | canonical_strongest.inverted |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MAPK14-193_parent | 10320 | 0.0012 | 573 | -0.0028 | [-0.006218125, 0.0006749999999999985] | 1.9405e-04 | 81 | -0.0229 | [-0.0336, -0.0069] | 2.9437e-05 | 267 | -0.01045 | [-0.016900000000000002, -0.0057] | 3.6112e-07 | 28 | -0.013775 | [-0.0557, 0.0166] | 0.0215038 | 0.01245 | [-0.007805000000000001, 0.024012499999999992] | true | 551 | -0.00295 | [-0.006363125, 0.0006999999999999992] | 4.0418e-04 | 88 | -0.02065 | [-0.033665625, -0.0016643750000000204] | 1.3489e-05 | 280 | -0.00995 | [-0.01745, -0.005750000000000002] | 2.0089e-07 | 30 | -0.013775 | [-0.0495, 0.019675] | 0.0329358 | 0.0107 | [-0.009065625, 0.024464999999999987] | true |
| MAPK14-193_pos01mut | 10338 | 0.0025 | 571 | -0.006375 | [-0.0105, -0.002747500000000002] | 8.4515e-06 | 84 | -0.0119875 | [-0.03250375, -0.0034837500000000385] | 1.0201e-04 | 267 | -0.0073 | [-0.0142, 0.00145] | 2.3344e-05 | 28 | -0.00645 | [-0.0659, 0.013975] | 0.0349951 | 0.0046875 | [-0.005454999999999999, 0.02591624999999998] | true | 552 | -0.006225 | [-0.00955125, -0.001975] | 2.6889e-05 | 88 | -0.011975 | [-0.034323125, -0.002700000000000001] | 7.2432e-05 | 280 | -0.0076 | [-0.0159, -0.0007212500000000034] | 6.0730e-06 | 30 | -0.00645 | [-0.061225, 0.015093749999999984] | 0.0433356 | 0.004375 | [-0.007538124999999998, 0.025191874999999996] | true |
| MAPK14-193_pos02mut | 10522 | -9.7500e-04 | 315 | -0.00935 | [-0.01901, -0.0027] | 2.2996e-04 | 108 | -0.01705 | [-0.038875, -0.005535625000000024] | 5.0827e-05 | 236 | -0.0119875 | [-0.0201, -0.003125] | 8.6124e-06 | 84 | -0.026475 | [-0.040600000000000004, -0.0070112500000000366] | 1.8795e-06 | 0.0050625 | [-0.010489374999999997, 0.029913125] | true | 302 | -0.00935 | [-0.0192384375, -0.0017237500000000013] | 0.00106501 | 111 | -0.0191 | [-0.042249999999999996, -0.0078] | 3.3792e-06 | 242 | -0.0119875 | [-0.020218125, -0.0035737500000000014] | 4.4852e-06 | 88 | -0.023875 | [-0.039525000000000005, -0.0037875] | 5.7268e-06 | 0.0071125 | [-0.006301875, 0.0330140625] | true |
| MAPK14-193_pos03mut | 10569 | 0.00635 | 438 | -0.0016 | [-0.00623375, 0.003428749999999997] | 0.00147047 | 86 | -0.025675 | [-0.0408, -0.010499999999999999] | 2.8833e-07 | 163 | 0.0076 | [-0.0011999999999999997, 0.0147] | 0.192779 | 31 | -0.0492 | [-0.0765, -0.016] | 5.3847e-05 | 0.033275 | [0.014758125, 0.04826999999999998] | true | 430 | -0.00105 | [-0.004875000000000001, 0.00425] | 0.00370114 | 90 | -0.02845 | [-0.05005, -0.010786875000000001] | 3.3456e-08 | 165 | 0.0076 | [-0.001514999999999999, 0.014628749999999996] | 0.187374 | 33 | -0.0492 | [-0.0765, -0.0109] | 2.6961e-05 | 0.03605 | [0.017430625, 0.058581249999999994] | true |
| MAPK14-193_pos04mut | 6361 | 0.005 | 2667 | 0.0027 | [0.0001425000000000004, 0.005152499999999997] | 0.00446309 | 535 | -0.0061 | [-0.013999999999999999, -0.0001] | 1.6036e-11 | 1432 | -0.0033 | [-0.006213125, -0.0005618750000000006] | 2.0111e-15 | 269 | -0.0167 | [-0.02555, -0.0106] | 1.2756e-14 | 0.0028 | [-0.0043862499999999995, 0.011152499999999997] | true | 2086 | 0.00415 | [0.0016, 0.006501249999999998] | 0.292554 | 676 | -0.0042 | [-0.00987625, 0.0001656249999999968] | 9.6354e-12 | 1749 | -0.0023 | [-0.0054525, 0.0003] | 6.1721e-16 | 392 | -0.016675 | [-0.0227025, -0.01145] | 2.2500e-20 | 0.0019 | [-0.0036024999999999994, 0.009054999999999994] | true |
| MAPK14-193_pos05mut | 7312 | 0.00305 | 1843 | -0.0015 | [-0.0048000000000000004, 0.0011787499999999969] | 1.6404e-08 | 407 | -0.01115 | [-0.0196, -0.0049499999999999995] | 7.8385e-11 | 1335 | -0.00405 | [-0.006575000000000001, -2.3750000000000994e-05] | 4.4183e-06 | 224 | -0.010675 | [-0.0182, -0.0022500000000000007] | 3.7433e-05 | 0.0071 | [0.00057375, 0.01645] | true | 1489 | -0.002775 | [-0.005704999999999999, 0.0004024999999999975] | 3.1408e-08 | 453 | -0.0109 | [-0.017499999999999998, -0.005649999999999999] | 1.8797e-11 | 1574 | -0.0018 | [-0.004744062500000001, 0.0015156249999999961] | 3.3490e-05 | 293 | -0.01095 | [-0.0183, -0.0030450000000000043] | 3.7869e-07 | 0.0091 | [0.0016671874999999998, 0.01555] | true |
| MAPK14-193_pos06mut | 10688 | -0.0012 | 367 | -0.0078 | [-0.0138, -0.0047] | 8.9543e-08 | 109 | -0.02785 | [-0.04170375, -0.013242500000000053] | 1.4124e-11 | 79 | -0.0102 | [-0.0264, -0.0038] | 4.0760e-04 | 26 | -0.034375 | [-0.0616, -0.020181875000000026] | 5.3275e-07 | 0.01765 | [-0.003773749999999998, 0.030719999999999983] | true | 363 | -0.008 | [-0.01415, -0.004999999999999999] | 2.9885e-08 | 110 | -0.0277 | [-0.039396875, -0.011] | 2.2785e-11 | 82 | -0.0082 | [-0.024541249999999997, -0.002190000000000009] | 0.00149189 | 26 | -0.034375 | [-0.0694, -0.0188] | 5.3275e-07 | 0.0195 | [-0.0014387499999999995, 0.032724374999999965] | true |
| MAPK14-193_pos07mut | 10548 | 7.0000e-04 | 599 | -0.0081 | [-0.0186, -0.0022500000000000003] | 3.5456e-05 | 85 | -0.0076 | [-0.0356, 0.02525] | 0.23096 | 62 | 1.0000e-04 | [-0.017374999999999998, 0.013] | 0.361284 | null | null | null | null | 0.0077 | [-0.027464999999999996, 0.037063749999999965] | true | 589 | -0.0081 | [-0.0171, -0.0024] | 5.6554e-05 | 90 | -0.00765 | [-0.033689375, 0.016425000000000002] | 0.15134 | 66 | 0.0016 | [-0.0143, 0.016988749999999987] | 0.414128 | null | null | null | null | 0.00925 | [-0.01923625, 0.03791687499999997] | true |
| MAPK14-193_pos08mut | 10347 | 8.0000e-04 | 693 | -0.0064 | [-0.0103, -0.00185] | 1.1621e-05 | 82 | -0.0135 | [-0.0415, -0.0005] | 0.00109374 | 147 | -0.0144 | [-0.025750000000000002, -0.0067] | 6.0754e-06 | 29 | -0.0139 | [-0.0318, -0.0051] | 0.0102022 | -9.0000e-04 | [-0.020305, 0.028186249999999993] | false | 681 | -0.0064 | [-0.010352499999999999, -0.00185] | 1.8803e-05 | 86 | -0.0135 | [-0.042707499999999995, -0.00011625000000000792] | 5.9596e-04 | 152 | -0.01435 | [-0.025750000000000002, -0.006187500000000012] | 1.2283e-05 | 32 | -0.0155 | [-0.0528, -0.0037662500000000083] | 0.00362079 | -8.5000e-04 | [-0.020188125, 0.035238124999999995] | false |
| MAPK14-193_pos09mut | 10343 | 4.0000e-04 | 574 | -0.0072 | [-0.0121, -0.0006950000000000045] | 9.6324e-04 | 83 | -0.01715 | [-0.0475, -0.0024] | 0.0013587 | 267 | -0.0103 | [-0.0227, 0.0028974999999999565] | 0.00327513 | 27 | -0.056 | [-0.16579999999999998, 0.0133] | 0.00300596 | 0.00685 | [-0.0133, 0.04030999999999999] | true | 552 | -0.0075 | [-0.01207625, -0.0005475000000000023] | 8.8704e-04 | 88 | -0.0172 | [-0.047799999999999995, 0.0008] | 0.00119825 | 281 | -0.0098 | [-0.0218, 0.0012] | 0.00361836 | 30 | -0.0284 | [-0.1422, 0.012516249999999963] | 0.0071103 | 0.0074 | [-0.0119225, 0.040676250000000004] | true |
| MAPK14-193_pos10mut | 10343 | 0.0042 | 573 | -0.0035 | [-0.0089, -0.0004] | 8.1101e-06 | 82 | -0.02025 | [-0.0387, 0.00023624999999998975] | 7.5559e-04 | 267 | -0.0112 | [-0.0201, -0.0012000000000000005] | 1.5433e-06 | 28 | -0.034175 | [-0.07381999999999998, 0.004984374999999935] | 0.0014269 | 0.00905 | [-0.016304999999999997, 0.02797625] | true | 552 | -0.0035 | [-0.00853125, 0.00017624999999999886] | 1.2258e-05 | 88 | -0.0182 | [-0.03745, 0.0029762499999999533] | 8.2174e-04 | 280 | -0.01185 | [-0.01975, -0.0013900000000000093] | 6.1556e-07 | 30 | -0.020025 | [-0.07255, 0.00835] | 0.00475645 | 0.00635 | [-0.016678749999999996, 0.027080624999999987] | true |
| MAPK14-193_pos11mut | 10336 | 0.0028 | 574 | -0.00655 | [-0.010639375, -0.00019999999999999998] | 4.3474e-04 | 80 | -0.01595 | [-0.0325, 0.0051] | 0.00180922 | 269 | -0.0064 | [-0.0163, 0.0027] | 6.2778e-04 | 27 | -0.01985 | [-0.0645, 0.011949999999999999] | 0.0208764 | 0.00955 | [-0.012052499999999999, 0.027850000000000003] | true | 551 | -0.0067 | [-0.0103575, -0.0001] | 7.6517e-04 | 88 | -0.01595 | [-0.031675, 0.0040787499999999964] | 6.1996e-04 | 281 | -0.0071 | [-0.0163, 0.0027] | 3.0441e-04 | 30 | -0.007775 | [-0.05945, 0.014475] | 0.0924889 | 0.00885 | [-0.010428749999999999, 0.027940625] | true |
| MAPK14-193_pos12mut | 10335 | -0.004825 | 574 | -0.010575 | [-0.0131, -0.0051106250000000015] | 0.00374004 | 81 | -0.0133 | [-0.041777499999999995, 0.0003] | 0.00116446 | 266 | -0.020225 | [-0.0291, -0.009636875] | 1.0570e-06 | 28 | -0.0385 | [-0.08807749999999999, -0.009750000000000002] | 6.3200e-04 | -0.006925 | [-0.022402500000000002, 0.02214874999999998] | false | 551 | -0.0099 | [-0.0131, -0.004632500000000016] | 0.0115806 | 88 | -0.0133 | [-0.0404925, 0.00035] | 5.8847e-04 | 280 | -0.021275 | [-0.0291, -0.0114] | 1.4301e-07 | 30 | -0.02965 | [-0.075775, -0.009750000000000002] | 0.00135116 | -0.007975 | [-0.023705625, 0.023814375] | false |
| MAPK14-193_pos13mut | 10325 | 0.0034 | 568 | -0.00625 | [-0.010605, -0.002025] | 2.5577e-06 | 83 | -0.0135 | [-0.0308, 0.0026] | 1.4689e-04 | 269 | -0.009 | [-0.0184, 0.0019] | 3.9833e-05 | 28 | -0.02535 | [-0.0757, -0.0136] | 0.00486944 | 0.0045 | [-0.0113575, 0.025533749999999994] | true | 550 | -0.00615 | [-0.0105025, -0.0015999999999999999] | 9.0223e-06 | 88 | -0.01105 | [-0.0346975, -0.002868750000000006] | 3.8480e-05 | 280 | -0.00815 | [-0.018355625, -0.0013] | 1.7665e-05 | 30 | -0.02325 | [-0.070025, -0.0011999999999999997] | 0.00728648 | 0.0029 | [-0.0103525, 0.02424624999999998] | true |
| MAPK14-193_pos14mut | 10327 | 0.0088 | 572 | -0.00645 | [-0.0174, 0.0005500000000000017] | 3.1790e-05 | 80 | -0.00815 | [-0.027500000000000004, 0.008551874999999987] | 0.0164254 | 269 | -0.0044 | [-0.024, 0.007599999999999999] | 0.0253639 | 27 | -0.04875 | [-0.1301, 0.02075] | 0.0110965 | 0.00375 | [-0.02155, 0.02453624999999999] | true | 550 | -0.00685 | [-0.018705, 0.00044999999999999966] | 4.3799e-05 | 88 | -0.00965 | [-0.031363749999999996, 0.007424999999999999] | 0.00464324 | 280 | -0.00485 | [-0.02345, 0.007174999999999999] | 0.0197841 | 30 | -0.03225 | [-0.12165000000000001, 0.034249999999999996] | 0.0735098 | 0.0048 | [-0.01925375, 0.025806874999999983] | true |
| MAPK14-193_pos15mut | 10311 | 0.00205 | 569 | -0.0054 | [-0.010405, 0.00015249999999999774] | 5.1625e-04 | 85 | -0.0104 | [-0.02945, 0.0061] | 0.00918918 | 268 | -0.01275 | [-0.022, -0.004680000000000018] | 2.2452e-07 | 27 | -0.0265 | [-0.0889, 0.0012] | 0.00280244 | -0.00235 | [-0.0213125, 0.019504999999999995] | false | 551 | -0.0047 | [-0.0103, 0.0014] | 0.00107211 | 88 | -0.01135 | [-0.029949999999999997, 0.00405] | 0.00206121 | 280 | -0.01275 | [-0.022315625000000002, -0.00425] | 1.1679e-07 | 30 | -0.01615 | [-0.0786, 0.01268624999999999] | 0.0166461 | -0.0014 | [-0.019014999999999997, 0.018438749999999986] | false |
| MAPK14-193_pos16mut | 10325 | 0.002 | 567 | -0.001 | [-0.00527625, 0.003867499999999984] | 0.131692 | 84 | -0.011 | [-0.0188, 0.007474999999999999] | 0.089943 | 268 | -0.00705 | [-0.01532625, 0.00019562499999999216] | 6.7993e-04 | 29 | -0.0057 | [-0.0333, 0.0276] | 0.171712 | 0.00395 | [-0.017263125, 0.012126249999999998] | true | 550 | 3.5000e-04 | [-0.0053, 0.005876249999999999] | 0.206486 | 88 | -0.01265 | [-0.02105, 0.00415] | 0.0276162 | 280 | -0.0063 | [-0.015074999999999998, -0.0011475000000000023] | 6.7898e-04 | 30 | -0.011625 | [-0.032025, 0.0214] | 0.144096 | 0.00635 | [-0.012773125, 0.017293749999999983] | true |
| MAPK14-193_pos17mut | 10320 | 0.0015 | 571 | -1.5000e-04 | [-0.0052, 0.0043] | 0.00944256 | 84 | -0.0032 | [-0.01852875, 0.004667499999999983] | 0.0179736 | 267 | -0.00885 | [-0.0163675, -0.0022] | 2.3211e-05 | 27 | -0.0438 | [-0.05685, 0.00995] | 0.00737964 | -0.00565 | [-0.015950000000000002, 0.008988749999999988] | false | 551 | -1.0000e-04 | [-0.0041, 0.0029] | 0.0118601 | 88 | -0.004675 | [-0.0191525, 0.0031] | 0.00720738 | 280 | -0.0085 | [-0.01667625, -0.002866250000000008] | 2.1915e-05 | 30 | -0.02865 | [-0.053075, 0.017125] | 0.0315547 | -0.003825 | [-0.013726249999999999, 0.011759999999999991] | false |
| MAPK14-193_pos18mut | 10340 | 3.0000e-04 | 574 | -0.0065 | [-0.01185, -0.0026] | 8.5951e-04 | 82 | -0.02295 | [-0.042050000000000004, -0.0051] | 0.00389093 | 265 | -0.0131 | [-0.0242, -0.0046500000000000005] | 4.4619e-05 | 28 | -0.01625 | [-0.06205, -0.0016500000000000013] | 0.0262783 | 0.00985 | [-0.013119999999999998, 0.02832625] | true | 551 | -0.0066 | [-0.012905, -0.0025] | 0.00104831 | 88 | -0.02295 | [-0.042050000000000004, -0.0016950000000000049] | 0.00174549 | 280 | -0.01285 | [-0.023399999999999997, -0.004673750000000002] | 4.8374e-05 | 30 | -0.0133 | [-0.047950000000000007, 0.005898749999999977] | 0.0608709 | 0.0101 | [-0.012512499999999998, 0.030204999999999996] | true |
| MAPK14-193_pos19mut | 10343 | -0.002375 | 576 | -0.0075 | [-0.0115, -0.003648750000000002] | 1.9615e-04 | 81 | -0.0158 | [-0.0241575, -0.005737500000000102] | 0.00116975 | 265 | -0.0118 | [-0.0188, -0.0055] | 1.2740e-07 | 27 | -0.0181 | [-0.09865, 0.00455] | 0.00391143 | 0.004 | [-0.00927625, 0.0145] | true | 551 | -0.0068 | [-0.0106, -0.0035] | 6.4872e-04 | 88 | -0.014775 | [-0.021875000000000002, -0.006667500000000029] | 9.5819e-04 | 280 | -0.0126 | [-0.02022875, -0.005906875000000005] | 2.3486e-08 | 30 | -0.01615 | [-0.0797, -0.0013737500000000008] | 0.00438344 | 0.002175 | [-0.010807499999999998, 0.011169374999999994] | true |
| PIK3CB-6338_parent | 7677 | -0.0018 | 2028 | -0.00365 | [-0.0053750000000000004, -0.0016950000000000044] | 0.00200589 | 485 | -0.0089 | [-0.0119, -0.005647500000000002] | 1.0601e-06 | 656 | -0.011275 | [-0.0162, -0.008172500000000003] | 2.8440e-10 | 231 | -0.01645 | [-0.0257, -0.0092] | 1.4500e-11 | -0.002375 | [-0.008190625, 0.002402499999999997] | false | 1790 | -0.002625 | [-0.0046, -0.0007212500000000034] | 0.0786248 | 548 | -0.0084 | [-0.011888125000000001, -0.006] | 2.0212e-07 | 787 | -0.011 | [-0.015250000000000001, -0.0085] | 3.4584e-13 | 275 | -0.0164 | [-0.0219, -0.0102] | 4.4477e-13 | -0.0026 | [-0.008, 0.0019893749999999972] | false |
| PIK3CB-6340_parent | 8485 | 0.0038 | 1172 | -0.003525 | [-0.00642625, -0.0012] | 4.4224e-16 | 532 | -0.01005 | [-0.0133, -0.004009375000000003] | 1.6448e-20 | 655 | -0.0098 | [-0.0141525, -0.0063475000000000024] | 4.1281e-22 | 279 | -0.01855 | [-0.0269575, -0.0155] | 4.2887e-25 | 2.5000e-04 | [-0.006982499999999999, 0.004876249999999998] | true | 984 | -0.00245 | [-0.0048762499999999995, 0.0003131249999999993] | 2.1345e-09 | 523 | -0.0101 | [-0.0132, -0.00435] | 5.1201e-19 | 777 | -0.01115 | [-0.0151, -0.006918750000000005] | 3.5415e-29 | 354 | -0.0181 | [-0.025275, -0.011983125000000004] | 2.6846e-29 | -0.00105 | [-0.0084525, 0.0040999999999999995] | false |
| PLK1-319_parent | 7986 | 5.0000e-04 | 1589 | -0.0012 | [-0.0037, 0.002152499999999998] | 0.0817877 | 627 | -0.0065 | [-0.0108, -0.002] | 1.0657e-06 | 545 | -0.0137 | [-0.019104999999999997, -0.0068425000000000066] | 6.7838e-13 | 380 | -0.01445 | [-0.022640625, -0.009335624999999998] | 3.3252e-11 | -0.0072 | [-0.014131249999999998, 0.00035000000000000135] | false | 1400 | -0.0011 | [-0.0037, 0.0022000000000000006] | 0.20815 | 690 | -0.00685 | [-0.0108, -0.002095000000000005] | 5.9101e-07 | 613 | -0.0112 | [-0.0168525, -0.0053375000000000115] | 1.1023e-11 | 438 | -0.0129 | [-0.020791874999999998, -0.008147500000000002] | 3.4469e-12 | -0.00435 | [-0.011924999999999998, 0.0028262499999999976] | false |
| PLK1-772_parent | 10374 | -0.0043 | 233 | -0.0153 | [-0.0242, -0.0043] | 0.0051391 | 339 | -0.0105 | [-0.021477499999999997, -0.001899999999999999] | 0.00299258 | 100 | -0.018325 | [-0.030074999999999998, -0.0043687500000000054] | 0.00980621 | 29 | -0.034 | [-0.0632, 0.0045] | 0.029334 | -0.007825 | [-0.02293375, 0.010040624999999977] | false | 227 | -0.0152 | [-0.02405, -0.00534500000000005] | 0.00758889 | 339 | -0.0105 | [-0.0209, -0.0006862500000000355] | 0.00427062 | 106 | -0.0218 | [-0.03780375, -0.0078] | 0.00312134 | 29 | -0.034 | [-0.0632, 0.0045] | 0.029334 | -0.0113 | [-0.027088124999999998, 0.0061337499999999925] | false |


**`pooled_spearman_with_null_and_ci`**

| rho | n_pairs_pooled | n_constructs | pooled_spearman_equilibrium | rank_pearson_identity_abs_err_equilibrium | pair_bootstrap_ci95_equilibrium_CONDITIONAL | pair_bootstrap_sd_equilibrium_CONDITIONAL | pooled_spearman_independent | rank_pearson_identity_abs_err_independent | pair_bootstrap_ci95_independent_CONDITIONAL | pair_bootstrap_sd_independent_CONDITIONAL | permutation_null_ci95_equilibrium | permutation_null_mean_equilibrium | permutation_null_sd_equilibrium | observed_outside_null_envelope_equilibrium | permutation_p_two_sided_about_null_mean_equilibrium | z_vs_permutation_null_equilibrium | null_centred_association_equilibrium | permutation_null_ci95_independent | permutation_null_mean_independent | permutation_null_sd_independent | observed_outside_null_envelope_independent | permutation_p_two_sided_about_null_mean_independent | z_vs_permutation_null_independent | null_centred_association_independent | equilibrium_minus_independent | paired_permutation_null_mean_gap | paired_permutation_null_sd_gap | paired_permutation_null_ci95_gap | observed_gap_minus_paired_null_mean | paired_permutation_p_two_sided_about_null_mean | paired_z_vs_permutation_null | paired_observed_outside_null_envelope | null_centred_difference | cluster_bootstrap_ci95_equilibrium | cluster_bootstrap_sd_equilibrium | cluster_bootstrap_ci95_independent | cluster_bootstrap_sd_independent | cluster_bootstrap_ci95_gap | cluster_bootstrap_median_gap | cluster_bootstrap_gap_excludes_zero | cluster_bootstrap_n_resamples | paired_net_gap | cluster_se_equilibrium_association | paired_net_gap_over_cluster_se | paired_and_cluster_criteria_met | improvement_exceeds_one_cluster_se |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.001 | 34676 | 24 | -0.061921 | 6.9389e-18 | [-0.07248720408798655, -0.05149160840516576] | 0.00538988 | -0.0529612 | 0 | [-0.06335903237643545, -0.042977599982646775] | 0.00522518 | [-0.018349876574116925, 0.0010426413131099533] | -0.00846943 | 0.00507515 | true | 9.9900e-04 | -10.532 | -0.0534516 | [-0.006564912469124138, 0.013541911497452267] | 0.00343308 | 0.00521362 | true | 9.9900e-04 | -10.8167 | -0.0563943 | -0.00895978 | -0.0119025 | 0.00103415 | [-0.01382479933799195, -0.009876790388438654] | 0.00294273 | 0.00699301 | 2.84554 | true | 0.00294273 | [-0.08156450411345981, -0.039154081555603036] | 0.0108259 | [-0.07644162254504719, -0.030576782499485086] | 0.0116134 | [-0.0187002163282459, 0.0043548220693466] | -0.00812951 | false | 2000 | 0.00294273 | 0.0108259 | 0.271822 | false | false |
| 0.01 | 34676 | 24 | -0.071026 | 1.3878e-17 | [-0.08161538952758016, -0.060482197751284085] | 0.00547675 | -0.0529612 | 6.9389e-18 | [-0.06319836775545128, -0.042751305475642244] | 0.00535553 | [-0.025988869695043403, -0.006258257500441114] | -0.0162752 | 0.00488427 | true | 9.9900e-04 | -11.2096 | -0.0547508 | [-0.006156726223120538, 0.014191018905572388] | 0.00369672 | 0.00505283 | true | 9.9900e-04 | -11.2131 | -0.0566579 | -0.0180649 | -0.019972 | 0.0010235 | [-0.021949844109367275, -0.018073814646402873] | 0.0019071 | 0.0619381 | 1.86332 | true | 0.0019071 | [-0.09044224992614101, -0.04582670378253433] | 0.011818 | [-0.07624306238403511, -0.02970815330497168] | 0.0120241 | [-0.029186771445416836, -0.0017679016386776196] | -0.016175 | true | 2000 | 0.0019071 | 0.011818 | 0.161372 | false | false |
| 0.1 | 34676 | 24 | -0.0745539 | 0 | [-0.08540073256601807, -0.06433748253561616] | 0.00530569 | -0.0529612 | 1.3878e-17 | [-0.06343398124012056, -0.04241303279574673] | 0.00543604 | [-0.030259053207475625, -0.011723075260683575] | -0.0205105 | 0.00482309 | true | 9.9900e-04 | -11.2051 | -0.0540434 | [-0.006945618801808525, 0.013141115856784713] | 0.00373035 | 0.00522275 | true | 9.9900e-04 | -10.8547 | -0.0566916 | -0.0215926 | -0.0242408 | 0.00103751 | [-0.026394059972165325, -0.022297863035385897] | 0.0026482 | 0.00999001 | 2.55245 | true | 0.0026482 | [-0.09379489489731742, -0.04724217121355254] | 0.0122352 | [-0.0757103761410142, -0.030907556714455796] | 0.0116364 | [-0.03373757935095039, -0.0050526811388451436] | -0.0205055 | true | 2000 | 0.0026482 | 0.0122352 | 0.21644 | false | false |
| 0.5 | 34676 | 24 | -0.0559441 | 6.9389e-18 | [-0.0662499578176872, -0.04501362264862658] | 0.00540546 | -0.0529612 | 6.9389e-18 | [-0.06315457040445178, -0.04242791625355981] | 0.00532641 | [-0.008931675798037634, 0.011269306331732181] | 9.8527e-04 | 0.00511102 | true | 9.9900e-04 | -11.1386 | -0.0569294 | [-0.006335006232607781, 0.013730095327385691] | 0.00356884 | 0.00510035 | true | 9.9900e-04 | -11.0836 | -0.05653 | -0.00298291 | -0.00258357 | 1.0932e-04 | [-0.002798365348451208, -0.0023739457340118705] | -3.9934e-04 | 0.001998 | -3.65289 | true | -3.9934e-04 | [-0.07827968920570566, -0.03348239346678697] | 0.0116545 | [-0.07696915130085569, -0.031035794473330307] | 0.0118606 | [-0.004992642680393155, -0.000556907494438758] | -0.00280478 | true | 2000 | -3.9934e-04 | 0.0116545 | -0.0342646 | true | false |
| 2 | 34676 | 24 | -0.0535443 | 6.9389e-18 | [-0.06414010716665453, -0.04306553831216124] | 0.00547316 | -0.0529612 | 0 | [-0.06320187670899009, -0.042272964389656414] | 0.00538871 | [-0.00617432937430332, 0.012853212696792344] | 0.00347074 | 0.00494997 | true | 9.9900e-04 | -11.5183 | -0.057015 | [-0.0056616736665932536, 0.013356364196267116] | 0.00397406 | 0.00494704 | true | 9.9900e-04 | -11.5089 | -0.0569352 | -5.8313e-04 | -5.0332e-04 | 2.0641e-05 | [-0.0005459737078648272, -0.0004641439560139955] | -7.9806e-05 | 9.9900e-04 | -3.86639 | true | -7.9806e-05 | [-0.07742277699909364, -0.03157213401388673] | 0.0117226 | [-0.07713451841723688, -0.031152544963358737] | 0.0117714 | [-0.0009423122270378797, -0.00012061432913147504] | -5.5461e-04 | true | 2000 | -7.9806e-05 | 0.0117226 | -0.00680786 | true | false |
| 10 | 34676 | 24 | -0.053075 | 0 | [-0.06349753996075552, -0.04200362157157546] | 0.00547989 | -0.0529612 | 6.9389e-18 | [-0.06346401320918928, -0.04254736962550978] | 0.00536641 | [-0.006428285208330996, 0.013942255397022155] | 0.00362209 | 0.00523297 | true | 9.9900e-04 | -10.8346 | -0.0566971 | [-0.0063292090532817945, 0.014037386881807697] | 0.00371987 | 0.00523277 | true | 9.9900e-04 | -10.832 | -0.0566811 | -1.1383e-04 | -9.7784e-05 | 4.9788e-06 | [-0.00010712777744676439, -8.774256555729915e-05] | -1.6049e-05 | 0.001998 | -3.2234 | true | -1.6049e-05 | [-0.07630890486978116, -0.03153548909990483] | 0.0117295 | [-0.07627040261361355, -0.03141284179494365] | 0.0117409 | [-0.00018885046518943172, -2.046277133182402e-05] | -1.0494e-04 | true | 2000 | -1.6049e-05 | 0.0117295 | -0.00136824 | true | false |


**`pooled_pair_dependence_diagnostic`**

```json
{
  "n_pairs": 34676,
  "n_distinct_genes": 8068,
  "mean_constructs_per_gene": 4.297967278135845,
  "max_constructs_per_gene": 23,
  "frac_pairs_whose_gene_appears_more_than_once": 0.9338447341100473,
  "note": "pooled pairs are clustered twice over: by construct, and by gene, because one gene is measured under many constructs. The pair-level bootstrap ignores both. The construct-cluster bootstrap resamples whole constructs and so respects the construct clustering and carries each gene's repeated appearances together with the construct that produced them; it does not remove the residual gene-level dependence ACROSS distinct constructs, which would need a crossed random-effects model that 24 constructs cannot support."
}
```


**`rho_values_meeting_paired_and_cluster_criteria`**: `[0.5, 2.0, 10.0]`


**`rho_values_where_improvement_exceeds_one_cluster_se`**: `[]`


### `e4_retrieval_invariance`  (OK)

seed `0`, wall clock `18.6872` s, recorded `2026-09-04T19:44:22Z`

| quantity | value |
|---|---|
| `construct` | MAPK14-193_parent |
| `reference_set_size_including_on_target` | 952 |
| `gencode_release` | 50 |
| `on_target_dg_kcal` | -34.9 |
| `on_target_kd_molecules_per_cell` | 36.1328 |
| `total_mrna_molecules_per_cell` | 80000 |
| `max_rel_err_o_target_affinity_rule` | 0.910842 |
| `max_rel_err_o_target_abundance_rule` | 0.818562 |
| `mean_rel_err_o_target_affinity_rule` | 0.235846 |
| `mean_rel_err_o_target_abundance_rule` | 0.480094 |
| `assumption_diagnostic` | The linear background (1+beta)f replaces X_bg f/(K_bg+f) and is valid only where K_bg >> f. frac_omitted_with_K_below_f measures directly how often that fails at each truncation depth. The affinity-weighted rule cannot rescue a truncation that removed transcripts whose K is comparable to or below... |
| `n_rows_where_linearisation_holds` | 4 |
| `n_truncated_rows` | 30 |
| `K_calibrated_log10_min` | -6.95617 |
| `K_calibrated_log10_max` | 13.3213 |


**`rho_values`**: `[0.01, 0.5, 10.0]`


**`R_values`**: `[25, 50, 100, 200, 500, 1000, 2000, 5000]`


**`table`**

| rho | R | rule | f | o_target | total_load | rel_err_o_target | rel_err_total_load | converged |
|---|---|---|---|---|---|---|---|---|
| 0.01 | 952 | full reference | 0.12248 | 0.0974126 | 799.878 | 0 | 0 | true |
| 0.01 | 25 | affinity_weighted_x_over_K | 0.0291807 | 0.0232684 | 799.971 | 0.761136 | 1.1664e-04 | true |
| 0.01 | 50 | affinity_weighted_x_over_K | 0.0758805 | 0.0604282 | 799.924 | 0.379668 | 5.8258e-05 | true |
| 0.01 | 100 | affinity_weighted_x_over_K | 0.112104 | 0.0891858 | 799.888 | 0.0844531 | 1.2972e-05 | true |
| 0.01 | 200 | affinity_weighted_x_over_K | 0.122137 | 0.0971407 | 799.878 | 0.00279169 | 4.2892e-07 | true |
| 0.01 | 500 | affinity_weighted_x_over_K | 0.12248 | 0.0974126 | 799.878 | 2.0662e-07 | 3.1746e-11 | true |
| 0.01 | 25 | abundance_mass_x | 0.0632699 | 0.0504032 | 799.937 | 0.482581 | 7.4024e-05 | true |
| 0.01 | 50 | abundance_mass_x | 0.0450889 | 0.0359376 | 799.955 | 0.631079 | 9.6753e-05 | true |
| 0.01 | 100 | abundance_mass_x | 0.0415404 | 0.0331125 | 799.958 | 0.66008 | 1.0119e-04 | true |
| 0.01 | 200 | abundance_mass_x | 0.0464324 | 0.0370069 | 799.954 | 0.620101 | 9.5074e-05 | true |
| 0.01 | 500 | abundance_mass_x | 0.0697888 | 0.0555863 | 799.93 | 0.429373 | 6.5874e-05 | true |
| 0.5 | 952 | full reference | 35350.8 | 28.8057 | 4649.15 | 0 | 0 | true |
| 0.5 | 25 | affinity_weighted_x_over_K | 3.53293 | 2.56827 | 39996.5 | 0.910842 | 7.60296 | true |
| 0.5 | 50 | affinity_weighted_x_over_K | 18.8149 | 9.87357 | 39981.2 | 0.657236 | 7.59967 | true |
| 0.5 | 100 | affinity_weighted_x_over_K | 99.06 | 21.1284 | 39900.9 | 0.26652 | 7.58241 | true |
| 0.5 | 200 | affinity_weighted_x_over_K | 981.673 | 27.8115 | 39018.3 | 0.0345149 | 7.39257 | true |
| 0.5 | 500 | affinity_weighted_x_over_K | 28777.4 | 28.799 | 11222.6 | 2.3319e-04 | 1.41391 | true |
| 0.5 | 25 | abundance_mass_x | 7.99901 | 5.22645 | 39992 | 0.818562 | 7.602 | true |
| 0.5 | 50 | abundance_mass_x | 8.75812 | 5.62567 | 39991.2 | 0.804703 | 7.60184 | true |
| 0.5 | 100 | abundance_mass_x | 9.61282 | 6.05931 | 39990.4 | 0.789649 | 7.60165 | true |
| 0.5 | 200 | abundance_mass_x | 12.4684 | 7.39751 | 39987.5 | 0.743193 | 7.60104 | true |
| 0.5 | 500 | abundance_mass_x | 30.3742 | 13.1692 | 39969.6 | 0.542827 | 7.59719 | true |
| 10 | 952 | full reference | 794749 | 28.8339 | 5250.72 | 0 | 0 | true |
| 10 | 25 | affinity_weighted_x_over_K | 71.512 | 19.1561 | 799928 | 0.335637 | 151.346 | true |
| 10 | 50 | affinity_weighted_x_over_K | 385.3 | 26.3629 | 799615 | 0.0856966 | 151.287 | true |
| 10 | 100 | affinity_weighted_x_over_K | 2050.83 | 28.3359 | 797949 | 0.0172689 | 150.969 | true |
| 10 | 200 | affinity_weighted_x_over_K | 20795.9 | 28.7852 | 779204 | 0.0016891 | 147.399 | true |
| 10 | 500 | affinity_weighted_x_over_K | 637410 | 28.8335 | 162590 | 1.1222e-05 | 29.9652 | true |
| 10 | 25 | abundance_mass_x | 161.923 | 23.5745 | 799838 | 0.1824 | 151.329 | true |
| 10 | 50 | abundance_mass_x | 179.294 | 23.9987 | 799821 | 0.167689 | 151.326 | true |
| 10 | 100 | abundance_mass_x | 198.589 | 24.3963 | 799801 | 0.153901 | 151.322 | true |
| 10 | 200 | abundance_mass_x | 260.123 | 25.3183 | 799740 | 0.121925 | 151.31 | true |
| 10 | 500 | abundance_mass_x | 640.581 | 27.2955 | 799359 | 0.0533515 | 151.238 | true |


**`rel_err_at_R25_affinity_rule`**: `[0.7611360767509552, 0.910841610437863, 0.3356371285870865]`


**`rel_err_at_R25_abundance_rule`**: `[0.48258079119971853, 0.818562252128757, 0.18240041920337888]`


**`synthetic_pilot_for_comparison`**

```json
{
  "affinity_rule_at_R25_vs_4000_reference": 0.0004,
  "abundance_rule": "86% and non-converging",
  "note": "pilot figures quoted from the build brief for comparison only; the measured values above supersede them and were computed on the real transcriptome"
}
```


### `e4b_binned_background`  (OK)

seed `0`, wall clock `19.428` s, recorded `2026-09-04T19:44:44Z`

| quantity | value |
|---|---|
| `construct` | MAPK14-193_parent |
| `reference_set_size_including_on_target` | 952 |
| `gencode_release` | 50 |
| `B_sweep_extension_note` | The brief asks for B in {1,2,3,5,10}. No B in that set restores invariance at R = 25, so the sweep was extended upward until the convergence is visible and the smallest sufficient B can be reported rather than merely bounded below. Both answers are given: smallest_B_within_required_sweep_o_target... |
| `total_mrna_molecules_per_cell` | 80000 |
| `invariance_criterion` | invariance is 'restored' at a given (rule, R, threshold) when the relative error of the on-target occupancy against the full-transcriptome reference is below the threshold at EVERY rho in rho_values, not merely on average. The threshold is a choice of ours and several are reported rather than one. |
| `smallest_B_at_R25_quantile_threshold_0.01` | 100 |
| `smallest_B_at_R25_quantile_threshold_0.1` | 20 |
| `smallest_B_at_R25_equal_width_threshold_0.01` | 100 |
| `max_rel_err_o_target_at_R25_linear_rule` | 0.910842 |
| `max_rel_err_o_target_at_R25_binned_B10_quantile` | 0.271417 |
| `max_rel_err_o_target_binned_B10_quantile_all_R` | 0.271417 |
| `regression_against_e4_max_rel_diff` | 0 |
| `regression_against_e4_passes_at_1e-12` | true |
| `regression_note` | B = 1 with the omitted mass collapsed to a single LINEAR term is the affinity-weighted rule of e4. It is recomputed here through riscpool.background and compared row by row against the stored results/e4_retrieval_invariance.json. A mismatch would mean the two experiments no longer describe the sa... |
| `n_rows` | 318 |
| `weak_limit_note` | frac_omitted_with_K_above_10f is the fraction of OMITTED transcripts in the weak-binding regime at the solved free pool. It is a property of the truncation, not of the background rule, so it is nearly the same for the linear and binned backgrounds at a given R; what changes is whether the backgro... |


**`rho_values`**: `[0.01, 0.5, 10.0]`


**`R_values`**: `[25, 50, 100, 200, 500]`


**`B_values`**: `[1, 2, 3, 5, 10, 20, 50, 100, 200, 500]`


**`B_values_required_by_brief`**: `[1, 2, 3, 5, 10]`


**`binning_rules`**: `["quantile", "equal_width"]`


**`error_thresholds_for_invariance`**: `[0.5, 0.1, 0.01, 0.001]`


**`reference_by_rho`**

```json
{
  "0.01": {
    "f": 0.12247984921416158,
    "o_target": 0.09741263560472395,
    "total_load": 799.8775201507858
  },
  "0.5": {
    "f": 35350.848642494864,
    "o_target": 28.80572242674353,
    "total_load": 4649.1513575051395
  },
  "10.0": {
    "f": 794749.2775378355,
    "o_target": 28.83385444484576,
    "total_load": 5250.722462164455
  }
}
```


**`smallest_B_restoring_invariance`**

| binning_rule | R | threshold | smallest_B_all_rho_o_target | smallest_B_all_rho_total_load | smallest_B_within_required_sweep_o_target | smallest_B_at_rho_0.01 | smallest_B_at_rho_0.5 | smallest_B_at_rho_10.0 |
|---|---|---|---|---|---|---|---|---|
| quantile | 25 | 0.5 | 10 | 1 | 10 | 10 | 1 | 1 |
| quantile | 25 | 0.1 | 20 | 3 | null | 20 | 1 | 1 |
| quantile | 25 | 0.01 | 100 | 20 | null | 100 | 1 | 1 |
| quantile | 25 | 0.001 | 200 | 50 | null | 200 | 1 | 1 |
| quantile | 50 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| quantile | 50 | 0.1 | 10 | 3 | 10 | 10 | 1 | 1 |
| quantile | 50 | 0.01 | 50 | 20 | null | 50 | 1 | 1 |
| quantile | 50 | 0.001 | 100 | 50 | null | 100 | 1 | 1 |
| quantile | 100 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| quantile | 100 | 0.1 | 1 | 3 | 1 | 1 | 1 | 1 |
| quantile | 100 | 0.01 | 20 | 20 | null | 20 | 1 | 1 |
| quantile | 100 | 0.001 | 100 | 50 | null | 100 | 1 | 1 |
| quantile | 200 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| quantile | 200 | 0.1 | 1 | 3 | 1 | 1 | 1 | 1 |
| quantile | 200 | 0.01 | 1 | 20 | 1 | 1 | 1 | 1 |
| quantile | 200 | 0.001 | 20 | 50 | null | 20 | 1 | 1 |
| quantile | 500 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| quantile | 500 | 0.1 | 1 | 2 | 1 | 1 | 1 | 1 |
| quantile | 500 | 0.01 | 1 | 10 | 1 | 1 | 1 | 1 |
| quantile | 500 | 0.001 | 1 | 20 | 1 | 1 | 1 | 1 |
| equal_width | 25 | 0.5 | 5 | 1 | 5 | 5 | 1 | 1 |
| equal_width | 25 | 0.1 | 20 | 2 | null | 20 | 1 | 1 |
| equal_width | 25 | 0.01 | 100 | 50 | null | 100 | 1 | 1 |
| equal_width | 25 | 0.001 | 200 | 100 | null | 200 | 1 | 1 |
| equal_width | 50 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| equal_width | 50 | 0.1 | 10 | 5 | 10 | 10 | 1 | 1 |
| equal_width | 50 | 0.01 | 50 | 20 | null | 50 | 1 | 1 |
| equal_width | 50 | 0.001 | 100 | 100 | null | 100 | 1 | 1 |
| equal_width | 100 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| equal_width | 100 | 0.1 | 1 | 5 | 1 | 1 | 1 | 1 |
| equal_width | 100 | 0.01 | 20 | 20 | null | 20 | 1 | 1 |
| equal_width | 100 | 0.001 | 50 | 100 | null | 50 | 1 | 1 |
| equal_width | 200 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| equal_width | 200 | 0.1 | 1 | 3 | 1 | 1 | 1 | 1 |
| equal_width | 200 | 0.01 | 1 | 20 | 1 | 1 | 1 | 1 |
| equal_width | 200 | 0.001 | 10 | 100 | 10 | 10 | 1 | 1 |
| equal_width | 500 | 0.5 | 1 | 1 | 1 | 1 | 1 | 1 |
| equal_width | 500 | 0.1 | 1 | 3 | 1 | 1 | 1 | 1 |
| equal_width | 500 | 0.01 | 1 | 20 | 1 | 1 | 1 | 1 |
| equal_width | 500 | 0.001 | 1 | 50 | 1 | 1 | 1 | 1 |


**`regression_against_e4`**

| rho | R | e4_stored_o_target | e4b_recomputed_o_target | abs_diff_o_target | e4_stored_f | e4b_recomputed_f | abs_diff_f | e4_stored_beta | e4b_recomputed_beta | abs_diff_beta |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.01 | 25 | 0.0232684 | 0.0232684 | 0 | 0.0291807 | 0.0291807 | 0 | 11178.7 | 11178.7 | 0 |
| 0.01 | 50 | 0.0604282 | 0.0604282 | 0 | 0.0758805 | 0.0758805 | 0 | 2072.69 | 2072.69 | 0 |
| 0.01 | 100 | 0.0891858 | 0.0891858 | 0 | 0.112104 | 0.112104 | 0 | 388.381 | 388.381 | 0 |
| 0.01 | 200 | 0.0971407 | 0.0971407 | 0 | 0.122137 | 0.122137 | 0 | 37.3539 | 37.3539 | 0 |
| 0.01 | 500 | 0.0974126 | 0.0974126 | 0 | 0.12248 | 0.12248 | 0 | 0.248468 | 0.248468 | 0 |
| 0.5 | 25 | 2.56827 | 2.56827 | 0 | 3.53293 | 3.53293 | 0 | 11178.7 | 11178.7 | 0 |
| 0.5 | 50 | 9.87357 | 9.87357 | 0 | 18.8149 | 18.8149 | 0 | 2072.69 | 2072.69 | 0 |
| 0.5 | 100 | 21.1284 | 21.1284 | 0 | 99.06 | 99.06 | 0 | 388.381 | 388.381 | 0 |
| 0.5 | 200 | 27.8115 | 27.8115 | 0 | 981.673 | 981.673 | 0 | 37.3539 | 37.3539 | 0 |
| 0.5 | 500 | 28.799 | 28.799 | 0 | 28777.4 | 28777.4 | 0 | 0.248468 | 0.248468 | 0 |
| 10 | 25 | 19.1561 | 19.1561 | 0 | 71.512 | 71.512 | 0 | 11178.7 | 11178.7 | 0 |
| 10 | 50 | 26.3629 | 26.3629 | 0 | 385.3 | 385.3 | 0 | 2072.69 | 2072.69 | 0 |
| 10 | 100 | 28.3359 | 28.3359 | 0 | 2050.83 | 2050.83 | 0 | 388.381 | 388.381 | 0 |
| 10 | 200 | 28.7852 | 28.7852 | 0 | 20795.9 | 20795.9 | 0 | 37.3539 | 37.3539 | 0 |
| 10 | 500 | 28.8335 | 28.8335 | 0 | 637410 | 637410 | 0 | 0.248468 | 0.248468 | 0 |


**`per_setting_summary`**

| binning_rule | R | B | max_rel_err_o_target_over_rho | mean_rel_err_o_target_over_rho | max_rel_err_total_load_over_rho | max_rel_err_o_target_linear_rule | mean_n_bins_used | mean_frac_omitted_with_K_above_10f | n_rows_where_linearisation_holds | n_rows |
|---|---|---|---|---|---|---|---|---|---|---|
| quantile | 25 | 1 | 0.745512 | 0.248512 | 0.17567 | 0.910842 | 1 | 0.314635 | 0 | 3 |
| quantile | 25 | 2 | 0.725097 | 0.241706 | 0.159731 | 0.910842 | 2 | 0.313556 | 0 | 3 |
| quantile | 25 | 3 | 0.701774 | 0.233929 | 0.0953072 | 0.910842 | 3 | 0.311399 | 0 | 3 |
| quantile | 25 | 5 | 0.645795 | 0.215267 | 0.0350027 | 0.910842 | 5 | 0.309601 | 0 | 3 |
| quantile | 25 | 10 | 0.271417 | 0.0904729 | 0.0157743 | 0.910842 | 10 | 0.298454 | 0 | 3 |
| quantile | 25 | 20 | 0.0706113 | 0.0235372 | 0.00503141 | 0.910842 | 20 | 0.294498 | 0 | 3 |
| quantile | 25 | 50 | 0.0112733 | 0.0037578 | 5.1644e-04 | 0.910842 | 50 | 0.293779 | 0 | 3 |
| quantile | 25 | 100 | 0.00248656 | 8.2885e-04 | 1.1664e-04 | 0.910842 | 100 | 0.293779 | 0 | 3 |
| quantile | 25 | 200 | 5.4795e-04 | 1.8265e-04 | 1.9575e-05 | 0.910842 | 200 | 0.293779 | 0 | 3 |
| quantile | 25 | 500 | 4.1773e-05 | 1.3924e-05 | 5.4125e-06 | 0.910842 | 499 | 0.293779 | 0 | 3 |
| quantile | 50 | 1 | 0.36539 | 0.121805 | 0.175623 | 0.657236 | 1 | 0.310791 | 0 | 3 |
| quantile | 50 | 2 | 0.3473 | 0.115774 | 0.155341 | 0.657236 | 2 | 0.310052 | 0 | 3 |
| quantile | 50 | 3 | 0.320677 | 0.106896 | 0.0886684 | 0.657236 | 3 | 0.308574 | 0 | 3 |
| quantile | 50 | 5 | 0.254683 | 0.0848959 | 0.0329653 | 0.657236 | 5 | 0.306356 | 0 | 3 |
| quantile | 50 | 10 | 0.0944144 | 0.0314719 | 0.0156473 | 0.657236 | 10 | 0.3034 | 0 | 3 |
| quantile | 50 | 20 | 0.0209719 | 0.00699075 | 0.00501346 | 0.657236 | 20 | 0.301922 | 0 | 3 |
| quantile | 50 | 50 | 0.00390174 | 0.00130059 | 4.0274e-04 | 0.657236 | 50 | 0.301922 | 0 | 3 |
| quantile | 50 | 100 | 8.3886e-04 | 2.7962e-04 | 1.1096e-04 | 0.657236 | 100 | 0.301922 | 0 | 3 |
| quantile | 50 | 200 | 2.2538e-04 | 7.5126e-05 | 1.9474e-05 | 0.657236 | 200 | 0.301922 | 0 | 3 |
| quantile | 50 | 500 | 7.3364e-05 | 2.4455e-05 | 2.5140e-06 | 0.657236 | 499 | 0.301922 | 0 | 3 |
| quantile | 100 | 1 | 0.0821235 | 0.0273825 | 0.175418 | 0.26652 | 1 | 0.320423 | 0 | 3 |
| quantile | 100 | 2 | 0.0787923 | 0.0262711 | 0.152989 | 0.26652 | 2 | 0.320423 | 0 | 3 |
| quantile | 100 | 3 | 0.0724531 | 0.0241541 | 0.0680263 | 0.26652 | 3 | 0.319249 | 0 | 3 |
| quantile | 100 | 5 | 0.0612736 | 0.0204257 | 0.0284311 | 0.26652 | 5 | 0.318858 | 0 | 3 |
| quantile | 100 | 10 | 0.0305513 | 0.0101841 | 0.0150183 | 0.26652 | 10 | 0.318466 | 0 | 3 |
| quantile | 100 | 20 | 0.00798247 | 0.00266091 | 0.00469552 | 0.26652 | 20 | 0.318466 | 0 | 3 |
| quantile | 100 | 50 | 0.00152528 | 5.0844e-04 | 3.8354e-04 | 0.26652 | 50 | 0.318466 | 0 | 3 |
| quantile | 100 | 100 | 4.2370e-04 | 1.4123e-04 | 8.5370e-05 | 0.26652 | 100 | 0.318466 | 0 | 3 |
| quantile | 100 | 200 | 1.3682e-04 | 4.5608e-05 | 1.4879e-05 | 0.26652 | 200 | 0.318466 | 0 | 3 |
| quantile | 100 | 500 | 2.2940e-05 | 7.6467e-06 | 1.6260e-06 | 0.26652 | 498 | 0.318466 | 0 | 3 |
| quantile | 200 | 1 | 0.0027517 | 9.2520e-04 | 0.173773 | 0.0345149 | 1 | 0.342642 | 1 | 3 |
| quantile | 200 | 2 | 0.00268281 | 8.9991e-04 | 0.123914 | 0.0345149 | 2 | 0.342199 | 1 | 3 |
| quantile | 200 | 3 | 0.00258057 | 8.6285e-04 | 0.0588132 | 0.0345149 | 3 | 0.341755 | 1 | 3 |
| quantile | 200 | 5 | 0.00223169 | 7.4492e-04 | 0.0274284 | 0.0345149 | 5 | 0.341755 | 1 | 3 |
| quantile | 200 | 10 | 0.00145999 | 4.8706e-04 | 0.0112892 | 0.0345149 | 10 | 0.341755 | 1 | 3 |
| quantile | 200 | 20 | 6.8571e-04 | 2.2866e-04 | 0.00213148 | 0.0345149 | 20 | 0.341755 | 1 | 3 |
| quantile | 200 | 50 | 2.0640e-04 | 6.8809e-05 | 5.1905e-04 | 0.0345149 | 50 | 0.341755 | 1 | 3 |
| quantile | 200 | 100 | 5.7842e-05 | 1.9282e-05 | 9.2819e-05 | 0.0345149 | 100 | 0.341755 | 1 | 3 |
| quantile | 200 | 200 | 2.1183e-05 | 7.0614e-06 | 1.4788e-05 | 0.0345149 | 200 | 0.341755 | 1 | 3 |
| quantile | 200 | 500 | 4.9618e-06 | 1.6540e-06 | 2.6220e-06 | 0.0345149 | 499 | 0.341755 | 1 | 3 |
| quantile | 500 | 1 | 1.5523e-05 | 5.2454e-06 | 0.113865 | 2.3319e-04 | 1 | 0.373156 | 1 | 3 |
| quantile | 500 | 2 | 5.0250e-06 | 1.7392e-06 | 0.0372368 | 2.3319e-04 | 2 | 0.373156 | 1 | 3 |
| quantile | 500 | 3 | 1.6709e-06 | 6.1316e-07 | 0.024422 | 2.3319e-04 | 3 | 0.373156 | 1 | 3 |
| quantile | 500 | 5 | 9.2202e-07 | 3.5330e-07 | 0.0150345 | 2.3319e-04 | 5 | 0.373156 | 1 | 3 |
| quantile | 500 | 10 | 2.2543e-07 | 1.0455e-07 | 0.00492251 | 2.3319e-04 | 10 | 0.373156 | 1 | 3 |
| quantile | 500 | 20 | 4.9700e-08 | 3.0971e-08 | 8.5693e-04 | 2.3319e-04 | 20 | 0.373156 | 1 | 3 |
| quantile | 500 | 50 | 2.2373e-08 | 9.7586e-09 | 1.1039e-04 | 2.3319e-04 | 50 | 0.373156 | 1 | 3 |
| quantile | 500 | 100 | 1.6823e-08 | 5.9438e-09 | 1.9387e-05 | 2.3319e-04 | 100 | 0.373156 | 1 | 3 |
| quantile | 500 | 200 | 1.3233e-08 | 4.5262e-09 | 7.2203e-06 | 2.3319e-04 | 200 | 0.373156 | 1 | 3 |
| quantile | 500 | 500 | 2.8493e-16 | 9.4976e-17 | 1.9563e-16 | 2.3319e-04 | 451 | 0.373156 | 1 | 3 |
| equal_width | 25 | 1 | 0.745512 | 0.248512 | 0.17567 | 0.910842 | 1 | 0.314635 | 0 | 3 |
| equal_width | 25 | 2 | 0.742737 | 0.247582 | 0.0594881 | 0.910842 | 2 | 0.313916 | 0 | 3 |
| equal_width | 25 | 3 | 0.710002 | 0.236675 | 0.161115 | 0.910842 | 3 | 0.312478 | 0 | 3 |
| equal_width | 25 | 5 | 0.327154 | 0.109056 | 0.104833 | 0.910842 | 5 | 0.300611 | 0 | 3 |
| equal_width | 25 | 10 | 0.226594 | 0.0755329 | 0.0348399 | 0.910842 | 10 | 0.297375 | 0 | 3 |
| equal_width | 25 | 20 | 0.0734263 | 0.0244759 | 0.0109228 | 0.910842 | 19 | 0.294498 | 0 | 3 |
| equal_width | 25 | 50 | 0.0119631 | 0.00398777 | 0.00135944 | 0.910842 | 36 | 0.293779 | 0 | 3 |
| equal_width | 25 | 100 | 0.00187283 | 6.2429e-04 | 2.9953e-04 | 0.910842 | 66 | 0.293779 | 0 | 3 |
| equal_width | 25 | 200 | 4.0919e-04 | 1.3640e-04 | 4.6268e-05 | 0.910842 | 117 | 0.293779 | 0 | 3 |
| equal_width | 25 | 500 | 1.1079e-04 | 3.6929e-05 | 5.1642e-06 | 0.910842 | 245 | 0.293779 | 0 | 3 |
| equal_width | 50 | 1 | 0.36539 | 0.121805 | 0.175623 | 0.657236 | 1 | 0.310791 | 0 | 3 |
| equal_width | 50 | 2 | 0.364479 | 0.121499 | 0.12198 | 0.657236 | 2 | 0.310421 | 0 | 3 |
| equal_width | 50 | 3 | 0.353484 | 0.117834 | 0.121917 | 0.657236 | 3 | 0.310052 | 0 | 3 |
| equal_width | 50 | 5 | 0.263794 | 0.0879337 | 0.0535297 | 0.657236 | 5 | 0.306356 | 0 | 3 |
| equal_width | 50 | 10 | 0.0782734 | 0.0260926 | 0.0337502 | 0.657236 | 10 | 0.30303 | 0 | 3 |
| equal_width | 50 | 20 | 0.0257451 | 0.0085821 | 0.00917784 | 0.657236 | 18 | 0.301922 | 0 | 3 |
| equal_width | 50 | 50 | 0.00371146 | 0.00123721 | 0.00127844 | 0.657236 | 38 | 0.301922 | 0 | 3 |
| equal_width | 50 | 100 | 9.0289e-04 | 3.0097e-04 | 2.1006e-04 | 0.657236 | 67 | 0.301922 | 0 | 3 |
| equal_width | 50 | 200 | 2.7167e-04 | 9.0561e-05 | 5.2569e-05 | 0.657236 | 123 | 0.301922 | 0 | 3 |
| equal_width | 50 | 500 | 1.6210e-05 | 5.4034e-06 | 3.8403e-06 | 0.657236 | 262 | 0.301922 | 0 | 3 |
| equal_width | 100 | 1 | 0.0821235 | 0.0273825 | 0.175418 | 0.26652 | 1 | 0.320423 | 0 | 3 |
| equal_width | 100 | 2 | 0.0820084 | 0.0273423 | 0.135679 | 0.26652 | 2 | 0.320031 | 0 | 3 |
| equal_width | 100 | 3 | 0.0800741 | 0.0266963 | 0.108099 | 0.26652 | 3 | 0.31964 | 0 | 3 |
| equal_width | 100 | 5 | 0.0614206 | 0.0204754 | 0.0421018 | 0.26652 | 5 | 0.318858 | 0 | 3 |
| equal_width | 100 | 10 | 0.0144066 | 0.00480353 | 0.0293577 | 0.26652 | 10 | 0.318466 | 0 | 3 |
| equal_width | 100 | 20 | 0.00493116 | 0.0016441 | 0.00859258 | 0.26652 | 18 | 0.318466 | 0 | 3 |
| equal_width | 100 | 50 | 8.1461e-04 | 2.7159e-04 | 0.00119294 | 0.26652 | 36 | 0.318466 | 0 | 3 |
| equal_width | 100 | 100 | 1.5206e-04 | 5.0697e-05 | 2.1170e-04 | 0.26652 | 67 | 0.318466 | 0 | 3 |
| equal_width | 100 | 200 | 2.7428e-05 | 9.1445e-06 | 4.1319e-05 | 0.26652 | 120 | 0.318466 | 0 | 3 |
| equal_width | 100 | 500 | 2.9876e-06 | 9.9607e-07 | 4.6371e-06 | 0.26652 | 248 | 0.318466 | 0 | 3 |

_100 rows total, first 80 shown; full data in the JSON._


**`table`**

| rho | R | B | binning_rule | background | f | o_target | total_load | rel_err_o_target | rel_err_total_load | rel_err_f |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.01 | 952 | null | full reference | none | 0.12248 | 0.0974126 | 799.878 | 0 | 0 | 0 |
| 0.5 | 952 | null | full reference | none | 35350.8 | 28.8057 | 4649.15 | 0 | 0 | 0 |
| 10 | 952 | null | full reference | none | 794749 | 28.8339 | 5250.72 | 0 | 0 | 0 |
| 0.01 | 25 | 1 | n/a | linear_affinity_weighted_e4_rule | 0.0291807 | 0.0232684 | 799.971 | 0.761136 | 1.1664e-04 | 0.761751 |
| 0.01 | 25 | 1 | quantile | binned_michaelis | 0.0310911 | 0.0247904 | 799.969 | 0.745512 | 1.1425e-04 | 0.746153 |
| 0.01 | 25 | 2 | quantile | binned_michaelis | 0.0335875 | 0.026779 | 799.966 | 0.725097 | 1.1113e-04 | 0.725771 |
| 0.01 | 25 | 3 | quantile | binned_michaelis | 0.0364399 | 0.0290509 | 799.964 | 0.701774 | 1.0757e-04 | 0.702482 |
| 0.01 | 25 | 5 | quantile | binned_michaelis | 0.0432882 | 0.034504 | 799.957 | 0.645795 | 9.9005e-05 | 0.646569 |
| 0.01 | 25 | 10 | quantile | binned_michaelis | 0.0891547 | 0.0709732 | 799.911 | 0.271417 | 4.1663e-05 | 0.272087 |
| 0.01 | 25 | 20 | quantile | binned_michaelis | 0.113804 | 0.0905342 | 799.886 | 0.0706113 | 1.0846e-05 | 0.0708337 |
| 0.01 | 25 | 50 | quantile | binned_michaelis | 0.121094 | 0.0963145 | 799.879 | 0.0112733 | 1.7320e-06 | 0.0113111 |
| 0.01 | 25 | 100 | quantile | binned_michaelis | 0.122174 | 0.0971704 | 799.878 | 0.00248656 | 3.8204e-07 | 0.00249496 |
| 0.01 | 25 | 200 | quantile | binned_michaelis | 0.122413 | 0.0973593 | 799.878 | 5.4795e-04 | 8.4188e-08 | 5.4981e-04 |
| 0.01 | 25 | 500 | quantile | binned_michaelis | 0.122475 | 0.0974086 | 799.878 | 4.1773e-05 | 6.4180e-09 | 4.1914e-05 |
| 0.01 | 25 | 1 | equal_width | binned_michaelis | 0.0310911 | 0.0247904 | 799.969 | 0.745512 | 1.1425e-04 | 0.746153 |
| 0.01 | 25 | 2 | equal_width | binned_michaelis | 0.0314304 | 0.0250607 | 799.969 | 0.742737 | 1.1383e-04 | 0.743383 |
| 0.01 | 25 | 3 | equal_width | binned_michaelis | 0.0354337 | 0.0282495 | 799.965 | 0.710002 | 1.0882e-04 | 0.710698 |
| 0.01 | 25 | 5 | equal_width | binned_michaelis | 0.0823187 | 0.0655437 | 799.918 | 0.327154 | 5.0209e-05 | 0.3279 |
| 0.01 | 25 | 10 | equal_width | binned_michaelis | 0.0946539 | 0.0753395 | 799.905 | 0.226594 | 3.4788e-05 | 0.227188 |
| 0.01 | 25 | 20 | equal_width | binned_michaelis | 0.113458 | 0.09026 | 799.887 | 0.0734263 | 1.1279e-05 | 0.0736569 |
| 0.01 | 25 | 50 | equal_width | binned_michaelis | 0.12101 | 0.0962473 | 799.879 | 0.0119631 | 1.8380e-06 | 0.0120032 |
| 0.01 | 25 | 100 | equal_width | binned_michaelis | 0.12225 | 0.0972302 | 799.878 | 0.00187283 | 2.8774e-07 | 0.00187916 |
| 0.01 | 25 | 200 | equal_width | binned_michaelis | 0.12243 | 0.0973728 | 799.878 | 4.0919e-04 | 6.2869e-08 | 4.1058e-04 |
| 0.01 | 25 | 500 | equal_width | binned_michaelis | 0.122466 | 0.0974018 | 799.878 | 1.1079e-04 | 1.7022e-08 | 1.1116e-04 |
| 0.01 | 50 | 1 | n/a | linear_affinity_weighted_e4_rule | 0.0758805 | 0.0604282 | 799.924 | 0.379668 | 5.8258e-05 | 0.380465 |
| 0.01 | 50 | 1 | quantile | binned_michaelis | 0.0776308 | 0.061819 | 799.922 | 0.36539 | 5.6070e-05 | 0.366175 |
| 0.01 | 50 | 2 | quantile | binned_michaelis | 0.0798486 | 0.0635812 | 799.92 | 0.3473 | 5.3297e-05 | 0.348068 |
| 0.01 | 50 | 3 | quantile | binned_michaelis | 0.083113 | 0.0661746 | 799.917 | 0.320677 | 4.9216e-05 | 0.321415 |
| 0.01 | 50 | 5 | quantile | binned_michaelis | 0.0912075 | 0.0726033 | 799.909 | 0.254683 | 3.9096e-05 | 0.255326 |
| 0.01 | 50 | 10 | quantile | binned_michaelis | 0.110881 | 0.0882155 | 799.889 | 0.0944144 | 1.4501e-05 | 0.0947041 |
| 0.01 | 50 | 20 | quantile | binned_michaelis | 0.119903 | 0.0953697 | 799.88 | 0.0209719 | 3.2219e-06 | 0.0210415 |
| 0.01 | 50 | 50 | quantile | binned_michaelis | 0.122 | 0.0970326 | 799.878 | 0.00390174 | 5.9946e-07 | 0.00391491 |
| 0.01 | 50 | 100 | quantile | binned_michaelis | 0.122377 | 0.0973309 | 799.878 | 8.3886e-04 | 1.2888e-07 | 8.4170e-04 |
| 0.01 | 50 | 200 | quantile | binned_michaelis | 0.122452 | 0.0973907 | 799.878 | 2.2538e-04 | 3.4627e-08 | 2.2614e-04 |
| 0.01 | 50 | 500 | quantile | binned_michaelis | 0.122471 | 0.0974055 | 799.878 | 7.3364e-05 | 1.1272e-08 | 7.3612e-05 |
| 0.01 | 50 | 1 | equal_width | binned_michaelis | 0.0776308 | 0.061819 | 799.922 | 0.36539 | 5.6070e-05 | 0.366175 |
| 0.01 | 50 | 2 | equal_width | binned_michaelis | 0.0777424 | 0.0619078 | 799.922 | 0.364479 | 5.5930e-05 | 0.365263 |
| 0.01 | 50 | 3 | equal_width | binned_michaelis | 0.0790904 | 0.0629788 | 799.921 | 0.353484 | 5.4245e-05 | 0.354258 |
| 0.01 | 50 | 5 | equal_width | binned_michaelis | 0.0900898 | 0.0717158 | 799.91 | 0.263794 | 4.0494e-05 | 0.264452 |
| 0.01 | 50 | 10 | equal_width | binned_michaelis | 0.112863 | 0.0897878 | 799.887 | 0.0782734 | 1.2023e-05 | 0.0785178 |
| 0.01 | 50 | 20 | equal_width | binned_michaelis | 0.119316 | 0.0949047 | 799.881 | 0.0257451 | 3.9552e-06 | 0.0258301 |
| 0.01 | 50 | 50 | equal_width | binned_michaelis | 0.122024 | 0.0970511 | 799.878 | 0.00371146 | 5.7023e-07 | 0.00372399 |
| 0.01 | 50 | 100 | equal_width | binned_michaelis | 0.122369 | 0.0973247 | 799.878 | 9.0289e-04 | 1.3872e-07 | 9.0594e-04 |
| 0.01 | 50 | 200 | equal_width | binned_michaelis | 0.122446 | 0.0973862 | 799.878 | 2.7167e-04 | 4.1741e-08 | 2.7260e-04 |
| 0.01 | 50 | 500 | equal_width | binned_michaelis | 0.122478 | 0.0974111 | 799.878 | 1.6210e-05 | 2.4905e-09 | 1.6265e-05 |
| 0.01 | 100 | 1 | n/a | linear_affinity_weighted_e4_rule | 0.112104 | 0.0891858 | 799.888 | 0.0844531 | 1.2972e-05 | 0.0847151 |
| 0.01 | 100 | 1 | quantile | binned_michaelis | 0.11239 | 0.0894128 | 799.888 | 0.0821235 | 1.2614e-05 | 0.0823789 |
| 0.01 | 100 | 2 | quantile | binned_michaelis | 0.112799 | 0.0897373 | 799.887 | 0.0787923 | 1.2103e-05 | 0.0790383 |
| 0.01 | 100 | 3 | quantile | binned_michaelis | 0.113578 | 0.0903548 | 799.886 | 0.0724531 | 1.1129e-05 | 0.0726809 |
| 0.01 | 100 | 5 | quantile | binned_michaelis | 0.114951 | 0.0914438 | 799.885 | 0.0612736 | 9.4123e-06 | 0.0614685 |
| 0.01 | 100 | 10 | quantile | binned_michaelis | 0.118726 | 0.0944365 | 799.881 | 0.0305513 | 4.6935e-06 | 0.0306517 |
| 0.01 | 100 | 20 | quantile | binned_michaelis | 0.121499 | 0.096635 | 799.879 | 0.00798247 | 1.2264e-06 | 0.00800931 |
| 0.01 | 100 | 50 | quantile | binned_michaelis | 0.122292 | 0.0972641 | 799.878 | 0.00152528 | 2.3435e-07 | 0.00153044 |
| 0.01 | 100 | 100 | quantile | binned_michaelis | 0.122428 | 0.0973714 | 799.878 | 4.2370e-04 | 6.5098e-08 | 4.2513e-04 |
| 0.01 | 100 | 200 | quantile | binned_michaelis | 0.122463 | 0.0973993 | 799.878 | 1.3682e-04 | 2.1022e-08 | 1.3729e-04 |
| 0.01 | 100 | 500 | quantile | binned_michaelis | 0.122477 | 0.0974104 | 799.878 | 2.2940e-05 | 3.5245e-09 | 2.3018e-05 |
| 0.01 | 100 | 1 | equal_width | binned_michaelis | 0.11239 | 0.0894128 | 799.888 | 0.0821235 | 1.2614e-05 | 0.0823789 |
| 0.01 | 100 | 2 | equal_width | binned_michaelis | 0.112404 | 0.089424 | 799.888 | 0.0820084 | 1.2596e-05 | 0.0822635 |
| 0.01 | 100 | 3 | equal_width | binned_michaelis | 0.112642 | 0.0896124 | 799.887 | 0.0800741 | 1.2299e-05 | 0.0803237 |
| 0.01 | 100 | 5 | equal_width | binned_michaelis | 0.114933 | 0.0914295 | 799.885 | 0.0614206 | 9.4348e-06 | 0.0616159 |
| 0.01 | 100 | 10 | equal_width | binned_michaelis | 0.120709 | 0.0960092 | 799.879 | 0.0144066 | 2.2134e-06 | 0.0144548 |
| 0.01 | 100 | 20 | equal_width | binned_michaelis | 0.121874 | 0.0969323 | 799.878 | 0.00493116 | 7.5762e-07 | 0.00494779 |
| 0.01 | 100 | 50 | equal_width | binned_michaelis | 0.12238 | 0.0973333 | 799.878 | 8.1461e-04 | 1.2516e-07 | 8.1737e-04 |
| 0.01 | 100 | 100 | equal_width | binned_michaelis | 0.122461 | 0.0973978 | 799.878 | 1.5206e-04 | 2.3363e-08 | 1.5258e-04 |
| 0.01 | 100 | 200 | equal_width | binned_michaelis | 0.122476 | 0.09741 | 799.878 | 2.7428e-05 | 4.2141e-09 | 2.7521e-05 |
| 0.01 | 100 | 500 | equal_width | binned_michaelis | 0.122479 | 0.0974123 | 799.878 | 2.9876e-06 | 4.5902e-10 | 2.9977e-06 |
| 0.01 | 200 | 1 | n/a | linear_affinity_weighted_e4_rule | 0.122137 | 0.0971407 | 799.878 | 0.00279169 | 4.2892e-07 | 0.00280112 |
| 0.01 | 200 | 1 | quantile | binned_michaelis | 0.122142 | 0.0971446 | 799.878 | 0.0027517 | 4.2277e-07 | 0.00276101 |
| 0.01 | 200 | 2 | quantile | binned_michaelis | 0.12215 | 0.0971513 | 799.878 | 0.00268281 | 4.1219e-07 | 0.00269188 |
| 0.01 | 200 | 3 | quantile | binned_michaelis | 0.122163 | 0.0971613 | 799.878 | 0.00258057 | 3.9648e-07 | 0.0025893 |
| 0.01 | 200 | 5 | quantile | binned_michaelis | 0.122206 | 0.0971952 | 799.878 | 0.00223169 | 3.4288e-07 | 0.00223924 |
| 0.01 | 200 | 10 | quantile | binned_michaelis | 0.1223 | 0.0972704 | 799.878 | 0.00145999 | 2.2431e-07 | 0.00146493 |
| 0.01 | 200 | 20 | quantile | binned_michaelis | 0.122396 | 0.0973458 | 799.878 | 6.8571e-04 | 1.0535e-07 | 6.8803e-04 |
| 0.01 | 200 | 50 | quantile | binned_michaelis | 0.122454 | 0.0973925 | 799.878 | 2.0640e-04 | 3.1712e-08 | 2.0710e-04 |
| 0.01 | 200 | 100 | quantile | binned_michaelis | 0.122473 | 0.097407 | 799.878 | 5.7842e-05 | 8.8869e-09 | 5.8038e-05 |
| 0.01 | 200 | 200 | quantile | binned_michaelis | 0.122477 | 0.0974106 | 799.878 | 2.1183e-05 | 3.2547e-09 | 2.1255e-05 |
| 0.01 | 200 | 500 | quantile | binned_michaelis | 0.122479 | 0.0974122 | 799.878 | 4.9618e-06 | 7.6234e-10 | 4.9786e-06 |
| 0.01 | 200 | 1 | equal_width | binned_michaelis | 0.122142 | 0.0971446 | 799.878 | 0.0027517 | 4.2277e-07 | 0.00276101 |
| 0.01 | 200 | 2 | equal_width | binned_michaelis | 0.122142 | 0.0971447 | 799.878 | 0.00275006 | 4.2252e-07 | 0.00275936 |
| 0.01 | 200 | 3 | equal_width | binned_michaelis | 0.122146 | 0.0971483 | 799.878 | 0.00271386 | 4.1696e-07 | 0.00272303 |

_318 rows total, first 80 shown; full data in the JSON._


### `e9_dose_response`  (OK)

seed `0`, wall clock `1651.67` s, recorded `2026-09-05T03:52:38Z`

| quantity | value |
|---|---|
| `PREDICTION_DIRECTION_CORRECTION` | The brief states that the equilibrium free pool grows SUBLINEARLY in dose and that a log-log slope below 1 is the signature of competition. The conservation equation says the opposite. M(f) is strictly concave in f because d2M/df2 = -sum_j 2 x_j K_j/(K_j+f)^3 < 0, so f is strictly convex in M, an... |
| `identifying_assumption` | the amplitude c, the log2 repression of a fully occupied transcript, is shared across doses within a construct because it is a property of the silencing machinery and cannot depend on how much siRNA was pipetted on. In the weak-binding limit only the product c * pool is identified, so the ABSOLUT... |
| `PROPORTIONAL_LOADING_ASSUMPTION` | We ASSUME that the intracellular guide-specific loaded pool M is proportional to the administered guide dose. Total transfected duplex is held constant across doses by making the specific siRNA up to 25 nM with non-targeting control siRNA, and to 10 nM with AllStars for HK2-4031, as the CEL file ... |
| `data_source` | GSE28786 (Caffrey et al. 2011, PMC3130022) |
| `gencode_release` | 50 |
| `K_source` | ViennaRNA duplex energy discounted by the pfl_fold opening cost on GENCODE v50 3'UTRs, anchored on the published seed-match Kd. K is never fitted to the expression response and is held fixed across doses, which is the whole point of the design. |
| `n_bootstrap` | 300 |
| `min_transcripts_required` | 100 |
| `n_constructs_fitted` | 5 |
| `AFFINITY_MODEL_FINDING` | the purely thermodynamic K used by e4, e5 and e7 does not rank off-target transcripts against the measured response in this dataset either: the Spearman correlation between -log10 K and the measured log2 fold change is within 0.06 of zero at every dose of every construct, which reproduces on MCF-... |
| `class_fit_pooled_slope_bootstrap_median` | 1.43267 |
| `class_fit_pooled_slope_frac_resamples_above_1` | 0.946667 |
| `class_fit_n_constructs_with_sane_class_ordering` | 5 |
| `class_fit_rho_median_zero_background` | 0.100909 |
| `class_fit_rho_median_bootstrap_n` | 300 |
| `class_fit_rho_per_dose_intervals_are_reported_separately_in` | per_construct[].class_fit_bootstrap.rho_ci95_per_dose_zero_background |
| `class_fit_rho_point_estimate_spread_decades` | 4.78884 |
| `RHO_IS_NOT_IDENTIFIED` | the point estimates of rho span class_fit_rho_point_estimate_spread_decades decades across construct-dose cells and the median carries a bootstrap interval of its own on top of that, so no single number here is a calibrated cellular estimate of the competition parameter. The median is reported as... |
| `class_fit_pooled_slope_all_constructs` | 1.42449 |
| `class_fit_pooled_slope_excluding_HK2_4031` | 0.633277 |
| `LOCO_NOTE` | HK2-4031 has two dose points, so its individual slope has zero residual degrees of freedom and is the line through two points. Dropping it moves the pooled exponent from class_fit_pooled_slope_all_constructs to class_fit_pooled_slope_excluding_HK2_4031, which is the sensitivity that decides wheth... |
| `pooled_slope_bootstrap_median` | 0.861086 |
| `pooled_slope_bootstrap_n` | 300 |
| `pooled_slope_frac_resamples_above_1` | 0.4 |
| `rho_data_driven_median_zero_background` | 0.198493 |
| `rho_data_driven_spread_note` | rho_data_driven_median_bootstrap_ci95 is an interval for the median rho over construct-dose cells, recomputed inside each resample. rho_data_driven_pooled_draw_spread_2p5_97p5 is the spread of the individual rho draws themselves and is a description of heterogeneity, not a confidence interval. |
| `e5_alpha_swept_band_width_decades` | 4.05436 |
| `e5_tau_0.9_contour_rho` | 0.0703872 |
| `comparison_note` | e5 could only bracket rho between 1.875e-04 and 2.125e+00, a span of 4.05 decades, because the loaded fraction alpha is unmeasured. The rho reported here uses no alpha and no Argonaute copy number: it is the total complex the fitted free pool implies through conservation, divided by the measured ... |
| `POWER_LIMITATION` | Three dose points per construct, two for HK2-4031. A slope from three points has one residual degree of freedom and from two points has none, so the per-construct interval is wide by construction and the bootstrap resamples transcripts, not doses: it propagates uncertainty in each fitted pool, an... |
| `SCALE_LIMITATION` | The molecules-per-cell scale uses the same published total mRNA count per cell as e5, which was measured in neither MCF-7 nor Hep3B. rho and the implied alpha inherit that, and they are an order-of-magnitude scale rather than a calibration. The SLOPE is invariant to it: rescaling every K and x by... |


**`constants_used`**

```json
{
  "kd_seed_match_molar": 2.6e-11,
  "kd_seed_match_molecules_per_cell": 46.972697928,
  "hela_cell_volume_litres": 3e-12,
  "anchor_site_class": "7mer-m8",
  "median_boltzmann_factor_anchor_class": 1.6317529820402435e-06,
  "K_scale_constant_C": 28786647.51650598,
  "mrna_molecules_per_cell": 80000.0,
  "ago2_copies_per_cell_low": 15000.0,
  "ago2_copies_per_cell_high": 170000.0
}
```


**`constructs`**: `["HK2-3581", "HK2-3581M", "HK2-4031", "STAT3-1676", "STAT3-1676M"]`


**`per_construct`**

| construct | status | cell_line | target_gene | doses_nM | n_transcripts_retrieved_at_every_dose | n_transcripts_strong_site_classes | total_retrieved_abundance_molecules_per_cell | background_beta_bracket_high | free_fit | loglog_slope_pool_vs_dose | constrained_independent | constrained_equilibrium | aic_free_unconstrained | aic_independent | aic_equilibrium | aic_equilibrium_minus_independent | preferred_by_aic | rho_inversion | class_fit | class_fit_n_genes | class_fit_loglog_slope_pool_vs_dose | class_fit_rho_inversion | class_fit_model_comparison | class_fit_positive_control | sensitivity | predictor_diagnostics_per_dose | bootstrap | class_fit_bootstrap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HK2-3581 | OK | Hep3B liver cancer cells | HK2 | [1.0, 10.0, 25.0] | 4633 | 2303 | 19848.6 | 14.4759 | {"pool_per_dose": [1362014.0718594096, 14107.394396129037, 1853.779012148735], "log10_pool_per_dose": [6.1341815945806735, 4.149446807951465, 3.26805796091709], "amplitude_c_log2_per_unit_bound_fraction": 0.13325186694095498, "rss": 2166.4211530811826, "n_observations": 13899, "sigma_pooled": 0.3948022929248032, "residual_sd_per_dose": [0.23169347775616775, 0.2867698136008684, 0.5760110321831216], "mean_bound_fraction_per_dose": [0.9881724513451995, 0.8979068114215828, 0.7717781016419456], "max_bound_fraction_per_dose": [0.9999999999999877, 0.9999999999988164, 0.999999999990992], "frac_sites_above_half_saturation_per_dose": [0.9926613425426289, 0.926829268292683, 0.7996978199870495], "optimiser_converged": true, "nll": -12917.315904239042} | {"slope": -2.0375759216714378, "intercept": 6.14589039557732, "n_points": 3, "residual_df": 1, "residual_rms_log10": 0.02997059237484696} | {"mode": "independent", "log10_kappa": 1.4827169904279593, "kappa_complexes_per_cell_per_nM": 30.389040674553566, "pool_per_dose": [30.389040674553566, 303.89040674553564, 759.7260168638392], "M_per_dose": [30.389040674553566, 303.89040674553564, 759.7260168638392], "amplitude_c_log2_per_unit_bound_fraction": 0.06380898035916793, "rss": 2170.721780464648, "n_observations": 13899, "sigma_pooled": 0.3951939655569076, "n_parameters": 6, "aic": -25795.067838136605, "nll": -12903.533919068303} | {"mode": "equilibrium", "log10_kappa": 2.757430460390082, "kappa_complexes_per_cell_per_nM": 572.0453509198935, "pool_per_dose": [0.002542331291601179, 7.891508108883039, 882.7079973555847], "M_per_dose": [572.0453509198935, 5720.453509198935, 14301.133772997338], "amplitude_c_log2_per_unit_bound_fraction": 0.07970853963760835, "rss": 2170.273367715517, "n_observations": 13899, "sigma_pooled": 0.39515314522544426, "n_parameters": 6, "aic": -25797.939294385502, "nll": -12904.969647192751} | -25818.6 | -25795.1 | -25797.9 | -2.87146 | equilibrium | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [1381593.04760661, 31526.265866811147, 16551.35099545795], "rho_per_dose": [17.269913095082625, 0.3940783233351393, 0.20689188744322437], "M_over_dose": [1381593.04760661, 3152.6265866811145, 662.054039818318], "loglog_slope_M_vs_dose": -1.426230302996288, "implied_alpha_loaded_fraction_low_ago2": [92.106203173774, 2.1017510577874097, 1.1034233996971967], "implied_alpha_loaded_fraction_high_ago2": [8.127017927097706, 0.18544862274594792, 0.09736088820857618]}, {"beta_case": "max_background_bracket", "beta": 14.475914636055771, "M_per_dose_molecules_per_cell": [21097992.484950155, 235743.70288234664, 43386.497729434835], "rho_per_dose": [263.72490606187694, 2.946796286029333, 0.5423312216179355], "M_over_dose": [21097992.484950155, 23574.370288234662, 1735.4599091773935], "loglog_slope_M_vs_dose": -1.927790779491703, "implied_alpha_loaded_fraction_low_ago2": [1406.5328323300103, 15.716246858823109, 2.8924331819623226], "implied_alpha_loaded_fraction_high_ago2": [124.10583814676562, 1.3867276640138038, 0.25521469252608725]}] | {"pool_per_dose": [18.741372060993957, 24.703332931480404, 39.51694199025337], "log10_pool_per_dose": [1.272801382533924, 1.3927555514823688, 1.5967833294342215], "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 62.776550775885866, "7mer-A1": 25.90427482402089, "8mer": 11.567712061295042}, "log10_K_by_class": {"7mer-m8": 1.6718455050755958, "6mer": 1.7977974499407727, "7mer-A1": 1.4133714389572694, "8mer": 1.063247469806349}, "anchor_class": "7mer-m8", "K_anchor_molecules_per_cell": 46.972697928, "class_order_by_increasing_K": ["8mer", "7mer-A1", "7mer-m8", "6mer"], "class_ordering_is_8mer_strongest": true, "expected_ordering_if_model_sane": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "amplitude_c_log2_per_unit_bound_fraction": 0.33037870086786814, "rss": 7019.693903217192, "n_observations": 51951, "sigma_pooled": 0.36758868249068766, "mean_bound_fraction_per_dose": [0.10485528108308365, 0.12075508049944085, 0.14857631495350707], "n_transcripts_with_no_site": 12684, "optimiser_converged": true, "u_hat": [1.7977974499407727, 1.4133714389572694, 1.063247469806349, 1.272801382533924, 1.3927555514823688, 1.5967833294342215], "nll": -51992.076436965384} | 17317 | {"slope": 0.2101310423641603, "intercept": 1.2528195433005114, "n_points": 3, "residual_df": 1, "residual_rms_log10": 0.051146787680100975} | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [7484.476179620041, 8661.016616931161, 10746.916680232733], "rho_per_dose": [0.09355595224525051, 0.10826270771163952, 0.13433645850290915], "M_over_dose": [7484.476179620041, 866.1016616931162, 429.8766672093093], "loglog_slope_M_vs_dose": 0.10292005787736384, "implied_alpha_loaded_fraction_low_ago2": [0.49896507864133605, 0.5774011077954108, 0.7164611120155155], "implied_alpha_loaded_fraction_high_ago2": [0.044026330468353185, 0.050947156570183304, 0.06321715694254548]}, {"beta_case": "max_background_bracket", "beta": 14.472530976780309, "M_per_dose_molecules_per_cell": [7755.711267320141, 9018.53636801173, 11318.826847294304], "rho_per_dose": [0.09694639084150176, 0.11273170460014663, 0.1414853355911788], "M_over_dose": [7755.711267320141, 901.853636801173, 452.75307389177215], "loglog_slope_M_vs_dose": 0.1073994770693043, "implied_alpha_loaded_fraction_low_ago2": [0.5170474178213428, 0.6012357578674487, 0.7545884564862869], "implied_alpha_loaded_fraction_high_ago2": [0.045621830984236125, 0.05305021392948076, 0.06658133439584885]}] | {"n_folds_completed": 5, "fold_assignment": "random over genes, one draw, shared by all three", "aic_free_unconstrained": -103962.15287393077, "n_parameters_free": 11, "aic_independent": -103779.76038908784, "aic_equilibrium": -103708.60677528603, "aic_equilibrium_minus_independent": 71.15361380181275, "aic_free_minus_best_constrained": -182.39248484293057, "preferred_by_aic": "free", "constrained_independent": {"mode": "independent", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 95.00574385373413, "7mer-A1": 7.261562247276459, "8mer": 4.290533095210999}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-A1", "7mer-m8", "6mer"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 5.426827177716979, "log10_kappa": 0.7345459912940583, "M_per_dose": [5.426827177716979, 54.268271777169794, 135.67067944292447], "pool_per_dose": [5.426827177716979, 54.268271777169794, 135.67067944292447], "amplitude_c_log2_per_unit_bound_fraction": 0.24861047354948093, "intercept_per_dose": [0.04700640010323301, 0.07118815984474132, 0.058081409648229936], "rss": 7044.924759299772, "n_observations": 51951, "sigma_pooled": 0.3682487011698209, "n_parameters": 9, "aic": -103779.76038908784, "nll": -51898.88019454392, "optimiser_converged": true, "u_hat": [1.9777498626422494, 0.8610300645544944, 0.6325112562697514, 0.7345459912940583]}, "constrained_equilibrium": {"mode": "equilibrium", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 31.392092061328142, "7mer-A1": 13.815359477167902, "8mer": 6.8848390005098725}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-A1", "6mer", "7mer-m8"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 14991.401151021219, "log10_kappa": 4.175842225491312, "M_per_dose": [14991.401151021219, 149914.01151021218, 374785.02877553046], "pool_per_dose": [63.910608236124844, 130068.96497778504, 354937.75456037524], "amplitude_c_log2_per_unit_bound_fraction": 0.16963211081838728, "intercept_per_dose": [0.06469398897917918, 0.074602695482442, 0.05155352250731862], "rss": 7054.580305693126, "n_observations": 51951, "sigma_pooled": 0.3685009696511662, "n_parameters": 9, "aic": -103708.60677528603, "nll": -51863.30338764301, "optimiser_converged": true, "u_hat": [1.4968202593258797, 1.1403621897895737, 0.8378937888910273, 4.175842225491312]}, "heldout_gene_rmse_free": 0.3677136813882775, "heldout_gene_n_free": 51951, "heldout_gene_rmse_independent": 0.3683610512135489, "heldout_gene_n_independent": 51951, "heldout_gene_rmse_equilibrium": 0.3685491324065939, "heldout_gene_n_equilibrium": 51951, "preferred_by_heldout_gene_rmse": "free", "heldout_rmse_equilibrium_minus_independent": 0.00018808119304503101} | [{"dose_nM": 1.0, "n_no_site": 12684, "median_log2fc_no_site": 0.06082371716666746, "n_6mer": 1990, "median_log2fc_6mer": -0.043067454000000005, "delta_vs_no_site_6mer": -0.10389117116666746, "mann_whitney_p_less_6mer": 3.8913719218998414e-94, "n_7mer-A1": 1153, "median_log2fc_7mer-A1": -0.06263817366666657, "delta_vs_no_site_7mer-A1": -0.12346189083333403, "mann_whitney_p_less_7mer-A1": 1.440985345271512e-87, "n_7mer-m8": 1079, "median_log2fc_7mer-m8": -0.0409073536666682, "delta_vs_no_site_7mer-m8": -0.10173107083333566, "mann_whitney_p_less_7mer-m8": 2.8376883913587258e-64, "n_8mer": 411, "median_log2fc_8mer": -0.05735351599999916, "delta_vs_no_site_8mer": -0.11817723316666662, "mann_whitney_p_less_8mer": 1.8392818304084716e-31}, {"dose_nM": 10.0, "n_no_site": 12684, "median_log2fc_no_site": 0.05701725183333339, "n_6mer": 1990, "median_log2fc_6mer": -0.028397827000000042, "delta_vs_no_site_6mer": -0.08541507883333344, "mann_whitney_p_less_6mer": 9.338178099722835e-64, "n_7mer-A1": 1153, "median_log2fc_7mer-A1": -0.08347233333333381, "delta_vs_no_site_7mer-A1": -0.1404895851666672, "mann_whitney_p_less_7mer-A1": 1.7147060335071731e-81, "n_7mer-m8": 1079, "median_log2fc_7mer-m8": -0.05492269599999933, "delta_vs_no_site_7mer-m8": -0.11193994783333272, "mann_whitney_p_less_7mer-m8": 9.348653665647162e-60, "n_8mer": 411, "median_log2fc_8mer": -0.09214667366666873, "delta_vs_no_site_8mer": -0.14916392550000213, "mann_whitney_p_less_8mer": 1.1647863347965564e-39}, {"dose_nM": 25.0, "n_no_site": 12684, "median_log2fc_no_site": 0.07345981016666725, "n_6mer": 1990, "median_log2fc_6mer": 0.020030425833332366, "delta_vs_no_site_6mer": -0.053429384333334884, "mann_whitney_p_less_6mer": 1.5263277906215485e-17, "n_7mer-A1": 1153, "median_log2fc_7mer-A1": -0.06502325599999992, "delta_vs_no_site_7mer-A1": -0.13848306616666717, "mann_whitney_p_less_7mer-A1": 2.8848179469658643e-48, "n_7mer-m8": 1079, "median_log2fc_7mer-m8": -0.037803111333333916, "delta_vs_no_site_7mer-m8": -0.11126292150000117, "mann_whitney_p_less_7mer-m8": 1.4548459079229682e-31, "n_8mer": 411, "median_log2fc_8mer": -0.10200930199999991, "delta_vs_no_site_8mer": -0.17546911216666716, "mann_whitney_p_less_8mer": 1.6695591415099488e-32}] | {"strong_sites_only": {"n_transcripts": 2303, "site_classes": ["7mer-m8", "8mer", "7mer-A1"], "pool_per_dose": [318038.4642660791, 1390.7724645647825, 314.8027228961755], "slope": -2.1898176309268913, "amplitude_c": 0.09129990676274354}, "excluding_top_dose": {"doses": [1.0, 10.0], "pool_per_dose": [651466.0306526441, 712.7940884966501], "slope": -2.9609276859967713}} | [{"dose_nM": 1.0, "spearman_minus_log10K_vs_log2fc": -0.013521109361371185, "p": 0.35750822562852796, "median_log2fc": -0.049188565333333045, "mean_log2fc": -0.06612996625030579}, {"dose_nM": 10.0, "spearman_minus_log10K_vs_log2fc": -0.06067136010943972, "p": 3.5906029299063655e-05, "median_log2fc": -0.050602626999999956, "mean_log2fc": -0.07916042065450754}, {"dose_nM": 25.0, "spearman_minus_log10K_vs_log2fc": -0.07885012579077694, "p": 7.703275716051047e-08, "median_log2fc": -0.02383503366666684, "mean_log2fc": -0.1318229123405281}] | {"n_resamples": 300, "n_successful": 300, "slope_ci95": [-4.106845718734523, -1.1032295066981115], "slope_median": -2.120240586439105, "slope_sd": 0.776682619389462, "M_vs_dose_slope_ci95": [-3.0006813761349513, -0.9532579032784368], "aic_equilibrium_minus_independent_ci95": [-15.044210673867473, 9.410968820738578], "frac_resamples_preferring_equilibrium": 0.7033333333333334, "frac_resamples_slope_above_1": 0.0, "pool_ci95_per_dose": [[440707.53011537966, 100000000.0], [232.73133744560172, 836579.4506400689], [183.98493480588857, 44716.51060524447]], "rho_ci95_per_dose_zero_background": [[5.7537922735167015, 1250.2554682254247], [0.13660802371549818, 10.692801149006938], [0.13110842221101843, 0.7888170216115226]], "rho_ci95_per_dose_max_background": [[85.49934959123186, 19345.148763295136], [0.18025094930458288, 162.07096007080779], [0.16388954153177232, 8.880221900909042]], "rho_median_per_dose_zero_background": [24.764345928304063, 0.4868753963385425, 0.21175286560506557]} | {"n_successful": 300, "slope_ci95": [0.12769673781546753, 0.2723893016155588], "slope_median": 0.21135525493121726, "frac_resamples_slope_above_1": 0.0, "M_vs_dose_slope_ci95": [0.05754863924707973, 0.14098123205342034], "pool_ci95_per_dose": [[11.230275559587842, 30.45149550879661], [14.954132480824017, 38.432191156596396], [24.190748626273503, 57.73740204733447]], "rho_ci95_per_dose_zero_background": [[0.06994263105354216, 0.11917672446391764], [0.0829147622536947, 0.1322094243089307], [0.10589462577968248, 0.1554239234504929]], "rho_median_per_dose_zero_background": [0.09236838189776428, 0.10742729682368195, 0.13373445261418576]} |
| HK2-3581M | OK | Hep3B liver cancer cells | HK2 | [1.0, 10.0, 25.0] | 4633 | 2303 | 19848.6 | 14.4759 | {"pool_per_dose": [1e-08, 3.136550378709291e-06, 8823.648190059212], "log10_pool_per_dose": [-8.0, -5.503547732510597, 3.945648183910617], "amplitude_c_log2_per_unit_bound_fraction": 0.08103740472520893, "rss": 851.5524674432666, "n_observations": 13899, "sigma_pooled": 0.2475220700309454, "residual_sd_per_dose": [0.12220461788734223, 0.16080520070924106, 0.37821809192845957], "mean_bound_fraction_per_dose": [0.00011783511760966757, 0.0027833112870567353, 0.8746789494537576], "max_bound_fraction_per_dose": [0.3745496813504942, 0.9947042789000687, 0.9999999999981075], "frac_sites_above_half_saturation_per_dose": [0.0, 0.0019425857975393912, 0.9043816101877833], "optimiser_converged": true, "nll": -19406.55559905487} | {"slope": 7.37519118320302, "intercept": -9.081055186135917, "n_points": 3, "residual_df": 1, "residual_rms_log10": 2.76713767085612} | {"mode": "independent", "log10_kappa": 2.2099851534233204, "kappa_complexes_per_cell_per_nM": 162.1754655907534, "pool_per_dose": [162.1754655907534, 1621.754655907534, 4054.386639768835], "M_per_dose": [162.1754655907534, 1621.754655907534, 4054.386639768835], "amplitude_c_log2_per_unit_bound_fraction": 0.02109605141618845, "rss": 852.6194251258539, "n_observations": 13899, "sigma_pooled": 0.2476770886064775, "n_parameters": 6, "aic": -38783.70726505275, "nll": -19397.853632526374} | {"mode": "equilibrium", "log10_kappa": 2.8129452605757024, "kappa_complexes_per_cell_per_nM": 650.047751742054, "pool_per_dose": [0.0035565252311621845, 14.137176413921281, 1698.540378749603], "M_per_dose": [650.047751742054, 6500.47751742054, 16251.193793551349], "amplitude_c_log2_per_unit_bound_fraction": 0.023662367151615078, "rss": 852.5743939363565, "n_observations": 13899, "sigma_pooled": 0.24767054797366364, "n_parameters": 6, "aic": -38784.44136166508, "nll": -19398.22068083254} | -38797.1 | -38783.7 | -38784.4 | -0.734097 | equilibrium | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [2.3889315382599046, 38.130427180557945, 25730.927982398556], "rho_per_dose": [2.9861644228248805e-05, 0.0004766303397569743, 0.32163659977998194], "M_over_dose": [2.3889315382599046, 3.8130427180557946, 1029.2371192959422], "loglog_slope_M_vs_dose": 2.5592040644531915, "implied_alpha_loaded_fraction_low_ago2": [0.0001592621025506603, 0.002542028478703863, 1.7153951988265703], "implied_alpha_loaded_fraction_high_ago2": [1.405253846035238e-05, 0.00022429663047387026, 0.1513583998964621]}, {"beta_case": "max_background_bracket", "beta": 14.475914636055771, "M_per_dose_molecules_per_cell": [2.388931683019051, 38.130472584993484, 153461.3059602837], "rho_per_dose": [2.9861646037738138e-05, 0.0004766309073124185, 1.9182663245035463], "M_over_dose": [2.388931683019051, 3.8130472584993482, 6138.452238411348], "loglog_slope_M_vs_dose": 3.006671314781706, "implied_alpha_loaded_fraction_low_ago2": [0.00015926211220127008, 0.002542031505666232, 10.23075373068558], "implied_alpha_loaded_fraction_high_ago2": [1.405253931187677e-05, 0.0002242968975587852, 0.902713564472257]}] | {"pool_per_dose": [0.43702459487775863, 1.1757895663766589, 24.51321827675239], "log10_pool_per_dose": [-0.35949412110938717, 0.07032960206402752, 1.3894003323896507], "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 48.72205803022983, "7mer-A1": 15.685260945989835, "8mer": 4.004857973146086}, "log10_K_by_class": {"7mer-m8": 1.6718455050755958, "6mer": 1.6877256247047692, "7mer-A1": 1.1954917481826817, "8mer": 0.6025871190288334}, "anchor_class": "7mer-m8", "K_anchor_molecules_per_cell": 46.972697928, "class_order_by_increasing_K": ["8mer", "7mer-A1", "7mer-m8", "6mer"], "class_ordering_is_8mer_strongest": true, "expected_ordering_if_model_sane": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "amplitude_c_log2_per_unit_bound_fraction": 0.22595805490439302, "rss": 2837.2695934022718, "n_observations": 51951, "sigma_pooled": 0.23369711232529422, "mean_bound_fraction_per_dose": [0.008211538268683611, 0.019848318600702117, 0.1386444614847108], "n_transcripts_with_no_site": 12684, "optimiser_converged": true, "u_hat": [1.6877256247047692, 1.1954917481826817, 0.6025871190288334, -0.35949412110938717, 0.07032960206402757, 1.3894003323896507], "nll": -75522.69573965776} | 17317 | {"slope": 1.0922034440709896, "intercept": -0.5062675076009754, "n_points": 3, "residual_df": 1, "residual_rms_log10": 0.3756905031756024} | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [557.1708277841271, 1356.5203808694184, 9977.495738479189], "rho_per_dose": [0.00696463534730159, 0.01695650476086773, 0.12471869673098986], "M_over_dose": [557.1708277841271, 135.65203808694184, 399.09982953916756], "loglog_slope_M_vs_dose": 0.7977131820687425, "implied_alpha_loaded_fraction_low_ago2": [0.037144721852275145, 0.09043469205796123, 0.6651663825652793], "implied_alpha_loaded_fraction_high_ago2": [0.003277475457553689, 0.00797953165217305, 0.058691151402818754]}, {"beta_case": "max_background_bracket", "beta": 14.472530976780309, "M_per_dose_molecules_per_cell": [563.4956797711103, 1373.5370317909799, 10332.264049330066], "rho_per_dose": [0.007043695997138878, 0.017169212897387248, 0.12915330061662583], "M_over_dose": [563.4956797711103, 137.35370317909798, 413.2905619732026], "loglog_slope_M_vs_dose": 0.8037386852356916, "implied_alpha_loaded_fraction_low_ago2": [0.037566378651407356, 0.09156913545273199, 0.688817603288671], "implied_alpha_loaded_fraction_high_ago2": [0.0033146804692418255, 0.00807962959877047, 0.06077802381958863]}] | {"n_folds_completed": 5, "fold_assignment": "random over genes, one draw, shared by all three", "aic_free_unconstrained": -151023.39147931553, "n_parameters_free": 11, "aic_independent": -150895.5532560146, "aic_equilibrium": -150962.7995769724, "aic_equilibrium_minus_independent": -67.24632095781271, "aic_free_minus_best_constrained": -60.59190234311973, "preferred_by_aic": "free", "constrained_independent": {"mode": "independent", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 48.287152957468955, "7mer-A1": 24.181229241182525, "8mer": 9.582459170676469}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-A1", "7mer-m8", "6mer"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 0.4860962927429798, "log10_kappa": -0.3132776910986865, "M_per_dose": [0.4860962927429798, 4.860962927429798, 12.152407318574495], "pool_per_dose": [0.4860962927429798, 4.860962927429798, 12.152407318574495], "amplitude_c_log2_per_unit_bound_fraction": 0.2761189924688985, "intercept_per_dose": [0.009955676378724052, 0.02512403834764528, 0.06134758625985738], "rss": 2844.4789949259957, "n_observations": 51951, "sigma_pooled": 0.2339938319980662, "n_parameters": 9, "aic": -150895.5532560146, "nll": -75456.7766280073, "optimiser_converged": true, "u_hat": [1.6838315998648037, 1.3834783742374577, 0.9814769774711134, -0.3132776910986865]}, "constrained_equilibrium": {"mode": "equilibrium", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 48.0550298548239, "7mer-A1": 18.808620667651947, "8mer": 6.547022645839033}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-A1", "7mer-m8", "6mer"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 372.62996281134093, "log10_kappa": 2.5712777731593786, "M_per_dose": [372.62996281134093, 3726.299628113409, 9315.749070283524], "pool_per_dose": [0.339007682093161, 4.819238338677167, 22.288772822152374], "amplitude_c_log2_per_unit_bound_fraction": 0.21657750169664539, "intercept_per_dose": [0.009333137925716228, 0.02325236918687392, 0.06462963778461206], "rss": 2840.799431448746, "n_observations": 51951, "sigma_pooled": 0.23384243805534355, "n_parameters": 9, "aic": -150962.7995769724, "nll": -75490.3997884862, "optimiser_converged": true, "u_hat": [1.6817388513983147, 1.2743569476826417, 0.8160438431284913, 2.5712777731593786]}, "heldout_gene_rmse_free": 0.2337785589597959, "heldout_gene_n_free": 51951, "heldout_gene_rmse_independent": 0.23406504185791022, "heldout_gene_n_independent": 51951, "heldout_gene_rmse_equilibrium": 0.23392030866755242, "heldout_gene_n_equilibrium": 51951, "preferred_by_heldout_gene_rmse": "free", "heldout_rmse_equilibrium_minus_independent": -0.00014473319035779308} | [{"dose_nM": 1.0, "n_no_site": 12684, "median_log2fc_no_site": -0.0025016609999986006, "n_6mer": 1990, "median_log2fc_6mer": -0.01640478333333295, "delta_vs_no_site_6mer": -0.01390312233333435, "mann_whitney_p_less_6mer": 2.878135196825848e-06, "n_7mer-A1": 1153, "median_log2fc_7mer-A1": -0.02273242000000053, "delta_vs_no_site_7mer-A1": -0.02023075900000193, "mann_whitney_p_less_7mer-A1": 4.6048400976313543e-07, "n_7mer-m8": 1079, "median_log2fc_7mer-m8": -0.01008533333333439, "delta_vs_no_site_7mer-m8": -0.007583672333335789, "mann_whitney_p_less_7mer-m8": 0.012453721869337103, "n_8mer": 411, "median_log2fc_8mer": -0.022325276666666838, "delta_vs_no_site_8mer": -0.019823615666668237, "mann_whitney_p_less_8mer": 0.004022451569739675}, {"dose_nM": 10.0, "n_no_site": 12684, "median_log2fc_no_site": 0.009504234, "n_6mer": 1990, "median_log2fc_6mer": -0.009488421499999511, "delta_vs_no_site_6mer": -0.01899265549999951, "mann_whitney_p_less_6mer": 1.0240225092750067e-06, "n_7mer-A1": 1153, "median_log2fc_7mer-A1": -0.0146259183333326, "delta_vs_no_site_7mer-A1": -0.0241301523333326, "mann_whitney_p_less_7mer-A1": 8.759708730631786e-08, "n_7mer-m8": 1079, "median_log2fc_7mer-m8": -0.0075689800000002805, "delta_vs_no_site_7mer-m8": -0.01707321400000028, "mann_whitney_p_less_7mer-m8": 9.196796481213242e-05, "n_8mer": 411, "median_log2fc_8mer": -0.024521389999998533, "delta_vs_no_site_8mer": -0.03402562399999853, "mann_whitney_p_less_8mer": 1.223579611855424e-08}, {"dose_nM": 25.0, "n_no_site": 12684, "median_log2fc_no_site": 0.11120118833333281, "n_6mer": 1990, "median_log2fc_6mer": 0.030597857000000284, "delta_vs_no_site_6mer": -0.08060333133333253, "mann_whitney_p_less_6mer": 2.585146035245444e-26, "n_7mer-A1": 1153, "median_log2fc_7mer-A1": -0.015518546999999216, "delta_vs_no_site_7mer-A1": -0.12671973533333203, "mann_whitney_p_less_7mer-A1": 3.778246299121674e-41, "n_7mer-m8": 1079, "median_log2fc_7mer-m8": 0.03297090833333316, "delta_vs_no_site_7mer-m8": -0.07823027999999965, "mann_whitney_p_less_7mer-m8": 1.3025179765403472e-20, "n_8mer": 411, "median_log2fc_8mer": -0.058427665666666684, "delta_vs_no_site_8mer": -0.1696288539999995, "mann_whitney_p_less_8mer": 7.987594683059039e-23}] | {"strong_sites_only": {"n_transcripts": 2303, "site_classes": ["7mer-m8", "8mer", "7mer-A1"], "pool_per_dose": [19194.528522552388, 0.09780444010962959, 6637.853904873605], "slope": -1.2898457159867387, "amplitude_c": 0.041736234453165794}, "excluding_top_dose": {"doses": [1.0, 10.0], "pool_per_dose": [6969.24875582592, 778.4422033767701], "slope": -0.9519595929729743}} | [{"dose_nM": 1.0, "spearman_minus_log10K_vs_log2fc": -0.01922126471886661, "p": 0.19084441918362136, "median_log2fc": -0.01730557133333477, "mean_log2fc": -0.0031371042867112623}, {"dose_nM": 10.0, "spearman_minus_log10K_vs_log2fc": -0.025052986889380745, "p": 0.08818180266631992, "median_log2fc": -0.012215314000000532, "mean_log2fc": -0.005706864417799838}, {"dose_nM": 25.0, "spearman_minus_log10K_vs_log2fc": -0.03499741367705887, "p": 0.017208335483711062, "median_log2fc": 0.015732408666667475, "mean_log2fc": -0.04942353661011583}] | {"n_resamples": 300, "n_successful": 300, "slope_ci95": [5.712358617024579, 7.872613259096178], "slope_median": 7.0529987916622305, "slope_sd": 0.627422620006426, "M_vs_dose_slope_ci95": [1.810229772567726, 3.4305636051778357], "aic_equilibrium_minus_independent_ci95": [-10.661597337165222, 5.160221842790995], "frac_resamples_preferring_equilibrium": 0.55, "frac_resamples_slope_above_1": 1.0, "pool_ci95_per_dose": [[1e-08, 1.307892991714921e-06], [1e-08, 0.004265220382864401], [315.29248652687113, 108738.88304170626]], "rho_ci95_per_dose_zero_background": [[1.9596630472564735e-06, 0.00031230050395426813], [2.8701582022824235e-05, 0.009134014191731486], [0.14776236684795946, 1.5925139534636612]], "rho_ci95_per_dose_max_background": [[1.959664856745803e-06, 0.00031230061521341217], [2.8701583832313568e-05, 0.009134785978808565], [0.20354053431798796, 21.267603822747937]], "rho_median_per_dose_zero_background": [5.498324738051806e-05, 0.00046225868121014705, 0.32937234146894123]} | {"n_successful": 300, "slope_ci95": [0.8703855732107202, 1.406434323845668], "slope_median": 1.0840212031800127, "frac_resamples_slope_above_1": 0.7833333333333333, "M_vs_dose_slope_ci95": [0.6560871180954891, 1.0110749177618108], "pool_ci95_per_dose": [[0.13694060611404613, 0.8986915830044313], [0.4818717610447945, 2.16698920358363], [11.391304653414828, 48.4790374708787]], "rho_ci95_per_dose_zero_background": [[0.003625573227505375, 0.01026656081481128], [0.011970664424736877, 0.021937158118429757], [0.08997684573075605, 0.15484642934692838]], "rho_median_per_dose_zero_background": [0.006777905419328131, 0.016294925056663984, 0.12321064573962023]} |
| HK2-4031 | OK | Hep3B liver cancer cells | HK2 | [1.0, 10.0] | 5625 | 3335 | 24228.2 | 13.4219 | {"pool_per_dose": [0.04342524986326507, 1274.5817644820884], "log10_pool_per_dose": [-1.3622576739994576, 3.1053677007110396], "amplitude_c_log2_per_unit_bound_fraction": 0.009678560180496358, "rss": 283.77935353217356, "n_observations": 11250, "sigma_pooled": 0.1588232710438936, "residual_sd_per_dose": [0.10622192417401123, 0.19792810840966463], "mean_bound_fraction_per_dose": [0.06219385066527031, 0.5998599211666877], "max_bound_fraction_per_dose": [0.99999978840889, 0.9999999999927911], "frac_sites_above_half_saturation_per_dose": [0.05262222222222222, 0.6053333333333333], "optimiser_converged": true, "nll": -20699.585975339167} | {"slope": 4.467625374710498, "intercept": -1.3622576739994579, "n_points": 2, "residual_df": 0, "residual_rms_log10": 6.473657049138938e-16} | {"mode": "independent", "log10_kappa": 1.2632624893977473, "kappa_complexes_per_cell_per_nM": 18.334222156004657, "pool_per_dose": [18.334222156004657, 183.34222156004657], "M_per_dose": [18.334222156004657, 183.34222156004657], "amplitude_c_log2_per_unit_bound_fraction": 0.004377947882530052, "rss": 283.8529958791722, "n_observations": 11250, "sigma_pooled": 0.15884387747559545, "n_parameters": 5, "aic": -41386.252890800075, "nll": -20698.126445400037} | {"mode": "equilibrium", "log10_kappa": 3.189514593120865, "kappa_complexes_per_cell_per_nM": 1547.0864881239631, "pool_per_dose": [0.058773413451020065, 1232.1269075244995], "M_per_dose": [1547.0864881239631, 15470.864881239631], "amplitude_c_log2_per_unit_bound_fraction": 0.009583297372803591, "rss": 283.77951890838176, "n_observations": 11250, "sigma_pooled": 0.15882331732207802, "n_parameters": 5, "aic": -41389.16539459249, "nll": -20699.582697296246} | -41387.2 | -41386.3 | -41389.2 | -2.9125 | equilibrium | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [1403.7793680419002, 15576.988798750768], "rho_per_dose": [0.017547242100523754, 0.1947123599843846], "M_over_dose": [1403.7793680419002, 1557.6988798750767], "loglog_slope_M_vs_dose": 1.045184652498632, "implied_alpha_loaded_fraction_low_ago2": [0.09358529120279334, 1.0384659199167179], "implied_alpha_loaded_fraction_high_ago2": [0.008257525694364118, 0.09162934587500451]}, {"beta_case": "max_background_bracket", "beta": 13.421913796517398, "M_per_dose_molecules_per_cell": [1404.362218002157, 32684.315368242398], "rho_per_dose": [0.017554527725026962, 0.40855394210303], "M_over_dose": [1404.362218002157, 3268.4315368242396], "loglog_slope_M_vs_dose": 1.366860255328724, "implied_alpha_loaded_fraction_low_ago2": [0.09362414786681048, 2.1789543578828265], "implied_alpha_loaded_fraction_high_ago2": [0.0082609542235421, 0.19226067863672]}] | {"pool_per_dose": [1e-06, 98.11754308416498], "log10_pool_per_dose": [-6.0, 1.9917466647040487], "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 363.0355401040396, "7mer-A1": 206.93953362548413, "8mer": 0.019565428030965077}, "log10_K_by_class": {"7mer-m8": 1.6718455050755958, "6mer": 2.5599491432607184, "7mer-A1": 2.3158434659933897, "8mer": -1.7085106466412547}, "anchor_class": "7mer-m8", "K_anchor_molecules_per_cell": 46.972697928, "class_order_by_increasing_K": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "class_ordering_is_8mer_strongest": true, "expected_ordering_if_model_sane": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "amplitude_c_log2_per_unit_bound_fraction": 0.01863275775708437, "rss": 873.7179230220335, "n_observations": 34634, "sigma_pooled": 0.15883064372208408, "mean_bound_fraction_per_dose": [2.5309733540081117e-06, 0.17604436885854563], "n_transcripts_with_no_site": 11692, "optimiser_converged": true, "u_hat": [2.5599491432607184, 2.3158434659933897, -1.7085106466412547, -6.000012379081448, 1.9917466647040487], "nll": -63723.67769768298} | 17317 | {"slope": 7.991746664704048, "intercept": -5.999999999999999, "n_points": 2, "residual_df": 0, "residual_rms_log10": 7.021666937153402e-16} | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [0.21734681021382404, 13365.83725518274], "rho_per_dose": [2.7168351276728004e-06, 0.16707296568978425], "M_over_dose": [0.21734681021382404, 1336.583725518274], "loglog_slope_M_vs_dose": 4.788842897913792, "implied_alpha_loaded_fraction_low_ago2": [1.448978734758827e-05, 0.8910558170121826], "implied_alpha_loaded_fraction_high_ago2": [1.278510648316612e-06, 0.07862257208931023]}, {"beta_case": "max_background_bracket", "beta": 13.418530137241934, "M_per_dose_molecules_per_cell": [0.2173602287439613, 14682.430464049741], "rho_per_dose": [2.7170028592995162e-06, 0.18353038080062176], "M_over_dose": [0.2173602287439613, 1468.2430464049742], "loglog_slope_M_vs_dose": 4.829617870252682, "implied_alpha_loaded_fraction_low_ago2": [1.4490681916264087e-05, 0.978828697603316], "implied_alpha_loaded_fraction_high_ago2": [1.2785895808468312e-06, 0.08636723802382201]}] | {"n_folds_completed": 5, "fold_assignment": "random over genes, one draw, shared by all three", "aic_free_unconstrained": -127429.35539536596, "n_parameters_free": 9, "aic_independent": -127425.89595059589, "aic_equilibrium": -127427.7785291199, "aic_equilibrium_minus_independent": -1.8825785240042023, "aic_free_minus_best_constrained": -1.5768662460613996, "preferred_by_aic": "free", "constrained_independent": {"mode": "independent", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 1000000000000.0, "7mer-A1": 83.21911299431446, "8mer": 20.539746945046023}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 0.4151776001775086, "log10_kappa": -0.38176608575142545, "M_per_dose": [0.4151776001775086, 4.151776001775086], "pool_per_dose": [0.4151776001775086, 4.151776001775086], "amplitude_c_log2_per_unit_bound_fraction": 0.08482414598598792, "intercept_per_dose": [0.0017983399431290396, 0.011483305596028774], "rss": 873.8556602374819, "n_observations": 34634, "sigma_pooled": 0.15884316265290283, "n_parameters": 8, "aic": -127425.89595059589, "nll": -63720.947975297946, "optimiser_converged": true, "u_hat": [12.00781327850078, 1.920223082476784, 1.312595088674739, -0.38176608575142545]}, "constrained_equilibrium": {"mode": "equilibrium", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 368.32822137352457, "7mer-A1": 144.9045754282642, "8mer": 7.657747228445273}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 1104.257651674977, "log10_kappa": 3.043070417274967, "M_per_dose": [1104.257651674977, 11042.57651674977], "pool_per_dose": [1.4279696632560879, 56.70541902386674], "amplitude_c_log2_per_unit_bound_fraction": 0.019490937317802347, "intercept_per_dose": [0.0018254923572729722, 0.012219986573296548], "rss": 873.8081619066807, "n_observations": 34634, "sigma_pooled": 0.15883884564269432, "n_parameters": 8, "aic": -127427.7785291199, "nll": -63721.88926455995, "optimiser_converged": true, "u_hat": [2.566234995849858, 2.1610820987346364, 0.8841010267931813, 3.043070417274967]}, "heldout_gene_rmse_free": 0.15885645085307148, "heldout_gene_n_free": 34634, "heldout_gene_rmse_independent": 0.1588734550500629, "heldout_gene_n_independent": 34634, "heldout_gene_rmse_equilibrium": 0.15887127654214273, "heldout_gene_n_equilibrium": 34634, "preferred_by_heldout_gene_rmse": "free", "heldout_rmse_equilibrium_minus_independent": -2.1785079201697144e-06} | [{"dose_nM": 1.0, "n_no_site": 11692, "median_log2fc_no_site": 0.0008171302500001865, "n_6mer": 1842, "median_log2fc_6mer": 0.0007840617500001201, "delta_vs_no_site_6mer": -3.3068500000066336e-05, "mann_whitney_p_less_6mer": 0.6079294439680893, "n_7mer-A1": 989, "median_log2fc_7mer-A1": 0.0012853234999994356, "delta_vs_no_site_7mer-A1": 0.00046819324999924916, "mann_whitney_p_less_7mer-A1": 0.3715885930834324, "n_7mer-m8": 1992, "median_log2fc_7mer-m8": 0.007158049249998966, "delta_vs_no_site_7mer-m8": 0.006340918999998779, "mann_whitney_p_less_7mer-m8": 0.999781745925409, "n_8mer": 802, "median_log2fc_8mer": 0.009677396999999921, "delta_vs_no_site_8mer": 0.008860266749999735, "mann_whitney_p_less_8mer": 0.995050840097744}, {"dose_nM": 10.0, "n_no_site": 11692, "median_log2fc_no_site": 0.015947320499999584, "n_6mer": 1842, "median_log2fc_6mer": 0.014805095749998998, "delta_vs_no_site_6mer": -0.0011422247500005867, "mann_whitney_p_less_6mer": 0.11323805857596991, "n_7mer-A1": 989, "median_log2fc_7mer-A1": 0.00856633499999937, "delta_vs_no_site_7mer-A1": -0.0073809855000002145, "mann_whitney_p_less_7mer-A1": 0.23494490253601963, "n_7mer-m8": 1992, "median_log2fc_7mer-m8": 0.0037176940000001046, "delta_vs_no_site_7mer-m8": -0.01222962649999948, "mann_whitney_p_less_7mer-m8": 0.0010073995723993833, "n_8mer": 802, "median_log2fc_8mer": -0.0014507995000010432, "delta_vs_no_site_8mer": -0.017398120000000628, "mann_whitney_p_less_8mer": 0.0002905126710483712}] | {"strong_sites_only": {"n_transcripts": 3335, "site_classes": ["7mer-m8", "8mer", "7mer-A1"], "pool_per_dose": [100000000.0, 273205.2749387925], "slope": -2.563510919724422, "amplitude_c": -0.02868616161416865}} | [{"dose_nM": 1.0, "spearman_minus_log10K_vs_log2fc": 0.010102713660103395, "p": 0.44871775186509955, "median_log2fc": 0.0044785145000005855, "mean_log2fc": 0.004914605945066677}, {"dose_nM": 10.0, "spearman_minus_log10K_vs_log2fc": -0.015306256751309543, "p": 0.2510588351560192, "median_log2fc": 0.0073334789999996985, "mean_log2fc": 0.0022965770043555647}] | {"n_resamples": 300, "n_successful": 300, "slope_ci95": [1.9735973129410713, 11.138609484128708], "slope_median": 4.5755521171203055, "slope_sd": 2.077849477514159, "M_vs_dose_slope_ci95": [0.43751766848515666, 4.007901051544073], "aic_equilibrium_minus_independent_ci95": [-8.430763380395728, 2.0007662662223], "frac_resamples_preferring_equilibrium": 0.7633333333333333, "frac_resamples_slope_above_1": 0.98, "pool_ci95_per_dose": [[1e-08, 1.1318009087371876], [12.15274906894001, 6458892.554852731]], "rho_ci95_per_dose_zero_background": [[4.37713152361982e-05, 0.04649048585804026], [0.0797769629182212, 81.03342716327376]], "rho_ci95_per_dose_max_background": [[4.377131691393742e-05, 0.046680807804248714], [0.08181587729814645, 1164.667165815791]], "rho_median_per_dose_zero_background": [0.015985445079885488, 0.19924721268928308]} | {"n_successful": 300, "slope_ci95": [3.6989425268560274, 17.999698417120104], "slope_median": 7.949356468575791, "frac_resamples_slope_above_1": 1.0, "M_vs_dose_slope_ci95": [1.6655013695481364, 15.512641049466062], "pool_ci95_per_dose": [[1e-06, 1.0000230545117232e-06], [0.005000798662520192, 999305820823.489]], "rho_ci95_per_dose_zero_background": [[3.1690402458381385e-09, 0.01063893712383297], [3.153552798861944e-05, 12491323.035956712]], "rho_median_per_dose_zero_background": [1.4675483004794408e-06, 0.16702742541702734]} |
| STAT3-1676 | OK | MCF-7 breast cancer cells | STAT3 | [1.0, 10.0, 25.0] | 5091 | 2744 | 20257.7 | 14.3775 | {"pool_per_dose": [273.1748205036085, 5.9297508998186235, 146.82428800777], "log10_pool_per_dose": [2.4364406663846854, 0.7730364496700834, 2.166797903504122], "amplitude_c_log2_per_unit_bound_fraction": 0.04937274280844569, "rss": 1031.8130776979742, "n_observations": 15273, "sigma_pooled": 0.25991918593789765, "residual_sd_per_dose": [0.14183448071530952, 0.27234495553233373, 0.32927947551727743], "mean_bound_fraction_per_dose": [0.8385462626147107, 0.5695270352827226, 0.8041048890245601], "max_bound_fraction_per_dose": [0.9999999999822152, 0.9999999991806816, 0.9999999999669105], "frac_sites_above_half_saturation_per_dose": [0.8601453545472403, 0.5698291101944608, 0.8241995678648596], "optimiser_converged": true, "nll": -20578.603767819743} | {"slope": -0.4773240214422081, "intercept": 2.1736231292251293, "n_points": 3, "residual_df": 1, "residual_rms_log10": 0.672724498214833} | {"mode": "independent", "log10_kappa": 0.015379117313326408, "kappa_complexes_per_cell_per_nM": 1.0360461884289134, "pool_per_dose": [1.0360461884289134, 10.360461884289133, 25.901154710722835], "M_per_dose": [1.0360461884289134, 10.360461884289133, 25.901154710722835], "amplitude_c_log2_per_unit_bound_fraction": 0.04091988992794852, "rss": 1032.1510925999028, "n_observations": 15273, "sigma_pooled": 0.25996175632487933, "n_parameters": 6, "aic": -41140.205024726165, "nll": -20576.102512363082} | {"mode": "equilibrium", "log10_kappa": 2.8360828637412663, "kappa_complexes_per_cell_per_nM": 685.6190306435849, "pool_per_dose": [0.0001609539881614913, 0.3229397186819649, 292.65077268662753], "M_per_dose": [685.6190306435849, 6856.1903064358485, 17140.47576608962], "amplitude_c_log2_per_unit_bound_fraction": 0.05237074800478022, "rss": 1032.446516015009, "n_observations": 15273, "sigma_pooled": 0.25999895693234315, "n_parameters": 6, "aic": -41135.83419543635, "nll": -20573.917097718175} | -41141.2 | -41140.2 | -41135.8 | 4.37083 | independent | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [17045.348210335673, 11250.508624916694, 16181.876825853404], "rho_per_dose": [0.21306685262919592, 0.1406313578114587, 0.20227346032316754], "M_over_dose": [17045.348210335673, 1125.0508624916695, 647.2750730341362], "loglog_slope_M_vs_dose": -0.04792708408119114, "implied_alpha_loaded_fraction_low_ago2": [1.1363565473557116, 0.7500339083277796, 1.078791788390227], "implied_alpha_loaded_fraction_high_ago2": [0.10026675417844513, 0.06617946249950997, 0.09518751074031415]}, {"beta_case": "max_background_bracket", "beta": 14.377458774087353, "M_per_dose_molecules_per_cell": [20972.907930245015, 11335.763374019443, 18292.836973719845], "rho_per_dose": [0.2621613491280627, 0.14169704217524304, 0.22866046217149805], "M_over_dose": [20972.907930245015, 1133.5763374019443, 731.7134789487937], "loglog_slope_M_vs_dose": -0.08594449557298806, "implied_alpha_loaded_fraction_low_ago2": [1.3981938620163343, 0.7557175582679629, 1.2195224649146563], "implied_alpha_loaded_fraction_high_ago2": [0.12337004664850008, 0.06668096102364378, 0.10760492337482261]}] | {"pool_per_dose": [9.110538335795468, 78.59586066919407, 55.481823804547865], "log10_pool_per_dose": [0.9595440399101894, 1.8953996740818315, 1.7441507288113516], "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 195.0373198476406, "7mer-A1": 39.04999839140639, "8mer": 20.39834818569611}, "log10_K_by_class": {"7mer-m8": 1.6718455050755958, "6mer": 2.2901177203529683, "7mer-A1": 1.5916210203233487, "8mer": 1.3095950006179469}, "anchor_class": "7mer-m8", "K_anchor_molecules_per_cell": 46.972697928, "class_order_by_increasing_K": ["8mer", "7mer-A1", "7mer-m8", "6mer"], "class_ordering_is_8mer_strongest": true, "expected_ordering_if_model_sane": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "amplitude_c_log2_per_unit_bound_fraction": 0.15766751255279177, "rss": 3117.191788962015, "n_observations": 51951, "sigma_pooled": 0.24495415243174742, "mean_bound_fraction_per_dose": [0.04989158691894027, 0.16416427264401662, 0.14335660976240022], "n_transcripts_with_no_site": 12226, "optimiser_converged": true, "u_hat": [2.2901177203529683, 1.5916210203233487, 1.3095950006179469, 0.9595440399101894, 1.8953996740818315, 1.7441507288113516], "nll": -73078.65185506632} | 17317 | {"slope": 0.6337163304988844, "intercept": 1.0264935665837547, "n_points": 3, "residual_df": 1, "residual_rms_log10": 0.1713682702606421} | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [3337.515871808855, 11241.264917653712, 9778.149590260375], "rho_per_dose": [0.041718948397610686, 0.1405158114706714, 0.12222686987825468], "M_over_dose": [3337.515871808855, 1124.1264917653712, 391.125983610415], "loglog_slope_M_vs_dose": 0.3713618739137652, "implied_alpha_loaded_fraction_low_ago2": [0.22250105812059034, 0.7494176611769142, 0.6518766393506916], "implied_alpha_loaded_fraction_high_ago2": [0.01963244630475797, 0.06612508775090419, 0.057518527001531615]}, {"beta_case": "max_background_bracket", "beta": 14.375960215783723, "M_per_dose_molecules_per_cell": [3468.488608468623, 12371.155883759326, 10575.754081973677], "rho_per_dose": [0.04335610760585779, 0.15463944854699158, 0.13219692602467095], "M_over_dose": [3468.488608468623, 1237.1155883759325, 423.0301632789471], "loglog_slope_M_vs_dose": 0.38617738108237964, "implied_alpha_loaded_fraction_low_ago2": [0.23123257389790822, 0.824743725583955, 0.7050502721315784], "implied_alpha_loaded_fraction_high_ago2": [0.02040287416746249, 0.07277150519858427, 0.062210318129256925]}] | {"n_folds_completed": 5, "fold_assignment": "random over genes, one draw, shared by all three", "aic_free_unconstrained": -146135.30371013263, "n_parameters_free": 11, "aic_independent": -146108.43315968904, "aic_equilibrium": -146099.91364409783, "aic_equilibrium_minus_independent": 8.519515591207892, "aic_free_minus_best_constrained": -26.870550443592947, "preferred_by_aic": "free", "constrained_independent": {"mode": "independent", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 482.7360089622584, "7mer-A1": 47.45428594131675, "8mer": 18.297834007502587}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 14.939315782245608, "log10_kappa": 1.1743307073321376, "M_per_dose": [14.939315782245608, 149.3931578224561, 373.4828945561402], "pool_per_dose": [14.939315782245608, 149.3931578224561, 373.4828945561402], "amplitude_c_log2_per_unit_bound_fraction": 0.12306078480448848, "intercept_per_dose": [0.019927984092666544, 0.03982001232341795, 0.14452575623669525], "rss": 3119.044650754141, "n_observations": 51951, "sigma_pooled": 0.2450269421084819, "n_parameters": 9, "aic": -146108.43315968904, "nll": -73063.21657984452, "optimiser_converged": true, "u_hat": [2.6837096955668347, 1.6762754428245252, 1.2623996834865312, 1.1743307073321376]}, "constrained_equilibrium": {"mode": "equilibrium", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 88200.5970203036, "7mer-A1": 36.21863266254335, "8mer": 17.674952210665566}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-A1", "7mer-m8", "6mer"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 4398.823477926017, "log10_kappa": 3.643336534356755, "M_per_dose": [4398.823477926017, 43988.23477926017, 109970.58694815043], "pool_per_dose": [16.667686523249095, 29710.119718614107, 93511.77809234624], "amplitude_c_log2_per_unit_bound_fraction": 0.10667604095135931, "intercept_per_dose": [0.019193716422190997, 0.04064229274955668, 0.14354270687345994], "rss": 3119.556189097998, "n_observations": 51951, "sigma_pooled": 0.24504703408399098, "n_parameters": 9, "aic": -146099.91364409783, "nll": -73058.95682204892, "optimiser_converged": true, "u_hat": [4.945471524834154, 1.5589320506627067, 1.2473582482300518, 3.643336534356755]}, "heldout_gene_rmse_free": 0.24508920509556958, "heldout_gene_n_free": 51951, "heldout_gene_rmse_independent": 0.24515679217475037, "heldout_gene_n_independent": 51951, "heldout_gene_rmse_equilibrium": 0.24515350133491956, "heldout_gene_n_equilibrium": 51951, "preferred_by_heldout_gene_rmse": "free", "heldout_rmse_equilibrium_minus_independent": -3.2908398308051368e-06} | [{"dose_nM": 1.0, "n_no_site": 12226, "median_log2fc_no_site": 0.01989485183333306, "n_6mer": 2036, "median_log2fc_6mer": 0.002559000000001088, "delta_vs_no_site_6mer": -0.017335851833331972, "mann_whitney_p_less_6mer": 9.223181111558326e-09, "n_7mer-A1": 938, "median_log2fc_7mer-A1": -0.0156980046666666, "delta_vs_no_site_7mer-A1": -0.03559285649999966, "mann_whitney_p_less_7mer-A1": 3.963363644881946e-15, "n_7mer-m8": 1370, "median_log2fc_7mer-m8": -0.008943473833333826, "delta_vs_no_site_7mer-m8": -0.028838325666666886, "mann_whitney_p_less_7mer-m8": 3.3172381874254292e-18, "n_8mer": 747, "median_log2fc_8mer": -0.02298105433333575, "delta_vs_no_site_8mer": -0.04287590616666881, "mann_whitney_p_less_8mer": 1.2852268638342376e-20}, {"dose_nM": 10.0, "n_no_site": 12226, "median_log2fc_no_site": 0.029394477499999905, "n_6mer": 2036, "median_log2fc_6mer": 0.00025964166666669897, "delta_vs_no_site_6mer": -0.029134835833333206, "mann_whitney_p_less_6mer": 3.914629722200741e-15, "n_7mer-A1": 938, "median_log2fc_7mer-A1": -0.0250187555000001, "delta_vs_no_site_7mer-A1": -0.054413233000000005, "mann_whitney_p_less_7mer-A1": 3.797163125791279e-31, "n_7mer-m8": 1370, "median_log2fc_7mer-m8": -0.04589889066666686, "delta_vs_no_site_7mer-m8": -0.07529336816666676, "mann_whitney_p_less_7mer-m8": 1.0293270172164783e-60, "n_8mer": 747, "median_log2fc_8mer": -0.040996964333333, "delta_vs_no_site_8mer": -0.0703914418333329, "mann_whitney_p_less_8mer": 7.80906271157844e-30}, {"dose_nM": 25.0, "n_no_site": 12226, "median_log2fc_no_site": 0.1777871544999996, "n_6mer": 2036, "median_log2fc_6mer": 0.14058317333333337, "delta_vs_no_site_6mer": -0.03720398116666623, "mann_whitney_p_less_6mer": 3.126486763251573e-14, "n_7mer-A1": 938, "median_log2fc_7mer-A1": 0.09942284766666654, "delta_vs_no_site_7mer-A1": -0.07836430683333306, "mann_whitney_p_less_7mer-A1": 2.074150697198247e-28, "n_7mer-m8": 1370, "median_log2fc_7mer-m8": 0.11777650516666682, "delta_vs_no_site_7mer-m8": -0.06001064933333278, "mann_whitney_p_less_7mer-m8": 5.456957485049985e-23, "n_8mer": 747, "median_log2fc_8mer": 0.08568972066666802, "delta_vs_no_site_8mer": -0.09209743383333158, "mann_whitney_p_less_8mer": 4.722752927357796e-27}] | {"strong_sites_only": {"n_transcripts": 2744, "site_classes": ["7mer-m8", "8mer", "7mer-A1"], "pool_per_dose": [15.034447715152979, 2.833727332631963, 10.261410106870601], "slope": -0.23589080192227907, "amplitude_c": 0.03175779728963534}, "excluding_top_dose": {"doses": [1.0, 10.0], "pool_per_dose": [1.04525341366016e-06, 6.696659198282735], "slope": 6.806636603112747}} | [{"dose_nM": 1.0, "spearman_minus_log10K_vs_log2fc": -0.0567636858799641, "p": 5.06878467119295e-05, "median_log2fc": -0.00727620266666662, "mean_log2fc": -0.009872089599096438}, {"dose_nM": 10.0, "spearman_minus_log10K_vs_log2fc": -0.0730569255258414, "p": 1.8047876180890976e-07, "median_log2fc": -0.019048358333334292, "mean_log2fc": -0.0442645545905192}, {"dose_nM": 25.0, "spearman_minus_log10K_vs_log2fc": -0.04608751360217741, "p": 0.0010042201825851468, "median_log2fc": 0.11792849766666658, "mean_log2fc": 0.06305978102010085}] | {"n_resamples": 300, "n_successful": 300, "slope_ci95": [-4.837075099610085, 1.7665687204994862], "slope_median": -0.5423406126629384, "slope_sd": 1.477010859534411, "M_vs_dose_slope_ci95": [-2.975657833130136, 0.24150803894532458], "aic_equilibrium_minus_independent_ci95": [-10.884024412174403, 25.28914033530163], "frac_resamples_preferring_equilibrium": 0.25666666666666665, "frac_resamples_slope_above_1": 0.05, "pool_ci95_per_dose": [[0.11031783876813614, 100000000.0], [0.9345875225462213, 42.84145374668253], [2.4424442575318115, 541.0639673147607]], "rho_ci95_per_dose_zero_background": [[0.07200813633423431, 1250.2528955225182], [0.10381082433800144, 0.1796356472634919], [0.12351752874891411, 0.23331069709863417]], "rho_ci95_per_dose_max_background": [[0.07204022822459662, 19222.07636313171], [0.10404983343966628, 0.18718369780300004], [0.12389498498663791, 0.32612941542581114]], "rho_median_per_dose_zero_background": [0.21448535709960004, 0.14094334909793438, 0.20010320541625837]} | {"n_successful": 300, "slope_ci95": [0.4695689733459587, 0.8648290486141881], "slope_median": 0.6381545313096157, "frac_resamples_slope_above_1": 0.006666666666666667, "M_vs_dose_slope_ci95": [0.322398051826875, 0.4305937461765674], "pool_ci95_per_dose": [[5.110986171873607, 13.964804261686744], [29.478046074026583, 176.70938390188283], [21.68031810749827, 148.15930457097764]], "rho_ci95_per_dose_zero_background": [[0.02841710316511147, 0.05076818321213641], [0.09260491144318413, 0.17131671326661027], [0.07760918365583676, 0.16960325364895482]], "rho_median_per_dose_zero_background": [0.04040788402747897, 0.13878516025473947, 0.11863751585107266]} |
| STAT3-1676M | OK | MCF-7 breast cancer cells | STAT3 | [1.0, 10.0, 25.0] | 5091 | 2744 | 20257.7 | 14.3775 | {"pool_per_dose": [9849.902482884328, 2.419270200161063, 9.434289001402579], "log10_pool_per_dose": [3.9934319308676756, 0.3836843759624172, 0.9747091758944166], "amplitude_c_log2_per_unit_bound_fraction": 0.052971098545986244, "rss": 1014.1661888906854, "n_observations": 15273, "sigma_pooled": 0.2576869278765364, "residual_sd_per_dose": [0.13005260031399649, 0.23560790608735424, 0.3561208098392454], "mean_bound_fraction_per_dose": [0.9562952361098581, 0.4964533768907329, 0.6071515513170499], "max_bound_fraction_per_dose": [0.9999999999995067, 0.99999999799181, 0.9999999994850324], "frac_sites_above_half_saturation_per_dose": [0.9670005892751915, 0.49302691023374584, 0.6138283244942054], "optimiser_converged": true, "nll": -20710.339030718536} | {"slope": -2.4399430411764302, "intercept": 3.734220840014131, "n_points": 3, "residual_df": 1, "residual_rms_log10": 0.66349320867544} | {"mode": "independent", "log10_kappa": -0.49803916840997875, "kappa_complexes_per_cell_per_nM": 0.3176587565754636, "pool_per_dose": [0.3176587565754636, 3.176587565754636, 7.94146891438659], "M_per_dose": [0.3176587565754636, 3.176587565754636, 7.94146891438659], "amplitude_c_log2_per_unit_bound_fraction": 0.042977097066501296, "rss": 1014.6488411538123, "n_observations": 15273, "sigma_pooled": 0.25774823853063683, "n_parameters": 6, "aic": -41401.41121054664, "nll": -20706.70560527332} | {"mode": "equilibrium", "log10_kappa": 2.7301201139895266, "kappa_complexes_per_cell_per_nM": 537.1803452356887, "pool_per_dose": [8.75384415688189e-05, 0.10156208421155791, 23.247990610093744], "M_per_dose": [537.1803452356887, 5371.803452356888, 13429.508630892218], "amplitude_c_log2_per_unit_bound_fraction": 0.054380785031059885, "rss": 1014.729546767634, "n_observations": 15273, "sigma_pooled": 0.2577584890307755, "n_parameters": 6, "aic": -41400.19643773947, "nll": -20706.098218869734} | -41404.7 | -41401.4 | -41400.2 | 1.21477 | independent | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [29079.280888156845, 9817.700660705244, 11997.381533105685], "rho_per_dose": [0.3634910111019606, 0.12272125825881555, 0.14996726916382105], "M_over_dose": [29079.280888156845, 981.7700660705244, 479.8952613242274], "loglog_slope_M_vs_dose": -0.3130594776888665, "implied_alpha_loaded_fraction_low_ago2": [1.938618725877123, 0.6545133773803496, 0.799825435540379], "implied_alpha_loaded_fraction_high_ago2": [0.17105459345974616, 0.057751180357089676, 0.0705728325476805]}, {"beta_case": "max_background_bracket", "beta": 14.377458774087353, "M_per_dose_molecules_per_cell": [170695.84776460694, 9852.483618271437, 12133.022634286175], "rho_per_dose": [2.1336980970575867, 0.12315604522839296, 0.15166278292857718], "M_over_dose": [170695.84776460694, 985.2483618271438, 485.320905371447], "loglog_slope_M_vs_dose": -0.9021046960378989, "implied_alpha_loaded_fraction_low_ago2": [11.37972318430713, 0.6568322412180958, 0.8088681756190783], "implied_alpha_loaded_fraction_high_ago2": [1.0040932221447467, 0.05795578598983198, 0.07137072137815398]}] | {"pool_per_dose": [19.069155285659605, 53.451068707710434, 146.24360975185104], "log10_pool_per_dose": [1.2803314553479428, 1.7279563929726995, 2.1650768982746165], "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 1459.7814968230753, "7mer-A1": 226.32682477204034, "8mer": 45.46958706296049}, "log10_K_by_class": {"7mer-m8": 1.6718455050755958, "6mer": 3.1642878545339688, "7mer-A1": 2.354736030578965, "8mer": 1.6577210101300706}, "anchor_class": "7mer-m8", "K_anchor_molecules_per_cell": 46.972697928, "class_order_by_increasing_K": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "class_ordering_is_8mer_strongest": true, "expected_ordering_if_model_sane": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "amplitude_c_log2_per_unit_bound_fraction": 0.14129557533018247, "rss": 2895.5728741289213, "n_observations": 51951, "sigma_pooled": 0.23608603256883562, "mean_bound_fraction_per_dose": [0.04627791911433206, 0.08601865065916947, 0.13077144167166652], "n_transcripts_with_no_site": 12226, "optimiser_converged": true, "u_hat": [3.1642878545339688, 2.354736030578965, 1.6577210101300706, 1.2803314553479428, 1.7279563929726995, 2.1650768982746165], "nll": -74994.33338060422} | 17317 | {"slope": 0.5970565425760251, "intercept": 1.2472196585709356, "n_points": 3, "residual_df": 1, "residual_rms_log10": 0.08475506281865908} | [{"beta_case": "zero_background", "beta": 0.0, "M_per_dose_molecules_per_cell": [3033.8923878730375, 5729.569824442729, 8887.8333430236], "rho_per_dose": [0.037923654848412966, 0.07161962280553412, 0.111097916787795], "M_over_dose": [3033.8923878730375, 572.956982444273, 355.513333720944], "loglog_slope_M_vs_dose": 0.32273772849240373, "implied_alpha_loaded_fraction_low_ago2": [0.20225949252486916, 0.3819713216295153, 0.59252222286824], "implied_alpha_loaded_fraction_high_ago2": [0.017846425811017867, 0.033703351908486646, 0.05228137260602118]}, {"beta_case": "max_background_bracket", "beta": 14.375960215783723, "M_per_dose_molecules_per_cell": [3308.029805608282, 6497.980261675896, 10990.225658628811], "rho_per_dose": [0.04135037257010352, 0.0812247532709487, 0.13737782073286015], "M_over_dose": [3308.029805608282, 649.7980261675896, 439.6090263451525], "loglog_slope_M_vs_dose": 0.3575694621008961, "implied_alpha_loaded_fraction_low_ago2": [0.22053532037388546, 0.4331986841117264, 0.7326817105752541], "implied_alpha_loaded_fraction_high_ago2": [0.019458998856519305, 0.03822341330397586, 0.06464838622722831]}] | {"n_folds_completed": 5, "fold_assignment": "random over genes, one draw, shared by all three", "aic_free_unconstrained": -149966.66676120844, "n_parameters_free": 11, "aic_independent": -149959.49775852278, "aic_equilibrium": -149916.42677989363, "aic_equilibrium_minus_independent": 43.07097862914088, "aic_free_minus_best_constrained": -7.169002685666783, "preferred_by_aic": "free", "constrained_independent": {"mode": "independent", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 4153.804131089008, "7mer-A1": 538.6232511048821, "8mer": 34.644232228394124}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["8mer", "7mer-m8", "7mer-A1", "6mer"], "class_ordering_is_8mer_strongest": true, "kappa_complexes_per_cell_per_nM": 19.891810013579637, "log10_kappa": 1.2986743026390117, "M_per_dose": [19.891810013579637, 198.91810013579635, 497.2952503394909], "pool_per_dose": [19.891810013579637, 198.91810013579635, 497.2952503394909], "amplitude_c_log2_per_unit_bound_fraction": 0.11078223163514142, "intercept_per_dose": [0.005871728781103672, 0.007290683732008317, 0.011469918411270388], "rss": 2896.195463452207, "n_observations": 51951, "sigma_pooled": 0.23611141213093711, "n_parameters": 9, "aic": -149959.49775852278, "nll": -74988.74887926139, "optimiser_converged": true, "u_hat": [3.6184460139148324, 2.7312850969562854, 1.539630941115624, 1.2986743026390117]}, "constrained_equilibrium": {"mode": "equilibrium", "parameterisation": "site_class", "K_by_class_molecules_per_cell": {"7mer-m8": 46.972697928, "6mer": 34758.20682196933, "7mer-A1": 3845.0168414225986, "8mer": 48.482784799067936}, "anchor_class": "7mer-m8", "class_order_by_increasing_K": ["7mer-m8", "8mer", "7mer-A1", "6mer"], "class_ordering_is_8mer_strongest": false, "kappa_complexes_per_cell_per_nM": 606.3111346038337, "log10_kappa": 2.7826955439113648, "M_per_dose": [606.3111346038337, 6063.111346038337, 15157.778365095843], "pool_per_dose": [3.4301967714452646, 116.12551542815629, 4104.176662181926], "amplitude_c_log2_per_unit_bound_fraction": 0.11298290496452545, "intercept_per_dose": [0.0019097573846328139, 0.0037985468238932356, 0.012860084489480963], "rss": 2898.5976057993203, "n_observations": 51951, "sigma_pooled": 0.23620930878059335, "n_parameters": 9, "aic": -149916.42677989363, "nll": -74967.21338994682, "optimiser_converged": true, "u_hat": [4.541057363075485, 3.5848982463795522, 1.6855875572831014, 2.7826955439113648]}, "heldout_gene_rmse_free": 0.23614089621931633, "heldout_gene_n_free": 51951, "heldout_gene_rmse_independent": 0.23615816770771647, "heldout_gene_n_independent": 51951, "heldout_gene_rmse_equilibrium": 0.23625266263177108, "heldout_gene_n_equilibrium": 51951, "preferred_by_heldout_gene_rmse": "free", "heldout_rmse_equilibrium_minus_independent": 9.449492405461113e-05} | [{"dose_nM": 1.0, "n_no_site": 12226, "median_log2fc_no_site": 0.010574265333333166, "n_6mer": 2036, "median_log2fc_6mer": -0.002364901500000016, "delta_vs_no_site_6mer": -0.012939166833333182, "mann_whitney_p_less_6mer": 2.1787731027874385e-06, "n_7mer-A1": 938, "median_log2fc_7mer-A1": -0.011623496999999539, "delta_vs_no_site_7mer-A1": -0.022197762333332705, "mann_whitney_p_less_7mer-A1": 7.668116177962157e-11, "n_7mer-m8": 1370, "median_log2fc_7mer-m8": -0.022248754999999676, "delta_vs_no_site_7mer-m8": -0.03282302033333284, "mann_whitney_p_less_7mer-m8": 3.7345943751604864e-28, "n_8mer": 747, "median_log2fc_8mer": -0.02189049333333415, "delta_vs_no_site_8mer": -0.032464758666667315, "mann_whitney_p_less_8mer": 3.3970885606219476e-16}, {"dose_nM": 10.0, "n_no_site": 12226, "median_log2fc_no_site": -0.013455142000000198, "n_6mer": 2036, "median_log2fc_6mer": -0.007826516166665964, "delta_vs_no_site_6mer": 0.005628625833334233, "mann_whitney_p_less_6mer": 0.3668951004932422, "n_7mer-A1": 938, "median_log2fc_7mer-A1": -0.027044055333333095, "delta_vs_no_site_7mer-A1": -0.013588913333332897, "mann_whitney_p_less_7mer-A1": 0.0002088851629526177, "n_7mer-m8": 1370, "median_log2fc_7mer-m8": -0.06392833483333282, "delta_vs_no_site_7mer-m8": -0.050473192833332625, "mann_whitney_p_less_7mer-m8": 3.8067458773701256e-32, "n_8mer": 747, "median_log2fc_8mer": -0.03463006333333141, "delta_vs_no_site_8mer": -0.02117492133333121, "mann_whitney_p_less_8mer": 3.7508245381661295e-09}, {"dose_nM": 25.0, "n_no_site": 12226, "median_log2fc_no_site": -0.01465330850000024, "n_6mer": 2036, "median_log2fc_6mer": -0.015284235666665591, "delta_vs_no_site_6mer": -0.0006309271666653515, "mann_whitney_p_less_6mer": 0.10220111699330142, "n_7mer-A1": 938, "median_log2fc_7mer-A1": -0.036673200666666794, "delta_vs_no_site_7mer-A1": -0.022019892166666555, "mann_whitney_p_less_7mer-A1": 6.066411405720856e-07, "n_7mer-m8": 1370, "median_log2fc_7mer-m8": -0.08188792049999938, "delta_vs_no_site_7mer-m8": -0.06723461199999914, "mann_whitney_p_less_7mer-m8": 5.727962329514894e-30, "n_8mer": 747, "median_log2fc_8mer": -0.05601216299999923, "delta_vs_no_site_8mer": -0.04135885449999899, "mann_whitney_p_less_8mer": 4.5513159651413445e-10}] | {"strong_sites_only": {"n_transcripts": 2744, "site_classes": ["7mer-m8", "8mer", "7mer-A1"], "pool_per_dose": [2103.6174043867354, 0.29960049107949643, 0.5221230311213011], "slope": -2.824100418397036, "amplitude_c": 0.029862489386058188}, "excluding_top_dose": {"doses": [1.0, 10.0], "pool_per_dose": [128.8957617864612, 2.2931258491657878], "slope": -1.7498107476549476}} | [{"dose_nM": 1.0, "spearman_minus_log10K_vs_log2fc": -0.052272754981319454, "p": 0.00019044791113708318, "median_log2fc": -0.012265998666666889, "mean_log2fc": -0.019733192267138117}, {"dose_nM": 10.0, "spearman_minus_log10K_vs_log2fc": -0.06628136492299862, "p": 2.208965610383774e-06, "median_log2fc": -0.031165465000000836, "mean_log2fc": -0.03562721783670531}, {"dose_nM": 25.0, "spearman_minus_log10K_vs_log2fc": -0.056922091471380165, "p": 4.828855176376512e-05, "median_log2fc": -0.04026889533333211, "mean_log2fc": -0.049774251063314366}] | {"n_resamples": 300, "n_successful": 300, "slope_ci95": [-6.154037367058387, -0.39951495698029243], "slope_median": -2.381361073532992, "slope_sd": 1.2018060923197142, "M_vs_dose_slope_ci95": [-3.123384534192967, -0.04513349581700166], "aic_equilibrium_minus_independent_ci95": [-9.99817778240813, 19.46420808520321], "frac_resamples_preferring_equilibrium": 0.32, "frac_resamples_slope_above_1": 0.0, "pool_ci95_per_dose": [[56.45943054423111, 100000000.0], [0.10744367998570058, 83.85218062852505], [0.2631548209852121, 142.37758081214358]], "rho_ci95_per_dose_zero_background": [[0.1821821107304035, 1250.2510703420498], [0.06814641047258893, 0.18956715775433855], [0.08392756642120498, 0.20225725391939653]], "rho_ci95_per_dose_max_background": [[0.19335933748562006, 19222.07453795124], [0.0681706451193835, 0.2062327763014459], [0.08397820098341816, 0.22349933841381883]], "rho_median_per_dose_zero_background": [0.37167576820186066, 0.12046601423930717, 0.14888451536407493]} | {"n_successful": 300, "slope_ci95": [0.36794125847427633, 0.8615801735285057], "slope_median": 0.5902480177816867, "frac_resamples_slope_above_1": 0.0, "M_vs_dose_slope_ci95": [0.27091720839629024, 0.3755362202742622], "pool_ci95_per_dose": [[7.042351061835297, 28.108860422131123], [15.329000407532424, 104.1833217631501], [26.407947962430715, 481.8135758118696]], "rho_ci95_per_dose_zero_background": [[0.01962234751899644, 0.04772790234875482], [0.03509218117351341, 0.0901135106323388], [0.05287461807359176, 0.13973028236297746]], "rho_median_per_dose_zero_background": [0.03587220289265149, 0.06884910239392711, 0.10676893928265141]} |


**`class_fit_pooled_slope_construct_fixed_effects`**

```json
{
  "slope": 1.4244891646525235,
  "n_points": 14,
  "n_constructs": 5,
  "residual_df": 8,
  "residual_rms_log10": 1.339217907816803,
  "construct_intercepts": {
    "HK2-3581": 0.2821669012034722,
    "HK2-3581M": -0.771867915498603,
    "HK2-4031": -2.7163712499742365,
    "STAT3-1676": 0.3944182943210919,
    "STAT3-1676M": 0.5858417289183868
  }
}
```


**`class_fit_pooled_slope_bootstrap_ci95`**: `[0.95602597682162, 2.51793758769985]`


**`class_fit_rho_all_construct_dose_zero_background`**: `[0.09355595224525051, 0.10826270771163952, 0.13433645850290915, 0.00696463534730159, 0.01695650476086773, 0.12471869673098986, 2.7168351276728004e-06, 0.16707296568978425, 0.041718948397610686, 0.1405158114706714, 0.12222686987825468, 0.037923654848412966, 0.07161962280553412, 0.111097916787795]`


**`class_fit_rho_median_bootstrap_ci95`**: `[0.06236413734013383, 0.11060889271332765]`


**`leave_one_construct_out_class_fit`**

| construct_excluded | slope | n_points | n_constructs | residual_df | residual_rms_log10 |
|---|---|---|---|---|---|
| HK2-3581 | 1.77325 | 11 | 4 | 6 | 1.45013 |
| HK2-3581M | 1.51992 | 11 | 4 | 6 | 1.49357 |
| HK2-4031 | 0.633277 | 12 | 4 | 7 | 0.280859 |
| STAT3-1676 | 1.6516 | 11 | 4 | 6 | 1.48281 |
| STAT3-1676M | 1.66213 | 11 | 4 | 6 | 1.48242 |


**`leave_one_construct_out_thermo_fit`**

| construct_excluded | slope | n_points | n_constructs | residual_df | residual_rms_log10 |
|---|---|---|---|---|---|
| HK2-3581 | 1.89865 | 11 | 4 | 6 | 2.78722 |
| HK2-3581M | -0.804682 | 11 | 4 | 6 | 1.38309 |
| HK2-4031 | 0.605087 | 12 | 4 | 7 | 2.75814 |
| STAT3-1676 | 1.45055 | 11 | 4 | 6 | 2.91691 |
| STAT3-1676M | 2.01421 | 11 | 4 | 6 | 2.70746 |


**`class_fit_pooled_slope_loco_range`**: `[0.6332768398775154, 1.7732508906459414]`


**`M_vs_dose_slope_summary`**

```json
{
  "per_construct": [
    {
      "construct": "HK2-3581",
      "n_doses": 3,
      "loglog_slope_M_vs_dose": 0.10292005787736384,
      "bootstrap_ci95": [
        0.05754863924707973,
        0.14098123205342034
      ],
      "ci_excludes_one": true
    },
    {
      "construct": "HK2-3581M",
      "n_doses": 3,
      "loglog_slope_M_vs_dose": 0.7977131820687425,
      "bootstrap_ci95": [
        0.6560871180954891,
        1.0110749177618108
      ],
      "ci_excludes_one": false
    },
    {
      "construct": "HK2-4031",
      "n_doses": 2,
      "loglog_slope_M_vs_dose": 4.788842897913792,
      "bootstrap_ci95": [
        1.6655013695481364,
        15.512641049466062
      ],
      "ci_excludes_one": true
    },
    {
      "construct": "STAT3-1676",
      "n_doses": 3,
      "loglog_slope_M_vs_dose": 0.3713618739137652,
      "bootstrap_ci95": [
        0.322398051826875,
        0.4305937461765674
      ],
      "ci_excludes_one": true
    },
    {
      "construct": "STAT3-1676M",
      "n_doses": 3,
      "loglog_slope_M_vs_dose": 0.32273772849240373,
      "bootstrap_ci95": [
        0.27091720839629024,
        0.3755362202742622
      ],
      "ci_excludes_one": true
    }
  ],
  "n_constructs": 5,
  "n_with_ci_excluding_one": 4,
  "test": "the assumed proportionality M_d = kappa * dose_d implies a log-log slope of exactly 1 for the conservation-inverted M against dose. These are the measured slopes. A slope away from 1 whose interval excludes 1 falsifies the assumption for that construct, or the affinity model through which the inversion runs, and the two cannot be separated here."
}
```


**`class_fit_model_comparison_summary`**

```json
{
  "n_constructs": 5,
  "preferred_by_aic": {
    "HK2-3581": "free",
    "HK2-3581M": "free",
    "HK2-4031": "free",
    "STAT3-1676": "free",
    "STAT3-1676M": "free"
  },
  "preferred_by_heldout_gene_rmse": {
    "HK2-3581": "free",
    "HK2-3581M": "free",
    "HK2-4031": "free",
    "STAT3-1676": "free",
    "STAT3-1676M": "free"
  },
  "n_preferring_equilibrium_by_aic": 0,
  "n_preferring_equilibrium_by_heldout": 0,
  "n_preferring_free_unconstrained_by_aic": 5,
  "aic_equilibrium_minus_independent": {
    "HK2-3581": 71.15361380181275,
    "HK2-3581M": -67.24632095781271,
    "HK2-4031": -1.8825785240042023,
    "STAT3-1676": 8.519515591207892,
    "STAT3-1676M": 43.07097862914088
  },
  "heldout_rmse_equilibrium_minus_independent": {
    "HK2-3581": 0.00018808119304503101,
    "HK2-3581M": -0.00014473319035779308,
    "HK2-4031": -2.1785079201697144e-06,
    "STAT3-1676": -3.2908398308051368e-06,
    "STAT3-1676M": 9.449492405461113e-05
  },
  "note": "three dose mechanisms in the site-class parameterisation: free pools per dose, M proportional to dose with the pool equal to M, and M proportional to dose with the pool the equilibrium free level. The class affinities are free in all three, so this compares the dose mechanism and nothing else. A preference for the FREE model says the data reject proportional loading in either mechanistic form."
}
```


**`pooled_slope_construct_fixed_effects`**

```json
{
  "slope": 1.0204027336128014,
  "n_points": 14,
  "n_constructs": 5,
  "residual_df": 8,
  "residual_rms_log10": 2.6450192357903646,
  "construct_intercepts": {
    "HK2-3581": 3.70160727452026,
    "HK2-3581M": -4.001588029496148,
    "HK2-4031": 0.36135364654938906,
    "STAT3-1676": 0.9764701598901437,
    "STAT3-1676M": 0.968320314278684
  }
}
```


**`pooled_slope_bootstrap_ci95`**: `[-0.15150613241588706, 1.8058867214599283]`


**`rho_data_driven_zero_background_all_construct_dose`**: `[17.269913095082625, 0.3940783233351393, 0.20689188744322437, 2.9861644228248805e-05, 0.0004766303397569743, 0.32163659977998194, 0.017547242100523754, 0.1947123599843846, 0.21306685262919592, 0.1406313578114587, 0.20227346032316754, 0.3634910111019606, 0.12272125825881555, 0.14996726916382105]`


**`rho_data_driven_max_background_all_construct_dose`**: `[263.72490606187694, 2.946796286029333, 0.5423312216179355, 2.9861646037738138e-05, 0.0004766309073124185, 1.9182663245035463, 0.017554527725026962, 0.40855394210303, 0.2621613491280627, 0.14169704217524304, 0.22866046217149805, 2.1336980970575867, 0.12315604522839296, 0.15166278292857718]`


**`rho_data_driven_median_bootstrap_ci95`**: `[0.14063585906867238, 0.2179807859361019]`


**`rho_data_driven_pooled_draw_spread_2p5_97p5`**: `[2.9401508063213007e-05, 108.32477215562601]`


**`rho_data_driven_range_zero_background`**: `[2.9861644228248805e-05, 17.269913095082625]`


**`e5_alpha_swept_band_for_comparison`**: `[0.0001875, 2.125]`


### `e9v_sim_estimator_validation`  (OK)

seed `0`, wall clock `5.7055` s, recorded `2026-09-05T06:39:19Z`

| quantity | value |
|---|---|
| `SIMULATION_NOTE` | every value here is simulated. Ground-truth pools and affinities do not exist in nature; this validates the estimators used in e9 and claims nothing about any cell. |
| `sim_n_transcripts_continuous` | 4000 |
| `sim_n_genes_class` | 12000 |
| `sim_worst_slope_error_independent_data` | 0.0193971 |
| `sim_worst_slope_error_equilibrium_data` | 0.00554712 |
| `sim_worst_slope_error_class_estimator` | 0.00561189 |
| `sim_worst_rel_pool_error_class_estimator` | 0.0408503 |
| `sim_worst_rel_K_error_class_estimator` | 0.0321698 |
| `sim_class_ordering_correct_in_all_runs` | true |
| `sim_equilibrium_true_slope_exceeds_one` | true |
| `sim_interpretation` | the estimator returns 1 on independent-generated data and the model's own exponent on equilibrium-generated data, so an exponent away from 1 in e9 is a property of the measurement and not an artefact of the fit. |


**`sim_doses_nM`**: `[1.0, 10.0, 25.0]`


**`sim_noise_levels`**: `[0.05, 0.15, 0.3]`


**`sim_continuous_K`**

| sim_noise_sd | sim_true_pool_per_dose | sim_fitted_pool_per_dose_equilibrium_data | sim_max_rel_pool_error_equilibrium_data | sim_true_slope_equilibrium | sim_fitted_slope_equilibrium_data | sim_true_slope_independent | sim_fitted_slope_independent_data | sim_amplitude_recovered_equilibrium_data | sim_true_amplitude |
|---|---|---|---|---|---|---|---|---|---|
| 0.05 | [0.021055806183960066, 1.5296115647981363, 79.21592458193544] | [0.02080089795131454, 1.5341420596095379, 78.9666117889188] | 0.0121063 | 2.42294 | 2.42647 | 1 | 1.00351 | 1.99761 | 2 |
| 0.15 | [0.021055806183960066, 1.5296115647981363, 79.21592458193544] | [0.02074712676605665, 1.5458450933247319, 79.12209797177634] | 0.0146601 | 2.42294 | 2.42847 | 1 | 1.0194 | 1.99722 | 2 |
| 0.3 | [0.021055806183960066, 1.5296115647981363, 79.21592458193544] | [0.021005190524622484, 1.575374262142766, 79.93537367953375] | 0.0299179 | 2.42294 | 2.42849 | 1 | 1.01886 | 1.99314 | 2 |


**`sim_site_class_K`**

| sim_noise_sd | sim_true_pool_per_dose | sim_fitted_pool_per_dose | sim_max_rel_pool_error | sim_true_K_by_class | sim_fitted_K_by_class | sim_max_rel_K_error | sim_true_slope | sim_fitted_slope | sim_class_ordering_correct | sim_amplitude_recovered |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.05 | [50.0, 300.0, 600.0] | [49.9217323377864, 302.9916459228208, 604.9317303178555] | 0.00997215 | {"6mer": 3000.0, "7mer-A1": 800.0, "7mer-m8": 300.0, "8mer": 80.0} | {"7mer-m8": 300.0, "6mer": 3024.9097130686173, "7mer-A1": 805.6594613973461, "8mer": 79.7843225180316} | 0.00830324 | 0.773173 | 0.776582 | true | 1.99241 |
| 0.15 | [50.0, 300.0, 600.0] | [48.88392292197725, 297.9463500019579, 593.9993028641883] | 0.0223215 | {"6mer": 3000.0, "7mer-A1": 800.0, "7mer-m8": 300.0, "8mer": 80.0} | {"7mer-m8": 300.0, "6mer": 3002.134468721534, "7mer-A1": 808.3511659902947, "8mer": 79.7721318579486} | 0.010439 | 0.773173 | 0.777631 | true | 2.01018 |
| 0.3 | [50.0, 300.0, 600.0] | [50.931653713381614, 306.3379148667833, 624.5101823363806] | 0.0408503 | {"6mer": 3000.0, "7mer-A1": 800.0, "7mer-m8": 300.0, "8mer": 80.0} | {"7mer-m8": 300.0, "6mer": 3096.509280051739, "7mer-A1": 807.8124906506637, "8mer": 77.79696850323646} | 0.0321698 | 0.773173 | 0.778785 | true | 1.9812 |


### `e10_cross_context`  (OK)

seed `0`, wall clock `33.8669` s, recorded `2026-09-04T19:51:40Z`

| quantity | value |
|---|---|
| `data_source` | GSE14073 (Burchard et al. 2009, PMC2648714) |
| `gencode_release` | 50 |
| `n_bootstrap` | 300 |
| `SEED_RECOVERY_NOTE` | the guide sequences are not in the deposit and the article is not open access, both recorded as failures in data/PROVENANCE.json. The 7-mer site is recovered from the measured response separately in each cell line by the enrichment scan of riscpool.kmers, and a construct enters the analysis only ... |
| `AFFINITY_MODEL_LIMITATION` | recovery identifies guide positions 2-8 and nothing else, so K here is built from the SEED duplex rather than from the full 19-mer as in the HeLa pipeline. That costs resolution within the retrieved set. It does not threaten the cross-context comparison, which requires only that K be identical be... |
| `DELIVERY_CONFOUND` | the independent-scoring prediction of a pool ratio of exactly 1 holds only if the total loaded complex M is equal in the two cell lines. M is not measured. Different uptake, different Argonaute abundance or different loading would move the ratio away from 1 with no competition involved, so a rati... |
| `n_constructs_attempted` | 7 |
| `n_constructs_with_agreeing_seed` | 3 |
| `n_constructs_fitted` | 3 |
| `pooled_geometric_mean_pool_ratio` | 0.441866 |
| `pooled_ratio_ci_excludes_1` | true |
| `n_constructs_whose_ci_excludes_1` | 2 |
| `POWER_LIMITATION` | three constructs survive the seed-agreement requirement out of seven attempted, two contexts each, and the bootstrap resamples transcripts rather than cell lines, so it propagates uncertainty in each fitted pool and says nothing about between-context variability beyond the one pair observed. Two ... |


**`contexts`**: `["HUH7", "PLC/PRF/5"]`


**`timepoints_hours_used`**: `[6.0, 12.0, 48.0]`


**`constants_used`**

```json
{
  "kd_seed_match_molar": 2.6e-11,
  "kd_seed_match_molecules_per_cell": 46.972697928,
  "hela_cell_volume_litres": 3e-12,
  "anchor_site_class": "7mer-m8",
  "median_boltzmann_factor_anchor_class": 0.17250543501637444,
  "K_scale_constant_C": 272.29691588291865,
  "mrna_molecules_per_cell": 80000.0,
  "ago2_copies_per_cell_low": 15000.0,
  "ago2_copies_per_cell_high": 170000.0
}
```


**`rho_grid`**: `[0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0]`


**`seed_recovery`**

| construct | agree_exact_7mer | top_site_HUH7 | welch_t_HUH7 | delta_mean_log2fc_HUH7 | top_site_PLC | welch_t_PLC | delta_mean_log2fc_PLC | n_transcripts_with_site | share_a_6mer | top10_HUH7 | top10_PLC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| APOB-Hs1 | true | GAAAAAT | -11.6572 | -0.0386571 | GAAAAAT | -10.0134 | -0.0342979 | 3927 | true | ["GAAAAAT", "AAAAATA", "AGAAAAA", "AAAATAT", "TAAAAAT", "TGAAAAA", "AAAAATG", "AAAAAAT", "GAAAAAA", "AAATATT"] | ["GAAAAAT", "AAAAATA", "AGAAAAA", "AAAATAT", "GAAAAAA", "TGAAAAA", "GGAAAAA", "TATAAAA", "AAAAATG", "AAGAAAA"] |
| APOB-Hs2 | false | GGGCCCC | -6.42972 | -0.0208637 | ATAACTA | -13.2634 | -0.073616 | 1683 | false | ["GGGCCCC", "CCCCTGC", "CCCCTCC", "CCCCCAG", "GGGGCCC", "CCACCCC", "GGCCCCC", "CCTGCCC", "CGCCCTG", "CCCCAGC"] | ["ATAACTA", "AATAACT", "ATAACTT", "TATAACT", "TAACTTT", "TAACTAT", "AACTTTA", "ATAACTG", "AAATAAC", "TTTAACT"] |
| APOB-Hs3 | true | CCTGAAA | -12.7716 | -0.0442737 | CCTGAAA | -16.0846 | -0.0646007 | 2425 | true | ["CCTGAAA", "CTGAAAA", "ACCTGAA", "TCCTGAA", "TCTGAAA", "AGAGGGC", "CTGAAAT", "GGGGGAG", "ACTGAAA", "GCTCCTC"] | ["CCTGAAA", "CTGAAAA", "CTGAAAT", "ACTGAAA", "ACCTGAA", "TCTGAAA", "TGAAAAT", "TCCTGAA", "CTGAAAC", "TGAAAAA"] |
| APOB-Hs4 | false | GCCCCCA | -9.99238 | -0.0298796 | TTTTTTA | -12.5358 | -0.030906 | 2226 | false | ["GCCCCCA", "GGCCCCC", "CCTGCCC", "GGGCCCC", "CCCCTCC", "CCCGCCC", "CCCACCC", "CCACCCC", "GGGGCCC", "CCCCGCC"] | ["TTTTTTA", "TTTTTAA", "TTTTAAA", "TTTTTTT", "ATATTTT", "ATACCAA", "ATTTTTT", "AATACCA", "GTTTTTT", "TTTTGTT"] |
| Apob-Mm1 | false | GCCCCGG | -4.86447 | -0.0155605 | AACGGCG | -3.36838 | -0.0404683 | 842 | false | ["GCCCCGG", "GGGGCCC", "CGGCCCC", "CCCGGAG", "CTGCGGC", "CCGCTCC", "GCGGCCC", "CGGCCAC", "CCGGCGG", "CCTGCCC"] | ["AACGGCG", "CGTAGCG", "GAGGGGG", "GGAGGGG", "GTTACGG", "CGGCCCC", "GGTGCCG", "ATCCGGG", "CCGGAGG", "ATAATCG"] |
| Apob-Mm2 | false | CCCGCGC | -4.36534 | -0.0347693 | AAGCAAA | -9.48383 | -0.0315626 | 259 | false | ["CCCGCGC", "GCCCCGG", "GCGGGCC", "CGCGGGG", "CGGGCCG", "CCCCCGC", "CCGACCG", "CCCGGGC", "AGGCCGC", "CCGCGGG"] | ["AAGCAAA", "AGCAAAA", "GCAAAAA", "GAAGCAA", "GCAAAAG", "GCAAAAT", "AAAGCAA", "TGCAAAA", "TAAGCAA", "CCCTCCG"] |
| RAD18 | true | ATTAATA | -11.0449 | -0.0341925 | ATTAATA | -14.8745 | -0.0568716 | 2615 | true | ["ATTAATA", "TTAATAA", "ACATTAA", "TAATAAT", "TTAATAT", "TATTAAT", "AATAATA", "AATTAAT", "AAATATT", "AACATTA"] | ["ATTAATA", "TTAATAA", "TATTAAT", "AATTAAT", "TAATAAA", "ACATTAA", "TAATAAT", "TTAATAT", "TTAATAC", "TTTAATA"] |


**`constructs_with_agreeing_seed`**: `["APOB-Hs1", "APOB-Hs3", "RAD18"]`


**`constructs_excluded_for_seed_disagreement`**: `["APOB-Hs2", "APOB-Hs4", "Apob-Mm1", "Apob-Mm2"]`


**`recovered_seeds`**

```json
{
  "APOB-Hs1": "GAAAAAT",
  "APOB-Hs3": "CCTGAAA",
  "RAD18": "ATTAATA"
}
```


**`delivery_control_on_target_knockdown`**

| construct | on_target_gene | on_target_log2fc_HUH7 | on_target_log2fc_PLC/PRF/5 | on_target_log2fc_difference |
|---|---|---|---|---|
| APOB-Hs1 | APOB | -2.25717 | -2.9725 | 0.71533 |
| APOB-Hs2 | APOB | -2.88821 | -3.62991 | 0.741706 |
| APOB-Hs3 | APOB | -1.65043 | -2.78515 | 1.13472 |
| APOB-Hs4 | APOB | -2.30892 | -3.47992 | 1.171 |
| Apob-Mm1 | APOB | -1.31254 | -2.80182 | 1.48928 |
| Apob-Mm2 | APOB | -0.900635 | -1.86763 | 0.966994 |
| RAD18 | RAD18 | -1.74483 | -3.63971 | 1.89488 |


**`per_construct`**

| construct | status | recovered_site_7mer | on_target_gene | n_transcripts_shared_by_both_contexts | total_retrieved_abundance_HUH7 | total_retrieved_abundance_PLC | retrieved_abundance_ratio_HUH7_over_PLC | mean_log2fc_HUH7 | mean_log2fc_PLC | fit | observed_pool_ratio_HUH7_over_PLC | observed_pool_ratio_ci95 | observed_ratio_ci_excludes_1 | bootstrap_n_successful | predicted_ratio_by_rho | rho_at_which_equilibrium_matches_observed_ratio | independent_prediction_pool_ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| APOB-Hs1 | OK | GAAAAAT | APOB | 8738 | 37837.8 | 38078.8 | 0.993672 | -0.00400581 | 0.0046181 | {"pool_per_dose": [9.851698103239148, 10.196914422120075], "log10_pool_per_dose": [0.993511094792499, 1.0084687744898377], "amplitude_c_log2_per_unit_bound_fraction": 0.08174024104862358, "rss": 497.1642836728314, "n_observations": 17476, "sigma_pooled": 0.1686665425938758, "residual_sd_per_dose": [0.16510829470569752, 0.17217017270061796], "mean_bound_fraction_per_dose": [0.2417180176849227, 0.24587383645201383], "max_bound_fraction_per_dose": [0.9646907354924674, 0.965845301549458], "frac_sites_above_half_saturation_per_dose": [0.19203479056992448, 0.19798580910963606], "optimiser_converged": true, "nll": -31104.337635303127} | 0.966145 | [0.6046633432831504, 1.5632308805653479] | false | 300 | [{"rho": 0.0001, "M_molecules_per_cell": 8.0, "f_HUH7": 0.003874197520759324, "f_PLC": 0.0037531168100935182, "predicted_pool_ratio_equilibrium": 1.0322613754893466, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.0003, "M_molecules_per_cell": 23.999999999999996, "f_HUH7": 0.011655444003277577, "f_PLC": 0.011291245120889866, "predicted_pool_ratio_equilibrium": 1.0322549797199876, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.001, "M_molecules_per_cell": 80.0, "f_HUH7": 0.03923311670080688, "f_PLC": 0.03800831157168419, "predicted_pool_ratio_equilibrium": 1.0322246655659169, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.003, "M_molecules_per_cell": 240.0, "f_HUH7": 0.1209345057027916, "f_PLC": 0.11717585324005222, "predicted_pool_ratio_equilibrium": 1.0320770223455442, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.01, "M_molecules_per_cell": 800.0, "f_HUH7": 0.4400368409362575, "f_PLC": 0.4267793754850173, "predicted_pool_ratio_equilibrium": 1.0310639787505513, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.03, "M_molecules_per_cell": 2400.0, "f_HUH7": 1.6400021661170197, "f_PLC": 1.597424059310065, "predicted_pool_ratio_equilibrium": 1.0266542290751175, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.1, "M_molecules_per_cell": 8000.0, "f_HUH7": 10.568921089309633, "f_PLC": 10.439705066677675, "predicted_pool_ratio_equilibrium": 1.0123773633265178, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.3, "M_molecules_per_cell": 24000.0, "f_HUH7": 258.6873981319968, "f_PLC": 258.4785011170188, "predicted_pool_ratio_equilibrium": 1.000808179458157, "predicted_pool_ratio_independent": 1.0}, {"rho": 1.0, "M_molecules_per_cell": 80000.0, "f_HUH7": 43632.372984431495, "f_PLC": 43503.35198042799, "predicted_pool_ratio_equilibrium": 1.0029657715585123, "predicted_pool_ratio_independent": 1.0}, {"rho": 3.0, "M_molecules_per_cell": 240000.0, "f_HUH7": 202890.93853390624, "f_PLC": 202754.66997768567, "predicted_pool_ratio_equilibrium": 1.0006720859067542, "predicted_pool_ratio_independent": 1.0}, {"rho": 10.0, "M_molecules_per_cell": 800000.0, "f_HUH7": 762622.1296862485, "f_PLC": 762469.9028759087, "predicted_pool_ratio_equilibrium": 1.0001996495989751, "predicted_pool_ratio_independent": 1.0}] | null | 1 |
| APOB-Hs3 | OK | CCTGAAA | APOB | 6584 | 26771.8 | 26389.9 | 1.01447 | -0.0094323 | -0.0180739 | {"pool_per_dose": [0.012777690582950469, 0.05222164935135331], "log10_pool_per_dose": [-1.8935476326966176, -1.282149415682749], "amplitude_c_log2_per_unit_bound_fraction": 0.09722182495171067, "rss": 287.3011300769305, "n_observations": 13168, "sigma_pooled": 0.14770961228824223, "residual_sd_per_dose": [0.1383824403500088, 0.15650299663461387], "mean_bound_fraction_per_dose": [0.1735697009491658, 0.3152679227809737], "max_bound_fraction_per_dose": [0.9811992840100462, 0.9953335395659902], "frac_sites_above_half_saturation_per_dose": [0.1295565006075334, 0.2735419198055893], "optimiser_converged": true, "nll": -25183.89233072842} | 0.244682 | [0.12557459862672907, 0.4506319699835748] | true | 300 | [{"rho": 0.0001, "M_molecules_per_cell": 8.0, "f_HUH7": 6.26771035816561e-06, "f_PLC": 6.356607748780637e-06, "predicted_pool_ratio_equilibrium": 0.986014963620796, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.0003, "M_molecules_per_cell": 23.999999999999996, "f_HUH7": 1.8936918305431604e-05, "f_PLC": 1.920873422141506e-05, "predicted_pool_ratio_equilibrium": 0.9858493582736744, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.001, "M_molecules_per_cell": 80.0, "f_HUH7": 6.466878500123484e-05, "f_PLC": 6.56324349050036e-05, "predicted_pool_ratio_equilibrium": 0.985317474429167, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.003, "M_molecules_per_cell": 240.0, "f_HUH7": 0.00020704616367830833, "f_PLC": 0.00021038599657198167, "predicted_pool_ratio_equilibrium": 0.9841252129509929, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.01, "M_molecules_per_cell": 800.0, "f_HUH7": 0.0008441633984189692, "f_PLC": 0.0008592622923336742, "predicted_pool_ratio_equilibrium": 0.9824280734190048, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.03, "M_molecules_per_cell": 2400.0, "f_HUH7": 0.004102255048005881, "f_PLC": 0.004158818308956097, "predicted_pool_ratio_equilibrium": 0.9863991988232799, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.1, "M_molecules_per_cell": 8000.0, "f_HUH7": 0.05017072841497987, "f_PLC": 0.050593265656903655, "predicted_pool_ratio_equilibrium": 0.9916483501027744, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.3, "M_molecules_per_cell": 24000.0, "f_HUH7": 18.651989424889138, "f_PLC": 21.269418722553638, "predicted_pool_ratio_equilibrium": 0.8769393121736311, "predicted_pool_ratio_independent": 1.0}, {"rho": 1.0, "M_molecules_per_cell": 80000.0, "f_HUH7": 53376.46079178703, "f_PLC": 53719.871969770786, "predicted_pool_ratio_equilibrium": 0.9936073716226093, "predicted_pool_ratio_independent": 1.0}, {"rho": 3.0, "M_molecules_per_cell": 240000.0, "f_HUH7": 213357.87345095142, "f_PLC": 213701.50449179887, "predicted_pool_ratio_equilibrium": 0.9983920045782334, "predicted_pool_ratio_independent": 1.0}, {"rho": 10.0, "M_molecules_per_cell": 800000.0, "f_HUH7": 773348.0315368385, "f_PLC": 773691.9493538127, "predicted_pool_ratio_equilibrium": 0.9995554848189109, "predicted_pool_ratio_independent": 1.0}] | null | 1 |
| RAD18 | OK | ATTAATA | RAD18 | 6285 | 27310.6 | 27739.6 | 0.984532 | -0.00399362 | -0.0109345 | {"pool_per_dose": [3.575868323165877, 9.79836923861333], "log10_pool_per_dose": [0.5533815180726072, 0.9911538012430706], "amplitude_c_log2_per_unit_bound_fraction": 0.1273413148933099, "rss": 263.04074031205516, "n_observations": 12570, "sigma_pooled": 0.14465847094090492, "residual_sd_per_dose": [0.13259800199355684, 0.1558094233660314], "mean_bound_fraction_per_dose": [0.0897788337466685, 0.1868334402744355], "max_bound_fraction_per_dose": [0.587505496083055, 0.7960310883623868], "frac_sites_above_half_saturation_per_dose": [0.002863961813842482, 0.07239459029435164], "optimiser_converged": true, "nll": -24302.582673595563} | 0.364945 | [0.2088660978517566, 0.5719790095564452] | true | 300 | [{"rho": 0.0001, "M_molecules_per_cell": 8.0, "f_HUH7": 0.009129073320435721, "f_PLC": 0.009292981515896272, "predicted_pool_ratio_equilibrium": 0.9823621519982392, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.0003, "M_molecules_per_cell": 23.999999999999996, "f_HUH7": 0.027435170411159893, "f_PLC": 0.02792809818851274, "predicted_pool_ratio_equilibrium": 0.982350112992814, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.001, "M_molecules_per_cell": 80.0, "f_HUH7": 0.09201188648265843, "f_PLC": 0.09366887900617787, "predicted_pool_ratio_equilibrium": 0.9823101061836114, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.003, "M_molecules_per_cell": 240.0, "f_HUH7": 0.2808964603743983, "f_PLC": 0.28598314247096823, "predicted_pool_ratio_equilibrium": 0.9822133498757315, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.01, "M_molecules_per_cell": 800.0, "f_HUH7": 0.9950500500668711, "f_PLC": 1.0132327348410253, "predicted_pool_ratio_equilibrium": 0.9820547795694669, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.03, "M_molecules_per_cell": 2400.0, "f_HUH7": 3.547879639241021, "f_PLC": 3.6104469702239435, "predicted_pool_ratio_equilibrium": 0.9826704750135018, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.1, "M_molecules_per_cell": 8000.0, "f_HUH7": 22.055978381393523, "f_PLC": 22.309336080131757, "predicted_pool_ratio_equilibrium": 0.9886434227433657, "predicted_pool_ratio_independent": 1.0}, {"rho": 0.3, "M_molecules_per_cell": 24000.0, "f_HUH7": 1137.9030141742383, "f_PLC": 1080.3278239786723, "predicted_pool_ratio_equilibrium": 1.0532941843370522, "predicted_pool_ratio_independent": 1.0}, {"rho": 1.0, "M_molecules_per_cell": 80000.0, "f_HUH7": 53301.57860775254, "f_PLC": 52923.64299167895, "predicted_pool_ratio_equilibrium": 1.0071411489215323, "predicted_pool_ratio_independent": 1.0}, {"rho": 3.0, "M_molecules_per_cell": 240000.0, "f_HUH7": 213017.59998936206, "f_PLC": 212628.25191095995, "predicted_pool_ratio_equilibrium": 1.0018311210993973, "predicted_pool_ratio_independent": 1.0}, {"rho": 10.0, "M_molecules_per_cell": 800000.0, "f_HUH7": 772887.581304739, "f_PLC": 772494.8445624234, "predicted_pool_ratio_equilibrium": 1.0005084004703462, "predicted_pool_ratio_independent": 1.0}] | null | 1 |


**`observed_pool_ratios`**: `[0.9661450214653118, 0.24468186550334106, 0.36494525120303956]`


**`pooled_pool_ratio_ci95`**: `[0.3238770545400938, 0.608247752392519]`


### `e2_redistribution`  (OK)

seed `0`, wall clock `22.0555` s, recorded `2026-09-04T19:43:44Z`

| quantity | value |
|---|---|
| `source_of_K` | ViennaRNA ddG on GENCODE v50 3'UTRs |
| `source_of_x` | GSE5814 mock Cy3 channel, real HeLa abundance |
| `n_draws` | 1200 |
| `n_transcripts_per_draw` | 120 |
| `claim_A_d_o_i_d_K_t_positive_violations` | 0 |
| `claim_B_d_o_t_d_K_t_negative_violations` | 0 |
| `min_margin_1_minus_u_over_D` | 0.0898443 |
| `mean_margin_1_minus_u_over_D` | 0.993085 |
| `max_d_o_t_d_K_t` | -1.4354e-32 |
| `min_d_o_i_d_K_t_offtarget_sum` | 1.4259e-32 |
| `all_margins_strictly_positive` | true |


**`rho_sampled_log10_uniform_over`**: `[-3, 1]`


### `e3_pairwise_limit`  (OK)

seed `0`, wall clock `18.3421` s, recorded `2026-09-04T19:44:02Z`

| quantity | value |
|---|---|
| `source_of_K` | ViennaRNA ddG on GENCODE v50 3'UTRs |
| `source_of_x` | GSE5814 mock Cy3 channel, real HeLa abundance |
| `n_transcripts` | 4000 |
| `sum_x` | 22373.4 |
| `n_decades_swept` | 9 |
| `loglog_slope_all` | -0.988055 |
| `loglog_slope_stderr_all` | 0.00429376 |
| `loglog_r2_all` | 0.999868 |
| `fit_window_rule` | points whose maximum relative occupancy error lies in (1e-12, 1e-2): above double-precision floor and inside the asymptotic regime |
| `n_points_in_fit_window` | 7 |
| `loglog_slope_asymptotic_window` | -0.997808 |
| `loglog_slope_stderr_asymptotic_window` | 7.9022e-04 |
| `loglog_r2_asymptotic_window` | 0.999997 |
| `loglog_slope_MEDIAN_transcript` | -1.99863 |
| `loglog_slope_stderr_MEDIAN_transcript` | 0.00249415 |
| `loglog_r2_MEDIAN_transcript` | 0.999997 |
| `n_points_in_fit_window_median` | 4 |
| `max_slope_consistent_with_minus_2` | false |
| `median_slope_consistent_with_minus_2` | true |
| `WHY_THE_MAX_AND_THE_MEDIAN_DIFFER` | The expansion o_eq/o_pw = 1 - S K /(M(K+M)) + ... is O(rho^-2) only where K << M. On the real transcriptome K spans about twenty decades, so at any finite rho a tail of transcripts has K >> M, and for those the leading term is instead (f-M)/M = -S/M = -1/rho. The MAXIMUM relative error is therefo... |
| `predicted_slope` | -2 |
| `f_converges_to_M_minus_sum_x_not_M` | true |
| `final_abs_f_minus_M` | 22352.1 |
| `final_abs_f_minus_M_minus_sum_x` | 21.3027 |
| `assumptions_of_the_expansion` | requires f > 0, K_j + f bounded away from zero for every j, rho large enough that sum_j o_j is within O(1/rho) of sum_j x_j, AND K_j << M for the transcript being expanded. The last one is the binding constraint on real data and is measured per rho in the sweep. |


**`sweep`**

| rho | M | f | M_minus_sum_x | abs_f_minus_M | abs_f_minus_M_minus_S | max_rel_occupancy_error | median_rel_occupancy_error | frac_transcripts_with_K_above_M | max_K_over_M |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 22373.4 | 6081.36 | 0 | 16292.1 | 6081.36 | 0.728188 | 0.0229334 | 0.1725 | 1.4322e+11 |
| 10 | 223734 | 203558 | 201361 | 20176.6 | 2196.84 | 0.090181 | 8.7524e-05 | 0.0735 | 1.4322e+10 |
| 100 | 2.2373e+06 | 2.2159e+06 | 2.2150e+06 | 21483.7 | 889.671 | 0.00960235 | 8.5688e-07 | 0.028 | 1.4322e+09 |
| 1000 | 2.2373e+07 | 2.2351e+07 | 2.2351e+07 | 22092.6 | 280.824 | 9.8745e-04 | 8.7363e-09 | 0.00825 | 1.4322e+08 |
| 10000 | 2.2373e+08 | 2.2371e+08 | 2.2371e+08 | 22243.3 | 130.105 | 9.9418e-05 | 8.7882e-11 | 0.00475 | 1.4322e+07 |
| 100000 | 2.2373e+09 | 2.2373e+09 | 2.2373e+09 | 22276.3 | 97.1437 | 9.9566e-06 | 8.8007e-13 | 0.004 | 1.4322e+06 |
| 1.0000e+06 | 2.2373e+10 | 2.2373e+10 | 2.2373e+10 | 22303.9 | 69.5399 | 9.9688e-07 | 8.7708e-15 | 0.003 | 143216 |
| 1.0000e+07 | 2.2373e+11 | 2.2373e+11 | 2.2373e+11 | 22336.8 | 36.6539 | 9.9829e-08 | 2.2204e-16 | 0.002 | 14321.6 |
| 1.0000e+08 | 2.2373e+12 | 2.2373e+12 | 2.2373e+12 | 22352.1 | 21.3027 | 9.9835e-09 | 0 | 0.0015 | 1432.16 |


**`fit_window_rho_values`**: `[100.0, 1000.0, 10000.0, 100000.0, 1000000.0, 10000000.0, 100000000.0]`


### `e1_solver_correctness`  (OK)

seed `0`, wall clock `18.9688` s, recorded `2026-09-04T19:43:22Z`

| quantity | value |
|---|---|
| `source_of_K` | ViennaRNA ddG on GENCODE v50 3'UTRs (features.parquet) |
| `seed_code_benchmark_conservation_residual` | 4.2633e-14 |
| `seed_code_benchmark_conservation_residual_expected` | 4.2600e-14 |
| `seed_code_benchmark_conservation_residual_matches` | true |
| `seed_code_benchmark_gradient_worst_relative_error` | 1.0742e-07 |
| `seed_code_benchmark_gradient_expected` | 1.0700e-07 |
| `seed_code_benchmark_gradient_matches` | true |
| `seed_code_benchmark_note` | reproduces the value that shipped with the seed code, on the seed code's own random draws, confirming that the refactor into src/riscpool/ left the mathematics unchanged |
| `n_gradient_coordinates_resolvable` | 35 |
| `n_gradient_coordinates_not_resolvable` | 0 |
| `not_resolvable_note` | a central difference is only meaningful when the two loss evaluations differ by more than double-precision cancellation noise. Coordinates failing that test are excluded from the worst-case statistic and counted here instead of being allowed to report a spurious relative error of 1. |
| `worst_relative_gradient_error_resolvable_only` | 1.5658e-04 |
| `worst_error_relative_to_gradient_norm` | 2.3040e-07 |
| `worst_error_relative_to_gradient_norm_note` | |finite difference - implicit gradient| divided by the largest gradient component. This is the measure that says whether the implicit gradients are right; a large per-coordinate RELATIVE error on a component that is itself ~0 does not. |
| `n_directional_derivative_checks` | 8 |
| `worst_directional_derivative_relative_error` | 1.9233e-06 |
| `median_relative_gradient_error_resolvable_only` | 2.3335e-09 |
| `source_of_x` | GSE5814 mock Cy3 channel (hela_abundance.parquet) |
| `n_batches` | 24 |
| `n_transcripts_per_batch` | 400 |
| `max_abs_residual_F_of_f` | 9.0949e-13 |
| `max_abs_conservation_closure` | 9.0949e-13 |
| `f_strictly_bracketed_in_0_M` | true |
| `gradient_coordinate_selection_rule` | the n_coords/3 coordinates of each of K, x and M carrying the largest analytic gradient magnitude. Stated in advance. A gradient component that is numerically zero cannot be checked against a difference quotient at double precision. |
| `n_gradient_coordinates_checked` | 35 |
| `worst_relative_gradient_error` | 1.5658e-04 |
| `median_relative_gradient_error` | 2.3335e-09 |
| `conditioning_note` | K spans about 26 decades on the real feature pipeline, against roughly two decades for the uniform draws the seed code used. Central differences are correspondingly worse conditioned here, so the tolerance is 1e-4 rather than the 1e-6 that the seed code's own distribution supports. The seed bench... |
| `f_monotone_increasing_in_M` | true |
| `occupancy_monotone_nondecreasing_in_M` | true |
| `tolerance_residual` | 1.0000e-09 |
| `tolerance_gradient_relative` | 1.0000e-04 |
| `passes_residual_tolerance` | true |
| `tolerance_gradient_relative_real_data` | 0.001 |
| `passes_gradient_tolerance` | true |
| `gradient_pass_criterion` | worst error relative to the gradient norm AND worst directional-derivative relative error both below 1e-3. That tolerance is looser than the 1.07e-7 the seed code achieves on its own uniform draws, and deliberately so: on the real pipeline K spans decades and the loss is O(1e4), so a double-preci... |
| `worst_per_coordinate_relative_error_for_reference` | 1.5658e-04 |


**`directional_derivative_checks`**

| finite_difference | implicit_gradient | relative_error |
|---|---|---|
| 66656.6 | 66656.6 | 7.6378e-07 |
| -3.1185e+06 | -3.1185e+06 | 7.1066e-07 |
| 1.2067e+06 | 1.2067e+06 | 4.7911e-07 |
| -4.0596e+06 | -4.0596e+06 | 1.8784e-06 |
| -1.8465e+06 | -1.8466e+06 | 1.9233e-06 |
| -3.7078e+06 | -3.7078e+06 | 1.0839e-06 |
| -4.0184e+06 | -4.0184e+06 | 1.5277e-06 |
| 2.9683e+06 | 2.9683e+06 | 6.3816e-07 |


**`gradient_checks`**

| parameter | finite_difference | implicit_gradient | relative_error | central_difference_resolvable | step_eps | error_relative_to_gradient_norm |
|---|---|---|---|---|---|---|
| K | -634739 | -634739 | 6.0251e-09 | true | 2.6674e-09 | 6.0251e-09 |
| K | 87529.8 | 87529.8 | 4.0026e-08 | true | 2.8622e-09 | 5.5195e-09 |
| K | 50896.4 | 50896.4 | 1.1772e-08 | true | 1.3354e-08 | 9.4397e-10 |
| K | 48525.4 | 48525.4 | 1.4736e-07 | true | 2.0890e-09 | 1.1266e-08 |
| K | 31721.1 | 31721.2 | 3.3227e-06 | true | 6.8379e-11 | 1.6605e-07 |
| K | 20560.6 | 20560.6 | 1.6188e-07 | true | 7.6852e-10 | 5.2438e-09 |
| K | 19254.6 | 19254.6 | 1.9260e-07 | true | 7.2860e-10 | 5.8423e-09 |
| K | 15014 | 15014 | 4.2821e-08 | true | 6.9360e-09 | 1.0129e-09 |
| K | 10753.6 | 10753.6 | 3.2670e-08 | true | 1.7911e-08 | 5.5348e-10 |
| K | 4320.83 | 4320.83 | 4.1897e-08 | true | 2.3120e-09 | 2.8520e-10 |
| K | 3473.39 | 3473.39 | 4.3105e-07 | true | 5.2568e-09 | 2.3588e-09 |
| K | 1886.64 | 1886.65 | 5.7206e-06 | true | 5.6787e-10 | 1.7004e-08 |
| K | 1308.54 | 1308.54 | 6.7596e-07 | true | 2.9753e-09 | 1.3935e-09 |
| K | 1225.44 | 1225.44 | 1.5412e-07 | true | 3.5680e-08 | 2.9754e-10 |
| K | 933.864 | 934.01 | 1.5658e-04 | true | 6.7503e-11 | 2.3040e-07 |
| K | 732.107 | 732.107 | 1.1487e-07 | true | 1.3173e-08 | 1.3249e-10 |
| x | 289.069 | 289.069 | 2.0454e-10 | true | 1.4686e-04 | 9.3150e-14 |
| x | 254.375 | 254.375 | 2.8107e-10 | true | 1.2878e-04 | 1.1264e-13 |
| x | 251.507 | 251.507 | 1.4333e-10 | true | 1.2833e-04 | 5.6794e-14 |
| x | 208.176 | 208.176 | 8.8766e-11 | true | 1.3986e-04 | 2.9113e-14 |
| x | 205.18 | 205.18 | 1.4048e-10 | true | 1.2751e-04 | 4.5409e-14 |
| x | 159.464 | 159.464 | 9.9477e-10 | true | 8.1229e-05 | 2.4991e-13 |
| x | 154.247 | 154.247 | 6.8962e-10 | true | 7.9738e-05 | 1.6758e-13 |
| x | 146.543 | 146.543 | 1.3798e-09 | true | 8.1559e-05 | 3.1857e-13 |
| x | 117.657 | 117.657 | 1.1788e-09 | true | 6.1035e-05 | 2.1851e-13 |
| x | 105.235 | 105.235 | 3.2813e-10 | true | 5.6666e-05 | 5.4402e-14 |
| x | 104.269 | 104.269 | 2.3335e-09 | true | 5.3705e-05 | 3.8332e-13 |
| x | 99.9627 | 99.9627 | 2.4126e-10 | true | 5.2259e-05 | 3.7996e-14 |
| x | 93.366 | 93.366 | 4.7975e-10 | true | 5.3466e-05 | 7.0567e-14 |
| x | 91.4815 | 91.4815 | 6.1204e-10 | true | 4.7208e-05 | 8.8209e-14 |
| x | 85.4646 | 85.4646 | 1.2060e-09 | true | 5.6362e-05 | 1.6238e-13 |
| x | -85.2864 | -85.2866 | 2.8173e-06 | true | 4.7937e-08 | 3.7855e-10 |
| M | 86.7169 | 86.7169 | 7.0825e-10 | true | 1.1755e-04 | 9.6759e-14 |
| M | 4.64023 | 4.64023 | 2.1525e-10 | true | 0.00331685 | 1.5736e-15 |
| M | 2.93393 | 2.93393 | 1.0541e-09 | true | 0.00244365 | 4.8725e-15 |


### `e8_huesken_efficacy`  (OK)

seed `0`, wall clock `9.312` s, recorded `2026-09-05T06:39:12Z`

| quantity | value |
|---|---|
| `OFF_TARGET_CLAIM` | NONE. This dataset observes on-target knockdown only. No off-target conclusion of any kind is drawn from it, and none may be drawn from these numbers. |
| `dataset` | Huesken et al. Nat Biotechnol 2005;23:995-1001, redistributed in the OligoFormer repository |
| `n_sirnas_used` | 2361 |
| `n_target_genes` | 30 |
| `n_features` | 12 |
| `split` | GroupKFold by target gene; no gene appears in both train and test in any fold |
| `n_splits` | 5 |
| `training_steps` | 600 |
| `learning_rate` | 0.003 |
| `M_pool_units` | 1 |
| `M_note` | dimensionless; the efficacy assay carries no absolute pool scale, so K is expressed in units of the pool |
| `mean_spearman_heldout_genes` | 0.479484 |
| `sd_spearman_heldout_genes` | 0.0440352 |
| `mean_pearson_heldout_genes` | 0.46206 |
| `sd_pearson_heldout_genes` | 0.0365113 |
| `pooled_out_of_fold_spearman` | 0.479745 |
| `pooled_out_of_fold_spearman_p` | 3.5190e-136 |
| `pooled_out_of_fold_pearson` | 0.461296 |
| `pooled_out_of_fold_pearson_p` | 9.7041e-125 |
| `max_genes_shared_any_fold` | 0 |


**`d5_acquisition`**

```json
{
  "n_sirnas": 2361,
  "n_assigned_to_a_target_gene": 2361,
  "n_target_genes": 30,
  "n_tiled_sequences_searched": 26459,
  "efficacy_mean": 0.514468110777052,
  "efficacy_sd": 0.15002114559039798,
  "remaining_expression_pct_min": 0.0,
  "remaining_expression_pct_max": 100.0
}
```


**`feature_names`**: `["dg_duplex_full", "dg_5p_end", "dg_3p_end", "asymmetry", "dg_guide_selffold", "seed_pairing_stability", "gc_fraction", "gc_seed", "a_at_pos1", "u_at_pos1", "g_at_pos19", "c_at_pos19"]`


**`folds`**

| fold | n_train | n_test | n_train_genes | n_test_genes | genes_shared_between_train_and_test | test_genes | spearman | spearman_p | pearson | pearson_p | final_train_loss |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1871 | 490 | 24 | 6 | 0 | ["C6orf110", "HIP2", "Rn_cacnb1", "UBE2M", "UBE2V1", "Ufc1"] | 0.499262 | 2.9895e-32 | 0.465671 | 9.6495e-28 | 0.00996164 |
| 1 | 1871 | 490 | 24 | 6 | 0 | ["Rn_Mmp7_1", "Rn_TCAP", "TC10", "UBE2C", "UBE2G1", "UBE2J1"] | 0.44739 | 1.7236e-25 | 0.459864 | 5.1839e-27 | 0.00923825 |
| 2 | 1880 | 481 | 24 | 6 | 0 | ["HSPC150", "NOG", "RAB6IP1", "Rn_Mmp7_2", "UBE2B", "UBE2L3"] | 0.444904 | 9.2757e-25 | 0.42598 | 1.2629e-22 | 0.0089944 |
| 3 | 1909 | 452 | 24 | 6 | 0 | ["CDC34", "P2RX3", "Rn_Fxyd6", "SOST", "UBE2D3", "UBE2E3"] | 0.457991 | 8.0725e-25 | 0.438088 | 1.2784e-22 | 0.00936364 |
| 4 | 1913 | 448 | 24 | 6 | 0 | ["FLJ11011", "Rn_P2rx2", "UBE2I", "UBE2L6", "UBE2N", "UBE2S"] | 0.547875 | 1.8612e-36 | 0.520695 | 1.6974e-32 | 0.00973547 |


### `e6_sim_interaction_recovery`  (OK)

seed `0`, wall clock `172.464` s, recorded `2026-09-04T08:17:28Z`

| quantity | value |
|---|---|
| `SIMULATION_ONLY` | Ground-truth K* is generated, not measured. Nothing in this experiment is evidence about any real cell, transcript or siRNA. It validates the training method under a known generating process and nothing else. |
| `sim_n_rho` | 4 |
| `sim_training_steps` | 350 |
| `sim_batch_train` | 250 |
| `sim_batch_test` | 60 |
| `sim_n_transcripts` | 40 |


**`sim_rho_values`**: `[0.005, 0.05, 0.5, 5.0]`


**`sim_seeds`**: `[0, 1, 2, 3, 4]`


**`sim_per_run`**

| rho | seed | sim_spearman_offtarget_equilibrium_trained | sim_spearman_offtarget_pairwise_trained | sim_spearman_allpairs_equilibrium_trained | sim_spearman_allpairs_pairwise_trained | sim_gap_equilibrium_minus_pairwise |
|---|---|---|---|---|---|---|
| 0.005 | 0 | 0.835815 | 0.486344 | 0.827094 | 0.482095 | 0.349471 |
| 0.005 | 1 | 0.934071 | 0.29122 | 0.922513 | 0.292566 | 0.642852 |
| 0.005 | 2 | 0.962513 | 0.343921 | 0.950499 | 0.341102 | 0.618592 |
| 0.005 | 3 | 0.915337 | 0.615603 | 0.90673 | 0.60758 | 0.299734 |
| 0.005 | 4 | 0.908022 | 0.605122 | 0.896029 | 0.591884 | 0.3029 |
| 0.05 | 0 | 0.995883 | 0.922786 | 0.985058 | 0.913942 | 0.0730974 |
| 0.05 | 1 | 0.994301 | 0.865671 | 0.98332 | 0.856586 | 0.12863 |
| 0.05 | 2 | 0.994323 | 0.921961 | 0.983007 | 0.912405 | 0.0723627 |
| 0.05 | 3 | 0.993047 | 0.920845 | 0.982911 | 0.910029 | 0.0722013 |
| 0.05 | 4 | 0.993861 | 0.901862 | 0.981297 | 0.888518 | 0.0919997 |
| 0.5 | 0 | 0.998812 | 0.996359 | 0.987894 | 0.985042 | 0.00245298 |
| 0.5 | 1 | 0.998967 | 0.995901 | 0.987785 | 0.984924 | 0.00306586 |
| 0.5 | 2 | 0.998631 | 0.995967 | 0.987436 | 0.984773 | 0.0026637 |
| 0.5 | 3 | 0.998918 | 0.996925 | 0.988509 | 0.9863 | 0.00199261 |
| 0.5 | 4 | 0.998983 | 0.995972 | 0.986752 | 0.983846 | 0.00301056 |
| 5 | 0 | 0.979927 | 0.975428 | 0.968498 | 0.964595 | 0.00449856 |
| 5 | 1 | 0.938878 | 0.924086 | 0.928272 | 0.914401 | 0.0147918 |
| 5 | 2 | 0.957402 | 0.952855 | 0.947087 | 0.942157 | 0.00454714 |
| 5 | 3 | 0.94685 | 0.95831 | 0.936541 | 0.947422 | -0.01146 |
| 5 | 4 | 0.987539 | 0.975627 | 0.974666 | 0.962461 | 0.0119114 |


**`sim_summary_by_rho`**

| rho | n_seeds | sim_mean_spearman_equilibrium_trained | sim_sd_spearman_equilibrium_trained | sim_mean_spearman_pairwise_trained | sim_sd_spearman_pairwise_trained | sim_mean_gap | sim_sd_gap | sim_gap_positive_in_all_seeds |
|---|---|---|---|---|---|---|---|---|
| 0.005 | 5 | 0.911152 | 0.0470805 | 0.468442 | 0.147962 | 0.44271 | 0.17297 | true |
| 0.05 | 5 | 0.994283 | 0.00103298 | 0.906625 | 0.0244871 | 0.0876582 | 0.024405 | true |
| 0.5 | 5 | 0.998862 | 1.4531e-04 | 0.996225 | 4.3125e-04 | 0.00263714 | 4.3968e-04 | true |
| 5 | 5 | 0.962119 | 0.0209693 | 0.957261 | 0.0211453 | 0.00485778 | 0.0101849 | false |


**`sim_pilot_for_comparison`**

```json
{
  "rho_0.005": {
    "equilibrium": 0.954,
    "pairwise": 0.547
  },
  "rho_5.0": {
    "equilibrium": 0.99,
    "pairwise": 0.976
  },
  "note": "pilot figures quoted from the build brief for comparison; the measured values above supersede them"
}
```


### `px0_audit_and_spec`  (OK)

seed `0`, wall clock `0.6527` s, recorded `2026-09-06T19:07:23Z`

| quantity | value |
|---|---|
| `frozen_spec_path` | results/positive_extensions/run_spec.json |


**`audit`**

```json
{
  "git_commit": "0da907be5184eea8732e44cd580e9efe431b8b0b",
  "git_dirty": true,
  "python": "3.13.12",
  "numpy": "2.4.2",
  "pandas": "3.0.2",
  "input_checksums": {
    "data/features.parquet": "12f7c2329bc72d4e",
    "data/accessibility_u8_u15.npz": "a5ed9111584d7220",
    "data/birmingham_response.parquet": "d63c5e8e76543bb7",
    "data/birmingham_sirna.parquet": "d8e5380bab9ea9ac"
  },
  "D2_used_for_model_selection_before": false,
  "D2_use_evidence": "no experiment in results/ consumes the D2 response: d2_birmingham records acquisition and d2b_birmingham_arrays records parsing only. The manuscript states D2 is an acquisition and that no experiment consumes it.",
  "candidate_universe": {
    "n_transcripts": 11304,
    "n_genes": 11304,
    "source": "GENCODE v50 canonical 3'UTRs, HeLa-expressed",
    "is_whole_transcriptome": false
  },
  "D1": {
    "n_constructs": 24,
    "n_families": 3
  },
  "D2": {
    "n_constructs_with_guide": 15,
    "n_distinct_guides": 12,
    "n_genes_measured": 19780,
    "n_genes_measured_with_canonical_utr": 7462,
    "response_definition": "log10(siRNA channel / mock channel), negative is repression"
  }
}
```


**`spec`**

```json
{
  "spec_version": 1,
  "frozen_utc": "2026-09-06T19:07:22Z",
  "purpose": "freezes the NEW analysis only; the historical archival study is not preregistered by this file",
  "datasets_by_accession": {
    "D1_training": "GSE5814",
    "D2_external": "E-MEXP-668",
    "note": "resolved by accession, not by repository D-number"
  },
  "rho_convention": {
    "definition": "rho = M / N_mRNA_whole_cell",
    "denominator": "total cellular mRNA count, NOT the retrieved competitor abundance sum",
    "verified_in": [
      "scripts/run_e5.py:total_x = float(n_mrna)",
      "src/riscpool/calibration.py:rho_from_alpha",
      "src/riscpool/real_experiments.py:score_construct"
    ]
  },
  "physics_preserved": {
    "dG_open": "-R*T*log(P_unpaired) >= 0",
    "dG_eff": "dG_duplex + dG_open",
    "K_site": "K_ref*exp((dG_eff-dG_ref)/(R*T))",
    "RT_kcal_per_mol": 0.61633008,
    "temperature_K": 310.15,
    "energy_units": "kcal/mol",
    "p_unpaired_floor": 1e-12,
    "aggregation": "1/K_j = sum_s 1/K_js (mutually exclusive sites)",
    "no_site_transcripts": "zero binding capacity, represented explicitly rather than as infinite K"
  },
  "experiment_A": {
    "model": "log K_js_corrected = log K_js_thermo + delta[class]",
    "anchor_class": "7mer-m8",
    "anchor_value": 0.0,
    "free_classes": [
      "8mer",
      "7mer-A1",
      "6mer"
    ],
    "init": 0.0,
    "bounds": [
      -3.0,
      3.0
    ],
    "score": "score_j = -log K_j = logsumexp_s(-log K_js_corrected)",
    "loss": "within-guide pairwise softplus(-t_jk*(score_j-score_k))",
    "y": "-log(expression ratio); larger y = stronger repression",
    "pairs_per_guide": 4096,
    "pair_seed": 1729,
    "drop_exact_ties": true,
    "balance": "equal weight per guide within family, then per family",
    "lambda_grid": [
      0.0,
      0.01,
      0.1,
      1.0
    ],
    "lambda_selection": "leave-one-family-out on D1 only; equal-family average of per-guide Spearman; ties to stronger regularisation",
    "dtype": "float64",
    "comparators": [
      "thermodynamic (current corrected baseline)",
      "class-only (no thermodynamic energy)",
      "thermodynamic + 3 class offsets"
    ],
    "primary_comparison": "model 3 minus model 1",
    "primary_metric": "equal-family average of within-guide Spearman between score_j and y_j",
    "bootstrap": {
      "n": 5000,
      "seed": 1730,
      "unit": "family cluster, paired, retaining all guides of a sampled family",
      "targets": "sampling variation across THIS set of families"
    },
    "sign_randomisation": {
      "unit": "family",
      "exact_if_families_le": 20,
      "draws_otherwise": 10000,
      "null": "family-level exchangeability and symmetry of the paired difference"
    },
    "eligible_population": "measured guide-gene pairs with a valid canonical UTR and >=1 canonical site under the shared response-independent pipeline; identical rows for all models",
    "external_exclusion_rule": "D2 families whose guide OR seed(2-8) exactly matches any D1 guide are removed from the primary external analysis and reported separately"
  },
  "experiment_B": {
    "reference": "the construct's full retrieved competitor set, which is a site-filtered universe and is NOT the whole transcriptome",
    "methods": [
      "full reference",
      "top-R truncation (omitted dropped)",
      "top-R + linear beta_omit = sum x_j/K_j",
      "top-R + saturable affinity-quantile bins"
    ],
    "bins": {
      "X_b": "sum_{j in b} x_j",
      "K_b": "X_b / sum_{j in b}(x_j/K_j)",
      "background_b": "X_b*f/(K_b+f)",
      "skip_zero_mass_bins": true
    },
    "rho_grid": [
      0.001,
      0.01,
      0.1,
      0.5,
      1.0,
      10.0
    ],
    "R_grid": [
      25,
      50,
      100,
      200,
      500
    ],
    "B_grid": [
      1,
      5,
      10,
      25,
      50,
      100,
      200
    ],
    "retrieval_order": "by x/K (weighted load), the project's existing rule; response-independent",
    "downstr
```


### `px_verify`  (OK)

seed `0`, wall clock `47.5714` s, recorded `2026-09-06T19:37:47Z`

| quantity | value |
|---|---|
| `n_checks` | 12 |
| `n_failed` | 0 |
| `verdict` | PASS |


**`checks`**

| check | ok | detail |
|---|---|---|
| features.build() with defaults is bit-identical to the committed features.parquet | true | max abs difference 0.0 |
| zero offsets reproduce the uncorrected thermodynamic score exactly (7mer-m8 anchor is inert) | true | max abs diff 0.0 |
| logsumexp site aggregation equals the direct 1/K = sum 1/K_js form | true | max abs diff 0.0 |
| no exact guide overlap between GSE5814 and E-MEXP-668 | true | [] |
| no exact seed(2-8) overlap between GSE5814 and E-MEXP-668 | true | [] |
| all three A comparators are scored on identical rows | true | {'M1_thermodynamic': 15, 'M2_class_only': 15, 'M3_thermo_plus_offsets': 15} |
| equilibrium and independent fractional occupancies rank identically within a construct (Proposition 1) | true | Spearman 1.0 |
| retained and omitted sets partition the reference exactly | true | 100 + 962 = 1062 |
| saturable bin masses sum to the omitted abundance (no mass lost or double counted) | true | bins 5280.864161017704 vs omitted 5280.864161017703 |
| primary effect recomputes from the saved per-family table | true | -0.00010597014274606278 vs -0.00010597014274608067 |
| frozen lambda is the strongest-regularisation maximiser as specified | true | 1.0 |
| no pre-existing result file was modified | true | [] |


### `pxa_affinity_correction`  (OK)

seed `0`, wall clock `5.441` s, recorded `2026-09-06T19:06:27Z`

| quantity | value |
|---|---|
| `WHAT_THIS_TESTS` | whether a three-parameter correction to per-site thermodynamic affinities improves within-guide repression ranking on guides that were never used to fit it. It does NOT test conservation coupling: for fixed affinities the equilibrium and independent fractional occupancies induce identical within-... |
| `D1_baseline_M1_equal_family_mean_spearman` | 0.0621751 |
| `fit_movement_diagnostic` | offsets_if_selected at each lambda shows how far the fit moves from zero. If the selected offsets are near zero the corrected model is numerically almost the baseline, and a null external effect means the correction did not move rather than that it moved and failed. |
| `secondary_paired_effect_M2_minus_M1` | 0.00680275 |
| `secondary_interpretation` | M2 uses site class alone and no thermodynamic energy. A positive M2 minus M1 means the ViennaRNA energies are not adding usable ranking information beyond the site class on these guides. |
| `primary_paired_effect_M3_minus_M1` | -1.0597e-04 |
| `bootstrap_n` | 5000 |
| `bootstrap_seed` | 1730 |
| `bootstrap_targets` | sampling variation across THIS set of 12 guide families, not across guides in general |
| `sign_randomisation_p` | 0.0170898 |
| `sign_randomisation_mode` | exact enumeration over 2^12 sign flips |
| `sign_randomisation_null` | family-level exchangeability and symmetry of the paired difference |
| `n_independent_families_external` | 12 |
| `supported_positive_result` | false |
| `CLAIM_SCOPE` | a positive result here supports better AFFINITIES, not added predictive value from coupling and not an identified rho |
| `LIMITATION_family_count` | 12 independent guide families support the external interval. Thousands of genes do not increase that number, and the interval is correspondingly unstable. |


**`frozen_before_external_evaluation`**

```json
{
  "lambda": 1.0,
  "offsets_thermo_plus_class": {
    "6mer": -0.02777371399140542,
    "7mer-A1": -0.0003700504164132457,
    "8mer": 0.0071827411837012585
  },
  "anchor": {
    "7mer-m8": 0.0
  },
  "class_only_constants": {
    "6mer": 0.008346200847129288,
    "7mer-A1": -0.0015471730788597482,
    "8mer": -0.004447652361237556
  },
  "optimiser_success": true,
  "n_iter": 2,
  "final_objective": 2.8121228315022466,
  "training_pairs_with_exact_response_ties_dropped": 65
}
```


**`lambda_selection_D1_leave_one_family_out`**

| lambda | loo_equal_family_mean_spearman | per_held_out_family | offsets_if_selected | offset_max_abs |
|---|---|---|---|---|
| 0 | 0.0440036 | {"MAPK14": 0.05603187333163011, "PIK3CB": 0.04048906437070515, "PLK1": 0.03548976811994774} | {"6mer": -2.9694780299936396, "7mer-A1": -1.9190179785495218, "8mer": 0.4017013869591871} | 2.96948 |
| 0.01 | 0.0530998 | {"MAPK14": 0.06109305292244409, "PIK3CB": 0.05585452404120643, "PLK1": 0.0423518450197046} | {"6mer": -1.310902755902361, "7mer-A1": -0.37843014651202955, "8mer": 0.3871742980309884} | 1.3109 |
| 0.1 | 0.0604101 | {"MAPK14": 0.06534367245332451, "PIK3CB": 0.06885178519364772, "PLK1": 0.04703473151957846} | {"6mer": -0.25020173340518004, "7mer-A1": -0.013760547723372105, "8mer": 0.06674290964294359} | 0.250202 |
| 1 | 0.0619837 | {"MAPK14": 0.06641235108913034, "PIK3CB": 0.0714748062131752, "PLK1": 0.0480638969861305} | {"6mer": -0.02777371399140542, "7mer-A1": -0.0003700504164132457, "8mer": 0.0071827411837012585} | 0.0277737 |


**`eligibility`**

```json
{
  "D1_families": [
    "MAPK14",
    "PIK3CB",
    "PLK1"
  ],
  "D1_constructs": [
    "MAPK14-193_parent",
    "MAPK14-193_pos01mut",
    "MAPK14-193_pos02mut",
    "MAPK14-193_pos03mut",
    "MAPK14-193_pos04mut",
    "MAPK14-193_pos05mut",
    "MAPK14-193_pos06mut",
    "MAPK14-193_pos07mut",
    "MAPK14-193_pos08mut",
    "MAPK14-193_pos09mut",
    "MAPK14-193_pos10mut",
    "MAPK14-193_pos11mut",
    "MAPK14-193_pos12mut",
    "MAPK14-193_pos13mut",
    "MAPK14-193_pos14mut",
    "MAPK14-193_pos15mut",
    "MAPK14-193_pos16mut",
    "MAPK14-193_pos17mut",
    "MAPK14-193_pos18mut",
    "MAPK14-193_pos19mut",
    "PIK3CB-6338_parent",
    "PIK3CB-6340_parent",
    "PLK1-319_parent",
    "PLK1-772_parent"
  ],
  "D1_eligible_pairs": 34679,
  "D2_families": [
    "ATTGGAA",
    "CAAATCT",
    "CACCGTA",
    "CACGATG",
    "CTTGATC",
    "GAACCTC",
    "GGTGAAG",
    "GTTGCTT",
    "TCTCCTG",
    "TTGAGGC",
    "TTGTAGC",
    "TTTTGGA"
  ],
  "D2_constructs": [
    "BIRM-ACAGCAAA-100nM",
    "BIRM-CAGGGCGG-100nM",
    "BIRM-GAAAGAGC-100nM",
    "BIRM-GAAAGGAT-100nM",
    "BIRM-GAGCAGAT-100nM",
    "BIRM-GAGGTTCT-100nM",
    "BIRM-GCACATGG-100nM",
    "BIRM-GCAGAGAG-100nM",
    "BIRM-GGAAAGAC-100nM",
    "BIRM-GGCCTTAG-100nM",
    "BIRM-GGCCTTAG-50nM",
    "BIRM-GTATGACA-100nM",
    "BIRM-GTATGACA-50nM",
    "BIRM-TGGTTTAC-100nM",
    "BIRM-TGGTTTAC-50nM"
  ],
  "D2_eligible_pairs": 31153
}
```


**`external_D2`**

```json
{
  "M1_thermodynamic": {
    "equal_family_mean_spearman": 0.028191425754754283,
    "per_construct": {
      "BIRM-ACAGCAAA-100nM": {
        "family": "CACGATG",
        "spearman": -0.008448027337262631,
        "n": 628
      },
      "BIRM-CAGGGCGG-100nM": {
        "family": "GGTGAAG",
        "spearman": 0.03723503267097548,
        "n": 2406
      },
      "BIRM-GAAAGAGC-100nM": {
        "family": "CACCGTA",
        "spearman": 0.009005136202474012,
        "n": 797
      },
      "BIRM-GAAAGGAT-100nM": {
        "family": "TTGTAGC",
        "spearman": 0.0633704701389495,
        "n": 1801
      },
      "BIRM-GAGCAGAT-100nM": {
        "family": "GTTGCTT",
        "spearman": 0.029043619412660867,
        "n": 1746
      },
      "BIRM-GAGGTTCT-100nM": {
        "family": "CTTGATC",
        "spearman": 0.0344656162363701,
        "n": 1960
      },
      "BIRM-GCACATGG-100nM": {
        "family": "GAACCTC",
        "spearman": 0.04678455789822533,
        "n": 1861
      },
      "BIRM-GCAGAGAG-100nM": {
        "family": "CAAATCT",
        "spearman": 0.05397745165731259,
        "n": 2505
      },
      "BIRM-GGAAAGAC-100nM": {
        "family": "TTTTGGA",
        "spearman": 0.03570799268232765,
        "n": 2983
      },
      "BIRM-GGCCTTAG-100nM": {
        "family": "TCTCCTG",
        "spearman": -0.024689090152281143,
        "n": 3119
      },
      "BIRM-GGCCTTAG-50nM": {
        "family": "TCTCCTG",
        "spearman": -0.0217680062200323,
        "n": 3119
      },
      "BIRM-GTATGACA-100nM": {
        "family": "TTGAGGC",
        "spearman": 0.03503037758197758,
        "n": 2289
      },
      "BIRM-GTATGACA-50nM": {
        "family": "TTGAGGC",
        "spearman": 0.03308416405654599,
        "n": 2289
      },
      "BIRM-TGGTTTAC-100nM": {
        "family": "ATTGGAA",
        "spearman": 0.02349574031097463,
        "n": 1825
      },
      "BIRM-TGGTTTAC-50nM": {
        "family": "ATTGGAA",
        "spearman": 0.029157333412852288,
        "n": 1825
      }
    },
    "per_family": {
      "CACGATG": -0.008448027337262631,
      "GGTGAAG": 0.03723503267097548,
      "CACCGTA": 0.009005136202474012,
      "TTGTAGC": 0.0633704701389495,
      "GTTGCTT": 0.029043619412660867,
      "CTTGATC": 0.0344656162363701,
      "GAACCTC": 0.04678455789822533,
      "CAAATCT": 0.05397745165731259,
      "TTTTGGA": 0.03570799268232765,
      "TCTCCTG": -0.023228548186156724,
      "TTGAGGC": 0.034057270819261784,
      "ATTGGAA": 0.02632653686191346
    }
  },
  "M2_class_only": {
    "equal_family_mean_spearman": 0.03499417971051843,
    "per_construct": {
      "BIRM-ACAGCAAA-100nM": {
        "family": "CACGATG",
        "spearman": -0.007462845286675412,
        "n": 628
      },
      "BIRM-CAGGGCGG-100nM": {
        "family": "GGTGAAG",
        "spearman": 0.023550658983968208,
        "n": 2406
      },
      "BIRM-GAAAGAGC-100nM": {
        "family": "CACCGTA",
        "spearman": 0.010634761233174975,
        "n": 797
      },
      "BIRM-GAAAGGAT-100nM": {
        "family": "TTGTAGC",
        "spearman": 0.05795138956656518,
        "n": 1801
      },
      "BIRM-GAGCAGAT-100nM": {
        "family": "GTTGCTT",
        "spearman": 0.05942979290224761,
        "n": 1746
      },
      "BIRM-GAGGTTCT-100nM": {
        "family": "CTTGATC",
        "spearman": 0.033835357845451275,
        "n": 1960
      },
      "BIRM-GCACATGG-100nM": {
        "family": "GAACCTC",
        "spearman": 0.05867864567855323,
        "n": 1861
      },
      "BIRM-GCAGAGAG-100nM": {
        "family": "CAAATCT",
        "spearman": 0.07574483821123415,
        "n": 2505
      },
      "BIRM-GGAAAGAC-100nM": {
        "family": "TTTTGGA",
        "spearman": 0.03479807452596516,
        "n": 2983
      },
      "BIRM-GGCCTTAG-100nM": {
        "family": "TCTCCTG",
        "spearman": 0.005335092323823042,
        "n": 3119
      },
      "BIRM-GGCCTTAG-50nM": {
        "family": "TCTCCTG",
        "spearman": 0.01102164371339
```


**`secondary_effect_ci95_family_cluster_bootstrap`**: `[-0.0005474987697613969, 0.014875356500546087]`


**`primary_effect_ci95_family_cluster_bootstrap`**: `[-0.00016748517717764307, -3.282881215787906e-05]`


**`per_family_paired_difference`**

```json
{
  "ATTGGAA": -5.775085224237961e-05,
  "CAAATCT": -0.00012346201694746206,
  "CACCGTA": 0.00019984181421765605,
  "CACGATG": -0.00020998698385942156,
  "CTTGATC": -0.00010684261632053216,
  "GAACCTC": -8.799619533520625e-05,
  "GGTGAAG": -5.194882866599304e-06,
  "GTTGCTT": -0.00010838125815505403,
  "TCTCCTG": -8.248646032316814e-05,
  "TTGAGGC": -0.00022283789719571012,
  "TTGTAGC": -0.00028310483786075924,
  "TTTTGGA": -0.0001834395260643315
}
```


### `pxb_approximation_cost`  (OK)

seed `0`, wall clock `311.754` s, recorded `2026-09-06T19:36:15Z`

| quantity | value |
|---|---|
| `WHAT_THIS_TESTS` | whether a saturable-bin background reproduces the full-reference solution and its gradients cheaply enough to be worth using. It is a computational claim, not evidence about coupling or rho. |
| `reference_universe` | the construct's full retrieved competitor set, a site-filtered universe of order a thousand transcripts. NOT the whole transcriptome. |
| `n_constructs` | 39 |
| `n_families` | 15 |
| `n_grid_rows` | 10518 |
| `n_exact_cases_excluded_from_selection` | 0 |
| `worst_full_reference_dimensionless_residual` | 7.2760e-12 |
| `frontier_path` | results/positive_extensions/B_frontier.csv |
| `grid_path` | results/positive_extensions/B_grid.csv |


**`development_families`**: `["ATTGGAA", "CACCGTA", "CTTGATC", "GGTGAAG", "MAPK14", "PLK1", "TCTCCTG", "TTGTAGC"]`


**`test_families`**: `["CAAATCT", "CACGATG", "GAACCTC", "GTTGCTT", "PIK3CB", "TTGAGGC", "TTTTGGA"]`


**`grid`**

```json
{
  "rho": [
    0.001,
    0.01,
    0.1,
    0.5,
    1.0,
    10.0
  ],
  "R": [
    25,
    50,
    100,
    200,
    500
  ],
  "B": [
    1,
    5,
    10,
    25,
    50,
    100,
    200
  ]
}
```


**`tolerances`**

```json
{
  "focal_rel_occupancy": 0.01,
  "grad_rel_l2": 0.01,
  "near_zero_abs": 1e-12,
  "note": "engineering targets, not biological efficacy thresholds"
}
```


**`full_reference_gradient_check`**

```json
{
  "per_coordinate": [
    {
      "coord": 0,
      "analytic": -0.0004996941592929102,
      "central_difference": -0.0004996941610491135
    },
    {
      "coord": 8,
      "analytic": -0.00013381712485391317,
      "central_difference": -0.0001338171032316815
    },
    {
      "coord": 16,
      "analytic": -2.1402693550799057e-06,
      "central_difference": -2.140260191296761e-06
    },
    {
      "coord": 24,
      "analytic": -0.0019707894960558385,
      "central_difference": -0.001970789489935676
    },
    {
      "coord": 32,
      "analytic": -0.002706470568946989,
      "central_difference": -0.0027064705684920476
    }
  ],
  "max_abs_rel_err": 4.28162107662935e-06
}
```


**`selected_on_development`**

```json
{
  "method": "bins",
  "R": 100,
  "B": 100,
  "cost_terms": 200,
  "n_dev_cases": 180,
  "worst_dev_focal_rel_err": 1.4930307266183918e-05,
  "worst_dev_grad_rel_err": 0.006227439349469615
}
```


**`held_out_result`**

```json
{
  "n_cases": 54,
  "n_families": 7,
  "median_focal_rel_err": 3.9968029100880555e-14,
  "p90_focal_rel_err": 5.098954171053748e-07,
  "worst_focal_rel_err": 1.160881721184173e-05,
  "median_grad_rel_err": 5.372371232584981e-05,
  "p90_grad_rel_err": 0.001097290949419895,
  "worst_grad_rel_err": 0.004661335177260349,
  "worst_dimensionless_residual": 2.6957602816679583e-16,
  "meets_both_tolerances_on_all_test_cases": true
}
```


**`timing`**

```json
{
  "construct": "MAPK14-193_pos04mut",
  "N_reference": 4919,
  "threads": 1,
  "dtype": "float64",
  "device": "cpu",
  "torch": "2.11.0+cu130",
  "warmup": 10,
  "repetitions": 50,
  "note": "timing repetitions are not independent biological samples",
  "full_forward": {
    "median_s": 0.007176482526119798,
    "p90_s": 0.007343936117831617,
    "min_s": 0.007023041951470077,
    "iqr_s": 5.092375795356929e-05
  },
  "full_forward_backward": {
    "median_s": 0.007353082473855466,
    "p90_s": 0.0074185528908856215,
    "min_s": 0.007280961028300226,
    "iqr_s": 6.3724146457389e-05
  },
  "selected_forward": {
    "median_s": 0.014909211953636259,
    "p90_s": 0.015163744846358896,
    "min_s": 0.01479929406195879,
    "iqr_s": 8.632999379187822e-05
  },
  "selected_forward_backward": {
    "median_s": 0.025598122971132398,
    "p90_s": 0.02587726302444935,
    "min_s": 0.025465015089139342,
    "iqr_s": 0.00013560522347688675
  },
  "setup_bin_construction": {
    "median_s": 0.0076358134974725544,
    "p90_s": 0.00771017000079155,
    "min_s": 0.007595204981043935,
    "iqr_s": 3.474074765108526e-05
  },
  "selected_forward_amortised": {
    "median_s": 0.0068878395250067115,
    "p90_s": 0.007075374433770776,
    "min_s": 0.006831299979239702,
    "iqr_s": 6.321989349089563e-05
  },
  "full_forward_amortised": {
    "median_s": 0.006507161015179008,
    "p90_s": 0.006655890063848346,
    "min_s": 0.006373608950525522,
    "iqr_s": 0.00015276312478818
  },
  "amortised_forward_speedup": 0.9447317974750098,
  "speedup_forward_backward_median": 0.2872508457806734,
  "solves_to_amortise_setup": null
}
```


## 3b. Mean +/- sd, per experiment

Every `mean_*` value in a result JSON, paired with its `sd_*` counterpart where one exists. Read from the JSONs, not typed.

| experiment | quantity | mean | sd | n |
|---|---|---|---|---|
| `d1_seed_validation` | `mean_t_parent_site_seed_preserving` | -5.15803 | - | - |
| `d1_seed_validation` | `mean_t_parent_site_seed_altering` | 4.65812 | - | - |
| `d2b_birmingham_arrays` | `per_construct[0].mean_log10ratio` | 0.00115597 | - | - |
| `d2b_birmingham_arrays` | `per_construct[1].mean_log10ratio` | -0.00128878 | - | - |
| `d2b_birmingham_arrays` | `per_construct[2].mean_log10ratio` | 7.0588e-04 | - | - |
| `d2b_birmingham_arrays` | `per_construct[3].mean_log10ratio` | -0.00100274 | - | - |
| `d2b_birmingham_arrays` | `per_construct[4].mean_log10ratio` | 0.00716054 | - | - |
| `d2b_birmingham_arrays` | `per_construct[5].mean_log10ratio` | 0.0123815 | - | - |
| `d2b_birmingham_arrays` | `per_construct[6].mean_log10ratio` | 0.00598467 | - | - |
| `d2b_birmingham_arrays` | `per_construct[7].mean_log10ratio` | 0.0101787 | - | - |
| `d2b_birmingham_arrays` | `per_construct[8].mean_log10ratio` | 0.00215458 | - | - |
| `d2b_birmingham_arrays` | `per_construct[9].mean_log10ratio` | 0.00236332 | - | - |
| `d2b_birmingham_arrays` | `per_construct[10].mean_log10ratio` | 0.00494147 | - | - |
| `d2b_birmingham_arrays` | `per_construct[11].mean_log10ratio` | 0.00114668 | - | - |
| `d2b_birmingham_arrays` | `per_construct[12].mean_log10ratio` | 1.9346e-04 | - | - |
| `d2b_birmingham_arrays` | `per_construct[13].mean_log10ratio` | -0.00164846 | - | - |
| `d2b_birmingham_arrays` | `per_construct[14].mean_log10ratio` | 6.5874e-04 | - | - |
| `d3_gencode` | `mean_utr3_len` | 1663.64 | - | - |
| `e5_hela_regime` | `hela_band_detail[0].mean_free_pool_f` | 9.5714e-05 | - | - |
| `e5_hela_regime` | `hela_band_detail[0].mean_f_over_M` | 6.3810e-06 | - | - |
| `e5_hela_regime` | `hela_band_detail[0].mean_offtarget_load_equilibrium` | 14.9999 | - | - |
| `e5_hela_regime` | `hela_band_detail[0].mean_offtarget_load_independent` | 2517.94 | - | - |
| `e5_hela_regime` | `hela_band_detail[1].mean_free_pool_f` | 9.5649e-05 | - | - |
| `e5_hela_regime` | `hela_band_detail[1].mean_f_over_M` | 6.3766e-06 | - | - |
| `e5_hela_regime` | `hela_band_detail[1].mean_offtarget_load_equilibrium` | 14.999 | - | - |
| `e5_hela_regime` | `hela_band_detail[1].mean_offtarget_load_independent` | 2517.94 | - | - |
| `e5_hela_regime` | `hela_band_detail[2].mean_free_pool_f` | 163626 | - | - |
| `e5_hela_regime` | `hela_band_detail[2].mean_f_over_M` | 0.962507 | - | - |
| `e5_hela_regime` | `hela_band_detail[2].mean_offtarget_load_equilibrium` | 6351.94 | - | - |
| `e5_hela_regime` | `hela_band_detail[2].mean_offtarget_load_independent` | 6366.49 | - | - |
| `e5_hela_regime` | `hela_band_detail[3].mean_free_pool_f` | 15479.7 | - | - |
| `e5_hela_regime` | `hela_band_detail[3].mean_f_over_M` | 0.091057 | - | - |
| `e5_hela_regime` | `hela_band_detail[3].mean_offtarget_load_equilibrium` | 5646.87 | - | - |
| `e5_hela_regime` | `hela_band_detail[3].mean_offtarget_load_independent` | 6366.49 | - | - |
| `e7_offtarget_ranking` | `positive_control_measured_repression_by_site_class.6mer.mean_of_median_log10ratio` | -0.00524896 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_measured_repression_by_site_class.6mer.mean_of_mean_log10ratio` | -0.0113176 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_measured_repression_by_site_class.7mer-A1.mean_of_median_log10ratio` | -0.0138089 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_measured_repression_by_site_class.7mer-A1.mean_of_mean_log10ratio` | -0.0298637 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_measured_repression_by_site_class.7mer-m8.mean_of_median_log10ratio` | -0.00925677 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_measured_repression_by_site_class.7mer-m8.mean_of_mean_log10ratio` | -0.0218289 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_measured_repression_by_site_class.8mer.mean_of_median_log10ratio` | -0.0255641 | - | 23 |
| `e7_offtarget_ranking` | `positive_control_measured_repression_by_site_class.8mer.mean_of_mean_log10ratio` | -0.053262 | - | 23 |
| `e7_offtarget_ranking` | `positive_control_detail[0].mean_log10ratio_with_site` | -0.00916545 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[1].mean_log10ratio_with_site` | -0.0320083 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[2].mean_log10ratio_with_site` | -0.0215201 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[3].mean_log10ratio_with_site` | -0.0555652 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[4].mean_log10ratio_with_site` | -0.0159601 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[5].mean_log10ratio_with_site` | -0.0094581 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[6].mean_log10ratio_with_site` | -0.0263006 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[7].mean_log10ratio_with_site` | -0.018832 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[8].mean_log10ratio_with_site` | -0.0460036 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[9].mean_log10ratio_with_site` | -0.014659 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[10].mean_log10ratio_with_site` | -0.0140429 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[11].mean_log10ratio_with_site` | -0.0277887 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[12].mean_log10ratio_with_site` | -0.0238589 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[13].mean_log10ratio_with_site` | -0.0417762 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[14].mean_log10ratio_with_site` | -0.0222942 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[15].mean_log10ratio_with_site` | -0.0061766 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[16].mean_log10ratio_with_site` | -0.0494916 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[17].mean_log10ratio_with_site` | -0.0143379 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[18].mean_log10ratio_with_site` | -0.0949984 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[19].mean_log10ratio_with_site` | -0.0170524 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[20].mean_log10ratio_with_site` | 6.2123e-04 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[21].mean_log10ratio_with_site` | -0.0208332 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[22].mean_log10ratio_with_site` | -0.0120651 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[23].mean_log10ratio_with_site` | -0.0380117 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[24].mean_log10ratio_with_site` | -0.00754464 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[25].mean_log10ratio_with_site` | -0.00769811 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[26].mean_log10ratio_with_site` | -0.0216015 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[27].mean_log10ratio_with_site` | -0.00587375 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[28].mean_log10ratio_with_site` | -0.0219288 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[29].mean_log10ratio_with_site` | -0.00938119 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[30].mean_log10ratio_with_site` | -0.0162271 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[31].mean_log10ratio_with_site` | -0.0502073 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[32].mean_log10ratio_with_site` | -0.0306475 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[33].mean_log10ratio_with_site` | -0.0628663 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[34].mean_log10ratio_with_site` | -0.02665 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[35].mean_log10ratio_with_site` | -0.0237634 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[36].mean_log10ratio_with_site` | -0.0233694 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[37].mean_log10ratio_with_site` | -0.0189427 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[38].mean_log10ratio_with_site` | -0.0234373 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[39].mean_log10ratio_with_site` | -0.010907 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[40].mean_log10ratio_with_site` | -0.033597 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[41].mean_log10ratio_with_site` | -0.0339495 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[42].mean_log10ratio_with_site` | -0.037406 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[43].mean_log10ratio_with_site` | -0.0172333 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[44].mean_log10ratio_with_site` | -0.0330601 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[45].mean_log10ratio_with_site` | -0.0610087 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[46].mean_log10ratio_with_site` | -0.0291487 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[47].mean_log10ratio_with_site` | -0.136544 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[48].mean_log10ratio_with_site` | -0.0373393 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[49].mean_log10ratio_with_site` | -0.0115928 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[50].mean_log10ratio_with_site` | -0.0328512 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[51].mean_log10ratio_with_site` | -0.0245204 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[52].mean_log10ratio_with_site` | -0.0597268 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[53].mean_log10ratio_with_site` | -0.0184798 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[54].mean_log10ratio_with_site` | -0.00872409 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[55].mean_log10ratio_with_site` | -0.0304744 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[56].mean_log10ratio_with_site` | -0.0194705 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[57].mean_log10ratio_with_site` | -0.0527519 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[58].mean_log10ratio_with_site` | -0.0148499 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[59].mean_log10ratio_with_site` | -0.0107943 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[60].mean_log10ratio_with_site` | -0.0336392 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[61].mean_log10ratio_with_site` | -0.0237406 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[62].mean_log10ratio_with_site` | -0.0648964 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[63].mean_log10ratio_with_site` | -0.0179692 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[64].mean_log10ratio_with_site` | -0.0124925 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[65].mean_log10ratio_with_site` | -0.0406184 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[66].mean_log10ratio_with_site` | -0.0218882 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[67].mean_log10ratio_with_site` | -0.0571946 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[68].mean_log10ratio_with_site` | -0.0189414 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[69].mean_log10ratio_with_site` | -0.0224626 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[70].mean_log10ratio_with_site` | -0.0398212 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[71].mean_log10ratio_with_site` | -0.0177581 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[72].mean_log10ratio_with_site` | -0.0692704 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[73].mean_log10ratio_with_site` | -0.0239257 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[74].mean_log10ratio_with_site` | -0.012673 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[75].mean_log10ratio_with_site` | -0.0314903 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[76].mean_log10ratio_with_site` | -0.0317716 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[77].mean_log10ratio_with_site` | -0.0785852 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[78].mean_log10ratio_with_site` | -0.0216272 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[79].mean_log10ratio_with_site` | -0.00136301 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[80].mean_log10ratio_with_site` | -0.0111515 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[81].mean_log10ratio_with_site` | -0.0114117 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[82].mean_log10ratio_with_site` | -0.0217724 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[83].mean_log10ratio_with_site` | -0.00569544 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[84].mean_log10ratio_with_site` | -0.00624663 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[85].mean_log10ratio_with_site` | -0.023231 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[86].mean_log10ratio_with_site` | -0.0195527 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[87].mean_log10ratio_with_site` | -0.05405 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[88].mean_log10ratio_with_site` | -0.0128537 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[89].mean_log10ratio_with_site` | -0.014974 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[90].mean_log10ratio_with_site` | -0.0304854 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[91].mean_log10ratio_with_site` | -0.0266771 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[92].mean_log10ratio_with_site` | -0.0490714 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[93].mean_log10ratio_with_site` | -0.0205883 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[94].mean_log10ratio_with_site` | -0.0100119 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[95].mean_log10ratio_with_site` | -0.0265062 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[96].mean_log10ratio_with_site` | -0.0255194 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[97].mean_log10ratio_with_site` | -0.0550278 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[98].mean_log10ratio_with_site` | -0.0170308 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[99].mean_log10ratio_with_site` | -0.00354837 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[100].mean_log10ratio_with_site` | -0.0129455 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[101].mean_log10ratio_with_site` | -0.0171611 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[102].mean_log10ratio_with_site` | -0.0295693 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[103].mean_log10ratio_with_site` | -0.00928319 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[104].mean_log10ratio_with_site` | -0.00544113 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[105].mean_log10ratio_with_site` | -0.0216938 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[106].mean_log10ratio_with_site` | -0.0176917 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[107].mean_log10ratio_with_site` | -0.0455987 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[108].mean_log10ratio_with_site` | -0.0160077 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[109].mean_log10ratio_with_site` | -0.00172435 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[110].mean_log10ratio_with_site` | -0.014775 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[111].mean_log10ratio_with_site` | -0.0251461 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[112].mean_log10ratio_with_site` | -0.0241124 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[113].mean_log10ratio_with_site` | -0.011102 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[114].mean_log10ratio_with_site` | -0.0196966 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[115].mean_log10ratio_with_site` | -0.0208406 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[116].mean_log10ratio_with_site` | -0.032408 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[117].mean_log10ratio_with_site` | -0.0282983 | - | 24 |
| `e7_offtarget_ranking` | `positive_control_detail[118].mean_log10ratio_with_site` | -0.022419 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[0].mean_spearman_equilibrium` | -0.0656005 | 0.0431399 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[0].mean_spearman_independent` | -0.0655998 | 0.0431395 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[0].mean_spearman_difference` | -7.5280e-07 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[0].mean_kendall_between_scorings_within_construct` | 0.999996 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[0].mean_f_over_M` | 5.9200e-05 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[1].mean_spearman_equilibrium` | -0.0656012 | 0.0431405 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[1].mean_spearman_independent` | -0.0655996 | 0.0431396 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[1].mean_spearman_difference` | -1.5732e-06 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[1].mean_kendall_between_scorings_within_construct` | 0.999996 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[1].mean_f_over_M` | 0.00385797 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[2].mean_spearman_equilibrium` | -0.0656014 | 0.0431406 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[2].mean_spearman_independent` | -0.0656008 | 0.0431407 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[2].mean_spearman_difference` | -5.3993e-07 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[2].mean_kendall_between_scorings_within_construct` | 0.999993 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[2].mean_f_over_M` | 0.445944 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[3].mean_spearman_equilibrium` | -0.0656017 | 0.0431407 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[3].mean_spearman_independent` | -0.0656008 | 0.0431406 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[3].mean_spearman_difference` | -8.9008e-07 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[3].mean_kendall_between_scorings_within_construct` | 0.999995 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[3].mean_f_over_M` | 0.836401 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[4].mean_spearman_equilibrium` | -0.0656001 | 0.0431401 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[4].mean_spearman_independent` | -0.0656001 | 0.0431409 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[4].mean_spearman_difference` | 6.5270e-08 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[4].mean_kendall_between_scorings_within_construct` | 0.999997 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[4].mean_f_over_M` | 0.955494 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[5].mean_spearman_equilibrium` | -0.0656005 | 0.0431403 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[5].mean_spearman_independent` | -0.0656005 | 0.0431406 | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[5].mean_spearman_difference` | 3.0500e-08 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[5].mean_kendall_between_scorings_within_construct` | 0.999995 | - | 24 |
| `e7_offtarget_ranking` | `per_rho_within_construct[5].mean_f_over_M` | 0.990613 | - | 24 |
| `e7b_null_calibration` | `pooled_site_class.best_ddG.6mer.mean_log10ratio` | -0.00834067 | - | - |
| `e7b_null_calibration` | `pooled_site_class.best_ddG.7mer-A1.mean_log10ratio` | -0.023751 | - | - |
| `e7b_null_calibration` | `pooled_site_class.best_ddG.7mer-m8.mean_log10ratio` | -0.0179436 | - | - |
| `e7b_null_calibration` | `pooled_site_class.best_ddG.8mer.mean_log10ratio` | -0.0390677 | - | - |
| `e7b_null_calibration` | `pooled_site_class.canonical_strongest.6mer.mean_log10ratio` | -0.00705026 | - | - |
| `e7b_null_calibration` | `pooled_site_class.canonical_strongest.7mer-A1.mean_log10ratio` | -0.024079 | - | - |
| `e7b_null_calibration` | `pooled_site_class.canonical_strongest.7mer-m8.mean_log10ratio` | -0.0174648 | - | - |
| `e7b_null_calibration` | `pooled_site_class.canonical_strongest.8mer.mean_log10ratio` | -0.0377058 | - | - |
| `e7b_null_calibration` | `pooled_pair_dependence_diagnostic.mean_constructs_per_gene` | 4.29797 | - | - |
| `e4_retrieval_invariance` | `mean_rel_err_o_target_affinity_rule` | 0.235846 | - | - |
| `e4_retrieval_invariance` | `mean_rel_err_o_target_abundance_rule` | 0.480094 | - | - |
| `e4b_binned_background` | `per_setting_summary[0].mean_rel_err_o_target_over_rho` | 0.248512 | - | - |
| `e4b_binned_background` | `per_setting_summary[0].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[0].mean_frac_omitted_with_K_above_10f` | 0.314635 | - | - |
| `e4b_binned_background` | `per_setting_summary[1].mean_rel_err_o_target_over_rho` | 0.241706 | - | - |
| `e4b_binned_background` | `per_setting_summary[1].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[1].mean_frac_omitted_with_K_above_10f` | 0.313556 | - | - |
| `e4b_binned_background` | `per_setting_summary[2].mean_rel_err_o_target_over_rho` | 0.233929 | - | - |
| `e4b_binned_background` | `per_setting_summary[2].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[2].mean_frac_omitted_with_K_above_10f` | 0.311399 | - | - |
| `e4b_binned_background` | `per_setting_summary[3].mean_rel_err_o_target_over_rho` | 0.215267 | - | - |
| `e4b_binned_background` | `per_setting_summary[3].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[3].mean_frac_omitted_with_K_above_10f` | 0.309601 | - | - |
| `e4b_binned_background` | `per_setting_summary[4].mean_rel_err_o_target_over_rho` | 0.0904729 | - | - |
| `e4b_binned_background` | `per_setting_summary[4].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[4].mean_frac_omitted_with_K_above_10f` | 0.298454 | - | - |
| `e4b_binned_background` | `per_setting_summary[5].mean_rel_err_o_target_over_rho` | 0.0235372 | - | - |
| `e4b_binned_background` | `per_setting_summary[5].mean_n_bins_used` | 20 | - | - |
| `e4b_binned_background` | `per_setting_summary[5].mean_frac_omitted_with_K_above_10f` | 0.294498 | - | - |
| `e4b_binned_background` | `per_setting_summary[6].mean_rel_err_o_target_over_rho` | 0.0037578 | - | - |
| `e4b_binned_background` | `per_setting_summary[6].mean_n_bins_used` | 50 | - | - |
| `e4b_binned_background` | `per_setting_summary[6].mean_frac_omitted_with_K_above_10f` | 0.293779 | - | - |
| `e4b_binned_background` | `per_setting_summary[7].mean_rel_err_o_target_over_rho` | 8.2885e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[7].mean_n_bins_used` | 100 | - | - |
| `e4b_binned_background` | `per_setting_summary[7].mean_frac_omitted_with_K_above_10f` | 0.293779 | - | - |
| `e4b_binned_background` | `per_setting_summary[8].mean_rel_err_o_target_over_rho` | 1.8265e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[8].mean_n_bins_used` | 200 | - | - |
| `e4b_binned_background` | `per_setting_summary[8].mean_frac_omitted_with_K_above_10f` | 0.293779 | - | - |
| `e4b_binned_background` | `per_setting_summary[9].mean_rel_err_o_target_over_rho` | 1.3924e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[9].mean_n_bins_used` | 499 | - | - |
| `e4b_binned_background` | `per_setting_summary[9].mean_frac_omitted_with_K_above_10f` | 0.293779 | - | - |
| `e4b_binned_background` | `per_setting_summary[10].mean_rel_err_o_target_over_rho` | 0.121805 | - | - |
| `e4b_binned_background` | `per_setting_summary[10].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[10].mean_frac_omitted_with_K_above_10f` | 0.310791 | - | - |
| `e4b_binned_background` | `per_setting_summary[11].mean_rel_err_o_target_over_rho` | 0.115774 | - | - |
| `e4b_binned_background` | `per_setting_summary[11].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[11].mean_frac_omitted_with_K_above_10f` | 0.310052 | - | - |
| `e4b_binned_background` | `per_setting_summary[12].mean_rel_err_o_target_over_rho` | 0.106896 | - | - |
| `e4b_binned_background` | `per_setting_summary[12].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[12].mean_frac_omitted_with_K_above_10f` | 0.308574 | - | - |
| `e4b_binned_background` | `per_setting_summary[13].mean_rel_err_o_target_over_rho` | 0.0848959 | - | - |
| `e4b_binned_background` | `per_setting_summary[13].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[13].mean_frac_omitted_with_K_above_10f` | 0.306356 | - | - |
| `e4b_binned_background` | `per_setting_summary[14].mean_rel_err_o_target_over_rho` | 0.0314719 | - | - |
| `e4b_binned_background` | `per_setting_summary[14].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[14].mean_frac_omitted_with_K_above_10f` | 0.3034 | - | - |
| `e4b_binned_background` | `per_setting_summary[15].mean_rel_err_o_target_over_rho` | 0.00699075 | - | - |
| `e4b_binned_background` | `per_setting_summary[15].mean_n_bins_used` | 20 | - | - |
| `e4b_binned_background` | `per_setting_summary[15].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[16].mean_rel_err_o_target_over_rho` | 0.00130059 | - | - |
| `e4b_binned_background` | `per_setting_summary[16].mean_n_bins_used` | 50 | - | - |
| `e4b_binned_background` | `per_setting_summary[16].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[17].mean_rel_err_o_target_over_rho` | 2.7962e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[17].mean_n_bins_used` | 100 | - | - |
| `e4b_binned_background` | `per_setting_summary[17].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[18].mean_rel_err_o_target_over_rho` | 7.5126e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[18].mean_n_bins_used` | 200 | - | - |
| `e4b_binned_background` | `per_setting_summary[18].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[19].mean_rel_err_o_target_over_rho` | 2.4455e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[19].mean_n_bins_used` | 499 | - | - |
| `e4b_binned_background` | `per_setting_summary[19].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[20].mean_rel_err_o_target_over_rho` | 0.0273825 | - | - |
| `e4b_binned_background` | `per_setting_summary[20].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[20].mean_frac_omitted_with_K_above_10f` | 0.320423 | - | - |
| `e4b_binned_background` | `per_setting_summary[21].mean_rel_err_o_target_over_rho` | 0.0262711 | - | - |
| `e4b_binned_background` | `per_setting_summary[21].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[21].mean_frac_omitted_with_K_above_10f` | 0.320423 | - | - |
| `e4b_binned_background` | `per_setting_summary[22].mean_rel_err_o_target_over_rho` | 0.0241541 | - | - |
| `e4b_binned_background` | `per_setting_summary[22].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[22].mean_frac_omitted_with_K_above_10f` | 0.319249 | - | - |
| `e4b_binned_background` | `per_setting_summary[23].mean_rel_err_o_target_over_rho` | 0.0204257 | - | - |
| `e4b_binned_background` | `per_setting_summary[23].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[23].mean_frac_omitted_with_K_above_10f` | 0.318858 | - | - |
| `e4b_binned_background` | `per_setting_summary[24].mean_rel_err_o_target_over_rho` | 0.0101841 | - | - |
| `e4b_binned_background` | `per_setting_summary[24].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[24].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[25].mean_rel_err_o_target_over_rho` | 0.00266091 | - | - |
| `e4b_binned_background` | `per_setting_summary[25].mean_n_bins_used` | 20 | - | - |
| `e4b_binned_background` | `per_setting_summary[25].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[26].mean_rel_err_o_target_over_rho` | 5.0844e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[26].mean_n_bins_used` | 50 | - | - |
| `e4b_binned_background` | `per_setting_summary[26].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[27].mean_rel_err_o_target_over_rho` | 1.4123e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[27].mean_n_bins_used` | 100 | - | - |
| `e4b_binned_background` | `per_setting_summary[27].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[28].mean_rel_err_o_target_over_rho` | 4.5608e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[28].mean_n_bins_used` | 200 | - | - |
| `e4b_binned_background` | `per_setting_summary[28].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[29].mean_rel_err_o_target_over_rho` | 7.6467e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[29].mean_n_bins_used` | 498 | - | - |
| `e4b_binned_background` | `per_setting_summary[29].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[30].mean_rel_err_o_target_over_rho` | 9.2520e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[30].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[30].mean_frac_omitted_with_K_above_10f` | 0.342642 | - | - |
| `e4b_binned_background` | `per_setting_summary[31].mean_rel_err_o_target_over_rho` | 8.9991e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[31].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[31].mean_frac_omitted_with_K_above_10f` | 0.342199 | - | - |
| `e4b_binned_background` | `per_setting_summary[32].mean_rel_err_o_target_over_rho` | 8.6285e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[32].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[32].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[33].mean_rel_err_o_target_over_rho` | 7.4492e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[33].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[33].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[34].mean_rel_err_o_target_over_rho` | 4.8706e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[34].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[34].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[35].mean_rel_err_o_target_over_rho` | 2.2866e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[35].mean_n_bins_used` | 20 | - | - |
| `e4b_binned_background` | `per_setting_summary[35].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[36].mean_rel_err_o_target_over_rho` | 6.8809e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[36].mean_n_bins_used` | 50 | - | - |
| `e4b_binned_background` | `per_setting_summary[36].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[37].mean_rel_err_o_target_over_rho` | 1.9282e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[37].mean_n_bins_used` | 100 | - | - |
| `e4b_binned_background` | `per_setting_summary[37].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[38].mean_rel_err_o_target_over_rho` | 7.0614e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[38].mean_n_bins_used` | 200 | - | - |
| `e4b_binned_background` | `per_setting_summary[38].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[39].mean_rel_err_o_target_over_rho` | 1.6540e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[39].mean_n_bins_used` | 499 | - | - |
| `e4b_binned_background` | `per_setting_summary[39].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[40].mean_rel_err_o_target_over_rho` | 5.2454e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[40].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[40].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[41].mean_rel_err_o_target_over_rho` | 1.7392e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[41].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[41].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[42].mean_rel_err_o_target_over_rho` | 6.1316e-07 | - | - |
| `e4b_binned_background` | `per_setting_summary[42].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[42].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[43].mean_rel_err_o_target_over_rho` | 3.5330e-07 | - | - |
| `e4b_binned_background` | `per_setting_summary[43].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[43].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[44].mean_rel_err_o_target_over_rho` | 1.0455e-07 | - | - |
| `e4b_binned_background` | `per_setting_summary[44].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[44].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[45].mean_rel_err_o_target_over_rho` | 3.0971e-08 | - | - |
| `e4b_binned_background` | `per_setting_summary[45].mean_n_bins_used` | 20 | - | - |
| `e4b_binned_background` | `per_setting_summary[45].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[46].mean_rel_err_o_target_over_rho` | 9.7586e-09 | - | - |
| `e4b_binned_background` | `per_setting_summary[46].mean_n_bins_used` | 50 | - | - |
| `e4b_binned_background` | `per_setting_summary[46].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[47].mean_rel_err_o_target_over_rho` | 5.9438e-09 | - | - |
| `e4b_binned_background` | `per_setting_summary[47].mean_n_bins_used` | 100 | - | - |
| `e4b_binned_background` | `per_setting_summary[47].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[48].mean_rel_err_o_target_over_rho` | 4.5262e-09 | - | - |
| `e4b_binned_background` | `per_setting_summary[48].mean_n_bins_used` | 200 | - | - |
| `e4b_binned_background` | `per_setting_summary[48].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[49].mean_rel_err_o_target_over_rho` | 9.4976e-17 | - | - |
| `e4b_binned_background` | `per_setting_summary[49].mean_n_bins_used` | 451 | - | - |
| `e4b_binned_background` | `per_setting_summary[49].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[50].mean_rel_err_o_target_over_rho` | 0.248512 | - | - |
| `e4b_binned_background` | `per_setting_summary[50].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[50].mean_frac_omitted_with_K_above_10f` | 0.314635 | - | - |
| `e4b_binned_background` | `per_setting_summary[51].mean_rel_err_o_target_over_rho` | 0.247582 | - | - |
| `e4b_binned_background` | `per_setting_summary[51].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[51].mean_frac_omitted_with_K_above_10f` | 0.313916 | - | - |
| `e4b_binned_background` | `per_setting_summary[52].mean_rel_err_o_target_over_rho` | 0.236675 | - | - |
| `e4b_binned_background` | `per_setting_summary[52].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[52].mean_frac_omitted_with_K_above_10f` | 0.312478 | - | - |
| `e4b_binned_background` | `per_setting_summary[53].mean_rel_err_o_target_over_rho` | 0.109056 | - | - |
| `e4b_binned_background` | `per_setting_summary[53].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[53].mean_frac_omitted_with_K_above_10f` | 0.300611 | - | - |
| `e4b_binned_background` | `per_setting_summary[54].mean_rel_err_o_target_over_rho` | 0.0755329 | - | - |
| `e4b_binned_background` | `per_setting_summary[54].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[54].mean_frac_omitted_with_K_above_10f` | 0.297375 | - | - |
| `e4b_binned_background` | `per_setting_summary[55].mean_rel_err_o_target_over_rho` | 0.0244759 | - | - |
| `e4b_binned_background` | `per_setting_summary[55].mean_n_bins_used` | 19 | - | - |
| `e4b_binned_background` | `per_setting_summary[55].mean_frac_omitted_with_K_above_10f` | 0.294498 | - | - |
| `e4b_binned_background` | `per_setting_summary[56].mean_rel_err_o_target_over_rho` | 0.00398777 | - | - |
| `e4b_binned_background` | `per_setting_summary[56].mean_n_bins_used` | 36 | - | - |
| `e4b_binned_background` | `per_setting_summary[56].mean_frac_omitted_with_K_above_10f` | 0.293779 | - | - |
| `e4b_binned_background` | `per_setting_summary[57].mean_rel_err_o_target_over_rho` | 6.2429e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[57].mean_n_bins_used` | 66 | - | - |
| `e4b_binned_background` | `per_setting_summary[57].mean_frac_omitted_with_K_above_10f` | 0.293779 | - | - |
| `e4b_binned_background` | `per_setting_summary[58].mean_rel_err_o_target_over_rho` | 1.3640e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[58].mean_n_bins_used` | 117 | - | - |
| `e4b_binned_background` | `per_setting_summary[58].mean_frac_omitted_with_K_above_10f` | 0.293779 | - | - |
| `e4b_binned_background` | `per_setting_summary[59].mean_rel_err_o_target_over_rho` | 3.6929e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[59].mean_n_bins_used` | 245 | - | - |
| `e4b_binned_background` | `per_setting_summary[59].mean_frac_omitted_with_K_above_10f` | 0.293779 | - | - |
| `e4b_binned_background` | `per_setting_summary[60].mean_rel_err_o_target_over_rho` | 0.121805 | - | - |
| `e4b_binned_background` | `per_setting_summary[60].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[60].mean_frac_omitted_with_K_above_10f` | 0.310791 | - | - |
| `e4b_binned_background` | `per_setting_summary[61].mean_rel_err_o_target_over_rho` | 0.121499 | - | - |
| `e4b_binned_background` | `per_setting_summary[61].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[61].mean_frac_omitted_with_K_above_10f` | 0.310421 | - | - |
| `e4b_binned_background` | `per_setting_summary[62].mean_rel_err_o_target_over_rho` | 0.117834 | - | - |
| `e4b_binned_background` | `per_setting_summary[62].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[62].mean_frac_omitted_with_K_above_10f` | 0.310052 | - | - |
| `e4b_binned_background` | `per_setting_summary[63].mean_rel_err_o_target_over_rho` | 0.0879337 | - | - |
| `e4b_binned_background` | `per_setting_summary[63].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[63].mean_frac_omitted_with_K_above_10f` | 0.306356 | - | - |
| `e4b_binned_background` | `per_setting_summary[64].mean_rel_err_o_target_over_rho` | 0.0260926 | - | - |
| `e4b_binned_background` | `per_setting_summary[64].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[64].mean_frac_omitted_with_K_above_10f` | 0.30303 | - | - |
| `e4b_binned_background` | `per_setting_summary[65].mean_rel_err_o_target_over_rho` | 0.0085821 | - | - |
| `e4b_binned_background` | `per_setting_summary[65].mean_n_bins_used` | 18 | - | - |
| `e4b_binned_background` | `per_setting_summary[65].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[66].mean_rel_err_o_target_over_rho` | 0.00123721 | - | - |
| `e4b_binned_background` | `per_setting_summary[66].mean_n_bins_used` | 38 | - | - |
| `e4b_binned_background` | `per_setting_summary[66].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[67].mean_rel_err_o_target_over_rho` | 3.0097e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[67].mean_n_bins_used` | 67 | - | - |
| `e4b_binned_background` | `per_setting_summary[67].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[68].mean_rel_err_o_target_over_rho` | 9.0561e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[68].mean_n_bins_used` | 123 | - | - |
| `e4b_binned_background` | `per_setting_summary[68].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[69].mean_rel_err_o_target_over_rho` | 5.4034e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[69].mean_n_bins_used` | 262 | - | - |
| `e4b_binned_background` | `per_setting_summary[69].mean_frac_omitted_with_K_above_10f` | 0.301922 | - | - |
| `e4b_binned_background` | `per_setting_summary[70].mean_rel_err_o_target_over_rho` | 0.0273825 | - | - |
| `e4b_binned_background` | `per_setting_summary[70].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[70].mean_frac_omitted_with_K_above_10f` | 0.320423 | - | - |
| `e4b_binned_background` | `per_setting_summary[71].mean_rel_err_o_target_over_rho` | 0.0273423 | - | - |
| `e4b_binned_background` | `per_setting_summary[71].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[71].mean_frac_omitted_with_K_above_10f` | 0.320031 | - | - |
| `e4b_binned_background` | `per_setting_summary[72].mean_rel_err_o_target_over_rho` | 0.0266963 | - | - |
| `e4b_binned_background` | `per_setting_summary[72].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[72].mean_frac_omitted_with_K_above_10f` | 0.31964 | - | - |
| `e4b_binned_background` | `per_setting_summary[73].mean_rel_err_o_target_over_rho` | 0.0204754 | - | - |
| `e4b_binned_background` | `per_setting_summary[73].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[73].mean_frac_omitted_with_K_above_10f` | 0.318858 | - | - |
| `e4b_binned_background` | `per_setting_summary[74].mean_rel_err_o_target_over_rho` | 0.00480353 | - | - |
| `e4b_binned_background` | `per_setting_summary[74].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[74].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[75].mean_rel_err_o_target_over_rho` | 0.0016441 | - | - |
| `e4b_binned_background` | `per_setting_summary[75].mean_n_bins_used` | 18 | - | - |
| `e4b_binned_background` | `per_setting_summary[75].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[76].mean_rel_err_o_target_over_rho` | 2.7159e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[76].mean_n_bins_used` | 36 | - | - |
| `e4b_binned_background` | `per_setting_summary[76].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[77].mean_rel_err_o_target_over_rho` | 5.0697e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[77].mean_n_bins_used` | 67 | - | - |
| `e4b_binned_background` | `per_setting_summary[77].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[78].mean_rel_err_o_target_over_rho` | 9.1445e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[78].mean_n_bins_used` | 120 | - | - |
| `e4b_binned_background` | `per_setting_summary[78].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[79].mean_rel_err_o_target_over_rho` | 9.9607e-07 | - | - |
| `e4b_binned_background` | `per_setting_summary[79].mean_n_bins_used` | 248 | - | - |
| `e4b_binned_background` | `per_setting_summary[79].mean_frac_omitted_with_K_above_10f` | 0.318466 | - | - |
| `e4b_binned_background` | `per_setting_summary[80].mean_rel_err_o_target_over_rho` | 9.2520e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[80].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[80].mean_frac_omitted_with_K_above_10f` | 0.342642 | - | - |
| `e4b_binned_background` | `per_setting_summary[81].mean_rel_err_o_target_over_rho` | 9.2345e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[81].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[81].mean_frac_omitted_with_K_above_10f` | 0.342642 | - | - |
| `e4b_binned_background` | `per_setting_summary[82].mean_rel_err_o_target_over_rho` | 9.0719e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[82].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[82].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[83].mean_rel_err_o_target_over_rho` | 8.3551e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[83].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[83].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[84].mean_rel_err_o_target_over_rho` | 3.1971e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[84].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[84].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[85].mean_rel_err_o_target_over_rho` | 1.0058e-04 | - | - |
| `e4b_binned_background` | `per_setting_summary[85].mean_n_bins_used` | 17 | - | - |
| `e4b_binned_background` | `per_setting_summary[85].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[86].mean_rel_err_o_target_over_rho` | 1.1151e-05 | - | - |
| `e4b_binned_background` | `per_setting_summary[86].mean_n_bins_used` | 36 | - | - |
| `e4b_binned_background` | `per_setting_summary[86].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[87].mean_rel_err_o_target_over_rho` | 3.3901e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[87].mean_n_bins_used` | 64 | - | - |
| `e4b_binned_background` | `per_setting_summary[87].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[88].mean_rel_err_o_target_over_rho` | 7.5619e-07 | - | - |
| `e4b_binned_background` | `per_setting_summary[88].mean_n_bins_used` | 117 | - | - |
| `e4b_binned_background` | `per_setting_summary[88].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[89].mean_rel_err_o_target_over_rho` | 3.1833e-08 | - | - |
| `e4b_binned_background` | `per_setting_summary[89].mean_n_bins_used` | 241 | - | - |
| `e4b_binned_background` | `per_setting_summary[89].mean_frac_omitted_with_K_above_10f` | 0.341755 | - | - |
| `e4b_binned_background` | `per_setting_summary[90].mean_rel_err_o_target_over_rho` | 5.2454e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[90].mean_n_bins_used` | 1 | - | - |
| `e4b_binned_background` | `per_setting_summary[90].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[91].mean_rel_err_o_target_over_rho` | 4.9318e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[91].mean_n_bins_used` | 2 | - | - |
| `e4b_binned_background` | `per_setting_summary[91].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[92].mean_rel_err_o_target_over_rho` | 2.4716e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[92].mean_n_bins_used` | 3 | - | - |
| `e4b_binned_background` | `per_setting_summary[92].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[93].mean_rel_err_o_target_over_rho` | 2.1396e-06 | - | - |
| `e4b_binned_background` | `per_setting_summary[93].mean_n_bins_used` | 5 | - | - |
| `e4b_binned_background` | `per_setting_summary[93].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[94].mean_rel_err_o_target_over_rho` | 5.0391e-07 | - | - |
| `e4b_binned_background` | `per_setting_summary[94].mean_n_bins_used` | 10 | - | - |
| `e4b_binned_background` | `per_setting_summary[94].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[95].mean_rel_err_o_target_over_rho` | 1.5749e-07 | - | - |
| `e4b_binned_background` | `per_setting_summary[95].mean_n_bins_used` | 16 | - | - |
| `e4b_binned_background` | `per_setting_summary[95].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[96].mean_rel_err_o_target_over_rho` | 1.8183e-08 | - | - |
| `e4b_binned_background` | `per_setting_summary[96].mean_n_bins_used` | 32 | - | - |
| `e4b_binned_background` | `per_setting_summary[96].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[97].mean_rel_err_o_target_over_rho` | 2.3635e-09 | - | - |
| `e4b_binned_background` | `per_setting_summary[97].mean_n_bins_used` | 56 | - | - |
| `e4b_binned_background` | `per_setting_summary[97].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[98].mean_rel_err_o_target_over_rho` | 7.4233e-10 | - | - |
| `e4b_binned_background` | `per_setting_summary[98].mean_n_bins_used` | 93 | - | - |
| `e4b_binned_background` | `per_setting_summary[98].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e4b_binned_background` | `per_setting_summary[99].mean_rel_err_o_target_over_rho` | 9.9456e-11 | - | - |
| `e4b_binned_background` | `per_setting_summary[99].mean_n_bins_used` | 187 | - | - |
| `e4b_binned_background` | `per_setting_summary[99].mean_frac_omitted_with_K_above_10f` | 0.373156 | - | - |
| `e9_dose_response` | `per_construct[0].free_fit.mean_bound_fraction_per_dose[0]` | 0.988172 | - | - |
| `e9_dose_response` | `per_construct[0].free_fit.mean_bound_fraction_per_dose[1]` | 0.897907 | - | - |
| `e9_dose_response` | `per_construct[0].free_fit.mean_bound_fraction_per_dose[2]` | 0.771778 | - | - |
| `e9_dose_response` | `per_construct[0].class_fit.mean_bound_fraction_per_dose[0]` | 0.104855 | - | - |
| `e9_dose_response` | `per_construct[0].class_fit.mean_bound_fraction_per_dose[1]` | 0.120755 | - | - |
| `e9_dose_response` | `per_construct[0].class_fit.mean_bound_fraction_per_dose[2]` | 0.148576 | - | - |
| `e9_dose_response` | `per_construct[0].predictor_diagnostics_per_dose[0].mean_log2fc` | -0.06613 | - | - |
| `e9_dose_response` | `per_construct[0].predictor_diagnostics_per_dose[1].mean_log2fc` | -0.0791604 | - | - |
| `e9_dose_response` | `per_construct[0].predictor_diagnostics_per_dose[2].mean_log2fc` | -0.131823 | - | - |
| `e9_dose_response` | `per_construct[1].free_fit.mean_bound_fraction_per_dose[0]` | 1.1784e-04 | - | - |
| `e9_dose_response` | `per_construct[1].free_fit.mean_bound_fraction_per_dose[1]` | 0.00278331 | - | - |
| `e9_dose_response` | `per_construct[1].free_fit.mean_bound_fraction_per_dose[2]` | 0.874679 | - | - |
| `e9_dose_response` | `per_construct[1].class_fit.mean_bound_fraction_per_dose[0]` | 0.00821154 | - | - |
| `e9_dose_response` | `per_construct[1].class_fit.mean_bound_fraction_per_dose[1]` | 0.0198483 | - | - |
| `e9_dose_response` | `per_construct[1].class_fit.mean_bound_fraction_per_dose[2]` | 0.138644 | - | - |
| `e9_dose_response` | `per_construct[1].predictor_diagnostics_per_dose[0].mean_log2fc` | -0.0031371 | - | - |
| `e9_dose_response` | `per_construct[1].predictor_diagnostics_per_dose[1].mean_log2fc` | -0.00570686 | - | - |
| `e9_dose_response` | `per_construct[1].predictor_diagnostics_per_dose[2].mean_log2fc` | -0.0494235 | - | - |
| `e9_dose_response` | `per_construct[2].free_fit.mean_bound_fraction_per_dose[0]` | 0.0621939 | - | - |
| `e9_dose_response` | `per_construct[2].free_fit.mean_bound_fraction_per_dose[1]` | 0.59986 | - | - |
| `e9_dose_response` | `per_construct[2].class_fit.mean_bound_fraction_per_dose[0]` | 2.5310e-06 | - | - |
| `e9_dose_response` | `per_construct[2].class_fit.mean_bound_fraction_per_dose[1]` | 0.176044 | - | - |
| `e9_dose_response` | `per_construct[2].predictor_diagnostics_per_dose[0].mean_log2fc` | 0.00491461 | - | - |
| `e9_dose_response` | `per_construct[2].predictor_diagnostics_per_dose[1].mean_log2fc` | 0.00229658 | - | - |
| `e9_dose_response` | `per_construct[3].free_fit.mean_bound_fraction_per_dose[0]` | 0.838546 | - | - |
| `e9_dose_response` | `per_construct[3].free_fit.mean_bound_fraction_per_dose[1]` | 0.569527 | - | - |
| `e9_dose_response` | `per_construct[3].free_fit.mean_bound_fraction_per_dose[2]` | 0.804105 | - | - |
| `e9_dose_response` | `per_construct[3].class_fit.mean_bound_fraction_per_dose[0]` | 0.0498916 | - | - |
| `e9_dose_response` | `per_construct[3].class_fit.mean_bound_fraction_per_dose[1]` | 0.164164 | - | - |
| `e9_dose_response` | `per_construct[3].class_fit.mean_bound_fraction_per_dose[2]` | 0.143357 | - | - |
| `e9_dose_response` | `per_construct[3].predictor_diagnostics_per_dose[0].mean_log2fc` | -0.00987209 | - | - |
| `e9_dose_response` | `per_construct[3].predictor_diagnostics_per_dose[1].mean_log2fc` | -0.0442646 | - | - |
| `e9_dose_response` | `per_construct[3].predictor_diagnostics_per_dose[2].mean_log2fc` | 0.0630598 | - | - |
| `e9_dose_response` | `per_construct[4].free_fit.mean_bound_fraction_per_dose[0]` | 0.956295 | - | - |
| `e9_dose_response` | `per_construct[4].free_fit.mean_bound_fraction_per_dose[1]` | 0.496453 | - | - |
| `e9_dose_response` | `per_construct[4].free_fit.mean_bound_fraction_per_dose[2]` | 0.607152 | - | - |
| `e9_dose_response` | `per_construct[4].class_fit.mean_bound_fraction_per_dose[0]` | 0.0462779 | - | - |
| `e9_dose_response` | `per_construct[4].class_fit.mean_bound_fraction_per_dose[1]` | 0.0860187 | - | - |
| `e9_dose_response` | `per_construct[4].class_fit.mean_bound_fraction_per_dose[2]` | 0.130771 | - | - |
| `e9_dose_response` | `per_construct[4].predictor_diagnostics_per_dose[0].mean_log2fc` | -0.0197332 | - | - |
| `e9_dose_response` | `per_construct[4].predictor_diagnostics_per_dose[1].mean_log2fc` | -0.0356272 | - | - |
| `e9_dose_response` | `per_construct[4].predictor_diagnostics_per_dose[2].mean_log2fc` | -0.0497743 | - | - |
| `e10_cross_context` | `per_construct[0].mean_log2fc_HUH7` | -0.00400581 | - | - |
| `e10_cross_context` | `per_construct[0].mean_log2fc_PLC` | 0.0046181 | - | - |
| `e10_cross_context` | `per_construct[0].fit.mean_bound_fraction_per_dose[0]` | 0.241718 | - | - |
| `e10_cross_context` | `per_construct[0].fit.mean_bound_fraction_per_dose[1]` | 0.245874 | - | - |
| `e10_cross_context` | `per_construct[1].mean_log2fc_HUH7` | -0.0094323 | - | - |
| `e10_cross_context` | `per_construct[1].mean_log2fc_PLC` | -0.0180739 | - | - |
| `e10_cross_context` | `per_construct[1].fit.mean_bound_fraction_per_dose[0]` | 0.17357 | - | - |
| `e10_cross_context` | `per_construct[1].fit.mean_bound_fraction_per_dose[1]` | 0.315268 | - | - |
| `e10_cross_context` | `per_construct[2].mean_log2fc_HUH7` | -0.00399362 | - | - |
| `e10_cross_context` | `per_construct[2].mean_log2fc_PLC` | -0.0109345 | - | - |
| `e10_cross_context` | `per_construct[2].fit.mean_bound_fraction_per_dose[0]` | 0.0897788 | - | - |
| `e10_cross_context` | `per_construct[2].fit.mean_bound_fraction_per_dose[1]` | 0.186833 | - | - |
| `e2_redistribution` | `mean_margin_1_minus_u_over_D` | 0.993085 | - | - |
| `e8_huesken_efficacy` | `mean_spearman_heldout_genes` | 0.479484 | 0.0440352 | 5 |
| `e8_huesken_efficacy` | `mean_pearson_heldout_genes` | 0.46206 | 0.0365113 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[0].sim_mean_spearman_equilibrium_trained` | 0.911152 | 0.0470805 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[0].sim_mean_spearman_pairwise_trained` | 0.468442 | 0.147962 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[0].sim_mean_gap` | 0.44271 | 0.17297 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[1].sim_mean_spearman_equilibrium_trained` | 0.994283 | 0.00103298 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[1].sim_mean_spearman_pairwise_trained` | 0.906625 | 0.0244871 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[1].sim_mean_gap` | 0.0876582 | 0.024405 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[2].sim_mean_spearman_equilibrium_trained` | 0.998862 | 1.4531e-04 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[2].sim_mean_spearman_pairwise_trained` | 0.996225 | 4.3125e-04 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[2].sim_mean_gap` | 0.00263714 | 4.3968e-04 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[3].sim_mean_spearman_equilibrium_trained` | 0.962119 | 0.0209693 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[3].sim_mean_spearman_pairwise_trained` | 0.957261 | 0.0211453 | 5 |
| `e6_sim_interaction_recovery` | `sim_summary_by_rho[3].sim_mean_gap` | 0.00485778 | 0.0101849 | 5 |

## 4. Data provenance

157 records: 143 OK, 14 FAILED.

| dataset | status | path | bytes | sha256 (first 16) | url |
|---|---|---|---|---|---|
| D1_GSE5814 | OK | `data/raw/GSE5814_family.soft.gz` | 29878019 | `d58c3957b9f6d2b3` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/soft/GSE5814_family.soft.gz |
| D1_GSE5814 | OK | `data/raw/GSE5814-GPL2029_series_matrix.txt.gz` | 1137612 | `cb4afbc53c9b6461` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/matrix/GSE5814-GPL2029_series_matrix.txt.gz |
| D1_GSE5814 | OK | `data/raw/GSE5814-GPL3991_series_matrix.txt.gz` | 112215 | `8cc55d6f0412396e` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/matrix/GSE5814-GPL3991_series_matrix.txt.gz |
| D1_GSE5814 | OK | `data/raw/GSE5814-GPL3992_series_matrix.txt.gz` | 2548184 | `906c8a3d374700a2` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/matrix/GSE5814-GPL3992_series_matrix.txt.gz |
| D1_GSE5814 | OK | `data/raw/GSE5814_filelist.txt` | 162 | `ef129cdc919c02b6` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/suppl/filelist.txt |
| D3_GENCODE | OK | `data/raw/gencode_README.TXT` | 69086 | `ea687e13394011df` | https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/_README.TXT |
| D3_GENCODE | OK | `data/raw/gencode_MD5SUMS.txt` | 3074 | `b681a9bbebc0a6ea` | https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/MD5SUMS |
| D3_GENCODE | OK | `data/raw/gencode.v50.pc_transcripts.fa.gz` | 129953566 | `ed3bcd295a39e97f` | https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.pc_transcripts.fa.gz |
| D3_GENCODE | OK | `data/raw/gencode.v50.annotation.gtf.gz` | 124527720 | `83fba3e9b03f0b8c` | https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.annotation.gtf.gz |
| D1_refseq_targets | OK | `data/raw/refseq_NM_001315.fasta` | 4383 | `f2b5b2a3ebceec44` | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_001315&rettype=fasta&retmode=text |
| D1_refseq_targets | OK | `data/raw/refseq_NM_005030.fasta` | 2250 | `f3a54e22a2e5a427` | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_005030&rettype=fasta&retmode=text |
| D1_refseq_targets | OK | `data/raw/refseq_NM_006219.fasta` | 6483 | `35e3c642f9aaf096` | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_006219&rettype=fasta&retmode=text |
| D1_refseq_targets | OK | `data/raw/refseq_NM_139013.fasta` | 1425 | `3930043f0d0451af` | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_139013&rettype=fasta&retmode=text |
| D3_GENCODE | OK | `data/gencode_transcripts.parquet` | 65580785 | `14936fdb53234245` |  |
| D3_GENCODE | OK | `data/gencode_tx_tags.parquet` | 4545169 | `4c710a7e96e5efaa` |  |
| D3_GENCODE | OK | `data/gencode_canonical_by_symbol.parquet` | 22697572 | `0533fa38822ff489` |  |
| D1_GSE5814 | OK | `data/gse5814_expression.parquet` | 29299637 | `a193a688eeba3c9a` |  |
| D1_GSE5814 | OK | `data/gse5814_probe_annotation.parquet` | 1024903 | `1f7db8d32690eac8` |  |
| D4_abundance | OK | `data/hela_abundance.parquet` | 440907 | `bb521d56c8fed9e1` |  |
| D1_sirna_sequences | OK | `data/lit/garcia2011/nsmb2115_MOESM7.xlsx` | 24875 | `a992674b166859fa` | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnsmb.2115/MediaObjects/41594_... |
| D1_sirna_sequences | OK | `data/lit/jackson2003/nbt831_MOESM2.pdf` | 18392 | `4719ea78bcb94ce5` | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnbt831/MediaObjects/41587_200... |
| D1_sirna_sequences | OK | `data/lit/sigoillot/srep00428-s1.xls` | 3557376 | `c27e044a396fab54` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3361704/supplementaryFiles |
| D1_sirna_sequences | OK | `data/lit/GSE5814_RAW.tar` | 184320 | `8029ee642c9c596f` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/suppl/GSE5814_RAW.tar |
| D1_sirna_sequences | FAILED | `None` | null | `` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/fullTextXML |
| D1_sirna_sequences | FAILED | `None` | null | `` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/supplementaryFiles |
| D1_sirna_sequences | FAILED | `None` | null | `` | https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC1484447 |
| D1_sirna_sequences | FAILED | `None` | null | `` | https://rnajournal.cshlp.org/content/12/7/1179/suppl/DC1 |
| D1_sirna_sequences | FAILED | `None` | null | `` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5814/matrix/GSE5814_series_matrix.txt.gz |
| D1_seed_recovery | OK | `data/recovered_seeds.parquet` | 20605 | `c982d92c568a46be` |  |
| D1_sirna_sequences | OK | `data/sirna_sequences.parquet` | 17166 | `452fe09ca9c21fb5` |  |
| features_accessibility | OK | `data/accessibility_u8_u15.npz` | 159487417 | `a5ed9111584d7220` |  |
| D5_huesken | OK | `data/raw/huesken_Hu.csv` | 93094 | `9b9f152c58e8106f` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/Monopoli-RF/datasets/Hu.csv |
| D5_huesken | OK | `data/raw/huesken_Hu_unnorm.csv` | 75773 | `2297c6a32a55786b` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/Monopoli-RF/datasets/Hu_unnor... |
| D5_huesken | OK | `data/raw/huesken_HuTD.csv` | 658006 | `798a641e9ec27a4a` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/dataset/HuTD.csv |
| D5_huesken | FAILED | `data/raw/huesken_main.csv` | null | `` | https://raw.githubusercontent.com/lulab/OligoFormer/main/data/Huesken.csv |
| D5_huesken | FAILED | `data/raw/huesken_main.txt` | null | `` | https://raw.githubusercontent.com/lulab/OligoFormer/main/data/huesken.txt |
| D5_huesken | OK | `data/raw/oligoformer_tree.json` | 282070 | `4d5fab08a511e927` | https://api.github.com/repos/lulab/OligoFormer/git/trees/main?recursive=1 |
| D5_huesken | OK | `data/raw/huesken_genes/C6orf110.csv` | 220764 | `0815a25e76113237` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/C6orf1... |
| D5_huesken | OK | `data/raw/huesken_genes/CD81P3.csv` | 84751 | `d594ee8701fd9e0e` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/CD81P3... |
| D5_huesken | OK | `data/raw/huesken_genes/CDC34.csv` | 58307 | `f2767556737db5be` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/CDC34.csv |
| D5_huesken | OK | `data/raw/huesken_genes/FLJ11011.csv` | 36699 | `5cc9ab8372da64be` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/FLJ110... |
| D5_huesken | OK | `data/raw/huesken_genes/HIP2.csv` | 36510 | `13d1cd9e88953428` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/HIP2.csv |
| D5_huesken | OK | `data/raw/huesken_genes/HSPC150.csv` | 50479 | `e303f4c106000de6` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/HSPC15... |
| D5_huesken | OK | `data/raw/huesken_genes/NOG.csv` | 55484 | `4e9e8c47ebcbd9f4` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/NOG.csv |
| D5_huesken | OK | `data/raw/huesken_genes/P2RX3.csv` | 111238 | `effc369f1d6e0962` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/P2RX3.csv |
| D5_huesken | OK | `data/raw/huesken_genes/RAB6IP1.csv` | 386761 | `427af914b9aa029d` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/RAB6IP... |
| D5_huesken | OK | `data/raw/huesken_genes/Rn_Cacng4.csv` | 85964 | `c35753daccca6933` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Rn_Cac... |
| D5_huesken | OK | `data/raw/huesken_genes/Rn_Dcbld2.csv` | 153196 | `2880dbb5fe4db4c5` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Rn_Dcb... |
| D5_huesken | OK | `data/raw/huesken_genes/Rn_Fxyd6.csv` | 82980 | `746ef368baa0de45` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Rn_Fxy... |
| D5_huesken | OK | `data/raw/huesken_genes/Rn_Mmp7_1.csv` | 32717 | `1a4f9e20836609de` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Rn_Mmp... |
| D5_huesken | OK | `data/raw/huesken_genes/Rn_Mmp7_2.csv` | 26228 | `8d4dd199a3cd5ab3` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Rn_Mmp... |
| D5_huesken | OK | `data/raw/huesken_genes/Rn_P2rx2.csv` | 130642 | `8ae958d900220858` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Rn_P2r... |
| D5_huesken | OK | `data/raw/huesken_genes/Rn_TCAP.csv` | 147898 | `0d3bba9ce92025e8` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Rn_TCA... |
| D5_huesken | OK | `data/raw/huesken_genes/Rn_cacnb1.csv` | 185186 | `f6305cd8253ceae5` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Rn_cac... |
| D5_huesken | OK | `data/raw/huesken_genes/SOST.csv` | 51800 | `caa96a87d2d39962` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/SOST.csv |
| D5_huesken | OK | `data/raw/huesken_genes/TC10.csv` | 59891 | `6a9fe331fc22953a` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/TC10.csv |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2B.csv` | 39606 | `51f2177dc30bd23e` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2B.csv |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2C.csv` | 27629 | `814fae5904be5b04` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2C.csv |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2D3.csv` | 32672 | `6b744da6cba32b03` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2D3... |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2E3.csv` | 53999 | `c7500ed336ed188d` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2E3... |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2G1.csv` | 43008 | `24d7d67b42ad70fb` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2G1... |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2H.csv` | 42503 | `67dd8c8d36a329bc` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2H.csv |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2I.csv` | 35005 | `844f0d7536c44b13` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2I.csv |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2J1.csv` | 86751 | `c9e3656187324069` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2J1... |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2L3.csv` | 33816 | `263b756c26ef7244` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2L3... |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2L6.csv` | 37319 | `a944e4d94ecfbdbf` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2L6... |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2M.csv` | 48702 | `05005d491a4abdce` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2M.csv |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2N.csv` | 37623 | `b6301e99ced69deb` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2N.csv |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2S.csv` | 55097 | `9e06e91c4a469d42` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2S.csv |
| D5_huesken | OK | `data/raw/huesken_genes/UBE2V1.csv` | 43006 | `5677ad5f44dcc6a1` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/UBE2V1... |
| D5_huesken | OK | `data/raw/huesken_genes/Ufc1.csv` | 42603 | `52ad723ebf757bfd` | https://raw.githubusercontent.com/lulab/OligoFormer/main/Comparison%20methods/siRNAPred/siRNAPred/Hu/Ufc1.csv |
| D6_constants | OK | `data/constants.json` | 6638 | `1e0036b7a3c27840` |  |
| D6_constants | OK | `data/lit/constants/CONSTANTS_SOURCES.md` | 30774 | `5f96fc5aa9aef0ec` |  |
| D6_constants | OK | `data/lit/constants/wang2012_genesdev_PMC3323880.pdf` | 1945281 | `711f64c83ab15c4e` |  |
| D6_constants | OK | `data/lit/constants/janas2012_PMC3479394.pdf` | 1908956 | `d4d5f48656144787` |  |
| D6_constants | OK | `data/lit/constants/rna_errata_PMC3504684.pdf` | 428564 | `a55e3207f1a33087` |  |
| D6_constants | OK | `data/lit/constants/marinov2014_PMC3941114.xml` | 146727 | `ff963b4dcfc48ca8` |  |
| D6_constants | OK | `data/lit/constants/wee2012_PMC3595543.html` | 258035 | `d36dccc06afc840a` |  |
| D6_constants | OK | `data/lit/constants/qiagen_faq_rna_per_cell.html` | 577395 | `fc888645d38c5bac` |  |
| D5_huesken | OK | `data/huesken.parquet` | 80118 | `0d11dfb0ed8e5fe6` |  |
| D2_birmingham | OK | `data/raw/d2_vandongen_PMC2635553_suppl.zip` | 8510500 | `37ee9da40c7b71ab` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2635553/supplementaryFiles |
| D2_birmingham | FAILED | `data/raw/d2_pmc1804340_suppl.zip` | null | `` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1804340/supplementaryFiles |
| D2_birmingham | OK | `data/raw/d2_GSE5291_family.soft.gz` | 8678339 | `6fa2dead95c452d3` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5291/soft/GSE5291_family.soft.gz |
| D2_birmingham | OK | `data/raw/d2_GSE5769_family.soft.gz` | 30439673 | `c48fe62a6ec2760d` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5769/soft/GSE5769_family.soft.gz |
| D7_caffrey2011 | OK | `data/lit/caffrey2011/PMC3130022_fulltext.xml` | 129587 | `45b6563d1bff5ca3` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3130022/fullTextXML |
| D7_GSE28786 | OK | `data/raw/GSE28786_series_matrix.txt.gz` | 5353043 | `dd5d4a4f711f9a55` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE28nnn/GSE28786/matrix/GSE28786_series_matrix.txt.gz |
| D7_GSE28786 | OK | `data/raw/GSE28786_filelist.txt` | 3092 | `f234d7cc44829d1f` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE28nnn/GSE28786/suppl/filelist.txt |
| D7_GSE28786 | OK | `data/raw/GSE28786_family.soft.gz` | 8386629 | `041bde5f47d82d79` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE28nnn/GSE28786/soft/GSE28786_family.soft.gz |
| D7_entrez_gene_info | OK | `data/raw/Homo_sapiens.gene_info.gz` | 5180368 | `d8b12066b4c2280e` | https://ftp.ncbi.nlm.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz |
| D7_caffrey2011_suppl | OK | `data/lit/caffrey2011/pone.0021503.s014.doc` | 48128 | `e54378762c15f106` | https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0021503.s014&type=supplementary |
| D7_caffrey2011_suppl | OK | `data/lit/caffrey2011/pone.0021503.s016.doc` | 67584 | `a8e0800d703d05a7` | https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0021503.s016&type=supplementary |
| D7_caffrey2011_suppl | OK | `data/lit/caffrey2011/pone.0021503.s018.doc` | 100352 | `71a2ce74afc9fe52` | https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0021503.s018&type=supplementary |
| D7_caffrey2011_suppl | OK | `data/lit/caffrey2011/pone.0021503.s020.doc` | 41984 | `8244f73fea807347` | https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0021503.s020&type=supplementary |
| D7_caffrey2011 | FAILED | `data/lit/caffrey2011/oa_fcgi_PMC3130022.xml` | null | `` | https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC3130022 |
| D7_GSE28786_derived | OK | `data/gse28786_expression.parquet` | 8921747 | `8a193cb137ffbc8c` |  |
| D7_GSE28786_derived | OK | `data/gse28786_samples.parquet` | 8169 | `52c1f342ca8848bb` |  |
| D7_GSE28786_derived | OK | `data/gse28786_abundance.parquet` | 784809 | `183b0092ce6e88eb` |  |
| D7_GSE28786_derived | OK | `data/gse28786_response.parquet` | 2574377 | `44dbca9a88e5ac0e` |  |
| D7_GSE28786_derived | OK | `data/candidate_utr3_gse28786.parquet` | 19814509 | `061b7e346de8e455` |  |
| D8_GSE14073 | OK | `data/lit/burchard2009/GSE14073_esummary.json` | 6964 | `f6207a51f9c9df18` | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gds&id=200014073&retmode=json |
| D8_GSE14073 | OK | `data/raw/GSE14073-GPL6793_series_matrix.txt.gz` | 9206603 | `65be1b689d9810ac` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE14nnn/GSE14073/matrix/GSE14073-GPL6793_series_matrix.txt.gz |
| D8_GSE14073 | OK | `data/raw/GSE14073-GPL6794_series_matrix.txt.gz` | 4195865 | `da2263b23316e6e9` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE14nnn/GSE14073/matrix/GSE14073-GPL6794_series_matrix.txt.gz |
| D8_GSE14073 | OK | `data/raw/GSE14073_filelist.txt` | 4467 | `6b0f12848212a52c` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE14nnn/GSE14073/suppl/filelist.txt |
| D8_burchard2009 | FAILED | `data/lit/burchard2009/PMC2648714_fulltext.xml` | null | `` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2648714/fullTextXML |
| D8_burchard2009 | OK | `data/lit/burchard2009/PMC2648714_suppl.zip` | 164 | `f0103c21b520b5c1` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2648714/supplementaryFiles |
| D7_GSE28786_derived | OK | `data/accessibility_gse28786_u8_u15.npz` | 225993095 | `dc36fbd74c793ba5` |  |
| D8_GSE14073 | FAILED | `data/raw/GPL6793.annot.gz` | null | `` | https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL6nnn/GPL6793/annot/GPL6793.annot.gz |
| D8_GSE14073 | OK | `data/raw/GPL6793_family.soft.gz` | 205435599 | `35bd13a00b868050` | https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL6nnn/GPL6793/soft/GPL6793_family.soft.gz |
| D8_GSE14073_derived | OK | `data/gse14073_expression.parquet` | 20822397 | `0e50fd83a1b6d587` |  |
| D8_GSE14073_derived | OK | `data/gse14073_samples.parquet` | 5566 | `b15c591bf6240b86` |  |
| D8_GSE14073_derived | OK | `data/gse14073_abundance.parquet` | 846085 | `f9aac3c0a6b47308` |  |
| D8_GSE14073_derived | OK | `data/gse14073_response.parquet` | 9150211 | `feccb85526b1dfce` |  |
| D8_GSE14073_derived | OK | `data/candidate_utr3_gse14073.parquet` | 16452437 | `7bde296a927f5d0d` |  |
| D8_GSE14073_derived | OK | `data/accessibility_gse14073_u8_u15.npz` | 199787744 | `74358ed06844604a` |  |
| D2_birmingham | OK | `data/raw/birmingham/E-MEXP-668.idf.txt` | 6292 | `6e5da7f46806326b` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/E-MEXP-668.idf.txt |
| D2_birmingham | OK | `data/raw/birmingham/E-MEXP-668.sdrf.txt` | 49906 | `ec6d823773c29f9f` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/E-MEXP-668.sdrf.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097016656_S01_A01.txt` | 15118590 | `08555941688d3b79` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097016656_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097016657_S01_A01.txt` | 15112801 | `f2acdb7bb3c36680` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097016657_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097016658_S01_A01.txt` | 15118708 | `78eaa60c5f8aac7b` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097016658_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097016659_S01_A01.txt` | 15118220 | `4363333a8fa6282b` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097016659_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097016666_S01_A01.txt` | 15119075 | `563b527877130b96` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097016666_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097016667_S01_A01.txt` | 15122118 | `783e7ee194e5fe91` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097016667_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097016668_S01_A01.txt` | 15126322 | `e345701b79a6c9c9` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097016668_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097016669_S01_A01.txt` | 15117188 | `f72b2b79ac94d4be` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097016669_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097017936_S01_A01.txt` | 15120496 | `a57bddfe7e3ec10e` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097017936_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097017938_S01_A01.txt` | 15118420 | `5811f6a5a96bfc97` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097017938_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097017939_S01_A01.txt` | 15110884 | `8b5a66782f32588a` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097017939_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097017940_S01_A01.txt` | 15114130 | `3d28b0ce5f658633` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097017940_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097017951_S01_A01.txt` | 15125805 | `f1be1fca3c76e9c6` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097017951_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097017952_S01_A01.txt` | 15123078 | `c140ed9881ad0243` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097017952_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097017953_S01_A01.txt` | 15097950 | `3510ad7f3939262d` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097017953_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097017954_S01_A01.txt` | 15097764 | `c2641790214476a0` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097017954_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097018568_S01_A01.txt` | 15085459 | `a03bfd73a393ddb7` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097018568_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097018569_S01_A01.txt` | 15120715 | `156d68a8e2104c0b` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097018569_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097018911_S01_A01.txt` | 15108404 | `5be87f312891db8d` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097018911_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097018912_S01_A01.txt` | 15086750 | `11f2b9013fd074b6` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097018912_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_16012097018913_S01_A01.txt` | 15114561 | `784a8f756ffbefc7` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_16012097018913_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_251209725370_S01_A01.txt` | 16305108 | `5ae41fe0c25765a9` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_251209725370_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_251209725371_S01_A01.txt` | 16302822 | `a52f4d785931fdf1` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_251209725371_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_251209725411_S01_A01.txt` | 16302269 | `70a5c829b590db33` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_251209725411_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_251209725412_S01_A01.txt` | 16310732 | `93c2fb4ea867e9a9` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_251209725412_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_251209725425_S01_A01.txt` | 16286331 | `266074b7e4b71e93` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_251209725425_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_251209725538_S01_A01.txt` | 16264549 | `8091593968ae0172` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_251209725538_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_251209725539_S01_A01.txt` | 16268406 | `eebe5d5b34b722b9` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_251209725539_S01_A01.txt |
| D2_birmingham_arrays | OK | `data/raw/birmingham/US22502584_251209725545_S01_A01.txt` | 16257281 | `b9fd76a7578d1f11` | https://www.ebi.ac.uk/biostudies/files/E-MEXP-668/US22502584_251209725545_S01_A01.txt |
| D2_birmingham_derived | OK | `data/birmingham_response.parquet` | 4715895 | `d63c5e8e76543bb7` |  |
| D2_birmingham_derived | OK | `data/birmingham_sirna.parquet` | 7356 | `d8e5380bab9ea9ac` |  |
| jackson2006_oa_retry | FAILED | `data/lit/jackson2006/oa_fcgi_PMC1484447.xml` | null | `` | https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC1484447 |
| jackson2006_oa_retry | FAILED | `data/lit/jackson2006/oa_fcgi_new_host_PMC1484447.xml` | null | `` | https://pmc.ncbi.nlm.nih.gov/utils/oa/oa.fcgi?id=PMC1484447 |
| jackson2006_oa_retry | FAILED | `data/lit/jackson2006/PMC1484447_fulltext_retry.xml` | null | `` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/fullTextXML |
| jackson2006_oa_retry | OK | `data/lit/jackson2006/PMC1484447_suppl_retry.zip` | 164 | `d0ce25d9cbb43140` | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1484447/supplementaryFiles |
| jackson2006_oa_retry | OK | `data/lit/jackson2006/efetch_PMC1484447.xml` | 7654 | `7447b6587898e6b0` | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=1484447&retmode=xml |
| features | OK | `data/features.parquet` | 2269533 | `12f7c2329bc72d4e` |  |
| D7_GSE28786_derived | OK | `data/features_gse28786.parquet` | 1552090 | `541a046b3f080730` |  |
| figures | OK | `figures/CAPTIONS.json` | 8079 | `d4905904723ba2d8` |  |
| figures | OK | `figures/CAPTIONS.md` | 8110 | `40ed991249d4e1d0` |  |
| D2_EMEXP668_derived | OK | `data/features_emexp668.parquet` | 3500072 | `4a750155a3beac66` |  |

## 5. Manifest

| key | value |
|---|---|
| `generated_utc` | 2026-09-06T19:41:07Z |
| `git_commit` | 0da907be5184eea8732e44cd580e9efe431b8b0b |
| `git_branch` | main |
| `python_version_short` | 3.13.12 |
| `platform` | Linux-6.17.0-22-generic-x86_64-with-glibc2.39 |
| `cpu_count` | 16 |
| `n_experiments` | 35 |
| `n_failed` | 0 |
| `total_experiment_wall_clock_seconds` | 3680.7 |

`pip freeze` has 228 entries; full list in `MANIFEST.json`.

## 6. verify.py

| key | value |
|---|---|
| `generated_utc` | 2026-09-05T07:19:16Z |
| `stages_run` | ABC |
| `rtol` | 1.0000e-06 |
| `allow_missing` | false |
| `n_checks` | 159 |
| `n_failed` | 0 |
| `exit_status` | 0 |
| `verdict` | PASS |


**`checks`**

| stage | name | ok | detail |
|---|---|---|---|
| A | data/raw/GSE5814_family.soft.gz | true |  |
| A | data/raw/GSE5814-GPL2029_series_matrix.txt.gz | true |  |
| A | data/raw/GSE5814-GPL3991_series_matrix.txt.gz | true |  |
| A | data/raw/GSE5814-GPL3992_series_matrix.txt.gz | true |  |
| A | data/raw/GSE5814_filelist.txt | true |  |
| A | data/raw/gencode_README.TXT | true |  |
| A | data/raw/gencode_MD5SUMS.txt | true |  |
| A | data/raw/gencode.v50.pc_transcripts.fa.gz | true |  |
| A | data/raw/gencode.v50.annotation.gtf.gz | true |  |
| A | data/raw/refseq_NM_001315.fasta | true |  |
| A | data/raw/refseq_NM_005030.fasta | true |  |
| A | data/raw/refseq_NM_006219.fasta | true |  |
| A | data/raw/refseq_NM_139013.fasta | true |  |
| A | data/gencode_transcripts.parquet | true |  |
| A | data/gencode_tx_tags.parquet | true |  |
| A | data/gencode_canonical_by_symbol.parquet | true |  |
| A | data/gse5814_expression.parquet | true |  |
| A | data/gse5814_probe_annotation.parquet | true |  |
| A | data/hela_abundance.parquet | true |  |
| A | data/lit/garcia2011/nsmb2115_MOESM7.xlsx | true |  |
| A | data/lit/jackson2003/nbt831_MOESM2.pdf | true |  |
| A | data/lit/sigoillot/srep00428-s1.xls | true |  |
| A | data/lit/GSE5814_RAW.tar | true |  |
| A | data/recovered_seeds.parquet | true |  |
| A | data/sirna_sequences.parquet | true |  |
| A | data/accessibility_u8_u15.npz | true |  |
| A | data/raw/huesken_Hu.csv | true |  |
| A | data/raw/huesken_Hu_unnorm.csv | true |  |
| A | data/raw/huesken_HuTD.csv | true |  |
| A | data/raw/oligoformer_tree.json | true |  |
| A | data/raw/huesken_genes/C6orf110.csv | true |  |
| A | data/raw/huesken_genes/CD81P3.csv | true |  |
| A | data/raw/huesken_genes/CDC34.csv | true |  |
| A | data/raw/huesken_genes/FLJ11011.csv | true |  |
| A | data/raw/huesken_genes/HIP2.csv | true |  |
| A | data/raw/huesken_genes/HSPC150.csv | true |  |
| A | data/raw/huesken_genes/NOG.csv | true |  |
| A | data/raw/huesken_genes/P2RX3.csv | true |  |
| A | data/raw/huesken_genes/RAB6IP1.csv | true |  |
| A | data/raw/huesken_genes/Rn_Cacng4.csv | true |  |
| A | data/raw/huesken_genes/Rn_Dcbld2.csv | true |  |
| A | data/raw/huesken_genes/Rn_Fxyd6.csv | true |  |
| A | data/raw/huesken_genes/Rn_Mmp7_1.csv | true |  |
| A | data/raw/huesken_genes/Rn_Mmp7_2.csv | true |  |
| A | data/raw/huesken_genes/Rn_P2rx2.csv | true |  |
| A | data/raw/huesken_genes/Rn_TCAP.csv | true |  |
| A | data/raw/huesken_genes/Rn_cacnb1.csv | true |  |
| A | data/raw/huesken_genes/SOST.csv | true |  |
| A | data/raw/huesken_genes/TC10.csv | true |  |
| A | data/raw/huesken_genes/UBE2B.csv | true |  |
| A | data/raw/huesken_genes/UBE2C.csv | true |  |
| A | data/raw/huesken_genes/UBE2D3.csv | true |  |
| A | data/raw/huesken_genes/UBE2E3.csv | true |  |
| A | data/raw/huesken_genes/UBE2G1.csv | true |  |
| A | data/raw/huesken_genes/UBE2H.csv | true |  |
| A | data/raw/huesken_genes/UBE2I.csv | true |  |
| A | data/raw/huesken_genes/UBE2J1.csv | true |  |
| A | data/raw/huesken_genes/UBE2L3.csv | true |  |
| A | data/raw/huesken_genes/UBE2L6.csv | true |  |
| A | data/raw/huesken_genes/UBE2M.csv | true |  |
| A | data/raw/huesken_genes/UBE2N.csv | true |  |
| A | data/raw/huesken_genes/UBE2S.csv | true |  |
| A | data/raw/huesken_genes/UBE2V1.csv | true |  |
| A | data/raw/huesken_genes/Ufc1.csv | true |  |
| A | data/constants.json | true |  |
| A | data/lit/constants/CONSTANTS_SOURCES.md | true |  |
| A | data/lit/constants/wang2012_genesdev_PMC3323880.pdf | true |  |
| A | data/lit/constants/janas2012_PMC3479394.pdf | true |  |
| A | data/lit/constants/rna_errata_PMC3504684.pdf | true |  |
| A | data/lit/constants/marinov2014_PMC3941114.xml | true |  |
| A | data/lit/constants/wee2012_PMC3595543.html | true | hash not enforced: server-side rendering of a PMC article page; re-fetching the same URL during this build returned different bytes. Europe PMC returns 404 for both fullTextXML and pdf=render for PMC3595543, so no byte-stable form of this source exists. The verbatim Kd sentences quoted in data/lit/constants/CONSTANTS_SOURCES.md are the durable record. |
| A | data/lit/constants/qiagen_faq_rna_per_cell.html | true |  |
| A | data/huesken.parquet | true |  |
| A | data/raw/d2_vandongen_PMC2635553_suppl.zip | true |  |
| A | data/raw/d2_GSE5291_family.soft.gz | true |  |
| A | data/raw/d2_GSE5769_family.soft.gz | true |  |
| A | data/lit/caffrey2011/PMC3130022_fulltext.xml | true | hash not enforced: volatile source |
| A | data/raw/GSE28786_series_matrix.txt.gz | true |  |
| A | data/raw/GSE28786_filelist.txt | true |  |
| A | data/raw/GSE28786_family.soft.gz | true |  |

_159 rows total, first 80 shown; full data in the JSON._

