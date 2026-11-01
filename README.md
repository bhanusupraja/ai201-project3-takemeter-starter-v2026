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

TakeMeter sorts posts from r/universe, a public subreddit about space and the cosmos, into three labels: `fact_post`, `question` and `speculation`. The goal is to tell apart posts that give checkable information, posts that ask the community something, and posts that push the poster's own unsupported theory.

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

**Where the posts came from:** r/universe, a public subreddit. The first 36 were copied by hand; the rest came from listing files (top, controversial, search) saved from my browser and converted with `scrape_posts.py`. Current count is 166 posts. The target was 200 and the minimum under the stop rule is 150. I stopped at 166, above the minimum, because of time, so `fact_post` and `speculation` have fewer examples than I would have liked and their test-split scores will be jumpy.

**How I labeled them:** I labeled 20 posts cold (no help, no tools), marked `cold` in the note column. Claude pre-labeled the other rows (the first 36 plus 112 more) and I then read every one and corrected the labels I disagreed with. I also removed two near-duplicate posts that appeared twice. I also set aside 17 posts in `excluded_posts.csv` (astrophoto captions with only equipment lists, image-only or link-only posts) because none of my three labels applies to them.

**Counts per label:** (166 rows, update after collecting more)

| Label | Count | Share |
|---|---|---|
| fact_post | 51 | 30.7% |
| question | 73 | 44.0% |
| speculation | 42 | 25.3% |
| **Total** | 166 | 100% |

My 20 cold labels first came out as 13 `question`, 4 `speculation` and 3 `fact_post`. I had been treating a title ending in "?" as a `question`. After rereading my own definitions I changed 12 of the 20 (now 9 `fact_post`, 7 `question`, 4 `speculation`) and marked those rows `cold; relabeled after rule clarification`. The original labels are kept in `cold_20_original.csv`. This means the cold set is no longer a pure first-instinct check, and it also shows exactly where my definitions were unclear: posts with a question title and an explanatory body.

**Three hard cases**

*(Wording drafted by Claude from the notes I wrote in the `note` column while reviewing `labels.csv`; I need to read it and edit it so it is mine.)*

**1.**
> *The post:* "Thought experiment: If observable universe was the size of the Earth" — a long list of scaled-down distances (one light year is 0.137 mm, Proxima Centauri is 0.582 mm away, the Milky Way is 13.7 m across).
>
> *Could have been:* `fact_post` or `speculation`
>
> *I chose, because:* `speculation`. The numbers are checkable, but the post is framed as the poster's own thought experiment and observation, not as a source of information. My review note said "assuming it is their thought/observation". This is the weakest of my calls: by my own rule that a post mainly stating checkable facts is `fact_post`, it could easily be the other label.

**2.**
> *The post:* "Interesting question I don't know if this is a unique thought..." — the poster describes an astronomy-class thought experiment about a universe where all life has vanished, defines "life" as anything that can perceive the universe, and then works through what that means.
>
> *Could have been:* `question` or `speculation`
>
> *I chose, because:* `question`. The title calls it a question and the poster mostly wonders aloud rather than asserting a result; my review note said "assuming they have only asked a question". But a long chain of the poster's own reasoning is what my decision rule calls `speculation`, so this sits right on my hardest boundary.

**3.**
> *The post:* "Some thoughts on the holographic principle." — explains the principle and links a video, then argues from accelerating expansion and horizons toward the poster's own conclusion.
>
> *Could have been:* `fact_post` or `speculation`
>
> *I chose, because:* `speculation`. The first half restates a known idea, but the second half is the poster connecting "puzzle pieces" into their own claim, and my review note said "assuming they have mentioned their thoughts". If I had only read the first paragraph I would have called it `fact_post`.

**What these three have in common:** each starts with something checkable or a question-shaped title and then turns into the poster's own reasoning. That is the same pattern that made me relabel 12 of my cold labels, so I expect the model to struggle in the same place.

