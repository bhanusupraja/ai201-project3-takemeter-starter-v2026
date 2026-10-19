# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

DRAFT, to be reviewed. TakeMeter sorts posts from r/universe, a public subreddit about space and the cosmos, into three labels: `fact_post`, `question` and `speculation`. The goal is to tell apart posts that give checkable information, posts that ask the community something, and posts that push the poster's own unsupported theory.

---

## Label Taxonomy

### `fact_post`

**Definition:** Shares or explains specific, checkable information (a number, a named object or mission, a mechanism) as its main content.

**Example 1:**
> Phoenix A: a galaxy forming stars at an astonishing rate. The Milky Way forms roughly 1–2 solar masses of new stars per year. But the central galaxy of the Phoenix Cluster has been observed forming stars at roughly 740 solar masses per year...

**Example 2:**
> DYK a neutron star is so dense that a teaspoon of its material would weigh about a billion tons on Earth? Neutron stars pack more mass than our Sun into a sphere only about 20 km (12 miles) across...

### `question`

**Definition:** Mainly asks the community something, with little or no claim of its own.

**Example 1:**
> Why is gravity attractive? I understand that gravity is the reason planets and stars form and what not. I'm just curious why gravity causes things to attract and not repel or do neither?

**Example 2:**
> Recent potential Dark Matter detection. I recently read the some experiments had 2.6 sigma dark matter detection. Can someone explain in simple words?

### `speculation`

**Definition:** Puts forward the poster's own theory or big claim about the universe with nothing checkable behind it.

**Example 1:**
> My theory related to the universe and its origins. Guys listen to my theory about the universe... what if big bang isn't the start... time itself existed before the big bang.

**Example 2:**
> The Superluminous Aether: Why the Cosmic Vacuum Appears Empty Yet Conceals Enormous Superluminal Energy (researchgate.net link, no supporting detail)

### The hardest boundary

**Which two labels:** `question` and `speculation`.

**The decision rule I used every time:** If most of the post is the poster's own theory or claim, it is `speculation`, even if it ends with a question mark. If most of the post is asking for an answer and the poster offers little of their own, it is `question`. A post that mainly states checkable facts is `fact_post` even if it ends with "Thoughts?".

---

## The Dataset

**Where the posts came from:** r/universe, copied by hand from the public subreddit. Draft count so far is 36 posts. The target is 200.

**How I labeled them:** DRAFT. The first 36 rows were pre-labeled by Claude and are marked "NOT YET REVIEWED" in the note column until I read and correct them. The 20 cold-labeled rows are still to do and will be marked `cold`.

**Counts per label:** (draft, update after collecting more)

| Label | Count | Share |
|---|---|---|
| fact_post | 18 | 50.0% |
| question | 13 | 36.1% |
| speculation | 5 | 13.9% |
| **Total** | 36 | 100% |

**Three hard cases**

**1.**
> *The post:* Are we closer to the Biggest or the Smallest thing in existence... in the whole universe? (asks a question, but also says "we'll never understand how the universe really works")
>
> *Could have been:* `question` or `speculation`
>
> *I chose, because:* `speculation` in the draft, since it makes its own sweeping claims. This is a draft call for me to confirm.

**2.**
> *The post:* How Do We Define the Largest Structures in the Universe? (mentions Quipu at roughly 1.4 billion light-years and the cosmological principle, then asks the reader)
>
> *Could have been:* `fact_post` or `question`
>
> *I chose, because:* `question` in the draft, since the facts support the question rather than being the point. This is a draft call for me to confirm.

**3.**
> *The post:* Pluto went from a blurry dot to a surprisingly complex world. (facts about New Horizons, then a reflective question to the reader)
>
> *Could have been:* `fact_post` or `question`
>
> *I chose, because:* `question` in the draft, since most of the post is the reflection and the closing ask. This is a draft call for me to confirm.

**Not labeled:** "The Moon has been following Earth for billions of years and still hasn't asked for directions." is a joke that fits none of the three labels. It suggests a fourth label such as `reaction` may be missing.

---

## The Training Run

**Base model:** TO FILL IN from the notebook after the run.

**Settings:** TO FILL IN (defaults are 3 epochs, learning rate 2e-5, batch size 16, 128 tokens).

**Anything I changed from the defaults, and why:** TO FILL IN.

**Split sizes:** TO FILL IN after section 3 of the notebook. Device: CPU only (torch 2.14.1+cpu, Python 3.12.7).

---

## How I Used AI

**Moment 1**

- *What I asked for:* Claude to draft label definitions and a labels.csv from the posts I pasted.
- *What came back:* three draft labels and 36 pre-labeled rows.
- *What I changed:* TO FILL IN after review.

**Moment 2**

- *What I asked for:* Claude to draft acceptance criteria.
- *What came back:* five draft criteria with reasons.
- *What I changed:* TO FILL IN. I need to rewrite the numbers and reasons in my own words.

**Pre-labelling disclosure:** The first 36 rows of `labels.csv` were pre-labeled by Claude and then reviewed by me. This section must be updated to match what I actually did.

---

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
