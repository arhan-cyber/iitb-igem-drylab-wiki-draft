<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Labels: **[computed]** our own run; **[literature]** published source; **[hypothesis]** reasoned, untested; **[pending]** not finished. **None of the numbers on this page is validated against wet-lab data.**
</div>

## Step 2. FAS interaction level {#structure}


**Question.** *Does the KS3 pocket hold a C14 chain, and which residues must we leave alone?*

**Setup.** Boltz-2 on the KS domain only (residues 1123–1657, UniProt annotation), on Google Colab (T4 GPU) with `--use_msa_server --diffusion_samples 1`. Ligand: myristic acid (SMILES CCCCCCCCCCCCCC(=O)O). **[computed]**

**Unconstrained runs are setup-dependent.** In the first run, without constraints, Boltz-2 did not place the fatty acid near the pocket (baseline ligand ipTM 0.511, interface position error 9.1 Å). A rerun on the lab server (five samples, fixed alignment) placed it near the catalytic cysteine C1305 without any constraint (ligand ipTM 0.80, closest distance to C1305 3.0–4.6 Å). We therefore do not claim that Boltz-2 fails without constraints; the result depends on the setup. The later constrained runs used explicit distance constraints.

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
| M1251 | M1217 | 0.96–1.77 Å in the first runs; 3.1–6.3 Å in the reruns | Excluded from mutagenesis |
| V1254 | I1220 | 4.35 Å in the first runs (superposition: 5.72 Å); 4.0–9.3 Å in the reruns | Retained; proposed V1254W |
| M1260 | M1226 | 6.91 Å in the first runs; 3.9–6.5 Å when forced, 15–17 Å otherwise (reruns) | Retained as secondary candidate |

The first-run distances come from team comments on the constrained run; the rerun distances are closest-atom distances measured across the reruns' models. They differ because the constraints differ (see below). The proximity criterion remains informal.

### Catalytic and mechanistic exclusions **[literature]**

From the cerulenin-inhibited ScFAS structure (Johansson 2008, PDB 2VKZ):

| Residue | Role | Why excluded |
|---|---|---|
| C1305 | Nucleophilic active-site cysteine | Forms the acyl-enzyme thioester. Absolute exclusion |
| F1646 | Shields the active site; flips to give access | Gates catalytic accessibility |
| M1251 | Centre of the acyl-binding tunnel; rotates to unlock the inner cavity | A conformational gate; mutating it alters tunnel access, not volume |
| G1250 | Next to M1251; strains mutated here are characterised in the same work | Mechanically coupled to the gate |
| K1413 to K1423 loop | Ligand-accessibility determinant | Not catalytic, but not safely mutable |

### The M1251 clash: reported in the first runs, not reproduced **[hypothesis]**

In the first constrained runs the acyl chain clashed with M1251 at 0.96–1.77 Å, and the clash was also present in the raw structural superposition built from 8PRW. In our reruns (below) no model shows it. The superposition is the remaining evidence that a closed gate is incompatible with the chain. Attempted fixes in the first round did not resolve it: OpenBabel UFF minimisation, PyMOL sculpting, and the PyMOL mutagenesis wizard (which only ranks pre-enumerated rotamers and cannot find an intermediate side-chain geometry).

**Working interpretation.** M1251 is a known conformational gate in the cerulenin-bound structure, which is why we exclude it from mutagenesis on mechanistic grounds. Whether a closed gate clashes with a C14 chain in the ligand-bound state is untested here: the superposition suggests it, and the Boltz-2 reruns do not show it. Molecular dynamics (GROMACS or Amber) would test it; it has not been run.

### Reruns on the lab GPU server **[computed]**

After the first runs we repeated the experiment on three RTX A6000 GPUs with one setup throughout: the same 535-residue KS-domain input, Boltz-2 with five samples per run, seed 42, a fixed multiple-sequence alignment, and myristic acid (C14) unless stated. Two constraint designs were compared:

- **C1305 contact (soft cutoff).** One pocket contact on the catalytic cysteine C1305 with a 6, 8 or 10 Å cutoff, plus an unconstrained baseline, a V1254W variant, and C16 and C22 ligands at 8 Å (7 runs).
- **Forced gate contacts.** Pocket contacts on M1251 and M1260 (and in one run V1254 as well) with `force: true`, with and without Boltz's steering potentials (8 runs).

