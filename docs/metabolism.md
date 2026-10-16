<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed. **None of the values on this page has been validated against wet-lab data.**
</div>

## Step 4. Whole-cell metabolic analysis {#metabolism}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Flux balance analysis, a way of calculating the most a cell's metabolism could produce, was applied to a genome-scale yeast model. The model makes myristic acid only by shortening longer fatty acids, output falls steadily as growth is required, and no gene deletion tested beat the unedited strain. **[computed]**
</div>

**Question.** Which quantity of C14:0 can the cell reach in the model, at what cost to growth, and by which route? The analyses used flux balance analysis (FBA)[@orth2010|FBA principles and assumptions] on Yeast9[@zhang2024|model used] with COBRApy[@ebrahim2013|software used]. Conditions of analysis B are given in the [Data](model#m3) section of the model overview.

## Feasibility frontier (analysis A) {#feasibility-frontier-analysis-a}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

In the unedited model, pure myristic acid can be exported at any growth up to 90 % of normal, and output falls in a straight line as more growth is required: 0.211 at 10 % growth to 0.024 at 90 % (mmol per gram dry weight per hour). **[computed]**
</div>

**[computed]** In unmodified Yeast9, the wild-type model exported pure C14:0 at any growth up to 90 % of the wild-type rate without genetic edits. Product purity was never limiting; growth traded off linearly against yield (Table 1, Figure 1).

<div class="key" markdown="1">

*Table 1. Maximum C14:0 export in unmodified Yeast9 at fixed fractions of the wild-type growth rate (analysis A).*

| Growth held at | C14:0 export (mmol gDW⁻¹ h⁻¹) | C14:0 share of exported fatty acid |
|---|---|---|
| 10 % of wild type | 0.211 | 100 % |
| 25 % | 0.178 | 100 % |
| 50 % | 0.119 | 100 % |
| 75 % | 0.060 | 100 % |
| 90 % | 0.024 | 100 % |

</div>

An independently written earlier pipeline gave 0.209152 at or above 10 % growth, compared with 0.2108 here (0.8 % apart).

<figure class="figure my-4">
  <img src="/static/figures/feasibility_frontier.png" class="figure-img img-fluid" alt="Line chart of maximum C14 export against growth held, falling from 0.211 at 10 percent to 0.024 at 90 percent. Wild type and two knockout sets overlap; sets containing POX1 are at zero.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> Maximum C14 export against the growth rate held, for wild type and selected knockout sets. No knockout set exceeded the wild-type maximum: FAA1, and DGA1 + FAA1 + LRO1, equalled the unedited strain; FAA1 + FAA4 was 2 % below it; any set containing <em>POX1</em> gave exactly zero. Model run without the early-release reaction; model-implied, not validated against wet-lab data.</figcaption>
</figure>

## Feasibility envelope under the conditions of analysis B {#same-envelope-second-analysis-analysis-b}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

A second analysis under slightly different conditions gave the same shape, with values 6–7 % higher. At full growth the model makes no myristic acid, so production does not come with growth for free. **[computed]**
</div>

**[computed]** Under the conditions of analysis B (see [Data](model#m3)), the maximum export with a minimum growth requirement is given in Table 2.

*Table 2. Maximum C14 export under a minimum growth requirement (analysis B).*

| Minimum growth (% of maximum) | Minimum growth rate (h⁻¹) | Maximum C14 export (mmol gDW⁻¹ h⁻¹) |
|---|---|---|
| none | 0 | 0.25001 |
| 10 % | 0.00977 | 0.22649 |
| 25 % | 0.02442 | 0.19036 |
| 50 % | 0.04884 | 0.12719 |
| 75 % | 0.07326 | 0.06359 |
| 90 % | 0.08791 | 0.02544 |
| 100 % | 0.09768 | 0 |

At maximum growth the model exported no C14, and the minimum possible export was zero at every growth rate; C14 production is therefore not growth-coupled. The values were consistently about 6–7 % higher than those of analysis A because the conditions differ; the shape is the same. The row without a growth requirement does not represent a capacity of a growing culture.

## Metabolic route to C14:0 {#the-route}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Without the added reaction, the model makes myristic acid only by chopping two carbons off palmitic acid (C16:0) in the peroxisome, so deleting the gene *POX1* removes it completely. The original plan of reducing breakdown is therefore inverted relative to what the model predicts. **[computed]**
</div>

**[computed]** At 50 % growth every step of one route carried identical flux (0.1192 mmol gDW⁻¹ h⁻¹), which identifies it as a single unbranched path:

C16:0 → (r_0402) hexadecanoyl-CoA → (r_0123, acyl-CoA oxidase, *POX1*) → (r_2251) enoyl-CoA hydratase → (r_0102) myristoyl-CoA → (r_0412) free C14:0 → export (Figure B).

<figure class="figure my-4">
  <img src="/static/figures/explainer_c14_route.png" class="figure-img img-fluid" alt="Vertical chain of seven boxes from C16:0 (palmitic acid) through hexadecanoyl-CoA, acyl-CoA oxidase (POX1, the committed step), enoyl-CoA hydratase, myristoyl-CoA and free C14:0 to export. Side notes give the ligase-reversal check, deletion of POX1, FOX2, POT1, PXA1 or PXA2 giving exactly zero, the r_0102 blocking result, and the consequence for the plan.">
  <figcaption class="figure-caption"><strong>Figure B.</strong> The single route to C14:0 in the model without early release, at 50 % of wild-type growth: C16:0, hexadecanoyl-CoA, acyl-CoA oxidase (<em>POX1</em>, the committed step), enoyl-CoA hydratase, myristoyl-CoA, free C14:0 and export. Deleting <em>POX1</em> gave exactly zero. Free C14:0, not methyl myristate, is modelled. Model-implied; not validated against wet-lab data.</figcaption>
</figure>

The model formed C14:0 by removing one two-carbon unit from C16:0 through β-oxidation, not by termination of synthesis. *POX1* catalyses the committed step, and its deletion therefore gave exactly zero. Robustness checks: forbidding reversal of the ATP-driven ligase step lowered production by 2 % (0.1192 to 0.1167 mmol gDW⁻¹ h⁻¹), and loopless FBA returned identical flux. Blocking r_0102 (analysis B) lowered export at the 50 % growth floor from 0.12719 to 0.10977 mmol gDW⁻¹ h⁻¹, and the model switched to an alternative route (degradation of C18:1 to C12 followed by re-elongation); blocking both reactions abolished C14 export.

The original plan was to reduce degradation in order to preserve C14:0. In this model, degradation is the only source of C14:0 in the absence of the early-release reaction, so the strategy is inverted relative to the model prediction.

## Knockout and blocking screen (analysis B) {#knockout-and-blocking-screen-analysis-b}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

All 1,143 single-gene deletions were screened in the model. None forced myristic acid export, and removing genes for peroxisomal fat breakdown abolished it. **[computed]**
</div>

**[computed]**

- All 1,143 single-gene deletions were screened in both ligase scenarios: 965 were viable and 178 lethal (lethal denotes no positive biomass flux, a computational classification and not a prediction of cell death). None forced myristate export at the maximum growth rate of the deleted strain.
- Deletion of *POX1*, *FOX2*, *POT1*, *PXA1* or *PXA2* abolished modelled C14 export, because the C14-producing routes depend on peroxisomal β-oxidation. Deletions of *FAS1*, *FAS2*, *ACC1* and *OLE1* were lethal in the specified medium.
- Blocking individual C14-consuming reactions (r_0125, r_0105, r_2155, r_2195/r_2201, r_2220) changed nothing at 50 % growth, because all carried zero flux at that optimum.

## Consistency checks {#consistency-checks}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Two ways of writing the cell's growth in the model gave identical results, so one was used throughout. **[computed]**
</div>

**[computed]** The biomass reaction r_2111 and the biomass pseudo-reaction r_4041 carried identical flux in every solution (the biomass metabolite has exactly one producer and one consumer), so either gives the same results. Reaction r_2111 was used throughout, being the default objective of the model.

## Growth-rate penalty {#growth-rate-penalty}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

A measure of how much each intervention slows growth has been defined but not yet calculated. **[pending]**
</div>

**[pending]** The penalty of an intervention is defined as (1 − μ<sub>max,i</sub> / μ<sub>max,WT</sub>) × 100, where μ<sub>max,WT</sub> is the maximum growth rate of the unmodified model and μ<sub>max,i</sub> that after intervention *i*. The unrestricted growth penalty of each intervention has not been calculated.

## Reachable set and frontier {#reachable-set-and-frontier}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The same model can also map which fatty-acid mixtures are reachable. The example uses an illustrative target, not a measurement, so it demonstrates the method and does not predict a result. **[computed]**
</div>

**[computed]** The same model supports a reachable-set analysis for a fatty-acid profile and not only for the amount of C14. Figure 2 shows the result for an illustrative C14-rich target; the target is an assumption and not a measurement.

<figure class="figure my-4">
  <img src="/static/figures/reachable_c14.png" class="figure-img img-fluid" alt="Left: curve of best achievable distance to the target profile against minimum total fatty-acid titre, flat near zero until a knee at 0.118 and then rising, with an unreachable region shaded above the maximum titre. Right: stacked bars showing fatty-acid composition at selected points on the frontier.">
  <figcaption class="figure-caption"><strong>Figure 2.</strong> Left: best achievable distance to an illustrative C14-rich target profile against the minimum total fatty-acid titre (Yeast9); the shaded region is unreachable. Right: fatty-acid composition at selected points on the frontier. The knee at 0.118 mmol gDW⁻¹ h⁻¹ is the largest titre within the assay's tie band of the target. Model-implied upper bounds; not validated against wet-lab data.</figcaption>
</figure>

---

**Previous:** [Step 3 Bridge](bridge) · **Next:** [Step 5 Trust](trust)
