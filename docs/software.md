
## Purpose of the software {#what-it-is-in-plain-language}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Pre-flight is a free tool that checks whether the score used to rank candidate gene edits can tell the candidates apart, before anyone acts on the ranking. It is a check, not a search method. In the team's own case, the score could not separate the best design from doing nothing. **[computed]**
</div>

**Pre-flight tests whether the scoring function of a model measures anything before its output is acted upon.**

When flux balance analysis (FBA) is used to choose knockouts, overexpression targets or other interventions, a scoring function forms part of the pipeline. Such a function can be entirely uninformative while producing output that appears valid, and COBRApy[@ebrahim2013|COBRApy] issues no warning. This occurred in the present project: the search was exact and the arithmetic correct, yet the top recommendation exceeded the unedited strain by 0.010 %, a difference that gas chromatography–mass spectrometry (GC-MS) cannot measure, and it was close to being passed to the wet lab. Pre-flight detects this in about ten minutes for any scoring function.

Pre-flight is **not a search method**. Brute force, greedy search and reinforcement learning address *which candidate scores best*. Pre-flight addresses *whether "best" is meaningful*. Both questions are relevant, and neither replaces the other.

## Applicability {#does-it-apply-to-you}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The tool is useful if a team ranks interventions by a score or is about to give a laboratory a list of strains to build. It is less useful if a team only reads a single product's output or is curating a model. **[computed]**
</div>

Pre-flight is likely to be applicable if interventions are ranked by a score without verification that the score separates them by more than the assay resolution; if a ratio or profile across several products is optimised; if product exchange reactions retain the default bounds of the model; if a list of strains is about to be passed to a wet lab; or if machine learning is being considered for a combinatorial design problem.

It is likely to be less applicable if the flux of a single product is maximised at fixed growth and read directly (a setup that is much harder to mislead), or if a model is being curated and not used for design; in the latter case memote[@lieven2020|memote model-testing suite] should be run instead, since it tests the model, which is a different task.

## The six checks {#the-six-checks}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Six automated checks each return pass, warning or fail with an explanation. Two of them (does doing nothing score as well as the best design, and can the score separate candidates at measurable resolution) were not found automated in any other tool. When either fails, the tool prints no ranked list. **[computed]**
</div>

Each check returns PASS, WARN or FAIL, with an explanation and a suggested remedy (Table 1).

<div class="key" markdown="1">

*Table 1. Pre-flight checks D1–D6: the condition detected, its consequence, and prior art.*

| | Detects | Consequence | Novelty |
|---|---|---|---|
| D1 | Doing nothing scores as well as the best design | The score does not respond to the intervention | Automated implementation not found in any tool surveyed |
| D2 | All candidates lie within one measurement-resolution band | The ranking is numerically real but experimentally untestable | Automated implementation not found in any tool surveyed |
| D3 | A weighted sum over several products returns only one of them | A linear program visits vertices only; weights cannot produce a blend | Not new: established methods (flux variability, alternate optima; Das and Dennis 1997[@das1997|weighted-sum scalarisation in multicriteria optimisation; relevance to D3 is a team attribution]) |
| D4 | Target exchange reactions are effectively unbounded | The model produces the target more freely than a cell could | Not new: implemented in memote |
| D5 | The score tracks biomass rather than product | Often intended, so the check asks and never fails | Not new (Schuetz et al. 2007[@schuetz2007|evaluation of objective functions for flux prediction; relevance to D5 is a team attribution]) |
| D6 | A scoring parameter changes nothing | The corresponding constraint is not binding | Not new: ordinary sensitivity analysis |

</div>

**Proposals are withheld.** When D1 or D2 fails, the tool prints no ranked list and states the reason. Of the eight strain-design tools surveyed (OptKnock,[@burgard2003] OptGene,[@patil2005] OptForce,[@ranganathan2010] RobustKnock,[@tepper2010] cameo,[@cardoso2018] MEWpy,[@pereira2021] OptFlux[@rocha2010] and StrainDesign[@schneider2022]), none checks its own scoring before emitting designs, and none withholds output.

**The threshold that matters is the resolution of the assay, not that of the solver.** The first version compared score differences with the solver tolerance and passed the defective pipeline. The thresholds are relative and tied to measurement resolution (`DETECTABLE_RELATIVE_MARGIN` = 1 %, `MEASURABLE_RELATIVE_MARGIN` = 5 %). For an assay more precise than GC-MS, the values should be reduced.

## Minimal adoption requirements {#how-little-you-have-to-adopt}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The tool needs only one function that returns a score for a set of edits. Checks that need more simply skip, so even a bare scoring function gets a useful report. **[computed]**
</div>

The checks require a single method, `evaluate(combo, target) -> float`. No COBRApy dependency is imposed, and the configuration system, evaluator and file layout need not be used. Checks that require more capability are skipped and do not fail, so that a bare scoring function still receives a useful report.

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

For the full pipeline on another organism, the configuration file is copied and its values changed. Nothing in the package itself needs editing.

## Installation and execution {#install-and-run}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The tool runs on Python 3.10 or newer with three packages and no separate solver. Four example scripts reproduce the team's analyses in 5 to 15 minutes each. The expected result of the diagnostics script is a failure, which is the demonstration. **[computed]**
</div>

