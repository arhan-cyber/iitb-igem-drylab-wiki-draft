<!-- DRAFT built 2026-10-15. Dry-lab engineering cycle only. TODO: wet-lab engineering entries belong to the wet-lab team's pages. -->

Our dry lab went through one full Design, Build, Test, Learn cycle, and the Test stage told us to change the design.

## Design

**Goal.** Choose genetic edits that move *S. cerevisiae*'s fatty-acid profile toward C14:0.

**Plan at the start.** Two ideas: (1) a FAS2 point mutation to release C14 early (by analogy with *Yarrowia* I1220W), and (2) gene knockouts that reduce fatty-acid degradation, to preserve C14:0. Candidate knockouts would be ranked by how closely the predicted fatty-acid profile matched a target, using flux balance analysis on Yeast9.

## Build

- A fast FBA evaluator and a scoring function over fatty-acid profiles.
- A search over knockout combinations: brute force, greedy and a reinforcement-learning agent.
- A structural pipeline for the FAS2 KS domain: homology-based site identification and Boltz-2 ligand placement.

## Test

- Brute force over 175 combinations returned a clear winner (FAA1 + FAA4, score 0.202529) against 0.202509 for the unedited strain, a margin of 0.010%. GC-MS composition varies by 1–5% between replicates, so no experiment could separate them. We built pre-flight, six automated checks, and our own scoring failed three of them.
- A route analysis of the FBA solution showed that the model makes C14:0 only by shortening C16:0 through beta-oxidation. Deleting *POX1* gave exactly zero.
- Benchmarking the reinforcement-learning agent over 20 seeds showed it found the exact best answer in 10% of runs, against 65% for greedy and 100% for brute force.
- The structural runs showed unconstrained Boltz-2 does not place the ligand, and that the acyl chain clashes with M1251 in every constrained run.

## Learn

- **The degradation-knockdown strategy was inverted.** In the model, degradation is the only source of C14:0, so we stopped planning it.
- **Our scoring could not support any ranking**, so we sent no knockout list to the wet lab.
- **Our model could not represent our own intervention.** Yeast9 has no early C14 release from FAS, so we added a documented reaction.
- **Simple search was enough.** At our scale exact enumeration finishes in minutes to under two hours.
- **M1251 is probably a gate, not a place to mutate**, so we excluded it.

## Next iteration

We added the early-release reaction and re-ran the analysis: C14:0 rose +2.6% and the limit moved to NADPH. The next cycle re-runs the frontier and knockout screen with the reaction, computes growth penalties and tests the model against published literature outcomes. See [Model](model) and [Results](results).

<div class="alert alert-secondary" role="alert" markdown="1">
**Honest scope.** This cycle is computational. The Test stage is model-against-model and model-against-literature; no wet-lab data closed the loop.
</div>
