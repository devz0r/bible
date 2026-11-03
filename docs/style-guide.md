# Style Guide

Companion to the [charter](charter.md). Defines how the English reads and how the text is marked up. Key-term renderings are in the [glossary](glossary.md).

---

## 1. English

- **Spelling and punctuation:** American. Curly quotation marks. Serial comma.
- **Register:** plain, dignified, modern. Not chatty, not slangy, no contractions in the main text (except in direct speech, where natural speech calls for them — use sparingly).
- **No archaisms:** no *thee, thou, thy, ye, -eth, -est, hath, doth, verily, unto, wist, shew*. A few traditional words that are still understood are kept, because they are precise: *behold, blessed, hallowed* (Lord's Prayer only), *iniquity, transgression, righteousness, covenant*. See the appendix for KJV words that are replaced because their meaning has changed.
- **Possessives:** *Jesus'*, *Moses'* (no second *s* after a name ending in *s*).
- **Sentence length:** follow the shape of the original where English allows. Paul's long sentences may be divided at natural joints, but each logical connective (*for, therefore, so that, because*) is kept. Hebrew narrative chains of *wayyiqtol* verbs ("and … and … and") may be rendered with *and, then, so, but* or new sentences as context requires. Do not reduce them to unconnected statements.
- **Capitalization:**
  - Pronouns for God are **lowercase** (he, him, his, you).
  - *Spirit* is capitalized when the Holy Spirit is clearly meant. When it is uncertain whether the Spirit of God or a human spirit, wind or breath is meant, choose by context and add a meaning note.
  - Titles: *Son of Man* (as a title of Jesus), *the Christ* (as a title in the Gospels and Acts), *Most High*, *Holy One of Israel*.
  - *Scripture(s)*, *the Law and the Prophets* (as divisions of the canon), *Sabbath*, *Passover*, *Day of Atonement*, *the Spirit*. Lowercase: *law* (as a concept, even the law of Moses), *gospel* (as the message), *temple*, *tabernacle*, *heaven*, *kingdom of God*.
- **Numbers:** spell out one to ninety-nine and round numbers (three hundred, a thousand); use numerals for large exact figures (Numbers 1:46: 603,550).
- **Names:** use standard KJV-tradition English spellings (Isaiah, not Yeshayahu). One spelling per person or place across both Testaments. The Greek forms in the KJV NT (Elias, Esaias, Jeremy, Osee, Noe, Sion, Agar, Charran, Jesus for Joshua in Acts 7:45 and Hebrews 4:8) are normalized to the OT spellings (Elijah, Isaiah, Jeremiah, Hosea, Noah, Zion, Hagar, Haran, Joshua), with a note at the first occurrence in each book. Where the OT itself spells one name two ways (Jehoram/Joram, Azariah/Uzziah), each spelling is kept where it occurs, with a note. Transliterated words that the Greek text itself leaves untranslated (*Abba*, *Hosanna*, *Hallelujah*, *Maranatha*, *Raca*, *Corban*, *Talitha cumi*, *Ephphatha*, *Eli, Eli, lama sabachthani*, *mammon*, *Golgotha*, *Rabbi*, *Cephas*) stay transliterated, with the translation in a note where the text does not give one.
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

Every second-person **plural** pronoun or verb (Hebrew or Greek) is marked with the custom USFM marker `\zpl ...\zpl*` (declared in `usfm/custom.sty` when the data is set up). Mark it mechanically from the morphology, everywhere, not only where context is unclear. Singular "you" is unmarked. Do not interpret: where Deuteronomy switches between singular and plural "you" in one speech, mark exactly what the Hebrew has.

Mark the pronoun or possessive (*you, your, yours, yourselves*). Where a plural verb has no English pronoun (an imperative like "Repent!"), mark the verb.

Inside another character marker (for example, inside `\wj`), use the nested form `\+zpl ...\+zpl*` (see §6).

The visual rendering for print and web will be fixed during the pilot. The data must be marked from the first chapter onward.

## 4. The divine name and divine titles

| Hebrew | Rendering | USFM |
|---|---|---|
| YHWH | LORD | `\nd LORD\nd*` |
| Adonai YHWH | Lord GOD | `Lord \nd GOD\nd*` |
| YHWH Adonai (rare order) | GOD the Lord | `\nd GOD\nd* the Lord` |
| YH (short form, Exodus 15:2; 17:16; Psalms; Isaiah 12:2; 26:4) | LORD | `\nd LORD\nd*` + note "Hebrew *Yah*". At Psalm 68:4 the note adds "KJV *JAH*". |
| *Hallelu-yah* | Praise the LORD | note "Hebrew *Hallelujah*" |
| Place and memorial names containing YHWH | Translated with hyphens, e.g. "The-LORD-Will-Provide" (Genesis 22:14) | note gives the Hebrew (*YHWH Yireh*) and the KJV form (*Jehovah-jireh*) |

**NT quotations of OT passages that contain YHWH:** render *kyrios* as LORD (`\nd`) wherever the Hebrew of the quoted passage has YHWH, and note at the first occurrence in each book that the Greek *Kyrios* here stands for the divine name. The rule is mechanical: it follows the Hebrew source, not the NT referent (so Romans 10:13, quoting Joel 2:32, has LORD; Hebrews 1:10, where the Greek *kyrie* has no YHWH behind it in Psalm 102:25, has "Lord").

## 5. Footnotes

Each note **begins with a category tag** so readers can scan or filter them. The tag is plain text in the USFM; output tooling renders it in bold.

| Tag | Use | Rendered example |
|---|---|---|
| **Text:** | Manuscript differences | **Text:** TR, Maj.: *And the Lord said.* CT omits. |
| **Or:** | A legitimate alternative rendering | **Or:** *wind* |
| **Lit.:** | The literal wording behind a natural rendering | **Lit.:** *gird up the loins of your mind* |
| **Heb.:** / **Gk.:** / **Aram.:** | Explanation of a source word | **Gk.:** *pneuma*, meaning both "wind" and "spirit"; Jesus plays on both senses. |
| **OT:** | Source of an OT quotation or allusion | **OT:** Isaiah 40:3 |
| **Note:** | Historical, cultural or measurement information | **Note:** A denarius was a laborer's daily wage. |

### USFM templates

Alternative wordings go in `\fqa` (footnote alternative translation); everything else goes in `\ft`. Copy these exactly:

```
\f + \fr 3:8 \ft Or: \fqa wind\f*
\f + \fr 1:13 \ft Lit.: \fqa gird up the loins of your mind\f*
\f + \fr 22:31 \ft Text: TR, Maj.: \fqa And the Lord said. \ft CT omits.\f*
\f + \fr 3:8 \ft Gk.: \fqa pneuma\ft , meaning both “wind” and “spirit”; Jesus plays on both senses.\f*
\f + \fr 3:3 \ft OT: Isaiah 40:3\f*
\f + \fr 20:2 \ft Note: A denarius was a laborer’s daily wage.\f*
```

A character marker inside a footnote uses the nested `\+` form: `\ft Heb.: \+nd LORD\+nd* is my banner`.

### Rules for notes

- **Be brief.** One or two sentences. Notes inform. They do not preach or argue.
- **Be fair.** When scholars or traditions disagree, state the options neutrally. Do not ridicule any tradition, including KJV-only and critical-text positions.
- **Textual notes** name the reading in the text, the alternative, and which editions support each: **TR** (Scrivener 1894), **Maj.** (Robinson-Pierpont), **CT** (NA28/SBLGNT). For OT: **MT**, **DSS**, **LXX**, **SP** (Samaritan Pentateuch), **Syr.**, **Vg.** For major passages (Mark 16:9–20, John 7:53–8:11, 1 John 5:7–8), the note briefly summarizes the manuscript evidence, including the date of the earliest Greek witnesses.
- **Do not note trivial variants** that make no difference in English (spelling, word order, *movable nu*).
- **Glossary terms** get a note at their first occurrence **in each book**, not at every occurrence, unless the sense departs from the glossary default.
- **Transliteration:** simple, readable transliteration (*hesed*, *nephesh*, *pneuma*, *logos*). No scholarly diacritics except long marks on Greek *ē* and *ō* where helpful.

## 6. Other USFM markup

Every book file begins with this header (Genesis shown):

```
\id GEN Transparent Bible (working title)
\h Genesis
\toc1 The First Book of Moses, Called Genesis
\toc2 Genesis
\toc3 Gen
\mt1 Genesis
\c 1
\s1 The Creation
\p
\v 1 In the beginning God created the heavens and the earth.
```

| Feature | Marker |
|---|---|
| Chapter, verse | `\c`, `\v` |
| Headings (section titles — editorial, not part of the text) | `\s1` |
| Major divisions (the five Books of the Psalms) | `\ms1` |
| Psalm superscriptions (part of the Hebrew text) | `\d`, placed after `\c` and before the first `\q1` |
| Hebrew letter headings in Psalm 119 (as the KJV prints them) | `\qa Aleph` |
| Paragraphs | `\p`; continuation without indent `\m`; blank line `\b` |
| Poetry lines | `\q1`, `\q2` (the second line of a parallel pair is `\q2`) |
| Supplied words | `\add ...\add*` |
| Plural "you" | `\zpl ...\zpl*` |
| The divine name | `\nd LORD\nd*` |
| Words of Jesus | `\wj ...\wj*` |
| Quotation of OT in NT | `\qt ...\qt*` (optional) |
| Selah | `\qs Selah\qs*` |
| Footnote | `\f + \fr C:V \ft ...\f*` (see §5) |

**Nesting.** USFM 3 requires that a character marker inside another character marker use the `\+` form, and the closing marker matches: `\wj … \+zpl you\+zpl* … \+add he\+add* … \+nd LORD\+nd* …\wj*`. The same applies inside footnotes. Never nest `\wj` inside anything.

**Verse boundaries.** Close every character marker before `\v` and reopen it after. A `\wj` speech that runs over several verses is closed and reopened at each verse.

**Section headings** are editorial. They are kept short and neutral, and they never interpret disputed passages.

**Poetry** is set as poetry (Psalms, Proverbs, Job, Song of Songs, Lamentations, most of the Prophets, and poetic passages elsewhere, such as Genesis 49, Exodus 15, Deuteronomy 32–33, Judges 5, 2 Samuel 22, Luke 1:46–55, 68–79). The lines follow the Hebrew parallelism.

## 7. Hebrew and Greek grammar

Rules for the recurring grammar questions. These are defaults, and context always wins.

**Hebrew verbs** have aspect, not tense. Translate by context: *wayyiqtol* in narrative as simple past; *qatal* as past or present perfect; *yiqtol* as future, habitual present, or modal ("would", "may", "must") as the context requires. A "prophetic perfect" (a *qatal* for a future event spoken of as done) is rendered as the English tense the context requires, and an **Or:** note gives the other tense where it affects the meaning (Isaiah 9:6; 53:4–6).

**Greek aorist** is normally simple past in narrative. Do not overtranslate aspect ("began to", "kept on", "once for all") unless the context clearly carries it. **Present imperatives and prohibitions** are not automatically "stop doing" or "keep on doing". **Perfects** are rendered with English present perfect or present as context requires ("it is written", "I have fought the good fight").

**Historical present** (Mark and John use the present tense in past narrative: "Jesus says to him") is rendered as English past tense, with no note.

**Hebrew *waw* consecutive** and verse-initial "and": see the charter, §3. Do not reduce narrative chains to unconnected sentences.

**Cohortatives and jussives** ("let us", "let there be", "may he") are kept.

**Emphatic constructions** (the infinitive absolute: "you shall surely die", "dying you shall die") are rendered with "surely", "indeed" or a similar word, not by repeating the verb.

## 8. Wordplay, acrostics and sounds

**Wordplay that English cannot reproduce** gets a **Heb.:** or **Gk.:** note explaining it: Genesis 2:23 (*'ish* / *'ishshah*, "man" / "woman"); Genesis 2:25–3:1 (*'arummim*, "naked" / *'arum*, "crafty"); Isaiah 5:7 (*mishpat* / *mispach*, *tsedaqah* / *tse'aqah*); Jeremiah 1:11–12 (*shaqed*, "almond" / *shoqed*, "watching"); Amos 8:1–2 (*qayits*, "summer fruit" / *qets*, "end"); Micah 1:10–15 (place names); Matthew 16:18 (*Petros* / *petra*); John 3:3–8 (*anōthen*, "again" / "from above"; *pneuma*, "wind" / "Spirit").

**Name explanations.** Where the text explains a name (Genesis 4:1; 5:29; 17:5; 25:26; 29:32–30:24; 1 Samuel 1:20), the note gives the Hebrew word and its sound-link to the name.

**Acrostics** (Psalms 9–10, 25, 34, 37, 111, 112, 119, 145; Proverbs 31:10–31; Lamentations 1–4; Nahum 1:2–8 in part) get a **Note:** at the first verse saying that the passage is an alphabetical acrostic in Hebrew. Psalm 119 keeps the Hebrew letter headings (`\qa`). No attempt is made to reproduce the acrostic in English.

**Musical and liturgical terms** in the Psalm titles (*Selah*, *Higgaion*, *Maskil*, *Miktam*, *Shiggaion*, *Sheminith*, *Gittith*, *Alamoth*, *Muth-labben*, *Jeduthun*) are transliterated, as in the KJV, with a **Heb.:** note at the first occurrence saying the meaning is uncertain and giving the leading suggestions.

## 9. Other recurring questions

**Words of Jesus (`\wj`).** Mark every direct quotation of Jesus' speech in the Gospels, in Acts (9:4–6, 10–16; 18:9–10; 20:35; 22:7–10, 18–21; 23:11; 26:14–18), in 2 Corinthians 12:9 and in Revelation (1:8, 11, 17–20; chapters 2–3; 16:15; 21:5–8 in part; 22:7, 12–16, 20). Where it is uncertain whether Jesus' speech continues (John 3:16–21 and 3:31–36), follow the traditional red-letter practice of marking it, and add a **Note:** saying that the Greek has no quotation marks and the speech may end earlier.

**Euphemisms and blunt language.** Where the original uses an idiom that is intelligible in English, keep it ("he knew his wife"; "uncover the nakedness of"). Where the literal idiom would be unintelligible or misread, use the natural English and add a **Lit.:** note ("every male" with the note "Lit. *one who urinates against a wall*", 1 Samuel 25:22; "relieve himself" with "Lit. *cover his feet*", 1 Samuel 24:3). Do not make the text more delicate than the original is (Ezekiel 16 and 23; Isaiah 64:6; Philippians 3:8).

**Pronoun reference.** Keep "he", "him" and "they" where the reference is clear from context. Supply a name in `\add` only where the English would otherwise be genuinely ambiguous.

**Ancient units.** Keep the original unit in the text (see §1). A table of equivalents will be kept in `docs/units.md` once the first books are drafted, and every unit gets a **Note:** at its first occurrence in each book.

## 10. Sample

Luke 22:31–32. It shows a textual note, the plural-you marker (nested inside `\wj`) and the words of Jesus.

```
\p
\v 31 And the Lord said,\f + \fr 22:31 \ft Text: TR, Maj.: \fqa And the Lord said. \ft CT omits.\f* “\wj Simon, Simon, behold, Satan has demanded to have \+zpl you\+zpl*, that he may sift \+zpl you\+zpl* like wheat,\wj*
\v 32 \wj but I have prayed for you, that your faith may not fail. And when you have turned back, strengthen your brothers.\wj*”
```

The rendered output: Satan demanded to have *you all*, but Jesus prayed for *you, Peter*.

## Appendix: KJV words whose meaning has changed

For readers who know the KJV. The right-hand column is this translation's rendering; a note gives the KJV word at the first occurrence in each book only where the KJV wording is famous.

| KJV | Reference (example) | Original | This translation |
|---|---|---|---|
| charity | 1 Corinthians 13 | *agapē* | love |
| conversation | Philippians 1:27; 1 Peter 1:15 | *politeuomai*, *anastrophē* | conduct, way of life |
| prevent | 1 Thessalonians 4:15; Psalm 119:148 | *phthanō*, *qadam* | precede, go before |
| let | 2 Thessalonians 2:7; Romans 1:13 | *katechō*, *kōlyō* | restrain, hinder |
| quick, quicken | 2 Timothy 4:1; Hebrews 4:12; Psalm 119:50 | *zaō*, *zōopoieō*, *chayah* | living, make alive |
| ghost (Holy Ghost; give up the ghost) | Matthew 1:18; Genesis 25:8 | *pneuma*, *gava'* | Spirit; breathe his last |
| suffer | Matthew 19:14 | *aphiēmi* | let, allow |
| meat | Genesis 1:29; Matthew 3:4 | *'oklah*, *trophē* | food |
| corn | Genesis 41:35; Matthew 12:1 | *bar*, *sitos*, *stachys* | grain; heads of grain |
| candle, candlestick | Matthew 5:15; Exodus 25:31 | *lychnos*, *lychnia*, *menorah* | lamp, lampstand |
| peculiar | Titus 2:14; 1 Peter 2:9 | *periousios*, *peripoiēsis* | his own possession |
| unicorn | Numbers 23:22; Job 39:9 | *re'em* | wild ox |
| Easter | Acts 12:4 | *pascha* | Passover |
| Lucifer | Isaiah 14:12 | *helel* | Day Star (note: "shining one"; KJV *Lucifer*, from the Latin) |
| Calvary | Luke 23:33 | *Kranion* | The Skull (note: KJV *Calvary*, from the Latin) |
| Godhead | Acts 17:29; Romans 1:20; Colossians 2:9 | *theion*, *theiotēs*, *theotēs* | divine nature; deity |
| sabaoth | Romans 9:29; James 5:4 | *sabaōth* | hosts |
| publican | Matthew 9:10 | *telōnēs* | tax collector |
| closet | Matthew 6:6 | *tameion* | inner room |
| mansions | John 14:2 | *monai* | dwelling places |
| bowels (of mercy) | Colossians 3:12; Philippians 1:8 | *splanchna* | compassion; affection |
| reins | Psalm 7:9; Revelation 2:23 | *kelayot*, *nephroi* | heart (note: lit. *kidneys*) |
| study | 2 Timothy 2:15 | *spoudazō* | be diligent |
| communicate | Hebrews 13:16; Galatians 6:6 | *koinōnia*, *koinōneō* | share |
| carriages | Acts 21:15 | *episkeuazomai* | baggage (got our baggage ready) |
| by and by | Luke 21:9 | *eutheōs* | immediately |
| firmament | Genesis 1:6 | *raqia'* | expanse |
| tabernacle of the congregation | Exodus 27:21 | *'ohel mo'ed* | tent of meeting |
| devils | Matthew 8:31 | *daimonia* | demons |
| hell (for *Sheol* / *Hades*) | Psalm 16:10; Acts 2:27 | *She'ol*, *hadēs* | Sheol; Hades |
| wist, wot | Exodus 16:15; Genesis 21:26 | *yada'* | knew, know |
| ere | John 4:49 | *prin* | before |