Python 3.10 or newer is required, with three packages. No solver needs to be installed: GLPK is supplied with COBRApy.

| | Linux / macOS | Windows (PowerShell) |
|---|---|---|
| Check Python | `python3 --version` | `py --version` |
| Environment | `python3 -m venv venv` | `py -m venv venv` |
| Activate | `source venv/bin/activate` | `venv\Scripts\Activate.ps1` |
| Install | `pip install -r requirements.txt` | `py -m pip install -r requirements.txt` |

On Windows, if activation reports "running scripts is disabled on this system", `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` should be run first; it applies to that window only.

**Metabolic model.** The model (about 11 MB) is not included because it belongs to SysBioChalmers/yeast-GEM[@zhang2024|Yeast-GEM / Yeast9]; it is placed beside `README.md`. On Linux/macOS: `wget https://github.com/SysBioChalmers/yeast-GEM/raw/main/model/yeast-GEM.xml`. On Windows, `Invoke-WebRequest` is used (`wget` and `curl` are PowerShell aliases for other commands).

**Analyses.** The scripts are run from the folder containing `README.md`, with `-u` added on every platform, since output otherwise appears frozen (Table 2).

*Table 2. Example scripts, the question each addresses, whether the metabolic model is required, and the approximate run time.*

| Script | Addresses | Needs model | Time |
|---|---|---|---|
| `run_feasibility.py` | What the model can reach, by what route, and whether the route is robust | yes | ~5 min |
| `run_diagnostics.py` | Whether the scoring function can rank anything | yes | ~15 min |
| `run_benchmark.py` | Whether a learned search is worthwhile | no | ~5 min |
| `run_search_comparison.py` | Brute force against greedy search on the real model | yes | ~10 min |

**Expected output.** `run_feasibility.py` prints `Wild-type growth: 0.081100 /h` and ends with `Verdict: SURVIVES`. That growth rate belongs to this tool's own conditions (Yeast9, prototrophic wild type, glucose uptake 1.0 mmol gDW⁻¹ h⁻¹) and is not the BY4742 baseline of the FBA report run, which is 0.09768 h⁻¹ at an uptake of 1.1 ([Model: Data](model#m3)). `run_diagnostics.py` prints `VERDICT: NOT USABLE` and `*** NO PROPOSALS ISSUED ***`. **This failure is the correct result:** it is the demonstration and not a defect, and it shows that the scoring setup of the team could not support a ranking.

## Design choices and trade-offs {#design-choices-and-trade-offs}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Five design choices were made, each with a cost: thresholds tied to the user's assay, skipping instead of crashing, refusing instead of warning, one configuration file per organism, and brute force as the default search. **[computed]**
</div>

- **Assay-tied thresholds** instead of solver tolerance. Trade-off: the resolution of the assay must be stated.
- **Skipping, not crashing**, when a capability is missing. Trade-off: a bare scoring function receives fewer checks.
- **Refusal rather than warning** for D1 and D2. Trade-off: a user who requires a list regardless must first correct the scoring.
- **All organism-specific settings in one YAML file.** The package is organism-agnostic.
- **Brute force as the default search** at the present scale (see [Trust](trust)).

## Architecture {#architecture}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The code is a small Python package with separate parts for the checks, an optional metabolic-model evaluator, configuration, search methods, a benchmark and a proposal sheet. **[computed]**
</div>

The package `preflight/` contains `diagnostics` (the six checks), `cobra_evaluator` (an optional COBRApy-backed evaluator), `config` (the YAML-driven setup), `filters`, `search` and `agent` (brute force, greedy and reinforcement learning), `benchmark` (the search benchmark) and `proposals` (the proposal sheet, empty when D1 or D2 fails). Examples are in `examples/` and tests in `tests/`.

## Limits of applicability {#what-not-to-take-from-this}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The tool is not a search method, nothing about it has been validated against laboratory data, and its benchmark uses an artificial test problem. Its thresholds assume a particular measurement method and can be changed. **[computed]**
</div>

- Pre-flight is **not a search method**.
- **Nothing here has been validated against wet-lab data.** Every number is a statement about a model.
- The search benchmark was run on a **synthetic landscape**, because the real landscape is flat and a comparison of strategies on a flat landscape measures nothing.
- The reinforcement-learning agent is a simple linear Q-learner; the result shows that this agent was outperformed, not that the approach cannot work.
- The thresholds assume **GC-MS composition analysis** with 1–5 % replicate error. A different assay requires different values, which are set in a single constant.

## Licence, code and testing {#licence-code-and-testing}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The code is open source under the MIT licence. A second person re-ran the tests on a different operating system and obtained the same results, as reported in the team write-up. **[computed]**
</div>

The software is released under the MIT licence and may be used, modified and incorporated into other pipelines. Repository: <a href="https://github.com/Siddhant-Chowdhary/igem-preflight">github.com/Siddhant-Chowdhary/igem-preflight</a>.

**Testing.** The team write-up reports a clean-install rerun on a different operating system by a second person: 26 of 26 tests passed, the feasibility frontier was identical to four decimals, and the diagnostic verdict was the same. The write-up also states that `tests/test_diagnostics.py` prints `10 passed, 0 failed`. The two counts refer to different test suites.

Reports of cases in which a check fires, and of failure modes that are not covered by the tests, are welcome.
