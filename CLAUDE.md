# Instructions for Claude

## Every reply

**Start every reply with the ideal model and effort level for the user's prompt**, in one line, with a few words on why. For example:

> **Ideal model for this prompt: Opus 5.5 at high effort.** Drafting narrative text at volume.

Available models: Fable 5.1 (most capable, most expensive), Opus 5.5, Sonnet 5.5, Haiku 5.5. Effort levels: low, medium, high, xhigh, max. The stage-by-stage defaults are:

| Stage | Model | Effort |
|---|---|---|
| Charter, style guide, glossary changes | Fable 5.1 | xhigh |
| Source data, scripts, file formats | Sonnet 5.5 | medium |
| Drafting narrative books and most letters | Opus 5.5 | high |
| Drafting poetry, prophets, Job, Romans, Hebrews | Fable 5.1 | high |
| Reviewing a draft against the source | The model that did *not* draft it | high |
| Textual cruxes and disputed passages | Fable 5.1 | max |
| Consistency checks | Sonnet 5.5 + scripts | medium |
| Formatting and exports | Sonnet 5.5 (Haiku 5.5 for bulk validation) | low |

## The project

An English Bible translation that is accurate, readable and transparent. Before any translation work, read and follow:

1. `docs/charter.md` — decisions and principles (this wins any conflict).
2. `docs/style-guide.md` — English style and USFM markup.
3. `docs/glossary.md` — key-term renderings.

## Rules

- **Translate from the source-text files in `sources/`, never from memory alone.** If the source files are missing, set them up first or stop and say so.
- **No gender-inclusive language** (the project owner's decision; charter decision 4).
- **Every rule change** goes into the charter's decision log (§8), and must be applied to chapters that are already translated.
- **Never silently depart from the glossary.** Either follow it or add a note and update the glossary.
- Mark supplied words (`\add`), plural "you" (`\zpl`), the divine name (`\nd`) and the words of Jesus (`\wj`) from the first draft onward. Inside `\wj` or inside a footnote, use the nested `\+` form (`\+zpl ...\+zpl*`).
- Before drafting a chapter, check `docs/glossary.md` §I (passages that always require a note) for that chapter.
- Footnotes are brief, fair to all traditions, and begin with a category tag (**Text:**, **Or:**, **Lit.:**, **Heb.:**, **Gk.:**, **OT:**, **Note:**).
- Update `PROGRESS.md` when a chapter changes status.
