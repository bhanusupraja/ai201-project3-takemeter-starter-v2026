"""Label cold_20.csv one post at a time. Progress is saved after every answer.

    python label_cold.py

Keys: f = fact_post, q = question, s = speculation, k = skip for now, x = quit.
"""
import csv

KEYS = {"f": "fact_post", "q": "question", "s": "speculation"}
DEFS = ("f fact_post    - main content is specific, checkable info\n"
        "q question      - mainly asks the community, little claim of its own\n"
        "s speculation  - poster's own theory/big claim, nothing checkable behind it\n"
        "Rule: mostly the poster's own claim = speculation, even if it ends in '?'")

rows = list(csv.DictReader(open("cold_20.csv", encoding="utf-8")))
for i, r in enumerate(rows):
    if r["label"]:
        continue
    print("\n" + "=" * 70 + f"\nPost {i + 1} of {len(rows)}\n" + "=" * 70)
    print(r["text"][:1800])
    print("-" * 70 + "\n" + DEFS)
    while True:
        k = input("label [f/q/s, k skip, x quit]: ").strip().lower()
        if k in KEYS:
            r["label"] = KEYS[k]; break
        if k in ("k", "x"):
            break
    if k == "x":
        break
    with open("cold_20.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["text", "label", "note"])
        w.writeheader(); w.writerows(rows)
done = sum(1 for r in rows if r["label"])
print(f"\n{done}/{len(rows)} labeled.")
