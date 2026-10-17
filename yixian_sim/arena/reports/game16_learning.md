# Game 16 — learning report (2026-09-27, model deepseek-chat, seed 316)

**Result:** 牧逸风 wins its THIRD title, 命40 after 19 rounds — back-to-back
with its game-14 title, sandwiching 小布's g15 blowout. Order out: 吾行之,
谭舒雁, 小布 (the last two fell in R19). Titles: 谭舒雁 8, 小布 4,
牧逸风 3, 吾行之 1. Fates 16/16; zero turn caps, zero crashes.

**Provenance:** this is a REPLAY. The original game 16 (seed 216) was lost
at R18 when the host PC slept mid-run — the in-flight API call hung and the
arena has no checkpoint. It is archived as games/game16_aborted_seed216.
The replay used a fresh seed because two bots had written mid-game notes
about seed 216's deals (foreknowledge). Fixes shipped: a Windows keep-awake
hold for the run's duration, unbuffered live logs, and append_ledger
restricted to review (bots had been writing ledgers mid-game since g13).

## The winning board: the g14 counter, hardened

[辟邪阵纹+1, 聚灵心法+1, 百鸟灵剑诀+1, 引气剑+1, 巨鲲灵剑+2, 云剑·点星,
白鹭灵剑, 万法归灵剑+1] — nearly identical to its dynasty-breaking g14 list,
with 百鸟灵剑诀 upgraded and 云剑·点星 in for 御空剑阵. The 辟邪阵纹 floor
(the find the user flagged after g14) is still slot 1, and the qi engine
kept its +2 巨鲲 finisher. It held 命40 untouched from R17 on while the
other three traded lethal blows. This is the first time a bot's COUNTER
archetype survived being known for two games — the rivals' reviews after
g14 did not produce an answer to it.

## Referee

Clean: no program violations, no stall flags, budgets respected. Open
review was live for this game's reflections (first game on it).
