
<div class="alert alert-warning" role="alert" markdown="1">
**Read this first.** Every number on the model pages describes a model. **None has been validated against wet-lab data.** Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed.
</div>

## Overview of the modelling chain {#m0}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The project asks whether baker's yeast could be engineered to make myristic acid, a 14-carbon fatty acid, for use in a bio-based data-centre coolant. Six linked computer models were built, none tested in the laboratory. The central assumption, that a single mutation (V1254W) releases this fatty acid early, is a hypothesis. **[hypothesis]**
</div>

- The work was organised in six steps, each passing one result to the next: sequence → fatty acid synthase (FAS) interaction → bridge → metabolism → trust → process (figure on the [home page](./)).
- **Central assumption:** a point mutation in *Saccharomyces cerevisiae* FAS2 (V1254W, by analogy with *Yarrowia lipolytica* I1220W) can release C14 early. This is a **[hypothesis]** and has not been established.
- **Main findings:** the model forms C14:0 only through peroxisomal β-oxidation, mainly by shortening C16:0; no knockout set exceeded wild type, which follows largely from the method, since a deletion can only remove flux; an early-release reaction increased C14 export by only 2.6 % and is limited by NADPH; the team's scoring setup did not satisfy its own checks.
- **Navigation:** [Data](#m3) · [Assumptions](#m4) · [1 Sequence](sequence) · [2 FAS interaction](fas-interaction) · [3 Bridge](bridge) · [4 Metabolism](metabolism) · [5 Trust](trust) · [6 Process](process) · [Effect on design](#m6) · [Limits](#m7) · [Reproducibility](#m8) · [References](#references). Further pages under Model: [Engineering](engineering), [Results](results), [Life Cycle Assessment](life-cycle-assessment).

## Approach and outputs of each step {#m1}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Each step answers one question with one method: a sequence comparison, a protein-ligand prediction, a metabolic-model extension, a flux calculation, checks on the ranking, and heat-flow and life cycle assessments. Flux balance analysis gives upper limits, not predictions. **[computed]**
</div>

<div class="key" markdown="1">

*Table 1. Steps of the modelling chain, the question addressed, the method and the output of each.*

| Step | Question | Method | Output |
|---|---|---|---|
| [1 Sequence](sequence) | Which ScFAS2 residue corresponds to the *Yarrowia* chain-length residue? | EMBOSS Needle global alignment | A candidate site (V1254W) |
| [2 FAS interaction](fas-interaction) | Does the ketoacyl synthase (KS) pocket accommodate a C14 chain; which residues must not be mutated? | Boltz-2 on the KS domain with distance constraints; structural comparison | A residue shortlist and an exclusion list |
| [3 Bridge](bridge) | Can a metabolic model represent the mutation? | Addition of an early-release reaction to Yeast9 | A model that can simulate the intervention |
| [4 Metabolism](metabolism) | What can the cell reach, and at what growth cost? | Flux balance analysis (FBA) on Yeast9, COBRApy | Feasibility frontier, route, knockout screen |
| [5 Trust](trust) | Does the top-ranked design differ from the unedited strain? Is learned search required? | Six checks on the scoring function; brute force, greedy and reinforcement-learning search | Rankings that may be relied on |
| [6 Process](process) | Is the product suitable for its intended use? | Computational fluid dynamics (CFD) of an immersion tank; screening life cycle assessment (LCA) | Use-phase and production footprint |

</div>

**Rationale for the methods.** FBA[@orth2010|principles and assumptions of FBA] requires no kinetic parameters and can therefore be applied to a genome-scale model; it yields an upper limit and not a prediction. Boltz-2[@passaro2025|ligand placement] was used because the KS pocket of the solved ScFAS2 structure (PDB 8PRW)[@singh2023|8PRW] contains no fatty acid, so ligand placement had to be predicted. Brute force was retained as the reference search because it is exact and inexpensive at the present scale. Existing strain-design tools, namely OptKnock,[@burgard2003] OptGene,[@patil2005] OptForce,[@ranganathan2010] RobustKnock,[@tepper2010] cameo,[@cardoso2018] MEWpy,[@pereira2021] OptFlux[@rocha2010] and StrainDesign,[@schneider2022] return designs whether or not the underlying scoring can separate candidates; none of those surveyed by the team checks this first.

## Data and parameters {#m3}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Protein structures come from public databases, and the metabolic model is the community yeast model Yeast-GEM v9.1.1. The strain, medium and solver settings of the flux analysis are stated in full, together with the medium assumption that sets the growth baseline. **[computed]**
</div>

### Structures **[literature]**

The structures used are listed in Table 2.

*Table 2. Protein structures used. Resolution in Å.*

| PDB | Contents | Resolution | Role |
|---|---|---|---|
| 8PRW | ScFAS2 | 1.9 Å | Primary receptor structure; the KS3 pocket contains no fatty acid |
| 1F91 | *E. coli* β-ketoacyl-ACP synthase I (KAS I) with capric acid | 2.40 Å | Reference for an acyl chain in a KS pocket |
| 2PFF | Yeast FAS | 4.00 Å | Retained as a homology template; not used in the final workflow |
| 2VKZ | Cerulenin-inhibited ScFAS | n/a | Reference for the catalytic state[@johansson2008|PDB 2VKZ] |

Residue numbering follows UniProt P19097 (FAS2, α subunit) and P07149 (FAS1, β subunit). KS-only models use a local offset of 1122; three model files carry an inserted `UNK` residue at local position 84 (a shift of +1 downstream). All residue identifiers on this site are converted to full-sequence P19097 numbering.

### Metabolic model and run conditions **[computed]**

Two FBA analyses exist. They use different conditions, so their numbers differ by design; the conditions are stated with every number (Table 3). Both used GLPK as solver.

<div class="key" markdown="1">

*Table 3. Conditions of the FBA analysis.*

| | |
|---|---|
| Model | Yeast-GEM v9.1.1: 4,105 reactions, 2,748 metabolites, 1,143 genes |
| Strain | BY4742 (HIS3, LEU2, LYS2 deleted, URA3 retained; His, Leu, Lys supplied) |
| Glucose uptake | 1.1 mmol gDW⁻¹ h⁻¹ |
| Oxygen | unlimited |
| Non-growth-associated maintenance (NGAM) | 0.7 mmol ATP gDW⁻¹ h⁻¹ |
| Supplements | His, Leu and Lys uptake capped at the model's own biomass requirement — a stated assumption, not a measurement |
| Fatty-acid-CoA ligases | Forward-only (primary scenario); bounds as shipped (sensitivity) |
| Maximum growth | 0.09768 h⁻¹ (primary), 0.09769 h⁻¹ (shipped bounds) |
| Solver | GLPK |

</div>

<div class="alert alert-secondary" role="alert" markdown="1">
The supplement cap sets the baseline: uncapping it lets the model catabolise leucine as a carbon source and raises maximum growth to 0.159 h⁻¹. The separate pre-flight tool ([Software](software)) runs a prototrophic wild type at a glucose uptake of 1.0 mmol gDW⁻¹ h⁻¹ and reports 0.0811 h⁻¹; that figure belongs to its own conditions and is not this baseline.
</div>

### Literature inputs **[literature]**

- Chain-length control by the KS domain and the *Yarrowia* I1220W result: Rigouin et al. (2017), in which C14 reached 11.6 % of total fatty acids.[@rigouin2017|I1220W result (abstract only)]
- Catalytic and gating residues of ScFAS: Johansson et al. (2008), PDB 2VKZ.[@johansson2008|catalytic and gating residues]
- Background fatty-acid profile of *S. cerevisiae* (CEN.PK113-7D, nitrogen-limited medium, harvested after 120 h; per cent of total fatty acids, n = 2): C16:0 13.7, C16:1 50.0, C18:0 3.5, C18:1 30.0.[@wei2017|Table 3]
- Assay noise: replicate variation of GC-MS fatty-acid composition of 1–5 %, taken from the project write-up and not yet checked against the literature.

## Assumptions and their basis {#m4}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Eleven assumptions underlie the results. The most important, A1, is that the mutation works in baker's yeast as it does in *Yarrowia*; if it does not, every downstream number is moot. Published work found by the team reports shorter chains (C6 and C8) instead. **[hypothesis]**
</div>

<div class="key" markdown="1">

*Table 4. Assumptions, their basis, consequence if incorrect, and status.*

| # | Assumption | Basis | If incorrect | Status |
|---|---|---|---|---|
| A1 | A FAS2 point mutation (V1254W) can release C14 in *S. cerevisiae* | Homology to *Yarrowia* I1220W. The *S. cerevisiae* FAS point-mutation literature found by the team reports C6/C8 shifts[@gajewski2017|S. cerevisiae FAS mutants with C6/C8 shifts] and not C14 | Every downstream number is moot | **[hypothesis]** |
| A2 | Only the KS domain needs to be modelled | The full α subunit (1,887 aa) exceeded GPU memory; the acyl tunnel and residues of interest lie within KS | β-subunit and chamber context are ignored | Reviewed by the team; not tested |
| A3 | Free myristic acid stands in for the covalent acyl-enzyme intermediate | A structure of *E. coli* KAS I with covalently bound C10 and C12 acyl groups (catalytic Cys-Ser mutant) provides a reference for acyl-chain occupancy of a KS pocket[@olsen2001|acyl-bound KAS I structures] | Geometry differs near the catalytic cysteine | **[literature]** precedent (partial) |
| A4 | Distance constraints are needed to place the ligand | The first unconstrained run did not place the chain near the pocket, but a rerun with five samples did | Constraint choice biases the pose | **[computed]** |
| A5 | FBA: steady state, no kinetics, no regulation | Standard FBA assumptions[@orth2010] | Results are upper limits, not predictions | **[literature]** |
| A6 | Fatty-acid-CoA ligases are forward-only in the primary scenario | The reaction is ATP-driven and strongly unidirectional; reversal gave a thermodynamically questionable route | Some knockouts appear viable only through reverse flux | **[computed]** (sensitivity shown) |
| A7 | Myristate export is a reaction without a gene | Representation in Yeast9 | The secretion mechanism is not established | **[literature]** model property |
| A8 | The model outputs free myristate, not methyl myristate | Esterification is not in the model | Titre of the coolant is not predicted | By construction |
| A9 | Assay resolution equals GC-MS replicate noise of 1–5 % | Project write-up | Thresholds for separability shift | Not checked against the literature |
| A10 | The search benchmark runs on a synthetic landscape | The real landscape was flat, so a comparison of searches on it would measure nothing | The ranking of methods may not transfer | **[computed]** |
| A11 | Tank CFD uses constant fluid properties | Simplification | Temperature-dependent viscosity is not captured | See [Life Cycle Assessment](life-cycle-assessment) |

</div>

## Effect of the results on the design {#m6}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The models changed the plan in six ways. A plan to reduce fat breakdown was dropped, some residues were ruled out, and no ranked list of gene deletions was sent to the laboratory. Choosing between two candidate coolants is still open. **[computed]**
</div>

1. **The plan to knock down degradation in order to preserve C14:0 was dropped.** The model indicates that degradation is the only C14:0 source in the absence of early release, and deletion of *POX1* gave zero. The rule against sending degradation knockdowns to the wet lab in a first iteration therefore has a mechanistic basis.
2. **An FAS early-release reaction was added as a documented model modification**, and its effect was measured: +2.6 %, NADPH-limited. This indicates where the model places the limit (cofactors, not chain supply). Acting on this result is **[pending]**.
3. **M1251, C1305, F1646, G1250 and K1413–K1423 were excluded from mutagenesis**; V1254W was retained as the lead candidate, with M1260 secondary.
4. **No ranked knockout list was passed to the wet lab**, because checks D1 and D2 failed on the team's own scoring. The tool withheld proposals, and this outcome was accepted.
5. **Brute-force enumeration is recommended** at the present scale, together with a trivial baseline before any learned search.
6. **The choice of coolant** between methyl and isopropyl myristate is **[pending]**; it does not alter the upstream strain-design question, since both are esters of the same C14 acid.

## Limitations and validation status {#m7}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

There are no laboratory data of any kind, so every number is a statement about a model. Several analyses are unfinished, and the life cycle assessment has not had an independent review. **[pending]**
</div>

<div class="key" markdown="1">

*Table 5. Limitations, their effect on the conclusions and their status.*

| Limitation | Effect on conclusions | Status |
|---|---|---|
| No wet-lab data of any kind | Every number is a statement about a model | Not available to the team |
| The V1254W route to C14 in *S. cerevisiae* is an assumption | All downstream numbers are conditional | **[hypothesis]** |
| The M1251 gate explanation is untested | The basis for excluding M1251 is a hypothesis; *S. cerevisiae* strains with G1250S and M1251W substitutions have been reported[@gajewski2017|G1250S-M1251W strain] and may bear on it | **[pending]** assessment against the paper |
| No molecular dynamics or relaxed ligand-bound pocket | Pocket geometry is rigid-receptor | Large-scale; a short minimisation is feasible |
| No formal proximity cut-off; no consensus across models | The candidate set rests on literature precedent plus inspection | **[pending]** |
| Conservation and phylogenetic analysis | Further mutation sites are blocked on it | **[pending]** |
| Growth penalty computed for the 37 curated interventions only | The cost of the genome-wide candidates is not quantified | **[pending]** in part |
| Knockout screen run without the early-release reaction | Repetition required | **[pending]** |
| The two runs use different conditions | Numbers differ by 6–7 %, accounted for by glucose uptake and supplements | Reconciled |
| 202 internal reactions fail the model's mass-balance check | An illustrative, assumption-dependent shift of about 3.4 % in export at non-zero growth; direction unresolved | Reported, not resolved |
| FBA yields an upper bound, not a probability | No probability of success is reported anywhere | By construction |
| Free myristate modelled, not methyl myristate | Coolant titre is not predicted | By construction |
| The RL agent is a simple linear Q-learner; benchmark on a synthetic landscape | Shows that this agent was outperformed, not that RL cannot work | Stated |
| LCA not critically reviewed; placeholders remain | Not for public comparative claims | See Life Cycle Assessment |

</div>

**Validation that does not require a wet lab (proposed, not yet planned):** reproduction of known literature outcomes in the modified model (for example the *Yarrowia* C14 shift or the *S. cerevisiae* C6/C8 shifts) with a report of the agreement; completion of positive and negative controls for the structural step; and reporting of per-residue confidence for the final models.

## Reproducibility {#m8}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The checking tool is open source (MIT licence) and two example scripts reproduce its main outputs. The expected output of the diagnostics script is a refusal to issue proposals, which is the demonstration and not a fault. **[computed]**
</div>

Flux balance analysis code, result files and figures: <a href="https://github.com/biprabhanu/yeast-genome-scale-fba-metabolic-modeling">github.com/biprabhanu/yeast-genome-scale-fba-metabolic-modeling</a>. Each analysis is a module run from the project root, and the figures on the [Metabolism](metabolism) page are the ones that repository generates from its own result files.

Pre-flight checking tool: <a href="https://github.com/Siddhant-Chowdhary/igem-preflight">github.com/Siddhant-Chowdhary/igem-preflight</a> (MIT licence).

```
git clone <repository>
cd <repository>
pip install -r requirements.txt
python3 examples/run_feasibility.py     # prints: Wild-type growth: 0.081100 /h ... Verdict: SURVIVES
python3 examples/run_diagnostics.py     # prints: VERDICT: NOT USABLE, *** NO PROPOSALS ISSUED ***
```

Python 3.10 or newer is required; GLPK is supplied with COBRApy.[@ebrahim2013|COBRApy] The Yeast-GEM model (about 11 MB) is downloaded separately from SysBioChalmers/yeast-GEM.[@zhang2024|Yeast9] The expected output of the diagnostics script is the demonstration and not a defect.
