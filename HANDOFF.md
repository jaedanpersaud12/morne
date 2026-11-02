# Handoff: where we are

Read this first in a new session, then `bible/00-index.md`.

## State (2026-11-01)

- Bible complete through file 18. Locked: theme, the Sleep, powers, sleepers, network and Gardener, island, cast, factions, relationships, conflicts, timeline, little ones, resources and roles, powers in practice (numbers, combat, crews), writing rules, prose fundamentals, book-one outline with parallel stories, visual style.
- Chapters 1 to 3 written (Kit, Juno, Fen), ~6,600 words, in `chapters/*/LATEST.md`. Each has v001 in `versions/`.
- Cast portraits generated on ElevenLabs (flow `swXwYpOym9CTRn4zYWDQ`); picks to be saved in `art/cast/`.
- Git not yet initialised. Run: `git init && git add -A && git commit -m "Story bible and chapters 1-3"`.

## Big decisions locked
- **Setting rewrite (2026-11-01):** no gated compound. The six grew up on Quarry Trace, a dead-end road of 9 ordinary houses climbing to an old quarry (the network's wound). 16 adults, 13 kids on day zero; about 30 kids by week one as the road comes up. No wall at first: the taxi across the bend in week one, cars in month two, a built wall months 4 to 6, Tock's welded gate later. Kit's father Winston is a taxi driver who moved to the flat at the bend eight months ago; the shotgun is in a steel box under his bed. Faction name: the Trace. See 06.
- Nobody leads the Trace; six domains argued in a kitchen. Juno is the medic, not the leader; everyone outside treats her as one, and that is her lie.
- Juno has no power in book one; awakens Life/decay at the age line (her lifespan as the cost). No hint before the siege.
- Fen and Lyra agree on letting their mother go. That bond never breaks.
- Juno's want is Granny. Book one ends with her carrying Granny to the garden and letting Tock take the other end.
- Jaylen's death in the siege is proposed, not locked.

## Next
1. Chapter 4, "Ice": Sol and Lonny, first light, the road, formula, Sol's ice undeniable. Use `scripts/new-chapter.sh 04 ice "Sol / Lonny"`.
2. Then chapter 5 onward per `bible/17-book-one-outline.md`.
3. Before each chapter: run the checklist in `bible/15-prose-fundamentals.md`. After: `scripts/save-version.sh` and `scripts/build-manuscript.sh`.

## Open questions
See `bible/16-open-questions.md`. Most pressing: island name, Gardener's name, Lonny's girlfriend's name, who dies in the siege, Juno's birthday date.
