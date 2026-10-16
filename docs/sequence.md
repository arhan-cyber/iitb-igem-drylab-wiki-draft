<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Labels: **[computed]** our own run; **[literature]** published source; **[hypothesis]** reasoned, untested; **[pending]** not finished. **None of the numbers on this page is validated against wet-lab data.**
</div>

## Step 1. Sequence level {#sequence}


**Question.** *Which ScFAS2 residue sits where Yarrowia I1220 sits?* Rigouin et al. 2017 identified I1220 in the fatty acid binding site of YlFAS as controlling chain length: replacing it with tryptophan raised C14 content to 11.6% of total lipid in stationary phase. **[literature]**

**Method.** EMBOSS Needle global pairwise alignment (BLOSUM62, gap open 10, extend 0.5) of YlFAS alpha (Q6C8H7, 1,852 aa) against ScFAS2 (P19097, 1,887 aa). Global alignment is used because the sequences differ in length, and insertions shift the numbering. **[computed]**

| ScFAS2 (P19097) | YlFAS | Relationship |
|---|---|---|
| M1251 | M1217 | Identical |
| V1254 | I1220 | Conservative; both β-branched aliphatic |
| M1260 | M1226 | Identical |

The three pairs are separated by a constant 34-residue offset from insertions in ScFAS2 upstream of the KS domain. There are no gaps at or beside the key column, so the V1254 ↔ I1220 equivalence does not depend on gap placement. The direct ScFAS2 analogue of the Rigouin mutation is therefore **V1254W**.

<figure class="figure my-4">
  <img src="/static/figures/alignment_strip.png" class="figure-img img-fluid" alt="Two rows of residue boxes: YlFAS M1217, I1220, M1226 above ScFAS2 M1251, V1254, M1260, joined by vertical lines labelled identical, conservative, identical.">
  <figcaption class="figure-caption">Equivalent positions from the Needle alignment (schematic). Transfer is by homology; the effect in <em>S. cerevisiae</em> is an assumption (A1).</figcaption>
</figure>

**How Rigouin placed the substrate, and what we could reuse.** Rigouin modelled the *Yarrowia* KS domain from three structures (2PFF, 2VKZ, 4V58), then superimposed it on *E. coli* KAS I bound to capric acid (1F91), copied the C10 chain into the equivalent pocket and extended it to C16. We have a better starting structure (8PRW, 1.9 Å), but it contains no fatty acid in the KS3 pocket, so ligand placement remained our task. **[computed, team review]**

**Conservation versus necessity.** A conservation filter would remove positions where mutation is likely destructive. Our three residues are conserved because they set chain length, which every fatty-acid-making organism selects for. The exclusion criterion we apply is therefore catalytic or mechanistic necessity, not conservation score alone.

**Status.** **[pending]** BLAST of the template against ScFAS2 (in review) and the conservation/phylogenetic analysis to identify segments to avoid. Identification of further mutation sites is blocked on the latter.

---

**Previous:** [Model overview](model) · **Next:** [Step 2 FAS interaction](fas-interaction)
