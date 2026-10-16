<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed. **None of the values on this page has been validated against wet-lab data.**
</div>

## Step 6. Process level {#process}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Heat-flow simulations suggest the candidate coolant, methyl myristate, keeps a 1,200 W server below 85 °C at a lower flow than two reference coolants. A screening life cycle assessment gives a footprint that depends on the electricity grid, and a separate comparison favours a related ester on practical grounds. All of this is modelled. **[computed]**
</div>

This step connects the strain to its intended use. Full detail is given on the [Life Cycle Assessment](life-cycle-assessment) page; the modelling components are summarised here.

## Summary of process-level analyses {#summary}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Three analyses were run: a heat-flow simulation, a screening life cycle assessment and a coolant comparison. None has been tested experimentally, and the choice between the two candidate coolants has not been recorded. **[pending]**
</div>

- **Computational fluid dynamics (CFD) [computed].** Seventeen OpenFOAM simulations (chtMultiRegionFoam, steady state, three-dimensional conjugate heat transfer, constant fluid properties) were run for a 1,200 W server immersed in each coolant. At the same flow (0.42 m/s), the hottest component reached 78.1 °C with methyl myristate, compared with 87.2 °C (mineral oil) and 88.0 °C (ester-based coolant). Methyl myristate remained below 85 °C at 0.27 m/s, whereas the other two coolants required 0.80 m/s.
- **Life cycle assessment (LCA) [computed, screening level].** The production footprint of methyl myristate per kilogram was far higher than that of the commercial coolants at present, whereas in use it can reduce cooling electricity. Whether the net result favours methyl myristate depends on the grid carbon factor. Caveats are given on the Life Cycle Assessment page.
- **Coolant selection [computed, data-limited].** A separate comparison of methyl myristate and isopropyl myristate rated methyl myristate about 9 % higher on thermal figures of merit, a difference within the estimated uncertainty. Isopropyl myristate was recommended on operability grounds, because methyl myristate melts at about 18 °C, which leaves about 2 °C of margin at a 20 °C inlet. Neither ester can be certified for energised immersion until dielectric breakdown voltage, volume resistivity and pour point have been measured. **[pending]** The team's decision between the two has not been recorded on this site.

---

**Previous:** [Step 5 Trust](trust) · **Next:** [Life Cycle Assessment](life-cycle-assessment)
