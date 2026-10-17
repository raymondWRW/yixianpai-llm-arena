# Game 7 — 林小月 猫画师剑意 (seed 117, `--ghosts`) — 3rd of 8, ELIMINATED R17 at 命 0, 8W-0D-11L

Played 2026-09-15 by an Opus agent following `agents/strategy_linxiaoyue.md` (the
2026-09-15 corpus revision), `agents/combat_rules.md`, `agents/top_player_analysis.md`
and the game4-game6 reviews. Randomly seated lobby of 7 recorded 境5-finisher ghosts:
pid1 龙瑶[ai5-lv4], pid2 杜伶鸳[ai6-lv4], pid3 炎尘[ai7-lv4], pid4 炎雪[ai7-lv4],
pid5 陆剑心[ai7-lv5], pid6 吴策[ai4-lv4], pid7 林小月[ai6-lv4] (a painter mirror).
Files: `log.txt` (586 lines / 363 moves), `replay.html`.

## Result

- **3rd of 8.** Eliminated in R17 (命 2 -> 0; -32 halved to -16 by 猫魂庇佑).
  龙瑶 died the same round; survivors at the cut were **陆剑心 (命 60)** and
  **杜伶鸳 (命 21)**.
- Record: **8W · 0D · 11L** over 19 battles (two of them "extra" odd-player-out
  battles at R11 and R16 — I lost both and, correctly, paid nothing for either).
- 命 curve: 100 -> 98 (R1 L) -> 98 (R2 W) -> **91** (R3 L -7) -> 91 (R4-R5 W) ->
  **93** (R6 W, +2 from a 小鱼干 [炼化]) -> 87 (R7 L -12->-6) -> 82 (R8 L -10->-5) ->
  **65** (R9 L **-17, odd, not halved**) -> 67 (R10 W, +2 小鱼干) -> 67 (R11 W) ->
  **55** (R12 L -24->-12) -> **41** (境5 天命 云巅雷劫 **-14 命**) -> 41 (R13 W) ->
  **27** (R14 L -28->-14) -> 27 (R15 W +29) -> **2** (R16 L -25, odd) -> **0** (R17).
- Elimination order: 吴策 R10 · 炎尘 + 炎雪 R13-R14 · 林小月 R16 · **龙瑶 + me R17**.
- Realm path: **境1 -> 境3 double break at R6** (灵剑传承 at the 境2 slot,
  **猫魂庇佑** at 境3) · **境4 at R9** (灵猫乱剑) · **境5 at R13** (云巅雷劫).
- Final board (R17):
  `画龙点睛+1 · 凝意诀+1 · 云舞诀+2 · 御空剑阵+1 · 剑挡+2 · 万邪入体咒 · 灵猫乱剑+1 · 玄晶护心镜`
  — +26 vs 龙瑶 and +27 vs 陆剑心 in my actual (second) seat, -32 vs 杜伶鸳.
  I drew 杜伶鸳.

## The game in one line

Phase 1 went better than any previous game (飞牙剑+2 by R3, 剑挡+2 by R5, 7/7 winning
boards at R4-R6), but **剑意激荡 never arrived** — not from ~45 rolls, not from either
道韵 offer, not from the fate line — so from R12 on the deck had no damage multiplier
while every ghost kept scaling, and four 24-32 命 losses in five rounds burned a
93-命 lead down to zero.

## What actually decided it (three numbers)

1. **剑意激荡: 0 copies, all game.** 6 copies sat in a 225-400-card pool; ~45 rolls,
   two 道韵 offers, an `以画入道` 境5 sect draw and a 5-card 云巅雷劫 all missed it.
   The corpus deck's whole late game is "激荡 x2 + 凝意诀 + 御空 + 连环"; I finished
   with 御空剑阵+1, 连环剑阵 (drawn R17, one round too late) and **no multiplier**.
   Board average vs the field went +19.4 (R10, 境4) -> -8.2 (R13) -> -6.8 (R16): the
   ghosts' curve kept rising and mine flattened at 灵猫乱剑+1.
2. **云巅雷劫 at the 境5 gate cost 14 命 for 5 cards — and I died 2 命 short.**
   Two rounds later that same 14 命 was exactly the difference between surviving R17
   (a -16 post-halving loss against 18 命 of buffer) and elimination. 善假于物
   (抽3张副职牌, free) was on the same offer screen. This is the clearest error of
   the game and it was a *preference-list* error, not a judgement made at the screen
   (see bug 1).
3. **猫魂庇佑 halved 6 losses (-12, -10, -24, -28, -30-class, -32), about 60 命 saved** —
   again the largest identifiable gain, exactly as in game6. Without it I die around
   R13. The losses it did NOT catch were the odd ones: **-17 (R9), -25 (R16)** —
   and those two alone are the 命 I needed at the end. Parity was worth more than any
   board choice in the last five rounds.

