
<div class="alert alert-warning" role="alert" markdown="1">
Every result below is a statement about a model and is **not validated against wet-lab data**. Full methods, assumptions and numbers: [Model](model).
</div>

## Summary of findings

1. **Wild-type yeast already makes pure C14:0 in the model, at a growth cost that is linear.** No knockout improves on it. [Details](model#metabolism)
2. **The model makes C14:0 only by shortening C16:0 through beta-oxidation.** *POX1* is the committed step. [Details](model#metabolism)
3. **A FAS early-release reaction raises C14:0 by only +2.6%.** The limit is NADPH, not chain supply. [Details](model#bridge)
4. **The ScFAS2 site equivalent to the *Yarrowia* chain-length residue is V1254.** M1251 is excluded; the effect of V1254W in *S. cerevisiae* is an assumption. [Details](model#sequence)
5. **Our own scoring failed its checks.** Best knockout beat doing nothing by 0.010%; the tool issued no proposals. [Details](model#trust)
6. **A learned search lost to a trivial one.** Brute force and greedy beat reinforcement learning. [Details](model#trust)
7. **The coolant case is mixed.** [Details](life-cycle-assessment)

## 1. What the model says is reachable

Maximum C14:0 export in Yeast9 as growth is held at a fraction of wild type (analysis A):

| Growth held at | C14:0 export (mmol/gDW/h) | Purity |
|---|---|---|
| 10% | 0.211 | 100% |
| 25% | 0.178 | 100% |
| 50% | 0.119 | 100% |
| 75% | 0.060 | 100% |
| 90% | 0.024 | 100% |

<figure class="figure my-4">
  <img src="/static/figures/feasibility_frontier.png" class="figure-img img-fluid" alt="Maximum C14 export falls linearly from 0.211 at 10 percent growth to 0.024 at 90 percent; wild type and two knockout sets overlap and POX1 sets are at zero.">
  <figcaption class="figure-caption">No knockout improves on wild type. Sets containing <em>POX1</em> give exactly zero.</figcaption>
</figure>

A second analysis under different conditions (glucose 1.1 mmol/gDW/h, strain BY4742) gives values about 6–7% higher with the same shape. Conditions are listed in [Model: Data](model#m3).

## 2. How C14:0 is made in the model

One unbranched route: C16:0 → hexadecanoyl-CoA → acyl-CoA oxidase (*POX1*) → enoyl-CoA hydratase → myristoyl-CoA → free C14:0 → export. Deleting *POX1* gives exactly zero. Loopless FBA and a forced one-way ligase change the result by at most 2%.

## 3. What changed in our plan

- We **dropped** the plan to knock down degradation to preserve C14:0: degradation is the only C14:0 source without early release.
- We **added** a FAS early-release reaction as a documented model modification: C14 +2.6% at 50% growth, limited by NADPH.
- We **excluded** M1251, C1305, F1646, G1250 and K1413–K1423 from mutagenesis and kept **V1254W** as the lead candidate.
- We **withheld** a ranked knockout list from the wet lab because checks D1 and D2 failed.

<figure class="figure my-4">
  <img src="/static/figures/bridge_early_release.png" class="figure-img img-fluid" alt="Left: C14 export with and without the early-release reaction at 10, 50 and 90 percent growth, nearly equal. Right: freeing NADPH raises C14 by 150.9 percent; freeing acetyl-CoA or malonyl-CoA changes it by 0.01 percent.">
  <figcaption class="figure-caption">The early-release reaction changes the route, not the amount; cofactors set the limit.</figcaption>
</figure>

## 4. Structural result: site and pocket

V1254 (ScFAS2) corresponds to I1220 (YlFAS), with a 34-residue offset and no gaps at or beside the key column. In the first constrained Boltz-2 runs C14 sat 4.35 Å from V1254 and 6.91 Å from M1260 and clashed with M1251 at 0.96–1.77 Å, which we read as a closed conformational gate (**[hypothesis]**). Reruns on the lab server did not reproduce the clash, and distances moved with the choice of constrained residues, so these numbers describe the setup as well as the pocket. [Details](model#structure)

## 5. Our scoring failed its own checks

| Check | Result |
|---|---|
| D1 null-intervention parity | FAIL: best beats no edit by 0.010% |
| D2 landscape discrimination | FAIL: 20 candidates inside one measurement band |
| D3 scalarisation degeneracy | FAIL: one product at every weight |
| D4–D6 | WARN |

Verdict: not usable; no proposals issued. [Software](software)

| 10 genes, up to 3 knockouts | Finds exact best | Evaluations |
|---|---|---|
| Brute force | 100% | 175 |
| Greedy | 65% | 23 |
| Reinforcement learning | 10% | 1,204 |

## 6. Life cycle assessment headline

Screening-level: in use, methyl myristate emits 5,012 kg CO₂-eq per server-year against 6,071 for an ester-based coolant (−17%) at an ecoinvent India grid factor of about 1.6 kg CO₂-eq/kWh. At the CEA factor 0.716 the optimised process is +14% worse than the ester. Production per kg is higher for methyl myristate in both cases. The study has had no ISO 14044 critical review. [Life Cycle Assessment](life-cycle-assessment)

## What went wrong and what we learned

- Our first ranking looked authoritative and was meaningless (0.010% margin). The threshold that matters is the assay's resolution, not the solver's.
- Unconstrained Boltz-2 placed the fatty acid poorly in the first run but near the catalytic cysteine in a rerun, so we make no claim either way.
- Three standard fixes (UFF minimisation, sculpting, mutagenesis wizard) did not resolve the M1251 clash seen in the first runs; the reruns did not show it.
- A reinforcement-learning agent lost to a twenty-line greedy loop.
- Our model could not represent our own intervention until we added a reaction by hand.

## Not yet validated

- No wet-lab data. No molecular dynamics. No formal proximity cutoff or cross-model consensus.
- The V1254W route to C14 in *S. cerevisiae* is an assumption.
- Knockout screen not yet re-run with the early-release reaction; growth penalty not computed.
- Two FBA analyses differ in conditions and are being reconciled.

## Next steps

Re-run the frontier and knockout screen with the early-release reaction; compute growth penalties; finish the structural controls and report per-residue confidence; check the model against published literature outcomes; decide between methyl and isopropyl myristate.
