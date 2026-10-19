# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy

Accuracy on the held-out test split is at least 0.65 in each of the three seeds.

**Why this target:** DRAFT. Three labels means a guesser gets about 33%, and `fact_post` alone is about 50% of my draft file, so 0.65 has to beat "always say fact_post". It is high enough to be useful and low enough for about 200 examples.

---

## 2. Per-label performance

Every label has an F1 of at least 0.50 on the held-out test split in each seed.

**Why this target:** DRAFT. `speculation` is my smallest label (5 of 36 draft rows, about 14%), so only a handful of its posts will land in the test split and its F1 will jump around. I set the floor lower than the accuracy target for that reason.

---

## 3. Balance

No label is above 60% or below 15% of the rows in `labels.csv`.

**Why this target:** DRAFT. The course cap is 70%, but a label near 70% makes "always guess it" score too well. `speculation` is already near the 15% floor in my draft, so this criterion is one I may fail unless I collect more of it.

---

## 4. Consistency

When I relabel the 30 staff posts under the staff taxonomy, I agree with staff on at least 21 of 30 (70%).

**Why this target:** DRAFT. Several of the 30 are chosen to be ambiguous, so I do not expect near-perfect agreement. 70% would show I apply written rules the same way most of the time.

---

## 5. Confidence

Among test predictions where the model's top probability is at least 0.80, at least 80% are correct, in each seed.

**Why this target:** DRAFT. A confident prediction should be right more often than an unsure one, or the confidence number tells me nothing. I set 0.80 and 80% to match each other, not because I have a baseline for it.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
