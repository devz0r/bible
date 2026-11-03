#!/usr/bin/env python3
"""Word-by-word study view of a passage, for drafting.

  python3 scripts/study.py Jhn.3          whole chapter
  python3 scripts/study.py Jhn.3.16-18    verse range

Greek rows show: word, gloss, morphology, editions (only when not in every edition).
Hebrew rows show: word, gloss, morphology, text type (Q = Qere, R = restored, etc.).
Words marked  <2PL>  are second-person plural: mark them \\zpl in the translation.
Greek words marked  [not TR]  are not in the TR and must NOT be translated in the main text.
"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "sources" / "raw"
NT = {"Mat","Mrk","Luk","Jhn","Act","Rom","1Co","2Co","Gal","Eph","Php","Col","1Th","2Th","1Ti","2Ti","Tit","Phm","Heb","Jas","1Pe","2Pe","1Jn","2Jn","3Jn","Jud","Rev"}
ROW = re.compile(r"^([1-3]?[A-Za-z]+)\.(\d+)\.(\d+)([^#\t]*)#(\d+)=([^\t]+)\t")
ALL = {"NA28","NA27","Tyn","SBL","WH","Treg","TR","Byz"}

def main(arg):
    m = re.fullmatch(r"([1-3]?[A-Za-z]+)\.(\d+)(?:\.(\d+)(?:-(\d+))?)?", arg)
    if not m: sys.exit(__doc__)
    book, ch = m.group(1), int(m.group(2))
    lo = int(m.group(3)) if m.group(3) else 0
    hi = int(m.group(4) or m.group(3)) if m.group(3) else 999
    files = sorted(RAW.glob("TAGNT_*.txt" if book in NT else "TAHOT_*.txt"))
    cur = None
    for f in files:
        for line in open(f, encoding="utf-8-sig"):
            r = ROW.match(line)
            if not r or r.group(1) != book: continue
            extra = r.group(4)
            c, v = int(r.group(2)), int(r.group(3))
            k = re.search(r"\[(\d+)\.(\d+)\]", extra) if book in NT else None
            if k: c, v = int(k.group(1)), int(k.group(2))
            if c != ch or not (lo <= v <= hi): continue
            cols = line.rstrip("\n").split("\t")
            if (c, v) != cur:
                cur = (c, v); print(f"\n== {book}.{c}.{v}")
            if book in NT:
                word = cols[1].split(" (")[0]
                morph = cols[3].split("=")[-1]
                eds = {re.sub(r"[»«(].*", "", t) for t in cols[5].split("+")}
                tag = "" if ALL <= eds else f"  eds={cols[5]}"
                if "TR" not in eds: tag += "  [not TR]"
                # verbs: V-PAI-2P / V-AAM-2P; pronouns: P-2DP; possessive S-2P..; reflexive F-2..P
                pl = "  <2PL>" if re.search(r"^V-[A-Z0-9]+-2P|^P-2[NGDAV]P|^S-2P|^F-2[NGDAV]P", morph) else ""
                print(f"  {word:18} {cols[2][:28]:28} {morph:14}{pl}{tag}")
            else:
                ttype = r.group(6)
                morph = cols[5]
                pl = "  <2PL>" if re.search(r"2[mfc]p", morph) else ""
                print(f"  {cols[1]:20} {cols[3][:34]:34} {morph:16} {ttype if ttype!='L' else ''}{pl}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) == 2 else sys.exit(__doc__))
