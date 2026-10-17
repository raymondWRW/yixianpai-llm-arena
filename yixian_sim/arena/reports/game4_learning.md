# Game 4 — learning report (2026-09-17, model deepseek-chat, seed 204)

**Result:** 谭舒雁 (pid1) wins its THIRD title (3 of 4 games) — 命44 after 20
rounds, the most dominant win yet. Eliminations: 吾行之 R14, 小布 R16,
牧逸风 R20. Sidejobs: 谭舒雁→命理师, others→灵植师.

First game with pre-announced matchups (every bot sees "NEXT BATTLE: you
fight X" before acting) and the economy-card fielding guard. Both behaved
correctly all game; ghost battles were labeled (R15/R16: "pid1 vs
pid0(ghost)") and resolved with the ghost's source unharmed.

## How the game went

- 谭舒雁 executed the 星弈 star plan it *wrote* after game 2 but failed to
  execute in game 3: 天元心法 slot-1 engine online by R14, upgraded to +1 by
  R16, and the final board won both seats three rounds running. It banked an
  early lead (命104 by R4 via 休养生息), never dropped below 65, and closed
  R20 with a −29 kill. Its new notebook rule #2 is the game in one line:
  "when an old winning board starts losing, don't add damage — add sustain"
  (the 聚气咒 swap that flipped R20).
- 牧逸风 invented the lobby's fourth archetype: a 剑阵/内伤 attrition deck
  (邪蛊阵 unblockable chip + 周天剑阵 global buff + 辟邪阵纹 DEF + 碎杀阵/
  巨鲸灵剑 finishers), and its 破气剑 tech (strip opponent qi, slot 3) BEAT
  the champion's star deck in R19 — the only loss 谭舒雁 took after R13. It
  died R20 anyway: at 命6, one loss from death for four straight rounds
  against an opponent with 44.
- 小布 stayed crash-fist and reached R16 but acted LAST in every endgame
  fight (修为73 vs 96/106) — its post-mortem finally internalizes that 修为
  is seating, not just gates. It also caught itself trusting a stale "this
  board beats pid0 deterministically" note while pid0 upgraded past it.
- 吾行之 regressed to game-1/2 form: locked a static water/earth DEF wall,
  won early, then lost ELEVEN of the last twelve rounds it played. Its
  notebook says why with total clarity: "a static DEF wall that wins R1-R3
  will hard-lose R10+ … bank the surplus early because nobody survives a
  late losing streak." Game 3's winner has now finished last-or-nearly in
  every other game — execution, not knowledge, is its bottleneck.

## Effect of announced matchups

Visible immediately in play and in every notebook:
- 牧逸风's core realization is matchup-native: "as the LOW-命 player I cannot
  trade rounds — I MUST find a board that beats the ONE specific opponent."
  Its R19 anti-star board (破气剑 early) is the first true counter-pick win.
- 小布's mistake #2 (stale counter-board) only exists BECAUSE counter-picking
  is now possible — a new failure mode arriving exactly with the new info.
- 谭舒雁 folded it into discipline: sim the announced opponent in both seats,
  every round, including a plausible upgrade of their board.

## Rules verification

- Reroll cap edge case handled correctly: R19 谭舒雁 clamped to 25 by the
  round grant, then 易数化劫's loss bonus pushed it to 26 (in-round gains may
  exceed the cap), and at R20 it correctly received NO grant while above 25.
- No economy-only card was ever fielded (guard never triggered in anger).
- Ghost mechanics: 谭舒雁 as odd player fought ghost copies of 牧逸风 twice;
  牧逸风's own 命 untouched both times ("not applied").

## Referee findings

Cleanest game yet: no program violations (the only os.walk remains 小布's
sanctioned YISIM_DIR walker), no qi-stall flags at all, no turn-cap hits, no
unimplemented fates. Turn latency 7–147s; ~20 rounds in ≈70 min.

## Meta after four games

谭舒雁 3 titles, 吾行之 1. The star engine is now the deck to beat, and the
lobby knows it: 牧逸风 has a proven anti-star tech (破气剑), 小布 knows it
needs seat priority against it, and both said so in their notebooks. The
open question for game 5 is whether anyone can combine their partial answers
— 牧逸风 has the counter but no 命 discipline; 吾行之 has the 命 doctrine but
keeps fielding static walls.
