#!/usr/bin/env python3
"""Build per-verse source indexes from the raw STEPBible data.

Reads  sources/raw/{TAHOT_*.txt, TAGNT_*.txt, KJV.csv}
Writes sources/index/NT.tsv  - one row per verse: TR / NA28 / SBL / Byz Greek text
       sources/index/OT.tsv  - one row per verse: Hebrew text (Leningrad, Qere followed)
                               plus flags (restored text, LXX-based additions, Ketiv/Qere)
       sources/index/REPORT.txt - verse-count comparison against the KJV

Versification: the KJV verse set is the project standard (charter decision 6).
TAGNT gives NRSV references with KJV differences in [square brackets]; this
script keys NT verses by the KJV reference when one is given.

Run:  python3 -I scripts/build_index.py
"""
import csv
import re
import sys
from collections import OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "sources" / "raw"
OUT = ROOT / "sources" / "index"

# KJV.csv book name -> STEPBible three/four-letter code
BOOKS = OrderedDict([
    ("Genesis", "Gen"), ("Exodus", "Exo"), ("Leviticus", "Lev"), ("Numbers", "Num"),
    ("Deuteronomy", "Deu"), ("Joshua", "Jos"), ("Judges", "Jdg"), ("Ruth", "Rut"),
    ("1 Samuel", "1Sa"), ("2 Samuel", "2Sa"), ("1 Kings", "1Ki"), ("2 Kings", "2Ki"),
    ("1 Chronicles", "1Ch"), ("2 Chronicles", "2Ch"), ("Ezra", "Ezr"), ("Nehemiah", "Neh"),
    ("Esther", "Est"), ("Job", "Job"), ("Psalms", "Psa"), ("Proverbs", "Pro"),
    ("Ecclesiastes", "Ecc"), ("Song of Solomon", "Sng"), ("Isaiah", "Isa"),
    ("Jeremiah", "Jer"), ("Lamentations", "Lam"), ("Ezekiel", "Ezk"), ("Daniel", "Dan"),
    ("Hosea", "Hos"), ("Joel", "Jol"), ("Amos", "Amo"), ("Obadiah", "Oba"),
    ("Jonah", "Jon"), ("Micah", "Mic"), ("Nahum", "Nam"), ("Habakkuk", "Hab"),
    ("Zephaniah", "Zep"), ("Haggai", "Hag"), ("Zechariah", "Zec"), ("Malachi", "Mal"),
    ("Matthew", "Mat"), ("Mark", "Mrk"), ("Luke", "Luk"), ("John", "Jhn"),
    ("Acts", "Act"), ("Romans", "Rom"), ("1 Corinthians", "1Co"), ("2 Corinthians", "2Co"),
    ("Galatians", "Gal"), ("Ephesians", "Eph"), ("Philippians", "Php"),
    ("Colossians", "Col"), ("1 Thessalonians", "1Th"), ("2 Thessalonians", "2Th"),
    ("1 Timothy", "1Ti"), ("2 Timothy", "2Ti"), ("Titus", "Tit"), ("Philemon", "Phm"),
    ("Hebrews", "Heb"), ("James", "Jas"), ("1 Peter", "1Pe"), ("2 Peter", "2Pe"),
    ("1 John", "1Jn"), ("2 John", "2Jn"), ("3 John", "3Jn"), ("Jude", "Jud"),
    ("Revelation", "Rev"),
])
CODE_ORDER = list(BOOKS.values())

ROW = re.compile(r"^([1-3]?[A-Za-z]+)\.(\d+)\.(\d+)([^#\t]*)#(\d+)=([^\t]+)\t")


def book_code(name):
    """Map a KJV.csv book name (which uses Roman numerals) to a code."""
    name = name.strip()
    for roman, arabic in (("III ", "3 "), ("II ", "2 "), ("I ", "1 ")):
        if name.startswith(roman):
            name = arabic + name[len(roman):]
            break
    if name.startswith("Revelation"):
        name = "Revelation"
    return BOOKS.get(name)


