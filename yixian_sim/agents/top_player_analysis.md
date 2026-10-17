# How top players pilot painter 林小月 — yxp_wiki recordings corpus

Analyzed 2026-09-15 from the wiki's recording archive (a 林小月-dedicated
archive: 2,531 games, 791 as painter). Sample: **all 83 ranked painter games at
rating ≥ 9300** — dominated by one specialist (愿与小月长相厮守, ~9500–9700,
50+ games). 19 of 83 are outright lobby wins (vs 12.5% baseline). These games
contain SEASON mechanics our sim lacks (per user: noted and ignored) — the
biggest being the card 迅影飞剑 and item-fates like 剑意大师/铜镜; base-game
conclusions below are drawn around them.

## The template (what ~80% of these games do)

| rounds | what happens |
|---|---|
| R1–R5 | 境1. Field 3→6 slots of the SAME five cards we use. Roll hard (~5/round) digging the core. Win rate is a shrug: 36–48%, losses cost −3…−5 命. |
| R6 | **Double-break 境1→境3** (79/83 games). Two fate picks, usually NOT the cat line. Deck by now: 剑劈+2 · 剑挡+2 · 灵气灌注+1 · 飞牙剑lv2-3 · 震雷剑+1. |
| R7 | **The great absorb**: 震雷剑, 灵气灌注, spare 剑挡/飞牙剑 copies eaten for 修为. Board compresses to 剑劈+2 · 剑挡+2 · 凝意诀 · 飞牙剑+2 (~5 slots). Rolls STOP (0.5–1/round R7–R10) — the hoard phase is 境3–境4. |
| R8 | **境4, pick 灵猫乱剑** (75/83 at R8, rest R9), eat 猫薄荷 immediately → 灵猫乱剑+1 (68 of 145 catnip uses land R8–9). Standard board: 剑劈 · 剑挡(·剑挡/凝意诀) · 飞牙剑 · 灵猫乱剑 — win rate peaks 76–80%. |
| R9–R10 | Coast on the 境4 board; bank rolls to ~17 by R10, absorb 2–3 junk/round. |
| R11 | **境5 — one round earlier than our guide** (58/83 at R11, 23 at R12, 2 at R10). Dump the entire roll bank (11–15 rolls) into phase-5 keepers. |
| R12+ | The 剑意激荡 engine: field **BOTH 激荡 copies unmerged** (two multiplier procs per cycle — 32 of 75 final boards run 激荡×2), 凝意诀+2, 御空剑阵, 连环剑阵, 云舞诀 around it; merge 激荡 to +2 later. Boards shrink every round; win rate stays 55–70% while命 losses are absorbed raw. |
| endgame | 4–6 card chains. Payoff: 灵猫乱剑+1 in 39 final boards, but **飞灵闪影剑+2 replaces it in 18** — several games ABSORB 灵猫乱剑 itself once 飞灵闪影剑+2 exists (the 9656 exemplar ate it at R18 and finished on 迅影飞剑+2 · 剑意激荡+1 · 剑意激荡+2 · 飞灵闪影剑+2, four cards). |

命 philosophy: front-load the bleeding. They freely drop to 27–45 命 by R11
(early/mid losses are cheap by the destiny formula), then the 激荡 engine wins
8–10 straight rounds losing zero. Final winners' 命: median ~24 (1 to 69).

## Where they contradict our playbook (with corpus numbers)

