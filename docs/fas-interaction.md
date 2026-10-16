<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed. **None of the values on this page has been validated against wet-lab data.**
</div>

<figure class="figure my-4 key">
  <img src="/static/figures/explainer_experiment_flow.png" class="figure-img img-fluid" alt="Flow chart of four rounds of Boltz-2 runs, from top to bottom. Round 1, first runs on Google Colab: unconstrained ligand ipTM 0.511, constrained 0.80 to 0.83, an M1251 overlap of 0.96 to 1.77 angstrom reported. Round 2, repeat on laboratory GPUs, 7 runs: baseline placed 3.0 to 4.6 angstrom from C1305, M1251 no closer than 3.3, M1260 at 15 to 17. Round 3, forced contacts on M1251 and M1260, 8 runs: M1260 at 3.9 to 6.5 angstrom, no overlap. Round 4, control batch, 4 runs: repeat identical, plug mutant moved the ligand 1.25 angstrom, V1254W 5.88 against 6.33 angstrom. Arrows between rounds state what was carried forward.">
  <figcaption class="figure-caption"><strong>Figure A.</strong> Sequence of Boltz-2 experiments for the KS domain. Each round was designed from the result of the previous one; the text between rounds states what was carried forward. Rounds 2 to 4 comprised 19 runs (95 models). All values are model outputs <strong>[computed]</strong> and are not validated against wet-lab data. Details of each round follow below.</figcaption>
</figure>

## Step 2. Ligand placement in the ketoacyl synthase domain {#structure}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

A computer model (Boltz-2) was used to predict where myristic acid, the 14-carbon fatty acid, sits in the active region of the yeast fatty acid synthase. The predicted position depended on how the calculation was set up, so it is not treated as a finding about the real enzyme. **[computed]**
</div>

**Question.** Does the ketoacyl synthase (KS) pocket accommodate a C14 acyl chain in silico, and which residues should be excluded from mutagenesis?

**Setup.** Boltz-2[@passaro2025|Boltz-2 used for ligand placement] was applied to the KS domain of *Saccharomyces cerevisiae* fatty acid synthase subunit 2 (ScFAS2; residues 1123–1657, UniProt annotation). Initial runs used Google Colab (T4 GPU) with `--use_msa_server --diffusion_samples 1`. The ligand was myristic acid (SMILES CCCCCCCCCCCCCC(=O)O). **[computed]**

**Ligand placement without distance constraints was setup-dependent.** In the initial run (single sample, no constraints), Boltz-2 positioned myristic acid away from the pocket (baseline ligand ipTM 0.511; interface position error 9.1 Å). In a repeat run on the laboratory server (five samples, fixed alignment), the ligand was placed 3.0–4.6 Å from the catalytic cysteine C1305 without constraints (ligand ipTM 0.80). Failure of Boltz-2 without constraints is therefore not claimed; the outcome depended on the setup. Subsequent runs used explicit distance constraints.

**Constrained runs.** Five models were generated and compared (Table 1). Confidence scores for the earlier C14 runs, taken from the KS-domain report, are given in Table 2.

*Table 1. Models compared. All ligands were modelled in the ScFAS2 KS domain; C16 and C22 serve as chain-length controls.*

| Model | Ligand |
|---|---|
| scfas2_ks3_c14_v2_model_0 | C14 |
| ks3_c14_constrained_model_0 | C14 |
| run_c16_model_0 | C16 (control) |
| run_c22_model_0 | C22 (control) |
| run3_model_0 | C14 |

*Table 2. Boltz-2 confidence scores for the earlier C14 runs (one sample each). Interface position error is given in Å. Model-implied; not validated against wet-lab data.*

| Run | Constraint | Confidence | Ligand ipTM | Interface position error (Å) | Complex ipLDDT |
|---|---|---|---|---|---|
| Baseline | none | 0.835 | 0.511 | 9.124 | 0.649 |
| v2 | max_dist 6.0 Å | 0.906 | 0.831 | 3.124 | 0.667 |
| Run1 (Colab) | none on max_dist | 0.920 | 0.806 | 2.023 | 0.836 |
| Run2 (Colab) | max_dist 6.0 Å | 0.917 | 0.796 | 2.072 | 0.829 |
| Run3 (Colab), selected | max_dist 8.0 Å | 0.919 | 0.812 | 2.031 | 0.831 |

