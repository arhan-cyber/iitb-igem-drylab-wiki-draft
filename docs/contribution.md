
What our modelling work offers other teams, and what you can take without adopting anything else.

## 1. Pre-flight: a check for whether your scoring function measures anything

Six automated checks (D1–D6) on the scoring function a team writes on top of a metabolic model. Two of them (D1: does doing nothing score as well as your best design? D2: can the score separate candidates at measurable resolution?) we could not find automated anywhere. Four automate established methods, and we say which. The key transferable idea: **the threshold a ranking must clear is the assay's resolution, not the solver's numerical precision.** It needs only an `evaluate(combo, target) -> float` method, is MIT licensed and runs on Windows, macOS and Linux. See [Software](software) and [Model](trust).

## 2. A benchmark showing when machine learning is not needed

We benchmarked a reinforcement-learning agent for knockout search against brute force, greedy and random search over 20 seeds. At 10 candidate genes and up to 3 knockouts, brute force took 52 seconds and was exact; greedy found the exact best 65% of the time at about one eighth of the evaluations; our RL agent found it 10% of the time. Even at 50 candidate genes, exhaustive enumeration finishes in under two hours. **Try a trivial baseline before building machine learning.** Limits: synthetic landscape, simple linear Q-learner. See [Model](trust).

## 3. A worked screening LCA of a bio-based coolant

An open description of how we compared a yeast-derived ester against commercial immersion coolants: functional units, system boundary, allocation choices, nine proxy datasets built from reaction stoichiometry where ecoinvent has none, and a CFD-derived use phase. Its limits are as useful as its method: the result depends on the grid carbon factor, and the study has not been critically reviewed. See [Life Cycle Assessment](life-cycle-assessment).

