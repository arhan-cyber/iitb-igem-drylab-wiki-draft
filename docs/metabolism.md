<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Labels: **[computed]** our own run; **[literature]** published source; **[hypothesis]** reasoned, untested; **[pending]** not finished. **None of the numbers on this page is validated against wet-lab data.**
</div>

## Step 4. Metabolism-wide level {#metabolism}


**Question.** *What C14:0 can the cell reach, at what cost to growth, and by which route?*

### Feasibility frontier (analysis A) **[computed]**

In unmodified Yeast9, wild-type yeast already exports pure C14:0 at any growth up to 90% of normal, with no genetic edits. Purity never limits; growth trades off linearly against yield.

| Growth held at | C14:0 export (mmol/gDW/h) | C14:0 share of exported fatty acid |
|---|---|---|
| 10% of wild type | 0.211 | 100% |
| 25% | 0.178 | 100% |
| 50% | 0.119 | 100% |
| 75% | 0.060 | 100% |
| 90% | 0.024 | 100% |

An independently written earlier pipeline gave 0.209152 at or above 10% growth, against 0.2108 here (0.8% apart).

<figure class="figure my-4">
  <img src="/static/figures/feasibility_frontier.png" class="figure-img img-fluid" alt="Line chart of maximum C14 export against growth held, falling from 0.211 at 10 percent to 0.024 at 90 percent. Wild type and two knockout sets overlap; sets containing POX1 are at zero.">
  <figcaption class="figure-caption">No knockout improves on wild-type C14:0 production. FAA1, and DGA1+FAA1+LRO1, equal no edit; FAA1+FAA4 is 2% below; any set containing POX1 gives exactly zero. Model run without the early-release reaction.</figcaption>
</figure>

### Same envelope, second analysis (analysis B) **[computed]**

Under analysis B's conditions (see [Data](model#m3)), maximum export with a minimum growth requirement:

| Minimum growth (% of max) | Min growth rate (h⁻¹) | Max C14 export (mmol/gDW/h) |
|---|---|---|
| none | 0 | 0.25001 |
| 10% | 0.00977 | 0.22649 |
| 25% | 0.02442 | 0.19036 |
| 50% | 0.04884 | 0.12719 |
| 75% | 0.07326 | 0.06359 |
| 90% | 0.08791 | 0.02544 |
| 100% | 0.09768 | 0 |

At maximum growth the model exports no C14, and the minimum possible export is zero at every growth rate, so **C14 production is not growth-coupled**. The values are consistently about 6–7% higher than analysis A because the conditions differ; the shape is the same. The "no growth requirement" row is not a capacity shown for a growing culture.

### The route **[computed]**

At 50% growth every step of one route carries identical flux (0.1192 mmol/gDW/h), which identifies it as a single unbranched path:

C16:0 → (r_0402) hexadecanoyl-CoA → (r_0123, acyl-CoA oxidase, *POX1*) → (r_2251) enoyl-CoA hydratase → (r_0102) myristoyl-CoA → (r_0412) free C14:0 → export.

The model makes C14:0 by removing one two-carbon unit from C16:0 through beta-oxidation, not by ending synthesis early. *POX1* catalyses the committed step, which is why deleting it gives exactly zero. Robustness checks: forbidding reversal of the ATP-driven ligase step lowers production by only 2% (0.1192 → 0.1167); loopless FBA returns identical flux. Blocking r_0102 (analysis B) lowers export at the 50% growth floor from 0.12719 to 0.10977, and the model switches to an alternative route (degradation of C18:1 to C12 then re-elongation); blocking both abolishes C14 export.

Our original plan was to knock down degradation to preserve C14:0. In this model degradation is the only source of C14:0 without the new reaction, so the strategy is inverted relative to what the model predicts.

### Knockout and blocking screen (analysis B) **[computed]**

- All 1,143 single-gene deletions screened in both ligase scenarios: 965 viable, 178 lethal (lethal = no positive biomass flux; a computational classification, not a prediction of cell death). None forced myristate export at the deleted strain's own maximum growth.
- Deleting *POX1*, *FOX2*, *POT1*, *PXA1* or *PXA2* abolished modelled C14 export, because the C14-producing routes depend on peroxisomal beta-oxidation. *FAS1*, *FAS2*, *ACC1* and *OLE1* deletions were lethal under the specified medium.
- Blocking individual C14-consuming reactions (r_0125, r_0105, r_2155, r_2195/r_2201, r_2220) changed nothing at 50% growth, because all carried zero flux at that optimum.

### Consistency checks **[computed]**

The biomass reaction r_2111 and the biomass pseudo-reaction r_4041 carry identical flux at every solution (the biomass metabolite has exactly one producer and one consumer), so using either gives the same results; r_2111 is used throughout, being the model's own default objective.

### Growth-rate penalty **[pending]**

The penalty of an intervention is (1 − μ<sub>max,i</sub> / μ<sub>max,WT</sub>) × 100, where μ<sub>max,WT</sub> is the maximum growth rate of the unmodified model and μ<sub>max,i</sub> that after intervention *i*. The unrestricted growth penalty of each intervention has not yet been calculated.

### Reachable set and frontier **[computed]**

The same model supports a reachable-set analysis for a fatty-acid *profile*, not only for C14 amount. The plot below is for an illustrative C14-rich target; the target is an assumption, not a measurement.

<figure class="figure my-4">
  <img src="/static/figures/reachable_c14.png" class="figure-img img-fluid" alt="Left: curve of best achievable distance to the target profile against minimum total fatty-acid titre, flat near zero until a knee at 0.118 and then rising, with an unreachable region shaded above the maximum titre. Right: stacked bars showing fatty-acid composition at selected points on the frontier.">
  <figcaption class="figure-caption">Reachable set and frontier for an illustrative C14-rich target, Yeast9. The knee at 0.118 mmol/gDW/h is the largest titre within the assay's tie band of the target. Model-implied upper bounds; no wet-lab validation.</figcaption>
</figure>

---

**Previous:** [Step 3 Bridge](bridge) · **Next:** [Step 5 Trust](trust)
