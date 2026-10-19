
The modelling work comprised one complete Design, Build, Test, Learn (DBTL) cycle, in which the Test stage indicated that the design should be changed. The cycle is computational: the Test stage is model against model and model against literature, and no wet-lab data closed the loop.

## Design {#design}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The goal was to choose genetic edits that move yeast's fatty acids toward myristic acid (C14:0). Two ideas were planned: a single mutation in the fatty acid synthase, and gene deletions that reduce fat breakdown, ranked with a metabolic model. **[computed]**
</div>

**Goal.** Selection of genetic edits that shift the fatty-acid profile of *Saccharomyces cerevisiae* toward C14:0.

**Initial plan.** Two strategies were planned: (1) a FAS2 point mutation to release C14 early (by analogy with *Yarrowia lipolytica* I1220W), and (2) gene knockouts that reduce fatty-acid degradation, in order to preserve C14:0. Candidate knockouts were to be ranked by agreement between the predicted fatty-acid profile and a target, using flux balance analysis (FBA) on Yeast9.

## Build {#build}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Three tools were built: a fast metabolic calculator with a scoring function, three ways of searching gene-deletion combinations, and a pipeline that predicts how a fatty acid sits in the enzyme. **[computed]**
</div>

- A fast FBA evaluator and a scoring function over fatty-acid profiles.
- A search over knockout combinations: brute force, greedy and a reinforcement-learning agent.
- A structural pipeline for the FAS2 ketoacyl synthase (KS) domain: homology-based site identification and Boltz-2 ligand placement.

## Test {#test}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The tests undermined the plan. The ranking had almost no margin over the unedited strain, the model showed myristic acid arising only from fat breakdown, a learning-based search lost to simpler ones, and early structure predictions depended on setup. **[computed]**
</div>

- Brute-force evaluation of 175 combinations returned a leading set (FAA1 + FAA4, score 0.202529) against 0.202509 for the unedited strain, a margin of 0.010 %. Gas chromatography–mass spectrometry (GC-MS) composition varies by 1–5 % between replicates, so no experiment could separate the two. Pre-flight, a set of six automated checks, was therefore built, and the team's own scoring function failed three of them.
- Route analysis of the FBA solution showed that the model forms C14:0 only through peroxisomal β-oxidation, mainly by shortening C16:0. Deletion of *POX1* gave exactly zero.
- Benchmarking of the reinforcement-learning agent over 20 seeds showed that it found the exact best answer in 10 % of runs, compared with 65 % for greedy search and 100 % for brute force.
- The first structural runs suggested that unconstrained Boltz-2 does not place the ligand and that the acyl chain overlaps M1251. Reruns with five samples reproduced neither observation, so both are treated as dependent on the setup.

## Learn {#learn}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Five lessons followed: the planned deletion strategy was reversed, no ranked list could be sent to the laboratory, the model needed a hand-added reaction, simple search was sufficient, and one residue was excluded as a likely gate. **[computed]**
</div>

- **The degradation-knockdown strategy was inverted.** In the model, degradation is the only source of C14:0, and the strategy was therefore no longer planned.
- **The scoring function could not support any ranking**, and no knockout list was passed to the wet lab.
- **The metabolic model could not represent the intended intervention.** Yeast9 has no early C14 release from FAS, and a documented reaction was therefore added.
- **Simple search was sufficient.** At the present scale, exact enumeration finishes in minutes to under two hours.
- **M1251 is probably a gate and not a site for mutation** (**[hypothesis]**), and it was therefore excluded.

## Next iteration {#next-iteration}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

After the new reaction was added, myristic acid output rose by 2.6 % and the limit moved to NADPH. The next cycle repeats the analyses with the reaction and compares the model with published results. **[pending]**
</div>

The early-release reaction was added and the analysis was repeated: C14:0 export increased by 2.6 % and the limit moved to NADPH. Growth penalties have since been computed for the curated interventions. The next cycle repeats the frontier and knockout screen with the reaction and tests the model against published literature outcomes. See [Model](model) and [Results](results).

<div class="alert alert-secondary" role="alert" markdown="1">
**Scope.** This cycle is computational. The Test stage is model against model and model against literature; no wet-lab data closed the loop.
</div>