This gives 75 models. The earlier Colab runs used one sample and constraints that are not fully recorded, so they are not directly comparable.

<figure class="figure my-4">
  <img src="/static/figures/boltz_distance_spread.png" class="figure-img img-fluid" alt="Dot plot of the distance from C14 to M1251, V1254 and M1260 for four Boltz-2 setups, five models each. Distance to M1251 stays between about 3 and 6 angstrom in every setup, above a shaded band at 0.96 to 1.77 angstrom. Distance to M1260 is about 15 angstrom without forced contacts and about 4 to 6 angstrom when M1260 is forced.">
  <figcaption class="figure-caption">Closest-atom distance from C14 to three residues in five Boltz-2 models of each setup (dot = model, bar = median). The shaded band is the 0.96–1.77 Å range reported for an M1251 clash in the first runs; no model of the reruns comes near it. Where the chain sits depends on which residues are forced as contacts. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

What we take from these runs, and what we do not:

- **Constraint design moves the pose.** The distance to M1260 is 15–17 Å when only C1305 is constrained and 3.9–6.5 Å when M1260 is forced. Any statement of the form "C14 is X Å from residue Y" describes the setup as well as the pocket.
- **No clash with M1251 in the reruns.** M1251 stays 3.1–6.3 Å from the ligand in every model, and no ligand atom comes closer than 2.4 Å to any protein atom, with or without steering potentials. The 0.96–1.77 Å values from the first runs are not reproduced. We do not yet know why (software version, sample count, constraints, or how the distance was measured).
- **Confidence does not discriminate.** Overall confidence is 0.90–0.94 and ligand ipTM 0.74–0.88 for every run, including the unconstrained baseline.

<figure class="figure my-4">
  <img src="/static/figures/boltz_confidence.png" class="figure-img img-fluid" alt="Dot plots of overall confidence (about 0.90 to 0.94) and ligand ipTM (about 0.75 to 0.90) for ten Boltz-2 runs; all runs overlap heavily.">
  <figcaption class="figure-caption">Overall confidence and ligand ipTM for ten of the reruns (five models each). Confidence stays high everywhere, including without constraints, so it does not tell the setups or the ligands apart.</figcaption>
</figure>

<figure class="figure my-4">
  <img src="/static/figures/boltz_chain_length.png" class="figure-img img-fluid" alt="Two panels of distance from C14, C16 and C22 to M1251, V1254 and M1260. In both constraint designs the three ligands reach the same residues at similar distances.">
  <figcaption class="figure-caption">C14, C16 and C22 under two constraint designs. All three ligands reach the same residues, so this KS-only setup does not discriminate by chain length. Model-implied.</figcaption>
</figure>

### Controls

C16 and C22 runs exist as controls: if the pocket discriminates on chain length, the ligands should behave differently in it. A preliminary team comparison found C14 about 6 Å from the two target residues, while for C16 the distances were non-uniform (about 5 Å and 8 Å). In the reruns C14, C16 and C22 reach the same residues at similar distances (figure above), so these controls do not show chain-length discrimination in a KS-only setup. A formal positive control (a system that definitely binds) is still missing, and the unconstrained baseline is not a clean negative control because it also found the pocket.

### Limits of this step

- No formal proximity criterion: we swept the cutoff (6, 8 and 10 Å) and report the spread across five models, but have not declared a threshold.
- **[pending]** No per-residue confidence extracted for the final constrained models.
- No cross-model consensus rule; the spread across five models is the only internal measure of how stable a pose is.
- **[pending]** No minimised ligand-bound state, so no model represents a relaxed pocket.

<figure class="figure my-4">
  <img src="/static/figures/boltz_pocket_c14.png" class="figure-img img-fluid" alt="Cartoon of the KS pocket with C14 in blue sticks. M1251 (orange), V1254 (red) and M1260 (green) are drawn as sticks with dashed distance lines of 4.3, 8.9 and 4.6 angstrom.">
  <figcaption class="figure-caption">C14 (blue) in the highest-confidence model of the run that forces M1251 and M1260 as contacts. Closest-atom distances: M1251 (orange) 4.3 Å, V1254 (red) 8.9 Å, M1260 (green) 4.6 Å; nearby residues in grey. One model of five; the others differ. Boltz-2 model, not an experimental structure.</figcaption>
</figure>

---

**Previous:** [Step 1 Sequence](sequence) · **Next:** [Step 3 Bridge](bridge)
