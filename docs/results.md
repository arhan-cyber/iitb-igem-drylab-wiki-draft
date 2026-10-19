<div class="alert alert-warning" role="alert" markdown="1">
Every result below is a statement about a model and has **not been validated against wet-lab data**. Full methods, assumptions and numbers are given on the [Model](model) pages.
</div>

## Summary of findings {#summary-of-findings}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

In the computer models, yeast can already make pure myristic acid, but only by shortening a longer fatty acid, and no gene deletion tested improved on the unedited strain. The team's own ranking method did not pass its checks. Nothing here has been tested in a laboratory. **[computed]**
</div>

1. **Wild-type yeast produced pure C14:0 in the model, at a linear growth cost.** No knockout set improved on wild type. [Details](metabolism)
2. **The model formed C14:0 only through peroxisomal β-oxidation**, mainly by shortening C16:0. *POX1* catalyses the committed step. [Details](metabolism)
3. **A fatty acid synthase (FAS) early-release reaction raised C14:0 export by 2.6 %.** The limit was NADPH, not chain supply. [Details](bridge)
4. **The ScFAS2 residue equivalent to the *Yarrowia* chain-length residue is V1254.** M1251 was excluded from mutagenesis; the effect of V1254W in *S. cerevisiae* is an assumption. [Details](sequence)
5. **The scoring function did not satisfy its own checks.** The best knockout set exceeded the unedited strain by 0.010 %, and the tool issued no proposals. [Details](trust)
6. **A learned search was outperformed by simpler searches.** Brute force and greedy search outperformed the reinforcement-learning agent. [Details](trust)
7. **The coolant case is mixed.** [Details](life-cycle-assessment)

## Reachable C14:0 under growth constraints {#1-what-the-model-says-is-reachable}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

In the model, output of myristic acid falls as more growth is required, from 0.226 at 10 % of maximum growth to 0.025 at 90 % (mmol per gram dry weight per hour), and is zero at maximum growth. No gene deletion improved on this. **[computed]**
</div>

Table 1 gives the maximum free-myristate export under a minimum growth requirement. The quantity is free C14:0 from the native β-oxidation routes, not methyl myristate and not a measured titre.

<div class="key" markdown="1">

*Table 1. Maximum free-myristate export (mmol gDW⁻¹ h⁻¹) under a minimum growth requirement. Model-implied; not validated against wet-lab data.*

| Minimum growth | Primary: forward-only | Sensitivity: shipped bounds |
|---|---|---|
| none | 0.25001 | 0.25692 |
| 10 % of maximum | 0.22649 | 0.23274 |
| 25 % | 0.19036 | 0.19647 |
| 50 % | 0.12719 | 0.13156 |
| 75 % | 0.06359 | 0.06578 |
| 90 % | 0.02544 | 0.02631 |
| 100 % | 0 | 0 |

</div>

<figure class="figure my-4">
  <img src="/static/figures/feasibility_frontier.png" class="figure-img img-fluid" alt="Maximum C14 export falls linearly from 0.211 at 10 percent growth to 0.024 at 90 percent; wild type and two knockout sets overlap and POX1 sets are at zero.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> Maximum C14 export against the growth rate held (data of Table 1). No knockout set exceeded wild type; sets containing <em>POX1</em> gave exactly zero. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

