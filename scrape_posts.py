"""Collect public r/universe posts into candidates.csv (text,label,note).

Timeboxed helper, not a scraping project. Uses only the standard library and
Reddit's public JSON listings (no login, no API key).

    python scrape_posts.py                  # all sorts + speculation searches
    python scrape_posts.py --max 250        # stop after 250 candidates
    python scrape_posts.py --subreddit universe

Output: candidates.csv with an EMPTY label column. Label them yourself (first 20
cold, marked `cold` in note), then copy the rows you keep into labels.csv.
Posts already in labels.csv are skipped so nothing is duplicated.

If you get HTTP 403/429, wait a few minutes and rerun, or run it on a different
network. Reddit sometimes blocks anonymous requests.
"""
import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (AI201 class project; reading public posts; contact: student)"
DELAY = 2.0          # seconds between requests, be polite
MIN_BODY = 60        # skip posts with almost no text (image-only, link-only)

# (path, params) listings — varied sorts so the sample isn't all one kind of post
LISTINGS = [
    ("top", {"t": "year"}),
    ("top", {"t": "month"}),
    ("new", {}),
    ("hot", {}),
    ("controversial", {"t": "year"}),
]
# searches aimed at the thin label (speculation)
SPEC_QUERIES = [
    "my theory", "what if", "I think the universe", "hypothesis",
    "before the big bang", "aether", "time is", "consciousness universe",
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def pages(base, params, max_pages=4):
    after = None
    for _ in range(max_pages):
        q = dict(params, limit=100, raw_json=1)
        if after:
            q["after"] = after
        url = f"{base}?{urllib.parse.urlencode(q)}"
        try:
            data = fetch(url)["data"]
        except Exception as e:  # noqa: BLE001
            print(f"  ! {url} -> {e}", file=sys.stderr)
            return
        for child in data["children"]:
            yield child["data"]
        after = data.get("after")
        time.sleep(DELAY)
        if not after:
            return


def to_text(p):
    title = (p.get("title") or "").strip()
    body = (p.get("selftext") or "").strip()
    if p.get("stickied") or p.get("over_18"):
        return None
    if body in ("[removed]", "[deleted]") or len(body) < MIN_BODY:
        return None
    return f"{title}\n{body}"


def norm(t):
    return " ".join(t.lower().split())


def existing_texts():
    try:
        with open("labels.csv", newline="", encoding="utf-8") as f:
            return {norm(r["text"]) for r in csv.DictReader(f)}
    except FileNotFoundError:
        return set()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subreddit", default="universe")
    ap.add_argument("--max", type=int, default=260)
    ap.add_argument("--out", default="candidates.csv")
    ap.add_argument("--from-json", nargs="+", metavar="FILE",
                    help="read listing .json files saved from your browser "
                         "instead of calling Reddit (use when you get 403)")
    args = ap.parse_args()

    sub = args.subreddit
    seen = existing_texts()
    rows = []

    def add(posts, tag):
        n = 0
        for p in posts:
            text = to_text(p)
            if not text or norm(text) in seen:
                continue
            seen.add(norm(text))
            rows.append({"text": text, "label": "", "note": tag})
            n += 1
            if len(rows) >= args.max:
                break
        print(f"{tag}: +{n} (total {len(rows)})")

    if args.from_json:
        for path in args.from_json:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)["data"]
            add((c["data"] for c in data["children"]), f"file:{path}")
        args.max = 0  # skip network sections below

    # spec searches first so the thin label is well represented
    for q in SPEC_QUERIES:
        if args.from_json or len(rows) >= args.max:
            break
        base = f"https://www.reddit.com/r/{sub}/search.json"
        add(pages(base, {"q": q, "restrict_sr": 1, "sort": "relevance"}, 1), f"search:{q}")
    for sort, params in LISTINGS:
        if args.from_json or len(rows) >= args.max:
            break
        add(pages(f"https://www.reddit.com/r/{sub}/{sort}.json", params),
            f"{sort}:{params.get('t', '')}")

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["text", "label", "note"])
        w.writeheader()
        w.writerows(rows)
    print(f"\nWrote {len(rows)} candidates to {args.out}. Label column is empty.")
    if not rows:
        print("Nothing collected — Reddit may be blocking this network (403/429).")


if __name__ == "__main__":
    main()
