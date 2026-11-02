# Morne Bay (working title)

A YA survival thriller. One night every adult on a small Caribbean island falls into a sleep nobody can wake them from, and some of the kids start waking up with powers. Six lifelong friends from a gated compound have to keep their sleeping families alive, build a society, and work out what the island wants from them.

**Theme:** *We are what survives the fire.* Nobody is born a monster. Experience shapes us, power magnifies what grew, and nobody is purely one thing.

## Layout

| Folder | What lives there |
| --- | --- |
| [`bible/`](bible/00-index.md) | The world. One file per subject. Start at the index. |
| [`bible/cast/`](bible/cast/_overview.md) | One file per character. |
| [`chapters/`](chapters/) | One folder per chapter. `LATEST.md` is always the current draft; `versions/` holds every saved revision. |
| [`manuscript/full.md`](manuscript/full.md) | All chapters stitched in order. Rebuilt by a script, never edited by hand. |
| [`scripts/`](scripts/) | Helpers: save a version, start a chapter, rebuild the manuscript. |
| [`notes/`](notes/) | Loose ideas not yet promoted to the bible. |

## Workflow

1. Write or revise a chapter in `chapters/chNN-name/LATEST.md`.
2. Before a big rewrite, run `scripts/save-version.sh chNN-name` to snapshot it into `versions/`. Diff any two in Seam.
3. Run `scripts/build-manuscript.sh` to regenerate `manuscript/full.md`.
4. Commit: `git add -A && git commit -m "ch03: rewrite scene 2"`. Git is the second layer of history.
5. Any rule, fact or number decided while writing goes into the bible the same day. The bible is the source of truth; chapters follow it.

## Cross-referencing

Every bible file links to the others with relative Markdown links, e.g. `[Judge](cast/judge.md)` or `[the Sleep](02-the-sleep.md#outcomes-by-age)`. These work in VS Code, GitHub and Obsidian. Open this folder as an Obsidian vault for backlinks and a graph view.

## One-time setup

```
cd ~/Documents/morne-bay
git init
git add -A
git commit -m "Story bible and chapters 1-3"
```
