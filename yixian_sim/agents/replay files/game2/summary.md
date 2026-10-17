# Game 2 — 林小月 猫画师剑意 (seed 77) — 1st place, 19W-1D-0L, 命 100 untouched

Played 2026-08-24 by an Opus agent following the game1 review rules
(`replay files/game1/review.md` + `summary.md`). Files: `log.txt` (597 lines,
exact-state sync), `replay.html` (355-move replay).

## Result

- Final: **100/100 命**, never lost a single point. R1 DRAW ±0, then 19 straight wins
  (+8 → +35). Last survivor: 吴策 at 23.
- Final board (cyclic): 凝意诀+1 → 剑挡+1 → 青铜猫+1 → 剑意激荡+1 → 流云乱剑+1 →
  云剑·猫爪+1 → 灵猫乱剑+1 → 云舞诀+1 (sim +37 vs the last survivor).
- Realm path: 境2 R4 (猫爪) · 境3 R6 (猫魂庇佑) · 境4 R9 (灵猫乱剑) · 境5 R12 (灵猫踏云).
- 好奇心: 6 triggers in R1 hunting the first 猫薄荷 (got 青铜猫×2 → merged, 破空雕,
  玄银甲, 云剑·飞砂, then 猫薄荷); 3 late (逗猫棒, 猫薄荷, 逗猫棒).
- 猫薄荷 #1 (R9) hit 云剑·猫爪 on a coin flip (灵猫乱剑 also lv1 — should have cleared
  competitors first); #2 (R12) done correctly: absorbed 逗猫棒 first, then catnip →
  灵猫乱剑+1.

## Agent's deviations from the review rules (with its reasons)

1. Broke 境2 at R4 (early): core already assembled, zero roll fodder left that round.
2. Dropped 飞牙剑/骤风剑/飞灵闪影剑 from the target list — the Oracle preferred
   流云乱剑+1 and 云舞诀+1 (飞灵闪影剑 tested −0.3 vs the incumbent at R18).
3. Did not hold 3 hand cards for 灵猫乱剑 — the hand-count bonus is not simulated
   (see bugs), so it absorbed for 修为 instead.
4. Flagged 研墨 (8攻/[灵气]+1) as keeper-grade, not dead — the "dead card" list may
   be wrong on it.

## Bugs the agent found — status

1. **灵猫乱剑 hand-count bonus is dead**. FIXED (2026-08-25) — three stacked causes:
   (a) `to_fixture` sent no hand info → now emits `handCards` (kept hand), which
   `oracle_sim._player` forwards to the engine's `NativeFixturePlayer.handCards`;
   (b) the bundled Oracle.dll predated the engine's handCards support → rebuilt+
   redeployed; (c) inside the engine, Card_9's effect is an async state machine that
   NEVER runs headless, and from-scratch sims have an empty battleParams queue (the
   attack count is server-computed live) → DllPatcher now shims the card synchronously
   and computes `attackCount + min(3, handCards.Count)` when the queue is empty
   (replays with a queued param are untouched, so parity holds). Verified scaling:
   hand 0/1/2/3/6 → life −12/−10/+11/+12/+12 (bonus caps at 3, per card text).
   Ghost opponents now also replay their recorded hands (`ghosts.json` + `apply_ghost`),
   and `sim` on a candidate board uses the remaining hand (held minus fielded).
   Implication for play: holding 3 cards for 灵猫乱剑 is now correctly valued —
   past sims systematically underrated the card.
2. **洗髓丹 [炼化] mis-mapped** — granted pills resolved to roguelike ids (洗髓丹→230,
   whose params gave +30 修为). FIXED: `cards.name_to_base_id` is now pool-aware —
   19 names re-resolved to their sect/sidejob million-block ids (all Elixirist pills,
   all 符咒师 talismans, 破空爪, 罗刹扑). NOTE: this game's log predates the fix, so
   its 洗髓丹 absorb (+30 修为 at R~15) is inflated.
3. **Silent hand trim at 16** ate 御空剑阵+1 / 画龙点睛+1 / 凝意诀 between R17-R18.
   FIXED: the driver now logs `!! hand over 16: dropped …`.
4. `merge` with a missing second copy exits 1 and kills `&&` chains (`roll` on a board
   card only warns). OPEN — minor CLI inconsistency; use `;` between chained commands.
5. **The R1 "DRAW" was a rules bug (found post-game).** The agent turtled an all-DEF
   board (剑挡/青铜猫+1/灵气灌注), the battle hit the engine's 64-turn cap, and the
   sim moved 0 命 because the cap reports lifeDamage 0. USER RULING: at turn cap the
   lower-HP side LOSES and pays the OFFICIAL 命元伤害 formula on the final HP diff:
   diff ≤ 20 → round + 1 + ceil(diff/5); diff > 20 → round + 5 +
   min(ceil((diff−20)/10), 2 + round/2); rounds 1-9 take 1 less (Immortal Relic).
   Implemented as `economy.destiny_damage`, wired into `env.apply_battle`'s cap
   branch and the driver's `sim` display (`[turn cap → −N 命]`). Verified that the
   Oracle's lifeDamage on DECIDED battles already equals this formula (hpΔ 11 →
   4/8/16 命 at R1/R5/R12; game1's R19 hpΔ 107 → 33 matches the log), so kills were
   always correct — only the cap case was free. Under the corrected rule this game's
   R1 stall would have cost ~4 命. 猫魂庇佑 still halves even losses.

## The user's play review (full text in review.md) — key rulings

- R1: HOLD rolls — keep junk cards (云剑·飞刺 etc.) as roll fodder for later rounds;
  a playable R1 board (even 轻剑/巨虎灵剑/剑挡) beats spending charges blind.
- Don't roll pieces of a good-enough board (护身灵气 with 剑挡/青铜猫/震雷剑 stands).
- Never roll 剑挡. Roll 骤风剑 once 震雷剑 + a qi card exist; never MERGE 骤风剑 then
  (merging wastes a roll-fodder copy).
- Preferred line: 剑挡+1 · 剑挡 · 灵气灌注 · 飞牙剑 · 震雷剑 — the 灵气灌注+飞牙剑
  pairing belongs in the board even when the raw sim ranks another set slightly higher.
- 道韵: take 自在随心 (draw 1 now) unless 剑意激荡 is offered; 画龙点睛 is not worth it.
- 天命: when behind on cultivation, 顿悟 (+2 cult) outranks 猫爪 (~1-cult value).

## Rules confirmed working in play

- +2 max HP/round (this was the first game with it).
- [置换]-before-好奇心 ordering: rolling 练笔 at the last charge refilled charges
  without consuming a trigger.
