# Game 6 — 林小月 猫画师剑意 (seed 113, `--ghosts`) — 1st place, WON, 13W-0D-6L, sole survivor at R19

Played 2026-09-04 by an Opus agent following the consolidated `agents/strategy_linxiaoyue.md`
plus the game5 review/summary. Randomly seated lobby of 7 recorded 境5-finisher ghosts:
pid1 南宫生[ai7-lv4], pid2 吴策[ai4], pid3 牧逸风[ai7], pid4 花沁蕊[ai2], pid5 姜袭明[ai7-lv5],
pid6 慕虎[ai2], pid7 陆剑心[ai7].
Files: `log.txt` (534 lines / 297 moves), `replay.html`.

## Result

- **1st of 8 — game won.** Last opponent (花沁蕊) eliminated in R19; I finished the only
  player alive at **命 70**, HP 112, 修为 79.
- Record: **13W · 0D · 6L**. Two of my battles were "extra" (odd-player-out) battles: R12
  (lost, paid) and R17 (won, killed 慕虎).
- 命 curve: 100 → 100 (R1–R2 W) → **95** (R3 L −5) → 95 through R8 (five straight wins) →
  **82** (R9 L −13) → 82 (R10–R11 W) → **112** (R12 breakthrough 休养生息 **+30 命**) →
  102 (R12 L −20 halved to −10) → 89 (R13 L −26→−13) → 79 (R14 L −20→−10) →
  70 (R15 L −18→−9) → **70 through R16–R19** (four straight wins, no 命 lost).
- Elimination order: 吴策 R11 · 南宫生 + 姜袭明 R14 · 牧逸风 R15 · 陆剑心 R16 ·
  **慕虎 R17 (I killed him)** · **花沁蕊 R19 (I killed her)**.
- Realm path: **境1 → 境3 in one command at R6** (猫爪 at the 境2 gate, **猫魂庇佑** at 境3) ·
  **境4 at R8** (灵猫乱剑) · **境5 at R12** (休养生息).
- Final board:
  `画龙点睛+1 · 云剑·游龙 · 剑劈+2 · 云舞诀+1 · 剑挡+2 · 御空剑阵 · 剑意激荡+2 · 灵猫乱剑+1`
  — sim +29/+31 vs 花沁蕊 in **both** seat orders.

## The game in one line

The phase-1 core came together a round early (剑劈+2 and 剑挡+2 both by R6), which bought
five straight wins and a 命 lead that never went away; the middle rounds (R12–R15) were four
straight losses to scaled-up wall decks, but 猫魂庇佑 halved every one of them and the 境5
天命 refunded 30 命, so the deck survived long enough for **剑意激荡+2** to arrive at R16
and turn every remaining matchup into a +24…+31 blowout.

## What actually won the game (three numbers)

1. **猫魂庇佑 halved 4 of my 5 late losses** — R12 −20→−10, R13 −26→−13, R14 −20→−10,
   R15 −18→−9. **≈42 命 saved.** I finished on 70. Without it I finish near 28 and probably
   lose the R15/R16 exchange. Game5 called losing this fate its largest identifiable cost;
   here it is the largest identifiable gain.
