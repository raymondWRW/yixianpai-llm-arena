# Game 3 — 林小月 猫画师剑意 (seed 105, `--ghosts`) — 2nd place, 9W-0D-9L, eliminated R20 at 命 0

Played 2026-08-27 by an Opus agent following `agents/strategy_linxiaoyue.md` plus the
game1/game2 reviews. Files: `log.txt` (471-move exact-state log), `replay.html`.

**First game against RECORDED REAL BOTS (`--ghosts`)** — a completely different opposition
class from game1/game2's Oracle-search baseline: pid1 姜袭明[ai7-lv5], pid2 吾行之[ai4],
pid3 慕虎[ai2], pid4 龙瑶[ai5], pid5 陆剑心[ai7], pid6 炎雪[ai3], pid7 炎尘[ai5].
That is the headline finding of the game (see "What actually went wrong").

## Result

- **命 100 → 0**, eliminated in R20 as the LAST player knocked out → **2nd of 8**.
  Winner: pid3 慕虎 (25 命, an all-土灵 defence wall).
- Record: **9W · 0D · 9L · 2 byes** (byes R14, R19).
  - R1-3 LOSS (-5/-6/-6, phase-1 board vs lv4-5 bots) → 83
  - R4-R10 **seven straight WINS** (+8 → +17), 命 untouched at 83
  - R11 on: the ghosts hit 境5 and the phase-1 core was outclassed —
    L, W, L, bye, L, L, W, L, bye, L
- Elimination order: 陆剑心 R11 · 炎尘 R11 · 吾行之 R12 · 姜袭明 R17 (killed by me) ·
  龙瑶 R18 · 炎雪 R19 · **me R20**.
- Final board (cyclic): 飞灵闪影剑 → 化灵诀+1 → 飞灵闪影剑+1 → 飞云丹 → 万法归灵剑+1 →
  飞牙剑+1 → 剑挡+2 → 剑意激荡 (sim -30 vs 慕虎; no board in a 4000-sample search beat
  the wall).
- Realm path: 境2 R5 (机缘造化) · 境3 R6 (猫魂庇佑) · 境4 R9 (灵猫乱剑) · 境5 R12
  (剑韵修炼). Final 修为 99.

## How the phase plan actually went

- **Phase 1 (R1-R5) — executed close to the guide.** The full target board was assembled by
  R4, one round early: 剑挡+2 (lv3) · 灵气灌注+1 (lv2) · 飞牙剑+1 ×3 (lv2) · 震雷剑+1
  (lv2), plus a 猫薄荷 banked at R3. The only miss was **剑劈, which never got past lv2** —
  it first appeared at R5 (a 练笔 [置换] roll) with a second copy the same round; two more
  never came. R4 was the moment the build came online: -2.9 avg → **+4.7 / 6-of-7 wins**.
- **Left phase 1 at R5**, the late end of the guide's R5-6 window, with 修为 17 (gate 9)
  banked. The breakthrough alone was worth ~+2.4 命/round immediately (HP 45→53 moved the
  same board from +4.0 to +7.1).
- **Roll hoarding held through phases 2-3** (R6-R10: rerolls climbed 5 → 22, only [置换]
  freebies spent). **It broke in phase 4 (R11)** — see deviations.
- **猫薄荷 timing done correctly.** 逗猫棒 (the only other 猫 card) was absorbed at R6, so
  when 灵猫乱剑 arrived at R9 it was the *only* level-1 猫 card in hand or deck and the
  catnip upgrade was **guaranteed** (`fx 猫薄荷[炼化]: 升级1级牌 灵猫乱剑`). This is the
  game1/game2 mistake fixed.
- **Phase 5 (R12-R20)**: hoard spent as planned; **剑意激荡 was found at R17** and did make
  the board (R19-R20). 万法归灵剑+1 and 飞灵闪影剑+1 (both from 妙笔生花 [置换] grants)
  were the strongest cards I ever fielded — the R17 board built around them scored **+24
  and eliminated 姜袭明**.

## 好奇心 usage (9/9 triggers, all consumed)

The fate reads *"when you use your LAST exchange chance"* — max 9 times. Two rules follow
that the earlier games' notes did not spell out:

1. A trigger fires only at **exactly 1 charge remaining**, and it refunds +1 → **triggers
   are free**. Stopping a roll chain at 2 charges banks them perfectly.
2. Spent: 2 in phase 1 (R2 逗猫棒, R3 **猫薄荷** — exactly the game1 rule: farm until the
   first catnip, then stop) and **7 farmed back-to-back in R12**, right after reaching
   境5, at a standing cost of 0 charges.
3. **The phase-5 surprise pool was junk**: 逗猫棒, 逗猫棒, 云剑·飞砂 ×3, 青铜猫, 猫薄荷.
   No 法宝/灵宠, nothing above phase-1 quality. Banking triggers for phase 5 (the game1
   ruling) paid **nothing** this game — either the surprise pool is not phase-aware in the
   sim, or 林小月's surprise table is cat/云剑 chaff (flagged below). The second 猫薄荷 was
   still used properly: 青铜猫 absorbed first to clear 猫 priority, catnip then upgraded
   云舞诀 → 云舞诀+1.

