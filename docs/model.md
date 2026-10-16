
<div class="alert alert-warning" role="alert" markdown="1">
**Read this first.** Every number on the model pages describes a model. **None is validated against wet-lab data.** Labels: **[computed]** our own run; **[literature]** published source; **[hypothesis]** reasoned, untested; **[pending]** not finished.
</div>

## At a glance {#m0}

- We worked in six steps, each handing one result to the next: sequence → FAS interaction → bridge → metabolism → trust → process (figure on the [home page](./)).
- **Central assumption:** a point mutation in *S. cerevisiae* FAS2 (V1254W, by analogy with *Yarrowia* I1220W) can release C14 early. This is **[hypothesis]**, not established.
- **Main findings:** the model makes C14:0 only by shortening C16:0 through beta-oxidation; no knockout beats wild type; an early-release reaction adds only +2.6% and is limited by NADPH; our own scoring setup failed its checks.
- **Where to jump:** [Data](#m3) · [Assumptions](#m4) · [1 Sequence](sequence) · [2 FAS interaction](fas-interaction) · [3 Bridge](bridge) · [4 Metabolism](metabolism) · [5 Trust](trust) · [6 Process](process) · [Effect on design](#m6) · [Limits](#m7) · [Reproducibility](#m8) · [References](#m9). Also under Model: [Engineering](engineering), [Results](results), [Life Cycle Assessment](life-cycle-assessment).

## Approach and what it tells us {#m1}

| Step | Question | Method | What it provides |
|---|---|---|---|
| [1 Sequence](sequence) | Which ScFAS2 residue corresponds to the *Yarrowia* chain-length residue? | EMBOSS Needle global alignment | A candidate site (V1254W) |
| [2 FAS interaction](fas-interaction) | Does the KS pocket accommodate a C14 chain; what must not be mutated? | Boltz-2 on the KS domain with distance constraints; structural comparison | A residue shortlist and an exclusion list |
| [3 Bridge](bridge) | Can a metabolic model represent the mutation? | Add an early-release reaction to Yeast9 | A model that can simulate the intervention |
| [4 Metabolism](metabolism) | What can the cell reach, at what growth cost? | Flux balance analysis (FBA) on Yeast9, COBRApy | Feasibility frontier, route, knockout screen |
| [5 Trust](trust) | Does "best" mean anything? Is learned search needed? | Six checks on the scoring function; brute force vs greedy vs RL | Which rankings may be believed |
| [6 Process](process) | Is the product worth making? | CFD of an immersion tank; screening LCA | Use-phase and production footprint |

**Why these methods.** FBA needs no kinetic parameters, so it can run on a genome-scale model; it gives an upper limit, not a prediction. Boltz-2 was used because the KS pocket of the solved ScFAS2 structure (8PRW) holds no fatty acid, so ligand placement had to be predicted. Brute force was kept as the reference search because at our scale it is exact and cheap. Existing strain-design tools (OptKnock, OptGene, OptForce, RobustKnock, cameo, MEWpy, OptFlux, StrainDesign) return designs whether or not the scoring underneath them can separate candidates; none of those we surveyed checks first.

## Data and parameters {#m3}


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
**[pending]** Reconcile the two analyses: confirm the exact model version in each (a team comment names v9.0.2 for one run), and the reason for the growth-rate difference. Glucose uptake differs (1.0 vs 1.1), which probably explains most of it.
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
| A4 | Distance constraints are needed to place the ligand | The first unconstrained run did not place the chain near the pocket, but a rerun with five samples did | Constraint choice biases the pose | **[computed]** |
| A5 | FBA: steady state, no kinetics, no regulation | Standard FBA assumptions | Results are upper limits, not predictions | **[literature]** |
| A6 | Fatty-acid-CoA ligases forward-only in the primary scenario | The reaction is ATP-driven and strongly one-way; reversal gave a thermodynamically questionable route | Some knockouts look viable only via reverse flux | **[computed]** (sensitivity shown) |
| A7 | Myristate export is a reaction without a gene | How Yeast9 represents it | Secretion mechanism is not established | **[literature]** model property |
| A8 | The model outputs free myristate, not methyl myristate | Esterification is not in the model | Titre of the coolant is not predicted | By construction |
| A9 | Assay resolution is GC-MS replicate noise of 1–5% | Project write-up | Thresholds for "separable" shift | Not checked against literature |
| A10 | Search benchmark runs on a synthetic landscape | Our real landscape turned out to be flat, so comparing searches on it measures nothing | Ranking may not transfer | **[computed]** |
| A11 | Tank CFD uses constant fluid properties | Simplification | Temperature-dependent viscosity is missed | See [Life Cycle Assessment](life-cycle-assessment) |

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
| LCA not critically reviewed; placeholders remain | Not for public comparative claims | See Life Cycle Assessment |

**Validation we can still do without a wet lab (proposed, not yet planned):** reproduce known literature outcomes in the modified model (for example the *Yarrowia* C14 shift, or the *S. cerevisiae* C6/C8 shifts) and report how closely it matches; finish the positive and negative controls for the structural step; report per-residue confidence for the final models.

## Reproducibility {#m8}

Code: <a href="https://github.com/Siddhant-Chowdhary/igem-preflight">github.com/Siddhant-Chowdhary/igem-preflight</a> (MIT).

```
git clone <repository>
cd <repository>
pip install -r requirements.txt
python3 examples/run_feasibility.py     # prints: Wild-type growth: 0.081100 /h ... Verdict: SURVIVES
python3 examples/run_diagnostics.py     # prints: VERDICT: NOT USABLE, *** NO PROPOSALS ISSUED ***
```

Python 3.10 or newer; GLPK ships with COBRApy. The Yeast-GEM model (about 11 MB) is downloaded separately from SysBioChalmers/yeast-GEM. The expected output of the diagnostics script is the demonstration, not a bug.

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
10. Das I, Dennis JE (1997). Weighted-sum drawbacks for Pareto set generation. doi:10.1007/BF01197559.
11. Schuetz R, Kuepfer L, Sauer U (2007). *Mol Syst Biol*. doi:10.1038/msb4100162.
12. Lieven C, et al. (2020). memote. *Nat Biotechnol*. doi:10.1038/s41587-020-0446-y.
13. Boltz-2 (Passaro et al. 2025). Boltz-1: Wohlwend M, et al. (2024), bioRxiv.
14. Gajewski J, et al. (2017). *S. cerevisiae* fatty acid synthase engineering (full citation to be added).