**Not labeled:** 17 posts in `excluded_posts.csv` are image captions or link-only posts with no claim, which fit none of the three labels. Also, "The Moon has been following Earth for billions of years and still hasn't asked for directions." is a joke that fits none of the three labels. It suggests a fourth label such as `reaction` may be missing.

---

## The Training Run

**Base model:** `distilbert-base-uncased`

**Settings:** 3 epochs, learning rate 2e-5, batch size 16, max length 128 tokens, seed 42.

**Anything I changed from the defaults, and why:** Nothing. I left every training setting at its default. The only things I edited in the notebook were my name/email and the label list (`fact_post`, `question`, `speculation`).

**Split sizes:** 166 posts split 70/15/15, stratified: train 116, validation 25, test 25. By label: `fact_post` 35 / 8 / 8, `question` 51 / 11 / 11, `speculation` 30 / 6 / 6 (train / val / test). Only 6 `speculation` posts landed in the test split, so any score for that label is very jumpy.

**Device:** CPU only (torch 2.14.1+cpu, Python 3.12.7). Training took about 110 seconds.

**Result (seed 42, the unit 5 run):** accuracy 0.640, macro F1 0.483. Per label: `fact_post` F1 0.714 (n=8), `question` F1 0.733 (n=11), `speculation` F1 0.000 (n=6). The model never predicted `speculation` on the test split: 5 of its 6 posts were called `question` and 1 was called `fact_post`. Validation accuracy rose each epoch (0.56, 0.60, 0.64), which says training converged, not that it learned my distinction. Saved in `results.json` and `test_split.csv`.

---

## How I Used AI

*(Wording drafted by Claude from what actually happened in this project; I need to check it against my own memory and edit it.)*

**Moment 1 — pre-labelling 112 posts, then correcting them**

- *What I asked for:* Claude to pre-label a batch of 138 r/universe posts I had collected, using my three definitions. I labelled 20 other posts cold first and did not show Claude those.
- *What came back:* a label for 112 of them and 17 set aside as fitting none of the labels, plus nine duplicates skipped. It marked about ten as "unsure".
- *What I changed:* I read every pre-labelled row and corrected the ones I disagreed with. Across the file the counts moved from 82 `question` / 52 `fact_post` / 34 `speculation` to 73 / 53 / 42, so at least nine posts changed label, mostly `question` to `speculation`. I also found two posts that appeared twice and removed one copy of each so they could not end up in both train and test.

**Moment 2 — misreading my own `question` rule**

- *What I asked for:* help labelling my cold 20, and then whether a title ending in "?" makes a post a `question`.
- *What came back:* an explanation that my definition looks at what most of the post does, not at the punctuation, with examples from my own data such as a "Friday Fun Fact" whose title is a question but whose body explains quantum gravity. Claude also listed the cold posts where title and body disagreed, but left the labels to me.
- *What I changed:* I relabelled 12 of my 20 cold posts (13 `question` / 4 `speculation` / 3 `fact_post` became 7 / 4 / 9) and kept the originals in `cold_20_original.csv`. Because I changed them after being told the rule, the cold set is no longer a pure first-instinct check, and I say so in The Dataset above.

**Moment 3 — unit 6: staff labels and retraining**

- *What I asked for:* Claude generated a draft set of labels for the 30 staff posts (`my_staff_labels_draft.csv`) from `data/staff_taxonomy.md`, and ran the retrain for my improvement (10 epochs, `RUN_LABEL = "after"`) by executing the notebook's cells from a script.
- *What came back:* the draft labels, and `results_three_seeds_after.json`. Claude also suggested more epochs as the improvement because my diagnosis pointed at undertraining, and drafted the Agreement Report, Run Log — After and the sections below.
- *What I changed:* I read each staff-post label against the staff rules and kept all 30, so I matched staff 30 of 30. Because they started as an AI draft, I say in the Agreement Report that this is weak evidence about my own consistency. I chose to keep the epochs improvement.
- *A mistake worth recording:* the notebook cell Claude ran also wrote `results.json`, overwriting my unit 5 file with 10-epoch numbers. It was restored from git before anything was committed, and `results.json` still shows the unit 5 accuracy of 0.64.

