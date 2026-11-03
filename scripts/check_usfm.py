#!/usr/bin/env python3
"""Validate translation files against the project's rules (docs/style-guide.md).

Usage: python3 -I scripts/check_usfm.py text/GEN.usfm [more files...]
Exit status 1 if any error is found.

Checks
  structure : \\id first; chapters 1..N in order; every verse of the KJV verse set
              present exactly once (ranges like \\v 3-4 allowed); no extra verses
  markup    : only known markers; character markers closed; nested character markers
              use the \\+ form; \\wj never nested; markers closed before the next \\v;
              footnotes closed, with a category tag
  rules     : bare LORD/GOD outside \\nd; archaisms (thee, thou, hath ...);
              "brothers and sisters" and other inclusive-language forms
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KJV = [l for l in (ROOT / "sources" / "index" / "kjv_verses.txt").read_text().split()]
USFM_IDS = ("GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH EZR NEH EST JOB PSA PRO ECC SNG "
            "ISA JER LAM EZK DAN HOS JOL AMO OBA JON MIC NAM HAB ZEP HAG ZEC MAL MAT MRK LUK JHN ACT "
            "ROM 1CO 2CO GAL EPH PHP COL 1TH 2TH 1TI 2TI TIT PHM HEB JAS 1PE 2PE 1JN 2JN 3JN JUD REV").split()

PARA = {"id", "h", "toc1", "toc2", "toc3", "mt1", "mt2", "ms1", "s1", "s2", "d", "p", "m", "b",
        "q1", "q2", "q3", "qa", "c", "v", "li1", "pi1"}
CHAR = {"add", "nd", "wj", "qt", "qs", "zpl", "it", "bd", "fqa", "ft", "fr", "f"}
NOTE_TAGS = ("Text:", "Or:", "Lit.:", "Heb.:", "Gk.:", "Aram.:", "OT:", "Note:")
ARCHAIC = re.compile(r"\b(thee|thou|thy|thine|ye|hath|doth|dost|hast|wilt|shalt|unto|verily|saith)\b", re.I)
INCLUSIVE = re.compile(r"\bbrothers and sisters\b|\bbrethren and sisters\b|\bhumankind\b|\bmankind\b"
                       r"|\bpeople of faith\b|\bhumanity\b", re.I)

TOKEN = re.compile(r"\\(\+?)([a-z0-9]+)(\*?)")


def check(path):
    errs = []
    def err(n, msg): errs.append(f"{path}:{n}: {msg}")
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    if not lines or not lines[0].startswith("\\id "):
        err(1, "file must begin with \\id")
        return errs
    book = lines[0].split()[1] if len(lines[0].split()) > 1 else ""
    if book not in USFM_IDS:
        err(1, f"unknown book id {book!r}")
        return errs
    # KJV refs use STEPBible codes ("Gen.1.1"); USFM ids are the same letters in capitals.
    expected = {r.upper(): r for r in KJV if r.split(".")[0].upper() == book}

    chapter, seen, stack = 0, set(), []
    for n, line in enumerate(lines, 1):
        m = re.match(r"\\(c|v)\s+(\d+)(?:-(\d+))?", line)
        if m and m.group(1) == "c":
            c = int(m.group(2))
            if c != chapter + 1:
                err(n, f"chapter {c} follows chapter {chapter}")
            chapter = c
        for vm in re.finditer(r"\\v\s+(\d+)(?:-(\d+))?", line):
            if stack:
                err(n, f"marker(s) {stack} still open at \\v")
                stack = []
            lo, hi = int(vm.group(1)), int(vm.group(2) or vm.group(1))
            for v in range(lo, hi + 1):
                key = f"{book}.{chapter}.{v}"
                if key not in expected:
                    err(n, f"verse {chapter}:{v} is not in the KJV verse set")
                elif key in seen:
                    err(n, f"verse {chapter}:{v} appears twice")
                else:
                    seen.add(key)
        # markers
        for t in TOKEN.finditer(line):
            plus, name, closing = t.groups()
            if name in PARA and not closing and not plus:
                continue
            if name not in CHAR:
                if name not in PARA:
                    err(n, f"unknown marker \\{name}")
                continue
            if name in ("fr", "ft", "fqa"):
                continue  # footnote content markers end at the next marker or \f*
            if closing:
                if not stack or stack[-1] != name:
                    err(n, f"\\{name}* closes {stack[-1] if stack else 'nothing'}")
                else:
                    stack.pop()
            else:
                if name == "wj" and stack:
                    err(n, "\\wj must not be nested")
                if stack and not plus and name != "f" and "f" not in stack[-1:]:
                    err(n, f"\\{name} opened inside \\{stack[-1]} must use the \\+ form")
                if plus and not stack:
                    err(n, f"\\+{name} used outside another character marker")
                stack.append(name)
                if name == "f":
                    body = line[t.end():]
                    if not any(tag in body for tag in NOTE_TAGS):
                        err(n, "footnote has no category tag (Text:/Or:/Lit.:/Heb.:/Gk.:/Aram.:/OT:/Note:)")
        # text rules (strip markers and footnote bodies first)
        plain = re.sub(r"\\f \+.*?\\f\*", "", line)
        plain_nd = re.sub(r"\\\+?nd .*?\\\+?nd\*", "", plain)
        plain_text = re.sub(r"\\\+?[a-z0-9]+\*?", "", plain_nd)
        if not line.startswith("\\id") and re.search(r"\b(LORD|GOD)\b", plain_text):
            err(n, "LORD/GOD must be inside \\nd ... \\nd*")
        if ARCHAIC.search(plain_text):
            err(n, f"archaic word: {ARCHAIC.search(plain_text).group(0)!r}")
        if INCLUSIVE.search(plain_text):
            err(n, f"inclusive-language form: {INCLUSIVE.search(plain_text).group(0)!r} (charter decision 4)")
    if stack:
        err(len(lines), f"unclosed markers at end of file: {stack}")
    missing = sorted(set(expected) - seen, key=lambda r: tuple(int(x) for x in r.split(".")[1:]))
    if missing:
        err(len(lines), f"{len(missing)} KJV verse(s) missing, first: {missing[:5]}")
    return errs


def main(argv):
    if not argv:
        sys.exit(__doc__)
    errs = [e for p in argv for e in check(p)]
    print("\n".join(errs) if errs else "OK")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
