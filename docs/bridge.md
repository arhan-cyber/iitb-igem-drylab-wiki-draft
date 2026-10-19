<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed. **None of the values on this page has been validated against wet-lab data.**
</div>

## Step 3. Representation of the mutation in a metabolic model {#bridge}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The genome-scale yeast model had no way to represent a fatty acid synthase that releases 14-carbon chains early, so one was added. It raised the model's maximum myristic acid output by only 2.6 %, because the limiting resource is a cofactor (NADPH), not the carbon supply. **[computed]**
</div>

**Question.** Can Yeast9[@zhang2024|genome-scale metabolic model of *S. cerevisiae*] represent early C14 release from fatty acid synthase (FAS)?

**Finding.** Yeast9 represents FAS as reactions that terminate at C16:0-CoA and C18:0-CoA and contains no reaction for early C14 release. The model therefore could not represent the intended intervention, and an earlier workaround added a myristate exchange reaction by hand. A documented early-release reaction (`fbareduce_FAS_C14_release`) was added and the analysis was repeated. **[computed]**

## Effect of the early-release reaction {#effect-of-the-early-release-reaction}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

With the new reaction switched on, all of the model's C14 comes from it rather than from breaking down longer fatty acids. Maximum C14 export increased by 2.6 % at half of wild-type growth. Supplying more NADPH would raise it by 150.9 %. **[computed]**
</div>

**Result.** With the reaction active, 100 % of C14:0 originated from the added reaction and none from β-oxidation. Maximum C14:0 export increased by 2.6 % at 50 % of wild-type growth (0.119191 to 0.122237 mmol gDW⁻¹ h⁻¹; +3.1 % at 10 % growth and +2.6 % at 90 %). The sensitivity of C14 export to the availability of individual resources is shown in Figure 1; Figure A summarises the reaction and its effect.

<figure class="figure my-4">
  <img src="/static/figures/explainer_bridge_early_release.png" class="figure-img img-fluid" alt="Flow chart. Yeast9 as published has FAS reactions ending at C16:0-CoA and C18:0-CoA and no early C14 release. An added early-release reaction, a hypothesis that inherits assumption A1, switches the C14 source: all C14:0 then comes from the added reaction. The result box gives +2.6 % maximum C14 export at 50 % of wild-type growth. A bar panel shows NADPH +150.9 % far above ATP +36 %, maintenance +7.6 % and acetyl-CoA or malonyl-CoA +0.01 %.">
  <figcaption class="figure-caption"><strong>Figure A.</strong> Yeast9 has no early C14 release from FAS, so a reaction was added (a modelling hypothesis that inherits assumption A1). With it, all C14:0 comes from the added reaction and maximum export rose 2.6 % at 50 % of wild-type growth; freeing NADPH would raise it 150.9 %, ATP 36 %, maintenance 7.6 % and acetyl-CoA or malonyl-CoA 0.01 %. The Step 4 analyses were run without this reaction. Model-implied upper bounds; not validated against wet-lab data.</figcaption>
</figure>

<figure class="figure my-4 key">
  <img src="/static/figures/bridge_early_release.png" class="figure-img img-fluid" alt="Left: bars of maximum C14 export at 10, 50 and 90 percent growth, with and without the early-release reaction, nearly equal. Right: horizontal bars showing the change in C14 export when each resource is made free: NADPH plus 150.9 percent, ATP plus 36 percent, NGAM zero plus 7.6 percent, acetyl-CoA and malonyl-CoA plus 0.01 percent.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> Left: maximum C14 export at 10, 50 and 90 % of wild-type growth with and without the early-release reaction. Right: change in maximum C14 export when each resource was made unconstrained (NADPH +150.9 %; ATP +36 %; non-growth-associated maintenance (NGAM) set to zero +7.6 %; acetyl-CoA and malonyl-CoA +0.01 %). The reaction changed the route, not the amount. Yeast9, glucose uptake 1.0 mmol gDW⁻¹ h⁻¹, NGAM 0.7. Model-implied upper bounds; not validated against wet-lab data.</figcaption>
</figure>

## Origin of the small effect {#why-so-small}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

In the model, the early-release route saves little compared with the route that already existed. The real limits are the glucose supply and the NADPH needed to build the chain. **[computed]**
</div>

Direct formation of free C14:0 from FAS saved cofactors relative to the β-oxidation route already present in the model, and the saving was small once the credits of that route were included. Neither acetyl-CoA nor malonyl-CoA was limiting. The limits were glucose carbon (about 0.52 of the 1.0 mmol gDW⁻¹ h⁻¹ glucose uptake was committed to growth and maintenance at 50 % growth) and NADPH (12 per C14), which is produced in the oxidative pentose phosphate pathway at a carbon cost; ATP was second. With NADPH and ATP freely regenerated and no maintenance, the model reached the carbon-conservation limit of 0.42857 mmol gDW⁻¹ h⁻¹ (1/2.333), so the gap between this limit and the achieved yield is attributable entirely to cofactor cost.

## Limitations and model gaps {#limitations-and-model-gaps}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The added reaction is a modelling hypothesis about what V1254W does, and the later knockout screen was run without it. Several genes were also missing or named differently in the model. **[hypothesis]**
</div>

<div class="alert alert-secondary" role="alert" markdown="1">
**Caveat.** The reaction is a modelling hypothesis about the effect of V1254W and inherits assumption A1; a reaction added by assumption cannot show that the real mutation has the intended effect. The Step 4 results are from the model as released, with no added reaction, and stand on their own; repetition with the reaction is **[pending]**.
</div>

**Gaps and naming in Yeast9 identified during the work** (from the team's model comparison). Yeast9 was chosen over Yeast8 because it represents more of the required pathways. The following genes were flagged as absent: *PEX11* (β-oxidation), *ATR1* and *CYP94C1* (ω-oxidation). *FOX1* is present as *POX1*, a naming mismatch for the same function. It is hypothesised, but has not been tested, that omission of the two ω-oxidation genes has little effect on yield. **[pending]**

---

**Previous:** [Step 2 FAS interaction](fas-interaction) · **Next:** [Step 4 Metabolism](metabolism)
