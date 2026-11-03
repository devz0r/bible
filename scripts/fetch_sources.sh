#!/usr/bin/env bash
# Download the source-text data into sources/raw/. Safe to re-run.
# Needs outbound HTTPS to raw.githubusercontent.com.
set -euo pipefail
cd "$(dirname "$0")/.."
RAW=sources/raw
mkdir -p "$RAW"

STEP="https://raw.githubusercontent.com/STEPBible/STEPBible-Data/master/Translators%20Amalgamated%20OT%2BNT"
hot() { echo "TAHOT%20$1%20-%20Translators%20Amalgamated%20Hebrew%20OT%20-%20STEPBible.org%20CC%20BY.txt"; }
gnt() { echo "TAGNT%20$1%20-%20Translators%20Amalgamated%20Greek%20NT%20-%20STEPBible.org%20CC-BY.txt"; }

# name|url
LIST="
TAHOT_Gen-Deu.txt|$STEP/$(hot Gen-Deu)
TAHOT_Jos-Est.txt|$STEP/$(hot Jos-Est)
TAHOT_Job-Sng.txt|$STEP/$(hot Job-Sng)
TAHOT_Isa-Mal.txt|$STEP/$(hot Isa-Mal)
TAGNT_Mat-Jhn.txt|$STEP/$(gnt Mat-Jhn)
TAGNT_Act-Rev.txt|$STEP/$(gnt Act-Rev)
KJV.csv|https://raw.githubusercontent.com/scrollmapper/bible_databases/master/formats/csv/KJV.csv
TR_scrollmapper.csv|https://raw.githubusercontent.com/scrollmapper/bible_databases/master/formats/csv/TR.csv
"
echo "$LIST" | while IFS='|' read -r name url; do
  [ -z "$name" ] && continue
  if [ -s "$RAW/$name" ]; then echo "have  $name"; continue; fi
  echo "fetch $name"
  curl -fsS --retry 3 -m 120 -o "$RAW/$name.part" "$url"
  mv "$RAW/$name.part" "$RAW/$name"
done
( cd "$RAW" && sha256sum *.txt *.csv > ../SHA256SUMS )
echo "done. checksums in sources/SHA256SUMS"
