<!-- DRAFT built 2026-10-15. Sources: team writeup (wiki word.pdf), repo analysis files, Linear issues, LCA report. Items marked TODO or [pending] need a human. Provenance comments sit next to each section. -->

<div class="alert alert-warning" role="alert" markdown="1">
**Read this first.** Every number on this page describes a model. **None is validated against wet-lab data.** Labels: **[computed]** our own run; **[literature]** published source; **[hypothesis]** reasoned, untested; **[pending]** not finished.
</div>

## At a glance {#m0}

- We worked in six steps, each handing one result to the next: sequence → FAS interaction → bridge → metabolism → trust → process (figure on the [home page](./)).
- **Central assumption:** a point mutation in *S. cerevisiae* FAS2 (V1254W, by analogy with *Yarrowia* I1220W) can release C14 early. This is **[hypothesis]**, not established.
- **Main findings:** the model makes C14:0 only by shortening C16:0 through beta-oxidation; no knockout beats wild type; an early-release reaction adds only +2.6% and is limited by NADPH; our own scoring setup failed its checks.
- **Where to jump:** [Data](#m3) · [Assumptions](#m4) · [Sequence](#sequence) · [Structure](#structure) · [Bridge](#bridge) · [Metabolism](#metabolism) · [Trust](#trust) · [Process](#process) · [Effect on design](#m6) · [Limits](#m7) · [Reproducibility](#m8) · [References](#m9)

## Approach and what it tells us {#m1}

| Step | Question | Method | What it provides |
|---|---|---|---|
| 1 Sequence | Which ScFAS2 residue corresponds to the *Yarrowia* chain-length residue? | EMBOSS Needle global alignment | A candidate site (V1254W) |
| 2 FAS interaction | Does the KS pocket accommodate a C14 chain; what must not be mutated? | Boltz-2 on the KS domain with distance constraints; structural comparison | A residue shortlist and an exclusion list |
| 3 Bridge | Can a metabolic model represent the mutation? | Add an early-release reaction to Yeast9 | A model that can simulate the intervention |
| 4 Metabolism | What can the cell reach, at what growth cost? | Flux balance analysis (FBA) on Yeast9, COBRApy | Feasibility frontier, route, knockout screen |
| 5 Trust | Does "best" mean anything? Is learned search needed? | Six checks on the scoring function; brute force vs greedy vs RL | Which rankings may be believed |
| 6 Process | Is the product worth making? | CFD of an immersion tank; screening LCA | Use-phase and production footprint |

**Why these methods.** FBA needs no kinetic parameters, so it can run on a genome-scale model; it gives an upper limit, not a prediction. Boltz-2 was used because the KS pocket of the solved ScFAS2 structure (8PRW) holds no fatty acid, so ligand placement had to be predicted. Brute force was kept as the reference search because at our scale it is exact and cheap. Existing strain-design tools (OptKnock, OptGene, OptForce, RobustKnock, cameo, MEWpy, OptFlux, StrainDesign) return designs whether or not the scoring underneath them can separate candidates; none of those we surveyed checks first.

## Data and parameters {#m3}

<!-- provenance: wiki word.pdf pp1-2; ks_analysis report (Linear IGE-14); FBA report; fas_c14_diagnosis.md -->

### Structures **[literature]**

| PDB | Contents | Resolution | Role |
|---|---|---|---|
| 8PRW | ScFAS2 | 1.9 Å | Primary receptor structure. KS3 pocket holds no fatty acid |
| 1F91 | *E. coli* KAS I with capric acid | 2.40 Å | Reference for an acyl chain in a KS pocket |
| 2PFF | Yeast FAS | 4.00 Å | Retained as a homology template; not used in the final workflow |
| 2VKZ | Cerulenin-inhibited ScFAS | n/a | Reference for the catalytic state (Johansson 2008) |

Numbering follows UniProt P19097 (FAS2, alpha) and P07149 (FAS1, beta). KS-only models use a local offset of 1122; three model files carry an inserted `UNK` residue at local position 84 (+1 shift downstream). All residue identifiers on this site are converted to full-sequence P19097 numbering.

### Metabolic model and run conditions **[computed]**

Two FBA analyses exist. They use different conditions, so their numbers differ by design. We show conditions with every number.

| | Analysis A (pre-flight / repo) | Analysis B (FBA report) |
|---|---|---|
| Model | Yeast9 (`data/models/yeast-GEM.xml`) | Yeast-GEM v9.1.1: 4,105 reactions, 2,748 metabolites, 1,143 genes |
| Glucose uptake | 1.0 mmol/gDW/h | 1.1 mmol/gDW/h |
| Non-growth maintenance | 0.7 mmol ATP/gDW/h | 0.7 mmol ATP/gDW/h |
| Strain | Wild type | BY4742 (HIS3, LEU2, LYS2 deleted; His, Leu, Lys supplied) |
| Wild-type growth | 0.0811 h⁻¹ | 0.09768 h⁻¹ |
| Fatty-acid-CoA ligases | Forward-only in the robustness check | Forward-only (primary); original bounds as sensitivity |
| Solver | GLPK | GLPK |

<div class="alert alert-secondary" role="alert" markdown="1">
**[pending]** Reconcile the two analyses: confirm the exact model version in each (a team comment names v9.0.2 for one run), and the reason for the growth-rate difference. Glucose uptake differs (1.0 vs 1.1), which probably explains most of it. Tracked internally.
</div>

### Literature inputs **[literature]**

- Chain-length control by the KS domain and the *Yarrowia* I1220W result: Rigouin et al. 2017 (C14 raised to 11.6% of total lipid in stationary phase).
- Catalytic and gating residues of ScFAS: Johansson et al. 2008 (PDB 2VKZ).
- Background fatty-acid profile of *S. cerevisiae*: Wei, Siewers, Nielsen 2017 (C16:0 13.7, C16:1 50.0, C18:0 3.5, C18:1 30.0 % of total fatty acids).
- Assay noise: GC-MS composition replicate variation of 1–5%, taken from our project write-up, not yet checked against the literature.

## Assumptions and why {#m4}

| # | Assumption | Why | If wrong | Status |
|---|---|---|---|---|
| A1 | A FAS2 point mutation (V1254W) can release C14 in *S. cerevisiae* | By homology to *Yarrowia* I1220W. *S. cerevisiae* FAS point-mutation literature we found reports C6/C8 shifts (Gajewski 2017), not C14 | Every downstream number is moot | **[hypothesis]** |
| A2 | Only the KS domain needs to be modelled | Full alpha subunit (1,887 aa) runs out of GPU memory; the acyl tunnel and residues of interest lie inside KS | Beta-subunit and chamber context are ignored | Reviewed by the team; not tested |
| A3 | Free myristic acid stands in for the covalent acyl-enzyme intermediate | Same approach as Rigouin 2017 and Olsen 2001 | Geometry differs near the catalytic cysteine | **[literature]** precedent |
| A4 | Distance constraints are needed to place the ligand | Unconstrained Boltz-2 does not place the chain near the pocket | Constraint choice biases the pose | **[computed]** |
| A5 | FBA: steady state, no kinetics, no regulation | Standard FBA assumptions | Results are upper limits, not predictions | **[literature]** |
| A6 | Fatty-acid-CoA ligases forward-only in the primary scenario | The reaction is ATP-driven and strongly one-way; reversal gave a thermodynamically questionable route | Some knockouts look viable only via reverse flux | **[computed]** (sensitivity shown) |
| A7 | Myristate export is a reaction without a gene | How Yeast9 represents it | Secretion mechanism is not established | **[literature]** model property |
| A8 | The model outputs free myristate, not methyl myristate | Esterification is not in the model | Titre of the coolant is not predicted | By construction |
| A9 | Assay resolution is GC-MS replicate noise of 1–5% | Project write-up | Thresholds for "separable" shift | Not checked against literature |
| A10 | Search benchmark runs on a synthetic landscape | Our real landscape turned out to be flat, so comparing searches on it measures nothing | Ranking may not transfer | **[computed]** |
| A11 | Tank CFD uses constant fluid properties | Simplification | Temperature-dependent viscosity is missed | See [Sustainability](sustainability) |

## Step 1. Sequence level {#sequence}

<!-- provenance: wiki word.pdf pp2-3; ScFAS2 KS Domain Analysis report (Linear IGE-14); Linear IGE-40 comments -->

**Question.** *Which ScFAS2 residue sits where Yarrowia I1220 sits?* Rigouin et al. 2017 identified I1220 in the fatty acid binding site of YlFAS as controlling chain length: replacing it with tryptophan raised C14 content to 11.6% of total lipid in stationary phase. **[literature]**

**Method.** EMBOSS Needle global pairwise alignment (BLOSUM62, gap open 10, extend 0.5) of YlFAS alpha (Q6C8H7, 1,852 aa) against ScFAS2 (P19097, 1,887 aa). Global alignment is used because the sequences differ in length, and insertions shift the numbering. **[computed]**

| ScFAS2 (P19097) | YlFAS | Relationship |
|---|---|---|
| M1251 | M1217 | Identical |
| V1254 | I1220 | Conservative; both β-branched aliphatic |
| M1260 | M1226 | Identical |

The three pairs are separated by a constant 34-residue offset from insertions in ScFAS2 upstream of the KS domain. There are no gaps at or beside the key column, so the V1254 ↔ I1220 equivalence does not depend on gap placement. The direct ScFAS2 analogue of the Rigouin mutation is therefore **V1254W**.

<figure class="figure my-4">
  <img src="/static/figures/alignment_strip.png" class="figure-img img-fluid" alt="Two rows of residue boxes: YlFAS M1217, I1220, M1226 above ScFAS2 M1251, V1254, M1260, joined by vertical lines labelled identical, conservative, identical.">
  <figcaption class="figure-caption">Equivalent positions from the Needle alignment (schematic). Transfer is by homology; the effect in <em>S. cerevisiae</em> is an assumption (A1).</figcaption>
</figure>

**How Rigouin placed the substrate, and what we could reuse.** Rigouin modelled the *Yarrowia* KS domain from three structures (2PFF, 2VKZ, 4V58), then superimposed it on *E. coli* KAS I bound to capric acid (1F91), copied the C10 chain into the equivalent pocket and extended it to C16. We have a better starting structure (8PRW, 1.9 Å), but it contains no fatty acid in the KS3 pocket, so ligand placement remained our task. **[computed, team review]**

**Conservation versus necessity.** A conservation filter would remove positions where mutation is likely destructive. Our three residues are conserved because they set chain length, which every fatty-acid-making organism selects for. The exclusion criterion we apply is therefore catalytic or mechanistic necessity, not conservation score alone.

**Status.** **[pending]** BLAST of the template against ScFAS2 (in review) and the conservation/phylogenetic analysis to identify segments to avoid. Identification of further mutation sites is blocked on the latter.

## Step 2. FAS interaction level {#structure}

<!-- provenance: wiki word.pdf pp3-8; Linear IGE-14 comment 2026-06-20; ks_analysis.pdf; Linear IGE-20 comments -->

**Question.** *Does the KS3 pocket hold a C14 chain, and which residues must we leave alone?*

**Setup.** Boltz-2 on the KS domain only (residues 1123–1657, UniProt annotation), on Google Colab (T4 GPU) with `--use_msa_server --diffusion_samples 1`. Ligand: myristic acid (SMILES CCCCCCCCCCCCCC(=O)O). **[computed]**

**Unconstrained runs fail.** Without constraints Boltz-2 does not place the fatty acid near the pocket (baseline ligand ipTM 0.511, interface position error 9.1 Å). The ligand is a flexible aliphatic chain with no strong polar anchor, so the scoring function has little to latch onto. We report this as a negative result. Every later run used explicit distance constraints.

**Constrained runs.** Five models were generated and compared:

| Model | Ligand |
|---|---|
| scfas2_ks3_c14_v2_model_0 | C14 |
| ks3_c14_constrained_model_0 | C14 |
| run_c16_model_0 | C16 (control) |
| run_c22_model_0 | C22 (control) |
| run3_model_0 | C14 |

Confidence scores for the earlier C14 runs (from the KS-domain report):

| Run | Constraint | Confidence | Ligand ipTM | Interface pos. error (Å) | Complex ipLDDT |
|---|---|---|---|---|---|
| Baseline | none | 0.835 | 0.511 | 9.124 | 0.649 |
| v2 | max_dist 6.0 Å | 0.906 | 0.831 | 3.124 | 0.667 |
| Run1 (Colab) | none on max_dist | 0.920 | 0.806 | 2.023 | 0.836 |
| Run2 (Colab) | max_dist 6.0 Å | 0.917 | 0.796 | 2.072 | 0.829 |
| Run3 (Colab), selected | max_dist 8.0 Å | 0.919 | 0.812 | 2.031 | 0.831 |

<div class="alert alert-secondary" role="alert" markdown="1">
**[pending]** These confidence values come from the first constrained runs. Per-residue confidence for the final three-residue constrained models has not yet been extracted. The model comparison across all five models (pairwise RMSD of backbone and ligand) has not been computed.
</div>

**Structural quality.** Protein-fold RMSD of the constrained C14 model against 8PRW chain A KS3: 1.39 Å (PyMOL `cealign`). Against *E. coli* KAS I (1F91): 2.38 Å over 232 aligned residues, which is fold-level agreement between distant homologues. It licenses using 1F91 as a reference for how an acyl chain occupies a KS tunnel, but not for transferring ligand coordinates atom by atom. Ligand placement comes from Boltz-2, not from 1F91.

### Structurally relevant residues

All three line the acyl tunnel, have an *Yarrowia* equivalent, and were examined in every constrained model.

| Residue | YlFAS | Distance to C14 in constrained model | Disposition |
|---|---|---|---|
| M1251 | M1217 | 0.96 Å (clash); 0.96–1.77 Å across models | Excluded from mutagenesis |
| V1254 | I1220 | 4.35 Å (superposition: 5.72 Å) | Retained; proposed V1254W |
| M1260 | M1226 | 6.91 Å | Retained as secondary candidate |

M1260 is slightly far, consistent with C14 being two carbons shorter than the C16 substrate Rigouin modelled. Distances in this table come from team comments on the constrained run and are pending the formal proximity criterion below.

### Catalytic and mechanistic exclusions **[literature]**

From the cerulenin-inhibited ScFAS structure (Johansson 2008, PDB 2VKZ):

| Residue | Role | Why excluded |
|---|---|---|
| C1305 | Nucleophilic active-site cysteine | Forms the acyl-enzyme thioester. Absolute exclusion |
| F1646 | Shields the active site; flips to give access | Gates catalytic accessibility |
| M1251 | Centre of the acyl-binding tunnel; rotates to unlock the inner cavity | A conformational gate; mutating it alters tunnel access, not volume |
| G1250 | Next to M1251; strains mutated here are characterised in the same work | Mechanically coupled to the gate |
| K1413 to K1423 loop | Ligand-accessibility determinant | Not catalytic, but not safely mutable |

### The persistent M1251 clash **[hypothesis]**

In every constrained run the acyl chain clashes with M1251 at 0.96–1.77 Å. The clash is also present in the raw structural superposition built from 8PRW, so it is not only a Boltz artefact. Attempted fixes did not resolve it: OpenBabel UFF minimisation, PyMOL sculpting, and the PyMOL mutagenesis wizard (which only ranks pre-enumerated rotamers and cannot find an intermediate side-chain geometry).

**Working interpretation.** The clash reflects the closed rotameric state of a known conformational gate, not an error in ligand placement. 8PRW and the structures that dominate Boltz-2 training are crystallographic states, so a method that holds the receptor rigid or samples only library rotamers will reproduce the closed gate. This is testable against data we already hold; the test is not yet run. It also makes molecular dynamics (GROMACS or Amber) a reasoned necessity rather than a fallback.

### Controls **[pending]**

C16 and C22 runs exist as controls: if the pocket discriminates on chain length, the ligands should behave differently in it. A preliminary team comparison found C14 about 6 Å from the two target residues, while for C16 the distances were non-uniform (about 5 Å and 8 Å). A formal positive control (a system that definitely binds) and a negative control are in progress and not yet written up.

### Limits of this step

- **[pending]** No formal proximity criterion (a declared distance cutoff with a sensitivity sweep).
- **[pending]** No per-residue confidence for the final constrained models.
- **[pending]** No cross-model consensus rule; cross-model agreement is the only internal confidence measure we have.
- **[pending]** No minimised ligand-bound state, so no model represents a relaxed pocket.

<div class="alert alert-info" role="alert" markdown="1">
**Figure to come.** A rendered image of the KS3 pocket with C14 and residues M1251, V1254, M1260, labelled with distances, has not been made yet (needs the Boltz output files and PyMOL).
</div>

## Step 3. The bridge: representing the mutation in a metabolic model {#bridge}

<!-- provenance: rl based model/analysis/fas_c14_diagnosis.md (reproducible: analysis/fas_c14_diagnosis.py); Linear IGE-31 comments -->

**Question.** *Can Yeast9 represent early C14 release from FAS at all?*

**Finding.** Yeast9 represents fatty-acid synthase as reactions ending at C16:0-CoA and C18:0-CoA. It has no reaction for early C14 release. The model could therefore not represent the intervention we are building, and an earlier workaround added a myristate exchange by hand. We added a documented early-release reaction (`fbareduce_FAS_C14_release`) and re-ran the analysis. **[computed]**

**Result.** With the reaction ON, 100% of C14:0 comes from the new reaction and none from beta-oxidation. Maximum C14:0 export rises only **+2.6%** at 50% of wild-type growth (0.119191 → 0.122237 mmol/gDW/h; +3.1% at 10% growth, +2.6% at 90%).

<figure class="figure my-4">
  <img src="/static/figures/bridge_early_release.png" class="figure-img img-fluid" alt="Left: bars of maximum C14 export at 10, 50 and 90 percent growth, with and without the early-release reaction, nearly equal. Right: horizontal bars showing the change in C14 export when each resource is made free: NADPH plus 150.9 percent, ATP plus 36 percent, NGAM zero plus 7.6 percent, acetyl-CoA and malonyl-CoA plus 0.01 percent.">
  <figcaption class="figure-caption">The reaction changes the route, not the amount. Freeing carbon-chain supply does nothing; freeing NADPH raises C14 by 150.9%. Yeast9, glucose uptake 1.0, NGAM 0.7. Model-implied upper bounds.</figcaption>
</figure>

**Why so small.** Making free C14:0 directly from FAS saves cofactors relative to the beta-oxidation route that already exists, and the saving is small once that route's own credits are counted. Neither acetyl-CoA nor malonyl-CoA is limiting. The limits are glucose carbon (about 0.52 of the 1.0 glucose is committed to growth plus maintenance at 50% growth) and **NADPH (12 per C14)**, made in the oxidative pentose phosphate pathway at a carbon cost, with ATP second. With NADPH and ATP freely regenerated and no maintenance, the model reaches the carbon-conservation limit of 0.42857 mmol/gDW/h (1/2.333), so the gap to the achieved yield is entirely cofactor cost.

<div class="alert alert-secondary" role="alert" markdown="1">
**Caveat.** The reaction is a modelling hypothesis about what V1254W does. It inherits assumption A1. Also, the frontier and knockout screen in Step 4 were run on the model **without** the reaction. Re-running them with it is **[pending]**.
</div>

**Gaps and naming in Yeast9 found along the way** (team model comparison; documents not yet summarised here). Yeast9 was chosen over Yeast8 because it represents more of the pathways we need. Genes flagged as absent: *PEX11* (beta-oxidation) and *ATR1*, *CYP94C1* (ω-oxidation). *FOX1* is present as *POX1*, a naming mismatch with the same function. A hypothesis, not yet run, is that omitting the two ω-oxidation genes costs little yield. **[pending]**

## Step 4. Metabolism-wide level {#metabolism}

<!-- provenance: wiki word.pdf pp13-15 (analysis A); FBA report pp11-12 (analysis B); analysis/reachable_demo; analysis/metrics -->

**Question.** *What C14:0 can the cell reach, at what cost to growth, and by which route?*

### Feasibility frontier (analysis A) **[computed]**

In unmodified Yeast9, wild-type yeast already exports pure C14:0 at any growth up to 90% of normal, with no genetic edits. Purity never limits; growth trades off linearly against yield.

| Growth held at | C14:0 export (mmol/gDW/h) | C14:0 share of exported fatty acid |
|---|---|---|
| 10% of wild type | 0.211 | 100% |
| 25% | 0.178 | 100% |
| 50% | 0.119 | 100% |
| 75% | 0.060 | 100% |
| 90% | 0.024 | 100% |

An independently written earlier pipeline gave 0.209152 at or above 10% growth, against 0.2108 here (0.8% apart).

<figure class="figure my-4">
  <img src="/static/figures/feasibility_frontier.png" class="figure-img img-fluid" alt="Line chart of maximum C14 export against growth held, falling from 0.211 at 10 percent to 0.024 at 90 percent. Wild type and two knockout sets overlap; sets containing POX1 are at zero.">
  <figcaption class="figure-caption">No knockout improves on wild-type C14:0 production. FAA1, and DGA1+FAA1+LRO1, equal no edit; FAA1+FAA4 is 2% below; any set containing POX1 gives exactly zero. Model run without the early-release reaction.</figcaption>
</figure>

### Same envelope, second analysis (analysis B) **[computed]**

Under analysis B's conditions (see [Data](#m3)), maximum export with a minimum growth requirement:

| Minimum growth (% of max) | Min growth rate (h⁻¹) | Max C14 export (mmol/gDW/h) |
|---|---|---|
| none | 0 | 0.25001 |
| 10% | 0.00977 | 0.22649 |
| 25% | 0.02442 | 0.19036 |
| 50% | 0.04884 | 0.12719 |
| 75% | 0.07326 | 0.06359 |
| 90% | 0.08791 | 0.02544 |
| 100% | 0.09768 | 0 |

At maximum growth the model exports no C14, and the minimum possible export is zero at every growth rate, so **C14 production is not growth-coupled**. The values are consistently about 6–7% higher than analysis A because the conditions differ; the shape is the same. The "no growth requirement" row is not a capacity shown for a growing culture.

### The route **[computed]**

At 50% growth every step of one route carries identical flux (0.1192 mmol/gDW/h), which identifies it as a single unbranched path:

C16:0 → (r_0402) hexadecanoyl-CoA → (r_0123, acyl-CoA oxidase, *POX1*) → (r_2251) enoyl-CoA hydratase → (r_0102) myristoyl-CoA → (r_0412) free C14:0 → export.

The model makes C14:0 by removing one two-carbon unit from C16:0 through beta-oxidation, not by ending synthesis early. *POX1* catalyses the committed step, which is why deleting it gives exactly zero. Robustness checks: forbidding reversal of the ATP-driven ligase step lowers production by only 2% (0.1192 → 0.1167); loopless FBA returns identical flux. Blocking r_0102 (analysis B) lowers export at the 50% growth floor from 0.12719 to 0.10977, and the model switches to an alternative route (degradation of C18:1 to C12 then re-elongation); blocking both abolishes C14 export.

Our original plan was to knock down degradation to preserve C14:0. In this model degradation is the only source of C14:0 without the new reaction, so the strategy is inverted relative to what the model predicts.

### Knockout and blocking screen (analysis B) **[computed]**

- All 1,143 single-gene deletions screened in both ligase scenarios: 965 viable, 178 lethal (lethal = no positive biomass flux; a computational classification, not a prediction of cell death). None forced myristate export at the deleted strain's own maximum growth.
- Deleting *POX1*, *FOX2*, *POT1*, *PXA1* or *PXA2* abolished modelled C14 export, because the C14-producing routes depend on peroxisomal beta-oxidation. *FAS1*, *FAS2*, *ACC1* and *OLE1* deletions were lethal under the specified medium.
- Blocking individual C14-consuming reactions (r_0125, r_0105, r_2155, r_2195/r_2201, r_2220) changed nothing at 50% growth, because all carried zero flux at that optimum.

### Consistency checks **[computed]**

The biomass reaction r_2111 and the biomass pseudo-reaction r_4041 carry identical flux at every solution (the biomass metabolite has exactly one producer and one consumer), so using either gives the same results; r_2111 is used throughout, being the model's own default objective.

### Growth-rate penalty **[pending]**

The penalty of an intervention is (1 − μ<sub>max,i</sub> / μ<sub>max,WT</sub>) × 100, where μ<sub>max,WT</sub> is the maximum growth rate of the unmodified model and μ<sub>max,i</sub> that after intervention *i*. The unrestricted growth penalty of each intervention has not yet been calculated.

### Reachable set and frontier **[computed]**

The same model supports a reachable-set analysis for a fatty-acid *profile*, not only for C14 amount. The plot below is for an illustrative C14-rich target; the target is an assumption, not a measurement.

<figure class="figure my-4">
  <img src="/static/figures/reachable_c14.png" class="figure-img img-fluid" alt="Left: curve of best achievable distance to the target profile against minimum total fatty-acid titre, flat near zero until a knee at 0.118 and then rising, with an unreachable region shaded above the maximum titre. Right: stacked bars showing fatty-acid composition at selected points on the frontier.">
  <figcaption class="figure-caption">Reachable set and frontier for an illustrative C14-rich target, Yeast9. The knee at 0.118 mmol/gDW/h is the largest titre within the assay's tie band of the target. Model-implied upper bounds; no wet-lab validation.</figcaption>
</figure>

## Step 5. Can we trust the ranking? {#trust}

<!-- provenance: wiki word.pdf pp9-13, 16-22; igem-preflight README; analysis/metrics/REPORT.md; Linear IGE-57 -->

### The failure that started it

Our pipeline ranked gene knockouts by how closely the predicted fatty-acid profile matched a target. Brute force over all 175 combinations returned a clear winner, FAA1 + FAA4, scoring 0.202529. The unedited strain scored 0.202509: a gap of **0.010%**. GC-MS fatty-acid composition varies by roughly 1–5% between biological replicates, so no experiment we could run would separate those two strains. The search was exact and the arithmetic correct; the scoring function measured nothing, and there was no error message for that. **[computed]**

### Six checks

Pre-flight runs six automated checks on a scoring function. Each returns PASS, WARN or FAIL with an explanation. The thresholds are tied to **assay resolution**, not solver tolerance: our first version compared score differences against solver tolerance (about one part in a million) and passed the broken pipeline.

| Check | Question | Result on our configuration |
|---|---|---|
| D1 | Does doing nothing score as well as the best intervention? | **FAIL**: best intervention beats doing nothing by 0.010% |
| D2 | Can the score separate candidates at measurable resolution? | **FAIL**: 20 candidates, all inside one measurement band |
| D3 | Does a weighted sum over several products control the blend? | **FAIL**: one product at every weight |
| D4 | Are product exchange reactions realistically bounded? | WARN: all four target exchanges bounded at 1000 |
| D5 | Is the score tracking growth rather than product? | WARN: growth identical across candidates |
| D6 | Do the scoring parameters change anything? | WARN: one parameter moves no score |

Verdict: **NOT USABLE. No proposals issued.** Four of the six checks are not new (D3–D6 automate established methods; D4 is already in memote). D1 and D2 we could not find automated in any tool we surveyed. See [Software](software).

<figure class="figure my-4">
  <img src="/static/figures/preflight_gate.png" class="figure-img img-fluid" alt="Diagram contrasting search, which ranks candidates, with pre-flight, which checks the scoring function. Pre-flight sits between the model and the search; on pass the search runs and produces a proposal sheet, on fail no proposals are issued with the reason.">
  <figcaption class="figure-caption">Search answers which candidate scores best. Pre-flight answers whether "best" means anything. Neither replaces the other.</figcaption>
</figure>

### Loss-function comparison **[computed]**

A comparison of ten distance measures for fatty-acid profiles (total variation, L2, cosine, Jensen–Shannon, Hellinger, KL, Bray–Curtis, Aitchison, 1-D and 2-D Earth Mover's) found that every metric except cosine and Aitchison resolves only about 4–8% relative differences at 3% noise. The recommended default is total variation (a true metric between 0 and 1; for a pure-C14 target it equals one minus the C14:0 fraction); the runner-up is the 2-D chain-aware Earth Mover's distance, which is the only candidate where C14:0 is genuinely closer to C16:0 than to C18:1. Designs whose total-variation losses differ by less than about 0.014 are tied at 3% noise. The profile target and yeast-like background used here are illustrative.

### Is learned search worth it? **[computed, synthetic landscape]**

We built a reinforcement-learning (RL) agent for knockout search and benchmarked it over 20 random seeds instead of assuming it helped:

| 10 genes, up to 3 knockouts | Finds exact best | Mean shortfall | Evaluations |
|---|---|---|---|
| Brute force | 100%, by definition | 0% | 175 |
| Greedy hill-climbing | 65% | 1.14% | 23 |
| Reinforcement learning | 10% | 10.13% | 1,204 |

Random search on the RL agent's budget also matched greedy, so the landscape has many near-optimal answers. A separate earlier RL run on a four-product profile found only 3 distinct flux vectors in 122 evaluations, the same degeneracy seen from another angle. **[pending]** Verification of that run by the named reviewers is not yet complete.

<figure class="figure my-4">
  <img src="/static/figures/rl_benchmark.png" class="figure-img img-fluid" alt="Three bar charts comparing brute force, greedy and reinforcement learning: share finding the exact best answer (100, 65, 10 percent), mean shortfall (0, 1.14, 10.13 percent) and evaluations (175, 23, 1204).">
  <figcaption class="figure-caption">Try the trivial baseline first. 20 seeds, synthetic landscape; our RL agent is a simple linear Q-learner, so we can say ours lost, not that the approach cannot work.</figcaption>
</figure>

**When does enumeration stop being affordable?** At 0.30 s per FBA solve (measured on our evaluator): 10 candidate genes take 52 s for exact search, 20 take 7 min, 30 take 23 min, 40 take 54 min, 50 take 1.7 h. Greedy takes 6–35 s throughout and reached 99.5–100% of the exact optimum (single seed; indicative only). In this range a learned search is not needed.

## Step 6. Process level {#process}

<!-- provenance: LCA report; Linear IGE-48 (coolant selection comments) -->

This step connects the strain to its use. Full detail is on [Sustainability](sustainability); the modelling parts are summarised here.

- **CFD [computed].** 17 OpenFOAM simulations (chtMultiRegionFoam, steady state, 3-D conjugate heat transfer, constant fluid properties) of a 1,200 W server immersed in each coolant. At the same flow (0.42 m/s) the hottest component reaches 78.1 °C with methyl myristate against 87.2 °C (mineral oil) and 88.0 °C (ester-based coolant). Methyl myristate stays below 85 °C at 0.27 m/s; the others need 0.80 m/s.
- **LCA [computed, screening level].** Methyl myristate's production footprint per kg is far higher than the commercial coolants' today; in use it can save cooling electricity. Whether that nets out in its favour depends on the grid carbon factor. See the caveats on the Sustainability page.
- **Coolant selection [computed, data-limited].** A separate comparison of methyl myristate and isopropyl myristate scored methyl myristate about 9% higher on thermal figures of merit, a margin inside the estimate uncertainty. It recommended **isopropyl myristate** on operability grounds because methyl myristate melts at about 18 °C, leaving about 2 °C of margin at a 20 °C inlet. Neither ester can be certified for energised immersion until dielectric breakdown voltage, volume resistivity and pour point are measured. **[pending]** The team's decision between the two is not recorded on this site.

## How the results affected our design {#m6}

1. **We dropped the plan to knock down degradation to preserve C14:0.** The model shows degradation is the only C14:0 source without early release, and deleting *POX1* gives zero. The rule against sending degradation knockdowns to the wet lab in a first iteration now has a mechanistic reason.
2. **We added a FAS early-release reaction as a documented model modification** and measured its effect: +2.6%, NADPH-limited. This tells us where the model says the limit lies (cofactors, not chain supply). Acting on it is **[pending]**.
3. **We excluded M1251, C1305, F1646, G1250 and K1413–K1423 from mutagenesis** and kept V1254W as the lead candidate, with M1260 secondary.
4. **We did not send a ranked knockout list to the wet lab**, because checks D1 and D2 failed on our own scoring. The tool refused to issue proposals, and we followed it.
5. **We recommend brute-force enumeration** at our scale, and a trivial baseline before any learned search.
6. **Coolant choice** between methyl and isopropyl myristate is **[pending]**; it does not change the upstream strain-design question, since both are esters of the same C14 acid.

## Limitations and validation status {#m7}

| Limitation | Effect on conclusions | Status |
|---|---|---|
| No wet-lab data of any kind | Every number is a statement about a model | Not available to the team |
| V1254W route to C14 in *S. cerevisiae* is an assumption | All downstream numbers are conditional | **[hypothesis]** |
| M1251 gate explanation untested | Basis for excluding M1251 is a hypothesis; a literature report of *S. cerevisiae* strains mutated at M1251 may bear on it | **[pending]** check against the paper |
| No MD or relaxed ligand-bound pocket | Pocket geometry is rigid-receptor | Large-scale; a short minimisation is feasible |
| No formal proximity cutoff; no consensus across models | Candidate set rests on literature precedent plus inspection | **[pending]** |
| Conservation/phylogenetic analysis | Further mutation sites are blocked on it | **[pending]** |
| Growth penalty not computed | Cost of each intervention is not quantified | **[pending]** |
| Knockout screen run without early-release reaction | Re-run needed | **[pending]** |
| Two FBA analyses use different conditions | Numbers differ by 6–7% | **[pending]** reconciliation |
| FBA is an upper bound, not a probability | We report no probability of success anywhere | By construction |
| Free myristate modelled, not methyl myristate | Coolant titre not predicted | By construction |
| RL agent is a simple linear Q-learner; benchmark on a synthetic landscape | Shows ours lost, not that RL cannot work | Stated |
| LCA not critically reviewed; placeholders remain | Not for public comparative claims | See Sustainability |

**Validation we can still do without a wet lab (proposed, not yet planned):** reproduce known literature outcomes in the modified model (for example the *Yarrowia* C14 shift, or the *S. cerevisiae* C6/C8 shifts) and report how closely it matches; finish the positive and negative controls for the structural step; report per-residue confidence for the final models.

## Reproducibility {#m8}

Code: <a href="https://github.com/Siddhant-Chowdhary/igem-preflight">github.com/Siddhant-Chowdhary/igem-preflight</a> (MIT). TODO: mirror to iGEM GitLab as required for the Software page.

```
git clone <repository>
cd <repository>
pip install -r requirements.txt
python3 examples/run_feasibility.py     # prints: Wild-type growth: 0.081100 /h ... Verdict: SURVIVES
python3 examples/run_diagnostics.py     # prints: VERDICT: NOT USABLE, *** NO PROPOSALS ISSUED ***
```

Python 3.10 or newer; GLPK ships with COBRApy. The Yeast-GEM model (about 11 MB) is downloaded separately from SysBioChalmers/yeast-GEM. The expected output of the diagnostics script is the demonstration, not a bug. **[pending]** State the exact test counts and the machine each was run on.

## References {#m9}

1. Rigouin C, et al. (2017). Production of medium chain fatty acids by *Yarrowia lipolytica*: combining molecular design and TALEN to engineer the fatty acid synthase. *ACS Synth Biol* 6:1870–1879.
2. Johansson P, et al. (2008). Inhibition of the fungal fatty acid synthase type I multienzyme complex. *PNAS* 105:12803. PDB 2VKZ.
3. Olsen JG, et al. (2001). Structures of β-ketoacyl-ACP synthase I complexed with fatty acids elucidate its catalytic machinery. *Structure* 9(3):233–243.
4. Zhang C, et al. (2024). Yeast9: a consensus genome-scale metabolic model for *S. cerevisiae* curated by the community. *Mol Syst Biol* 20:1134–1150.
5. Orth JD, Thiele I, Palsson BØ (2010). What is flux balance analysis? *Nat Biotechnol* 28:245–248.
6. Ebrahim A, et al. (2013). COBRApy: constraints-based reconstruction and analysis for Python. *BMC Syst Biol* 7:74.
7. Wei Y, Siewers V, Nielsen J (2017). *Appl Microbiol Biotechnol*. doi:10.1007/s00253-017-8126-7.
8. Madeira F, et al. (2022). Search and sequence analysis tools services from EMBL-EBI in 2022. *Nucleic Acids Res* 50:W276–W279.
9. Needleman SB, Wunsch CD (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. *J Mol Biol* 48:443–453.
10. Das I, Dennis JE (1997). Weighted-sum drawbacks for Pareto set generation. doi:10.1007/BF01197559. TODO: add full title.
11. Schuetz R, Kuepfer L, Sauer U (2007). *Mol Syst Biol*. doi:10.1038/msb4100162. TODO: add full title.
12. Lieven C, et al. (2020). memote. *Nat Biotechnol*. doi:10.1038/s41587-020-0446-y.
13. Boltz-2 (Passaro et al. 2025). TODO: confirm full citation. Boltz-1: Wohlwend M, et al. (2024), bioRxiv.
14. Gajewski J, et al. (2017). TODO: full citation of the *S. cerevisiae* FAS engineering paper referred to in our decisions record.
