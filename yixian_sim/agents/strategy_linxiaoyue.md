# 林小月 画师·剑意 — General Strategy

Compiled 2026-09-04 from the user's annotations across games 1–5
(`replay files/gameN/review.md`) plus their original build guide. This is the
BINDING playbook: where a sim number and this document disagree, this document
wins. Numbers marked *(measured)* are agent measurements the user has not
contradicted.

---

## 1. The core idea

Sword intent (剑意): every stack gives +1 ATK, and a card's stacks are only
exhausted **after that card finishes ALL of its attacks**. So:

- Non-attacking generators (剑挡, 凝意诀, 御空剑阵…) bank stacks for free.
- A multi-hit payoff cashes the whole bank on EVERY hit — 灵猫乱剑 at lv2
  attacks 6 times, so banked intent does ×6 damage. Plus +1 attack per card
  kept in hand (max +3): always hold ≥3 cards once it's fielded. The 3rd held
  card alone is worth ~9.5 命 of margin *(measured)*.
- 飞牙剑 is special: it benefits from intent while keeping the bank — but
  per the engine (combat_rules.md) the mechanic is consume-then-REFUND, gated
  on actually dealing HP damage ([击伤]): a 飞牙剑 that is fully blocked by 防
  refunds nothing and the whole bank is lost. It belongs BETWEEN the
  generators and the payoff, and never into an expected block turn.

The whole game is one arc: build a phase-1 core that wins the early rounds,
convert economy into 灵猫乱剑 + upgrades, and end on a compressed pure-intent
chain that kills before the opponent's plan comes online.

## 1.5 Read the battle, not the verdict (user directive, 2026-09-05)

Do not shop boards by asking the Oracle "does this win?" over and over. For any
matchup that matters — a must-win round, a wall you can't crack, a seat-order
question — **trace the battle turn by turn by hand**: my card this turn, their
card, qi in/out, intent banked/spent, DEF up/gone, HP after each exchange.
`agents/combat_rules.md` holds the combat rules (distilled from yisim). The
trace tells you WHAT is failing — dying one turn before the payoff, feeding
intent into a block turn, a qi gap — and therefore what the better board IS.
The seat question and cycle-length questions are decided this way per matchup,
not by blanket rules.

**Cycle-length correction (game7 engine finding).** The battle cycle is ALWAYS
the full unlocked-slot count: unfielded slots become 普通攻击 turns — real
attacks that SPEND the whole 剑意 bank. So "cutting dead cards" does not
shorten the cycle; it swaps them for bank-burning normal attacks (at R12 the
8-card board beat the 6-card chain by ~16 命). True compression comes only
from [消耗] cards that remove their slot (画龙点睛) and [再次行动] chains
(御空剑阵, 运笔如飞). Judge every slot as "is this card better than a
普通攻击 here?", not "can I delete it?". (Game6's ±48 compression numbers were
an artifact of unpadded test fixtures — superseded.)

## 2. Board construction principles

**Count the tempo, not just the totals.** Compare boards by damage/defense *per
turn over the cycle*, including qi costs. Game5 R1: 护身灵气·巨虎灵剑·骤风剑 =
5 def + 16 atk over 3 turns BEATS 剑挡·骤风剑·巨虎灵剑 = 4 def + 20 atk over 4
turns, because 巨虎灵剑 costs 1 qi and with no qi generator that's a wasted
turn. Every board must pass the **qi budget check: qi generated ≥ qi consumed**
(game3 R4 lost to a 3-generated/4-spent board).

**Ordering rules:**
- Sword-intent bonus goes to the card AFTER the generator — make sure that's a
  real attacker (game5 R2: 护身灵气·研墨·剑挡·震雷剑, so 震雷剑 gets the bonus,
  not 研墨).
- 灵气灌注's [无视防御] rider lands on the NEXT card — place it immediately
  before 飞牙剑 (or before the one huge hit you need to pierce a wall), never
  wasted on 剑劈.
- 飞牙剑 sits between generators and multi-hit payoffs.
- Front-load: battles run ~9–13 turns ≈ only ~5–6 of your plays. Slots 6–8
  often never fire; a key card there is a blank.