## Playbook adherence — the NEW corpus rules, one by one

**Fate line: cultivation-first — attempted, executed badly.**
Offers actually seen (none ever contained 剑韵修炼, 顿悟 or 感悟丛生):

| gate | offered | taken | comment |
|---|---|---|---|
| 境2 (R6) | 猫爪 / 灵剑传承 / 稳固根基 / 副职兼修 | **灵剑传承** | cards-over-stats, correct; delivered **1** card (境2 version) though the log advertised the 境3 text — see bug 2 |
| 境3 (R6) | **猫魂庇佑** / 变换之道(+8换牌,+8上限) / 机缘造化 / 陨星淬体 | **猫魂庇佑** | **deviation.** The binding rule says 猫魂庇佑 only when nothing gives cult/cards; 机缘造化 (a card) and 变换之道 (+8 rolls) both qualified. Forced by an over-long preference list. It paid ~60 命 — but the process was wrong. |
| 境4 (R9) | **灵猫乱剑** / 变换之道 / 云巅雷劫 / 剑阵守护 | **灵猫乱剑** | mandatory, correct |
| 境5 (R13) | 灵猫踏云 / **善假于物 (抽3张副职牌)** / 云巅雷劫 / 机缘造化 | **云巅雷劫 (-14 命)** | **error.** See above. |

**剑韵修炼 never appeared in four gates** — the most-recommended corpus pick is not
reliably on offer in this sim, and the fate plan needs a fallback ordering that
assumes it will not be.

**Absorb tempo: followed, and it is NOT the constraint here.** 2/round R7-R8,
1-4/round R9-R13, finishing at 修为 78. But holding cards is free and absorbing is
instant, so the right policy (found at R11) is *hold everything, absorb in bulk at
the gate round* — same 修为, full-strength board in the meantime. That let me keep an
8-card winning board at R12 and still break 境5 at R13.

**境5 round: R13, not R11-R12.** R11 was arithmetically impossible (55 修为 would have
meant a 3-card board) and R12 would have cost the 8-card board that was worth +12.5 命
that round. The corpus's R11 break is powered by a much richer roll/absorb economy; in
this sim the honest number for a 境1-until-R6 line is **R12-R13**.

**剑意激荡 handling: n/a — never drew one.** The "field both copies unmerged" rule was
untestable. Its substitute was **画龙点睛+1** (4 level-up stacks), the closest thing to
a multiplier the deck had: it upgrades 凝意诀->lv3, 御空剑阵->lv3 and
**灵猫乱剑+1->lv3 (7 hits)** every battle, and moved board average from -8.2 to +6.2 in
one round (R14). Rule found: **count the upgradable cards between 画龙点睛 and the
payoff and keep that number <= (stacks - 1)** so the last stack lands on 灵猫乱剑;
lv3 cards (云舞诀+2, 剑挡+2) are free passes because `try_upgrade_card` fails without
spending a stack.

**Finisher choice: 灵猫乱剑+1 throughout.** 飞灵闪影剑 reached +1 only (two more lv1
copies never paired), so the corpus's 飞灵闪影剑+2 swap never became available and the
3-cards-in-hand rule was kept every round from R9 on.

**Other standing rules kept:** 灵气灌注 immediately before the pierce target; 飞牙剑
between generators and payoff and never into a block turn; 万法归灵剑 rolled away on
sight; sword-formation deck shelved (水月剑阵/镜花剑阵 rolled away); never rolled
凝意诀/云舞诀/连环剑阵/剑挡; hand-16 cap respected (absorbed 6 at R16 when the hand hit
exactly 16).

## Deviations (with reasons)

1. **境3: took 猫魂庇佑 over 机缘造化/变换之道** — process error (stale preference
   list), outcome positive (~60 命).