1. **The cat fates are mostly SKIPPED.** 猫爪 in 20/83 games; **猫魂庇佑 in
   2/83**; 休养生息 2/83. The 境2/境3/境5 picks are instead: **剑韵修炼**
   (33 games — and it STACKS: 11 games took 2–3 copies; the exemplar took it at
   筑基 AND 金丹 in the same double-break, then again at 化神), 顿悟, 善假于物,
   云巅雷劫/感悟丛生 (card = cult), 云剑传承, 稳固根基. Only 灵猫乱剑 (82/83)
   and innate 好奇心 are untouchable. Their reasoning is visible in the 命
   curves: battle-start 剑意 compounds the engine that stops ALL losses, while
   猫魂庇佑 only discounts losses they plan not to take. (Our game6 won BECAUSE
   of 猫魂庇佑's 42 命 — but our engine arrives ~3 rounds later than theirs.)
2. **境5 at R11, not R12.** 修为 line: they hit 55 a round earlier because R7
   onward they absorb 2–4 cards EVERY round (2,902 absorbs across the corpus)
   — including the phase-1 core itself the moment it leaves the board (震雷剑
   and 灵气灌注 at R7; later even 剑挡+2, 御空剑阵+1, and 灵猫乱剑).
   Nothing is sentimental; everything not in the final chain is 修为.
3. **修为 never stops mattering: it is the seat dial, forever.** Top players
   keep absorbing to 90–106 修为 at 境5, tracking their rivals point-for-point
   (exemplar: 74v74, 88v88, 97v94, 106v103 in consecutive rounds). Corpus seat
   record: first = 70% win (403-172), second = 52% (441-408). They take first
   when they can get it — but spend most rounds slightly BELOW the table
   leader rather than overpaying (lower-cult rounds: 719 of 1,330).
4. **Double copies are fielded, not merged, when the effect repeats.**
   剑意激荡×2 unmerged (two ×1.8 procs beats one ×2.4 until lv3 is affordable),
   剑挡×2 boards at R8–9 (11×), 连环剑阵×2. Merging is for when a LEVEL
   threshold pays (激荡+2, 飞灵闪影剑+2), not by default.
5. **飞灵闪影剑+2 is a real alternative finisher** — 18 of 75 final boards end
   on it (its 6×1攻 all get the bank, and each 击伤 refunds qi), usually after
   灵猫乱剑 is eaten. Confirms and extends the user's game4 note.
6. **飞牙剑: ONE copy, pushed to lv3 early** (飞牙剑+2 by R7 in the exemplar),
   benched at 境5. Matches the user's later rulings, not the original guide's
   "two lv2 copies".
7. **猫薄荷 is spent, not hoarded**: first catnip → 灵猫乱剑+1 at R8–9, later
   catnips (R12–14 wave) → 连环剑阵/剑意激荡/凝意诀/御空剑阵 upgrades. 75 of
   145 catnip results are 灵猫乱剑 2级. (11 hit another 猫薄荷 in hand —
   catnip dilutes catnip, mind the hand.)
8. **Early rounds are deliberately cheap**: R1 boards are three junk beaters
   (轻剑·剑挡·震雷剑 / 灵气灌注·震雷剑·巨虎灵剑 / 剑劈·剑挡·骤风剑), 36% win
   rate, −2.7 命 average — they'd rather roll than defend. The R3 modal board
   (19/83 games!) is **灵气灌注 · 震雷剑 · 剑劈 · 剑挡 · 飞牙剑** — note the
   order: 灌注's pierce rider lands on 震雷剑, 飞牙剑 last to eat 剑挡's bank.

## What our playbook already gets right (validated at scale)

- The phase-1 five (剑劈/剑挡/灵气灌注/飞牙剑/震雷剑): 85–100% presence R4–7.
- 剑劈+2/剑挡+2 by R6; 境1 held until R5–6, then double-break.
- The roll hoard through 境4 (bank ~17 by R10) and the 境5 dump.
- Hold exactly 3+ hand cards with 灵猫乱剑 fielded (modal hand size = 3,
  354 of 742 rounds; mean 4.6).
- 灵猫乱剑 fate always taken; catnip guaranteed onto it promptly.
- Endgame = compressed pure-intent chain (凝意诀/御空剑阵/连环剑阵/云舞诀 +
  激荡 + payoff); board length shrinks every round late.

## Season features seen and ignored (per user instruction)

迅影飞剑 (in 70–81% of late boards — attack that banks intent, never spends
it, and chases while intent > 0; would be the best card in the deck if we had
it), 丹雀灵剑, 幻·云舞诀, 天音困仙曲/万邪入体咒/血光之灾 splashes, item-fates
(剑意大师/剑阵大师/铜镜/三思抉择/天衍-触类旁通, 323 uses), and a much richer
roll economy (7–15 rolls/round at 境5; exchangeLimit 25). Where these carried
a board, conclusions were drawn from the base-game cards around them.

## Questions for the user before updating the playbook

1. Adopt the top-player fate line (剑韵修炼-stacking / 顿悟 / card-fates,
   skipping 猫爪+猫魂庇佑) — or keep 猫魂庇佑 because our sim's opponents
   (lv4–5 ghosts) still beat us mid-game more than top players' lobbies beat
   them?
2. Break 境5 at R11 (their line) instead of R12?
3. Field both 剑意激荡 copies unmerged until lv3 is reachable?
4. Endgame payoff swap: absorb 灵猫乱剑 for 飞灵闪影剑+2 when it reaches lv3
   (hand-hold requirement disappears too)?
