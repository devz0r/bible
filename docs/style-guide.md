# Style Guide

Companion to the [charter](charter.md). Defines how the English reads and how the text is marked up. Key-term renderings are in the [glossary](glossary.md).

---

## 1. English

- **Spelling and punctuation:** American. Curly quotation marks. Serial comma.
- **Register:** plain, dignified, modern. Not chatty, not slangy, no contractions in the main text (except in direct speech, where natural speech calls for them — use sparingly).
- **No archaisms:** no *thee, thou, thy, ye, -eth, -est, hath, doth, verily, unto, wist, shew*.
- **Sentence length:** follow the shape of the original where English allows. Paul's long sentences may be divided at natural joints, but each logical connective (*for, therefore, so that, because*) is kept. Hebrew narrative chains of *wayyiqtol* verbs ("and … and … and") may be rendered with *and, then, so, but* or new sentences as context requires. Do not reduce them to unconnected statements.
- **Capitalization:**
  - Pronouns for God are **lowercase** (he, him, his, you).
  - *Spirit* is capitalized when the Holy Spirit is clearly meant. When it is uncertain whether the Spirit of God or a human spirit, wind or breath is meant, choose by context and add a meaning note.
  - Titles: *Son of Man* (as a title of Jesus), *the Christ* (as a title in the Gospels and Acts), *Most High*, *Holy One of Israel*.
- **Numbers:** spell out one to ninety-nine and round numbers (three hundred, a thousand); use numerals for large exact figures (Numbers 1:46: 603,550).
- **Names:** use standard KJV-tradition English spellings (Isaiah, not Yeshayahu; Elijah, not Elias, even in the NT — the NT form is noted). The Greek forms in the KJV NT (Elias, Esaias, Jesus for Joshua in Acts 7:45 and Hebrews 4:8) are normalized to the OT spellings, with a note.
- **Measures, money and time:** keep the original unit (cubit, ephah, shekel, talent, denarius, the third hour). Give the modern equivalent in a note at the first occurrence in each book.

## 2. Supplied words (KJV italics)

Mark with `\add ...\add*` (rendered in *italics*).

**Mark** words that add content not present in the source:
- Nouns supplied for elliptical adjectives: "the rich *man*", "these *things*".
- Words added to clarify reference: "he said to *Jesus*" when the Greek has only "him". Prefer keeping "him" when the meaning is clear.
- Verbs supplied in elliptical clauses: "I am *he*" (John 8:24).

**Do not mark** what English grammar requires automatically:
- The copula in Hebrew nominal clauses ("The LORD *is* my shepherd" → "is" is not marked).
- Articles, and "of" in Hebrew construct chains.
- Auxiliary verbs used to express tense, mood or aspect.
- Pronoun subjects expressed by Greek or Hebrew verb endings.

When in doubt, mark it.

## 3. Plural "you"

Every second-person **plural** pronoun or verb (Hebrew or Greek) is marked with the custom USFM marker `\zpl ...\zpl*`. Mark it mechanically from the morphology, everywhere, not only where context is unclear. Singular "you" is unmarked.

Mark the pronoun or possessive (*you, your, yours, yourselves*). Where a plural verb has no English pronoun (an imperative like "Repent!"), mark the verb.

The visual rendering for print and web will be fixed during the pilot. The data must be marked from the first chapter onward.

## 4. The divine name and divine titles

| Hebrew | Rendering | USFM |
|---|---|---|
| YHWH | LORD | `\nd LORD\nd*` |
| Adonai YHWH | Lord GOD | `Lord \nd GOD\nd*` |
| YHWH Adonai (rare order) | GOD the Lord | `\nd GOD\nd* the Lord` |
| YH (short form, Exodus 15:2; Psalms; Isaiah 12:2) | LORD | `\nd LORD\nd*` + note "Hebrew *Yah*" |
| *Hallelu-yah* | Praise the LORD | note "Hebrew *Hallelujah*" |
| Place and memorial names containing YHWH | Translated with hyphens, e.g. "The-LORD-Will-Provide" (Genesis 22:14) | note gives the Hebrew (*YHWH Yireh*) and the KJV form (*Jehovah-jireh*) |

