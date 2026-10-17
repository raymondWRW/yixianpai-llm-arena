# Game 5 — 林小月 猫画师剑意 (seed 109, `--ghosts`) — 2nd place, 9W-0D-9L, eliminated R18 at 命 0

Played 2026-08-31 by an Opus agent following `agents/strategy_linxiaoyue.md` (with the
game4 endgame revision) plus the game1–game4 reviews. Same recorded-bot lobby as game3/4:
pid1 姜袭明[ai7-lv5], pid2 吾行之[ai4], pid3 慕虎[ai2], pid4 龙瑶[ai5], pid5 陆剑心[ai7],
pid6 炎雪[ai3], pid7 炎尘[ai5].
Files: `log.txt` (722 lines / 501 moves), `replay.html`.

**First game under the new rules: fog-of-war sims (opponents' LAST-round boards only) and
NO byes.** Both changed the game materially, and the fog is what killed me.

## Result

- **2nd of 8.** Eliminated in R18 as the last player knocked out; winner **慕虎 at 11 命**.
- Record: **9W · 0D · 9L · 0 byes**.
- 命 curve: 100 → 95 (R1 L) → 89 → 83 → 83 (R4 W) → 75 → 75 (R6 W) → 64 (R7 L) →
  64 through R9 (two wins) → 47 (R10 L) → 47 (R11 W) → 31 (R12 L) → **5** (R13 L −26) →
  7 (小鱼干 [炼化] +2 命) → 7 through R17 (four straight wins) → **0** (R18 L −34).
- Elimination order: 炎尘 R13 · 吾行之 + 陆剑心 R14 · 姜袭明 + 龙瑶 + 炎雪 R16 (I killed
  龙瑶) · **me R18**.
- Realm path: **境1 → 境3 in one round at R6** (double breakthrough: 锻体, 顿悟) ·
  境4 R8 (灵猫乱剑) · 境5 R12 (灵剑传承). Final 修为 82, HP 115.
- Final board: 剑劈+2 · 剑挡+2 · 御空剑阵 · 画龙点睛 · 凝意诀 · 剑意激荡+1 · 灵猫乱剑+1 ·
  流云乱剑 (sim **+28 vs 慕虎's R17 board**; his actual R18 board beat it **+34**).

## The game in one line

The phase-1 core came online exactly as the guide draws it, then the ghosts out-scaled it
from R10 to R13 and I fell to 5 命. From R14 a **cycle-compression** rebuild (drop everything
that is not an intent generator or the payoff) turned the deck around: four straight wins
worth +27/+24/+24/+26 that eliminated 龙瑶 and took 慕虎 from 58 to 11. R18 needed one more
win the sim scored at +28 — and 慕虎's *unseen* R18 board (土灵·合八荒 swapped in) won by 34.

## How the guide's phase plan went

- **Phase 1 (R1–R6): the guide's target board was assembled in full, one round late.**
  By R6: **剑劈+2 · 剑挡+2 · 灵气灌注+1 · 飞牙剑+1 ×2 · 震雷剑+1**, with 猫薄荷 banked at
  R2. First game where *both* 剑劈 and 剑挡 reached lv3 (game3 missed 剑劈, game4 missed
  剑挡). R6 drew four 剑劈 in one round of rolls.
- **Broke phase 1 at R6** (guide window R5–6) — and broke **twice in the same command**,
  境1 → 境3, because three merges took 修为 from 18 to exactly 21 (the 境3 gate).
  Necessary: every ghost was already 境3 with 修为 23–29 while I was 境1/18.
- **Roll hoard held through phases 2–4.** R7–R11 spent only [置换] freebies; charges climbed
  3 → **21** by the 境5 breakthrough at R12, then bought 云舞诀, 镜花剑阵, 画龙点睛,
  剑意激荡 ×2, 连环剑阵 ×2, 凝意诀, 御空剑阵, 水月剑阵, 飞灵闪影剑, 巨鲲灵剑 ×2,
  流云乱剑 ×3, 运笔如飞 ×2 — essentially the whole guide keeper list.
- **猫薄荷 #1 (R8) landed on 灵猫乱剑 deterministically** — absorbed immediately after the
  境4 fate granted it, with no rival lv1 猫 card anywhere.
- **猫薄荷 #2 (R13) went to 镜花剑阵** after absorbing four junk lv1s (云剑·回守, 反身剑,
  形意剑, 慈念曲) to shrink the candidate pool; every remaining lv1 was a keeper.

## 好奇心 (9/9 triggers, all consumed)

1. **R2, trigger #1 → 猫薄荷 on the first try**, then stopped per the game1 ruling.
2. **Triggers #2–#9 farmed in phase 5 (R13 ×2, R14 ×6)** at zero standing charge cost.
   Yield: 猫薄荷, 青铜猫, **小鱼干**, 逗猫棒 ×3, 云剑·飞砂, 云剑·月影.
3. **小鱼干's [炼化] is +1 max HP and +2 命** — at 5 命 that was 40% of my life total and it
   is why I was alive at R15. At low 命 a banked 好奇心 trigger is a lottery ticket for 命,
   not just for cards.

## The R14 rebuild — the most important discovery of this game

At R13 my 8-slot "full" board (画龙点睛 · 剑劈+2 · 剑挡+2 · 云舞诀 · 剑意激荡 · 灵气灌注+1 ·
飞牙剑+2 · 灵猫乱剑+1) scored **−4.4 and 3/7**, kills landing on turn 15–16 while 龙瑶/炎雪
killed me on turn 11–12. Cutting the board to the **minimum intent chain** —

    剑劈+2 · 剑挡+2 · 画龙点睛 · 剑意激荡+1 · 灵猫乱剑+1     (5 cards)

— moved the kill to **turn 9–10** and flipped the same matchups to **+23/+24/+27**.
Everything dropped (灵气灌注, 飞牙剑, 云舞诀, 流云乱剑, all the 剑阵s) was a *turn* the
payoff had to wait for. At R16, swapping 画龙点睛 → **凝意诀** (a third intent generator)
produced a board that beat **all four survivors in both seat orders** (+27/+29/+24/+28).

**Generalisable rule: with 灵猫乱剑 + 剑意激荡, board length is the clock.** Every extra card
delays the payoff by a full cycle. Field the shortest board containing
generators → 剑意激荡 → 灵猫乱剑, and put nothing in front of 剑劈. Slots 6–8 are free
parking; they change nothing (confirmed repeatedly — byte-identical sims).

## Turn order: this deck wants to move SECOND

Measured at R14–R18 by running both seatings of the same fixture:

| opponent | me first | opponent first |
|---|---|---|
| 姜袭明 | +27 | +28 |
| 慕虎 | +19 | **+29** |
| 龙瑶 | −29 / +22 | **+24** |
| 炎雪 | +21 | **+23** |

Acting second was better in **every** matchup, sometimes by 50 命 (the R14 board flipped from
−27 to +28 across the seat). From R14 I **stopped absorbing** except when forced, to keep
修为 *below* 慕虎/龙瑶/炎雪. This inverts the guide's "keep 修为 ABOVE the opponent" line —
the correct statement is **buy the seat that suits your clock**: a 9-turn combo deck wants
the last word, a slower grinder wants the first.

## How the two new rules changed the play

**Fog of war (last-round boards only).**
- R1 sims are *completely blind* — every ghost's round-open fixture is an empty board, so all
  seven matchups return the identical number. R1 board choice is pure judgement.
- Four losses are directly attributable to the fog: **R5** (sim +8.3 vs 龙瑶's R4 board,
  real −8), **R10** (sim +11.7, real −17 — 陆剑心 had added 水月剑阵+1/镜花剑阵+2),
  **R12** (sim +17 vs 慕虎, real −16 — 土灵阵+2/土灵·山崩 added), and the game-ending
  **R18** (sim +28, real −34 — 土灵·合八荒 replaced 土灵·断崖+2).
- Adaptation: stop trusting a single number; require boards to win **in both seat orders**
  and prefer the board whose worst case is least bad (a minimax hill-climber). That carried
  R14–R17. It cannot cover a ghost swapping a new card in on the decisive round.

**No byes.** Game4 won on four byes, three of which replaced a −25 round. Here there were
none: R13 (7 alive) and R15/R16 (5 alive) each produced an "extra" battle and the odd player
was someone else every time. The rule removed the whole game4 endgame plan (keep 慕虎 alive
as a bye generator) and meant that from R14 at 7 命 **every remaining round had to be won** —
five straight must-win rounds, four of them won.

## Deviations from the guide (with reasons)

1. **R1 board 剑挡 · 骤风剑 · 巨虎灵剑** — an aggressive 20-damage board rather than a
   defensive one, chosen blind (see fog note). Lost −5. Rolling two 巨虎灵剑 first deleted
   all 5 remaining copies from the pool: the best available R1 deck-thin.
2. **Double breakthrough 境1 → 境3 at R6.** The guide only says "leave phase 1 at R5–6";
   taking two gates at once was forced by being a full realm behind the whole lobby.
3. **境3 fates were the default scorer's, not mine — a driver bug (below).** I lost
   **猫魂庇佑** (offered, in my preference list, ignored) and got 顿悟, which also burned 3
   banked rerolls. By game3's arithmetic 猫魂庇佑 was worth ~40 命 across R10–R18; this is
   the largest identifiable cost in the game.
4. **R10: absorbed one card too many and dropped to 2 hand cards.** The same board went
   **+11.9 → +2.4** for one point of (inert) 修为 — the 3rd hand card for 灵猫乱剑 is worth
   **~9.5 命**. Never absorb below 3 hand cards while 灵猫乱剑 is fielded; the cap is a
   cliff, not a slope.
5. **万法归灵剑 drawn twice, never fielded** (guide ban respected); both copies rolled away
   as fodder. Given the pure-intent board's +24…+29 per round in R15–R17, the ban looks right.
6. **飞牙剑 and 灵气灌注+1 were benched from R14 on** despite being phase-1 keepers — each
   costs a turn the 9-turn clock cannot pay for. 剑劈/剑挡/凝意诀/剑意激荡/灵猫乱剑 were the
   only cards that mattered late.
7. **R14 道韵 offered 画龙点睛; took 自在随心** per the game2 ruling (自在随心 unless
   剑意激荡). Defensible, but a second 画龙点睛 would have merged to +1 — worth revisiting.
8. **The anti-慕虎 sword-formation deck was assembled and never beat him.** By R17 I held
   水月剑阵 · 镜花剑阵+1 · 云舞诀 · 巨鲲灵剑 ×2 · 运笔如飞 ×2 · 连环剑阵 ×2 · 御空剑阵 —
   the guide's list bar upgrades. Every formation board tested **−20 to −28** against him
   while the pure intent board tested **+27**. On this board state the formation deck was
   strictly worse; it likely needs the +2 levels the guide specifies.

## Bugs / suspicious behaviour (reported, not fixed)

1. **`break <ids>` ignores the ids on the invocation that actually breaks through.** The
   `break` branch sets `PREFS["fate"]` / `st["prefs"]`, then calls `env.try_breakthrough`
   *before* `save(st)` refreshes `env.prefs`; `_prefs(env)` returns the stale `env.prefs`
   loaded from disk. Both 境3 fates were picked by the default scorer with a valid preference
   list in hand — **this cost 猫魂庇佑**. Fix: assign `env.prefs = st["prefs"]` in the
   `break` branch before `try_breakthrough`. Workaround used afterwards: run `break <ids>`
   once while 修为 is *below* the gate (prints "cannot break" but saves the prefs), then
   break for real later — this worked at 境4 (灵猫乱剑) and 境5.
2. **`sim` takes seat order from the LAST-round fixture's `exp`, not current 修为.** It
   compares `ofx["exp"]` (a round-open snapshot = last round's cultivation) with mine, while
   `env.acts_first` uses live values. 修为 is public information, so this is a pure error —
   and a ~30-命 one on a seat-sensitive deck: at R14 `sim` reported **−1.7 / 3-of-6** for the
   board a correct-seat evaluation scored **+16.3 / 5-of-6**. Fix: take the seat test from
   `env.state.players[pid].cultivation`, keep the board from the fixture.
3. **`show` leaks the current round's opponent boards.** `begin_round` snapshots
   `round_open_fixtures` *before* `apply_ghost` (correct = last round), but `show` prints
   `q.board`, which `apply_ghost` has already overwritten with **this** round's recorded
   board, under the heading "OPPONENTS (last fielded board)". `sim` respects the fog, the
   display does not. I played off `sim` plus a local evaluator and ignored `show`'s boards.
4. **境5 天命 灵剑传承 granted THREE cards, not one.** Text is "获得1张名字含'灵剑'的牌"; at
   the R12 breakthrough the hand gained 巨鹏灵剑 + 巨鲸灵剑 + 巨鲲灵剑 in one step. Possibly
   one grant per realm already reached, possibly a bug. It was in my favour.
5. **`慈念曲`'s 命-damage reduction appears not to be modelled.** Fielding it changed only the
   HP margin; `lifeDamage` on wins and losses was unchanged. Would have been a strong card
   for me at 5–7 命 if it worked.
6. **Random board search is useless on this deck.** 300 random 5–8 card boards from a 19-card
   pool produced **zero** wins, while a hill-climb seeded with the incumbent found +27
   immediately. Order dominates membership by 40–50 命 — any future helper must be a local
   search from the incumbent, not a sampler.
7. Still open from game2/game3: `merge` exits 1 on a missing second copy (kills `&&` chains —
   I used `;` throughout), and `roll` on a board card warns on stdout but silently continues
   the rest of the argument list.

## Rules confirmed working in play

- No-bye handling is correct and logs clearly (`[extra for pidN]`), and only the odd player
  pays 命 — exercised at R13, R15 and R16.
- Realm-cap messaging is fixed: `show` prints "(MAX realm — 修为 past here is inert)" and
  `break` at 境5 no longer invents a gate.
- `pool` is accurate and useful: 巨虎灵剑 8→0 in two R1 rolls, 云剑·厚土 8→0 in R2; thinning
  the phase-1 pool is why four 剑劈 arrived in a single R6 roll chain.
- [置换] ordering (练笔 / 触类旁通 / 以画入道 resolve before 好奇心) held all game; 以画入道
  at 境5 correctly granted a 境5 sect card (云剑·游龙).
- 机缘造化 was never offered, so the fixed behaviour went untested.
- 猫薄荷 targets lv1 cards in hand-or-deck with 猫-name priority — deterministic when
  灵猫乱剑 is the only lv1 猫 card (R8), random among keepers when it is not (R13 → 镜花剑阵).
- 灵猫乱剑's hand bonus caps hard at 3, and the 3rd card is worth ~9.5 命 (R10 measurement).

## Post-game triage of the bugs (2026-08-31)

1. **`break <ids>` ignoring its ids on the breaking call — FIXED.** The command
   now syncs `env.prefs` before `try_breakthrough` (the chooser fires inside it).
   `daoyun` got the same immediate sync.
2. **`sim` seat order — FIXED.** Now compares LIVE cultivation (修为 is public)
   instead of the last-round fixture's exp.
3. **`show` opponent-board leak — FIXED.** Prints the round-open snapshot (their
   actual last fielded board), consistent with `sim`'s fog of war.
4. **灵剑传承 ×3 — NOT a bug.** Its 境5 version reads 获得3张 (fate magnitudes
   scale with pick phase; only the offer line shows base text).
5. **慈念曲 — FIXED (implemented).** [持续] 败者所受[命元]伤害减 4/6/8 by level,
   floor 1, non-stacking (max of both sides' copies); applied before 猫魂庇佑's
   even-halving. Ordering vs the halving is an assumption — flag for user review.
6. Random-board sampling uselessness / seat-choice ("buy the seat that suits your
   clock" vs the guide's "stay above to go first") — measurement notes; the seat
   question needs a user ruling. CLI exit-code quirks still open.

## Playbook numbers measured this game

- The 3rd kept hand card for 灵猫乱剑 ≈ **9.5 命** of margin (+2.4 → +11.9).
- 小鱼干 [炼化] = **+2 命** — at low destiny a banked 好奇心 trigger is life.
- Cycle compression: cutting the board to the bare intent chain (5 cards) moved
  the kill from turn ~15 to ~9 and was worth ~30 命 per matchup from R14 on.
