<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed. **None of the values on this page has been validated against wet-lab data.**
</div>

## Step 5. Reliability of the strain-design ranking {#trust}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The team's own method for ranking gene deletions could not tell the best strain from the unedited one, so an automated checking tool withheld any recommendations. A simple benchmark also showed that a simple search method does nearly as well as exhaustive search, while a learning-based method did worse. **[computed]**
</div>

This step examines whether the ranking of gene knockouts produced by the scoring function carries information that could justify an experiment. Three analyses are reported: a failure of the scoring function against its own checks, a comparison of distance measures, and a benchmark of search methods.

## Failure of the scoring function against its checks {#the-failure-that-started-it}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The best-ranked knockout scored only 0.010 % better than the unedited strain, far less than the 1–5 % variation expected between repeated measurements. The ranking therefore could not be acted on. **[computed]**
</div>

**[computed]** The pipeline ranked gene knockouts by the agreement between the predicted fatty-acid profile and a target profile. Exhaustive evaluation of all 175 combinations returned FAA1 + FAA4 as the highest-scoring set (score 0.202529). The unedited strain scored 0.202509, a difference of 0.010 %. The composition of fatty acids measured by gas chromatography–mass spectrometry (GC-MS) varies by roughly 1–5 % between biological replicates, so an experiment could not be expected to separate the two strains. The search was exact and the arithmetic correct; the scoring function did not discriminate between candidates, and no error message indicated this.

## Pre-flight checks D1–D6 {#six-checks}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

An automated tool called pre-flight runs six checks on a scoring function. Three failed and three gave warnings for the team's setup, so the tool issued no strain proposals. **[computed]**
</div>

The pre-flight tool (Software page) applies six automated checks to a scoring function; each returns PASS, WARN or FAIL with an explanation (Table 1). The thresholds are tied to assay resolution rather than to solver tolerance. A first version compared score differences with solver tolerance (about one part in a million) and passed the pipeline described above.

<div class="key" markdown="1">

*Table 1. Pre-flight checks and their outcome for the configuration described in the previous section. Model-implied; not validated against wet-lab data.*

| Check | Question | Result for this configuration |
|---|---|---|
| D1 | Does doing nothing score as well as the best intervention? | **FAIL**: the best intervention exceeded doing nothing by 0.010 % |
| D2 | Can the score separate candidates at measurable resolution? | **FAIL**: 20 candidates, all within one measurement band |
| D3 | Does a weighted sum over several products control the blend? | **FAIL**: one product at every weight |
| D4 | Are product exchange reactions realistically bounded? | WARN: all four target exchanges bounded at 1000 |
| D5 | Does the score track growth rather than product? | WARN: growth identical across candidates |
| D6 | Do the scoring parameters change anything? | WARN: one parameter moved no score |

</div>

The verdict was NOT USABLE: the tool withheld strain proposals because checks D1, D2 and D3 failed, and no ranked knockout list was therefore passed to experimental work. Four of the six checks are not new: D3–D6 automate established methods, and D4 is already implemented in memote.[@lieven2020|memote, the model-testing tool; the overlap with D4 is a team statement that was not checked against the memote tests] Automated versions of D1 and D2 were not found in any tool surveyed by the team (Figure 1).

<figure class="figure my-4">
  <img src="/static/figures/preflight_gate.png" class="figure-img img-fluid" alt="Diagram contrasting search, which ranks candidates, with pre-flight, which checks the scoring function. Pre-flight sits between the model and the search; on pass the search runs and produces a proposal sheet, on fail no proposals are issued with the reason.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> Workflow position of pre-flight. Search identifies the candidate that scores best; pre-flight assesses whether the score is informative. Neither replaces the other. Schematic.</figcaption>
</figure>

## Comparison of loss functions {#loss-function-comparison}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Ten ways of measuring how far a predicted fatty-acid mixture is from a target were compared. A simple one, total variation, is the recommended default, and designs closer than about 0.014 cannot be told apart at 3 % measurement noise. The target used was illustrative. **[computed]**
</div>

**[computed]** Ten distance measures for fatty-acid profiles were compared: total variation, L2, cosine, Jensen–Shannon, Hellinger, Kullback–Leibler (KL), Bray–Curtis, Aitchison, and one- and two-dimensional Earth Mover's distance. Every metric except cosine and Aitchison resolved only about 4–8 % relative differences at 3 % noise. Total variation is the recommended default (a true metric between 0 and 1; for a pure-C14 target it equals one minus the C14:0 fraction). The runner-up is the two-dimensional chain-aware Earth Mover's distance, the only candidate for which C14:0 is closer to C16:0 than to C18:1. Designs whose total-variation losses differ by less than about 0.014 are tied at 3 % noise. The profile target and the yeast-like background used here are illustrative.

## Cost-effectiveness of learned search relative to brute force and greedy search {#is-learned-search-worth-it}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

On an artificial test problem, a simple greedy search found the best answer 65 % of the time, while a basic reinforcement-learning method found it 10 % of the time and needed far more evaluations. This does not show that the learning approach cannot work. **[computed]**
</div>

**[computed, synthetic landscape]** A reinforcement-learning (RL) agent for knockout search was benchmarked over 20 random seeds against brute force and greedy hill-climbing (Table 2, Figure 2). Random search on the RL agent's budget also matched greedy search, which indicates that the landscape contains many near-optimal solutions. A separate earlier RL run on a four-product profile found only 3 distinct flux vectors in 122 evaluations, consistent with the same degeneracy. Independent verification of that run has not been done.

<div class="key" markdown="1">

*Table 2. Search methods on a synthetic landscape of 10 genes with up to 3 knockouts (20 seeds). Shortfall is the gap to the exact optimum.*

| Method | Finds exact best | Mean shortfall | Evaluations |
|---|---|---|---|
| Brute force | 100 % (by definition) | 0 % | 175 |
| Greedy hill-climbing | 65 % | 1.14 % | 23 |
| Reinforcement learning | 10 % | 10.13 % | 1,204 |

</div>

<figure class="figure my-4">
  <img src="/static/figures/rl_benchmark.png" class="figure-img img-fluid" alt="Three bar charts comparing brute force, greedy and reinforcement learning: share finding the exact best answer (100, 65, 10 percent), mean shortfall (0, 1.14, 10.13 percent) and evaluations (175, 23, 1204).">
  <figcaption class="figure-caption"><strong>Figure 2.</strong> Share of seeds reaching the exact optimum, mean shortfall and evaluations for brute force, greedy search and reinforcement learning (20 seeds, synthetic landscape). The RL agent was a simple linear Q-learner, so the result shows that this agent was outperformed, not that the approach cannot work.</figcaption>
</figure>

## Cost of enumeration {#when-does-enumeration-stop-being-affordable}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Trying every combination stays practical for up to about 50 candidate genes at the measured speed of 0.30 s per calculation, and greedy search was much faster and came close to the best answer. In this range a learned search was not needed. **[computed]**
</div>

At 0.30 s per flux balance analysis (FBA) solve (measured on the team's evaluator), exact search over 10 candidate genes takes 52 s, 20 genes 7 min, 30 genes 23 min, 40 genes 54 min and 50 genes 1.7 h. Greedy search took 6–35 s throughout and reached 99.5–100 % of the exact optimum (single seed; indicative only). In this range a learned search was not required.

---

**Previous:** [Step 4 Metabolism](metabolism) · **Next:** [Step 6 Process](process)
