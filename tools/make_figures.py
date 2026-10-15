"""Draw the infographics that did not exist yet.

Every number below is copied from a team document (source noted next to it).
Nothing here is new data. Run with a Python that has matplotlib:

    python tools/make_figures.py

Output goes to static/figures/ (local preview only, see README_DRYLAB.md).
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent.parent / "static" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

BLUE, GREEN, ORANGE, RED, GREY, INK = "#2a74d4", "#2e8b57", "#e8693a", "#b03a2e", "#8a8f98", "#1b1f24"
FOOT = "Model-implied upper bounds; not validated against wet-lab data."


def box(ax, x, y, w, h, title, body, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.02",
                                fc="white", ec=color, lw=2))
    ax.text(x + w / 2, y + h - 0.045, title, ha="center", va="top", fontsize=11.5,
            fontweight="bold", color=color)
    ax.text(x + w / 2, y + h - 0.13, body, ha="center", va="top", fontsize=8.6, color=INK,
            linespacing=1.35)


def overview():
    fig, ax = plt.subplots(figsize=(16, 6.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0.5, 0.96, "One story, six steps: from a residue to a coolant", ha="center",
            fontsize=18, fontweight="bold", color=INK)
    ax.text(0.5, 0.905, "Each step hands one result to the next. Status shown under every step.",
            ha="center", fontsize=11, color=GREY)
    tiers = [
        ("1  Sequence", "Which residue sets\nchain length?\n\nScFAS2 V1254 matches\nYlFAS I1220\n(34-residue offset)", "BLAST and conservation\nanalysis still open", BLUE),
        ("2  FAS interaction", "Does the KS pocket\nhold a C14 chain?\n\nBoltz-2, 5 models;\nM1251 clashes\n(0.96 to 1.77 A)", "No MD, no wet-lab\ncheck yet", BLUE),
        ("3  Bridge", "Can the model\nrepresent the mutation?\n\nEarly-release reaction\nadded to Yeast9:\nC14 +2.6%", "Limit is NADPH,\nnot carbon", GREEN),
        ("4  Metabolism", "What can the cell reach?\n\nNo knockout beats\nwild type; one\nbeta-oxidation route", "Yeast9 FBA;\nupper bounds only", GREEN),
        ("5  Trust", "Does 'best' mean\nanything?\n\nPre-flight failed our\nown scoring: best beat\nno-edit by 0.010%", "Search benchmark on a\nsynthetic landscape", ORANGE),
        ("6  Process", "Is it worth making,\nand how green?\n\nLCA + CFD of the\nmethyl myristate\ncoolant", "Screening level; not\ncritically reviewed", RED),
    ]
    w, gap, x0, y0, h = 0.135, 0.03, 0.02, 0.36, 0.42
    for i, (t, b, s, c) in enumerate(tiers):
        x = x0 + i * (w + gap)
        box(ax, x, y0, w, h, t, b, c)
        ax.text(x + w / 2, y0 - 0.04, s, ha="center", va="top", fontsize=8.4, color=GREY, style="italic")
        if i < len(tiers) - 1:
            ax.annotate("", xy=(x + w + gap - 0.004, y0 + h / 2), xytext=(x + w + 0.004, y0 + h / 2),
                        arrowprops=dict(arrowstyle="-|>", color=GREY, lw=2))
    ax.text(0.5, 0.05, "Key assumption behind steps 1 to 3: a FAS2 point mutation can release C14 in "
            "S. cerevisiae. This is an assumption, not an established result.",
            ha="center", fontsize=10, color=RED)
    fig.savefig(OUT / "overview_story.png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def bridge():
    # Source: rl based model/analysis/fas_c14_diagnosis.md, sections 1 and 2.
    fig, (a, b) = plt.subplots(1, 2, figsize=(13, 5.4), gridspec_kw={"width_ratios": [1, 1.25]})
    gf = ["10%", "50%", "90%"]
    off = [0.210796, 0.119191, 0.023838]
    on = [0.217359, 0.122237, 0.024447]
    xs = range(3)
    a.bar([x - 0.19 for x in xs], off, 0.38, label="beta-oxidation route only", color=GREY)
    a.bar([x + 0.19 for x in xs], on, 0.38, label="with early-release reaction", color=GREEN)
    a.set_xticks(list(xs))
    a.set_xticklabels(gf)
    a.set_xlabel("Growth held at (% of wild-type growth)")
    a.set_ylabel("Max C14:0 export (mmol/gDW/h)")
    a.set_title("Adding the reaction: +2.6% at 50% growth", fontsize=12, fontweight="bold", loc="left")
    a.legend(frameon=False, fontsize=9)
    labels = ["Free acetyl-CoA", "Free malonyl-CoA", "NGAM = 0", "Free ATP", "Free NADPH"]
    gains = [0.01, 0.01, 7.6, 36.0, 150.9]
    cols = [GREY, GREY, GREY, ORANGE, RED]
    b.barh(labels, gains, color=cols)
    for i, g in enumerate(gains):
        b.text(g + 2, i, f"+{g:g}%", va="center", fontsize=9)
    b.set_xlim(0, 185)
    b.set_xlabel("Change in max C14:0 when the resource is made free (50% growth)")
    b.set_title("What limits C14? Cofactors, not carbon chain", fontsize=12, fontweight="bold", loc="left")
    for ax in (a, b):
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.01, 0.01, "Diagnostic relaxations in Yeast9; glucose uptake 1.0, NGAM 0.7. " + FOOT, fontsize=8.5, color=GREY)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(OUT / "bridge_early_release.png", dpi=150, facecolor="white")
    plt.close(fig)


def alignment():
    # Source: ScFAS2 KS domain analysis (EMBOSS Needle, BLOSUM62, gap open 10, extend 0.5).
    fig, ax = plt.subplots(figsize=(11, 3.6))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 3.6)
    ax.axis("off")
    ax.text(0.1, 3.3, "The ScFAS2 equivalent of the Yarrowia chain-length residue", fontsize=14, fontweight="bold")
    ax.text(0.1, 2.95, "Schematic of three equivalent positions; 34-residue offset; no gaps at or beside the key column",
            fontsize=9.5, color=GREY)
    rows = [("YlFAS (Rigouin 2017)", ["M1217", "I1220", "M1226"], 2.1),
            ("ScFAS2 (P19097)", ["M1251", "V1254", "M1260"], 0.9)]
    xs = [3.6, 6.2, 8.8]
    for name, res, y in rows:
        ax.text(0.1, y + 0.25, name, fontsize=11, va="center")
        for x, r in zip(xs, res):
            key = r in ("I1220", "V1254")
            ax.add_patch(FancyBboxPatch((x - 0.7, y), 1.4, 0.5, boxstyle="round,pad=0.02",
                                        fc="#fdebd8" if key else "#eef3fb", ec=ORANGE if key else BLUE, lw=2))
            ax.text(x, y + 0.25, r, ha="center", va="center", fontsize=12, fontweight="bold")
    notes = ["identical", "conservative:\nboth beta-branched", "identical"]
    for x, n in zip(xs, notes):
        ax.plot([x, x], [1.45, 2.05], color=GREY, lw=1.5)
        ax.text(x, 1.75, n, ha="center", va="center", fontsize=8.5, color=GREY,
                bbox=dict(fc="white", ec="none", pad=1))
    ax.text(0.1, 0.25, "Proposed substitution V1254W is the ScFAS2 analogue of Yarrowia I1220W. "
            "Transfer is by homology; the effect in S. cerevisiae is an assumption.", fontsize=9, color=RED)
    fig.savefig(OUT / "alignment_strip.png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def rl_benchmark():
    # Source: wiki draft, search benchmark, 10 genes, up to 3 knockouts, 20 seeds.
    names = ["Brute force", "Greedy", "Reinforcement\nlearning"]
    found = [100, 65, 10]
    evals = [175, 23, 1204]
    short = [0.0, 1.14, 10.13]
    fig, axs = plt.subplots(1, 3, figsize=(13, 4.6))
    for ax, vals, title, fmt, col in [
        (axs[0], found, "Finds the exact best answer (%)", "{:g}%", GREEN),
        (axs[1], short, "Mean shortfall (%)", "{:g}%", ORANGE),
        (axs[2], evals, "Evaluations (FBA solves)", "{:,}", BLUE),
    ]:
        ax.bar(names, vals, color=col)
        for i, v in enumerate(vals):
            ax.text(i, v, fmt.format(v), ha="center", va="bottom", fontsize=10)
        ax.set_title(title, fontsize=11.5, fontweight="bold", loc="left")
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_ylim(0, max(vals) * 1.18)
    fig.suptitle("Try the trivial baseline first: a simple search beat our learned agent",
                 fontsize=14, fontweight="bold", x=0.01, ha="left")
    fig.text(0.01, 0.01, "10 candidate genes, up to 3 knockouts, 20 random seeds, synthetic landscape. "
             "Our RL agent is a simple linear Q-learner. Not validated against wet-lab data.",
             fontsize=8.5, color=GREY)
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    fig.savefig(OUT / "rl_benchmark.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    overview()
    bridge()
    alignment()
    rl_benchmark()
    print("figures written to", OUT)
