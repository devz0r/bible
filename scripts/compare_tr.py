#!/usr/bin/env python3
"""Compare the two Textus Receptus texts we hold, verse by verse, ignoring accents/case/punctuation.

  A = TAGNT 'TR' words (STEPBible/Tyndale)     sources/index/NT.tsv
  B = scrollmapper TR.csv ("TR 1550/1894")    sources/raw/TR_scrollmapper.csv

Writes sources/index/TR_DISAGREEMENTS.tsv and prints a summary.
Run: python3 -I scripts/compare_tr.py
"""
import csv, re, sys, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from build_index import book_code  # noqa: E402

def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("ς", "σ")
    return re.sub(r"[^α-ω ]", " ", t).split()

A = {}
with open(ROOT / "sources/index/NT.tsv", encoding="utf-8") as fh:
    for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
        A[r["ref"]] = norm(r["TR"])
B = {}
with open(ROOT / "sources/raw/TR_scrollmapper.csv", encoding="utf-8-sig", newline="") as fh:
    for r in csv.DictReader(fh):
        c = book_code(r["Book"])
        if r["Text"].strip():
            B[f"{c}.{r['Chapter']}.{r['Verse']}"] = norm(r["Text"])

common = sorted(set(A) & set(B))
dis = [k for k in common if sorted(A[k]) != sorted(B[k])]
out = ROOT / "sources/index/TR_DISAGREEMENTS.tsv"
with open(out, "w", encoding="utf-8") as fh:
    fh.write("ref\tonly_in_TAGNT\tonly_in_scrollmapper\n")
    for k in dis:
        a, b = list(A[k]), list(B[k])
        for w in list(a):
            if w in b: a.remove(w); b.remove(w)
        fh.write(f"{k}\t{' '.join(a)}\t{' '.join(b)}\n")
print(f"verses in both: {len(common)} (TAGNT {len(A)}, scrollmapper {len(B)})")
print(f"verses where the two TR texts disagree (as word sets): {len(dis)}")
for k in ("Luk.2.22", "Rev.16.5", "Rev.22.19", "1Jn.5.7", "Act.8.37"):
    print(f"  {k}: {'DISAGREE' if k in dis else 'agree'}")
print(f"details: {out}")
