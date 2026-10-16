<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Labels: **[computed]** our own run; **[literature]** published source; **[hypothesis]** reasoned, untested; **[pending]** not finished. **None of the numbers on this page is validated against wet-lab data.**
</div>

## Step 6. Process level {#process}


This step connects the strain to its use. Full detail is on [Life Cycle Assessment](life-cycle-assessment); the modelling parts are summarised here.

- **CFD [computed].** 17 OpenFOAM simulations (chtMultiRegionFoam, steady state, 3-D conjugate heat transfer, constant fluid properties) of a 1,200 W server immersed in each coolant. At the same flow (0.42 m/s) the hottest component reaches 78.1 °C with methyl myristate against 87.2 °C (mineral oil) and 88.0 °C (ester-based coolant). Methyl myristate stays below 85 °C at 0.27 m/s; the others need 0.80 m/s.
- **LCA [computed, screening level].** Methyl myristate's production footprint per kg is far higher than the commercial coolants' today; in use it can save cooling electricity. Whether that nets out in its favour depends on the grid carbon factor. See the caveats on the Life Cycle Assessment page.
- **Coolant selection [computed, data-limited].** A separate comparison of methyl myristate and isopropyl myristate scored methyl myristate about 9% higher on thermal figures of merit, a margin inside the estimate uncertainty. It recommended **isopropyl myristate** on operability grounds because methyl myristate melts at about 18 °C, leaving about 2 °C of margin at a 20 °C inlet. Neither ester can be certified for energised immersion until dielectric breakdown voltage, volume resistivity and pour point are measured. **[pending]** The team's decision between the two is not recorded on this site.

---

**Previous:** [Step 5 Trust](trust) · **Next:** [Life Cycle Assessment](life-cycle-assessment)
