
<div class="alert alert-warning" role="alert" markdown="1">
**Screening-level study, not critically reviewed.** It has not had an ISO 14044 critical review and should not be used for public comparative claims. Several inputs are placeholders (listed [below](#limitations-and-open-items)). The result depends on the grid carbon factor, as shown in the results section. Read it as a method and a first estimate, not a verdict.
</div>

## Why this study

Air cooling is reaching its limits as data-centre power density rises, and single-phase immersion cooling is a leading alternative. The incumbent dielectric fluids each carry a liability: fluorinated fluids (PFAS) face phase-out under the proposed EU universal PFAS restriction; ester-based and mineral-oil-based coolants are made largely from fossil feedstocks. Our team is engineering *S. cerevisiae* to produce methyl myristate (MM), a C14 fatty acid methyl ester, as a bio-based, biodegradable, halogen-free dielectric fluid. This study asks how it compares.

**Objectives.** (1) Compare MM's impacts against two commercial coolant families, ester-based and mineral-oil-based, using the same database, method and process detail. (2) Find which fermentation and downstream steps drive MM's impacts, to guide strain and process design. (3) Test what productivity, energy integration and renewable energy MM needs to match the incumbents. Isopropyl myristate, named in an earlier scope draft, has not been modelled yet.

## Method

**Two functional units.** FU-1: 1 kg of finished coolant at the plant gate (cradle-to-gate). FU-2: cooling one 1,200 W server for one year (8,760 h), hottest component at or below 85 °C, coolant supply at 25 °C, covering production plus use-phase cooling electricity. Per-kg results alone ignore that the fluids need different flow rates and pumping energy to cool the same server. The server's own IT electricity (10,512 kWh/yr) is identical for every coolant and is excluded.

<figure class="figure my-4">
  <img src="/static/figures/lca_boundary.jpg" class="figure-img img-fluid" alt="Flow diagram: feedstocks, fermentation, downstream, then methyl myristate at plant gate; below, the use phase is modelled; packaging, transport and end of life are drawn dashed as not yet modelled.">
  <figcaption class="figure-caption">Modelled boundary: cradle-to-gate production plus use-phase cooling electricity. Packaging, transport and end of life are not yet modelled. Figure from the LCA report.</figcaption>
</figure>

| Choice | What was used |
|---|---|
| Standards | ISO 14040:2006 and ISO 14044:2006 |
| Software | openLCA 2.6.2, product systems auto-linked with "prefer default providers" |
| Background database | ecoinvent 3.9.1, cut-off system model; Indian datasets first, then RoW, then GLO |
| Impact method | EF 3.1 (16 midpoint categories), copy extended with PFHxA characterisation factors for PFAS |
| Allocation (MM) | Economic at distillation column DC-1 between the C14-rich distillate (16.5%) and the heavy FAME co-product (83.5%); mass allocation (about 10%) as sensitivity |
| Cut-off | Flows under 1% of unit-process mass or energy may be excluded unless toxic; excluded total under 5%; capital goods excluded |

**Foreground data.** Most MM data come from the team's process flow design: a 100 m³ reactor giving 45.6 kg of MM (98.5% purity) per batch, sugarcane molasses then AFEX-pretreated corn stover hydrolysate, in-situ transesterification with sulfuric acid and methanol. Where ecoinvent has no dataset (nine materials, including linear alpha-olefin, boron trifluoride, trimethylolpropane, p-toluenesulfonic acid, a PFAS additive and corn stover) a proxy process was built from the industrial reaction stoichiometry. Use-phase data come from 17 OpenFOAM CFD simulations of an immersion tank run by the team.

**Allocation matters.** Without allocation all burden falls on MM (3,830 kg CO₂-eq/kg); economic allocation gives 632; mass allocation gives about 394. Economic allocation was kept because it is the stricter choice for MM. The market prices behind the 16.5% factor still need a cited source.

**PFAS.** MM, the ester-based coolant and both mineral-oil-based coolants contain no PFAS. A clearly labelled hypothetical comparator with a fluorinated additive was modelled for illustration only. Midpoint methods score emissions, not persistence or accumulation, which are the reasons PFAS are being restricted, so PFAS content is reported as a separate hazard indicator.

## Results

<figure class="figure my-4">
  <img src="/static/figures/lca_summary.jpg" class="figure-img img-fluid" alt="Horizontal stacked bars of kilograms of CO2-equivalent per server-year: methyl myristate optimised process 5,011 (minus 17 percent), after process steps 1 to 3 about 4,399 (minus 28 percent), ester-based coolant 6,071, mineral oil 6,055 (placeholder).">
  <figcaption class="figure-caption">Climate impact per server-year at an ecoinvent India grid factor of about 1.6 kg CO₂-eq/kWh. The mineral-oil bar uses a placeholder (about 1.5 kg/kg); the "steps 1 to 3" bar is an estimate. Figure from the LCA report; the figure shows 5,011 where the report text says 5,012, a rounding difference.</figcaption>
</figure>

### Per kilogram (cradle-to-gate, kg CO₂-eq/kg) **[computed]**

| | Value |
|---|---|
| MM baseline process | 632 |
| MM optimised process (openLCA, 14 October) | 449 |
| MM with planned process steps 1–3 | about 270 (estimate) |
| Ester-based coolants | 5.17–5.25 |
| Mineral-oil-based coolants | about 1.5 (placeholder) to 3.00 (synthetic grade) |

**Per kilogram, MM is far worse than the commercial coolants today.** Its process energy (about 95% of its footprint, led by methanol recovery) is the hotspot. Cutting methanol to 20 mL/g, heat integration and gentler cell disruption take it to about 270; more lipid and C14 per cell take it further. The per-kg gap is probably overstated because MM data are scaled from lab and design calculations while commercial data come from mature plants.

### Per server-year: the result depends on the grid factor **[computed]**

MM needs about one third of the flow of the ester-based coolant (0.27 vs 0.80 m/s) and 26 times less pump power (6.1 W vs 158.9 W). That saves about 1,600 kWh of cooling electricity a year, and the value of that saving depends on how carbon-intensive the electricity is.

| MM vs ester-based coolant, per server-year, chiller | Baseline (632) | Optimised (449) | Steps 1–3 (about 270) |
|---|---|---|---|
| Base case: ecoinvent India grid, about 1.6 kg CO₂-eq/kWh (derived, not read directly from ecoinvent) | −7% | −17% | −28% |
| Sensitivity: CEA grid-average factor 0.716 kg CO₂-eq/kWh | +37% | **+14%** | −9% |

The ranking flips with the grid factor because MM's advantage is electricity it does not use. On a low-carbon grid, MM's production footprint matters more and the process improvements become essential. At the CEA factor, the optimised MM process repays its extra production impact in 9.3 years for a 20 L fill; it breaks even within a 5-year life only if the fill is below about 11 L per server or MM production falls below about 340 kg CO₂-eq/kg.

### Where MM does well **[computed]**

MM is the best of the three coolants on 8 of 9 reported metrics; the one it loses is production per kg. The hottest server component at equal flow (0.42 m/s) reaches 78.1 °C with MM against 87.2 °C (mineral oil) and 88.0 °C (ester-based); partial PUE is 1.035 with free cooling; MM is about 93% biogenic carbon, PFAS-free and readily biodegradable, and its end-of-life fossil CO₂ is far lower than that of mineral-oil-based coolants.

## Which ester? A separate analysis points the other way

A coolant-selection comparison of methyl myristate and isopropyl myristate (IPM) scored MM about 9% higher on thermal figures of merit, a margin inside the uncertainty of estimated heat capacity and conductivity. It nonetheless recommended **IPM**, on operability: MM melts at about 18 °C, leaving about 2 °C of margin at a 20 °C inlet, while IPM melts at about 3 °C. The LCA also notes that MM melts at about 18.5 °C and that cold-start trace heating is not modelled. Neither ester can be certified for energised immersion until breakdown voltage, volume resistivity, dielectric loss and pour point are measured. This LCA models MM only. **[pending]** The team's decision between the two esters.

## How this links to the rest of our dry lab

The yeast strain's output enters the LCA as MM. Three links are not yet consistent with the metabolic model: (1) the LCA borrows a fatty-acid profile from the *Yarrowia* I1220W result, which is the assumption our [Model](model#m4) flags as unsupported in *S. cerevisiae*; (2) it assumes xylose use from corn-stover hydrolysate, while the FBA optimises free C14:0 on glucose; (3) the FBA predicts free myristate, whereas the LCA models methyl myristate, so the esterification step must be stated. **[pending]** Replace the borrowed profile with the team strain's measured lipid content and C14 share.

## Limitations and open items

The report's own list, plus items found in review:

- Read the exact ecoinvent grid factor from a 1 kWh openLCA run (currently about 1.6, derived) and use it as the base case.
- Export mineral oil from openLCA and replace the 1.5 kg/kg placeholder.
- Re-run the in-vivo scenario; its current value (629 against about 575 expected) is known to be wrong and should not be published.
- Set the PFAS proxy in the ester-based coolant to zero and re-export (the 14 October export still carried it; effect under 0.01 kg CO₂-eq/kg).
- Take the tank fill from the simulation geometry (20 L and a 5-year life are placeholders).
- Link the optimised process (DC-2, VD-1, HR-1, BC-1 changes) and re-run steps 1–3 with fossil methanol.
- Run the commercial coolants at 0.65 and 0.70 m/s to bracket their true minimum flow.
- Cite the market prices behind the 16.5% allocation; resolve the mass-allocation share (10.3% in one place, 9.9% in another).
- Add a sensitivity (tornado) analysis; model packaging, transport and end of life; model isopropyl myristate.
- Replace internal references and file names with public sources; obtain an ISO 14044 critical review if comparative claims are to be made.

## Acknowledgements

Access to ecoinvent 3.9.1 and guidance on the bioprocess analysis were provided by Prof. Yogendra Shastri, Department of Chemical Engineering, IIT Bombay.
