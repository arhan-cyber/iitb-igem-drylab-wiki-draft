
## What it is, in plain language

**Pre-flight checks whether your model's scoring function is measuring anything, before anyone acts on what it says.**

If you use flux balance analysis to choose knockouts, overexpression targets or any other intervention, there is a scoring function somewhere in your pipeline. It can be completely broken while producing output that looks perfect, and nothing in COBRApy will warn you. That is what happened to us: our search was exact, our arithmetic was right, and our top recommendation beat doing nothing by 0.010%, a difference no GC-MS could ever measure. We were close to sending it to our wet lab. Pre-flight catches this in about ten minutes, on any scoring function.

It is **not a search method**. Brute force, greedy search and reinforcement learning answer *which candidate scores best*. Pre-flight answers *whether "best" means anything*. Both questions are worth asking; neither replaces the other.

## Does it apply to you?

**Probably yes if** you rank interventions by a score without checking that the score separates them by more than your assay could measure; you optimise a ratio or profile across several products; your product exchange reactions still carry the model's default bounds; you are about to hand a wet lab a list of strains to build; or you are considering machine learning for a combinatorial design problem.

**Probably not if** you maximise a single product's flux at fixed growth and read the number directly (that setup is much harder to fool), or you are curating a model rather than designing with one (run [memote](https://doi.org/10.1038/s41587-020-0446-y) instead; it checks the model, which is a different job).

## The six checks

Each returns PASS, WARN or FAIL, with an explanation and a suggested fix.

| | Catches | Why it matters | Is it new? |
|---|---|---|---|
| D1 | Doing nothing scores as well as your best design | The score is not responding to the intervention at all | We could not find this automated in any tool |
| D2 | All candidates sit inside one measurement-resolution band | The ranking is numerically real and experimentally untestable | We could not find this either |
| D3 | A weighted sum over several products returns only one of them | A linear program only visits vertices; weights cannot buy a blend | No. Established methods (flux variability, alternate optima; Das & Dennis 1997) |
| D4 | Target exchange reactions are effectively unbounded | The model produces your target more freely than a cell could | No. memote already ships this |
| D5 | The score tracks biomass rather than product | Often intended, so this check only asks and never fails | No (Schuetz 2007) |
| D6 | A scoring parameter changes nothing | That constraint is not binding | No. Ordinary sensitivity analysis |

**It refuses to issue proposals.** When D1 or D2 fail, the tool prints no ranked list and explains why. Of the eight strain-design tools we surveyed (OptKnock, OptGene, OptForce, RobustKnock, cameo, MEWpy, OptFlux, StrainDesign), none checks its own scoring before emitting designs, and none refuses.

**The idea we most want other teams to take: the threshold that matters is the assay's resolution, not the solver's.** Our first version compared score differences against solver tolerance and passed the broken pipeline. Thresholds here are relative and tied to measurement resolution (`DETECTABLE_RELATIVE_MARGIN` = 1%, `MEASURABLE_RELATIVE_MARGIN` = 5%). If your assay is tighter than GC-MS, tighten them.

## How little you have to adopt

The checks need one method: `evaluate(combo, target) -> float`. No COBRApy requirement, no need to use our config system, evaluator or file layout. Checks that need more capability skip rather than crash, so a bare scoring function still gets a useful report.

```python
from preflight import run_diagnostics

class MyEvaluator:
    def evaluate(self, combo, target):
        return my_existing_scoring_function(combo, target)

report = run_diagnostics(
    MyEvaluator(),
    {"product_A": 0.7, "product_B": 0.3},
    candidate_combos=[("geneX",), ("geneY",), ("geneX", "geneY")],
)
print(report.to_text())
print(report.usable)  # False means any ranking is an artefact
```

For the full pipeline on your own organism, copy the config file and change the values. Nothing in the package itself needs editing.

## Install and run