**Structural quality.** The protein-fold RMSD of the constrained C14 model against chain A of the KS3 domain of PDB 8PRW[@singh2023|template structure for the KS3 domain] was 1.39 Å (PyMOL `cealign`). Against *Escherichia coli* β-ketoacyl-ACP synthase I (KAS I; PDB 1F91[@olsen2001|PDB 1F91 identified as E. coli KAS I with a C10 fatty acid]), the RMSD was 2.38 Å over 232 aligned residues, which indicates fold-level agreement between distant homologues. This agreement supports the use of 1F91 as a reference for how an acyl chain occupies a KS tunnel, but not the transfer of ligand coordinates atom by atom. Ligand placement was obtained from Boltz-2 and not from 1F91.

## Residues examined in the acyl tunnel {#structurally-relevant-residues}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Three residues lining the acyl tunnel were checked in every constrained model. One of them, V1254, was kept as the proposed mutation site (V1254W), which is an assumption by homology. M1251 was excluded from mutagenesis. **[computed]**
</div>

All three residues line the acyl tunnel, have an equivalent in *Yarrowia lipolytica* FAS (YlFAS), and were examined in every constrained model (Table 3).

<div class="key" markdown="1">

*Table 3. Closest-atom distance between each residue and the C14 chain in the constrained models. Distances in Å. Model-implied; not validated against wet-lab data.*

| Residue | YlFAS equivalent | Distance to C14 in constrained model | Disposition |
|---|---|---|---|
| M1251 | M1217 | 0.96–1.77 Å in the first runs; 3.1–6.3 Å in the reruns | Excluded from mutagenesis |
| V1254 | I1220 | 4.35 Å in the first runs (superposition: 5.72 Å); 4.0–9.3 Å in the reruns | Retained; V1254W proposed |
| M1260 | M1226 | 6.91 Å in the first runs; 3.9–6.5 Å when forced, 15–17 Å otherwise (reruns) | Retained as secondary candidate |

</div>

The first-run distances were taken from team comments on the constrained run; the rerun distances are closest-atom distances measured across the models of the reruns. The two sets differ because the constraints differ (see the rerun section below). The proximity criterion remains informal.

## Catalytic and mechanistic exclusions {#catalytic-and-mechanistic-exclusions}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Five positions in the enzyme were ruled out as mutation sites because a published structure of the yeast enzyme links them to the catalytic mechanism or to access to the active site. **[literature]**
</div>

**[literature]** The exclusions are based on the cerulenin-inhibited ScFAS structure (PDB 2VKZ)[@johansson2008|roles of C1305, M1251, F1646, G1250 and the K1413–K1423 loop] (Table 4).

<div class="key" markdown="1">

*Table 4. Residues excluded from mutagenesis and the basis for exclusion. Entries marked 'Interpretation' are inferences made in this study, not reported observations.*

| Residue | Reported role | Basis for exclusion |
|---|---|---|
| C1305 | Active-site cysteine that forms a covalent bond with the inhibitor | Nucleophile of the acyl-enzyme thioester; excluded absolutely |
| F1646 | Shields the active site; flips to allow access to the cysteine | Interpretation: gates catalytic accessibility |
| M1251 | Located in the centre of the acyl-binding tunnel; rotates and unlocks the inner part of the tunnel | Interpretation: a conformational gate; mutation would be expected to alter tunnel access rather than volume |
| G1250 | Adjacent to M1251; a glycine-to-serine substitution at this position is discussed in relation to cerulenin resistance | Interpretation: possibly coupled to the movement of M1251 |
| K1413–K1423 loop | Conformation differs between fungal and bacterial enzymes and is proposed to influence inhibitor access | Interpretation: not catalytic, but excluded as a precaution |