**Other help:** Claude also wrote `scrape_posts.py` and `label_cold.py`, drafted the first versions of my label definitions, the README, and the five acceptance criteria, and ran the notebook cells for me to produce `results.json`. I treat the criteria numbers as my own decisions to confirm, not as something Claude set.

**Pre-labelling disclosure:** 146 of the 166 rows in `labels.csv` were pre-labelled by Claude and then reviewed one by one by me, with my corrections applied; the other 20 are my cold labels (12 of which I changed after clarifying my rule).

---

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

*(Unit 6 sections below were drafted by Claude from the numbers the notebook and `baseline.py` produced. I need to read them and rewrite anything that is not in my own words.)*

Same 25 held-out posts (`test_split.csv`, seed 42) for every column. The baseline is `facebook/bart-large-mnli`, zero-shot, no training, run on CPU (about 25 posts in a couple of minutes).

| Measure | Baseline (my definitions) | Baseline (bare label names) | Trained | Trained minus baseline (definitions) |
|---|---|---|---|---|
| Overall accuracy | 0.440 | 0.720 | 0.640 | +0.200 |
| Macro F1 | 0.401 | 0.681 | 0.483 | +0.082 |
| F1 — `fact_post` | 0.480 | 0.857 | 0.714 | +0.234 |
| F1 — `question` | 0.500 | 0.741 | 0.733 | +0.233 |
| F1 — `speculation` | 0.222 | 0.444 | 0.000 | -0.222 |

I report the run **with my definitions** (`baseline_results.json`) as the baseline, because that is what the brief describes. I also ran it once with `label_definitions.txt` moved away so it fell back to bare label names (`baseline_results_bare_names.json`).

**What I predicted before I looked:**

*(Drafted by Claude and committed before any baseline number was produced; I need to confirm or rewrite it.)* I expect my trained model to beat the baseline on `question` and `fact_post`, because those have clear surface patterns (a question asked of the community; numbers and named objects) that it saw in 116 training posts. I expect the baseline to match or beat it on `speculation`, since my trained model never predicted that label in the unit 5 run and a general model at least knows what "a theory" sounds like.

**What the gap actually means:** Against the baseline that uses my definitions, fine-tuning helped on `fact_post` and `question` (about +0.23 F1 each) and on accuracy (+0.20). But it did nothing for `speculation`: the baseline got 0.222 and my trained model got 0.000 because it never predicted that label. My prediction above was right on both counts. The surprise is the second baseline: with bare label names, zero-shot got 0.720 accuracy, which is *higher* than my trained model's 0.640 on these 25 posts, and ahead on every label including `speculation` (0.444). So my definitions made the general model worse (0.440 vs 0.720), perhaps because the long definition sentences confuse the entailment prompt, and a simple zero-shot model with no training is at least as good as what I trained. With only 25 test posts one post is 4 points, and my seeds below swing by 16 points, so I would not claim the bare-names baseline is truly better, but I also cannot claim fine-tuning added anything over it.

---

## Run Log — Before

Three seeds (42, 7, 2024), each a different 70/15/15 split of the same 166 posts. Source: `results_three_seeds_before.json` (CPU, torch 2.14.1+cpu).

| Measure | Seed 42 | Seed 7 | Seed 2024 | Spread |
|---|---|---|---|---|
| Overall accuracy | 0.640 | 0.560 | 0.480 | 0.160 |
| Macro F1 | 0.483 | 0.404 | 0.284 | 0.199 |
| F1 — `fact_post` | 0.714 | 0.545 | 0.222 | 0.492 |
| F1 — `question` | 0.733 | 0.667 | 0.629 | 0.105 |
| F1 — `speculation` | 0.000 | 0.000 | 0.000 | 0.000 |

