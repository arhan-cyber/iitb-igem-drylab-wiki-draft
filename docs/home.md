
<div class="alert alert-warning" role="alert" markdown="1">
**Draft status.** This site presents our dry-lab results as they currently stand. All results are statements about models. **None has been validated against wet-lab data.** Where something is unfinished, we say so on the page.
</div>

## What this dry lab did

Our team is engineering *Saccharomyces cerevisiae* to make a C14:0-rich fatty-acid product (myristic acid) that can be turned into methyl myristate, a bio-based immersion coolant for data centres. The dry lab asked one question at three scales and then asked whether the answer was worth trusting and worth making:

1. **Sequence.** Which residue in the yeast fatty acid synthase (FAS) controls chain length?
2. **FAS interaction.** Does the enzyme's binding pocket hold a C14 chain, and which residues must we leave alone?
3. **Bridge.** Can a genome-scale metabolic model represent that mutation at all?
4. **Metabolism.** What can the whole cell reach, at what cost to growth, and by which route?
5. **Trust.** Does our scoring of candidate designs measure anything, and is a learned search better than a simple one?
6. **Process.** Is the product worth making, and how does it compare with other coolants?

<figure class="figure my-4">
  <img src="/static/figures/overview_story.png" class="figure-img img-fluid" alt="Six boxes in a row, left to right: Sequence, FAS interaction, Bridge, Metabolism, Trust, Process. Each box states the question, the key result and the status.">
  <figcaption class="figure-caption">The six steps and what each hands to the next. Key assumption behind steps 1 to 3: a FAS2 point mutation can release C14 in <em>S. cerevisiae</em>. This is an assumption, not an established result.</figcaption>
</figure>

## Where to read what

| If you want… | Go to |
|---|---|
| Methods, assumptions, data, parameters, limits, in full | [Model](model) |
| The headline findings and what they changed | [Results](results) |
| The design cycle we went through | [Engineering](engineering) |
| The tool other teams can run on their own models | [Software](software) |
| What we offer to the community | [Contribution](contribution) |
| The coolant life cycle assessment | [Sustainability](sustainability) |

## How to read the status labels

Every claim on this site carries one of four labels:

- **[computed]** we ran it and the numbers come from our own code or documents.
- **[literature]** taken from a published source, cited.
- **[hypothesis]** a reasoned explanation we have not yet tested.
- **[pending]** planned or in progress; no result yet.

## Three things to know first

1. **The headline result is mostly negative, and useful.** In our metabolic model no gene knockout improves C14:0 production over wild type, and our own scoring setup failed its checks. We report both.
2. **The mutation route is an assumption.** That a FAS2 point mutation can release C14 in *S. cerevisiae* is supported by a *Yarrowia lipolytica* result, not by *S. cerevisiae* data. All downstream numbers are conditional on it.
3. **The coolant case is not settled.** Our screening LCA favours methyl myristate in use under some assumptions and not others, and a separate coolant-selection analysis recommends isopropyl myristate on operability grounds. See [Sustainability](sustainability).