2. **境5: took 云巅雷劫 (-14 命) over 善假于物** — same cause, outcome fatal.
3. **Spent ~10 charges at R10 to farm 好奇心 for 猫薄荷** instead of hoarding to the
   境5 break (game6's line). It worked — 灵猫乱剑+1 from R10 instead of R13, and
   R10-R11 were the two strongest rounds of the game (+19.4 / +19.0 board averages).
   I would do it again: the hoard is only worth more if phase-5 keepers are findable,
   and at ~2.7% per roll they mostly are not.
4. **R9: absorbed 震雷剑+1 to move 修为 36 -> 37**, breaking two simultaneous ties
   (炎雪 36, 林小月 36) for free — the hand was at 4 cards and 灵猫乱剑 caps at +3, so
   the absorb cost literally nothing. Generalisable: *absorbing down to exactly 3 hand
   cards is always free once 灵猫乱剑 is fielded.*
5. **Seat policy inverted the "go first 99%" rule all game.** Measured repeatedly: at
   R10 the mirror matchup was **-19 first / +22 second**; my second-seat average beat
   my first-seat average in 6 of 7 late rounds (R13 -8.3/-7.5; R17 board A -32 first
   vs +27 second against 陆剑心). I deliberately kept 修为 BELOW the field for R11-R17
   to guarantee the second seat. A 9-12-turn 剑意-burst clock wants the last word;
   this reproduces game6's finding, not the playbook's blanket rule.

## The parity game (new, and it mattered more than board quality)

From R13 on I scored boards on **post-猫魂庇佑 命**, not raw margin, because the
destiny formula's banding makes a *larger* HP gap sometimes cheaper:

- R15: two boards differing by one slot gave 龙瑶 hp -40 -> **-23 命 (odd, full)** and
  hp -43 -> **-24 命 (even -> -12)**. The "worse" board was 11 命 cheaper.
- R16: moving 玄晶护心镜 from slot 7 to slot 5 changed 杜伶鸳 from -31 命 (fatal at
  命 27) to -30 -> -15, and 龙瑶 from -25 to -24 -> -12. Board
  `画龙点睛+1 · 凝意诀+1 · 云舞诀+2 · 御空剑阵+1 · 玄晶护心镜 · 剑挡+2 · 灵猫乱剑+1 · 飞牙剑+2`
  had effective worst case -15 where every neighbour was -29 or worse.
- **Fatal bands at R15-R17** (命 <= 27): hp gaps of 81-90 and >=101 produce ODD damage
  (27/29/31) that 猫魂庇佑 cannot halve. Steering the gap out of those bands is a real,
  controllable lever and belongs in the playbook.

Tooling built for this and left in `agents/`: **`seatsim.py`** (both seat orders per
opponent, actual-seat and post-halving effective 命, hp gap, turn count),
**`boardsearch.py`** and **`mustwin.py`** (seat-aware random board search). seatsim paid
for itself many times; the random searchers did not — **ordering dominates selection**
in this deck and random permutations lost to a hand-built chain every time (R13: best
random board avg -7.0 / worst -25 vs the hand-built chain from the identical card set).

## Fog of war

Four of eleven losses were straight fog misses (sim on last-round board said win):

| round | sim (my actual seat) | actual | what changed |
|---|---|---|---|
| R3 | +4.9 avg, 6/7 | **-7** | 龙瑶 added 云剑·探云+1 and 地灵丹 |
| R7 | +12.7, 7/7 | **-12** | mirror 林小月 added 青铜猫 + a 2nd 飞牙剑 |
| R9 | +17.9, 7/7 | **-17** | mirror added 灵猫乱剑 |
| R16 | -24 -> -12 expected vs 龙瑶 | **-25 (odd)** | 龙瑶 upgraded 云剑·游龙+1 / 云剑·闪风+1 — one point either side of the parity line |

R16 is the instructive one: the board was chosen *because* every loss came out even,
and a single fog upgrade moved one of them from 24 to 25 and cost 13 命 — the
elimination margin. Under fog, parity-steering is fragile; aim at the middle of an even
band, not its edge.

## Matchup notes

- **杜伶鸳 (水灵 sustain: 水灵·腾浪 x3 + 水灵·潜遁+1 + 回响阵纹+1)** beat me in every
  meeting after R8 and killed me. 潜遁 puts **水灵·潜 (my damage x0.6)** on every
  exchange while 腾浪 raises her max HP each cycle, so the HP gap *grows with time*:
  hp -113 at t18 became -302 at t27 on a more defensive board. Against this archetype
  **more defense is actively worse** — the only lever that shrank the gap was more
  damage (and a faster end). Nothing in the intent deck without 剑意激荡 beats her.
- **陆剑心 (this game: 御空剑阵 x3 + 水月剑阵+1 + 镜花剑阵+1 + 聚灵心法+1)** is the
  playbook's "pierce doesn't help" case, confirmed: 灵气灌注 and 轮指连音 (3 hits, all
  [无视防御]) both failed to move the number. What DID beat him was **玄晶护心镜
  (防+20 + 2 [护体]) plus the second seat**, turning the fight into a 64-turn cap I won
  on HP (+67 ... +111). Rule: against a pure wall you cannot burst, don't race — out-stall
  it and win the turn cap.
- **The painter mirror (pid7 林小月)** ran the same build one tier behind and was beaten
  3-2 (R2, R13, R15 wins; R7, R9 losses). He drew **剑意激荡 at R14** and I never did —
  a clean illustration of that one card's worth: he went from losing to me by 19 to
  needing 陆剑心 to finish him.

## Bugs / suspicious behaviour (reported, not fixed)