</div>

## The reported M1251 clash was not reproduced {#the-m1251-clash-reported-in-the-first-runs-not-reproduced}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The first runs suggested that the fatty-acid chain collides with a residue called M1251. Repeat runs did not show this collision, so the idea remains an untested hypothesis. **[hypothesis]**
</div>

**[hypothesis]** In the first constrained runs, the acyl chain overlapped M1251 at a distance of 0.96–1.77 Å, and the overlap was also present in the raw structural superposition constructed from 8PRW. In the reruns (next section) no model showed the overlap. The superposition is the remaining evidence that a closed gate is incompatible with the chain. Attempted remedies in the first round did not resolve the overlap: OpenBabel UFF minimisation, PyMOL sculpting, and the PyMOL mutagenesis wizard (which ranks pre-enumerated rotamers only and cannot identify an intermediate side-chain geometry).

**Working interpretation.** M1251 is a conformational gate in the cerulenin-bound structure[@johansson2008], which is the basis for excluding it from mutagenesis on mechanistic grounds. Whether a closed gate collides with a C14 chain in the ligand-bound state is not resolved by these data: the superposition suggests that it does, whereas the Boltz-2 reruns do not.

## Reruns on the laboratory GPU server {#reruns-on-the-lab-gpu-server}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The calculation was repeated 15 times on laboratory graphics processors in two rounds, giving 75 predicted structures. The ligand position changed with the constraints chosen, the earlier collision was not seen, and the confidence scores were uniformly high, so they could not separate the setups or chain lengths. **[computed]**
</div>

**[computed]** After the first runs, the experiment was repeated on three RTX A6000 GPUs with one setup throughout: the same 535-residue KS-domain input, Boltz-2 with five samples per run, seed 42, a fixed multiple-sequence alignment, and myristic acid (C14) unless stated. Two constraint designs were compared:

- **C1305 contact (soft cutoff).** One pocket contact on the catalytic cysteine C1305 with a cutoff of 6, 8 or 10 Å, plus an unconstrained baseline, a V1254W variant, and C16 and C22 ligands at 8 Å (7 runs).
- **Forced gate contacts.** Pocket contacts on M1251 and M1260 (and in one run also V1254) with `force: true`, with and without the Boltz steering potentials (8 runs).

In these two rounds, 75 models were generated. The earlier Colab runs used one sample and constraints that were not fully recorded, so they are not directly comparable. Figure A (top of the page) outlines the sequence of experiments and Figure B the two constraint designs. Figure 1 shows the distances obtained, Figure 2 the confidence scores and Figure 3 the comparison across chain lengths. Figure 4 shows one model as an example.

<figure class="figure my-4">
  <img src="/static/figures/explainer_constraint_designs.png" class="figure-img img-fluid" alt="Two panels. Design A, soft contact on C1305 (7 runs): M1251 at 3.1 to 6.3 angstrom and M1260 at 15 to 17 angstrom from the C14 chain, neither constrained. Design B, forced contacts on M1251 and M1260 (8 runs): M1251 at 3.1 to 6.3 angstrom and M1260 at 3.9 to 6.5 angstrom.">
  <figcaption class="figure-caption"><strong>Figure B.</strong> Two constraint designs on the same KS-domain input. With a soft contact on C1305 (7 runs) the C14 chain lay 15–17 Å from M1260; with forced contacts on M1251 and M1260 (8 runs) it lay 3.9–6.5 Å. M1251 stayed 3.1–6.3 Å away in both, no clash was seen, and confidence (0.90–0.94) did not separate the designs. Schematic of constraints and measured distances, not of geometry. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

