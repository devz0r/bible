#!/usr/bin/env python3
"""Render USFM translation files to one readable HTML page.

  python3 -I scripts/render_html.py -o preview/pilot.html text/GEN.usfm text/JHN.usfm ...

Supplied words in italics, LORD in small capitals, plural "you" with a dotted
underline, words of Jesus in red, footnotes listed after each chapter.
"""
import html
import re
import sys
from pathlib import Path

CSS = """
:root{--bg:#fdfcf9;--fg:#1d1b17;--muted:#6b6458;--red:#a3261b;--rule:#e4ded2;--accent:#5b4a2e}
@media (prefers-color-scheme:dark){:root{--bg:#17150f;--fg:#ece6da;--muted:#a59c8c;--red:#ff8a7a;--rule:#3a352b;--accent:#d8c49c}}
body{background:var(--bg);color:var(--fg);font:18px/1.65 Georgia,'Times New Roman',serif;margin:0;padding:0 16px}
main{max-width:40rem;margin:2rem auto 4rem}
h1{font-size:1.9rem;margin:3rem 0 .2rem;color:var(--accent)} h2{font-size:1.3rem;margin:2rem 0 .5rem;color:var(--accent)}
h3{font:600 .95rem system-ui,sans-serif;margin:1.6rem 0 .3rem;color:var(--muted)}
.legend{font:.85rem/1.5 system-ui,sans-serif;color:var(--muted);border:1px solid var(--rule);padding:.6rem .9rem;border-radius:6px}
p{margin:.6rem 0} .q1{margin:0 0 0 1.2rem} .q2{margin:0 0 0 2.6rem} .d{font-style:italic;color:var(--muted)}
sup.v{font:600 .65em system-ui,sans-serif;color:var(--muted);margin-right:.15em}
sup.fn a{font:.7em system-ui,sans-serif;color:var(--accent);text-decoration:none;margin-left:1px}
.add{font-style:italic} .nd{font-variant:small-caps;letter-spacing:.02em}
.zpl{text-decoration:underline dotted;text-underline-offset:3px} .wj{color:var(--red)}
ol.notes{list-style:lower-alpha;font:.85rem/1.5 system-ui,sans-serif;color:var(--muted);border-top:1px solid var(--rule);padding-top:.6rem;margin-top:1.4rem}
ol.notes b{color:var(--fg)} ol.notes i{color:var(--fg)}
"""
TAGS = ("Text:", "Or:", "Lit.:", "Heb.:", "Gk.:", "Aram.:", "OT:", "Note:")


def inline(s):
    """Convert character markers inside a run of text to HTML."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\\\+?(add|nd|zpl|wj|qt|it|bd)\*", "</span>", s)
    s = re.sub(r"\\\+?(add|nd|zpl|wj|qt|it|bd) ", lambda m: f'<span class="{m.group(1)}">', s)
    s = re.sub(r"\\qs (.*?)\\qs\*", r'<span class="add">\1</span>', s)
    return s


def letter(n):
    """1 -> a, 26 -> z, 27 -> aa"""
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(97 + r) + s
    return s


def note_html(body):
    body = re.sub(r"^\\fr \S+ ", "", body.strip())
    parts = re.split(r"\\(ft|fqa) ", body)
    out, mode = [], "ft"
    for i, part in enumerate(parts):
        if part in ("ft", "fqa") and i % 2 == 1:
            mode = part
            continue
        text = inline(part)
        out.append(f"<i>{text}</i>" if mode == "fqa" else text)
    s = "".join(out)
    for t in TAGS:
        if s.startswith(t):
            s = f"<b>{t}</b>{s[len(t):]}"
            break
    return s


def render(path):
    src = Path(path).read_text(encoding="utf-8")
    title = re.search(r"^\\mt1 (.*)$", src, re.M).group(1)
    out = [f"<h1>{html.escape(title)}</h1>"]
    notes, chapter, block = [], None, None

    def flush_notes():
        if notes:
            out.append('<ol class="notes">' + "".join(
                f'<li id="{nid}">{txt}</li>' for nid, txt in notes) + "</ol>")
            notes.clear()

    def close_block():
        nonlocal block
        if block:
            out.append("</p>")
            block = None

    book = Path(path).stem
    for line in src.split("\n"):
        m = re.match(r"\\(\w+)\s?(.*)$", line)
        if not m:
            continue
        mk, rest = m.groups()
        if mk in ("id", "h", "toc1", "toc2", "toc3", "mt1"):
            continue
        if mk == "c":
            close_block(); flush_notes()
            chapter = rest.strip()
            out.append(f"<h2>Chapter {chapter}</h2>")
            continue
        if mk == "s1":
            close_block(); out.append(f"<h3>{inline(rest)}</h3>"); continue
        if mk in ("p", "m", "q1", "q2", "d", "b"):
            close_block()
            cls = {"p": "p", "m": "p", "q1": "q1", "q2": "q2", "d": "d", "b": "p"}[mk]
            out.append(f'<p class="{cls}">'); block = cls
            if not rest:
                continue
            line = rest
        elif mk != "v":
            continue
        # replace footnotes with links, verses with superscripts
        def fn(mt):
            nid = f"{book}-{chapter}-{len(notes) + 1}"
            notes.append((nid, note_html(mt.group(1))))
            return f'\x00{nid}\x00'
        line = re.sub(r"\\f \+ (.*?)\\f\*", fn, line)
        line = re.sub(r"^\\v (\d+) ", lambda mt: f"\x01{mt.group(1)}\x01", line)
        line = inline(line)
        line = re.sub(r"\x01(\d+)\x01", r'<sup class="v">\1</sup>', line)
        line = re.sub(r"\x00(.*?)\x00", lambda mt: f'<sup class="fn"><a href="#{mt.group(1)}">{letter(int(mt.group(1).rsplit("-", 1)[1]))}</a></sup>', line)
        if block is None:
            out.append('<p class="p">'); block = "p"
        out.append(line + " ")
    close_block(); flush_notes()
    return "\n".join(out)


def main(argv):
    if len(argv) < 3 or argv[0] != "-o":
        sys.exit(__doc__)
    dest, files = Path(argv[1]), argv[2:]
    body = "\n".join(render(f) for f in files)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Pilot Passages</title><style>{CSS}</style></head>
<body><main><p class="legend"><b>Pilot draft, not reviewed.</b> <span class="add">Italics</span>: words supplied in English.
<span class="nd">LORD</span>: the divine name. <span class="zpl">Dotted underline</span>: “you” is plural in the original.
<span class="wj">Red</span>: words of Jesus. Lettered notes follow each chapter.</p>
{body}</main></body></html>
""", encoding="utf-8")
    print(f"wrote {dest}")


if __name__ == "__main__":
    main(sys.argv[1:])