Accuracy moved 0.16 across seeds, more than the 10 points the notebook warns about, so my dataset is too small (25 test posts, 6 to 8 per label) for a stable measure.

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.65 in every seed | 0.640 | 0.560 | 0.480 | MISSED |
| 2. Every label F1 | ≥ 0.50 in every seed | min 0.000 (`speculation`) | min 0.000 (`speculation`) | min 0.000 (`speculation`) | MISSED |
| 3. Balance of `labels.csv` | no label above 60% or below 15% | 44.0% / 30.7% / 25.3% | same file | same file | MET |
| 4. Agreement with staff | ≥ 21 of 30 | 30 / 30 | same (labels do not depend on the seed) | same | MET (see caveat in Agreement Report) |
| 5. Confident predictions right | ≥ 80% right when top probability ≥ 0.80 | no prediction reached 0.80 (max 0.526) | none (max 0.513) | none (max 0.538) | MISSED |

Criterion 5 was checked from per-prediction probabilities saved in `confidence_before.json` (a separate rerun of the same three seeds, same settings).

### Confusion matrix

Seed 42 (rows are true labels, columns are the model's guesses):

| true \ predicted | fact_post | question | speculation |
|---|---|---|---|
| **fact_post** | 5 | 3 | 0 |
| **question** | 0 | 11 | 0 |
| **speculation** | 1 | 5 | 0 |

**My biggest off-diagonal number, and what it means:** 5 of the 6 real `speculation` posts were called `question`, while 0 real `question` posts were called `speculation`. The model has not learned the `question` / `speculation` boundary at all, and it leans one way: anything that is not clearly a fact becomes a `question`.

---

## Verdicts and Diagnoses

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Overall accuracy | ≥ 0.65 in every seed | MISSED | 0.640, 0.560, 0.480. Even the best seed is just under, and the target has to hold in all three. |
| 2 | Every label F1 | ≥ 0.50 in every seed | MISSED | `speculation` F1 is 0.000 in all three seeds, and `fact_post` also falls to 0.222 in seed 2024. |
| 3 | Balance | no label above 60% or below 15% | MET | The shares are 44.0%, 30.7% and 25.3%, so every label is inside the band. This does not depend on the seed. |
| 4 | Agreement with staff | ≥ 21 of 30 | MET | 30 of 30 matched staff. Caveat: the labels began as an AI draft that I reviewed and kept, so this is weak evidence about my own consistency. |
| 5 | Confidence | ≥ 80% right when top probability ≥ 0.80 | MISSED | No test prediction in any seed reached 0.80, so the target can't be shown to hold. The highest confidence was 0.538. |

**Diagnoses**

- **Criteria 1 and 2 (`speculation` never predicted):** In all three seeds the model gets `speculation` F1 of 0.000, and in seed 42 it sends 5 of 6 to `question` and none the other way. I see two causes that I can't yet tell apart. (a) *Labeling consistency:* I relabeled 12 of my 20 cold posts after realising I had been reading the title and not the body, and my own hard cases all sit between `question` and `speculation`. If I applied that boundary two ways in the 116 training posts, there is no consistent pattern for the model to learn. My staff-set agreement check did not settle it: I matched staff 30 of 30, but from an AI draft and under a different taxonomy, so it gives no evidence either way. (b) *Too little signal:* `speculation` has only 30 training posts per split, and only 6 test posts, so one or two posts swing its F1 by 0.2 or more.
- **Criterion 5 (confidence):** the model is never confident. The highest top probability across all three seeds is 0.538, and the validation loss only fell from about 1.02 to 0.94 over three epochs against a chance level of about 1.10 for three labels. That looks like an undertrained model (3 epochs on 116 posts at the default 2e-5), not a labeling problem.
- **Accuracy instability (criterion 1):** accuracy ranges 0.48 to 0.64. With 25 test posts, each one is 4 points, so some of the miss is the small test set and not only the model.
- **Pattern:** the three misses share one cause: the model barely moved off guessing the biggest class. It's one problem, undertraining plus a hard boundary, not three.

## Agreement Report

**Agreement rate:** 30 / 30 = 100%

**Where my labels came from (disclosure):** Claude generated a draft set of labels for the 30 staff posts (`my_staff_labels_draft.csv`) from `data/staff_taxonomy.md`. I then read each post against the staff definitions and decision rules, agreed with every draft label, and kept all 30 unchanged in `my_staff_labels.csv`. So these are labels I reviewed and endorsed, not labels I produced cold. I did not open the staff answer key until `my_staff_labels.csv` was saved. Because the starting point was an AI draft, a 100% rate says less about my own consistency than a cold 30 would have.

**Disagreements:** none. There was nothing to adjudicate and I have not invented any. Both sets split 10 `analysis` / 10 `hot_take` / 10 `reaction`.

**The borderline posts:** staff flagged 7 posts as borderline (sp_005, sp_010, sp_014, sp_019, sp_020, sp_028, sp_029). I matched staff on all seven, but a post being ambiguous means a match here could have gone either way, so I don't read it as proof the rules are tight.

**What this tells me, and what it doesn't:**

- It does not show that I labeled my own 166 `r/universe` posts consistently. This check used the staff taxonomy (`analysis` / `hot_take` / `reaction`), not my own (`fact_post` / `question` / `speculation`), and it started from an AI draft.
- It gives me no pile (a), (b) or (c) disagreements, so I have no agreement-based evidence for or against a labeling problem on the `question` / `speculation` boundary. My diagnosis of that boundary below rests on the confusion matrix and the relabeling I did in unit 5 only.
- Criterion 4 (at least 21 of 30) is met on the number, but with the caveat above.

---

## The Improvement

**What I changed:** One setting: `EPOCHS` 3 → 10 in the training settings. Learning rate (2e-5), batch size (16), max length (128), the model (`distilbert-base-uncased`), my labels, taxonomy, criteria and the three seeds (42, 7, 2024) are all unchanged. Retrained with `RUN_LABEL = "after"`; numbers are in `results_three_seeds_after.json`.

**Which diagnosis pointed at it:** The Criterion 5 diagnosis: the model was never confident (top probability never above 0.538) and validation loss only fell from about 1.02 to 0.94 against about 1.10 for chance, which I read as undertrained at 3 epochs on 116 posts. The `speculation` F1 of 0.000 was partly the same story, since the model never moved off guessing the biggest class.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.65 in every seed | 0.800 | 0.720 | 0.720 | MET |
| 2. Every label F1 | ≥ 0.50 in every seed | min 0.600 (`speculation`) | min 0.000 (`speculation`) | min 0.250 (`speculation`) | MISSED |
| 3. Balance of `labels.csv` | no label above 60% or below 15% | 44.0% / 30.7% / 25.3% | same file | same file | MET |
| 4. Agreement with staff | ≥ 21 of 30 | 30 / 30 | same | same | MET (weak evidence, see Agreement Report) |
| 5. Confident predictions right | ≥ 80% right when top probability ≥ 0.80 | not re-measured | not re-measured | not re-measured | NOT RE-MEASURED |

Criterion 5 note: the after run saved only summary confidence numbers, not per-prediction probabilities, so I cannot say how many predictions reached 0.80. What I do have: mean confidence when right was 0.700 / 0.667 / 0.672 (before: 0.462 / 0.452 / 0.498), and the most-confident third of predictions was right 0.875 of the time in all three seeds. The before-run verdict (MISSED, nothing reached 0.80) stands as written.

| Measure | Before: 42 | Before: 7 | Before: 2024 | After: 42 | After: 7 | After: 2024 |
|---|---|---|---|---|---|---|
| Accuracy | 0.640 | 0.560 | 0.480 | 0.800 | 0.720 | 0.720 |
| Macro F1 | 0.483 | 0.404 | 0.284 | 0.756 | 0.553 | 0.625 |
| F1 `fact_post` | 0.714 | 0.545 | 0.222 | 0.750 | 0.889 | 0.824 |
| F1 `question` | 0.733 | 0.667 | 0.629 | 0.917 | 0.769 | 0.800 |
| F1 `speculation` | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 | 0.250 |

Confusion matrix after, seed 42 (rows are true labels, columns are the model's guesses):

| true \ predicted | fact_post | question | speculation |
|---|---|---|---|
| **fact_post** | 6 | 1 | 1 |
| **question** | 0 | 11 | 0 |
| **speculation** | 2 | 1 | 3 |

**Did it help, and how do I know:** Yes on accuracy and mostly on `fact_post` and `question`; only partly on `speculation`. Accuracy rose in all three seeds (0.64 → 0.80, 0.56 → 0.72, 0.48 → 0.72), and the spread across seeds shrank from 0.16 to 0.08, so criterion 1 went from MISSED to MET. `fact_post` F1 rose most where it had collapsed (0.222 → 0.824 in seed 2024). `speculation` went from 0.000 in every seed to 0.600, 0.000 and 0.250: the model now predicts it sometimes, but in seed 7 it still never does (5 of 6 `speculation` posts went to `question`), so criterion 2 is still MISSED. That supports the undertraining part of my diagnosis, and it shows the `question` / `speculation` boundary was not only an undertraining problem. Caveats: each test split is 25 posts, so one post is 4 points and `speculation` has only 6 test posts, and I only tried one setting (10 epochs), so I cannot say 10 is the right number or that more epochs would not overfit.

---

## What's Still Broken

*(Drafted by Claude from the after-run numbers; I need to read it and rewrite it in my own words.)*

- **Criterion 2 (every label F1 ≥ 0.50): still MISSED.** `speculation` F1 is 0.600, 0.000 and 0.250 across the three seeds. *What I'd do:* add more `speculation` posts (I only have 42 of 166, and 6 land in each test split), then re-check the `question` / `speculation` boundary in my own labels, since that is where my hard cases and my unit 5 relabeling all sat. *Why I stopped:* the unit allows one change, and I used it on epochs. Adding posts or relabeling would have been a second change.
- **Criterion 5 (confidence): MISSED before, not re-measured after.** The after run saved only summary confidence numbers, so I can't tell whether any prediction reached 0.80. *What I'd do:* save per-prediction probabilities in the after run (as I did for `confidence_before.json`) and re-check. Mean confidence when right did rise from about 0.46 to about 0.67, so it may now be closer, but I haven't shown it.
- **Criteria 1, 3 and 4 are met, with caveats.** Criterion 1 (accuracy) is met only after the fix, on 25-post test splits where one post is 4 points. Criterion 4 (agreement) is met at 30/30, but the labels began as an AI draft I reviewed, so it says little about my own consistency.
- **Not tested:** whether 10 epochs is the right number or whether more epochs would overfit. I tried one setting.

**The gap between what I meant my labels to capture and what the model learned:**
I meant `speculation` to mean the poster's own reasoning going beyond checkable facts, and `question` to mean the post mostly asks. In the before run the model learned neither distinction (seed 42 sent 5 of 6 `speculation` posts to `question`, and seed 7 sent 6 of 6). After 10 epochs it started separating `speculation` in some seeds (3 of 6 correct in seed 42), but it still often sends those posts to `fact_post` or `question` (2 and 1 of 6 in seed 42), which suggests it is picking up surface cues like numbers and question-shaped titles, not the reasoning pattern I defined.


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