<figure class="figure my-4 key">
  <img src="/static/figures/boltz_distance_spread.png" class="figure-img img-fluid" alt="Dot plot of the distance from C14 to M1251, V1254 and M1260 for four Boltz-2 setups, five models each. Distance to M1251 stays between about 3 and 6 angstrom in every setup, above a shaded band at 0.96 to 1.77 angstrom. Distance to M1260 is about 15 angstrom without forced contacts and about 4 to 6 angstrom when M1260 is forced.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> Closest-atom distance from C14 to three residues in five Boltz-2 models of each setup (dot, model; bar, median). The shaded band marks the 0.96–1.77 Å range reported for an M1251 clash in the first runs; no model of the reruns approaches it. The position of the chain depended on which residues were forced as contacts. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

Three observations were made, with their limits:

- **The constraint design altered the pose.** The distance to M1260 was 15–17 Å when only C1305 was constrained and 3.9–6.5 Å when M1260 was forced. Any statement of the form "C14 lies X Å from residue Y" therefore describes the setup as well as the pocket.
- **No clash with M1251 was observed in the reruns.** M1251 remained 3.1–6.3 Å from the ligand in every model, and no ligand atom came closer than 2.4 Å to any protein atom, with or without steering potentials. The 0.96–1.77 Å values of the first runs were not reproduced, and the cause is unknown (software version, sample count, constraints and the distance measurement are candidate explanations that were not tested).
- **Confidence did not discriminate between setups.** Overall confidence was 0.90–0.94 and ligand ipTM 0.74–0.88 for every run, including the unconstrained baseline.

<figure class="figure my-4">
  <img src="/static/figures/boltz_confidence.png" class="figure-img img-fluid" alt="Dot plots of overall confidence (about 0.90 to 0.94) and ligand ipTM (about 0.75 to 0.90) for ten Boltz-2 runs; all runs overlap heavily.">
  <figcaption class="figure-caption"><strong>Figure 2.</strong> Overall confidence and ligand ipTM for ten of the reruns (five models each). Confidence remained high in every setup, including without constraints, and therefore did not distinguish setups or ligands. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

<figure class="figure my-4">
  <img src="/static/figures/boltz_chain_length.png" class="figure-img img-fluid" alt="Two panels of distance from C14, C16 and C22 to M1251, V1254 and M1260. In both constraint designs the three ligands reach the same residues at similar distances.">
  <figcaption class="figure-caption"><strong>Figure 3.</strong> Closest-atom distances for C14, C16 and C22 under the two constraint designs (five models per run). All three ligands reached the same residues, so this KS-only setup did not discriminate by chain length. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

## Control batch: repeatability, pocket mutation and decoy ligand {#control-batch}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Four further runs tested whether the model gave repeatable results and whether it responded to a change in the pocket. A repeated run was identical to the original, substitutions in the pocket moved the ligand little, and a decoy ligand was not clearly separated from myristic acid by the confidence scores. **[computed]**
</div>

**[computed]** A fourth round of four runs (20 models) was performed under the settings of the second round (soft contact on C1305 at 8 Å, five samples, seed 42) with the binding-probability output of Boltz-2 enabled (Table 5). The runs were: a repeat of the wild-type C14 run (repeatability); a variant carrying four tryptophan substitutions in the pocket (M1251W, A1304W, A1348W and A1548W; sensitivity to pocket mutation); caffeine in place of myristic acid (decoy ligand); and V1254W. Expected outcomes and thresholds were recorded and hashed before the runs; the thresholds were provisional, and the results are therefore reported as measurements and not as pass or fail verdicts.

<div class="key" markdown="1">

*Table 5. Control batch (medians of five models per run). Distances are closest-atom distances in Å. Displacement is the distance between ligand centroids after superposition of the protein on the stored wild-type model. The binding probability is the binary output of the Boltz-2 affinity module (one value per run). Model-implied; not validated against wet-lab data.*

| Run | Ligand ipTM | M1251 | V1254 | M1260 | C1305 | Displacement (Å) | Binding probability |
|---|---|---|---|---|---|---|---|
| Wild type, C14 (repeat) | 0.861 | 3.53 | 6.33 | 15.46 | 3.16 | 1.32 | 0.270 |
| Plug mutant, C14 | 0.870 | 3.30 | 6.79 | 15.18 | 3.55 | 1.25 | 0.297 |
| V1254W, C14 | 0.847 | 4.15 | 5.88 | 15.99 | 3.00 | 2.30 | 0.290 |
| Wild type, caffeine | 0.894 | 9.14 | 14.01 | 21.96 | 3.19 | 4.05 | 0.211 |

