#!/usr/bin/env bash
# Stitch every chapters/*/LATEST.md into manuscript/full.md, in folder order.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/manuscript/full.md"
{
  echo "# Morne Bay (working title)"
  echo
  echo "_Built $(date '+%Y-%m-%d %H:%M'). Do not edit; edit chapters/*/LATEST.md and rerun scripts/build-manuscript.sh._"
  echo
  for d in "$ROOT"/chapters/ch*/; do
    [ -f "$d/LATEST.md" ] || continue
    echo
    cat "$d/LATEST.md"
    echo
    echo
  done
} > "$OUT"
WORDS=$(wc -w < "$OUT" | tr -d ' ')
echo "built $OUT ($WORDS words)"
