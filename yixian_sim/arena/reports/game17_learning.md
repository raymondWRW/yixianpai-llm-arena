# Game 17 — learning report (2026-09-27, model deepseek-chat, seed 217)

**Result: TIE — 谭舒雁 and 小布 both alive at 命1 when the 20-round cap hit.**
Order out: 牧逸风 (the two-time defending counter-champion, first out),
吾行之. Fates 16/16; zero turn caps, zero crashes.

## The finish, and a scoring bug it exposed

The harness originally recorded 谭舒雁 as winner. That was an artifact:
`max(players, key=(alive, 命))` broke the 1-1 tie by SEAT ORDER (pid1 < pid3).
Fixed: ties at the cap are now logged and stored as ties (`tie`,
`co_winners` in result.json), and tied bots are told "TIED for 1st" in
review. This game's result.json is annotated accordingly. How cap ties
SHOULD be resolved is a rules question pending the user's ruling (options:
shared title, head-to-head, or sudden-death rounds past 20).

The endgame itself was the best comeback in arena history: at R18 小布 led
命49 to 谭舒雁's 命1 — then 谭舒雁, one loss from death for three straight
rounds, won R19 (−28) and R20 (−20) head-to-head, dragging 小布 from 49 to
exactly 1. Under a head-to-head tiebreak 谭舒雁 takes it; under a strict
"last one standing" reading nobody has won yet.

## Open review: can't measure yet

Games 16 and 17 both ran with open review (rival playbooks, ledgers,
economy and all battle logs readable post-game). No notebook cites a rival
file — but review tool calls weren't logged, so "unused" and "used without
citation" are indistinguishable. Added: every review tool call is now
logged (tool + rival name + round), so game 18 will show exactly how much
the bots study each other.

## Referee

Two qi-stall flags (R10 吾行之 first-seat 8, R16 second-seat 6): both
qi-hungry formation boards in long fights — genuine, not stall-farming.
Otherwise clean.


## CORRECTION (2026-09-27): game unfinished

This game did not end. The arena stopped it at round 20, but that cap was a harness invention: the real game continues until one player is left (user ruling). Two players were still alive, so there is **no winner**. Any title or tie claimed above is void; the game is recorded as UNFINISHED. The cap has been removed (verified: play continues past R20 and ends naturally). The game cannot be resumed, because there is no checkpoint and the bots already reviewed it.