Python 3.10 or newer. Three packages. No solver to install: GLPK ships with COBRApy.

| | Linux / macOS | Windows (PowerShell) |
|---|---|---|
| Check Python | `python3 --version` | `py --version` |
| Environment | `python3 -m venv venv` | `py -m venv venv` |
| Activate | `source venv/bin/activate` | `venv\Scripts\Activate.ps1` |
| Install | `pip install -r requirements.txt` | `py -m pip install -r requirements.txt` |

On Windows, if activation reports "running scripts is disabled on this system", run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first; it applies to that window only.

**Get the metabolic model** (about 11 MB, not included because it belongs to SysBioChalmers/yeast-GEM) and put it beside `README.md`. On Linux/macOS: `wget https://github.com/SysBioChalmers/yeast-GEM/raw/main/model/yeast-GEM.xml`. On Windows use `Invoke-WebRequest` (`wget` and `curl` are PowerShell aliases for something else).

**Run the analyses** from the folder containing `README.md`, adding `-u` on every platform or output looks frozen:

| Script | Answers | Needs model | Time |
|---|---|---|---|
| `run_feasibility.py` | What the model can reach, by what route, and whether the route is robust | yes | ~5 min |
| `run_diagnostics.py` | Whether the scoring function can rank anything | yes | ~15 min |
| `run_benchmark.py` | Whether a learned search is worth it | no | ~5 min |
| `run_search_comparison.py` | Brute force against greedy on the real model | yes | ~10 min |

**What success looks like.** `run_feasibility.py` prints `Wild-type growth: 0.081100 /h` and ends with `Verdict: SURVIVES`. `run_diagnostics.py` prints `VERDICT: NOT USABLE` and `*** NO PROPOSALS ISSUED ***`. **That failure is the correct result:** it is the demonstration, not a bug. The tool is showing that our own scoring setup cannot support a ranking.

## Design choices and trade-offs

- **Assay-tied thresholds** instead of solver tolerance. Trade-off: you must state your assay's resolution.
- **Skip, do not crash**, when a capability is missing. Trade-off: a bare scoring function gets fewer checks.
- **Refuse rather than warn** for D1 and D2. Trade-off: a user who wants a list anyway must fix the scoring first.
- **Everything organism-specific lives in one YAML file.** The package is organism-agnostic.
- **Brute force is the default search** at our scale (see [Model](trust)).

## Architecture

The package `preflight/` contains: `diagnostics` (the six checks), `cobra_evaluator` (an optional COBRApy-backed evaluator), `config` (the YAML-driven setup), `filters`, `search` and `agent` (brute force, greedy, RL), `benchmark` (the search benchmark) and `proposals` (the proposal sheet, empty when D1 or D2 fail). Examples live in `examples/` and tests in `tests/`.

## What not to take from this

- It is **not a search method**.
- **Nothing here is validated against wet-lab data.** Every number is a statement about a model.
- The search benchmark runs on a **synthetic landscape**, because our real one is flat and comparing strategies on a flat landscape measures nothing.
- Our RL agent is a simple linear Q-learner, so we can say ours lost, not that the approach cannot work.
- Thresholds assume **GC-MS composition analysis** at 1–5% replicate error. Different assay, different numbers; it is a single constant to change.

## Licence, code and testing

MIT licensed: use it, modify it, fold it into your own pipeline. Repository: <a href="https://github.com/Siddhant-Chowdhary/igem-preflight">github.com/Siddhant-Chowdhary/igem-preflight</a>.

**Testing.** The team writeup reports a clean-install re-run on a different operating system by a second person: 26 of 26 tests passing, feasibility frontier identical to four decimals, and the same diagnostic verdict. It also says `tests/test_diagnostics.py` prints `10 passed, 0 failed`. The two counts refer to different test suites.

If a check fires on your project, especially if it catches something, we would be glad to know, and if you find a failure mode we do not test for, that is the most useful thing you could send back.