**Know your kill cycle.** If one cycle can't kill and two full cycles is too
slow, use the tools below to land the kill on the "1.5th" cycle:
- **Reverse board**: put the payoff BEFORE the generators, so the second pass
  arrives at the payoff with a full bank (game5 R3 concept).
- **Stall cards**: a non-attacking filler (护身灵气) mid-board dodges the
  opponent's block turns.
- **Empty front slot**: plays 普通攻击 (3 atk) and delays the combo one turn.
- **Skip the qi card**: spending a turn gaining 1 qi is a free "virtual card" —
  extends the board beyond 8 slots and beats one-time blocks (地灵丹/叶盾花).
- **"Faster board" ≠ fewer slots** (corrected after game7 — see §1.5): the
  cycle is always unlocked-slots long, unfielded slots fight as bank-burning
  普通攻击. What made game5's late boards fast was the QUALITY of the chain
  (画龙点睛's [消耗] shortening the cycle, upgrades, no bank-wasting attacks
  mid-chain), not the slot count. Speed comes from [消耗], [再次行动], and
  making sure no attack fires before the bank is multiplied.

**Speed and seating.** Higher 修为 acts first; ties are coin flips — never sit
on a tie you need to win (game4 R10: absorbing one filler card guaranteed first
move and flipped a loss). **Going first is better in ~99% of cases** (user
ruling): if a matchup seems to favor moving second, go first anyway and STALL
one turn — that is effectively going second, with the choice kept in your
hands. Leaving trailing slots empty to keep 修为 above the opponent is often
right (game4 R6).

## 3. The game, phase by phase

**Round 1–2 (境1).** Play a merely-playable board; don't chase perfection.
When behind, favor attack over defense — it closes the HP difference (game5
R2: 轻剑 over 护身灵气 with a weak hand). Rolling in R1 is fine (user ruling):
roll junk whose combo partner is missing (云剑·飞刺 without 探云) — the ONE
rule is **don't roll for 好奇心**: never spend the last charge just to fish a
trigger; curiosity triggers are banked for when they're worth something.

**Phase 1 target (stay 境1 until ~R5–6):**

    剑劈 lv3 · 剑挡 lv3 · 灵气灌注 lv2 · 飞牙剑 lv2 ×2 · 震雷剑 lv2
    …plus one banked 猫薄荷.

- 剑劈/剑挡 are the forever-cards: push to lv3. If spare rolls can also reach
  震雷剑 lv3, take it (game5 R6) — but lv2 is enough for 灵气灌注/飞牙剑/震雷剑.
- Only TWO 飞牙剑 copies are ever needed; a third copy means merge two lv2s
  into a lv3.