</div>

Four observations were made:

- **The repeat was identical.** For all five matched models, the ligand RMSD to the stored wild-type model was 0.00 Å and all distances were unchanged, so the stored numbers are a valid baseline for this setup.
- **The plug mutant moved the ligand little.** The ligand centroid was displaced by 1.25 Å (ligand RMSD 2.00 Å) and the ligand ipTM did not decrease (0.870 against 0.861). For comparison, the five wild-type models differed from the first model by a median ligand RMSD of 2.55 Å, so the spread within one run was larger than the effect of the four substitutions.
- **V1254W changed the median distance by 0.45 Å.** The median distance to residue 1254 was 5.88 Å against 6.33 Å for wild type. Three of the five V1254W models placed the ligand 4.1–5.9 Å from residue 1254; two placed it about 10 Å from M1251 and V1254, in a different location, so the median does not describe a typical model.
- **The decoy was not clearly separated.** The five caffeine models lay 9, 14 and 22 Å from M1251, V1254 and M1260 while remaining 3.2 Å from C1305 (the restrained contact). The binding probability was 0.211 against 0.270 for C14, and the ligand ipTM was higher for caffeine (0.894) than for C14 (0.861), so the confidence scores did not distinguish the decoy.

Under this setup Boltz-2 therefore showed little response to the substitutions tested, and differences of about 1 Å between wild-type and mutant models are not interpreted. The V1254W result is reported as a description of the models and does not support or refute the proposed effect of the substitution. The low response may reflect the contact restraint on C1305 or the unchanged alignment as well as the model itself; these factors were not separated. The binding-probability values are Boltz-2 scores and not binding constants.

## Chain-length controls {#controls}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Longer and shorter fatty acids were modelled as controls. If the pocket preferred one chain length, they should have behaved differently; they did not, so these runs do not show that the pocket distinguishes chain length. **[computed]**
</div>

C16 and C22 runs were included as controls: if the pocket discriminated on chain length, the ligands would be expected to behave differently within it. A preliminary team comparison reported C14 at about 6 Å from the two target residues, whereas the C16 distances were non-uniform (about 5 Å and 8 Å). In the reruns, C14, C16 and C22 reached the same residues at similar distances (Figure 3), so these controls do not show chain-length discrimination in a KS-only setup. The unconstrained baseline also located the pocket and therefore does not serve as a negative control; a decoy ligand (caffeine), a repeat of the wild-type run and a pocket-plug variant were used instead (previous section).

## Limitations of this step {#limits-of-this-step}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The results rest on one random seed per condition, on constraints that influence the pose, and on model-derived scores, so they indicate plausible geometry only. **[computed]**
</div>

- No formal proximity criterion was defined. The cutoff was varied (6, 8 and 10 Å) and the spread across five models is reported, but no threshold was adopted.
- Five samples drawn with one seed are not independent replicates. The spread across the five models describes the variability of the sampling, not run-to-run variability.
- The pose depended on the constraint design (Figure B); distances measured to residues that were themselves constrained partly reflect the constraint.
- Free myristic acid was modelled in place of the covalent acyl-enzyme intermediate (assumption A3 on the model overview).
- The binding-probability and affinity outputs of Boltz-2 are model-derived scores, not binding constants.

<figure class="figure my-4">
  <img src="/static/figures/boltz_pocket_c14.png" class="figure-img img-fluid" alt="Cartoon of the KS pocket with C14 in blue sticks. M1251 (orange), V1254 (red) and M1260 (green) are drawn as sticks with dashed distance lines of 4.3, 8.9 and 4.6 angstrom.">
  <figcaption class="figure-caption"><strong>Figure 4.</strong> C14 (blue) in the highest-confidence model of the run that forced M1251 and M1260 as contacts. Closest-atom distances: M1251 (orange), 4.3 Å; V1254 (red), 8.9 Å; M1260 (green), 4.6 Å; neighbouring residues in grey. One model of five is shown; the others differ. Boltz-2 prediction, not an experimental structure.</figcaption>