1. **`break <ids>` preference lists are all-or-nothing and silently override the default
   scorer.** If none of the *good* offered fates is in the list but a *bad* one is
   (further down), the driver takes the bad one. This cost 14 命 at the 境5 gate
   (云巅雷劫 was 9th in my list; 善假于物 and 机缘造化 were not in the list at all and
   were both better). There is no way to express "prefer these, otherwise fall back to
   the scorer". Suggested fix: treat the list as a whitelist with a scorer fallback, or
   print the offer and pause before resolving.
2. **The 天命 offer log prints the post-increment realm on a double break** (open since
   game6). At R6 both gates logged `@realm3`, so the 境2 slot's 灵剑传承 was displayed
   with the 境3 text (抽2张名字含"灵剑"的牌) and delivered **1** card. Not merely
   cosmetic: the displayed magnitude is the input to the pick.
3. **`resolve()` prefix-matching can eat a levelled keeper.** `roll 巨鲲灵剑` matched
   **巨鲲灵剑+1** once the lv1 copy had left the hand, rolling away a merged card (R10).
   `nm()` renders levels as a `+N` suffix, so a bare name is a legal prefix of every
   level of that card. Suggest: an exact-name argument should prefer the lowest level,
   or refuse when levels are ambiguous (same family as the game2 roll-on-board-card trap).
4. **"Compression" cannot shorten the cycle in this driver.** `play.py sim` and
   `oracle_sim._pad_slots` both pad the board to `unlocked_slots`, and the engine treats
   `len(usedCards)` as the cycle — so a 5-card board at R14 still runs an 8-turn cycle
   with three 普通攻击 turns (each of which *spends the whole 剑意 bank*). The only real
   cycle-shorteners are `[消耗]` (画龙点睛 locks its slot) and `[再次行动]` (御空剑阵).
   Measured at R12: the 8-card board beat the 6-card compressed chain by ~16 命 at 境4.
   The playbook's "cycle compression" wording reads as if a short board cycles faster;
   it does not.
5. **好奇心's guaranteed 猫薄荷 is conditional.** `curiosity_surprise` forces the catnip
   on the LAST (9th) trigger **only if no catnip has been granted yet**
   (`st.get("catnip")`). I rolled one naturally on trigger 3, so triggers 4-9 were pure
   random and returned no second catnip. The playbook's "guaranteed 猫薄荷 on the 9th"
   needs that caveat.
6. **好奇心's 10% 法宝/灵宠 branch produced two excellent cards** (玄晶护心镜: 防+20 +
   2 [护体] — it won the 陆剑心 matchup; 九冥镇魔印: clear the opponent's 防/护体 and
   deal 30). The branch is phase-gated (`ph <= p.phase`), so farming it at 境5 is
   materially better than at 境3-4. I rolled 九冥镇魔印 away while chain-farming — a
   real loss. **Stop chaining the moment a 法宝 appears.**
7. **The no-bye rule worked exactly as documented** at R11 and R16: I was the non-odd
   side of someone else's extra battle, lost both, and paid nothing. But `show`'s
   LAST BATTLE line only reports the *last* battle involving me, so in a round with two
   of my battles (R16) it hides the one that actually cost 命 — easy to misread.
8. `pool` counts stayed accurate and drove every roll choice; deck thinning worked as
   documented (剑挡 8->1, 飞牙剑 7->0, 巨虎灵剑 7->0, pool 407 -> 225 by R15).

## Playbook numbers measured this game

- **Seat value, mirror matchup (R10):** -19 first / +22 second on an identical board
  (+/-41 命). Second seat was better in 6 of 7 late rounds.
- **画龙点睛+1 (4 stacks):** board average -8.2 -> +6.2 in one round; the practical
  stand-in for 剑意激荡 when the multiplier never arrives.
- **Parity steering:** 11 to 13 命 per round from a one-slot change that moved the HP
  gap across an even/odd band boundary (R15, R16).
- **Roll productivity at 境5:** ~45 rolls R13-R17 produced 御空剑阵 x2, 飞灵闪影剑 x2,
  画龙点睛 x2, 连环剑阵 x1, 轮指连音, 万邪入体咒 — and **zero** 剑意激荡 (6/225 ~ 2.7%
  per roll; expected ~1.2 copies, so drawing zero is a ~30% outcome). The endgame plan
  should not be single-card dependent.
- **`触类旁通` / `以画入道` are the best digs available**: 触类旁通 is charge-neutral
  (+1 charge) and draws from the much smaller *sidejob* pool; 以画入道 draws a sect card
  **of your current phase** (a 境5 card at 境5). Roll these on sight.
- **万邪入体咒** (2 [内伤] + 2 [破绽] + 1 [虚弱], a sidejob card) placed immediately
  before the payoff is worth about +25 命 of margin: 破绽 puts x1.4 on the whole 灵猫乱剑
  burst. At slot 1 it is worth -30 (a wasted opening turn). Placement is everything.
