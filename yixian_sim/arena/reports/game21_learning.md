# Game 21 — learning report (2026-10-04, model deepseek-chat, seed 221)

**Result:** 牧逸风 wins its FOURTH title — 命48 after 19 rounds, untouched
from R14 on. It then beat 谭舒雁 in three straight head-to-heads
(46 → 15 → 1 → 0). Order out: 吾行之, 小布, 谭舒雁. Fates 16/16; no turn
caps, no crashes; off-peak throughout (Sunday).
Titles: 谭舒雁 8, 小布 5, 牧逸风 4, 吾行之 2, + 2 unfinished (g9, g17).

First game with frozen rival files in review (snapshot taken at game end;
all four bots read the same versions).

## The win: 牧逸风's finisher, assembled for the first time ever

Final board: [辟邪阵纹, 百鸟灵剑诀+1, 引气剑+2, 化灵诀, 云剑·点星, 云剑·点星,
白鹭灵剑+1, 万法归灵剑+1]. After four games without drawing 万法归灵剑 (a
phase-5 card, ~1 expected copy per game), it rolled two in about seven rolls
right after reaching 境5 at R11, merged them to +1, and won every round from
R13 except one. Its R19 kill line: bank 15 qi by turn 7, 白鹭灵剑+1 fires for
50, then 万法归灵剑+1 dumps all 15 qi for 95 — over half 谭舒雁's HP in one
card. The 辟邪阵纹 in slot 1 (its game-14 find) blanked 谭舒雁's 内伤 clock.

Its review added matchup nuance: 辟邪阵纹 is a dead slot against 小布's burst
— there, a third 云剑·点星 is better. One board per opponent, not one board.

## What the others learned

- **谭舒雁** won the 修为 seat race against 牧逸风 (96 vs 90) and lost
  anyway. Its diagnosis: against the 万法 dump the answer is 厄劫缠身 (its
  opening downgrades the opponent's same-slot card), which it never drew.
  It held two 诸事不宜 at the end but deliberately left them out — that card
  is its anti-小布 tool, and 小布 was already eliminated.
- **小布 relapsed on a lesson it had already fixed.** It fielded a force
  board with none of its force generators (冲霄破浪, 踏破九霄, 势如破竹) —
  its hand was EMPTY at R15, the same over-absorbing trap that sank 谭舒雁
  last game — and 威震四方 (the force-cap raiser) went undrawn for a third
  game. Its board landed about half its normal damage.
- **吾行之** (last) studied the winner's economy curve through open review:
  zero rolls R1-7, then heavy rolls R8/R10/R11 aimed at 万法 right after
  reaching 境5. Its own root cause: reaching 境5 a round later than the
  winner, so one fewer round of phase-5 draws.

## Harness checks

- Frozen rival files: working (logged at review start).
- All four ledger entries record the right winner and game number.
- One qi-stall flag (R10, 吾行之 first seat, 6 turns): its water-formation
  board is qi-hungry in long fights — genuine, not stalling.
- 小布 appended two ledger entries for this game (allowed; cosmetic).