## What actually went wrong

The build worked as designed and still lost, because **the recorded bots scale and
林小月's phase-1 core does not**:

| Round | my board (unchanged core) | sim avg 命 |
|---|---|---|
| R7 | 剑劈+1·剑挡+2·化灵诀+1·飞牙剑+1×3·震雷剑+1·灵气灌注+1 | **+9.0** |
| R8 | same | +4.9 |
| R11 | same | **-10.0** |
| R13 | same | **-25.0** |

Nothing about my board changed between R7 and R13 — 龙瑶/炎雪 reached 境5 with full 8-slot
云剑 combo decks (云剑·游龙+1 / 月影+2 / 闪风+2 chains) and 慕虎 with a 土灵 wall, and a
board of 4-9 ATK phase-1 cards stops competing. 炎雪 was killing me in **7 turns** at R12.
The sword-intent engine never got the card quality to cash its stack: 剑劈 stuck at lv2
meant only ~9-12 intent, and every attempt to insert a bigger body (巨鲲灵剑, 巨鹏灵剑+1,
灵感剑, 三峰剑) **broke the qi chain** the 飞牙剑s run on, costing 5-15 命 in sim.

Two mechanics understood only mid-game, worth writing into the guide:

1. **`turns` in the sim counts BOTH sides' turns** — a 12-turn battle is only ~6 of my card
   plays. Slots 7-8 frequently never fire; front-loading is not a preference, it is most of
   the board. Several R6-R10 sims were byte-identical no matter which card sat in slot 8.
2. **The 灵猫乱剑 hand-count bonus outweighs the 8th board slot.** At R12 the same 8-card
   board scored **-14.8 with 2 hand cards and -7.4 with 4** — a 7-命 swing. From R12 on I
   deliberately fielded **7** cards to keep 3 in hand.

## 猫魂庇佑 exploitation (why this finished 2nd instead of 5th)

Once every board was losing, the fate became the whole strategy. `economy.destiny_damage`
gives, at round *r*, `dmg = r + 5 + extra` with `extra = min(ceil((hpDiff-20)/10), 2+r/2)`;
猫魂庇佑 halves only EVEN `dmg`. So the 命 cost of a loss is a **sawtooth** in HP margin:
at r=13, hpDiff 81-90 → 25 (full), hpDiff 91-100 → 26 → **13**. Losing *harder* can cost
half as much.

I wrote two helper scripts (session scratchpad, not committed) that score candidate boards
by **post-halving 命** rather than raw margin, plus a hill-climber:

- R13: raw-best board = -16.5 effective; parity-aware best = **-12.0**. Same card pool.
- R11-R20 total raw margin was -189; actual 命 lost was **-83**.
- Halving confirmed: R11 raw -20 → 命 83→73; R18 raw **-34 → only 17 lost**, which is what
  let me survive R18 at 2 命 and then take the R19 bye.

**The parity gamble also cost me the game once.** At R16 the sim predicted raw **-30**
(even → 15) at hpDiff -103; the real battle came in at **-29** (odd → full 29), taking me
48 → 19 in one round. Cause: `oracle_sim.matchup(fx, ofx)` always puts MY fixture first,
but `env.acts_first` gives the first move to the **higher-修为** side, and 慕虎 was ahead.
Boards whose predicted hpDiff sits within ~5 of a band edge are coin flips. From R17 I
absorbed spare cards purely to buy 修为/initiative (81 → 99 over R18-R20) and preferred
bands with ≥10 HP of margin on both sides.

## Deviations from the guide (with reasons)

1. **境2 天命: 机缘造化 over 休养生息 (+14 命).** Guide says prioritise cultivation/card
   fates; 机缘造化 is a card fate and produced 化灵诀, which became a permanent board
   fixture (the qi engine the whole 飞牙剑 chain runs on). At 83 命 the +14 命 was tempting
   and in hindsight probably the better pick given how the game ended.
2. **境5 天命: 剑韵修炼 over 储纳灵气.** 剑韵修炼 gives 修为+2 **and** +2 剑意 at battle
   start — both cultivation (guide-sanctioned) and the build's core resource.
3. **Broke the phase-2-4 roll hoard at R11.** Spent 20 of 22 banked rerolls in one round
   because the board had fallen to -10.0 avg while bleeding ~20 命/round; the hoard is
   worthless if you die before phase 5. It bought 三峰剑, a 3rd 剑劈, and the
   巨鹏灵剑/巨鲸灵剑 tests. Judgement call I would repeat — but it left only 7 charges for
   the actual phase-5 arrival at R12.
4. **Dropped 灵气灌注 from the board from R12.** The guide/game2 review want the
   灵气灌注+飞牙剑 pairing fielded, and the brief says never absorb the last [无视防御]
   card. I never absorbed it, but from R12 the sim was emphatic it does not fit (any
   insertion into slots 4-7 cost 5-15 命 by starving qi). The [无视防御] role was later
   filled by 飞云丹 (2 attacks).
