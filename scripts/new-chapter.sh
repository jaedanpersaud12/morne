#!/usr/bin/env bash
# Create a new chapter folder.
# Usage: scripts/new-chapter.sh 04 ice "Tori"
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NUM="$1"; SLUG="$2"; POV="${3:-}"
DIR="$ROOT/chapters/ch$NUM-$SLUG"
mkdir -p "$DIR/versions"
TITLE="$(echo "$SLUG" | sed 's/.*/\u&/')"
cat > "$DIR/LATEST.md" <<MD
# Chapter $NUM — $TITLE

<!-- POV: $POV. Three scenes: set up, complicate, turn. End on a turn. See bible/14-writing-rules.md -->

MD
echo "# Changelog: ch$NUM-$SLUG" > "$DIR/CHANGELOG.md"
echo "created $DIR"