- Never roll 剑挡. Roll 骤风剑 once 震雷剑 + a qi card exist (never merge it —
  it's fodder). Roll spare copies of the lv2-capped cards to dig for the lv3
  targets, THEN stop and save (game5 R6: once 剑劈+2 was reachable, the
  remaining fodder waits for phase 5).

**Phases 2–3 (R6–R8ish).** Breakthrough when the core is assembled. 天命 rule
(user ruling + top-player corpus, 2026-09-15): **cultivation comes first.
猫爪 and 猫魂庇佑 are FALLBACK picks — take them only when no offered fate
gives cultivation/cards** (top players skip 猫爪 in 63/83 games and 猫魂庇佑
in 81/83). The premium picks: **剑韵修炼 (battle-start 剑意 — it STACKS, take
it again on later gates), 顿悟, 善假于物, 云巅雷劫/感悟丛生** (1 card = 1
cult; 2 cards = 2). 灵猫乱剑 at 境4 is always taken. Hoard rolls — spend
nothing you don't have to. Keep 凝意诀 and 云舞诀 when dealt. 三峰剑 can
replace 震雷剑 if found in phase 3. Absorb 逗猫棒 at end of round (+1 roll).

**Phase 4 break (~R8–9).** The standard line: merge the spare 飞牙剑, absorb
the leftovers (灵气灌注 spare, 灵宠认主, 震雷剑), break to 境4, ALWAYS pick
灵猫乱剑. Standard phase-4 board: 剑劈 · 剑挡 · (灵气灌注) · 飞牙剑 · 灵猫乱剑
— about 5–6 slots, empty front is fine. Keep 猫薄荷 and a payoff in hand.

**猫薄荷 discipline.** Card text: upgrades ONE random lv1 card in your hand or
fielded board, **preferring names containing 猫**. So the guarantee works in
two tiers: while any other 猫-named lv1 exists, clear THOSE first (non-猫 lv1s
can't be hit yet); once no 猫-named lv1 remains, it rolls uniformly over ALL
lv1s — then clear every non-core lv1 too (only the intended target and
剑意激荡 are worth shielding; even 云舞诀/画龙点睛 are expendable, game5 R13).
If the current turn doesn't need it, hold it. Extra catnips from 好奇心 are
farmed the same way: clear, then eat. Target priority (user ruling,
situational): **灵猫乱剑 > 剑意激荡 > 御空剑阵 = 连环剑阵 = 凝意诀 = 云舞诀**.

**好奇心 economy.** Triggers only at exactly 1 charge and refunds +1, so
triggers are effectively free and can be chain-farmed; 9 lifetime uses. Bank
them for phase 5 where the 10% 法宝/灵宠 branch and the exchanged charges are
worth most. 小鱼干 [炼化] = +2 命 — at low destiny that's a life-or-death
absorb *(measured)*.

**Phase 4 → 5: do not roll.** Phase 4 has little we need; every charge saved
is a phase-5 card. It is OK to lose a round while setting up (games 4–5 both
validated the hoard: 20+ charges at the 境5 break buys the entire endgame).
The 境5 break is normally R12; **R11 is possible when enough cultivation
fates were picked** (user ruling — top players hit R11 in 58/83 games by
absorbing 2–4 spare cards EVERY round from R7 on, including the phase-1 core
itself once it leaves the board; nothing off the final chain is sentimental).
Before the 境5 break: merge 飞牙剑 down to ONE copy, roll away 灵气灌注 spares
and cards this game will never play (震雷剑, 万法归灵剑, 反身剑 — game5 R12:
"use the last rolls, those are cards we will not play"), and NEVER roll
凝意诀 / 云舞诀 / 连环剑阵.

**Phase 5 endgame: pure sword intent.** 万法归灵剑 is banned on this
character. Reference end board:

    凝意诀+2 · 御空剑阵+2 · 剑挡+2 · 连环剑阵 · 剑意激荡+1 · 连环剑阵 ·
    运笔如飞+2 · 剑意激荡+1 · 灵猫乱剑+1

Key cards (never roll/absorb without cause): 剑劈, 剑挡, 凝意诀, 御空剑阵,
连环剑阵, 剑意激荡, 运笔如飞, 画龙点睛, 灵猫乱剑. 连环剑阵+御空剑阵 together
give big defense while the bank builds (御空剑阵 has chase — effectively free).
飞灵闪影剑 / 流云乱剑 at MAX level beat 灵猫乱剑 — keep them when not under
pressure. With 剑韵修炼 (start with 2 intent), open with 云舞诀, not 剑劈.
画龙点睛 upgrades the NEXT card — e.g. lv3 灵气灌注 to pay 巨鲲灵剑's cost
(game5 R12). Its 道韵 valuation is UNCHANGED — 自在随心 still beats it at the
道韵 offer; but if the card reaches you in phase 5, keep and use it.

Two user rulings from the top-player corpus (2026-09-15):

- **Field BOTH 剑意激荡 copies unmerged when more damage is needed** (very
  common at top level — two ×1.8 procs per cycle beat one ×2.1; merge to +2
  when the lv3 threshold is affordable). Top players run 激荡×2 in 32 of 75
  final boards.
- **When 飞灵闪影剑 reaches +2, it can REPLACE 灵猫乱剑 as the finisher — and
  灵猫乱剑 itself becomes absorb fodder — but only if you need to** (e.g. the
  修为 matters or the hand-hold constraint hurts). Its 6 hits all carry the
  bank and each 击伤 refunds qi; the ≥3-hand rule dies with the swap.

**The second-cycle gambit (advanced, game5 R12).** Against a strong defensive
board you can't burst in one cycle: plan the kill on cycle two — 巨鲲灵剑 to
cycle faster (paid via 画龙点睛-upgraded 灵气灌注 + 飞牙剑), then choose the
flex slot by win odds: 镜花剑阵 pushes damage if you think you win, 慈念曲
saves 命 if you think you lose (慈念曲 reduces the loser's 命 damage 4/6/8).

## 4. Economy details

- **Deck thinning is deterministic**: a sect-card roll deletes 3 copies from
  the pool, a sidejob roll deletes 2. Check `pool` counts to pick WHICH junk to
  roll when options are equal — but deletion quality never overrides strategy.
- **[置换] cards are free value**: 练笔 (+2 charges + a draw), 以画入道 (sect
  card of your phase, replaces the draw), 触类旁通 (+1 charge + sidejob card),
  妙笔生花 (an upgraded card). Hunt and roll them from R7, not R13.
- **Merging gives +1 修为** but eats a fodder copy — don't merge what you'd
  rather roll (骤风剑), and don't merge to lv3 while the core is missing cards
  (剑挡 lv3 can wait; game3 R4).
- **Stop absorbing at 55 修为** (境5 gate; MAX realm) except for [炼化] value
  (小鱼干 → 命, 逗猫棒 → charge) and the hand-16 cap.

## 5. Destiny management (losing well)

- 猫魂庇佑 halves EVEN 命 losses only (card text). When a loss is unavoidable,
  steer the final HP gap so the destiny formula lands on an even number — it's
  routinely worth 15 命 late. Score boards on post-halving 命, not HP margin.
- At 3 players the pairing avoids repeats → the next opponent is predictable:
  tailor the board to them (their LAST known board — the current one is hidden).
- No byes exist: the odd player out fights a random opponent (they alone risk
  命). Never count on a free round.

## 6. Matchups

- **慕虎 / earth-wall decks** are this build's worst matchup. Stay on the
  sword-intent build (user ruling — do NOT chase the sword-formation deck for
  now; whether it's better depends on both sides' cards and is a later lesson).
  What helps within intent: never absorb your last [无视防御] card
  (灵气灌注/云剑·猫爪/云剑·无妄), and a one-huge-hit 无视防御 line (灵气灌注
  immediately before the bomb) cracks walls.
- Fog of war is real: sims face LAST-round boards; decisive rounds can be lost
  to a card swap you couldn't see. Prefer robust boards over perfect counters
  in must-win rounds.

## Game7 additions (engine-verified)

- **画龙点睛+1 is the practical stand-in when 剑意激荡 never shows** (~30% of
  games it won't, even with a full roll bank). Placement rule: keep the number
  of UPGRADABLE cards between 画龙点睛 and the payoff ≤ stacks−1 so the last
  stack lands on 灵猫乱剑 (lv3 cards are free passes — no stack spent).
- **万邪入体咒 immediately before the payoff ≈ +25 命** (破绽 = ×1.4 on the
  whole burst); the same card at slot 1 is ≈ −30. Debuffs are payoff riders,
  not openers.
- **陆剑心-type 水月+镜花 engines can be out-STALLED**: 玄晶护心镜-class
  防+护体 plus the later seat won the 64-turn cap by +67…+111 HP where pierce
  did nothing. A third answer besides "kill faster" and "lose even".
- **杜伶鸳-type 水灵 decks (潜遁 ×0.6 damage + growing max HP) cannot be
  beaten without an intent multiplier** — and MORE defense makes the gap
  worse. Don't tank; race or dodge.
- **Fate gates: `peek` before every `break`.** Offers are drawn inside the
  break, so preview them, write a COMPLETE ranking of what's actually shown,
  then commit — two of game7's three decisive losses were blind-pick failures
  (云巅雷劫's 境5 version costs −14 命 for its 5 cards; 善假于物 was free on
  the same screen).
- Once 灵猫乱剑 is fielded, absorbing the hand down to exactly 3 is free 修为
  (the bonus caps at +3) — a zero-cost seat-dial nudge.
