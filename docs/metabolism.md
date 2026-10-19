<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed. **None of the values on this page has been validated against wet-lab data.**
</div>

## Step 4. Whole-cell metabolic analysis {#metabolism}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Flux balance analysis, a way of calculating the most a cell's metabolism could produce, was applied to a genome-scale yeast model. The model makes myristic acid only by breaking down longer fatty acids, output falls steadily as growth is required, and no gene deletion tested beat the unedited strain. **[computed]**
</div>

**Question.** Which quantity of C14:0 can the cell reach in the model, at what cost to growth, and by which route? The analyses used flux balance analysis (FBA)[@orth2010|FBA principles and assumptions] on Yeast-GEM v9.1.1[@zhang2024|model used] with COBRApy[@ebrahim2013|software used]. Run conditions are given in the [Data](model#m3) section of the model overview. The quantity throughout is free-myristate (C14:0) export; methyl myristate is not in the model. Two ligase scenarios are reported: the primary scenario, with the fatty-acid-CoA ligases restricted to the activating direction, and a sensitivity case with the bounds as shipped in the model.

## Feasibility frontier {#feasibility-frontier-analysis-a}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

In the unedited model, myristic acid can be exported at any growth below the maximum, and output falls as more growth is required: 0.226 at 10 % of maximum growth to 0.025 at 90 % (mmol per gram dry weight per hour). At maximum growth the model makes none, so production always costs growth. **[computed]**
</div>

**[computed]** The unmodified model exported free C14:0 at every growth rate below its maximum without genetic edits. Growth traded off against yield (Table 1, Figure 1).

<div class="key" markdown="1">

*Table 1. Maximum free-myristate export under a minimum growth requirement (BY4742, glucose uptake 1.1 mmol gDW⁻¹ h⁻¹, unlimited O₂). Maximum growth is 0.09768 h⁻¹ in the primary scenario and 0.09769 h⁻¹ with shipped bounds.*

| Minimum growth | Growth rate (h⁻¹) | Primary: forward-only | Sensitivity: shipped bounds |
|---|---|---|---|
| none | 0 | 0.25001 | 0.25692 |
| 10 % of maximum | 0.00977 | 0.22649 | 0.23274 |
| 25 % | 0.02442 | 0.19036 | 0.19647 |
| 50 % | 0.04884 | 0.12719 | 0.13156 |
| 75 % | 0.07326 | 0.06359 | 0.06578 |
| 90 % | 0.08791 | 0.02544 | 0.02631 |
| 100 % | 0.09768 | 0 | 0 |

</div>

At maximum growth the model exported no C14, and the minimum export was zero at every growth rate, so production is not growth-coupled. The row without a growth requirement is a zero-growth limit, not a capacity of a growing culture. The shipped-bounds values are 2.7–3.3 % higher because those bounds permit a reverse ligase flux that regenerates ATP.

<figure class="figure my-4">
  <img src="/static/figures/fig2_validation_envelope.png" class="figure-img img-fluid" alt="Two panels. Left: predicted against measured maximum growth at four chemostat dilution rates, all four model points below the 1:1 line by 5 to 11 percent, with a shaded plus or minus 10 percent band. Right: maximum free-myristate export falling linearly from about 0.25 at zero growth to zero at 0.0977 per hour, for forward-only and shipped-bounds scenarios, with the minimum at zero everywhere.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> (a) Predicted against measured growth in glucose-limited chemostats of the industrial strain DS28911.[@vanhoek1998|measured growth and uptake rates in glucose-limited chemostats] The model under-predicts at all four points by 5–11 %, two of them outside the ±10 % criterion set in advance; the strain is not BY4742, so this is a plausibility check, not a validation. (b) Production envelope in both ligase scenarios; the minimum is zero at every growth rate. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

## Metabolic route to C14:0 {#the-route}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Without the added reaction, the model makes myristic acid by chopping two carbons off palmitic acid (C16:0) in the peroxisome. A second route exists and is used only when that one is blocked, and both depend on fat breakdown, so deleting the gene *POX1* removes C14 completely. The original plan of reducing breakdown is therefore inverted relative to what the model predicts. **[computed]**
</div>

**[computed]** At the production optimum every step of the route that carried flux had the same value, which identifies it as a single unbranched path. Written with the reaction identifiers of Yeast-GEM v9.1.1:

C16:0-CoA in the peroxisome → (r_0123, acyl-CoA oxidase, *POX1*) → (r_2251, 2-enoyl-CoA hydratase, *FOX2*) → (r_2268, 3-hydroxyacyl-CoA dehydrogenase, *FOX2*) → (r_0102, thiolase, *POT1*) → myristoyl-CoA → free C14:0 → (r_1772) → (r_1777) → export (r_2193) (Figure B).

Peroxisomal C16:0-CoA comes from fatty acid synthase (r_2140) through the transporter r_2221. Release depends on the ligase scenario: in the primary scenario the thioesterase *TES1* (r_0848) carries the whole product flux and deleting it abolishes export, whereas the shipped bounds let the model run the C14 ligase r_0412 backwards — thermodynamically questionable, and the only reason *TES1* appears dispensable. The final transport step r_1777 has no gene association, so secretion is a model assumption (A7).

<figure class="figure my-4">
  <img src="/static/figures/fig1_c14_routes.png" class="figure-img img-fluid" alt="Compartment diagram with cytosol, peroxisome, ER membrane and outside the cell. Blue route A: fatty acid synthase makes C16:0-CoA, which is transported into the peroxisome and shortened to C14:0-CoA by POX1, FOX2 and POT1. Green route B: C18:0-CoA is desaturated and degraded to C12, re-elongated to C14:0-CoA in the ER membrane and returned to the peroxisome. TES1 releases myristate, which leaves through r_1772, r_1777 and r_2193. A dashed orange box marks direct C14:0 release by FAS2 V1254W as intended but not in the model, and a dashed grey box marks methyl myristate as not modelled.">
  <figcaption class="figure-caption"><strong>Figure B.</strong> The two routes to C14:0 in the model. Route A (blue), one round of peroxisomal β-oxidation shortening C16:0-CoA, carries the flux at every optimum examined. Route B (green), degradation of C18:1 to C12 and re-elongation in the endoplasmic reticulum, is used when r_0102 is blocked. Free myristate is released by <em>TES1</em> (r_0848) in the primary scenario and leaves through the gene-less transporter r_1777. Dashed: the intended direct release of C14:0 by FAS2 V1254W and the ex-cell formation of methyl myristate, neither of which the model represents. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

The model formed C14:0 by removing one two-carbon unit from C16:0 through β-oxidation, not by termination of synthesis. *POX1* catalyses the committed step, and its deletion therefore gave exactly zero. Robustness checks: forbidding reversal of the ATP-driven ligase step lowered maximum export by 2.7 % with no growth requirement and by 3.1–3.3 % at growth floors of 25–90 %, and loopless FBA reproduced the same optima. Blocking r_0102 lowered export at the 50 % growth floor from 0.12719 to 0.10977 mmol gDW⁻¹ h⁻¹, and the model switched to the second route; blocking both r_0102 and r_2154 abolished C14 export, so these are the only two routes the network contains.

The original plan was to reduce degradation in order to preserve C14:0. In this model, degradation is the only source of C14:0 in the absence of the early-release reaction, so the strategy is inverted relative to the model prediction.

## Knockout and blocking screen {#knockout-and-blocking-screen-analysis-b}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

All 1,143 single-gene deletions were screened in the model, together with pairs, triples and a 13-member stack. None raised export, and removing genes for peroxisomal fat breakdown abolished it. **[computed]**
</div>

**[computed]**

- All 1,143 single-gene deletions were screened in both ligase scenarios: 965 were viable and 178 lethal (lethal denotes no positive biomass flux, a computational classification and not a prediction of cell death). None forced myristate export at the maximum growth rate of the deleted strain. At the 50 % growth floor the primary scenario gave 884 candidates with export unchanged, 43 reduced and 7 abolished; the sensitivity scenario gave 883, 45 and 6.
- Deletion of *POX1*, *FOX2*, *POT1*, *PXA1* or *PXA2* abolished modelled C14 export, because the C14-producing routes depend on peroxisomal β-oxidation. The genome-wide pass added *MDH3*, which reoxidises the NADH that β-oxidation generates inside the peroxisome. Deletion of *TES1* abolished export in the primary scenario, where it is the only release step. Deletions of *FAS1*, *FAS2*, *ACC1* and *OLE1* were lethal in the specified medium.
- Blocking individual C14-consuming reactions (r_0125, r_0105, r_2155, r_2195/r_2201, r_2220) changed nothing at 50 % growth, because all carried zero flux at that optimum.
- Combinations behaved the same way: of 189 pairs, 133 were neutral and 56 reduced export, and none beat its best single member; all 200 triples and the 13-member stack were neutral in the primary scenario. In the ranking of 432 candidates, 356 of the 427 viable ones tied with the unmodified strain.
- No tested intervention raised the modelled export optimum. With the objective and the growth floor held fixed, a deletion or block leaves the mutant a subset of the wild-type flux space, so its maximum can only match or fall below the unmodified strain; the large tie follows from that formulation and is not evidence that those strains would behave alike in a real cell. The result also does not transfer to designs scored a different way, such as product flux read at the growth optimum.

<figure class="figure my-4">
  <img src="/static/figures/fig3_single_interventions.png" class="figure-img img-fluid" alt="Two panels. Left: horizontal bars of maximum export retained at the 50 percent growth floor for 37 curated interventions in both ligase scenarios; no bar exceeds 100 percent, 19 interventions are neutral, and deletions of TES1, FOX2, POT1, POX1, PXA1 and PXA2 give zero. Right: growth penalties, with block r_0112 at 3.53 percent and the rest at or below 0.75 percent.">
  <figcaption class="figure-caption"><strong>Figure 2.</strong> Single interventions at the 50 % growth floor. Left, maximum export retained as a percentage of the unmodified strain in the same scenario; no intervention exceeds it, and those that abolish export are marked. Right, the growth penalty of each in the primary scenario. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

<figure class="figure my-4">
  <img src="/static/figures/fig5_combinations_ranking.png" class="figure-img img-fluid" alt="Two panels. Left: a heat map of export loss for every evaluated pair of the 23 shortlisted interventions, with losses following the precursor member of the pair and the darkest cells at redundant supply routes. Right: maximum growth against maximum export for the 427 viable candidates, with 356 coinciding at a single circled point and the rest below or to the left of it, none above.">
  <figcaption class="figure-caption"><strong>Figure 3.</strong> Combined interventions at the 50 % growth floor. Left, export loss for every evaluated pair of the shortlisted interventions. Right, maximum growth against maximum export for the viable candidates; 356 coincide with the unmodified strain at the circled point and none lies above it. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

**Supply constraints.** Capping a supply reaction at half its flux at the optimum reduced export by 53.2 % for *ACC1* (malonyl-CoA), 17.3 % for *ACS1*/*ACS2* (acetyl-CoA) and 2.2 % for *ZWF1*/*GND* (NADPH); *ACC1* is essential. Raising these caps did not increase export, because none binds at the optimum — a sensitivity result, not a model of enzyme over-expression, which would need enzyme-constrained modelling or measurement. Oxygen is unlimited here; capping it at 2.0 mmol gDW⁻¹ h⁻¹ cost 12.9 % of export at the 50 % floor in the primary scenario and 4.7 % in the sensitivity case, and nothing without a growth requirement (Figure 4).

<figure class="figure my-4">
  <img src="/static/figures/fig4_sensitivity.png" class="figure-img img-fluid" alt="Three panels. Left: maximum export against the cap on a supply reaction, with ACC1 falling steeply to zero, ACS1 and ACS2 intermediate, and the two NADPH routes nearly flat. Middle: molar yield at half of maximum growth rising gently across glucose uptakes from 0.3 to 10. Right: maximum export against an oxygen uptake cap, flat above about 2.5 and falling sharply below it when growth is required.">
  <figcaption class="figure-caption"><strong>Figure 4.</strong> Sensitivity of free-myristate export. (a) Export at the 50 % growth floor when a supply reaction is capped at a fraction of its flux at the optimum; × marks the growth floor becoming infeasible. (b) Molar yield at half of each condition's own maximum growth across glucose uptakes. (c) Export against an oxygen uptake cap, with and without a growth requirement. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

## Consistency checks {#consistency-checks}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Two ways of writing the cell's growth in the model gave identical results, so one was used throughout. **[computed]**
</div>

**[computed]** The biomass reaction r_2111 and the biomass pseudo-reaction r_4041 carried identical flux in every solution (the biomass metabolite has exactly one producer and one consumer), so either gives the same results. Reaction r_2111 was used throughout, being the default objective of the model.

## Growth-rate penalty {#growth-rate-penalty}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

How much each intervention slows growth has been calculated for the 37 curated interventions. Most cost nothing; the largest among the viable ones is 3.5 %. **[computed]**
</div>

**[computed]** The penalty of an intervention is defined as (1 − μ<sub>max,i</sub> / μ<sub>max,WT</sub>) × 100, where μ<sub>max,WT</sub> is the maximum growth rate of the unmodified model and μ<sub>max,i</sub> that after intervention *i*. Of the 37 curated interventions, 4 were lethal (*fas1*Δ, *fas2*Δ, *acc1*Δ, *ole1*Δ) and 33 viable, of which 29 carried no penalty; the rest were *zwf1*Δ 0.41 %, blocking r_0889 0.41 %, *mae1*Δ 0.75 % and blocking r_0112 3.53 %. Each was evaluated against growth floors set as fractions of the unmodified strain's maximum, so a slow-growing deletion is not rewarded with a lower demand. Penalties for the genome-wide screen have not been tabulated here. **[pending]**

## Reachable set and frontier {#reachable-set-and-frontier}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The same model can also map which fatty-acid mixtures are reachable. The example uses an illustrative target, not a measurement, so it demonstrates the method and does not predict a result. **[computed]**
</div>

**[computed]** The same model supports a reachable-set analysis for a fatty-acid profile and not only for the amount of C14. Figure 5 shows the result for an illustrative C14-rich target; the target is an assumption and not a measurement.

<figure class="figure my-4">
  <img src="/static/figures/reachable_c14.png" class="figure-img img-fluid" alt="Left: curve of best achievable distance to the target profile against minimum total fatty-acid titre, flat near zero until a knee at 0.118 and then rising, with an unreachable region shaded above the maximum titre. Right: stacked bars showing fatty-acid composition at selected points on the frontier.">
  <figcaption class="figure-caption"><strong>Figure 5.</strong> Left: best achievable distance to an illustrative C14-rich target profile against the minimum total fatty-acid titre (Yeast9); the shaded region is unreachable. Right: fatty-acid composition at selected points on the frontier. The knee at 0.118 mmol gDW⁻¹ h⁻¹ is the largest titre within the assay's tie band of the target. Model-implied upper bounds; not validated against wet-lab data.</figcaption>
</figure>

---

**Previous:** [Step 3 Bridge](bridge) · **Next:** [Step 5 Trust](trust)