def kjv_verses():
    """Return {(code, chapter, verse)} from KJV.csv, and book-name warnings."""
    seen, unknown = set(), set()
    with open(RAW / "KJV.csv", encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            code = book_code(row["Book"])
            if code is None:
                unknown.add(row["Book"])
                continue
            seen.add((code, int(row["Chapter"]), int(row["Verse"])))
    return seen, unknown


def first_word(field):
    """'Βίβλος (Biblos)' -> 'Βίβλος'."""
    return field.split(" (")[0].strip()


def parse_nt():
    verses = OrderedDict()
    for fn in ("TAGNT_Mat-Jhn.txt", "TAGNT_Act-Rev.txt"):
        for line in open(RAW / fn, encoding="utf-8-sig"):
            m = ROW.match(line)
            if not m:
                continue
            code, ch, vs, extra, pos, wtype = m.groups()
            cols = line.rstrip("\n").split("\t")
            # Reference is NRSV; a [kjv] bracket gives the KJV reference.
            kjv = re.search(r"\[(\d+)\.(\d+)\]", extra)
            if kjv:
                ch, vs = kjv.group(1), kjv.group(2)
            key = (code, int(ch), int(vs))
            eds = {re.sub(r"[»«(].*", "", t) for t in cols[5].split("+")}
            greek = first_word(cols[1])
            rec = verses.setdefault(key, {"TR": [], "NA28": [], "SBL": [], "Byz": []})
            for ed in rec:
                if ed in eds:
                    rec[ed].append(greek)
    return verses


def parse_ot():
    verses = OrderedDict()
    for fn in ("TAHOT_Gen-Deu.txt", "TAHOT_Jos-Est.txt", "TAHOT_Job-Sng.txt", "TAHOT_Isa-Mal.txt"):
        for line in open(RAW / fn, encoding="utf-8-sig"):
            m = ROW.match(line)
            if not m:
                continue
            code, ch, vs, extra, pos, wtype = m.groups()
            if code == "Ezk":  # defensive; STEPBible uses 'Eze'
                pass
            cols = line.rstrip("\n").split("\t")
            key = (code, int(ch), int(vs))
            rec = verses.setdefault(key, {"words": [], "flags": set()})
            kind = wtype[0]  # L, Q, K, R, X (variants follow in brackets)
            heb = cols[1].replace("/", "").replace("\\", "")
            if kind in "LQR":
                rec["words"].append(heb)
            if kind == "R":
                rec["flags"].add("restored")
            if kind == "X":
                rec["flags"].add("lxx-addition")
            if kind == "Q":
                rec["flags"].add("qere")
            if re.search(r"\((?:[^)]*\+)?[dD]\b", wtype) or "(D" in wtype:
                rec["flags"].add("dss-variant")
            if re.search(r"\((?:[^)]*\+)?[hH]\b", wtype):
                rec["flags"].add("ben-hayyim-variant")
    return verses


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    kjv, unknown = kjv_verses()
    nt, ot = parse_nt(), parse_ot()
    report = []
    if unknown:
        report.append(f"WARNING: unknown KJV.csv book names: {sorted(unknown)}")

    def sort_key(k):
        return (CODE_ORDER.index(k[0]) if k[0] in CODE_ORDER else 999, k[1], k[2])

    with open(OUT / "NT.tsv", "w", encoding="utf-8") as fh:
        fh.write("ref\tTR\tNA28\tSBL\tByz\ttr_differs_from_na28\n")
        for k in sorted(nt, key=sort_key):
            r = nt[k]
            diff = "yes" if r["TR"] != r["NA28"] else ""
            fh.write(f"{k[0]}.{k[1]}.{k[2]}\t" + "\t".join(" ".join(r[e]) for e in ("TR", "NA28", "SBL", "Byz")) + f"\t{diff}\n")
    with open(OUT / "OT.tsv", "w", encoding="utf-8") as fh:
        fh.write("ref\thebrew\tflags\n")
        for k in sorted(ot, key=sort_key):
            r = ot[k]
            fh.write(f"{k[0]}.{k[1]}.{k[2]}\t{' '.join(r['words'])}\t{','.join(sorted(r['flags']))}\n")

    # Verse-count comparison against the KJV (verse 0 = Psalm titles, not counted).
    ours = {k for k in list(nt) + list(ot) if k[2] != 0}
    missing = sorted(kjv - ours, key=sort_key)
    extra = sorted(ours - kjv, key=sort_key)
    report.append(f"KJV verses: {len(kjv)}  source verses (excl. v0): {len(ours)}")
    report.append(f"In KJV but not in source data ({len(missing)}):")
    report += [f"  {a}.{b}.{c}" for a, b, c in missing]
    report.append(f"In source data but not in KJV ({len(extra)}):")
    report += [f"  {a}.{b}.{c}" for a, b, c in extra]
    n_tr_diff = sum(1 for r in nt.values() if r["TR"] != r["NA28"])
    report.append(f"NT verses where TR text differs from NA28: {n_tr_diff} of {len(nt)}")
    (OUT / "kjv_verses.txt").write_text(
        "".join(f"{a}.{b}.{c}\n" for a, b, c in sorted(kjv, key=sort_key)), encoding="utf-8")
    (OUT / "REPORT.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report[:12]))
    print(f"... full report: {OUT / 'REPORT.txt'}")


if __name__ == "__main__":
    sys.exit(main())
