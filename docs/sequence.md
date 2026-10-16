<div class="alert alert-secondary" role="alert" markdown="1">
Part of the [model](model). Status labels: **[computed]** produced in this study; **[literature]** taken from a published source; **[hypothesis]** reasoned but untested; **[pending]** not completed. **None of the values on this page has been validated against wet-lab data.**
</div>

## Step 1. Residue correspondence between YlFAS and ScFAS2 {#sequence}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

A published mutation in a related yeast (*Yarrowia lipolytica*) changes the length of the fatty acids it makes. Aligning the two proteins' sequences showed that the matching position in baker's yeast is V1254, so V1254W is the candidate mutation. That the same change works in baker's yeast is an assumption. **[computed]**
</div>

**Question.** Which residue of *Saccharomyces cerevisiae* fatty acid synthase subunit 2 (ScFAS2) occupies the position of I1220 in the *Yarrowia lipolytica* enzyme (YlFAS)? Rigouin et al. identified I1220 in the fatty acid binding site of YlFAS as a determinant of chain length; the I1220W substitution increased C14 to 11.6 % of total fatty acids.[@rigouin2017|I1220W and C14 at 11.6 % of total fatty acids (abstract)] **[literature]**

**Method.** The YlFAS α chain (UniProt Q6C8H7, 1,852 aa) was aligned globally with ScFAS2 (UniProt P19097, 1,887 aa) using EMBOSS Needle[@madeira2022|EMBOSS Needle web service][@needleman1970|global alignment algorithm] (BLOSUM62, gap opening penalty 10, gap extension penalty 0.5). A global alignment was chosen because the sequences differ in length and insertions shift the residue numbering. **[computed]**

## Aligned positions {#aligned-positions}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Three positions line up between the two enzymes with a constant offset of 34 residues and no gaps beside the key position. The proposed ScFAS2 counterpart of the *Yarrowia* mutation is V1254W. **[computed]**
</div>

The aligned positions are listed in Table 1 and shown schematically in Figure 1.

<div class="key" markdown="1">

*Table 1. Equivalent positions in ScFAS2 (UniProt P19097) and YlFAS (UniProt Q6C8H7) from the EMBOSS Needle alignment.*

| ScFAS2 (P19097) | YlFAS | Relationship |
|---|---|---|
| M1251 | M1217 | Identical |
| V1254 | I1220 | Conservative; both β-branched aliphatic |
| M1260 | M1226 | Identical |

</div>

The three pairs are separated by a constant offset of 34 residues, which arises from insertions in ScFAS2 upstream of the ketoacyl synthase (KS) domain. No gaps occur at or beside the key column, so the V1254 ↔ I1220 equivalence does not depend on gap placement. The direct ScFAS2 analogue of the I1220W substitution is therefore V1254W. Transfer of the effect between species is by homology; its occurrence in *S. cerevisiae* is an assumption (A1).

<figure class="figure my-4">
  <img src="/static/figures/alignment_strip.png" class="figure-img img-fluid" alt="Two rows of residue boxes: YlFAS M1217, I1220, M1226 above ScFAS2 M1251, V1254, M1260, joined by vertical lines labelled identical, conservative, identical.">
  <figcaption class="figure-caption"><strong>Figure 1.</strong> Equivalent positions from the Needle alignment (schematic; the data are those of Table 1). Transfer is by homology; the effect in <em>S. cerevisiae</em> is an assumption (A1). Not validated against wet-lab data.</figcaption>
</figure>

## Basis for ligand placement and for exclusion criteria {#basis-for-ligand-placement}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

The published approach placed a fatty acid in the enzyme by copying it from a bacterial structure. The available yeast structure has no fatty acid bound, so placement had to be predicted. Positions were excluded for catalytic or mechanistic reasons, not because they are conserved. **[computed]**
</div>

**Ligand placement in the published approach.** Rigouin et al. modelled the *Yarrowia* KS domain from three structures (PDB 2PFF, 2VKZ and 4V58), superimposed it on *Escherichia coli* β-ketoacyl-ACP synthase I (KAS I) with bound capric acid (PDB 1F91), copied the C10 chain into the equivalent pocket and extended it to C16. The starting structure used here (PDB 8PRW, resolution 1.9 Å) has no fatty acid in the KS3 pocket, so ligand placement had to be predicted (Step 2). **[computed, team review]**

**Conservation and necessity.** A conservation filter would remove positions at which mutation is likely to be destructive. The three residues considered here are conserved because they set chain length, a property that every fatty-acid-producing organism requires; conservation score alone is therefore not a suitable exclusion criterion. The criterion applied was catalytic or mechanistic necessity.

## Status of this step {#status}

<div class="brief" markdown="1">
<div class="brief-h">In brief</div>

Two analyses are not finished: a further sequence search and an analysis of which regions of the protein should not be changed. Finding more mutation sites is blocked until the second is done. **[pending]**
</div>

**[pending]** A BLAST search of the template against ScFAS2 (in review) and a conservation and phylogenetic analysis to identify segments that should not be mutated. Identification of further mutation sites depends on the latter.

---

**Previous:** [Model overview](model) · **Next:** [Step 2 FAS interaction](fas-interaction)
