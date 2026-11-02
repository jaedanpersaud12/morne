#!/usr/bin/env bash
# Snapshot a chapter's LATEST.md into versions/vNNN-YYYYMMDD-HHMM.md
# Usage: scripts/save-version.sh ch01-dust ["note"]
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CH="$ROOT/chapters/$1"
[ -f "$CH/LATEST.md" ] || { echo "no $CH/LATEST.md"; exit 1; }
mkdir -p "$CH/versions"
N=$(ls "$CH/versions" 2>/dev/null | wc -l | tr -d ' ')
N=$((N+1))
STAMP=$(date +%Y%m%d-%H%M)
OUT="$CH/versions/v$(printf '%03d' $N)-$STAMP.md"
cp "$CH/LATEST.md" "$OUT"
echo "- v$(printf '%03d' $N) ($STAMP): ${2:-snapshot}" >> "$CH/CHANGELOG.md"
echo "saved $OUT"
