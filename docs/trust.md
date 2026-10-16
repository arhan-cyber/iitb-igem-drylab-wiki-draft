<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Labels: **[computed]** our own run; **[literature]** published source; **[hypothesis]** reasoned, untested; **[pending]** not finished. **None of the numbers on this page is validated against wet-lab data.**
</div>

## Step 5. Can we trust the ranking? {#trust}


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

Random search on the RL agent's budget also matched greedy, so the landscape has many near-optimal answers. A separate earlier RL run on a four-product profile found only 3 distinct flux vectors in 122 evaluations, the same degeneracy seen from another angle. Independent verification of that run has not been done.

<figure class="figure my-4">
  <img src="/static/figures/rl_benchmark.png" class="figure-img img-fluid" alt="Three bar charts comparing brute force, greedy and reinforcement learning: share finding the exact best answer (100, 65, 10 percent), mean shortfall (0, 1.14, 10.13 percent) and evaluations (175, 23, 1204).">
  <figcaption class="figure-caption">Try the trivial baseline first. 20 seeds, synthetic landscape; our RL agent is a simple linear Q-learner, so we can say ours lost, not that the approach cannot work.</figcaption>
</figure>

**When does enumeration stop being affordable?** At 0.30 s per FBA solve (measured on our evaluator): 10 candidate genes take 52 s for exact search, 20 take 7 min, 30 take 23 min, 40 take 54 min, 50 take 1.7 h. Greedy takes 6–35 s throughout and reached 99.5–100% of the exact optimum (single seed; indicative only). In this range a learned search is not needed.

---

**Previous:** [Step 4 Metabolism](metabolism) · **Next:** [Step 6 Process](process)
