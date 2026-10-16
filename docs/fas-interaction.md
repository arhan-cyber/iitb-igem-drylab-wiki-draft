<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed. **None of the values on this page has been validated against wet-lab data.**
</div>

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

<div class="alert alert-secondary" role="alert" markdown="1">
**[pending]** The confidence values in Table 2 originate from the first constrained runs. Per-residue confidence for the final three-residue constrained models has not been extracted, and the pairwise comparison of all five models (backbone and ligand RMSD) has not been computed.
</div>

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

**Working interpretation.** M1251 is a conformational gate in the cerulenin-bound structure[@johansson2008], which is the basis for excluding it from mutagenesis on mechanistic grounds. Whether a closed gate collides with a C14 chain in the ligand-bound state was not tested: the superposition suggests that it does, whereas the Boltz-2 reruns do not. Molecular dynamics (GROMACS or Amber) would test the interpretation; it has not been run.

## Reruns on the laboratory GPU server {#reruns-on-the-lab-gpu-server}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The calculation was repeated 15 times on laboratory graphics processors, giving 75 predicted structures. The ligand position changed with the constraints chosen, the earlier collision was not seen, and the confidence scores were uniformly high, so they could not separate the setups or chain lengths. **[computed]**
</div>

**[computed]** After the first runs, the experiment was repeated on three RTX A6000 GPUs with one setup throughout: the same 535-residue KS-domain input, Boltz-2 with five samples per run, seed 42, a fixed multiple-sequence alignment, and myristic acid (C14) unless stated. Two constraint designs were compared:

- **C1305 contact (soft cutoff).** One pocket contact on the catalytic cysteine C1305 with a cutoff of 6, 8 or 10 Å, plus an unconstrained baseline, a V1254W variant, and C16 and C22 ligands at 8 Å (7 runs).
- **Forced gate contacts.** Pocket contacts on M1251 and M1260 (and in one run also V1254) with `force: true`, with and without the Boltz steering potentials (8 runs).

In total, 75 models were generated. The earlier Colab runs used one sample and constraints that were not fully recorded, so they are not directly comparable. Figure 1 shows the distances obtained, Figure 2 the confidence scores and Figure 3 the comparison across chain lengths. Figure 4 shows one model as an example.

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

## Chain-length controls {#controls}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Longer and shorter fatty acids were modelled as controls. If the pocket preferred one chain length, they should have behaved differently; they did not, so these runs do not show that the pocket distinguishes chain length. **[computed]**
</div>

C16 and C22 runs were included as controls: if the pocket discriminated on chain length, the ligands would be expected to behave differently within it. A preliminary team comparison reported C14 at about 6 Å from the two target residues, whereas the C16 distances were non-uniform (about 5 Å and 8 Å). In the reruns, C14, C16 and C22 reached the same residues at similar distances (Figure 3), so these controls do not show chain-length discrimination in a KS-only setup. A formal positive control (a system known to bind) is lacking, and the unconstrained baseline is not a clean negative control because it also located the pocket.

## Limitations of this step {#limits-of-this-step}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

No agreed distance threshold, per-residue confidence, consensus rule or relaxed ligand-bound structure exists for this step, so the results indicate plausible geometry only. **[pending]**
</div>

- No formal proximity criterion was defined. The cutoff was varied (6, 8 and 10 Å) and the spread across five models is reported, but no threshold was adopted.
- **[pending]** Per-residue confidence was not extracted for the final constrained models.
- No cross-model consensus rule was defined; the spread across five models is the only internal measure of pose stability.
- **[pending]** No energy-minimised ligand-bound state was produced, so no model represents a relaxed pocket.

<figure class="figure my-4">
  <img src="/static/figures/boltz_pocket_c14.png" class="figure-img img-fluid" alt="Cartoon of the KS pocket with C14 in blue sticks. M1251 (orange), V1254 (red) and M1260 (green) are drawn as sticks with dashed distance lines of 4.3, 8.9 and 4.6 angstrom.">
  <figcaption class="figure-caption"><strong>Figure 4.</strong> C14 (blue) in the highest-confidence model of the run that forced M1251 and M1260 as contacts. Closest-atom distances: M1251 (orange), 4.3 Å; V1254 (red), 8.9 Å; M1260 (green), 4.6 Å; neighbouring residues in grey. One model of five is shown; the others differ. Boltz-2 prediction, not an experimental structure.</figcaption>
</figure>

---

**Previous:** [Step 1 Sequence](sequence) · **Next:** [Step 3 Bridge](bridge)
