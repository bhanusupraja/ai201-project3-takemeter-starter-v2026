"""Pre-training sanity check for labels.csv: counts, 70% cap, duplicates, spelling."""
import sys
import pandas as pd

ALLOWED = {"fact_post", "question", "speculation"}  # keep in sync with label_definitions.txt
df = pd.read_csv("labels.csv")
print(f"{len(df)} rows")
counts = df["label"].value_counts()
for label, n in counts.items():
    share = n / len(df)
    flag = "  [FIX ME: over 70%]" if share > 0.70 else ""
    print(f"  {label:<12} {n:>4}  {share:5.1%}{flag}")
bad = set(df["label"]) - ALLOWED
if bad:
    print("[FIX ME] labels not in the allowed set:", sorted(bad))
dupes = df[df["text"].duplicated(keep=False)]
if len(dupes):
    print(f"[FIX ME] {len(dupes)} rows share duplicate text")
cold = df["note"].fillna("").str.contains("cold").sum()
unrev = df["note"].fillna("").str.contains("NOT YET REVIEWED").sum()
print(f"cold-labelled rows: {cold} (need 20)")
print(f"rows still marked NOT YET REVIEWED: {unrev}")
if len(df) < 200:
    print(f"[FIX ME] only {len(df)} rows; the target is 200 (150 minimum under the stop rule)")