</figure>

## Reproducing the Boltz-2 runs {#reproducing-the-boltz-2-runs}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The software, inputs, commands and measurements needed to repeat the runs and recompute the reported distances and scores are listed here. **[computed]**
</div>

**Software and hardware.** Rounds 2 to 4 were run with Boltz-2[@passaro2025] (Python package `boltz` 2.2.1 with the Boltz-2 weights) on Linux with NVIDIA RTX A6000 GPUs (48 GB), one GPU per run. Round 1 used Google Colab with a T4 GPU. A run with five samples took about 7 min on an idle GPU and 13–15 min on a heavily shared one. The output of one run (structures and confidence files) occupied about 13 MB.

**Input.** The protein was residues 1123–1657 of *S. cerevisiae* FAS2 (UniProt P19097; 535 residues). Residue indices in the inputs are local: UniProt number minus 1122, so that M1251, V1254, M1260 and C1305 are residues 129, 132, 138 and 183. The ligand was given as a SMILES string (myristic acid, `CCCCCCCCCCCCCC(=O)O`; C16 and C22 by extending the chain; caffeine for the decoy). Variants were made by substituting the residue in the input sequence: V1254W at residue 132, and the plug mutant at residues 129, 182, 226 and 426 (M1251W, A1304W, A1348W, A1548W). The constraint designs were a soft contact on C1305 (`contacts: [[A, 183]]`, `max_distance: 8.0`; 6 or 10 in the sweep) and forced contacts on M1251 and M1260 (`contacts: [[A, 129], [A, 138]]`, with residue 132 added in one run, and `force: true`). The binding-probability output was requested with a `properties` block.

```yaml
version: 1
sequences:
  - protein:
      id: A
      sequence: <535-residue KS-domain sequence, P19097 residues 1123-1657>
      msa: <path to the alignment file>   # omitted when the public alignment server is used
  - ligand:
      id: B
      smiles: 'CCCCCCCCCCCCCC(=O)O'
constraints:
  - pocket:
      binder: B
      contacts: [[A, 183]]
      max_distance: 8.0            # forced design: contacts [[A, 129], [A, 138]] and force: true
properties:
  - affinity:
      binder: B
```

**Alignments.** Round 2 used the public alignment server of Boltz (`--use_msa_server`). Rounds 3 and 4 read a fixed alignment file (`msa:` field) generated for the wild-type sequence in round 2. For variants, the first row of that file must be the variant sequence: in the installed version, an alignment whose first row differed from the input sequence was replaced by a single-sequence placeholder.

**Command.**

```bash
boltz predict inputs/<run>.yaml --cache <cache_dir> --out_dir runs/<run> \
  --accelerator gpu --devices 1 --diffusion_samples 5 --recycling_steps 3 \
  --sampling_steps 200 --use_potentials --output_format mmcif --seed 42 --override
```

Round 2 additionally used `--use_msa_server`; the comparison without steering potentials in round 3 omitted `--use_potentials`.

**Measurements.** For each of the five models of a run, the closest heavy-atom distance between the ligand and each residue of interest (local residues 129, 132, 138 and 183) and the closest ligand–protein atom pair were computed from the structure file. Overall confidence (`confidence_score`), ligand ipTM (`ligand_iptm`) and complex ipLDDT (`complex_iplddt`) were read from the `confidence_*.json` files. Ligand displacement was the distance between the centroids of the ligand heavy atoms after superposing the protein Cα atoms on the reference model. Medians over the five models are reported unless stated.

**Expected agreement.** With the same seed, alignment, settings and software on the same server, a rerun reproduced the stored wild-type models exactly (matched-model ligand RMSD 0.00 Å).

---

**Previous:** [Step 1 Sequence](sequence) · **Next:** [Step 3 Bridge](bridge)