**NT quotations of OT passages that contain YHWH:** render *kyrios* as LORD (`\nd`) and note at the first occurrence in each book that the Greek *Kyrios* here stands for the divine name.

## 5. Footnotes

USFM: `\f + \fr C:V \ft text\f*`. Each note **begins with a category tag** in bold so readers can scan or filter them:

| Tag | Use | Example |
|---|---|---|
| **Text:** | Manuscript differences | **Text:** TR, Majority: *And the Lord said*. Critical text (NA28/SBLGNT) omits. |
| **Or:** | A legitimate alternative rendering | **Or:** *wind* |
| **Lit.:** | The literal wording behind a natural rendering | **Lit.:** *gird up the loins of your mind* |
| **Heb.:** / **Gk.:** / **Aram.:** | Explanation of a source word | **Gk.:** *pneuma*, meaning both "wind" and "spirit"; Jesus plays on both senses. |
| **OT:** | Source of an OT quotation or allusion | **OT:** Isaiah 40:3 |
| **Note:** | Historical, cultural or measurement information | **Note:** A denarius was a laborer's daily wage. |

### Rules for notes

- **Be brief.** One or two sentences. Notes inform. They do not preach or argue.
- **Be fair.** When scholars or traditions disagree, state the options neutrally. Do not ridicule any tradition, including KJV-only and critical-text positions.
- **Textual notes** name the reading in the text, the alternative, and which editions support each: **TR** (Scrivener 1894), **Maj.** (Robinson-Pierpont), **CT** (NA28/SBLGNT). For OT: **MT**, **DSS**, **LXX**, **SP** (Samaritan Pentateuch), **Syr.**, **Vg.** For major passages (Mark 16:9–20, John 7:53–8:11, 1 John 5:7–8), the note briefly summarizes the manuscript evidence, including the date of the earliest Greek witnesses.
- **Do not note trivial variants** that make no difference in English (spelling, word order, *movable nu*).
- **Glossary terms** get a note at their first occurrence **in each book**, not at every occurrence, unless the sense departs from the glossary default.
- **Transliteration:** simple, readable transliteration (*hesed*, *nephesh*, *pneuma*, *logos*). No scholarly diacritics except long marks on Greek *ē* and *ō* where helpful.

## 6. Other USFM markup

| Feature | Marker |
|---|---|
| Book identification | `\id GEN Transparent Bible (working title)` |
| Headings (section titles — editorial, not part of the text) | `\s1` |
| Psalm superscriptions (part of the Hebrew text) | `\d` |
| Paragraphs | `\p`; poetry lines `\q1`, `\q2` |
| Words of Jesus | `\wj ...\wj*` |
| Quotation of OT in NT | `\qt ...\qt*` (optional) |
| Selah | `\qs Selah\qs*` |

**Section headings** are editorial. They are kept short and neutral, and they never interpret disputed passages.

**Poetry** is set as poetry (Psalms, Proverbs, Job, Song of Songs, most of the Prophets, and poetic passages elsewhere). The lines follow the Hebrew parallelism.

## 7. Sample

Luke 22:31–32. It shows a textual note, the plural-you marker and the words of Jesus.

```
\v 31 And the Lord said,\f + \fr 22:31 \ft \bd Text:\bd* TR, Maj.: \it And the Lord said\it*. CT omits.\f* “\wj Simon, Simon, behold, Satan has demanded to have \zpl you\zpl*, that he may sift \zpl you\zpl* like wheat,\wj*
\v 32 \wj but I have prayed for you, that your faith may not fail. And when you have turned back, strengthen your brothers.\wj*”
```

The rendered output: Satan demanded to have *you all*, but Jesus prayed for *you, Peter*.
