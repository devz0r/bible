# Source texts

Translation is done from these files, never from memory alone (charter §5).

## Get the data

```
./scripts/fetch_sources.sh        # downloads ~100 MB into sources/raw/ (not in git); checksums in SHA256SUMS
python3 -I scripts/build_index.py # builds sources/index/ (committed; ~13 MB)
python3 scripts/verse.py Jhn.3.16 # look up any verse; also Jhn.3 or Jhn.3.16-18
python3 -I scripts/compare_tr.py  # compare the two TR texts (see "Known problems")
```

Verse codes follow STEPBible: Gen Exo Lev Num Deu Jos Jdg Rut 1Sa 2Sa 1Ki 2Ki 1Ch 2Ch Ezr Neh Est Job Psa Pro Ecc Sng Isa Jer Lam Ezk Dan Hos Jol Amo Oba Jon Mic Nam Hab Zep Hag Zec Mal Mat Mrk Luk Jhn Act Rom 1Co 2Co Gal Eph Php Col 1Th 2Th 1Ti 2Ti Tit Phm Heb Jas 1Pe 2Pe 1Jn 2Jn 3Jn Jud Rev.

## What is here

| File | What it is | License / credit |
|---|---|---|
| `raw/TAHOT_*.txt` (4 files) | Translators Amalgamated Hebrew OT: Leningrad Codex (via OpenScriptures), Qere/Ketiv, restored text, morphology, lexical tags, some variants | CC BY 4.0. Credit: STEP Bible (www.STEPBible.org), data by Tyndale House, Cambridge |
| `raw/TAGNT_*.txt` (2 files) | Translators Amalgamated Greek NT: every word of NA27/28, TR, SBL, WH, Treg and Byz, with the editions that contain it, morphology and Strong's | CC BY 4.0. Same credit |
| `raw/KJV.csv` | KJV text, used only for verse counts and comparison | Public domain (outside the UK) |
| `raw/TR_scrollmapper.csv` | A Textus Receptus text ("1550/1894"), unaccented | Origin and license not verified |
| `index/NT.tsv` | One row per verse: TR / NA28 / SBL / Byz Greek, keyed by **KJV** verse numbers | Derived from TAGNT (CC BY 4.0) |
| `index/OT.tsv` | One row per verse: Hebrew (Leningrad, Qere followed) and flags | Derived from TAHOT (CC BY 4.0) |
| `index/kjv_verses.txt` | The 31,102-verse KJV reference list the validator checks against | — |
| `index/REPORT.txt` | Verse-count check (see below) | — |
| `index/TR_DISAGREEMENTS.tsv` | Verses where the two TR texts differ | — |

Third-party data keeps its own license (see `/LICENSE`). The CC0 dedication covers only the translation text and project documents.

## Checks that pass

- The Hebrew and Greek data together contain **exactly 31,102 verses**, and the set is identical to the KJV's (nothing missing, nothing extra). Psalm titles (verse 0) are kept separately.
- The three verses the charter says the Leningrad Codex lacks are confirmed: TAHOT marks **Joshua 21:36, 21:37 and Nehemiah 7:68** (KJV numbering) as *restored text* (type R, taken from the parallel passages in Chronicles and Ezra). Nehemiah 7:68 is Nehemiah 7:67b in TAHOT's NRSV numbering.

## Known problems (read before drafting)

1. **The Greek "TR" in TAGNT is not Scrivener's text.** Its `TR` tag matches the KJV in most places but not in the famous ones: Revelation 16:5 lacks "and shall be" (*esomenos*), Revelation 22:19 lacks "book of life" (*biblou*), and Luke 2:22 reads "their". The other TR file (scrollmapper) has the KJV readings at Rev. 16:5 and 22:19, but it is unaccented, lists both readings side by side at Luke 2:22, and its origin is unverified. The two files disagree in **3,045 of 7,957 verses**, mostly in spelling (*outhenos/oudenos*, *Mōuseōs/Mōseōs*, elision) but also in real words (`TR_DISAGREEMENTS.tsv`). **Neither can yet be treated as Scrivener 1894.** In the pilot chapters (John 1, 3; Romans 3; 1 John 5) the scrollmapper text matched the KJV in every real-word disagreement (about 20), while TAGNT's TR tag simply lacks TR-only words that have no row of their own. So the interim rule (charter §8) is: translate from the scrollmapper text; use TAGNT for grammar and comparison. A proper Scrivener 1894 text file is still needed.
2. **TAHOT records very few Dead Sea Scrolls or Septuagint variants.** It has one explicit Dead Sea meaning-variant in the whole Old Testament (Psalm 22:16). Footnotes about DSS, LXX and Samaritan Pentateuch readings must come from published editions (charter §5), not from this data.
3. **`NT.tsv` counts spelling and accent differences.** "TR differs from NA28" is true in 3,779 verses, but many of those are not differences of meaning. Do not read that number as a count of real variants.
4. TAGNT is an interlinear for study. It is not a printed edition. When it and a printed edition disagree, the printed edition (once we have it) wins.
