
<div class="alert alert-warning" role="alert" markdown="1">
**Screening-level study, not critically reviewed.** The study has not undergone an ISO 14044 critical review[@iso14044|requirement for critical review] and should not be used for public comparative claims. Several inputs are placeholders (listed [below](#limitations-and-open-items)). The result depends on the grid carbon factor, as shown in the results section. It should be read as a method and a first estimate, not as a verdict.
</div>

## Goal and scope {#why-this-study}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

A screening life cycle assessment compared the candidate bio-based coolant, methyl myristate, with two commercial coolant families. Its aim is to show which production steps matter and what would be needed to match the existing products. It is a first estimate, not a verdict. **[computed]**
</div>

Air cooling is approaching its limits as data-centre power density rises, and single-phase immersion cooling is an alternative. The incumbent dielectric fluids each carry a liability: fluorinated fluids (PFAS) face phase-out under the proposed EU universal PFAS restriction,[@rivm_pfas|proposal submitted by five national authorities and published by ECHA on 7 February 2023] whereas ester-based and mineral-oil-based coolants are made largely from fossil feedstocks. The team is engineering *Saccharomyces cerevisiae* to produce methyl myristate (MM), a C14 fatty acid methyl ester, as a bio-based, biodegradable, halogen-free dielectric fluid. This study assesses how MM compares with the incumbents.

**Objectives.** (1) To compare the impacts of MM with those of two commercial coolant families, ester-based and mineral-oil-based, using the same database, method and process detail. (2) To identify the fermentation and downstream steps that drive the impacts of MM, in order to guide strain and process design. (3) To test the productivity, energy integration and renewable energy that MM requires to match the incumbents. Isopropyl myristate, named in an earlier scope draft, has not been modelled.

## Functional units, system boundary and methods {#method}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Two measures were used: one kilogram of coolant, and cooling one 1,200 W server for a year. The second matters because the fluids need different pumping power. The study follows the ISO life cycle assessment standards and uses ecoinvent data. **[computed]**
</div>

**Functional units.** FU-1: 1 kg of finished coolant at the plant gate (cradle-to-gate). FU-2: cooling of one 1,200 W server for one year (8,760 h), with the hottest component at or below 85 °C and coolant supply at 25 °C, covering production plus use-phase cooling electricity. Per-kg results alone ignore that the fluids require different flow rates and pumping energy to cool the same server. The IT electricity of the server (10,512 kWh yr⁻¹) is identical for every coolant and was excluded.

<figure class="figure my-4">
  <img src="/static/figures/lca_boundary.jpg" class="figure-img img-fluid" alt="Flow diagram: feedstocks, fermentation, downstream, then methyl myristate at plant gate; below, the use phase is modelled; packaging, transport and end of life are drawn dashed as not yet modelled.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> System boundary: cradle-to-gate production plus use-phase cooling electricity. Packaging, transport and end of life are not modelled (dashed). Figure from the life cycle assessment report; screening-level study.</figcaption>
</figure>

*Table 1. Methodological choices.*

| Choice | What was used |
|---|---|
| Standards | ISO 14040:2006[@iso14040|framework followed] and ISO 14044:2006[@iso14044] |
| Software | openLCA 2.6.2,[@openlca|software] product systems auto-linked with "prefer default providers" |
| Background database | ecoinvent 3.9.1,[@wernet2016|ecoinvent database] cut-off system model; Indian datasets first, then RoW, then GLO |
| Impact method | Environmental Footprint (EF) 3.1 (16 midpoint categories),[@andreasi2023|EF 3.1 characterisation factors] copy extended with PFHxA characterisation factors for PFAS |
| Allocation (MM) | Economic allocation at distillation column DC-1 between the C14-rich distillate (16.5 %) and the heavy fatty acid methyl ester co-product (83.5 %); mass allocation (about 10 %) as sensitivity |
| Cut-off | Flows under 1 % of unit-process mass or energy may be excluded unless toxic; excluded total under 5 %; capital goods excluded |

**Foreground data.** Most MM data originate from the team's process flow design: a 100 m³ reactor giving 45.6 kg of MM (98.5 % purity) per batch, sugarcane molasses followed by AFEX-pretreated corn stover hydrolysate, and in-situ transesterification with sulfuric acid and methanol. Where ecoinvent has no dataset (nine materials, including linear alpha-olefin, boron trifluoride, trimethylolpropane, p-toluenesulfonic acid, a PFAS additive and corn stover), a proxy process was built from the industrial reaction stoichiometry. Use-phase data were taken from 17 OpenFOAM CFD simulations of an immersion tank run by the team.

**Allocation.** Without allocation, the entire burden falls on MM (3,830 kg CO₂-eq kg⁻¹); economic allocation gives 632 and mass allocation about 394 kg CO₂-eq kg⁻¹. Economic allocation was retained because it is the stricter choice for MM. The market prices behind the 16.5 % factor still require a cited source.

**PFAS.** MM, the ester-based coolant and both mineral-oil-based coolants contain no PFAS. A clearly labelled hypothetical comparator with a fluorinated additive was modelled for illustration only. Midpoint methods score emissions but not persistence or accumulation, which are the reasons for the restriction of PFAS, and PFAS content is therefore reported as a separate hazard indicator.

## Impact assessment results {#results}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Making methyl myristate emits far more carbon per kilogram than the commercial coolants, but it needs much less pumping power in use. Whether the total is lower depends on how carbon-intensive the local electricity is: lower by 17 % on one grid factor, 14 % higher on another. **[computed]**
</div>

<figure class="figure my-4 key">
  <img src="/static/figures/lca_summary.jpg" class="figure-img img-fluid" alt="Horizontal stacked bars of kilograms of CO2-equivalent per server-year: methyl myristate optimised process 5,011 (minus 17 percent), after process steps 1 to 3 about 4,399 (minus 28 percent), ester-based coolant 6,071, mineral oil 6,055 (placeholder).">
  <figcaption class="figure-caption"><strong>Figure 2.</strong> Climate impact per server-year at an ecoinvent India grid factor of about 1.6 kg CO₂-eq kWh⁻¹. The mineral-oil bar uses a placeholder (about 1.5 kg kg⁻¹); the bar for process steps 1 to 3 is an estimate. Figure from the life cycle assessment report; the figure shows 5,011 where the report text gives 5,012, a rounding difference. Screening-level; not critically reviewed.</figcaption>
</figure>

### Per kilogram (cradle-to-gate) **[computed]**

Climate-change results per kilogram are given in Table 2.

<div class="key" markdown="1">

*Table 2. Cradle-to-gate climate impact per kilogram of coolant (kg CO₂-eq kg⁻¹).*

| | Value |
|---|---|
| MM baseline process | 632 |
| MM optimised process (openLCA, 14 October) | 449 |
| MM with planned process steps 1–3 | about 270 (estimate) |
| Ester-based coolants | 5.17–5.25 |
| Mineral-oil-based coolants | about 1.5 (placeholder) to 3.00 (synthetic grade) |

</div>

Per kilogram, MM exceeded the commercial coolants by a large margin. Process energy (about 95 % of the footprint, led by methanol recovery) is the hotspot. Reduction of methanol to 20 mL g⁻¹, heat integration and gentler cell disruption lower the value to about 270; higher lipid and C14 content per cell would lower it further. The per-kg gap is probably overstated because MM data are scaled from laboratory and design calculations whereas commercial data originate from mature plants.

### Per server-year: dependence on the grid factor **[computed]**

MM required about one third of the flow of the ester-based coolant (0.27 against 0.80 m s⁻¹) and 26 times less pump power (6.1 against 158.9 W). This saved about 1,600 kWh of cooling electricity per year, and the value of that saving depends on the carbon intensity of the electricity (Table 3).

<div class="key" markdown="1">

*Table 3. Climate impact of MM relative to the ester-based coolant, per server-year, chiller case, for three MM process variants. The two grid cases are shown side by side.*

| MM vs ester-based coolant, per server-year, chiller | Baseline (632) | Optimised (449) | Steps 1–3 (about 270) |
|---|---|---|---|
| Base case: ecoinvent India grid, about 1.6 kg CO₂-eq kWh⁻¹ (derived, not read directly from ecoinvent) | −7 % | −17 % | −28 % |
| Sensitivity: CEA grid-average factor 0.716 kg CO₂-eq kWh⁻¹ | +37 % | **+14 %** | −9 % |

</div>

The ranking reversed with the grid factor because the advantage of MM lies in electricity not used. On a low-carbon grid the production footprint of MM weighs more and process improvements become essential. At the CEA factor, the optimised MM process repays its additional production impact in 9.3 years for a 20 L fill; it breaks even within a 5-year life only if the fill is below about 11 L per server or MM production falls below about 340 kg CO₂-eq kg⁻¹.

### Other indicators **[computed]**

MM was the best of the three coolants on 8 of 9 reported metrics; the exception was production per kg. The hottest server component at equal flow (0.42 m s⁻¹) reached 78.1 °C with MM against 87.2 °C (mineral oil) and 88.0 °C (ester-based). Partial power usage effectiveness (PUE) was 1.035 with free cooling. MM is about 93 % biogenic carbon, PFAS-free and readily biodegradable, and its end-of-life fossil CO₂ is far lower than that of mineral-oil-based coolants.

## Coolant selection: a separate analysis favours isopropyl myristate {#which-ester-a-separate-analysis-points-the-other-way}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

A separate comparison recommended a related ester, isopropyl myristate, mainly because methyl myristate melts at about 18 °C, which leaves little margin in a 20 °C coolant loop. The team has not recorded a decision, and this assessment covers methyl myristate only. **[pending]**
</div>

A coolant-selection comparison of methyl myristate and isopropyl myristate (IPM) rated MM about 9 % higher on thermal figures of merit, a margin within the uncertainty of the estimated heat capacity and conductivity. It nevertheless recommended IPM on operability grounds: MM melts at about 18 °C,[@pubchem_mm|reported melting points 18.5 and 19 °C] which leaves about 2 °C of margin at a 20 °C inlet, whereas IPM melts at about 3 °C.[@pubchem_ipm|reported melting point approximately 3 °C] The life cycle assessment also notes that MM melts at about 18.5 °C and that cold-start trace heating is not modelled. Neither ester can be certified for energised immersion until breakdown voltage, volume resistivity, dielectric loss and pour point have been measured. This life cycle assessment models MM only. **[pending]** The team's decision between the two esters.

## Consistency with the metabolic model {#how-this-links-to-the-rest-of-our-model}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The assessment does not yet match the metabolic model in three ways: it borrows a fatty-acid profile from another yeast, assumes a different sugar, and models the ester form while the metabolic model predicts the free acid. These must be reconciled. **[pending]**
</div>

The output of the yeast strain enters the life cycle assessment as MM. Three links are not yet consistent with the metabolic model: (1) the assessment borrows a fatty-acid profile from the *Yarrowia* I1220W result, which is the assumption that the [Model](model#m4) identifies as unsupported in *S. cerevisiae*; (2) it assumes xylose use from corn-stover hydrolysate, whereas the flux balance analysis (FBA) optimises free C14:0 on glucose; (3) the FBA predicts free myristate, whereas the life cycle assessment models methyl myristate, so the esterification step must be stated. **[pending]** The borrowed profile should be replaced with the lipid content and C14 share measured for the team strain.

## Limitations and open items {#limitations-and-open-items}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Several inputs are placeholders or known to be wrong, packaging, transport and end of life are not modelled, and no independent review has been done. The results are therefore a screening estimate. **[pending]**
</div>

The list below comprises the open items of the report plus items found in review.

- The exact ecoinvent grid factor should be read from a 1 kWh openLCA run (currently about 1.6, derived) and used as the base case.
- Mineral oil should be exported from openLCA and the 1.5 kg kg⁻¹ placeholder replaced.
- The in-vivo scenario should be rerun; its current value (629 against about 575 expected) is known to be wrong and must not be published.
- The PFAS proxy in the ester-based coolant should be set to zero and the export repeated (the 14 October export still included it; effect under 0.01 kg CO₂-eq kg⁻¹).
- The tank fill should be taken from the simulation geometry (20 L and a 5-year life are placeholders).
- The optimised process (DC-2, VD-1, HR-1, BC-1 changes) should be linked and steps 1–3 rerun with fossil methanol.
- The commercial coolants should be run at 0.65 and 0.70 m s⁻¹ to bracket their true minimum flow.
- The market prices behind the 16.5 % allocation should be cited, and the mass-allocation share resolved (10.3 % in one place, 9.9 % in another).
- A sensitivity (tornado) analysis should be added; packaging, transport and end of life modelled; and isopropyl myristate modelled.
- Internal references and file names should be replaced with public sources, and an ISO 14044 critical review obtained if comparative claims are to be made.

## Acknowledgements {#acknowledgements}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Access to the ecoinvent database and guidance on the bioprocess analysis came from Prof. Yogendra Shastri of IIT Bombay.
</div>

Access to ecoinvent 3.9.1 and guidance on the bioprocess analysis were provided by Prof. Yogendra Shastri, Department of Chemical Engineering, IIT Bombay.
