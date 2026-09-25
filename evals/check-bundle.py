"""Proves one lugas install carries all four skills: every file a guide points to exists.

Run from a fresh clone: `python evals/check-bundle.py`. Exit code 0 = complete.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDES = {"lugas": "SKILL.md", "rangka": "rangka/GUIDE.md",
          "atmajaya": "kampus/atmajaya/GUIDE.md", "pedoman": "kampus/pedoman/GUIDE.md"}
REF = re.compile(r"`((?:references|assets|examples|kampus|rangka|tests)/[\w./-]+\.(?:md|html|json))`")

bad = 0
for name, rel in GUIDES.items():
    path = os.path.join(ROOT, rel)
    if not os.path.isfile(path):
        print(f"MISSING GUIDE {name}: {rel}")
        bad += 1
        continue
    base = os.path.dirname(path)
    refs, missing = set(), []
    ok = lambda r: os.path.exists(os.path.join(base, r)) or os.path.exists(os.path.join(ROOT, r))
    for line in open(path, encoding="utf-8"):
        # A line may give the standalone path plus the in-lugas path "(in lugas: `../x`)".
        alt = [a for a in re.findall(r"`(\.\./[\w./-]+)`", line) if ok(a)]
        for r in REF.findall(line):
            refs.add(r)
            if not ok(r) and not alt and r not in missing:
                missing.append(r)
    print(f"{name:9} {rel:28} {len(refs):3} referenced files, {len(missing)} missing")
    for m in missing:
        print("   missing:", m)
    bad += len(missing)
sys.exit(1 if bad else 0)