2. **休养生息 at the 境5 gate paid +30 命, not the card's +14** — fate magnitudes scale with
   the pick phase (same effect as game5's 灵剑传承 ×3). 82 → 112 in one click.
3. **剑意激荡 scaled to +2 (+140% intent) by R16.** Board average went
   +5.3 (R13) → +14.5 (R14, lv1) → +27.8 (R15, lv2) → +28.5 (R17, lv3). Nothing else in the
   deck moves the number like this card's level.

## How the guide's phase plan went

- **Phase 1 (R1–R6): the target board was assembled a round EARLY and over-delivered.**
  By R6: **剑劈+2 · 剑挡+2 · 灵气灌注+1 · 飞牙剑+1 · 震雷剑+2**. 震雷剑 reached lv3 (the
  guide's optional bonus) for free at R5 off duplicate draws; 剑挡 hit lv3 at R6 off a
  练笔 roll chain. The R1 roll of 巨虎灵剑 immediately produced the 2nd 飞牙剑.
- **境1 → 境3 double break at R6**, same as game5 and for the same reason (the whole lobby was
  already 境3 / 修为 21–27 while I sat at 境1/23). Both fate picks landed: **猫爪** at the
  境2 slot and **猫魂庇佑** at 境3. `break <ids>` honoured the preference list on the
  breaking call — the game5 bug is genuinely fixed.
- **境4 at R8, on schedule.** Reached the 36 gate by absorbing 3 junk cards plus one board
  card (the spare 飞牙剑 lv1). 灵猫乱剑 taken as always.
- **境5 at R12** (guide window; game5 also broke at R12). Reached 55 by absorbing 6 cards in
  one round, affordable only because by then the board needs 5–6 slots.
- **Roll hoard held through phases 2–4**: 3 charges at R7 → **20 at the 境5 break**, spending
  only on [置换] freebies and clear junk. The guide's number (20+) reproduced exactly.

## 好奇心 (9/9) — the whole bank farmed in ONE round

At R12, immediately after the 境5 break, I burned the roll bank down to **exactly 1 charge**
and then farmed all nine triggers back to back. Each trigger grants a cat card **and refunds
the charge**, so from 1 charge the loop is free and self-sustaining as long as one disposable
card is in hand (the cat cards it grants are their own fodder).

Yield: 逗猫棒 ×3, 云剑·飞砂, 青铜猫 ×2, 小鱼干 ×2, and — on the 9th, via the pity rule —
**猫薄荷**. Nine triggers' worth of value for zero net charges.

**猫薄荷 (1 use, R12): deterministic hit on 灵猫乱剑 → 灵猫乱剑+1.** The prep was done three
rounds earlier: 云剑·猫爪 was absorbed at R9, leaving 灵猫乱剑 as the only lv1 card with 猫
in its name. `absorb_fx._upgrade` builds a favored list of lv1 cards whose name contains 猫
and picks uniformly from it whenever it is non-empty — so the only card that ever dilutes a
catnip is another 猫-named lv1; the guide's "absorb EVERY other lv1" ritual can be narrowed.

## Playbook adherence

**Followed, and it paid:**

- Sword-intent build only; sword-formation deck never assembled (user ruling). 万法归灵剑
  drawn once (R12) and rolled away.
- 剑劈/剑挡 pushed to lv3 first; 灵气灌注/飞牙剑/震雷剑 stopped at the target levels.
- Never rolled 剑挡, 凝意诀, 云舞诀, 连环剑阵, 剑意激荡, 灵猫乱剑.
- 1-card = 1-cultivation fate rule at the 境2/境3 gates (猫爪 over 变换之道/云之道/云剑传承).
- ≥3 cards kept in hand every round 灵猫乱剑 was fielded (R8 onward), enforced when absorbing.
- Roll hoard R7–R11; [置换] cards (练笔 ×4, 触类旁通 ×3, 以画入道) rolled on sight from R5.
- Deck thinning by `pool` counts: 巨虎灵剑 7→0 by R4, 剑挡 8→0 by R6, 骤风剑 7→0 by R4.
- R1 rolling allowed; never rolled for a 好奇心 trigger while the bank was large.

**Deviations (with reasons):**

1. **R12 境5 天命: took 休养生息 (+30 命) over 灵剑传承 / 斩道 (cards).** This inverts
   "fates that GIVE CARDS outrank stat fates". Reasoning: at MAX realm 修为 is inert, I held
   **20 roll charges**, and the pool still had every phase-5 keeper — cards were purchasable,
   命 was not, and I was in a 3-way 命 race (82 / 83 / 78). It paid 30 命 and is the single
   largest swing in the game. Proposed rule change: the card-over-stat heuristic is a
   BUILD-phase rule; at the 境5 gate with a full roll bank, take the 命.
2. **R9: absorbed 云剑·猫爪 for 1 修为.** The letter of the rule held (灵气灌注+1 remained as
   my [无视防御] source) but it removed my only pierce attacker. R10–R15 I could not beat
   慕虎's earth wall or 陆剑心's formation deck (−18…−27 each) and 4 of my 6 losses came from
   those two. It bought the R8 境4 break window, so I would take it again — but it is the
   clearest cost line in the game.
3. **R10–R11: fielded 7–8 card boards, not the compressed intent chain.** Measured at R10 with
   the same card pool: 剑劈+2·剑挡+2·飞牙剑+1·灵猫乱剑 = **−10.6, 1/7**, while
   三峰剑·灵气灌注+1·剑劈+2·剑挡+2·飞牙剑+1·灵猫乱剑·震雷剑+2 = **+11.7, 6/7**.
4. **Missed the R4 道韵 offer, which contained 剑意激荡** (bug 1 below) — an outright error,
   worth roughly ten rounds of having the key card.
5. **Absorbed a BOARD card (飞牙剑 lv1) at R8** to cross the 境4 gate a round early. Cost about
   1 命 of board margin, bought 灵猫乱剑 a round sooner.

## Notable decisions

- **R6 double break with the fate list pre-loaded.** `break 45 46 44 55 …` before the call got
  both 猫爪 and 猫魂庇佑 in one command. The character-fate slot is deterministic per phase
  (林小月: 境2 猫爪, 境3 猫魂庇佑, 境4 灵猫乱剑, 境5 灵猫踏云), so the preference list can be
  written once at R1 and never revisited.
- **R12 sequencing: absorb → break → farm → catnip.** Absorbed 6 to hit 55, broke, burned the
  bank to 1 and farmed all 9 curiosity triggers, then ate the catnip on 灵猫乱剑. Farming after
  the break also makes the 10% 法宝/灵宠 branch roll at max phase.
- **R15: absorbed exactly ONE card to move 修为 66 → 67.** 花沁蕊 was on 66 — a coin-flip tie —
  and against her my board was +25 first / −28 second, while 牧逸风 (70) and 陆剑心 (71) were
  +29 only in the second seat. One point of 修为 bought the good side of every matchup at once.
- **R16: declined all absorbs to stay on 71.** Two more merges would have tied me with 慕虎 on
  73, where the same board went **−31 first / +31 second**. From R15 on, cultivation was managed
  as a seat dial, not as a resource.
- **R16 ordering discovery.** …剑意激荡+2 · 飞牙剑+1 · 灵猫乱剑+1 beat 花沁蕊 (+28) and
  慕虎 (+25) but lost to 陆剑心 (−29); swapping the last two cards flipped it exactly
  (−29 / +31 / +31). I took the first because the pairing rule avoids your immediate-previous
  opponent and 陆剑心 had just been my opponent — the no-repeat pairing rule is exploitable:
  at 4 players or fewer, discard the matchup you cannot be paired into.
- **R17: the minimax board.** 云剑·游龙 · 画龙点睛 · 剑劈+2 · 凝意诀 · 御空剑阵 · 剑挡+2 ·
  剑意激荡+2 · 灵猫乱剑+1 scored **+22 or better against both survivors in both seat orders** —
  the first board all game with no losing branch. It killed 慕虎 the same round.

## Playbook rules that look wrong in practice (with numbers)

1. **"Going FIRST is better in ~99% of cases."** Not in this game. Both seats measured on the
   fielded board:

   | round | matchups where 2nd was better | worst first-seat result |
   |---|---|---|
   | R2 | 7 / 7 | 慕虎 −3 (2nd: +4) |
   | R3 | 7 / 7 | 慕虎 −6 (2nd: +5) |
   | R15 | 3 / 4 | 牧逸风 **−29** (2nd: **+29**) |
   | R16 | 3 / 3 | 慕虎 **−31** (2nd: **+31**) |

   R15/R16 are ±58–62 命 from the seat alone on an identical board. What held was game5's
   "buy the seat that suits your clock" — a 9-turn 剑意激荡 combo wants the last word. The half
   of the user ruling that clearly held is the tie clause: never sit on a coin flip (R15 and R16
   were both resolved by nudging 修为 by exactly one point).
2. **"Cycle compression / board length is the clock."** True only once 剑意激荡 is fielded.
   Before it (R9–R11, 境4, 灵猫乱剑+1 the only payoff) the compressed 4-card chain was
   **−10.6 命, 1/7** while the 8-slot board was **+8.3, 5/7**. After it (R15+) the 6-card chain
   and the 8-card version scored byte-identically because the kill lands on turn 9 and slots 7–8
   never fire. Suggested wording: compression is a phase-5 tool that needs an intent multiplier;
   at 境4 with only 灵猫乱剑, field the long board.
3. **猫薄荷 "absorb EVERY other lv1 card first"** is over-strict — only 猫-named lv1 cards can
   dilute the roll. "Absorb every other lv1 猫 card" is sufficient (shielding 剑意激荡 is
   therefore unnecessary too).
4. **"Only TWO 飞牙剑 copies are ever needed."** One lv2 copy carried R6–R16 and was benched
   from R17. The 3rd/4th copies are better spent as 修为 for the 境4 gate.

## Bugs / suspicious behaviour (reported, not fixed)

1. **`daoyun` preferences must be set BEFORE the `end` that opens R4 (or R14).** The 道韵 offer
   fires inside `begin_round`, which runs at the tail of `play.py end`. The R4 offer here
   contained **剑意激荡** and was resolved by the default (自在随心) because the preference was
   set after the offer appeared in the R3→R4 log. Driver-UX trap, not an engine fault, but the
   docstring ("preference list for the R4/R14 道韵 offer") reads as if it can be set during R4.
   Fix: prompt for 道韵 prefs at R3/R13 end, or defer the selection to the start of the player's
   R4/R14 command phase.
2. **The 天命 offer log prints the post-increment realm.** A 境1→境3 double break logs
   "天命 offer @realm3" twice, even though the first offer is the 境2 slot (it contained 猫爪,
   the phase-2 character fate). `fate_chooser` reads `p.realm` after `try_breakthrough` has
   already advanced it. Cosmetic, but it makes double-break logs hard to read.
3. **休养生息 granted +30 命 at 境5 against card text "命元+14".** Confirmed-by-design per the
   game5 triage (magnitudes scale with pick phase; the offer line shows base text) — flagged
   again only because the offer display is materially misleading at the moment of choosing: at
   境5 every stat fate is worth roughly double what it advertises, which is exactly the
   information needed to weigh it against a card fate.
4. **好奇心 at exactly 1 charge is an unbounded free-roll engine.** `env.reroll` decrements to 0,
   `curiosity_surprise` grants a card and does `p.rerolls += 1`, so the loop never terminates on
   charges — 9 triggers cost 0 net charges and 0 cards. Working as written, but it means the
   "never roll FOR a 好奇心 trigger" rule only binds while the bank is large.
5. **`roll` on a board card still warns on stdout and silently continues the rest of the
   argument list** (open since game2). Use `take` first, always.
6. `show`'s opponent line mixes live 修为/命 with the round-open board snapshot. That is the
   intended fog behaviour (修为 is public) but the two halves come from different points in
   time, which is easy to misread.
7. Hand-limit trimming logs correctly ("!! hand over 16: dropped …" at R19) — the game2 silent
   drop is fixed.

## Rules confirmed working in play

- `break <ids>` honours the preference list on the breaking call (game5 bug 1 fixed) — verified
  at R6 (two gates in one command, both preferences taken), R8 and R12.
- `sim` seat order uses live cultivation (game5 bug 2 fixed); its seat verdicts matched the
  actual assignment in all 19 rounds.
- `show` reports the round-open (last fielded) opponent boards (game5 bug 3 fixed).
- No-bye handling exercised at R12 (7 alive, I was the odd one and paid −20) and R17 (3 alive,
  I was the odd one and killed 慕虎). Only the odd player risks 命 — correct both times.
- Pairing avoids the immediate-previous opponent when the pool allows — visible and exploitable
  at 3–4 players.
- `pool` counts are accurate and drove every roll choice.
- 猫魂庇佑 parity halving works. 慈念曲 never appeared, so its new implementation is untested.
- 机缘造化 was never offered.

## Fog of war

Six losses, four of them straight fog misses where the sim (opponent's last board) said win:

| round | sim | actual | what changed |
|---|---|---|---|
| R3 | +5.9 vs 牧逸风's R2 board | **−5** | he added 剑劈, upgraded 剑挡/灵气灌注 |
| R9 | +14 / +15 vs 花沁蕊's R8 board | **−13** | 水灵·春雨 added, 水灵·波澜 upgraded |
| R13 | +29 me-second vs 陆剑心's R12 board | **−26** | 聚灵心法+2, 巨鲲灵剑+1, 白鹭灵剑+1 |
| R15 | +29 me-second vs 陆剑心's R14 board | **−18** | 聚灵丹+1, 白鹭灵剑+1 |

R16–R19 boards were chosen by a **minimax** criterion (best worst-case across both seat orders
against every survivor) rather than best average — all four rounds won, three by more than the
sim predicted. That is the practical answer to the fog: stop optimising the mean.

## Playbook numbers measured this game

- 猫魂庇佑 halving: **≈42 命** across four losses (the difference between 1st place and ~28 命).
- 休养生息 at 境5: **+30 命** (card text says 14).
- 剑意激荡 level curve on the same board: lv1 +14.5 → lv2 +27.8 → lv3 +28.5 avg 命 margin.
- Board length at 境4 without an intent multiplier: 4-card chain **−10.6 (1/7)** vs 8-card
  **+8.3 (5/7)**.
- Seat value on the R15/R16 boards: **±58 to ±62 命** from the seat alone.
- 好奇心 farm: 9 triggers, **0 net charges**, 9 cards, guaranteed 猫薄荷 on the 9th.