5. **三峰剑 did not replace 震雷剑** (guide, phase 3). Found at R11 at lv1 (3攻×3); every
   board containing it tested 5-10 命 worse than the 震雷剑+1 incumbent. Absorbed.
6. **Absorbed aggressively from R7 on** for cultivation (and from R17 for turn-order
   initiative) rather than keeping spare cards as roll fodder. With 55 修为 needed for 境5
   and only +2 passive/round, absorbs were the only scaling cultivation source. Note that
   rolling is cultivation-NEUTRAL (1-for-1 exchange), so hoarding rolls and racing to 境5
   do not conflict — but hoarding *cards* and racing to 境5 do.
7. **R1: held all rolls** per the binding rule, eating a -5 loss with a 0/7 board. Correct
   by the rule; against ghosts this strong the alternative (farming 好奇心 in R1 as in
   game1) would not have produced a winning R1 board either.

## Bugs / suspicious behaviour (reported, not fixed)

1. **`sim` assumes I always act first.** `oracle_sim.matchup(fx, ofx, rnd)` puts my fixture
   in the acting-first seat unconditionally, while the real battle gives the first move to
   the higher-修为 side (`env.acts_first`). Every sim against a higher-修为 opponent is
   therefore optimistic, and at R16 the resulting 1-point error flipped 猫魂庇佑's parity
   and cost 14 命. Suggest `sim` take act-order from `acts_first`, or report both seats.
2. **A bye re-logs the previous round's battle line.** `finish_round` never clears
   `st["last_battle"]`, so on bye rounds R14 and R19 the log reprints `R13 vs pid3 …` /
   `R18 vs pid3 …` with no indication a bye happened (log lines 560, 694). Misleading in
   both log and replay; a bye should be logged explicitly.
3. **好奇心's "随机惊喜" pool looks phase-blind.** All 7 triggers farmed at 境5/phase 5
   returned phase-1-grade cat/云剑 chaff (逗猫棒 ×2, 云剑·飞砂 ×3, 青铜猫, 猫薄荷). If the
   real game escalates the surprise pool with phase, the "bank triggers for phase 5" ruling
   is currently unrewardable in the sim.
4. **`roll` on a board card only warns on stdout and silently continues the rest of the
   argument list** (R19: `画蛇添足 is on the board — take it first`, while the other five
   rolls in the same command went through). Still OPEN from game2's item 4, along with
   `merge` exiting 1 on a missing copy.
5. **8-slot boards are frequently indistinguishable in `sim`.** At R6-R10, swapping slot 8
   between cards of wildly different power (灵气灌注+1 vs 破气剑 11攻 vs 飞牙剑+1) gave
   identical results. Explained by the turn count (both sides' turns → ~6-7 of my plays in
   a 13-turn battle), so probably correct — but it makes the "always field all 8 slots"
   instinct actively wrong, and the guide should say so.
6. No hand-16 trims occurred (`!! hand over 16` never fired) — I absorbed down to the cap
   manually at R16-R19. The R17 hand did reach 21 cards before cleanup, so the guard is
   reachable and worth watching.

## Rules confirmed working in play

- 猫魂庇佑 halves EVEN 命 losses only, applied to `|lifeDamage|` in `env.apply_battle`
  (verified twice: raw -20 → 10, raw -34 → 17).
- Turn order = higher 修为 acts first (ties → coin flip).
- Reroll grants bank without limit: +3/round R1-9, +4 R10-12, +6 R13+.
- [置换] cards are free value and never burn the pool — 练笔 (+2 charges, net +1),
  以画入道 (a sect card at your CURRENT realm — worth holding until after a breakthrough:
  mine cashed at 境4 for 白鹭灵剑), 触类旁通 (+1 charge + a non-painter sidejob card),
  妙笔生花 (an already-UPGRADED 金丹期+ card — produced 万法归灵剑+1 and 百鸟灵剑诀+1, the
  best roll target in the game).
- 猫薄荷 targets level-1 cards in **hand or deck** with 猫-name priority — clearing rival
  猫 cards first makes the upgrade deterministic.

## Post-game triage of the bugs (2026-08-27)

1. **sim first-mover bias — FIXED.** `sim` now seats the higher-修为 side as p1,
   mirroring `env.acts_first` (opponent higher → matchup runs flipped and the
   result is negated; ties keep me as p1, where reality coin-flips).
2. **Bye reprinting stale battle — FIXED.** `finish_round` resets `last_battle`
   to an explicit "BYE (no opponent this round)" before pairing.
3. **好奇心 surprise pool "phase-blind" — by design (user ruling):** the 90%
   branch is always the five p1 cat cards; only the 10% 法宝/灵宠 branch scales
   with phase. Banked triggers pay out via the 10% branch and 换牌+1, not better
   cat cards.
4. CLI arg-list continuation after a bad `roll` — still open (minor).
5. `turns` counting both sides (≈half are my plays) — informational; the
   "front-load, field 7 when the hand bonus beats slot 8" playbook notes stand.
