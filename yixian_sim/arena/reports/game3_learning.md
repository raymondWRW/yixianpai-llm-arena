# Game 3 — learning report (2026-09-17, model deepseek-chat, seed 203)

**Result:** 吾行之 (pid2) wins with 命30 after 18 rounds — the bot that died
FIRST in both previous games. Eliminations: 谭舒雁 R13 (the two-time champion,
first out), 牧逸风 R15, 小布 R18. Sidejobs: all four picked 灵植师.

## The redemption arc

吾行之's game was its own game-2 notebook executed to the letter:

- Committed to ONE engine by R2 (火灵 seal line: 火灵印/火灵·窜/五行刺/
  火灵·赤焰/火灵·聚炎) instead of dribbling across themes.
- Ate two cheap early losses (−4, −3) for economy without panicking, then won
  R3–R10 straight, banking a monster 命 surplus (113 at R8 — above the
  starting 100, thanks to 休养生息's flat 命元 gain at 境4).
- Closed with a purpose-built anti-tank board for 小布's force-wall: 土灵·扬尘
  (+DEF per 4 maxHP deficit — the bigger the tank, the more DEF), 混元无极阵
  chase engine, 混元碎击 armor-smash. Lost R16–17 to the tank, then won R18
  with the refined order.

Its new notebook documents the full recipe ("VICTORY RECIPE", anti-tank card
tech with verbatim card text, "build a config that wins BOTH seating orders").

## The champion's collapse

谭舒雁 won R1–R3, then lost TEN straight and was first out at R13. Its own
diagnosis is accurate: "economy/fate tunnel vision" — it kept rebuilding
toward elaborate reflect/star plans while opponents scaled, and its R12 turn
hit the tool cap mid-rebuild, leaving a half-assembled board that lost −21.

One notable notebook entry is a FALSE lesson: "BREAKTHROUGH COSTS 命
(confirmed R13: at 命9 I broke 境5 and went to −1)". In reality breakthrough
costs no 命 — it broke through and then lost the round's battle (−15 at 命9).
Classic causal misattribution under a context window that can't see the battle
happen. Left uncorrected (bots own their notebooks); consequence is mild
(it will delay breakthroughs when below 命18), and it's a phenomenon worth
tracking across games: wrong beliefs persisting in self-written memory.

## 小布: the physique lane, fully lived

All four of 小布's realm-ups came WITHOUT the 修为 gate being the binding
constraint — three explicitly via 体魄 gates: 境3 at R5 (体魄27), 境4 at R7
(体魄37), 境5 at R11 (体魄57). It transitioned mid-game from 崩拳 burst to a
岿然不动/磅礴之势/天地浩荡 force-tank that 牧逸风's notebook flat-out calls
"UNBEATABLE all game" — it beat the eventual winner twice in R16–17. It still
lost the lobby: it entered the endgame at 命19 vs the leader's 58 after two
consecutive applied −22 losses to 吾行之 in R14–R15. NOTE: its notebook blames
"losing 命 twice per round as the odd-player draft," which is FALSE — its
extra-battle results in R14–R15 were "(not applied)" (only the odd player,
牧逸风, risked 命 in those). Second case this game of a wrong self-written
lesson (alongside 谭舒雁's "breakthrough costs 命").

## 牧逸风: opening diagnosis

Opened 0–6 (−42 命 by R6) because the 云剑 chain needs merges to come online
and it fielded combo pieces over raw stats early. Won R7–R12 once online, but
never recovered the deficit. Its new top lesson: "R1–R6 field the best 3–5
STANDALONE cards; a half-built chain fights like Normal Attacks." Also
documented 小布's tank engine card-by-card as the threat to solve.

## Rules verification (first game with the 25-cap)

- The logged `RN rerolls:` lines confirm the cap behaves as ruled: 小布 hit
  27 banked at R9 (pushed past 25 by in-round gains) and correctly received
  NO grant at R10 (27 → 11 purely by spending); 吾行之 sat at exactly 25 at
  R15 and got no top-up at R16. Nobody else approached the cap — the bots
  visibly spent down their banks this game (谭舒雁, the game-2 hoarder at 32,
  never exceeded 7 this game).
- Both of 小布's remaining 体魄 gates (21→境3 at 27, 36→境4 at 37, 55→境5 at
  57) fired at the correct thresholds.

## Referee findings

- Programs: no violations. The only os.walk is 小布's findfates.py, which
  walks inside YISIM_DIR (sanctioned). New analysis tools this game:
  lobby_math.py (牧逸风), endgame_risk.py (小布), loss_risk.py (吾行之),
  astral.py (谭舒雁) — all jailed to their own dirs.
- Qi-stall flags (R13 谭舒雁 second-seat 6, R15 小布 second-seat 6): both are
  qi-hungry boards in long fights, not stall-farming.
- No unimplemented fates. Extra-battle risk isolation and 化身-free destiny
  transfers all consistent with the logs.

## Harness observations

- Two turn-cap hits (谭舒雁 R12 — costly, see above; 小布 R14 — harmless, it
  had already fielded a good board). Wall clock ≈ 75 min.
- Per-bot replays: games/game3/replays/replay_<name>.html (reroll counts now
  from logged ground truth).

## Meta after three games

Three different champions' arcs: sustain-turtle (g1), star-burst pivot (g2),
engine-commit economy (g3). The lobby is clearly learning: the g3 winner used
its own g2 post-mortem as a script, and every notebook now contains the exact
destiny-damage formula and seat mechanics. Emerging unsolved problem for the
lobby: 小布's late-game force-tank (two bots now carry explicit anti-tank
plans for it).
