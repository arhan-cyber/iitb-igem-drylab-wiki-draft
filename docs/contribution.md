
This page describes what the modelling work offers to other teams and what can be used without adopting the rest of the work.

## Pre-flight: a check of whether a scoring function measures anything {#1-pre-flight-a-check-for-whether-your-scoring-function-measures-anything}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

An open-source tool checks whether the score used to rank gene edits can distinguish good designs from doing nothing. It needs only one function that returns a score, and runs on Windows, macOS and Linux. **[computed]**
</div>

Pre-flight applies six automated checks (D1–D6) to the scoring function built on top of a metabolic model. Two of the checks could not be found automated elsewhere: D1 (whether doing nothing scores as well as the best design) and D2 (whether the score separates candidates at measurable resolution). The other four automate established methods, which are identified on the Software page. The transferable principle is that **the threshold a ranking must exceed is the resolution of the assay, not the numerical precision of the solver.** The tool requires only an `evaluate(combo, target) -> float` method, is released under the MIT licence and runs on Windows, macOS and Linux. See [Software](software) and [Trust](trust).

## A benchmark of when machine learning is not required {#2-a-benchmark-showing-when-machine-learning-is-not-needed}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

On an artificial test problem, a simple greedy search found the best answer more often than a basic learning-based search, and trying every combination stayed practical at the scale tested. A trivial baseline should therefore be tried before building machine learning. **[computed]**
</div>

A reinforcement-learning agent for knockout search was benchmarked against brute force, greedy and random search over 20 seeds. For 10 candidate genes and up to 3 knockouts, brute force took 52 s and was exact; greedy search found the exact best answer in 65 % of seeds with about one eighth of the evaluations; the reinforcement-learning agent found it in 10 %. Even at 50 candidate genes, exhaustive enumeration finishes in under two hours. A trivial baseline should be tried before machine learning is built. Limits: the landscape is synthetic and the agent is a simple linear Q-learner. See [Trust](trust).

## A worked screening life cycle assessment of a bio-based coolant {#3-a-worked-screening-lca-of-a-bio-based-coolant}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

An open description is provided of how a yeast-derived coolant was compared with commercial ones, covering the choices made and their limits. The result depends on the electricity grid, and the study has not been independently reviewed. **[computed]**
</div>

The Life Cycle Assessment page describes how a yeast-derived ester was compared with commercial immersion coolants: functional units, system boundary, allocation choices, nine proxy datasets constructed from reaction stoichiometry where ecoinvent has none, and a use phase derived from computational fluid dynamics. The limits are as informative as the method: the result depends on the grid carbon factor, and the study has not been critically reviewed. See [Life Cycle Assessment](life-cycle-assessment).
