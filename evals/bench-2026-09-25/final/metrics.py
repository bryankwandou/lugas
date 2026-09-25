"""Before/after metrics for the lugas bench. Deterministic; rerun with `python metrics.py`."""
import glob, json, os, random, re, statistics

HERE = os.path.dirname(os.path.abspath(__file__))

AI_TELLS = {
    "id": ["di era", "tidak dapat dipungkiri", "signifikan", "krusial", "holistik", "komprehensif",
           "berbagai aspek", "sangat penting", "oleh karena itu", "kesimpulannya", "secara keseluruhan",
           "memegang peranan", "efektif dan efisien", "optimal", "inovatif", "sinergi", "pesat",
           "perlu dicatat", "dalam rangka", "tak hanya", "tidak hanya"],
    "en": ["in today's", "fast-paced", "it's worth noting", "it is worth noting", "delve", "robust",
           "seamless", "leverage", "tapestry", "pivotal", "crucial", "landscape", "unlock", "empower",
           "in conclusion", "overall,", "ever-evolving", "game-changer", "holistic", "furthermore",
           "moreover", "cutting-edge", "navigate"],
}


def words(t):
    return re.findall(r"\w+", t)


def sents(t):
    return [s for s in re.split(r"(?<=[.!?])\s+", t.strip()) if s]


def tells(t, lang):
    low = t.lower()
    return sum(low.count(p) for p in AI_TELLS[lang])


def cv(t):
    lens = [len(words(s)) for s in sents(t)]
    return statistics.pstdev(lens) / statistics.mean(lens) if len(lens) > 1 else 0.0


def main():
    corpus = {r["id"]: r for r in map(json.loads, open(os.path.join(HERE, "corpus.jsonl"), encoding="utf-8"))}
    out = {}
    for f in sorted(glob.glob(os.path.join(HERE, "out-*.jsonl"))):
        for line in open(f, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                out[r["id"]] = r["rewrite"]
    rows = []
    for i, c in corpus.items():
        if i not in out:
            continue
        a, b, lang = c["text"], out[i], c["lang"]
        lost = [f for f in c["facts"] if f not in b]
        rows.append(dict(id=i, lang=lang, w0=len(words(a)), w1=len(words(b)), t0=tells(a, lang),
                         t1=tells(b, lang), cv0=cv(a), cv1=cv(b), facts=len(c["facts"]), lost=lost))
    json.dump(rows, open(os.path.join(HERE, "metrics.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    def agg(rs, label):
        n = len(rs)
        if not n:
            return
        cut = statistics.mean(1 - r["w1"] / r["w0"] for r in rs)
        t0, t1 = sum(r["t0"] for r in rs), sum(r["t1"] for r in rs)
        nf, nl = sum(r["facts"] for r in rs), sum(len(r["lost"]) for r in rs)
        print(f"{label:5} n={n:2}  words cut {cut:5.1%}  AI tells {t0}->{t1} ({1 - t1 / max(t0, 1):.0%} fewer)  "
              f"sentence-length CV {statistics.mean(r['cv0'] for r in rs):.2f}->{statistics.mean(r['cv1'] for r in rs):.2f}  "
              f"facts kept {nf - nl}/{nf}")

    agg(rows, "all")
    agg([r for r in rows if r["lang"] == "id"], "id")
    agg([r for r in rows if r["lang"] == "en"], "en")
    for r in rows:
        if r["lost"]:
            print("  lost", r["id"], r["lost"])

    # Blind A/B packet for judges: random order, fixed seed, key kept separately.
    rnd = random.Random(20260925)
    pairs, key = [], {}
    for r in rows:
        a, b = corpus[r["id"]]["text"], out[r["id"]]
        flip = rnd.random() < 0.5
        pairs.append({"pair": r["id"], "A": b if flip else a, "B": a if flip else b})
        key[r["id"]] = "A" if flip else "B"  # which letter is lugas
    rnd.shuffle(pairs)
    with open(os.path.join(HERE, "blind-pairs.jsonl"), "w", encoding="utf-8") as f:
        for p in pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    json.dump(key, open(os.path.join(HERE, "blind-key.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
