
<div class="alert alert-warning" role="alert" markdown="1">
**Draft status.** This site presents the modelling results as they currently stand. All results are statements about models. **None has been validated against wet-lab data.** Unfinished items are identified on the relevant pages.
</div>

**Summary.** The IIT Bombay iGEM 2026 dry-lab team modelled the engineering of *Saccharomyces cerevisiae* to produce a C14:0-rich fatty-acid product (myristic acid) that can be esterified to methyl myristate, a bio-based immersion coolant for data centres. Six linked models were built, from a single residue of fatty acid synthase to a coolant life cycle assessment. In the metabolic model, C14:0 was formed only through peroxisomal fat breakdown, mainly by shortening C16:0; no gene knockout set exceeded the wild type; and a separate hypothetical early-release reaction increased C14 export by 2.6 %. The team's scoring function did not satisfy its own checks, so no strain proposals were issued. The central mutation (V1254W) is an assumption by homology and is untested in *S. cerevisiae*.

## Overview of the modelling work {#what-our-modelling-did}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

One question was asked at six scales, from a single amino acid to a coolant's life cycle, and each step passed a result to the next. The key assumption, that one mutation can make yeast release the 14-carbon fatty acid early, is untested. **[hypothesis]**
</div>

The modelling addressed one question at three scales and then examined whether the answer was reliable and worth acting upon (Figure 1):

1. **Sequence.** Which residue of yeast fatty acid synthase (FAS) controls chain length?
2. **FAS interaction.** Does the binding pocket of the enzyme accommodate a C14 chain, and which residues should remain unaltered?
3. **Bridge.** Can a genome-scale metabolic model represent that mutation?
4. **Metabolism.** What can the whole cell reach, at what cost to growth, and by which route?
5. **Trust.** Does the scoring of candidate designs measure anything, and is a learned search better than a simple one?
6. **Process.** Is the product suitable for its intended use, and how does it compare with other coolants?

<figure class="figure my-4 key">
  <img src="/static/figures/explainer_overview.png" class="figure-img img-fluid" alt="Six cards in two rows: Sequence, FAS interaction, Bridge, Metabolism, Trust and Process, read left to right in row 1 and right to left in row 2. Each card lists input, method, result and status tags. A dashed arrow from Bridge to Metabolism notes that Step 4 ran without the early-release reaction added in Step 3.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> The six modelling steps, with the input, method, result and status of each. Steps 1 to 3 assume that V1254W releases C14 in <em>S. cerevisiae</em> (assumption A1, a hypothesis). The Step 4 analyses were run without the early-release reaction added in Step 3; the rerun is pending. Process results are screening level and the choice of coolant is pending. Figures and identifiers shown are those reported on the step pages. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

## Guide to the pages {#where-to-read-what}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The Model pages give methods and numbers, Results gives the headline findings, Engineering the design cycle, Software the tool for other teams, and Life Cycle Assessment the coolant study.
</div>

*Table 1. Pages of this site and their content.*

| Topic | Page |
|---|---|
| Methods, assumptions, data, parameters, limits | [Model](model), with one page per step |
| Headline findings and the changes they prompted | [Results](results) |
| The design cycle | [Engineering](engineering) |
| The tool that other teams can run on their own models | [Software](software) |
| What is offered to the community | [Contribution](contribution) |
| The coolant life cycle assessment | [Life Cycle Assessment](life-cycle-assessment) |

## Status labels {#how-to-read-the-status-labels}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Every claim is tagged as computed, from the literature, a hypothesis or pending, so that results can be told apart from ideas.
</div>

Every claim on this site carries one of four labels:

- **[computed]** produced in this study; the numbers originate from the team's own code or documents.
- **[literature]** taken from a published source, which is cited.
- **[hypothesis]** a reasoned explanation that has not been tested.
- **[pending]** planned or in progress; no result is available.

## Key points {#three-things-to-know-first}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The main outcome is largely negative: no gene deletion helped and the team's own ranking failed its checks. The key mutation is an assumption, and the coolant case is not settled. **[computed]**
</div>

1. **The principal result is predominantly negative.** In the metabolic model, no gene knockout set exceeded wild-type C14:0 production, and the scoring setup of the team did not satisfy its checks. Both outcomes are reported.
2. **The mutation route is an assumption.** The proposal that a FAS2 point mutation can release C14 in *S. cerevisiae* rests on a *Yarrowia lipolytica* result[@rigouin2017|I1220W in Y. lipolytica (abstract)] and not on *S. cerevisiae* data. All downstream numbers are conditional on it.
3. **The coolant case is not settled.** The screening life cycle assessment favours methyl myristate in use under some assumptions and not others, and a separate coolant-selection analysis recommends isopropyl myristate on operability grounds. See [Life Cycle Assessment](life-cycle-assessment).
