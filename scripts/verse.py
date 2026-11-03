#!/usr/bin/env python3
"""Print the source text for a verse or chapter: python3 -I scripts/verse.py Jhn.3.16
Chapter form: Jhn.3   Range form: Jhn.3.16-18   (codes as in sources/index/kjv_verses.txt)
"""
import csv, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
IDX, RAW = ROOT / "sources" / "index", ROOT / "sources" / "raw"

def load(name):
    rows = {}
    with open(IDX / name, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
            rows[r["ref"]] = r
    return rows

def main(arg):
    m = re.fullmatch(r"([1-3]?[A-Za-z]+)\.(\d+)(?:\.(\d+)(?:-(\d+))?)?", arg)
    if not m:
        sys.exit(__doc__)
    book, ch, v1, v2 = m.group(1), int(m.group(2)), m.group(3), m.group(4)
    refs = [r for r in (IDX / "kjv_verses.txt").read_text().split() if r.startswith(f"{book}.{ch}.")]
    if v1:
        lo, hi = int(v1), int(v2 or v1)
        refs = [r for r in refs if lo <= int(r.rsplit(".", 1)[1]) <= hi]
    if not refs:
        sys.exit(f"no verses match {arg}")
    nt, ot = load("NT.tsv"), load("OT.tsv")
    kjv = {}
    sys.path.insert(0, str(Path(__file__).parent))
    from build_index import BOOKS, book_code
    with open(RAW / "KJV.csv", encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            c = book_code(row["Book"])
            kjv[f"{c}.{row['Chapter']}.{row['Verse']}"] = row["Text"]
    for r in refs:
        print(f"== {r}\n  KJV: {kjv.get(r, '?')}")
        if r in nt:
            n = nt[r]
            print(f"  TR  : {n['TR']}\n  NA28: {n['NA28']}\n  Byz : {n['Byz']}")
        elif r in ot:
            o = ot[r]
            print(f"  WLC : {o['hebrew']}" + (f"\n  flags: {o['flags']}" if o["flags"] else ""))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) == 2 else sys.exit(__doc__))
