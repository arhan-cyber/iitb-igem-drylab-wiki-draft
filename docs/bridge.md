<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Labels: **[computed]** our own run; **[literature]** published source; **[hypothesis]** reasoned, untested; **[pending]** not finished. **None of the numbers on this page is validated against wet-lab data.**
</div>

## Step 3. The bridge: representing the mutation in a metabolic model {#bridge}


**Question.** *Can Yeast9 represent early C14 release from FAS at all?*

**Finding.** Yeast9 represents fatty-acid synthase as reactions ending at C16:0-CoA and C18:0-CoA. It has no reaction for early C14 release. The model could therefore not represent the intervention we are building, and an earlier workaround added a myristate exchange by hand. We added a documented early-release reaction (`fbareduce_FAS_C14_release`) and re-ran the analysis. **[computed]**

**Result.** With the reaction ON, 100% of C14:0 comes from the new reaction and none from beta-oxidation. Maximum C14:0 export rises only **+2.6%** at 50% of wild-type growth (0.119191 → 0.122237 mmol/gDW/h; +3.1% at 10% growth, +2.6% at 90%).

<figure class="figure my-4">
  <img src="/static/figures/bridge_early_release.png" class="figure-img img-fluid" alt="Left: bars of maximum C14 export at 10, 50 and 90 percent growth, with and without the early-release reaction, nearly equal. Right: horizontal bars showing the change in C14 export when each resource is made free: NADPH plus 150.9 percent, ATP plus 36 percent, NGAM zero plus 7.6 percent, acetyl-CoA and malonyl-CoA plus 0.01 percent.">
  <figcaption class="figure-caption">The reaction changes the route, not the amount. Freeing carbon-chain supply does nothing; freeing NADPH raises C14 by 150.9%. Yeast9, glucose uptake 1.0, NGAM 0.7. Model-implied upper bounds.</figcaption>
</figure>

**Why so small.** Making free C14:0 directly from FAS saves cofactors relative to the beta-oxidation route that already exists, and the saving is small once that route's own credits are counted. Neither acetyl-CoA nor malonyl-CoA is limiting. The limits are glucose carbon (about 0.52 of the 1.0 glucose is committed to growth plus maintenance at 50% growth) and **NADPH (12 per C14)**, made in the oxidative pentose phosphate pathway at a carbon cost, with ATP second. With NADPH and ATP freely regenerated and no maintenance, the model reaches the carbon-conservation limit of 0.42857 mmol/gDW/h (1/2.333), so the gap to the achieved yield is entirely cofactor cost.

<div class="alert alert-secondary" role="alert" markdown="1">
**Caveat.** The reaction is a modelling hypothesis about what V1254W does. It inherits assumption A1. Also, the frontier and knockout screen in Step 4 were run on the model **without** the reaction. Re-running them with it is **[pending]**.
</div>

**Gaps and naming in Yeast9 found along the way** (from our model comparison). Yeast9 was chosen over Yeast8 because it represents more of the pathways we need. Genes flagged as absent: *PEX11* (beta-oxidation) and *ATR1*, *CYP94C1* (ω-oxidation). *FOX1* is present as *POX1*, a naming mismatch with the same function. A hypothesis, not yet run, is that omitting the two ω-oxidation genes costs little yield. **[pending]**

---

**Previous:** [Step 2 FAS interaction](fas-interaction) · **Next:** [Step 4 Metabolism](metabolism)