The row without a growth requirement is a zero-growth limit and is not available to a growing culture. The conditions are listed in [Model: Data](model#m3).

## Metabolic route to C14:0 {#2-how-c140-is-made-in-the-model}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The model makes myristic acid by one route only: chopping two carbons off palmitic acid, with the gene *POX1* controlling the key step. Deleting *POX1* removed all output. **[computed]**
</div>

The route carrying the flux was a single unbranched path: peroxisomal C16:0-CoA → acyl-CoA oxidase (*POX1*) → hydratase and dehydrogenase (*FOX2*) → thiolase (*POT1*) → myristoyl-CoA → free C14:0 → export, with release by the *TES1* thioesterase. A second route, through C18:1 degradation and re-elongation, is used when the thiolase step is blocked; blocking both abolishes export. Deletion of *POX1* gave exactly zero. Loopless FBA reproduced the same optima, and forcing the ligases one-way lowered export by 2.7–3.3 %.

## Changes to the plan {#3-what-changed-in-our-plan}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Four decisions followed from the models: a planned gene-deletion strategy was dropped, a new reaction was added to the model, five residues were ruled out as mutation sites, and no ranked list of deletions went to the laboratory. **[computed]**
</div>

- The plan to knock down degradation to preserve C14:0 was **dropped**, because degradation is the only C14:0 source in the absence of early release.
- A FAS early-release reaction was **added** as a documented model modification: C14 +2.6 % at 50 % growth, limited by NADPH (Figure 2).
- M1251, C1305, F1646, G1250 and K1413–K1423 were **excluded** from mutagenesis, and **V1254W** was retained as the lead candidate.
- A ranked knockout list was **withheld** from the wet lab because checks D1 and D2 failed.

<figure class="figure my-4">
  <img src="/static/figures/bridge_early_release.png" class="figure-img img-fluid" alt="Left: C14 export with and without the early-release reaction at 10, 50 and 90 percent growth, nearly equal. Right: freeing NADPH raises C14 by 150.9 percent; freeing acetyl-CoA or malonyl-CoA changes it by 0.01 percent.">
  <figcaption class="figure-caption"><strong>Figure 2.</strong> Maximum C14 export with and without the early-release reaction at 10, 50 and 90 % of wild-type growth (left) and the change in maximum C14 export when individual resources were made unconstrained (right; NADPH +150.9 %, acetyl-CoA and malonyl-CoA +0.01 %). The reaction changed the route, not the amount; cofactors set the limit. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

## Structural result: site and pocket {#4-structural-result-site-and-pocket}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The matching position in baker's yeast for the *Yarrowia* chain-length residue is V1254. An early structure prediction suggested a collision with another residue, M1251, but repeat runs did not show it, so this remains a hypothesis. **[hypothesis]**
</div>

V1254 (ScFAS2) corresponds to I1220 (YlFAS), with a 34-residue offset and no gaps at or beside the key column. In the first constrained Boltz-2 runs, C14 was positioned 4.35 Å from V1254 and 6.91 Å from M1260 and overlapped M1251 at 0.96–1.77 Å, which was interpreted as a closed conformational gate (**[hypothesis]**). Reruns on the laboratory server did not reproduce the overlap, and distances varied with the choice of constrained residues, so these numbers describe the setup as well as the pocket. [Details](fas-interaction)

## Scoring checks and search benchmark {#5-our-scoring-failed-its-own-checks}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Three of six automated checks on the team's scoring method failed, so the tool refused to issue strain proposals. On an artificial test, a greedy search found the best answer 65 % of the time and a learning-based search 10 %. **[computed]**
</div>

Results of the pre-flight checks are given in Table 2 and of the search benchmark in Table 3.

<div class="key" markdown="1">

*Table 2. Pre-flight checks that failed or warned for the team's scoring function.*

| Check | Result |
|---|---|
| D1 null-intervention parity | FAIL: the best knockout set exceeded no edit by 0.010 % |
| D2 landscape discrimination | FAIL: 20 candidates within one measurement band |
| D3 scalarisation degeneracy | FAIL: one product at every weight |
| D4–D6 | WARN |

</div>

The verdict was NOT USABLE and no proposals were issued ([Software](software)).

*Table 3. Search methods on a synthetic landscape of 10 genes with up to 3 knockouts (20 seeds).*

| Method | Finds exact best | Evaluations |
|---|---|---|
| Brute force | 100 % | 175 |
| Greedy | 65 % | 23 |
| Reinforcement learning | 10 % | 1,204 |

## Life cycle assessment headline {#6-life-cycle-assessment-headline}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

A screening life cycle assessment suggests that, in use, the candidate coolant could emit less carbon than a commercial one on a high-carbon grid, but not on a cleaner grid. Making it emits more per kilogram in both cases. The study has not been independently reviewed. **[computed]**
</div>

In this screening-level study, methyl myristate emitted 5,012 kg CO₂-eq per server-year in use, against 6,071 kg CO₂-eq for an ester-based coolant (−17 %), at an ecoinvent India grid factor of about 1.6 kg CO₂-eq kWh⁻¹. At the CEA factor of 0.716 kg CO₂-eq kWh⁻¹, the optimised process emitted 14 % more than the ester-based coolant. Production per kg was higher for methyl myristate in both cases. The study has not undergone an ISO 14044 critical review. [Life Cycle Assessment](life-cycle-assessment)

## Setbacks and lessons {#what-went-wrong-and-what-we-learned}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Several early results turned out to be weaker than they looked: a ranking with almost no margin, a structure prediction that depended on setup, and a learning method that lost to a simple loop. **[computed]**
</div>

- The first ranking appeared authoritative but carried no information (margin 0.010 %). The relevant threshold is the resolution of the assay, not the tolerance of the solver.
- Unconstrained Boltz-2 placed the fatty acid poorly in the first run but near the catalytic cysteine in a rerun, so no claim is made either way.
- Three standard remedies (UFF minimisation, sculpting, mutagenesis wizard) did not resolve the M1251 overlap seen in the first runs; the reruns did not show it.
- A reinforcement-learning agent was outperformed by a twenty-line greedy loop.
- The metabolic model could not represent the intended intervention until a reaction was added by hand.

## Status of validation {#not-yet-validated}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

No laboratory data exist, the key mutation is an assumption, and several analyses are unfinished. **[pending]**
</div>

Figure A summarises the status of each step.

<figure class="figure my-4 key">
  <img src="/static/figures/explainer_validation_status.png" class="figure-img img-fluid" alt="Table of six rows, Sequence to Process, and four columns: literature, computed, hypothesis and pending, each filled with short entries or none. An orange bar states that no wet-lab data exist for any step.">
  <figcaption class="figure-caption"><strong>Figure A.</strong> Validation status of each step: what rests on literature, what was computed here, what is a hypothesis and what is pending. No step has wet-lab data. Entries are taken from the step pages and follow their status labels. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

- No wet-lab data. No molecular dynamics. No formal proximity cut-off or cross-model consensus.
- The V1254W route to C14 in *S. cerevisiae* is an assumption.
- The knockout screen has not been repeated with the early-release reaction, and the growth penalty has not been computed.
- The two FBA analyses differ in conditions and are being reconciled.

## Next steps {#next-steps}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Planned work: repeat the main analyses with the new reaction, quantify growth costs, finish the structural controls, test the model against published results, and choose between two candidate coolants. **[pending]**
</div>

Planned work: repeat the frontier and knockout screen with the early-release reaction; compute growth penalties; finish the structural controls and report per-residue confidence; compare the model with published literature outcomes; and decide between methyl and isopropyl myristate.
