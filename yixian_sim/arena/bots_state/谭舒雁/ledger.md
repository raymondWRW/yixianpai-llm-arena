# 谭舒雁 — game ledger (append-only archive)

==== LEDGER ENTRY · Game 13 ====
game27 R17 (谭舒雁/pid1, 命理师7). vs 小布(pid3, 崩拳/气势 burst). 命63, 境5, 修为91.
DISCOVERY (major): 厄劫缠身 [开局] downgrades the opponent's SAME-SLOT card. Two 厄劫缠身 = downgrade BOTH of a burst deck's key cards. vs 小布 placing them at the slots aligned to 磅礴之势 and 崩拳·惊触 cut their 45dmg finisher to 27 and follow-up 18->11. That flipped a 0% loss into a 100% win.
Final board: [命运轮回, 天星·牵引, 血光之灾+1, 血光之灾, 厄劫缠身, 厄劫缠身, 梅开二度, 杯弓蛇影]
sim_matchup vs pid3: 100% both seats vs real board; 100% going-first vs +1 upgrade. (going-second vs +1 = 0%, near-miss, but I act first 修为91>79.)
Board is a 内伤 clock: 2x血光(4 opening) + 厄劫x2 + 杯弓蛇影 immediate-tick burst doubled by 梅开二度.
NOTE: 众星拱月 was on board before but REPLACED by a 2nd 厄劫 — the double downgrade > star power here.
Exchanges spent: ~11 hunting Build-B pieces (逆施/顺应/金蝉) which never came; the win came from a natural 2nd 厄劫 draw. LESSON: don't force a build switch late; check if a duplicate key card (厄劫/血光) already solves it.

==== LEDGER ENTRY · Game 13 ====
## Game 14 (the reviewed game) — 谭舒雁/pid1, 命理师(7)
RESULT: **1st place, WINNER, final 命 63**. Background: 4-player lobby; pid0 牧逸风 (云剑, 修为87), pid2 吾行之 (水灵, 修为57), pid3 小布 (崩拳/气势, 修为100). I outlasted all; pid3 finished at 命1 (I beat them R19 for -3), pid0 & pid2 hit 命0 earlier.

SIDEJOB: 命理师 (7) — correct, only pool with the 内伤/星 engine.
FATES (境2→境5): 勤学苦练, 星蚀, 休养生息, 观星, 斩断俗尘. 观星 (+1星力) good for star; rest mostly economy/defensive. 勤学苦练 drew several free cards over the game (helped).

FINAL BOARD (R20, 16 rolls' worth of hunting converged on a pure 内伤 CLOCK):
[命运轮回, 天星·牵引, 血光之灾+1, 血光之灾, 厄劫缠身, 厄劫缠身, 梅开二度, 杯弓蛇影]
W/L: R1 L(pid2) R2 W(pid0) R3 W(pid2) R4 L(pid0) R5 W(pid2) R6 L(pid0) R7 L(pid2) R8 L(pid3) R9 W(pid0) R10 W(pid2) R11 W(pid3) R12 W(pid0) R13 L(pid3) R14 W(pid0) R15 W(pid3) R16 W(pid0) R17 W(pid3) R17 W(pid0) R18 W(pid3) R19 W(pid3) R20 W(pid3).
The R1-R13 phase was a weak 雷/星 hybrid that lost the 命 race (dropped to 命63 by R13); the R14-R20 phase was the finished 内伤 clock that won 11 of the last 12.

PER-RIVAL CAUSE (from final-board sims + real logs):
- vs pid0 云剑 (final board 聚灵心法+1/天罡聚力阵/飞灵闪影剑+1/巨鹏灵剑+1/白鹭灵剑/巨鲸灵剑+1/巨鲲灵剑/形意剑+1): MY final board wins 100% going FIRST (~7t) but 0% going SECOND (~7t). Pure seat race — 剑意 ramp (白鹭 25, 巨鹏 14, 巨鲸 16-22, 形意 13) outspeeds my clock when he moves first. I act first (修为 111 > 87). **FIX (search_board-verified): reorder to put a leveled 厄劫缠身 in the 天星·牵引-triggered slot AND 梅开二度 right before 杯弓蛇影 → board [命运轮回,天星·牵引,厄劫缠身+2,血光之灾,厄劫缠身,血光之灾+1,梅开二度,杯弓蛇影] wins 100%/100%.** Slot order was worth an entire seat.
- vs pid3 崩拳 (崩天步+1/崩拳·寸劲/崩拳·惊触+1/崩拳·连崩+1/磅礴之势+1): 100%/100% base AND vs +1 (5-8 reps). 厄劫缠身 [开局] DOWNGRADES his 磅礴之势 and 崩拳·惊触 (dropped his end-game finisher ~45->27). His sustained ~16-17/turn (崩拳+气势+身法) is real but the clock wins the 6-7t race.
- vs pid2 水灵 (水灵印+2/波澜+1/泉涌+1/潜遁/汹涌+2/八门金锁阵/天罡聚力阵/木灵·复苏): 100%/100% base AND vs +1. Water summons ramp but my clock is faster; also his 修为 57 is lowest (I always act first).

TOP DISCOVERY (BIG, cross-game): the 内伤 clock's damage comes almost ENTIRELY from the [开局] STACKS and the 杯弓蛇影 immediate-tick — NOT from any played card's attack. card_stats(R19): every board card reads "0 dmg" except Snake in Reflection (杯弓蛇影) = 30 dmg. The clock: base 3 stacks (from 厄劫x2 [开局] + 血光+1 [开局]) + 血光+1 played (2) + 厄劫 played (4) + 天星·牵引 re-triggering 2 开局 (2) = ~11 by turn 3; 梅开二度→杯弓蛇影 doubles (adds 2 stacks + fires the WHOLE clock twice). Reaches 16-18 内伤 by turn 6-7 → opponent loses 16-18 HP at their OWN turn start, IGNORING DEF (verified: do_internal_injury calls reduce_idx_hp, no def check). Kills through any defense.
EVIDENCE: 3 sim battles read turn-by-turn (R17, R19, simulated pid0-second-seat) + card_stats.

MECHANIC VERIFIED (engine): 命运轮回 = fate_reincarnates_stacks; at the card-index advance, if next_card_index===3||4 (0-idx = slots 4&5 1-indexed) it DECREMENTS a stack, calls do_opening(slot), advances — i.e. SKIPS playing that slot but FIRES its [开局], for 4 cycles. So ANY [开局] card (血光之灾/厄劫缠身/吉运初显) parked in slots 4-5 fires FREE every cycle. That is THE slot-order rule.

ECONOMY AUDIT: R8 spent **20 rolls** junk-hunting a 雷 build → wasted the whole bank AND lost R8. R13 4 rolls, R15 9, R17 11, R19 6 — these targeted rolls (血光之灾+1, 厄劫缠身, 梅开二度, 命运轮回) built the winning board. Bank hit the 25 cap R20. LESSON holds: name the target before rolling; don't roll with no plan; but DO roll hard once the engine target is known.

SURPRISE: I nearly lost the game on a SEAT coin-flip vs pid0. My board won 100%-first/0%-second — the "same" board is a different card depending on who moves first. In a race deck, SLOT ORDER that makes you win from BOTH seats is worth more than a level upgrade.
SURPRISE 2: 修为 (seat) is a real weapon — I finished at 修为 111 (highest) so I moved first all game; that alone converted the pid0 matchup.

==== LEDGER ENTRY · Game 14 ====
## Game 15 (reviewed) — 谭舒雁/pid1, 命理师(7). RESULT: **NOT first — 命 0, eliminated at R16.** Lobby: pid0 牧逸风 (云剑, 修为94→ final 94), pid3 小布 (崩拳/气势, 修为93), pid2 吾行之 (金灵/五行, 修为72). I finished 境5 修为87, maxHP105.

FATES (境2→境5): 勤学苦练, 储纳灵气, 顿悟, 观星, 斩断俗尘 (same as g14). Mostly economy; 观星 = +1星力 (irrelevant to 内伤 clock). I never re-rolled into a combat fate.

FINAL BOARD (R16, the WEAK HYBRID that lost):
[落花有意, 血光之灾+1, 流水无情+1, 杯弓蛇影+2, 斩草除根, 星弈·挡+1, 海底捞月, 飞星刺]
W/L: R1 W(pid2) R2 W(pid3) R3 W(pid0) R4 L(pid3) R5 L(pid2) R6 L(pid3) R7 L(pid2) R8 W(pid3) R9 W(pid2) R10 L(pid0) R11 W(pid2) R12 W(pid3) R13 L(pid2) R14 L(pid0) R15 W(pid3) R16 L(pid0)+L(pid3) → 命0.
Pattern: I beat pid2 (金灵/五行) cleanly all game; I was a coin-flip vs pid3; I LOST every late-round fight vs pid0 云剑 (R10,R14,R16) once their ramp came online.

PER-RIVAL CAUSE (from battle logs + sims):
- vs pid0 牧逸风 云剑 (聚灵心法+1 qi engine → 辟邪阵纹 +10def/+3护体 → 巨鹏12+巨虎16+巨鲲13+白鹭18 chases): MY CLOCK WAS TOO WEAK. R16 log: my total 内伤 only reached 8 by turn 10; pid0 dealt 100+ dmg and killed me t10. R14 same: 5 内伤 by t9, died t9. The 云剑 deck's 聚灵心法 generates qi so they chain 巨鹏→巨虎 every turn (28 dmg burst).
- vs pid3 小布 崩拳/气势: close; I won base boards but lost to burst when my clock was diluted with non-clock cards (斩草除根/星弈·挡/海底捞月/飞星刺 waste slots).
- vs pid2 吾行之 金灵: I beat this all game (lowest 修为 72, and 金灵 ramp slower than my clock).

TOP DISCOVERY (cross-game, CONFIRMED via sim this review): the fix vs pid0 云剑 is adding **厄劫缠身 + 天星·御心** to the 内伤 clock — a DOWNGRADE engine:
  BOARD (search_board-verified 100%/100% both seats vs pid0 base): [流水无情+1, 天星·牵引, 厄劫缠身, 天星·御心, 杯弓蛇影+2, 血光之灾, 杯弓蛇影, 血光之灾+1]
  - 天星·御心 = `retrigger_next_opening(-1,1,2)`: fires the PREVIOUS card's [开局] TWICE. Put it right AFTER 厄劫缠身 → DOUBLE downgrade + double 内伤 stacks. [src: card_actions.js:8966-8971]
  - 厄劫缠身 [开局] DOWNGRADES pid0's SAME-SLOT card. In the win-log it downgraded his 聚灵心法 (qi engine → 0 qi) AND his 灵剑 chain, choking the ramp AND adding 内伤.
  - Even ONE lv1 厄劫缠身 + 天星·御心 wins 100%/100% vs pid0's real board. WITHOUT these two, the clock wins only going FIRST vs pid0 (100%/0%) — a pure coin-flip on 修为, and pid0 out-修为'd me (94 vs 87), so I was doomed to lose.
  - vs pid3, just swapping my dead slot 斩草除根 → 黄雀在后 flipped 0%/0% → 100%/100%.
EVIDENCE: search_board trace (oracle pre-filter + yisim verdict), 2 full-log sims read turn-by-turn, matrix cross-checks.

ECONOMY AUDIT (this was the real leak): I rolled ~R13 6 / R14 8 / R15 6 / R16 6 = 26 rolls, but with the WRONG NAMED TARGETS. R14 I rolled hunting 命运轮回, R16 I rolled hunting 星弈·断/天元心法 — but the winning pieces were **厄劫缠身 and 天星·御心**, which I never once named. I also ABSORBED a 天星·牵引 in R16 (it was the R10 draw) — that was a real key piece, wasted. R8 6 rolls junk, R11 6 rolls junk.
NAMED ROLL TARGETS for next game (priority order): 厄劫缠身 > 天星·御心 > 血光之灾 > 杯弓蛇影 > 命运轮回 > 梅开二度 > 天星·牵引. NEVER absorb a clock piece for 修为 once ≥2 clock pieces are held.

SURPRISE: 修为/seat decided the whole lobby. pid0 云剑 out-realms me → they move first → their 巨鹏→巨虎 burst lands before my clock ticks → autoloss. So vs 云剑, 修为 (or the downgrade pieces that bypass the seat race) is MANDATORY, not optional.
SURPRISE 2: 天星·御心 (backward-trigger) is the cheap doubler — it only needs ONE 厄劫缠身, far easier to assemble than the old 命运轮回+梅开二度 combo. This is the new target package.

==== LEDGER ENTRY · Game 15 ====
# Game 30 (reviewed) — 谭舒雁/pid1, 命理师(7). RESULT: **NOT first — 命 0, eliminated ~R17.** Lobby: pid0 牧逸风 (云剑, 修为74), pid2 吾行之 (水灵, 修为76), pid3 小布 (崩拳兼命理, 修为81). I finished 境5 修为75, maxHP103.
W/L: R1 L(pid2) R2 L(pid0) R3 W(pid3) R4 W(pid0) R5 W(pid3) R6 L(pid0) R7 L(pid2) R8 L(pid3) R9 L(pid0) R10 L(pid3) R11 W(pid2) R12 L(pid3) R13 L(pid2) R14 W(pid0) R15 L(pid2). Net downhill after R5.

FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 雪羽清风, 雁影化身, 斩断俗尘 (same shuffle as g29). None are combat-relevant to the clock; 飞鸿踏雪 is a chi/chase card. Did not help.

FINAL BOARD (R15, the DUD): [落花有意, 梅开二度, 流水无情+1, 天星·牵引, 诸事不宜, 天星·御心, 吉运初显, 天星·御心]
HAND: [黄雀在后, 梅开二度]. This board is 60% DEF/HP filler (诸事不宜/吉运初显/御心×2) with only ~2 内伤 sources (落花 1 + 流水 3-if-debuff). vs pid2 (105 HP) it topped out at 8 内伤 → LOST 8/8 both seats even to the "easy" rival. Verified: search over my ACTUAL held cards = 0%/0% vs pid2. THE LOSS WAS LOCKED BY DRAW FAILURE, not board order.

TOP DISCOVERY (g30, yisim-verified): **I held the ENTIRE support package (天星·牵引, 天星·御心×2, 梅开二度, 落花有意, 流水无情+1) but was missing the ONE load-bearing card: 厄劫缠身.** search_board(pool=7, start=my-held cards): swapping 诸事不宜 → 厄劫缠身+1 and putting a 天星·御心 right AFTER it flipped the board 0%/0% → 100%/100% both seats vs pid2, and 100%/100% vs pid0 and pid3 too. Win-log (full): 落花+流水 stack 4 内伤 t1-2; 天星·牵引 → 厄劫(+1) opening fires 5 内伤 TWICE (御心) = 14 内伤 by t5; clock deals 14/foe-turn-start → pid2 dead t9. 厄劫's opening ALSO downgraded pid2's 水灵·涛 finisher. FINAL RECIPE (minimal, from my own held cards): [落花有意, 流水无情+1, 天星·牵引, 梅开二度, 厄劫缠身, 天星·御心, 天星·御心, 吉运初显] — 100%/100% vs ALL THREE rivals. Only ONE 厄劫缠身 needed.

ECONOMY AUDIT (the real leak): ~57 rolls total (R6:9, R7:5, R9:5, R13:6, R14:6, R15:6 among them). I hit 天星·御心 (R10,R15) and 天星·牵引 (R15) but NEVER once drew 血光之灾 (境3, 8 copies) or 厄劫缠身 (境5, 6 copies) in the whole game. I also ABSORBED many junk cards (天谕·守, 天机·顺应, 星轨推衍, 御雷卦诀) for 修为 in R13-R15 instead of RE-ROLLING them — and I was already highest 修为, so those absorbs bought seat I didn't need and cost me draws I did need. Banked 0 exchanges at every round end R7-R15 → no saved budget for the R13+ hunt.

PER-RIVAL CAUSE: lost to everyone because the board had no clock. pid2 水灵 ramps to 14 force_of_water and hits 13-23/turn; my 8-内伤 dud couldn't race. pid0 云剑 剑意 ramp kills t10; pid3 崩拳 气势 burst kills t8.

SURPRISE: with 天星·御心 held, 厄劫缠身 alone is a ONE-CARD flip of the whole matchup. The support was worthless without it — I had 2×天星·御心 retriggering NOTHING (only def/hp openings). A retrigger engine with no [开局]-damage card is dead weight.

MECHANICS RE-VERIFIED THIS GAME: (1) 命运轮回 fires when next_card_index===3||4 (0-idx) = slots 4&5. [gamestate_full.js:3307] (2) 天星·御心 = retrigger PREVIOUS opening ×2 → put immediately AFTER 厄劫缠身/血光之灾. (3) 厄劫缠身 [开局] downgrade is restored post-battle (safe). (4) 内伤 ticks foe turn-start, ignores DEF (ruthless_water added 3 to a def-blocked target).

==== LEDGER ENTRY · Game 16 ====
## Game 33 (reviewed) — 谭舒雁/pid1, 命理师(7). RESULT: **命 0, eliminated R19.** Lobby: pid0 牧逸风 云剑/万法 (修为94, eventual winner), pid3 小布 崩拳/气势 (修为93), pid2 吾行之 金灵/五行 (修为72). I finished 境5 修为~87, maxHP~126.

W/L: R1 W(pid3) R2 L(pid0) R3 W(pid3) R4 L(pid2) R5 L(pid0) R6 L(pid3) R7 L(pid0) R8 L(pid3) R9 W(pid0) R10 L(pid3) R11 W(pid0) R12 W(pid2) R13 L(pid0) R14 L(pid0) R15 W(pid3) R16 L(pid0)+W(pid3) R17 W(pid3) R18 L(pid3) R19 L(pid0)→0. Losing record overall; the few wins were close.

FATES (境2→境5): 勤学苦练, 储纳灵气, 顿悟, 观星, 斩断俗尘. Same non-combat set as g14/g15. A/B sim with these fates ([1,2,3]) = NO flip vs pid3 (still a win) → CONFIRMED fates are combat-irrelevant for this kit.

*** ROOT CAUSE — BOARD CONSTRUCTION, NOT DRAW LUCK. ***
My fielded R16-R19 board (card_stats R19): [天星·牵引, 血光之灾+1, 天星·御心, 反震心法+1, 杯弓蛇影, 流水无情, 落花有意, 诸事不宜]. card_stats: EVERY slot = 0 dmg except 杯弓蛇影 (8-10 dmg). A 60%-defense dud. NO 厄劫缠身. The 天星·御心 retriggered only 血光之灾 (weak [开局]=1 内伤) — a retrigger pointing at a dud.
**THE FIX (search_board-verified, 5-rep sim_matchup): reconstruct the SAME held cards into a real clock → `[杯弓蛇影+2, 血光之灾+1, 落花有意, 天星·牵引, 天星·御心, 流水无情+1, 梅开二度, 五雷轰顶+1]` wins 100%-first/40%-second vs pid3's REAL final board (base).** And with the actual engine cards `[天星·牵引, 厄劫缠身+2, 天星·御心, 杯弓蛇影+2, 五雷轰顶+2, 血光之灾+1, 卜命, 梅开二度]` → **100%/100% (~6t), kills pid3 for 33命.** So the SAME lobby, same hands, was winnable with correct slot order + a named hunt for 厄劫缠身.

*** vs pid0 牧逸风 云剑/万法 — STRUCTURALLY UNBEATABLE AT THIS REALM. ***
Search over ALL careers (1-7, 380 evals) could NOT beat pid0's final board from any board I could build: best = 0%/0%. Verified with full_log: even my perfect 内伤 clock (11 内伤 by t7) dies to his **万法归灵剑 one-shot: 13 qi × 5 = ~65-70 dmg at t7**, while his 辟邪阵纹 (4 hexproof) blanks part of my 内伤 application. His 聚灵心法+百鸟+引气剑+点星 = 13-qi bank by t7 every game. My clock needs until t8-9 to reach lethal → he wins the race by 1-2 turns every time. This matches his notebook CP1-CP10 (万法 is his win-con, 谭舒雁 noted as "kill by t6-9"). *** LESSON: the 内伤 clock has a HARD SPEED CEILING ~t8; a 13-qi 万法 fires at t7. Cannot out-clock; must add BURST (五雷轰顶) to shorten MY kill to t5-6, or 反震 if he's multi-hit — neither was enough here. GOING FIRST is mandatory (already had 修为 lead) but insufficient vs pid0.***

ECONOMY AUDIT (the leak that mattered): rolls/round = 0,0,0,0,0,12(R6),0,12(R8),3(R9),0,9(R11),4(R12),6(R13),6(R14),6(R15),6(R16),0,0,18(R19). TOTAL ~82 rolls.
- OVER-rolled EARLY with NO target: R6 (12 rolls → got 落花有意 only, rest junk), R8 (12 rolls → junk: 藕断丝连/金鸡独立/御雷卦诀). Those 24 rolls went to a phase where my pool was 境1-3 generic cards — near-zero yield. **WASTED the entire early bank.**
- UNDER-targeted LATE: R13-R16 (6 each) and R19 (18) were spent BUT never once named 厄劫缠身 (境5, 6 copies). I drew 天星·御心 (R12), 天星·牵引 (R14,R16), 杯弓蛇影 (R12,R19), 血光之灾 (R11,R15), 流水无情 (R16,R19) — the whole SUPPORT suite — but NEVER 厄劫缠身 in the entire game. Same failure mode as g30.
- ABSORBED engine pieces: R16-R17 I absorbed into 修为 while already 修为-lead.
- pid3's economy (contrast): banked 3→24 through R8-R11, then DUMPED 17 (R15), 19 (R17), 16 (R18) hunting his named endgame (威震四方/崩拳·寸劲/磅礴之势+1) — textbook. Mine was backwards: dumped early on junk, banked/targeted late.

TOP DISCOVERY (cross-game, THIRD confirmation): **The single load-bearing card for the 内伤 clock is 厄劫缠身. Its [开局] applies 4/5/6 内伤 AND downgrades the SAME-SLOT enemy card — and with 天星·御心 placed IMMEDIATELY AFTER it the opening fires TWICE. One 厄劫缠身+天星·御心 = the whole matchup. Everything else (血光/落花/流水/牵引/梅开二度) is support.** g30 found this; g33 re-verified: ideal board [天星·牵引,厄劫缠身+2,天星·御心,...] = 100%/100% vs pid3 vs my real dud board = 0%.

MECHANICS RE-VERIFIED (g33 log evidence):
- 天星·牵引 (slot1) fired slot2 厄劫缠身's [开局] → 8 内伤 at t1 (log line "reduced OPP hp by 12... gained 1 internal_injury").
- 天星·御心 triggers the PREVIOUS card's [开局] ×2. Place it IMMEDIATELY AFTER 厄劫缠身/血光之灾.
- 厄劫缠身 [开局] downgrade (restored post-battle) also chokes qi engines (downgraded pid0's 聚灵心法 lv2→lv1).
- 内伤 ticks foe turn-start, ignores DEF.
- 五雷轰顶: 5× 30%-chance 8atk — great BURST to complement the clock (helped close pid3 from t5).

SURPRISE: (1) I lost R18 to pid3 by only -3命 (got him to 2 HP) — one 厄劫缠身 or one better slot order flips it. (2) pid0's 万法 nuke (~70) is unbeatable by clock at this realm — accept the loss, spend the round building for the OTHER matchups and minimize 命 loss. (3) 修为-lead alone does NOT beat 万法 — I was first and still died t7.

==== LEDGER ENTRY · Game 17 ====
# Game 35 (reviewed) — 谭舒雁/pid1, 命理师(7). RESULT: **1st PLACE — WINNER, final 命 1.** Lobby: pid0 牧逸风 云剑 (died), pid2 吾行之 五行/水灵 (died), pid3 小布 崩拳/气势 (runner-up, ended 21命 then lost final). I finished 境5 修为110, maxHP113.

W/L: R1 W(pid2) R2 L(pid0) R3 L(pid3) R4 L(pid2) R5 L(pid0) R6 L(pid3) R7 W(pid0) R8 W(pid2) R9 W(pid0) R10 L(pid3) R11 L(pid2) R12 L(pid3) R13 L(pid2) R14 W(pid3)+W(pid2) R15 L(pid3) R16 W(pid2) R17 W(pid3)+L(pid2) R18 L(pid2) R19 W(pid3) R20 W(pid3, FINAL). Won as the lowest-命 player by beating pid3 down the stretch; pid2 died to pid3 R17 (lost 24命) just before facing me.

FATES (境2→境5): 勤学苦练, 储纳灵气, 休养生息, 雁影化身, 观星. A/B sim with all 5 fates = NO change (still wins). CONFIRMED economy fates are combat-irrelevant for the 内伤 kit (4th confirmation: g30/g33/g35).

FINAL BOARD (R19-R20, fielded): [天星·牵引, 血光之灾+1, 天星·御心, 落花有意+1, 诸事不宜, 梅开二度, 杯弓蛇影+1, 流水无情] = 100% BOTH seats vs pid3 base AND +1 (5-10 reps yisim).

*** TOP DISCOVERY (g35, search_board + simulate verified) — THE pid2 FLIP. ***
My fielded board = **0%/0% vs pid2** (the water healer). Adding ONE **厄劫缠身** (境5) flips it:
`[天星·牵引, 厄劫缠身, 流水无情, 血光之灾+1, 天星·御心, 诸事不宜, 梅开二度, 杯弓蛇影+1]`
= **100% first / 100% second vs pid2 base, AND 100%/100% vs pid0, AND 100%/100% vs pid3 base (only weak spot: 0% second-seat vs pid3 FULLY +1, a non-real edge case).** This is a board that beats EVERYONE. search_board over pool 7 locked [厄劫/御心/牵引/杯弓/流水] found it at 71 evals.
KEY ORDER INSIGHT: 天星·御心 goes AFTER 血光之灾+1 (retrigger its 2-内伤 opening ×2), with 厄劫缠身 EARLY (its [开局] downgrades the enemy same-slot card + 4 内伤 as card effect). 牵引 FIRST triggers the 2 openings (厄劫+血光).
**Worst part: I DREW 厄劫缠身 at R20 (my very last hand) and ABSORBED it for +1修为 instead of fielding it. If I'd had it by R17, I beat pid2 both remaining fights (instead of losing R17/R18 by -2命 each). This is the 4th consecutive game g30/g33/g35 where 厄劫缠身 was THE missing lever.**

PER-RIVAL CAUSE:
- pid2 吾行之 (water healer, the WRECKER of my game): his 水灵·纳百川 (+maxHP per 水势) + 水灵·纳百川/五行天髓诀 chase-heal out-tanks my 内伤 clock; my clock reached only ~18 内伤 by t10 while he healed +22/+23 twice (R16/R17 logs). I beat him only 3/8 tries. FIX = 厄劫缠身 (above) → 100%.
- pid3 小布 (崩拳/气势 burst, FINAL OPPONENT): my clock + 杯弓蛇影 kills him t10-11. 杯弓蛇影+1 = 23 dmg INSTANT in R20 (triggers 内伤 immediately + 3 stacks). He has 43 体魄 (extra HP) but clock ignores it. 100% both seats.
- pid0 牧逸风 (云剑): died before the finals; my final board is 100%/100% vs his last board too.

ECONOMY AUDIT: rolls/round = R7:4, R9:17, R10:10, R11:3, R12:5, R13:6, R14:6, R15:6, R16:6, R17:4, R18:8, R19:0. ~75 rolls total.
- R9's 17 rolls = GOOD (no named target but landed the whole support suite: 御心/牵引/流水无情/落花有意).
- R10's 10 rolls = junk (rolled 天谕·攻/守, 众星拱月, 气贯长虹 — absorbed them).
- LATE MISS: from R17+ I had 12+ exchanges banking and NEVER rolled for 厄劫缠身 (境5, 6 copies). I drew it (R20) and absorbed it. CONTRAST pid2 banked to 22 and never dumped (his loss); pid3 dumped 17/19/16 late hunting his named endgame.
- Bank-at-end sequence: 3,6,9,12,15,18,17,20,6,0,1,0,0,0,0,0,2,0,6,12.

SURPRISE: (1) I won the lobby with a board that was 0% vs the water healer — because pid3 eliminated pid2 for me. The 内伤 clock is a SEAT-INDEPENDENT killer vs burst decks but HARD-LOSES to heal/tank decks. (2) 杯弓蛇影's "令对方[内伤]立刻生效一次" = potentially huge burst when stacks are high; it dealt 23 in R20. (3) 落花有意+1 (cheap 1-内伤/cycle) — g35's earlier states show adding it flipped the pid3 board to both-seats (matches my v30 note).

MECHANICS RE-VERIFIED: 厄劫缠身 card effect = apply 4 ([开局]=downgrade same-slot enemy card / 6 dmg). 血光之灾+1 = 2 内伤 + [开局] 1 内伤. 天星·御心 = retrigger PREVIOUS opening ×2 (put AFTER the opening card). 天星·牵引 = trigger the NEXT 2 openings (put FIRST). 内伤 ticks foe turn-start, ignores DEF. 杯弓蛇影 = apply N 内伤 + force foe's 内伤 to tick once NOW.

==== LEDGER ENTRY · Game 18 ====
## Game 36 (reviewed) — 谭舒雁/pid1, 命理师(7). RESULT: NOT 1st, final 命 0 (eliminated). Lobby: pid0 牧逸风 云剑/阵法师5 (ALIVE 命1, then won), pid3 小布 崩拳/气势5 (ALIVE 命20, RUNNER-UP/winner), pid2 吾行之 水灵5 (died). I finished 境5 修为77 maxHP105, 体魄0.

W/L: R1 W(pid3) R2 W(pid2) R3 L(pid3) R4 L(pid2) R5 L(pid0) R6 L(pid3) R7 L(pid2) R8 W(pid3) R9 W(pid0) R10 W(pid2) R11 W(pid3) R12 W(pid2) R13 L(pid3) R14 W(pid2) R15 L(pid3,-23) R16 L(pid3,-25 DEAD). Record 8-8. **pid3 小布 killed me 4 times late (R13/R15/R16 + R3/R6); he was my fatal opponent.**
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 雪羽清风, 星蚀, 斩断俗尘. (economy fates, combat-irrelevant — 5th confirmation.)

*** ROOT CAUSE — SAME AS g30/g33/g35: 厄劫缠身 NEVER DRAWN + FIELDED A 0-DAMAGE DEFENSE BOARD. ***
My R16 fielded board: [天星·牵引, 血光之灾+1, 天星·御心, 反震心法, 诸事不宜, 斗转星移, 星弈·断, 杯弓蛇影+1]. card_stats R16: 反震心法=0dmg, 诸事不宜=0dmg, 斗转星移=3dmg, 血光=0dmg, 牵引=0dmg, 御心=0dmg. I had 星弈·断 (16-28 nuke), 五雷轰顶 (burst), 流水无情 (6atk+2内伤) IN HAND and fielded pure defense instead.

*** POST-GAME PROOF (yisim search_board + sim_matchup, my OWN career 7) — THE FIX. ***
`[杯弓蛇影+1, 天星·牵引, 星弈·断+2, 五雷轰顶+2, 天星·御心, 厄劫缠身, 血光之灾+1, 落花有意+1]`
 = **80% first / 40% second vs pid3's EXACT final board (base)**, and **100%/100% vs pid0 & pid2**.
With 探灵 instead of 落花有意 → 60%/80% base; 60% first vs pid3 FULLY +1 (only weak spot: 0-40% second vs fully-+1 pid3 — the structural wall, matches 牧逸风's notebook).
MY ACTUAL fielded board: ~0%/0% vs pid3 (5 reps). The fix won t4-5 vs the dud's t9+ (or death).

*** THE RECIPE — KEY ORDER (this is the whole game): ***
1. **杯弓蛇影 FIRST** (=6 内伤 seeded + forces immediate tick at t1; the clock starts ticking in round 1).
2. 天星·牵引 SECOND: +2qi, triggers next 2 openings.
3. 星弈·断 mid (22-28 dmg, [星位] forces enemy skip — tempo denial).
4. 五雷轰顶 as burst closer (30%×5 × 10-12).
5. 天星·御心 AFTER the opening region (retrigger previous opening ×2).
6. 厄劫缠身: 4 内伤 + opening downgrades enemy same-slot card. THE LOAD-BEARING PIECE.
7. 血光之灾+1 (2 内伤 + opening 1), 落花有意+1 (+2qi, 1 内伤 filler).
NEVER field 反震心法/诸事不宜/斗转星移 as pure defense — they are 0-dmg slow-death slots.

*** ECONOMY AUDIT (rolls/round): 0,0,0,7(R5),0,14(R7),0,6(R9),4(R10),0,5(R12),4(R13),10(R14),7(R15),6(R16). ***
- R7 (14) and R14 (10) and R5 (7) = SHOTGUN with no named target → junk (absorbed 艮卦/两仪阵/星弈·立 etc).
- From R12 (境5) onward I had exchanges but NEVER named 厄劫缠身 (境5, 6 copies). Drew it ZERO times in 17 rounds — 5th consecutive game! Same as pid0 never drawing 万法.
- CONTRAST pid3: banked 13, then DUMPED 15 (R5) + 18 (R11 hunting 崩拳·降龙/寸劲/势如破竹 by NAME). Textbook scaling econ. He reached 体魄26/99HP by R13.
- pid0 (winner): never drew 万法 either; won on 云剑 qi-suite + 灵气灌注 into 白鹭/巨鲲.

*** TOP DISCOVERY (cross-game, 5th confirmation): 厄劫缠身 is THE 内伤-clock lever, AND the clock board must be fielded as DAMAGE not defense. 杯弓蛇影 goes FIRST (not last) to seed the clock at t1. The 内伤 clock has a hard speed ceiling ~t5-6 vs 崩拳 burst; you MUST pair it with burst (五雷轰顶/星弈·断) to close the race. ***

*** SURPRISE: pid3's 崩拳 burst is ~38+45+30 = 113 dmg across t3-6 through 0 def. A clock-only board CANNOT survive it; a clock+burst board races it t4-5. Also: 星弈·断+2's [星位] skip is a real tempo card vs a 2-cards/turn chase deck. ***

==== LEDGER ENTRY · Game 19 ====
# Game 37 (reviewed) — 谭舒雁/pid1, 命理师(7). RESULT: NOT 1st, final 命 0 (eliminated). Lobby: pid0 牧逸风 云剑, pid2 吾行之 水灵 (KILLED ME 3×: R14/R15/R16), pid3 小布 崩拳 (WINNER, 命20). Ended 境5 修为79 maxHP115, 体魄0.

W/L: R1 L(pid0) R2 L(pid3) R3 W(pid0) R4 L(pid2) R5 W(pid3) R6 L(pid2) R7 W(pid3) R8 W(pid0) R9 W(pid3) R10 L(pid2) R11 L(pid3) R12 W(pid2) R13 W(pid0) R14 L(pid2,-20) R15 L(pid2,-20) R16 L(pid2,-22 DEAD). Record 8-8. **pid2 吾行之 killed me 3 consecutive rounds to end me — he was my fatal opponent, NOT pid3.**

FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 雪羽清风, 妙手回春, 斩断俗尘. (economy — 6th confirmation combat-irrelevant.)

*** ROOT CAUSE — I fielded a 0-DMG SETUP SLOT (察体+1) over 内伤-generators, AND lost the 修为 seat to pid2. ***
My R16 board: [杯弓蛇影+1, 天星·牵引+1, 察体+1, 星弈·断, 轰雷掣电+1, 天星·御心+1, 血光之灾+1, 枯木逢春].
- VERIFIED post-game: this board = **0%/0% vs pid2** (5 reps). 察体 is a 0-dmg setup card (next-ATK +5 / [开局]碎防).
- R14 I acted SECOND vs pid2 (he won the 修为 seat); my board is SEAT-DEPENDENT vs pid2 = 100% first / 0% second.

*** TOP DISCOVERY (yisim-verified, 5-10 reps) — THE pid2 FIX, replacing the STALE 厄劫缠身 claim. ***
`[杯弓蛇影+1, 白鹤亮翅, 血光之灾+1, 流水无情+2, 落花有意, 天星·牵引+1, 血光之灾, 天星·御心+1]`
 = **100% FIRST / 100% SECOND vs pid2 EXACT final board (base)**, AND **100%/100% vs pid0 base AND +1.**
 LEVER = 白鹤亮翅 (+1-3 qi enabler) → lets 牵引+1/qigen come online a turn earlier → clock reaches 19 内伤 by t9-10 → ticks 19/turn through his 132 HP + heals → dead. NOT 厄劫缠身.
 厄劫缠身-version of my g36 recipe = only 33%/0% vs pid2 (STALE g35 claim "100%" DISPROVEN — M14 again).
 ORDER (verified; reorders FAIL): 杯弓蛇影 FIRST (seed+tick), 白鹤亮翅 (qi), 血光+1, 流水无情 (needs a debuff present → 2-4 内伤), 落花有意, 天星·牵引 (triggers the 2 openings AFTER it), 血光 (2nd opener), 天星·御心 (retriggers the opening BEFORE it ×2).
 ONLY pid3 小布 still 0%/0% — exhaustively searched my career-7 pool, NO winning board (崩拳 burst kills t5-6). STRUCTURAL wall (g30/g33/g36/g37 all confirm). Do NOT fight him head-on; beat everyone else.

*** ECONOMY AUDIT (rolls/round): 0,0,0,0,0,18,0,0,8,5,4,4,6,6,12,6. ***
- R6 = 18 shotgun rolls (no named target → junk: 两仪阵/白蛇/金鸡独立...). R15 = 12 rolls, 6+ hit nothing useful (banked by then, near-useless).
- NEVER NAMED 厄劫缠身 (境5, 6 copies live, 2.2%/roll, 7.1%/deal) from the 境5 gate → 6th consecutive game without drawing it. BUT this game proved 厄劫缠身 is NOT the win-con anyway — 白鹤亮翅+双血光+流水 is.
- CONTRAST: pid3 (winner) = 修为90, absorb-everything, ~78 rolls incl. R17=25 merge-dump. pid2 = 修为76, ~68 rolls. Me = 修为79, ~65 rolls. **I did NOT win the 修为 seat vs pid2 (critical).**

*** SURPRISE: The winner of the lobby (pid3, 崩拳 burst) is my WORST matchup (0%/0%) yet pid2 (whom I now beat 100%/100%) beat pid3 100%. The lobby is a rock-paper-scissors, and my job was to NOT lose to pid2 so pid2 could keep eliminating pid3. I lost the wrong matchup. ***

==== LEDGER ENTRY · Game 20 ====
# Game 20 (ARENA g20, ledger-entry #20) — 谭舒雁/pid1, 命理师(7). RESULT: **NOT 1st, final 命 0 (eliminated R18, the last round).** Winner = 小布 (pid3, 命49). pid0 牧逸风 & pid2 吾行之 also dead.
Record: W R1(pid0) L R2(pid2) W R3(pid3) W R4(pid2) L R5(pid3) L R6(pid0) L R7(pid3) W R8(pid0) W R9(pid2) L R10(pid0) W R11(pid2) W R12(pid3) W R13(pid0) W R14(pid2) W R15(pid0) L R16(pid3,-18) L R17(pid3,-21) L R18(pid3,-20,DEAD). 11-7. I won 6 straight (R8-R15) then pid3 killed me 3 straight to end me.
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 雪羽清风, 妙手回春, 斩断俗尘. (economy — 7th consecutive confirmation: combat-irrelevant for the 内伤 kit.)
Ended 境5 修为100 (2nd highest — beat pid3's 86 at start, WON the seat vs him every late round) maxHP114.

*** MY FATAL MISTAKE — I FIELDED A 6-SLOT BOARD THAT OMITTED 诸事不宜 + 天星·御心 + 落花有意. ***
R17 fielded: [天星·牵引, 血光之灾, 血光之灾, 杯弓蛇影+1, 杯弓蛇影+1, 流水无情, 白鹤亮翅+1, 落花有意] (8 slots, but NO 诸事不宜, NO 御心).
R18 fielded: [天星·牵引, 血光之灾, 梅开二度, 杯弓蛇影+2, 流水无情, 白鹤亮翅+1] (only 6 slots — I'd rolled away 血光+落花+御心 chasing junk at the 命0 deadline).
I went FIRST in R16/R17/R18 (won the 修为 seat) and STILL lost — because the board was wrong, not the seat.

*** DECISIVE POST-GAME PROOF (yisim, 10+ reps, both seats): ***
WINNER BOARD = `[天星·牵引, 血光之灾, 天星·御心, 诸事不宜, 落花有意, 梅开二度, 杯弓蛇影+2, 流水无情]`
  - vs 小布's EXACT R18 final board: **100% FIRST / 100% SECOND, ~8-9t.** (search_board over pools 1/6/7 + lock = converged on it immediately, 21 evals.)
  - My ACTUAL R18 fielded board (the 6-slot one): **20% first / 0% second** vs the SAME opponent board. THE GAP IS 诸事不宜 + 御心 + 落花有意 + 梅开二度.
  - vs pid3's fully-+1 board: still 0% (structural wall) — but he didn't field that.
  - MIRROR test: my board beats a copy-of-my-board opponent 25命 in 10t.
LOAD-BEARING CARD = **诸事不宜** (−6 atk on opponent's next 2 hits + 4 防 + opening 4 防). It cuts pid3's 34/27/24 崩拳 finishers down to 28/21/18. Combined with 梅开二度 doubling 杯弓蛇影+2 (→ 10 内伤 tick) and the clock hitting 16-18 by t8, the race flips.

*** WHY THE CLOCK LOST IN R17/R18 (Phase-1 trace): ***
pid3's curve: t1 崩拳·缠(11)+体魄/heal → t2 踏破九霄(+3force,+6agi) → t3 冲霄破浪(chase→崩拳·寸劲 24dmg) → t4 势如破竹(Mighty Force 34dmg, force-capped) → t5 崩拳·连崩(24) → t6 崩拳·戳(21). ~103 dmg through 0 def in 6-7t. My clock reached only 13-14 内伤 by t6-7 = 13-14/turn → too slow. NEEDED: slow him 6/hit (诸事不宜) so the clock's ~16-18/turn wins t8. That is exactly what the fix board does.
Also: 流水无情 fires its 2-内伤 only "if opponent has a debuff" — 血光/杯弓/内伤 counts, so 流水 MUST come after a 内伤 source (it did).

*** ECONOMY AUDIT (rolls/round): 0,0,0,0,0,2,0,14,0,15,4,4,6,4,0,0,1,25 (~75 total). ***
- R8=14 (境3!, landed 杯弓蛇影 only — the rest junk), R10=15 (landed 血光/杯弓/白鹤 — keepers), R18=25 (DESPERATION at 命0 — pure shotgun, landed 梅开二度 but rolled away 血光/落花 I needed).
- I WON the 修为 race (100, 2nd) yet lost — board quality > seat (matches 小布's g19 lesson).
- I HAD 诸事不宜 in hand R9-R10 and 天星·御心 R14 — and rolled/discarded BOTH. Pool shows they were plentiful (诸事不宜 2 left, 御心 5 left, 厄劫缠身 6 left live). **I threw away the exact cards that flip my hardest matchup. ROOT ECONOMY ERROR: no named keep-list for 诸事不宜/御心.**
- 小布's economy (g20): ~48 rolls total, absorb-everything, targeted dumps at phase unlocks. Ends 修为92 + 体魄31.

*** PER-RIVAL CAUSES: ***
- pid3 小布 (崩拳 burst, WINNER): killed me R5,R7,R16,R17,R18. My 内伤 clock loses the t6-7 race UNLESS I field 诸事不宜. FIX verified: 100%/100% both seats.
- pid0 牧逸风 (云剑/qi battery): I beat him R1,R8,R13,R15; lost R6,R10. His actual board had NO converter (he died). His notebook claims a 万法 board beats me 100% — I simmed it: my best 内伤 board LOSES 25命 t10 (his 万法 fires 12×(qi) + 白鹭 chase). HYPOTHETICAL only — he never built it.
- pid2 吾行之 (水灵): I beat him R2-loss? no: R4,R9,R11,R14 wins; lost R2. Beat him 4-1 late.

*** TOP DISCOVERY [g20]: THE 内伤 BOARD MUST BE 8 SLOTS AND MUST INCLUDE 诸事不宜 vs 崩拳 BURST. ***
Removing 诸事不宜 from the board drops pid3 matchup 100%→20% first / 0% second. It is THE anti-burst lever (flat −6 atk ×2 hits). Second lever = 梅开二度 → double 杯弓蛇影+2 (single biggest burst tick, 10-内伤). 天星·御心 retriggers the 血光 opening ×2 (more early stacks). Ranked: 诸事不宜 > 梅开二度 > 御心 > 落花有意.
The old notebook claim "C7 recipe = 100% first vs pid3" was TRUE for the g38 board but my g20 board had drifted to 6 slots without the defense slot.

*** SURPRISE: I won the seat AND still lost — the g38 C8 claim ("seat is the whole game") is REFUTED for THIS board. The fix board wins BOTH seats (100%/100%). Going second is no longer an auto-loss once 诸事不宜 is in. ***
*** SURPRISE 2: 命0 at the final round — I over-rolled 25 at R18 destroying my own board (rolled away 血光/落花) instead of keeping the 8-slot clock. Desperation rolling = self-sabotage. Freeze the board once it sims a win. ***

==== LEDGER ENTRY · Game 21 ====
==== LEDGER ENTRY · Game 21 (ARENA g21) ====
# Game 21 — 谭舒雁/pid1, 命理师(7). RESULT: **NOT 1st, final 命 0 (eliminated).** Winner = 牧逸风 (pid0, 命48). pid2 吾行之 & pid3 小布 dead. Ended 境5 修为96 maxHP111 体魄0.
W/L: L R1(pid0) W R2(pid3) W R3(pid2) L R4(pid0) W R5(pid2) L R6(pid3) L R7(pid0) L R8(pid2) L R9(pid0) W R10(pid3) W R11(pid2) W R12(pid0) W R13(pid2) W R14(pid3) W R15(pid0) W R16(pid3) L R17(pid0) L R18(pid0) L R19(pid0). Record 10-9.
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 雪羽清风, 雁影化身, 斩断俗尘. (economy fates — 8th+ confirmation: combat-irrelevant. A/B simulate(my_extra_fates=[1..5]) changed nothing.)

*** FATAL OPPONENT = pid0 牧逸风 (万法 battery), who killed me R17/R18/R19 to end the game. ***
His R19 final board: [辟邪阵纹, 百鸟灵剑诀+1, 引气剑+2, 化灵诀, 云剑·点星, 云剑·点星, 白鹭灵剑+1, 万法归灵剑+1]. Line: banks qi to 15 by t8 → 白鹭 t7 = 50 dmg → 万法 t8 = 95 dmg (5 + 6×15qi). Kills at t8.
My fielded boards R17/R18/R19 were pure 内伤 clocks WITHOUT 厄劫缠身 → 0%/0% vs his 万法 board.

*** ★★★★★ TOP DISCOVERY [g21] — 厄劫缠身 IS THE ANTI-万法 CARD. ★★★★★ ***
YISIM-VERIFIED (sim_matchup 5 reps): board `[杯弓蛇影+1, 厄劫缠身, 天星·牵引, 血光之灾, 梅开二度, 杯弓蛇影+2, 杯弓蛇影, 流水无情]` = **100% FIRST / 0% SECOND vs 牧逸风's EXACT final 万法 board** (I win t8, he dies at 内伤 16-17).
My ACTUAL R19 clock board (no 厄劫缠身) = 0%/0% (he ends at 16 HP, I'm 16 short).
WHY it works (TWO mechanisms, source-verified):
  1. 厄劫缠身 applies 4-6 内伤 → pushes the clock from 14 to 16-17 stacks by t8 (enough to kill 109 HP).
  2. Its [开局] DOWNGRADES the enemy card in the SAME slot index (gamestate_full.js:1303,1309 — lv2→lv1; 5994 downgrade_enemy_card_or_deal_damage uses currently_triggering_card_idx).
     - Placed slot 2 → downgrades his 百鸟灵剑诀+1→lv1 = less qi = 万法 delayed/weaker.
     - Placed slot 8 → downgrades his 万法归灵剑+1→lv1 = 95→80 dmg.
  3. Going first I tick him BEFORE his 万法 fires (t8a tick → he's at ~13 HP, then t8b my tick kills). Going second his 万法 (t8) fires BEFORE my last tick → structural loss. SEAT DECIDES THIS MATCHUP.
厄劫缠身 = 命理师 pool (career 7), 6 copies @境5, 3.1%/roll — I DREW IT ZERO TIMES IN 19 ROUNDS. Roll it BY NAME from R12.

*** ROOT CAUSE OF LOSS (two parts): ***
(a) I never drew 厄劫缠身 (the one card that flips my hardest matchup) — 7th consecutive game failing to NAME+hunt the key 境5 card.
(b) I lost the 修为 seat to pid0 late. His economy: broke 境5 at R11 (I broke R12); he reached 修为90 vs my 96 at R19 start but he'd absorbed faster. Actually I LED 修为 96 vs 90 — I DID go first R17/R19 and STILL lost because the board lacked 厄劫缠身. BOARD QUALITY > SEAT (matches g20/g24).

*** ECONOMY AUDIT (rolls/round): 0,0,0,0,0,10(R9),19(R10),4,4,6,3,9,0,0,12,12. ***
- R10 = 19 shotgun rolls at 境4→境5 (境5 unlocked end of R12... wait: I broke 境5 at R12). R10's 19 rolls were AT 境4 — 万法/厄劫 NOT UNLOCKED → largely wasted (landed 杯弓蛇影/血光, which are pre-境5 anyway, so not 0 value but inefficient). MATCHES pid0's M29.
- R19 = 12 desperation rolls at 命0 — rolled away 落花有意 and kept junk. SELF-SABOTAGE again.
- I hit the bank cap: ended several rounds at 0-6, but R16 banked 6, R17 banked 12, R18 banked 6 — no big waste. 
- pid0's economy is the model: R13 he rolled 7 and landed TWO 万法归灵剑 BY NAME. Targeted rolling from the 境5 gate.

*** PER-RIVAL CAUSES: ***
- pid0 牧逸风 (云剑/qi battery, WINNER): beat me R1,R4,R7,R9,R17,R18,R19. My 内伤 clock loses to his 万法 dump at t8. FIX = 厄劫缠身 board + first seat (100% verified). Without seat it's structural.
- pid3 小布 (崩拳 burst): I beat him R2,R10,R14,R16; lost R6. He died R? this game (eliminated). My clock + 诸事不宜 beats 崩拳 (confirmed g20).
- pid2 吾行之 (水灵): I beat him R3,R5,R11,R13. Lost R8. He died early-ish. Easy matchup.

*** SURPRISE: I led the 修为 seat vs pid0 (96>90) yet STILL lost — the missing card (厄劫缠身) cost me, not the seat. Also: the WINNER (牧逸风) won on the exact 万法 board that is my hard counter; my only path was to eliminate him before he assembled it, or field 厄劫缠身.**

*** FIXES FOR NEXT GAME: ***
1. FROM R12 (境5 gate): EVERY roll NAMED 厄劫缠身 (6 copies, my own sidejob). It is THE anti-burst card. Then 杯弓蛇影/梅开二度/血光之灾 for merge.
2. Keep the 8-slot clock board; NEVER field a 6-slot clock. FIELD 厄劫缠身 (slot 2 or slot 8 depending on enemy converter position).
3. vs pid0's 万法 board: sim the 厄劫缠身 board BOTH seats before set_board; if I'm second, expect structural loss → protect 命.

==== LEDGER ENTRY · Game 22 ====
==== LEDGER ENTRY · Game 22 (ARENA g22) ====
# Game 22 — 谭舒雁/pid1, 命理师(7). RESULT: **NOT 1st, final 命 0 (eliminated).** Winner = 小布 (pid3, 命100). pid0 牧逸风 & pid2 吾行之 also dead.
W/L: L R1(pid0) L R2(pid3) L R3(pid2) L R4(pid0) L R5(pid2) W R6(pid0) L R7(pid2) L R8(pid3) W R9(pid2) L R10(pid3) L R11(pid0) L R12(pid3) W R13(pid2) W R14(pid0) L R15(pid3). Record 4-11. Catastrophic open (0-5), never recovered.
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 后发制人, 雁影化身, 斩断俗尘. (Economy fates — 10th+ confirmation combat-irrelevant for 内伤 kit.)
Ended 境5 修为78 (highest of the 4 — I WON the seat every late round) maxHP103 体魄0.

*** ★★★★★ THE SINGLE ROOT CAUSE OF g22: MY BOARD WAS NOT THE 内伤 CLOCK. PERIOD. ★★★★★ ***
My R13-R15 fielded board: ['厄劫缠身','探灵','杯弓蛇影','卜命','天运·趋吉','吉运初显','金蝉脱壳','枯木逢春'].
card_stats(R15): 厄劫 0dmg(only 4 内伤), 探灵 0, 杯弓蛇影 6dmg, 卜命 6, 天运·趋吉 0(!), 吉运初显 3, 金蝉脱壳 0, 枯木逢春 11. TOTAL ~26 dmg over 10 turns.
内伤 bank never exceeded 6-9. That is NOT a clock, it's a pile of half-cards. The 内伤 sources that MATTER (血光之灾, 天星·御心, 天星·牵引, 梅开二度, 落花有意, 诸事不宜, 流水无情) were 0-1 present.

*** DECISIVE FIX (yisim-verified, 5 reps, both seats): ***
WIN BOARD = ['天星·牵引','厄劫缠身','血光之灾','天星·御心','梅开二度','杯弓蛇影+2','流水无情','诸事不宜']
  - vs 小布's EXACT final board: **100% FIRST / 100% SECOND, ~7-8t.**
  - vs 小布's +1 board: **100% first / 0% second** (OLD board was 0%/0% — the +1 wall is BROKEN on the seat I actually held).
  - vs 牧逸风 base: 100/100. vs 吾行之 base AND +1: 100/100/100/100. (pid0's +1 万法 board remains a 0% wall — but he didn't field it.)
  - search_board (lock 诸事不宜+厄劫缠身, 31 evals) converged on it instantly from this start. It IS the recipe.

*** HOW THE FIX WINS (from full_log): ***
t4b 天星·御心 retriggers 血光 opening ×2 → bank 8-9. t6b 梅开二度 doubles 杯弓蛇影+2 → applies 4+4 内伤 AND ticks the bank TWICE: 9→13→17 in ONE turn. t8 **turn-start tick of 17 kills** (opp at 14 → -3). The win comes on MY turn-start 8a — SEAT MATTERS, but with 诸事不宜 soaking 6dmg/hit I survive to t8 even second.
诸事不宜 = THE anti-burst lever: −6 atk on opponent's next 2-3 hits + 4def + opening 4def. Cut 小布's 32/25 崩拳 finishers to 26/19. WITHOUT it the clock dies t6-7; WITH it I live to the t8 kill.
厄劫缠身 = 4 内伤 + opening DOWNGRADE of the opponent's same-slot card (小布 slot-1 崩拳·降龙+1→+1... actually lv2→lv1 = −3 atk on his opener).

*** ECONOMY AUDIT (rolls/round): 0,0,0,0,0,2,3,1,0,0,4,24,0,0,0. ***
- **R12 = 24 SHOTGUN ROLLS AT 境5. THIS IS THE GAME-LOSING ERROR.** The log shows the roll chain: 反震心法→掌心雷→星弈·点→野马分鬃→星弈·断→金鸡独立→气贯长虹→天机·逆施→御雷卦诀→静气心法→螳螂捕蝉→星轨推衍→白鹤亮翅→星弈·飞→斩草除根→艮卦→天谕·攻→吉运初显→卜命→天命·飞逝→落雷术→杯弓蛇影→离卦→血光之灾→金蝉脱壳.
  I ROLLED THROUGH 杯弓蛇影 AND 血光之灾 — the exact cards my winning board needs — and STOPPED on 金蝉脱壳 (a pure def card). Then fielded it. M22/M18 at maximum scale: rolled past my own win-cons with no named target.
- R10 ended banked 25 (hit cap, wasted R11 grant). R1-R11 total only 10 rolls (fine, absorb-all) but R12 burned 24 in one shotgun burst.
- 修为: I ended 78 = HIGHEST in lobby. I won the seat and still lost — BOARD QUALITY >> SEAT (matches g20/g21). 
- 小布's economy (winner): absorbed all game, ~0 shotgun rolls, assembled a coherent 崩拳+气势+体魄 board and just executed it. He never self-sabotaged. C13 confirmed again (4th game).

*** PER-RIVAL CAUSES: ***
- pid3 小布 (崩拳 burst, WINNER): killed me R2,R8,R10,R12,R15 (5 times!). My non-clock board each time; his 崩拳 firing 25-33/hit from t5. FIX board beats him 100/100 base, 100% first at +1.
- pid0 牧逸风 (云剑/qi): I beat him R6,R14; lost R1,R4,R11. His base board = my 100/100. His +1 万法 = 0% wall.
- pid2 吾行之 (水灵/五行): beat him R9,R13; lost R3,R5,R7. FIX board = 100/100/100/100 vs him. He was my easiest matchup and I still dropped 3 early — all board-quality.

*** TOP DISCOVERY [g22]: THE 8-SLOT CLOCK WITH **BOTH** 厄劫缠身 AND 诸事不宜 BREAKS 小布's +1 wall (first seat). ***
Prior (g20/g21) 7-card clocks were 0% vs his +1 board. Adding 厄劫缠身 (more stacks + downgrade) AND 诸事不宜 (−6 atk ×N) → 100% first. The recipe: [天星·牵引, 厄劫缠身, 血光之灾, 天星·御心, 梅开二度, 杯弓蛇影+2, 流水无情, 诸事不宜]. Card ranking: 诸事不宜 > 厄劫缠身 > 梅开二度 > 御心≈牵引 > 血光 > 流水.

*** SURPRISES: ***
1. I fielded a "clock" that never got past 9 内伤 — I had NAMED the recipe for 3 games and still never assembled it, because I rolled shotgun instead of keeping the named cards. THE FAILURE IS ECONOMIC, not tactical.
2. 6 of my 8 cards dealt ~0-6 dmg. I was effectively fighting with 2 cards.
3. I won the seat AGAIN (78 修为, highest) and lost AGAIN. Third straight game. Seat is a red herring when the board is wrong.

==== LEDGER ENTRY · Game 23 ====
# Game 23 (ARENA g23) — 谭舒雁/pid1, 命理师(sidejob 7). RESULT: **NOT 1st, final 命 0 (eliminated).** Winner = 吾行之 (pid2, 命1). 牧逸风(pid0)/me/小布(pid3) all dead. Ended 境5 修为64 maxHP99 体魄0.
W/L: W R1(pid2) L R2(pid0) W R3(pid2) L R4(pid3) W R5(pid2) L R6(pid0) W R7(pid3) L R8(pid2) L R9(pid3) L R10(pid2, -18) L R11(pid0, -21) L R12(pid3, -15) L R13(pid0, -25→dead). Record 4-9, catastrophic close (0-5 last five).
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 雪羽清风, 雁影化身, 斩断俗尘. (Economy fates — 12th+ straight confirmation: combat/传承 fates are combat-irrelevant for the 内伤 kit.)

*** ★★★★★ SINGLE ROOT CAUSE: I NEVER ASSEMBLED THE 内伤 CLOCK. 5TH STRAIGHT GAME. ★★★★★ ***
- My ACTUAL final board (R13): ['诸事不宜','天星·御心','星弈·虎','梅开二度','流水无情','白蛇吐信','天谕·守','命运轮回'].
  card_stats(R13): 诸事不宜 0dmg(+16def), 天星·御心 0dmg(+51def!), 星弈·虎 12, 梅开二度 0, 流水无情 6, 白蛇吐信 18, 天谕·守 2, 命运轮回 0. TOTAL ~38 dmg over 24 turns.
  → ZERO 内伤-generating clock. Only 1-2 内伤 sources (流水无情 needs a debuff already; 诸事不宜/御心 are pure def). It is a pile of def cards, NOT a clock.
- R10 board was literally [天星·牵引, 流水无情, 天运·趋吉] + 5 empty slots (Normal Attack) → 33 dmg over 13 turns.
- 内伤 bank never mattered. THE RECIPE WAS NAMEABLE (my own C4 from g22) AND WAS HANDED TO ME:
  R11 dealt 梅开二度 + 诸事不宜 FOR FREE; R12 dealt 天星·御心 FOR FREE → I ROLLED ALL THREE AWAY.
  My live deck had 6× 厄劫缠身, 8× 血光之灾, 8× 杯弓蛇影, 5× 梅开二度, 7× 天星·御心, 5× 天星·牵引, 4× 诸事不宜.

*** ★★★★★ TOP DISCOVERY [g23]: THE C4 CLOCK BOARD BEATS THE LOBBY WINNER (吾行之) 100%/100%. ★★★★★ ***
yisim sim_matchup (3 reps each, vs ACTUAL last-known boards):
  C4 = ['天星·牵引','厄劫缠身','血光之灾','天星·御心','梅开二度','杯弓蛇影+2','流水无情','诸事不宜']
  - vs pid2 吾行之 (THE WINNER, 水灵 maxHP-grind tank): **100% first / 100% second** (~10-11t). His +1 board: 0/0 (unavoidable wall).
  - vs pid0 牧逸风 (云剑/万法): **100% first / 100% second, base AND +1** (~10t).
  - vs pid3 小布 (崩拳/气势/体魄 burst): **100% first / 100% second base; 100% first / 0% second vs his +1 board.**
  → THE BOARD THAT WOULD HAVE WON ME THE GAME. My actual boards were 0% vs everyone.
  → search_board (lock 厄劫缠身, career 7, 41 evals) converged on it INSTANTLY — it IS the recipe.
  → full_log vs the tank: 梅开二度→杯弓蛇影+2 doubles the apply (→17 内伤 in one turn, t6b), then each victim turn-start tick
    (9→13→17→19→20) outpaces the tank's 纳百川 heal/maxHP grind. I win t11 EVEN GOING SECOND. 内伤 IS the tank counter.

*** WHY 内伤 BEATS THE WATER TANK (matches 牧逸风's own g27 note: "vs a healing/HP-scaling tank, CHIP cannot win — need 内伤/[减攻]") ***
- The tank (纳百川) heals +12 maxHP/cycle and can reach 156-207 HP — no chip board kills it.
- 内伤 ticks at VICTIM turn-start, IGNORES 防 and heal-per-hit, PERMANENT. ~20 stacks = 20 dmg/turn that
  out-runs a 12 HP/cycle heal. The clock grows faster than the tank.

*** ECONOMY AUDIT (rolls/round): 0,0,0,0,0,0,1(R7),4(R8),2(R9),15(R10),6(R11),11(R12),6(R13). ~45 rolls, ~39 POST-境5 but ZERO named. ***
- Broke 境5 at R10 END (earliest ever — 修为55 hit during R10's rolls). GOOD pacing, but then R10-R13 = 38 SHOTGUN rolls.
- R10=15 rolls (境4→境5 transition), R12=11, R13=6 — all nameless. The chain rolled THROUGH my win-cons (天星·御心, 梅开二度, 诸事不宜 were all dealt and rolled away).
- Winner 吾行之 (pid2): rolls ≈ [0,0,0,0,0,9,0,0,0,3,0,25,7,8,0,0,1] — ONE big named dump at R13 right after 境5, then absorb. Ended 修为80.
- 小布 (pid3): rolls ≈ [0,0,0,0,2,0,0,22,0,0,4,0,0,3,9,11,0,0] — one dump at R8 (境4), coherent board every round. Ended 修为100.
- PATTERN (now 5 games): rivals absorb hard, fire ONE targeted dump right after the gate, STOP. I shotgun 10-25 rolls/round with no target name → roll past my own win-cons.

*** PER-RIVAL CAUSES ***
- pid2 吾行之 (WINNER, 水灵 tank): I beat him R1,R3,R5 (early, his board thin) but lost R8,R10 (his tank scaled). C4 clock beats him 100/100 — my only real loss here was not fielding it.
- pid0 牧逸风 (云剑/万法): beat me R2,R6,R11,R13. C4 clock beats his base AND +1 board 100/100. His 修为 led mine → he took the seat late.
- pid3 小布 (崩拳 burst): I beat him R7; lost R4,R9,R12. His 崩拳·寸劲 气势 burst + 磅礴之势 (36-45 dmg finisher, chase) killed my scattered piles. C4 + 诸事不宜 beats his base 100/100.

*** SURPRISES ***
1. I broke 境5 at R10 (earliest ever) — my pacing FINALLY good — yet assembled a WORSE board than ever (pure def pile). Economy fixed, BOARD-BUILDING rule still violated.
2. The winner was the SLOW TANK, not the burst — and my clock is the exact hard-counter to it. I literally held the anti-winner tech and never played it.
3. 天星·御心 (the retrigger engine) was dealt FREE at R12 and I rolled it away; my R13 board had it but as a pure def card next to no 开局-generators → +51 def and 0 clock.

*** FIXES (reinforced, now 5 games failing on the SAME thing) ***
1. ★ THE RECIPE IS FIXED. FROM the 境5 gate, my board IS C4 by name. NO EXCEPTIONS. Absorb/roll ONLY to FIND C4 pieces.
2. EVERY roll from R10+ must be NAMED (厄劫缠身 > 血光之灾 > 杯弓蛇影 > 梅开二度 > 天星·御心 ≈ 天星·牵引 > 流水无情 > 诸事不宜).
3. KEEP-LIST (never roll/absorb): those 8 cards. If dealt, STOP rolling that round.
4. FIELD 8-slot clock, NEVER a def pile. A no-内伤 board is a guaranteed loss.
5. 修为 pacing is FINE (broke 境5 R10). The fail is board assembly, not economy.

==== LEDGER ENTRY · Game 24 ====
# Game 24 (ARENA g24) — 谭舒雁/pid1, 命理师(sidejob 7). RESULT: **NOT 1st, final 命 0 (eliminated).** Winner = 吾行之 (pid2, 命18). 牧逸风(pid0)/me/小布(pid3) all dead 命0.
W/L: L R1(pid0) L R2(pid3) L R3(pid2) W R4(pid0) W R5(pid2) W R6(pid3) W R7(pid2) W R8(pid3) L R9(pid0) L R10(pid3) L R11(pid2) L R12(pid3) L R13(pid2) L R14(pid0). Record 5-9. Won 5 straight R4-R8 then collapsed 0-6.
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 稳固根基, 雁影化身, 斩断俗尘. (Economy fates — 13th straight confirmation combat/传承 fates are combat-irrelevant for the 内伤 kit.) Ended 境5 修为69 maxHP109 体魄0.

*** ★★★★★ ROOT CAUSE: 6TH STRAIGHT GAME WITHOUT THE 内伤 CLOCK. ★★★★★ ***
My ACTUAL final board (R13-R14): ['血光之灾','紫气东来','星弈·立','星弈·断','螳螂捕蝉','流水无情','诸事不宜','静气心法'].
card_stats(R14): 血光之灾 0dmg (just 2 内伤), 紫气东来 0 (+10qi), 星弈·立 11, 星弈·断 29, 螳螂捕蝉 4, 流水无情 6, 诸事不宜 0, 静气心法 0. 内伤 bank never exceeded ~2-3. This is NOT a clock — it's a random 星弈 pile.
R10 board was literally ['天运·趋吉','血光之灾','血光之灾'] then ['静气心法'] then 3 Normal-Attack slots → I fielded 3 cards and lost with empty slots attacking for 3. UNCONSCIONABLE.
The C4 pieces were in my pool ALL GAME (厄劫缠身×6, 天星·御心×8, 天星·牵引×8, 梅开二度×6, 诸事不宜×6, 杯弓蛇影×8, 血光之灾×1left). I was DEALT 诸事不宜 R12, 流水无情 R13, 诸事不宜 R14 and ROLLED/ABSORBED them.

*** ★★★★★ TOP DISCOVERY [g24]: TWO 杯弓蛇影 BEAT 天星·御心 — THE NEW BEST CLOCK. ★★★★★ ***
NEW RECIPE (supersedes C4-with-御心): `[杯弓蛇影+2, 天星·牵引+1, 厄劫缠身, 血光之灾, 诸事不宜, 梅开二度, 杯弓蛇影, 流水无情]`
  - **vs pid2 吾行之's EXACT final board (THE WINNER'S tank): 100% first / 100% second (3 reps, yisim).** [vs +1: 100% first / 0% second]
  - vs pid0 牧逸风 base AND +1: **100% / 100%.**
  - vs pid3 小布's +1 board: **100% / 100%** (the OLD 天星·御心 C4 was 0%/0% vs his +1!!). vs his base: 100% first / 0% second.
  WHY: 御心 only retriggers 1 opening ×2 (def-ish); a SECOND 杯弓蛇影 adds more raw 内伤 AND ticks the bank again. Two 杯弓 set slot1+slot7; 牵引 at slot2 retriggers the openings after it.
  KEY ORDERING: 杯弓蛇影 first (its 内伤 apply feeds the bank), 天星·牵引+1 slot2 (retriggers 厄劫+血光 openings → +4+2 内伤 turn 1), 梅开二度→杯弓蛇影 (+2 内伤 AND ticks), 流水无情 last (needs officer debuff).
  HOW IT WINS (full_log vs the tank, going FIRST, 9t): turn1 openings land ~6 内伤; t3 厄劫 +4 (=10); t4 血光+1 +2 (=12); t6 梅开二度→杯弓蛇影+2 → +2 & tick 12→14→16; t9 second 杯弓蛇影 lv3 +4 & tick 22 → dead. The tank reached 155 maxHP and STILL died — 内伤 is permanent + ignores 防 + out-runs the +12/cycle heal.
  Even going SECOND it wins (10t): last tick 22 dmg at opp turn-start.

*** THE ORIGINAL C4 (with 天星·御心) — STILL GOOD vs 吾行之 but WEAKER ***
`[杯弓蛇影+2,天星·牵引+1,厄劫缠身,血光之灾,天星·御心,梅开二度,流水无情,诸事不宜]` = vs 吾行之 100%/100% base; vs 牧逸风 100/100 base; vs 小布 +1 = 0%/0% (WRONG).
The 2× 杯弓 variant DOMINATES it. USE 2× 杯弓.

*** ECONOMY AUDIT (rolls/round): 0,0,0,2,0,0,1,11,17,4,4,7,6 ≈ 52 rolls, ALL SHOTGUN, ZERO named. ***
- R9=11, R10=17, R13=7, R14=6 — every 境4-境5 roll NAMELESS. In R10 the chain rolled THROUGH 血光之灾 TWICE (rolled it away, took it back, rolled again). In R14 I ABSORBED 流水无情 + 诸事不宜 (my win-cons!) for 修为.
- Broke 境5 at R11 (early! good pacing) but had ZERO clock pieces assembled. Pacing is FINE; board assembly is the failure.
- Winner 吾行之: broke 境5 R12, ONE 25-roll dump R12, then 5-8 NAMED rolls/round for 水灵·纳百川/水灵·波澜/水灵阵, STOPPING when fielded. 小布: one 16-roll dump R14 at 境5, otherwise absorb-all.
- ★ THE PATTERN (6 games now): rivals absorb hard, fire ONE named dump right after the gate, then STOP. I shotgun 10-17 rolls/round with no target name.

*** PER-RIVAL CAUSES ***
- pid2 吾行之 (WINNER, 水灵 tank): lost R3,R11,R13. NEW 2×杯弓 clock beats him 100/100 (both seats, actual final board). His tank hit 155HP and still died to 内伤. HE WAS MY EASIEST MATCHUP.
- pid3 小布 (崩拳 burst): lost R2,R10,R12. NEW board beats his +1 board 100/100 (old 御心 board was 0/0). R10 loss = I fielded only 3 cards.
- pid0 牧逸风 (云剑/qi): lost R1,R9,R14, won R4. NEW board beats his base AND +1 board 100/100.
- Net: the NEW clock board wins/mostly-wins EVERY announced matchup. My non-clock boards won nothing.
- 小布's OWN notebook (frozen): "vs pid1 谭舒雁 命理师/内伤 clock — I win most" — TRUE ONLY because I never fielded a clock.

*** SURPRISES ***
1. The winner was the SLOW TANK again (2nd straight), and my clock is its hard counter — held the tech, never fielded it. 6th game.
2. My R10 board literally had 3 empty slots attacking as Normal Attack 3. I fielded a 3-card board at 境4 with 命 already dropping.
3. A SECOND 杯弓蛇影 beats 天星·御心 — retrigger engines (御心/牵引) matter less than raw 内伤 + extra ticks.
4. I went 5-0 mid-game (R4-R8) with a mediocre pile purely on early-board quality, then 0-6 as rivals scaled.

*** FIXES (now 6 games on the SAME failure) ***
1. ★ THE RECIPE (2× 杯弓 version above) IS THE BOARD. FROM 境5, field it BY NAME. NO EXCEPTIONS.
2. KEEP-LIST (NEVER roll/absorb): 杯弓蛇影, 厄劫缠身, 诸事不宜, 天星·牵引, 梅开二度, 血光之灾, 流水无情, (天星·御心 backup).
3. EVERY post-gate roll NAMED. STOP the moment a recipe piece is dealt.
4. NEVER field a board with empty slots or <8 cards at 境4+. Empty slot = Normal Attack 3 = a wasted turn.
5. 修为 pacing OK (broke 境5 R11). Fail is assembly.

==== LEDGER ENTRY · Game 25 ====
==== LEDGER ENTRY · ARENA Game 25 ====
## ARENA Game 25 — 谭舒雁 (pid1), 命理师(sidejob 7). **RESULT: 1st PLACE / WINNER, final 命 40.** ★★★
牧逸风(pid0) eliminated 命0; 吾行之(pid2) eliminated 命0; 小布(pid3) eliminated 命0.
W/L: W R1(pid2) L R2(pid3) W R3(pid0) W R4(pid2) L R5(pid3) L R6(pid2) L R7(pid0) W R8(pid3) W R9(pid0)
L R10(pid3) W R11(pid0) L R12(pid3) W R13(pid0) W R14(pid2) W R15(pid3) W R15(pid0) W R16(pid3) L R16(pid0) W R17(pid0).
Ended 境5 修为88 (HIGHEST of the 4 — won the seat every late round) maxHP107 体魄0.
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 顿悟, 雁影化身, 斩断俗尘. (Economy/misc fates — 15th straight confirmation these are combat-irrelevant for the 内伤 kit. 勤学苦练 = free extra draw, the one MEANINGFUL pick.)

## FINAL BOARD (R17, fielded & WON the title round):
['天星·牵引', '厄劫缠身', '杯弓蛇影+1', '杯弓蛇影', '流水无情', '诸事不宜+1', '命运轮回+1', '吉运初显']
  - yisim sim_matchup vs ALL THREE rivals' EXACT final boards: 100% first / 100% second EACH.
    vs pid0 牧逸风 (万法 qi-battery): 100/100 (~9-10t). vs pid2 吾行之 (水灵 tank): 100/100 (~13-15t).
    vs pid3 小布 (崩拳 burst): 100/100 AND vs his +1 board 100/100! (my old clock failed at his +1; this one doesn't.)
  - Only structural loss: a HYPOTHETICAL +1/+2 upgrade of 牧逸风's 万法 board (0%/0%) — HE NEVER FIELDED IT (his 万法 was already +1; a +2 needs 4 copies he didn't hold).

### ★★★★★ WHY THIS GAME FINALLY WON (after g22/g23/g24 all failing on the SAME thing) ★★★★★
The 内伤 CLOCK *PLUS SURVIVAL CARDS*. Prior games I fielded either a def-pile (0 clock) or a bare clock (got out-burst t6-8).
g25 board = clock (厄劫 4+杯弓+1 3+杯弓 2 = 9 内伤 by t4, +流水 2) ADDED to survival (诸事不宜+1 -6atk×3, 命运轮回+1 +12HP+skip, 吉运初显 +7HP+开局+4).
  - 命运轮回+1 was LOAD-BEARING: sim A/B removing it for 落花有意+1 = LOSE 0/0; the +12 maxHP is EXACTLY the margin that survives 牧逸风's
    88-dmg 万法 one-shot (I finished the winning sim at 10/123 HP). Removing it loses.
  - 诸事不宜+1 cut 牧逸风's 百鸟 27-dmg hit and 小布's 崩拳 finishers → survives his +1 board (old boards were 0% there).
  - 吉运初显's 开局 (HP+4 ×2 via 牵引) matters more than a raw-attack card: swapping it for 气吞山河+1 = LOSE 0/0. KEEP it.
  - 命运轮回 skips MY slots 4&5 (杯弓蛇影, 流水无情 — NO 开局) so the skip is pure downside, BUT its +12HP dominates. In a board where
    slot4/5 DO have 开局 (e.g. 血光/厄劫) 命运轮回 is even better (triggers them). Order slots so 开局-cards land in 4/5.

### ★ VERIFIED vs RIVAL BOARDS (yisim, 3-4 reps each, both seats):
- 牧逸风 (聚灵心法/百鸟/引气剑/化灵诀/回响/灵气灌注/白鹭/万法+1): 100%first/100%second (~9t).
- 吾行之 (邪蛊/不动/辟邪/潜遁/纳百川/泉涌/木灵印/疗愈): 100/100 (~13-15t) — the tank's heal loses to the permanent clock.
- 小布 (气若悬河+1/冲霄破浪/灵玄迷踪步/踏破九霄/势如破竹/崩拳·突+1/崩拳·缠/崩拳·惊触): 100/100, AND +1 board 100/100.
- search_board (locks 厄劫+杯弓+杯弓+1, careers [6,1], 41 evals): best alternate = 100/0 — WORSE. My board is the optimum vs the field.

### ★ TOP DISCOVERY [g25]: CLOCK + SURVIVAL, NOT clock-alone and NOT def-pile. The recipe:
['天星·牵引','厄劫缠身','杯弓蛇影+1','杯弓蛇影','流水无情','诸事不宜+1','命运轮回+1','吉运初显']
  = 4 clock cards + 4 survival cards. Clock cards (厄劫>杯弓+1>杯弓>流水) do the killing; survival (诸事不宜+1, 命运轮回+1, 吉运初显, 牵引)
  buy the ~9-10 turns the clock needs to tick to lethal. Evidence: removing ANY survival card → 0/0 loss. Removing clock → no kill.
  牵引 at slot1 retriggers the 2 openings AFTER it (厄劫's 开局-downgrade + 吉运's 开局+HP+4) = free value every cycle.

### ★ ECONOMY (rolls/round): 0,0,0,0,0,13,5,3,3,4,4,3,7,2,4,0,0.
- R6 = 13 rolls at 境3 (PRE-境5!) — pure M29 shotgun, rolled 星罗棋布→众星拱月→气疗术→天命飞逝→海底捞月→...→坤卦 (all junk absorbed for 修为). WASTE.
- R1-R5 & R7-R11 = absorb-all, ≤5 rolls/round. GOOD (this is what got me 修为 88 = highest).
- Broke 境5 @ R11 (修为55). Rolls R12-R15 = 3,7,2,4 all aiming (loosely) at clock pieces; landed 厄劫缠身(R13), 天星·御心(R13), 流水无情(R15).
- R16 = 0 rolls, MERGED 4 cards (命运轮回/诸事不宜/气吞山河/杯弓蛇影 all +1) = the winning power spike. R17 = 0 rolls, merged 御心+1.
- LESSON: the R16 mass-merge (4× +1 at once) was the game-winning economy move — bank exchanges R13-R15, then MERGE the doubles at the end.
  R6's 13-roll shotgun at 境3 was the one clear leak (pre-gate rolls ≈ 0 value, M29 6th confirmation).

### PER-RIVAL CAUSES (final):
- pid0 牧逸风 (云剑/万法 qi-battery): 5W-3L. BEAT him when clock reached lethal before his 万法 one-shot (my 11/turn tick killed him t9 even after his 88 hit left me at 10HP). LOST R7/R16 when I hadn't assembled the full 8-slot clock (transitional piles).
  His 万法+1 (88-107 dmg one-shot) is the single biggest threat; 命运轮回+1/诸事不宜+1 are the exact answer.
- pid2 吾行之 (水灵 heal-tank): 3W-2L early, then W R14. Clock (permanent, ignores 防+heal) out-races his maxHP ramp. My EASIEST matchup.
- pid3 小布 (崩拳 burst): 5W-4L. His t7-10 崩拳 burst is the fastest kill in the lobby; 诸事不宜+1 (-6×3) + 命运轮回+1 HP soak survive it, then clock wins t9-11. Lost only when my board was a transitional pile (R2/R5/R10/R12).

### SURPRISES:
1. I WON with 命40 while never being the strongest round-1-to-15 player — the 命 system rewards SURVIVAL (last standing), and my clock+sustain went 9-13t consistently, outlasting burst rivals.
2. 小布's +1 board (which 0%-killed my old clocks per g22/g24 notes) is now 100/100 BEATEN — 诸事不宜+1 (level 2: -6atk×3 hits) is the lever.
3. The R16 mass-merge of 4 doubles at once was worth more than any single roll — merging = free power + 修为, no deck-burn.
4. R6's 13 pre-境5 rolls (M29 AGAIN) cost me nothing this game because I absorbed the junk for 修为 (ended highest) — but it was still unnecessary risk.
5. 命运轮回's self-skip of slots 4/5 is a NON-issue when those slots hold non-开局 cards; its +HP is the whole point. Would be a net plus if slots 4/5 held 开局 cards.

### NEXT-GAME (from g25 evidence):
1. R2 sidejob = 7 (命理师). Board = CLOCK + SURVIVAL 8-slot, never def-pile, never bare-clock.
2. Named clock targets (roll from R11+): 厄劫缠身 > 杯弓蛇影 > 流水无情 > 血光之灾 > 梅开二度.
   Named survival targets: 诸事不宜 > 命运轮回 > 吉运初显 > 天星·牵引 > 天星·御心 > 落花有意.
3. NEVER roll before 境5 gate (M29). Absorb ALL junk R1-R10 for 修为/seat.
4. BANK exchanges R13-R15, mass-MERGE doubles R16-R17 for the power spike.
5. Per-rival: 牧逸风→race the 万法 one-shot (need 命运轮回 HP + 诸事不宜 dmg-cut). 吾行之→clock out-races tank, easy.
   小布→诸事不宜+1 + 命运轮回 HP survive burst, win t9-11. Seat matters less than the assembled board.

==== LEDGER ENTRY · Game 26 ====
==== LEDGER ENTRY · ARENA Game 26 ====
## 谭舒雁 (pid1), 命理师(sidejob 7). RESULT: NOT 1st — final 命 0 (eliminated). WINNER = 小布 (pid3, 命17). 牧逸风(pid0)/me/吾行之(pid2) dead 命0.
W/L: W R1(2) W R2(0) W R3(2) W R4(0) L R5(3) W R6(2) W R7(3) W R8(2) L R9(3) L R10(0) L R11(3) W R12(2) L R13(3) L R14(2) L R15(0). Record 8W-7L. 5-0 start (R1-R8 mostly) then collapsed 1-6.
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 副职兼修, 雁影化身, 斩断俗尘. (Economy only — 16th straight confirmation combat/传承 fates are combat-IRRELEVANT for the 内伤 kit; my_extra_fates=[1,2,3]/[101] gave ZERO change.)
Ended 境5 修为72 maxHP103 体魄0. Gates: 境2@R3, 境3@R6, 境4@R8, 境5@R10 (GOOD pacing, fastest of lobby).

## FINAL BOARD (R15, the one that lost): ['反震心法','杯弓蛇影+1','流水无情','藕断丝连','螳螂捕蝉+1','海底捞月','命运轮回','吉运初显+1']
card_stats(R15): 反震 0dmg, 杯弓蛇影+1 3dmg, 流水 6, 藕断 0, 螳螂+1 6, 海底捞月 0, 命运轮回 0dmg(+8HP), 吉运初显 0. 内伤 bank never exceeded 5. THIS IS NOT A CLOCK.
yisim vs 小布's ACTUAL final board: LOSE -29命 (7t). My board is a leftover pile (only 1 real clock card).

## ★★★★★ ROOT CAUSE (7th game, SAME failure): ROLLED THROUGH THE RECIPE AT THE 境5 GATE. ★★★★★
R11 = **25-roll shotgun** at the 境5 gate. The roll chain (economy_history R11) literally passed through:
  螳螂捕蝉→轰雷掣电→杯弓蛇影(kept one)→坤卦→天元心法→白蛇吐信→反震心法→紫气东来→**诸事不宜→落雷术(ROLLED IT AWAY)**→...
  →凶象→流水无情(kept)→天星·御心→星弈·打→...→卜命→天谕·守→藕断丝连.
I rolled AWAY 诸事不宜 (my #1 survival card) and burned 25 exchanges naming NOTHING. Ended R11 with a 4-card board.
I held pool access to: 厄劫缠身×6, 杯弓蛇影×6, 血光之灾×5, 流水无情×7, 诸事不宜×5, 天星·牵引×8, 命运轮回×5, 吉运初显×6, 梅开二度×6, 落花有意×8 — the whole clock kit was drawable ALL GAME.
Net rolls/round: 0,0,0,0,0,0,0,0,2,1,25,4,5,7,6 ≈ 50, ALL NAMELESS, mostly at 境5.

## ★★★★★ TOP DISCOVERY [g26]: THE ANTI-BURST SURVIVAL STACK = DOUBLE 诸事不宜 + DOUBLE 命运轮回. ★★★★★
NEW RECIPE (supersedes g25's clock+sustain): 
  `['天星·牵引','厄劫缠身','杯弓蛇影+1','杯弓蛇影','诸事不宜','诸事不宜','命运轮回','命运轮回']`
  yisim sim_matchup vs ALL THREE rivals' EXACT final boards: **100% first / 100% second EACH.**
   vs pid0 牧逸风 (万法 qi-nuke): 100/100 (~11t). vs pid2 吾行之 (水灵 tank): 100/100 (~14-15t). vs pid3 小布 (崩拳 burst): 100/100 (~9-10t).
  The g25 single-诸事不宜 recipe **LOSES -26命 in 6 turns to 小布's final board** — 小布's burst (t5 寸劲 30 + 惊触 30; t6 连崩 20+17+30 = ~127 dmg over 2 turns) out-races a single-survival clock. TWO 诸事不宜 = 4 stacks of -6atk (mitigates his 30-hits to 24) is the EXACT margin that survives to t9-10.
  VERIFIED it's the DOUBLE that matters: removing ONE 诸事不宜 → LOSE -26 (7t). Removing ONE 命运轮回 (keeping 1× 诸事不宜... no, need both 诸事) and substituting 吉运初显 for 2nd 命运轮回 → STILL WIN 100/100. So load-bearing = 诸事不宜×2; 命运轮回 is flex (1 or 2 both fine).
  CATCH: still 0%/0% vs a HYPOTHETICAL all-+1/2 小布 board (his 寸劲+1 44 + 惊触+1 51 = 95 dmg/turn) — UNREACHABLE (needs 4× 威震四方). Realistic target = his actual board, beaten.

## ECONOMY AUDIT
- Rolls: 0,0,0,0,0,0,0,0,2,1,25,4,5,7,6 ≈ 50. R11=25 is the single biggest leak in the game (M29 7th confirmation).
- 修为 pacing EXCELLENT: broke 境5 @R10 (fastest), ended 修为72 (but 小布 had 80, 牧逸风 93 → I did NOT even hold seat by end; both out-修为'd me because I rolled instead of absorbing).
- ★ Lesson: I burned 25 exchanges that could have been ~12 absorptions = +12 修为 AND kept the recipe cards I rolled past. Rolling THROUGH 诸事不宜 cost me the game twice (card loss + 修为 loss).

## PER-RIVAL CAUSES
- pid3 小布 (WINNER, 崩拳 burst — got 威震四方@R13, +1@R16): lost R5,R9,R11,R13. His burst kills t6-7; my leftover boards had no survival stack. NEW double-诸事 board beats his actual final board 100/100 both seats. He out-修为'd me (80>72) = he had seat when it mattered.
- pid0 牧逸风 (云剑/qi 万法 nuke): lost R10,R15. R15 log: his 万法 (Dharma Spirit Sword) hit 70 at t8 after 白鹭 46 at t7 — 116 dmg in 2 turns, killed me through 命运轮回's +8HP. NEW board wins 100/100 (~11t) — double 命运轮回 (+16 HP) + 诸事不宜 mitigation is the margin.
- pid2 吾行之 (水灵 heal-tank): W R1,R3,R6,R8,R12; L R14. EASIEST — clock out-races tank (permanent 内伤 ignores 护/防).
- Net: I was 8-7 but 0-5 in the final 4 rounds because my board was never the assembled clock.

## SURPRISES
1. The winner was the BURST again, and his burst beats my SINGLE-survival clock — but double-诸事不宜 flips it. I never once fielded the double-诸事 board in-game.
2. 诸事不宜's -6atk (min-to-1) per incoming attack × 2 stacks is worth MORE than raw HP vs 崩拳, because 小布 attacks 2x/turn via chase (身法≥10 auto-chase from 闪击).
3. I held 修为 lead in mid-game but let it slip by ROLLING (25 rolls = -25 potential 修为) — final 修为 72 vs 小布 80 meant he had seat.
4. R2 sidejob 7 again (correct).

## NEXT-GAME
1. R2 sidejob = 7. FROM 境5: field THE double-诸事 recipe BY NAME. Before 境5: absorb-all, ZERO rolls.
2. KEEP-LIST (NEVER roll/absorb): 诸事不宜, 厄劫缠身, 杯弓蛇影, 命运轮回, 天星·牵引, 流水无情, 血光之灾, 吉运初显, 落花有意.
3. ★ NAMED rolls only, and STOP when a recipe piece appears. R11's 25-roll shotgun is the anti-pattern.
4. Target: 2× 诸事不宜 (the load-bearing card) + 1× 杯弓蛇影+1 + 1× 厄劫缠身 + 2× 命运轮回/吉运初显.

==== LEDGER ENTRY · Game 27 ====
==== LEDGER ENTRY · ARENA Game 27 ====
## ARENA Game 27 — 谭舒雁 (pid1), 命理师(sidejob 7). **RESULT: NOT 1st — final 命 0 (LAST place).** WINNER = 牧逸风 (pid0, 命59). 小布(pid3) eliminated 命0, me eliminated 命0, 吾行之(pid2) eliminated 命0.
W/L: W R1(3) L R2(2) L R3(3) L R4(2) L R5(3) L R6(0) L R7(2) L R8(0) L R9(2) W R10(0) L R11(3) W R12(0) W R13(2) L R14(0) L R15(2). Record 4W-11L. Started 1-1, then lost 8 of the next 9.
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 稳固根基, 副职兼修, 变换之道. (Economy/misc only — 17th straight confirmation combat/传承 fates are combat-IRRELEVANT for the 内伤 kit.)
Ended 境5 修为66 maxHP111 体魄0. Gates: 境2@R3, 境3@R6, 境4@R8, 境5@R11.

## FINAL BOARD (R15/R18, a LEFT-OVER PILE — the reason I lost):
['厄劫缠身','天星·牵引','落花有意','杯弓蛇影','流水无情','诸事不宜','反震心法','反震心法']
  = 1 real clock card (杯弓), 2 DEAD reflect cards (反震心法 ~0 dmg), and I had a SECOND 诸事不宜 in HAND that I never fielded.
  card_stats(R14 of a similar board): my cards did 5-6 dmg each while every rival's cards did 13-51. NOT A CLOCK.
  yisim vs 小布's FINAL board: 0%/0% (both seats). vs my CURRENT board.

## ★★★★★ ROOT CAUSE #1 (economy): TWO PRE-GATE SHOTGUNS + JUNK-ROLLS. (8th game, SAME failure) ★★★★★
Rolls/round: 0,0,0,0,0,0,0,1,**22**,7,**16**,4,6,4,3 ≈ 63 total.
  - R9=22 rolls at 境3 (PRE-境5!) — the classic M29 shotgun. Rolled 揽雀尾+1→御雷卦诀→落花有意→...→众星拱月→流水无情→...→卜命 — LANDED essentially NOTHING useful, burned 22 exchanges I could have ABSORBED for 修为.
  - R11=16 rolls at the 境5 gate (breakthrough grants a huge exchange surge — the TRAP again). Junk all the way.
  - Ended 修为66 vs 牧逸风 83 / 小布 85 → I LOST the seat AND had 17 fewer absorptions of stats.
  - 牧逸风 by contrast did ONE big dump (R12=26 rolls) but it LANDED his whole board; then R14-R18 mostly absorbed. Named/purposeful > volume.

## ★★★★★ ROOT CAUSE #2 (assembly): I HAD THE PIECES AND FIELDED JUNK. ★★★★★
At R18 hand = ['海底捞月','吉运初显','卜命+1','天星·牵引','紫气东来+1','凶象','诸事不宜','螳螂捕蝉','藕断丝连','藕断丝连','万事如意','诸事不宜'].
  → I literally held TWO 诸事不宜 + a 天星·牵引 + a 吉运初显 and 厄劫缠身/杯弓蛇影 on board. The full recipe was reachable; I fielded 反震心法×2 + 落花有意 instead.
  I never merged/collected a 命运轮回 (6 copies were drawable, 7.8%/deal!). I never merged 厄劫缠身→+1 (5 copies drawable).
  ★ LESSON: the loss this game was NOT "no pieces" — it was "did not ASSEMBLE / did not NAME-HUNT / did not field what I held."

## ★★★★★ TOP DISCOVERY [g27] — THE MASTER BOARD IS NOW 3-CLOCK, NOT 2-ClOCK. ★★★★★
  NEW MASTER (supersedes g26's double-杯弓):
  `['天星·牵引','厄劫缠身','杯弓蛇影','杯弓蛇影','诸事不宜','诸事不宜','命运轮回','杯弓蛇影']`
  yisim sim_matchup (3-5 reps, BOTH seats) vs ALL THREE rivals' EXACT final boards:
   vs pid0 牧逸风 (万法 qi-nuke):  100% first / 100% second
   vs pid2 吾行之 (水灵 heal-tank): 100% first / 100% second
   vs pid3 小布  (崩拳 burst):      **100% first / 100% second**  ← THE FLIP.
  ★ THE KEY MOVE: the THIRD 杯弓蛇影 (3 clock cards) flips 小布 from g26's "100%/0% going second" to "100%/100%". A search_board (locks 厄劫+杯弓+诸事, careers [7], 61 evals) explicitly found: replace a survival card with a 3rd 杯弓蛇影 → both seats. MORE CLOCK DENSITY BEATS MORE SURVIVAL vs a burst opponent — the clock must kill by t9-11, and 3 杯弓 cards (each: apply 2 内伤 + force enemy's 内伤 to tick immediately) accelerate the kill ~2 turns, which is exactly the margin vs 小布's t9-11 burst.
  Verified HOW it wins (full log vs 小布): 内伤 ticks 9-14/turn; 诸事不宜×2 holds his big hits to manageable (43/111 HP at t5); 命运轮回 +8HP; kill lands t9-11.
  Only loss = a HYPOTHETICAL fully-+1 rival board (unreachable — needs 4× copies; nobody fielded it).

## PER-RIVAL CAUSES (final boards):
- pid0 牧逸风 (云剑/阵法师5, qi-battery, 万法+1 one-shot, WINNER): 2W-4L. BEAT him R10/R12 — when my board had a real clock. LOST R6/R8/R14: my pile couldn't kill before his 白鹭/万法 burst (R14: his 白鹭灵剑 hit me 36 then 51 = 87 dmg over 2 turns). MASTER BOARD beats his final board 100/100.
- pid2 吾行之 (水灵 heal-tank, 阵法师5): 2W-2L (won R2? no — L R2, W R13...). Actually 1W-2L vs him. My EASIEST matchup (permanent 内伤 ignores his 防+heal). MASTER BOARD 100/100.
- pid3 小布 (崩拳 burst, 阵法师5, WINNER-material): 1W-4L. His t6-10 崩拳 burst + auto-chase (2 attacks/turn via 身法≥10) is the fastest kill. MASTER BOARD (3-clock) beats his final board 100/100 — the 3rd 杯弓 is the fix.

## SURPRISES:
1. I had ALL the pieces in hand at R18 (2× 诸事不宜!) and fielded 反震心法×2 — a pure discipline failure, not a draw failure. This is the FIRST game where the bottleneck was clearly ASSEMBLY DISCIPLINE, not availability.
2. 牧逸风's R12=26-roll 境5 dump WORKED (landed 聚灵心法+1/引气剑+1/百鸟灵剑诀+1) — so big 境5 dumps are fine IF named, but PRE-gate dumps (my R9=22) are pure waste.
3. The 3rd 杯弓蛇影 (not a 诸事不宜 or 命运轮回) was the decisive upgrade vs 小布 — clock density, not survival, was the missing piece.
4. 反震心法 (reflect 2/turn) is a TRAP card for me — 0 real contribution; card_stats repeatedly shows it doing nothing.

## NEXT-GAME RULES (sharpened from g25/g26/g27):
1. R2 sidejob = 7 (命理师). Board = CLOCK + SURVIVAL, never a pile.
2. ★★ NEVER roll before the 境5 gate. R1-R10 = ABSORB-ALL junk for 修为 (M29/M63, 8th confirmation — my R9=22 fired here).
3. ★★ At 境5: NAME-HUNT (厄劫/杯弓/诸事/命运/天星·牵引/吉运), CAP 4-6 rolls/round (M67), STOP the instant a piece lands.
4. ★★ When you HOLD the pieces, FIELD THE RECIPE. At R15+ always check hand for a 2nd 诸事不宜 / 3rd 杯弓 before fielding ref时.
5. TARGET BOARD: ['天星·牵引','厄劫缠身','杯弓蛇影','杯弓蛇影','诸事不宜','诸事不宜','命运轮回','杯弓蛇影'] (3 clock + 2 诸事 + 牵引 + 命运).
6. KEEP-LIST (never roll/absorb): 杯弓蛇影, 厄劫缠身, 诸事不宜, 命运轮回, 天星·牵引, 吉运初显, 流水无情, 血光之灾, 落花有意.
7. BAN-LIST (never field): 反震心法 (0 contribution), 海底捞月 (白板 without setup).
8. Bank exchanges R13-R15, mass-MERGE doubles R16+ (厄劫缠身+1 is reachable — 5 copies in pool).
9. Per-rival: 牧逸风→race his 白鹭/万法 burst, need 2 诸事不宜 + 命运轮回 HP. 小布→3-clock density is the fix (100/100). 吾行之→free win.

==== LEDGER ENTRY · Game 28 ====
## ARENA Game 28 — 谭舒雁 (pid1), 命理师(sidejob 7). RESULT: NOT 1st — final 命 0 (eliminated). WINNER = 牧逸风 (pid0, 命1, last-man-standing by ONE point). 谭舒雁/吾行之/小布 all 命0.
W/L: W R1(0) L R2(3) L R3(2) W R4(0) W R5(3) W R6(2) L R7(0) W R8(2) L R9(0) L R10(2) L R11(3) L R12(2) L R13(3) L R14(0). Record 5W-9L. 3-0 open (R1/R4/R5/R6) then collapsed 1-6 late. Eliminated R14 vs 牧逸风 (-24命).
FATES (境2→境5): 勤学苦练, 顿悟, 稳固根基, 雁影化身, 斩断俗尘. (18th straight confirmation: combat/传承 fates are IRRELEVANT for the 内伤 kit — simulate(my_extra_fates=[1]) and [101] gave IDENTICAL output, kill t11 both ways.)
Gate pacing: 境2@R3, 境3@R5, 境4@R8, 境5@R12 (via absorb; 修为55 at R12). Ended 境5 修为68 maxHP109. Slower than 小布(境5@R12, 修为90) but similar to 牧逸风(R13).

## FINAL BOARD (R14, the pile that lost 0%/0% to everyone):
['星弈·断','落雷术+1','海底捞月','金鸡独立','星弈·立','星弈·挡','螳螂捕蝉','轰雷掣电']
card_stats(R14): total ~57 dmg over 13 turns (星弈·断 28, 落雷 10, 星弈·立 5, 星弈·挡 4, 海底捞月 0, 金鸡 0, 螳螂 0, 轰雷 0). THIS IS NOT A CLOCK. 4 of 8 slots did ZERO. It was a 星力/卦象 ATTACK mishmash — NOT my 内伤 kit.

## ★★★★★ ROOT CAUSE #1 (8th+ time, SAME failure): NEVER ASSEMBLED THE 内伤 CLOCK. ★★★★★
At R14 my POOL held 厄劫缠身×6, 杯弓蛇影×6, 诸事不宜×8, 命运轮回×6, 天星·牵引×8, 血光之灾×8, 落花有意×8. I fielded the wrong cards (星弈/落雷) AND my economy_history shows I ROLLED AWAY the kit repeatedly: R13 rolled 诸事不宜->兑卦 (THREW AWAY 诸事不宜!), R11 rolled 天星·牵引->气疗术, 星弈·虎->斗转星移. R14 rolled 黄雀在后->落花有意 (kept), 梅开二度->紫气东来.
Rolls/round: 0,0,0,0,0,5,0,4,2,21,3,6,7 ≈ 48. The R11=21 was a shotgun that hit nothing (rolled past 星弈·虎, 天星·牵引, 诸事不宜-related). R13/R14 fired but LANDED junk while I had the whole kit in pool.
Ended 修为68 vs 牧逸风 91 / 小布 90 → lost seat AND 20+ absorptions.

## ★★★★★ TOP DISCOVERY [g28]: DOUBLE 厄劫缠身 (SLOT-2 ENGINE-STARVE) BEATS 牧逸风'S 万法 NUKE. ★★★★★
My g26/g27 notebook recipe ['天星·牵引','厄劫缠身','杯弓蛇影','杯弓蛇影','诸事不宜','诸事不宜','命运轮回','杯弓蛇影'] LOSES to 牧逸风 (-29命, t7) and to 小布 -24 (t11) — SINGLE 厄劫 is not enough.
★ THE FIX (search_board + yisim, 5 reps):
  ['天星·牵引','厄劫缠身','杯弓蛇影','杯弓蛇影','诸事不宜','诸事不宜','厄劫缠身','命运轮回']
  → yisim sim_matchup vs ALL THREE rivals' ACTUAL final boards: **100% first / 100% second EACH.**
   vs pid0 牧逸风 (万法 qi-nuke): 100/100 (~10-11t). vs pid2 吾行之 (水灵 tank): 100/100 (~10-11t). vs pid3 小布 (崩拳 burst): 100/100 (~10-11t).
★ MECHANISM (verified in full log): 厄劫缠身's [开局] targets the OPPONENT'S CARD IN THE SAME SLOT. My SLOT-2 厄劫 downgrades his SLOT-1 聚灵心法+1 (lv2 = +1 qi EVERY turn, doubled by 回响阵纹) → to lv1 (=+1 qi every 2 TURNS). That HALVES his qi ramp, so 万法 deals only **75** instead of **89** — survivable; I end at 2 HP, then the clock wins t11.
★ ORDER IS LOAD-BEARING: moving the engine-starve 厄劫 off slot 2 (e.g. to slot 8) → LOSE (-29/-31, 万法 fires 79-89). Put 厄劫 at slot 8 to target 万法 itself → ALSO LOSE (downgrading 万法 doesn't stop the qi; it fired 89). The WIN comes from starving the QI ENGINE, not the nuke.
★ Third 厄劫 or 杯弓+1 → search found even more margin; 五雷轰顶(slot8) variant gets 100/100 as-is AND 33% vs 小布+1 (better than 0%). But the minimal all-lv1 board is the reachable one.

## PER-RIVAL CAUSES (final boards):
- pid0 牧逸风 (云剑+阵法师5, 聚灵+回响 双灵气→万法归灵剑 75-89 dmg one-shot at t7): 1W-4L (won R1 early). LOST R9,R10,R14 when my board was a pile. His 万法 killed me t7/t9/t13. DOUBLE-厄劫 BOARD beats his actual board 100/100 both seats.
- pid2 吾行之 (水灵 heal-tank, 阵法师5, 水势 ramp + 巡林 chase): 1W-1L (W R6, L R3/R10). Tank; my clock would out-race him. DOUBLE-厄劫 BOARD 100/100.
- pid3 小布 (崩拳 burst + 体魄 48 + 身法 chase, 阵法师5): 1W-4L (W R5, L R2/R11/R13). His burst + auto-chase kills t6-7. DOUBLE-厄劫 BOARD beats his ACTUAL board 100/100 (clock 8→12→16 + 诸事 mitigation). His +1-everything board (173 HP) is UNBEATABLE (0%) — but unreachable (needs 4 copies of each).

## SURPRISES:
1. 牧逸风 won the lobby on 命1 — it was razor thin. A working board (which I HAD the pieces for) would have flipped it.
2. 小布's final board was FAR stronger than in my old notes (173 HP, 48 体魄, 惊触+1) — but my double-厄劫 clock still beats it 100/100.
3. The 万法 nuke is beatable by ENGINE DISRUPTION (slot-2 厄劫 downgrade of 聚灵心法), not by more survival. This is a NEW category of answer for me.
4. 五雷轰顶 (a 境5 雷 card) at slot 8 works with the clock — alternative finisher.

## NEXT-GAME RULES (sharpened):
1. R2 sidejob = 7 (命理师). Board = CLOCK + SURVIVAL + ENGINE-DISRUPT, never a 星弈/落雷 pile.
2. ★★ NEVER roll a KEEP-LIST card. This game I rolled away 诸事不宜 (R13) and 天星·牵引 (R11) — inexcusable. KEEP-LIST: 厄劫缠身, 杯弓蛇影, 诸事不宜, 命运轮回, 天星·牵引, 血光之灾, 落花有意, 吉运初显.
3. ★★ NEVER roll before 境5. R1-R11 = ABSORB-ALL (0-2 rolls/round max). My R11=21 shotgun was pure waste (rolled past 星弈·虎/天星·牵引).
4. ★★ TARGET BOARD (all lv1, reachable): ['天星·牵引','厄劫缠身','杯弓蛇影','杯弓蛇影','诸事不宜','诸事不宜','厄劫缠身','命运轮回'] — 100/100 vs all three ACTUAL final boards.
5. ★★ 厄劫缠身 at SLOT 2 = engine-starve (targets opp slot-1 qi engine). This is LOAD-BEARING vs 牧逸风. NEVER move it.
6. BAN-LIST (never field): 反震心法 (0 contribution), 海底捞月 (白板), 星弈·断/轰雷掣电 as generic fillers (a 星弈/落雷 pile does ~57 dmg/13t = no clock).
7. Bank exchanges ≤24 pre-grant; absorb junk for 修为 (seat). Broke 境5 R12 = 1-2 rounds late; aim R10-R11.

==== LEDGER ENTRY · Game 29 ====
==== LEDGER ENTRY · ARENA Game 29 ====
## ARENA Game 29 — 谭舒雁 (pid1), 命理师(sidejob 7). **RESULT: 1st PLACE / WINNER — final 命 87.** Others all 命0: 牧逸风(pid0), 吾行之(pid2), 小布(pid3).
W/L: L R1(vs0,-3) W R2(vs2,-5) W R3(vs3,-6) W R4(vs0,-6) W R5(vs2,-9) W R6(vs0,-9) L R7(vs2,-8) W R8(vs3,-11) W R9(vs2,-16) W R10(vs0,-18) W R11(vs3,-18) W R12(vs0,-19) L R13(vs2,-20) W R14(vs3,-11) W R15(vs2,-23) W R16(vs3,-22) L R16(vs2,-23) W R17(vs2,-2) W R18(vs2,-29). Record 15W-3L (last three losses all pre-kit muddle boards; the kit went 11-1 once online).
FATES (境2→境5): 勤学苦练, 感悟丛生, 休养生息, 雁影化身, 斩断俗尘. (economy/misc only — 19th straight confirmation combat/传承 fates are combat-irrelevant for the 内伤 kit).
Gates: 境2@R3, 境3@R5, 境4@R8, 境5@R12 (修为55). Ended 境5 修为92 (HIGHEST in lobby) maxHP109. **修为 92 beat 牧逸风74/吾行之79/小布79 → I WON EVERY SEAT → won the game.** CP4 (absorb junk for 修为=seat) was the single biggest factor this game.

## FINAL BOARD (fielded R17/R18):
['天星·牵引','血光之灾','杯弓蛇影','杯弓蛇影','诸事不宜','诸事不宜','星弈·断','反震心法+1']
Sim vs all 3 actual final boards: 100% first / 0% second (seat-decisive in EVERY matchup).

## ★★★★★ TOP DISCOVERY [g29]: THE TRUE UNIVERSAL MASTER BOARD — ALL lv1, ALL CARDS I HELD. ★★★★★
  ['杯弓蛇影','血光之灾','杯弓蛇影','天星·牵引','诸事不宜','诸事不宜','流水无情','星弈·断']
  yisim sim_matchup (5-8 reps): vs pid0 牧逸风 100/100, vs pid2 吾行之 100/100, vs pid3 小布 100/100.
  **BOTH SEATS, no upgrades, ~11-13t.** vs my fielded board (100/0 seat-locked) this is strictly better.
  ★ THE THREE FIXES vs my fielded board:
    (1) SWAP 反震心法+1 → **流水无情** (6atk + if opp has any debuff apply 2 内伤; my 内伤 IS a debuff, so it always fires).
    (2) MOVE 天星·牵引 slot1 → **slot 4**. Its trigger fires the [开局] of the 2 slots AFTER it; at slot 4 it triggers
        诸事不宜×2 [开局][防]+4 (SURVIVAL), at slot 1 it triggers damage openings. Puts mitigation where burst hits.
    (3) 星弈·断 → **slot 8**.
  ★ REACHABILITY: I held EVERY piece — 流水无情 was fielded R9-R16 then ABSORBED R16 (fatal); 天星·牵引 in HAND
    at R18; 2× 杯弓 + 2× 诸事不宜 + 血光 + 星弈·断 all on board. Assembly-discipline failure AGAIN (matches g27/g28).
  ★ MECHANISM (full log vs 小布 100/100 first): 内伤 ticks 3→5→7→9/turn; 诸事不宜 clipping his big hits; I end 19/109 HP.
    vs 牧逸风 (100/100 first): his 万法 never lands a killing nuke; 内伤 kills t12, I end 53/109 HP.

## ROLL / ECONOMY NUMBERS (rolls per round): 0,0,0,0,0,0,0,1,**21**,0,0,**15**,0,11,8,6,6,5 ≈ 73 total.
- R9=21 rolls at 境3 = the M29 PRE-境5 SHOTGUN for the **9TH CONSECUTIVE GAME**. It only "worked" by luck (landed 诸事不宜, 血光之灾) — it burned 21 exchanges that should have been 修为. THIS IS MY #1 LEAK, STILL UNFIXED.
- R12=15 rolls at the 境5 gate (breakthrough exchange surge trap, landed nothing).
- Post-境5: R14=11, R15=8, R16=6, R17=6, R18=5 — landed the clock at R16/R17 but SO LATE I fielded 反震+1 instead of assembling.
- 厄劫缠身 (境5, 6 copies, 2.7%/roll) was NEVER DRAWN all game — the anti-牧逸风 silver bullet was absent, yet I still won on seat+clock.

## PER-RIVAL (final board, one-line cause):
- pid0 牧逸风 (云剑+阵法师5, 聚灵+回响→万法 qi-nuke): 5W-1L (only R1 loss, pre-kit). MASTER BOARD beats him 100/100.
- pid2 吾行之 (水灵 heal-tank, 阵法师5): 4W-3L (R7/R13 losses pre-kit; R16 loss). MASTER BOARD 100/100 both seats.
- pid3 小布 (崩拳 burst + 体魄, 阵法师5): 4W-0L. My 内伤 clock + 诸事 mitigation outraced his burst. MASTER BOARD 100/100 both seats.

## SURPRISES:
1. I WON the lobby despite my board being only 2/3 optimized — because 修为 92 won every seat and the seat decided every matchup. Seat discipline carried a suboptimal board.
2. The seat-decisive finding (100/0 in all 3 matchups) is NEW and consistent across all four bots' notebooks — the whole lobby is playing a seat war.
3. 流水无情 is the missing 8th clock slot — 6 copies in pool, every prior game I ignored it. It self-synergizes with my whole kit.
4. 天星·牵引's slot choice is a SURVIVAL-vs-CLOCK dial (slot1=damage openings, slot4=防 openings). Non-obvious.
5. 反震心法 / 反震心法+1 = BAN (card_stats: 0 contribution in R18 again — 3rd game confirming).

## NEXT-GAME: R2 sidejob=7. ABSORB-ALL pre-境5, ZERO shotgun rolls (kill the R9≈21 leak). Break 境5 R11-12.
Post-境5 target board = the MASTER BOARD above (KEEP 流水无情, NEVER absorb it). 厄劫缠身 if drawn → slot 2 (engine-starve).

==== LEDGER ENTRY · Game 30 ====
==== LEDGER ENTRY · ARENA Game 30 ====
## ARENA Game 30 — 谭舒雁 (pid1), 命理师 (sidejob 7). **RESULT: 1st PLACE / WINNER — final 命 10.** Others all 命0: 牧逸风(pid0), 吾行之(pid2), 小布(pid3).
W/L (18 battles): W R1(0) W R2(3) L R3(2) L R4(3) W R5(2) L R6(0) L R7(2) W R8(3) W R9(0) L R10(3) W R11(0) W R12(3) W R13(2) W R14(0) W R15(2) W R16(0) L R17(3) W R17(0) L R18(3) W R19(3). Record 12W-6L. Won R19 (must-win, 命10 vs 小布 命1) 8t going FIRST.
FATES (境2→境5): 勤学苦练, 飞鸿踏雪, 雪羽清风, 雁影化身, 妙手回春. (**21st straight confirmation**: combat/传承 fates are combat-irrelevant — simulate(my_extra_fates=[1,101]) gave IDENTICAL kills (t7, same HP) again this game.)
Gates: 境2@R3, 境3@R5, 境4@R8, 境5@R12 (修为55). Ended 境5 **修为105 — HIGHEST in lobby** (牧逸风86/小布91/吾行之80) → won EVERY seat. maxHP 117.
**修为 105 carried the lobby**: my board was seat-dependent (100%-first/0%-second vs 小布 pre-fix), and I went FIRST in every decisive late round because I out-absorbed everyone.

## FINAL BOARD (fielded R19, WON):
['诸事不宜','厄劫缠身','杯弓蛇影','杯弓蛇影','天星·牵引','星弈·断+1','流水无情','吉运初显']
= 厄劫 at SLOT2. 100%-first / 0%-second vs 小布; 100/100 vs 牧逸风/吾行之.

## ★★★★★ TOP DISCOVERY [g30]: 厄劫缠身 at SLOT 1 (not slot 2) → 100%/100% vs ALL THREE RIVALS. ★★★★★
★ THE FIX (sim_matchup, 5-20 reps):
  ['厄劫缠身','诸事不宜','杯弓蛇影','杯弓蛇影','天星·牵引','星弈·断+1','流水无情','吉运初显']
   → vs pid3 小布 100% first / **100% second** (was 0% second!). vs pid0 牧逸风 100/100. vs pid2 吾行之 100/100.
   → ALSO beats 小布's REAL R19 board WITH its +1s (威震四方+1/连崩+1/突+1): 100 first (t7) / 100 second (t9). VERIFIED.
★ MECHANISM (engine source gamestate_full.js:5994-5998): 厄劫's [开局] calls `downgrade_enemy_card_or_deal_damage`,
   which uses `currently_triggering_card_idx` — i.e. it targets the OPPONENT'S CARD **AT THE SAME INDEX AS MY 厄劫's slot**.
   - slot1 厄劫 vs 牧逸风: downgrades his slot1 聚灵心法+1 → lv1 = STARVES THE QI ENGINE (万法 fires ~75 not 89). [g28 discovery, re-confirmed]
   - slot1 厄劫 vs 小布: front-loads the clock (4 内伤 + 6 dmg fired FIRST each cycle instead of after a 诸事不宜 whiff).
   - slot2 厄劫 vs 小布: targets his slot2 威震四方+1 (downgrades）... but leaves the clock a beat late → loses the SECOND seat.
★ LOAD-BEARING ORDER (tested): 厄劫 MUST be slot1. 诸事不宜 MUST be slot2 (swapping it to slot3 → 100/0, loses second seat).
   杯弓 can be slot3 or 4. 天星·牵引 slot4/5. Last 2 slots flexible (流水无情/反震心法/命运轮回/落花有意/探灵 ALL give 100/100).
★ 反震心法 is NOT a hard "BAN" (my old note g27/g28/g29): at slot7 it gave 100/100 vs 小布 (its +4 maxHP + 2 reflect/hit is real sustain).
   Downgrade that BAN to "situational slot7/8 filler" — it still underperforms 流水无情 on damage but is not 0-contribution.

## ★ SEARCH TRACES (Phase 4):
- search_board(opp=3, pool=[7]) from the slot1 board: NO improvement over start (local optimum). Confirms the board is best-in-class as-is.
- search_board(opp=0): same — only marginal level-ups (杯弓+2, 断+2). The +1-LOBBY case (all 8 upgraded) stays 0% and is UNREACHABLE (needs 4 copies/card).

## PER-RIVAL (final boards, one-line cause):
- pid0 牧逸风 (云剑+阵法师5, 聚灵+百鸟→万法归灵剑 qi-nuke): 4W-2L (lost R6 pre-kit, R17 when my clock was 1 tick short). slot1-厄劫 STARVES his 聚灵 engine → his 万法 never one-shots; my 内伤 kills t11-12.
- pid2 吾行之 (水灵 heal-tank, 阵法师5): 3W-2L (R3/R7 early pre-kit). My clock out-competes his ramp; slot1-厄劫 100/100.
- pid3 小布 (崩拳 burst + 体魄, 阵法师5): 4W-3L (R4/R10/R18 losses). LOST R18 going FIRST by 4 HP (t7 崩拳·突+1 hit for 28). My new slot1-厄劫 board flips this to 100/100.

## ★ ECONOMY (my rolls/round): 0,0,0,0,0,0,0,0,6,2,4,**17**,0,0,0,0,1,0,0 ≈ 30 total. **BEST ECONOMY OF ANY GAME SO FAR (was 48-73).**
- R1-R8: ZERO rolls (pure absorb-all for 修为). R9=6, R10=2, R11=4 = light pre-境5 noise.
- **R12=17 = the pre-境5-gate shotgun (11th consecutive game with this leak)** — but it LANDED 诸事不宜 (the mitigation keystone!) AND 杯弓蛇影 (the clock!). So the shotgun "worked" by luck. It also burned exchanges that should have been 修为.
- Post-境5: R13-R19 ≈ 1 roll total. Banked at 25 most rounds (grants wasted at cap — but banked exchanges served no purpose once board was set; fine).
- ★ LESSON: the 修为-first discipline (0 rolls R1-R8) is what won me 修为105 → every seat. KEEP. The R12=17 shotgun is the ONE remaining leak: NAME it (roll for 诸事不宜/杯弓蛇影/厄劫缠身 only) and cap at ≤8.

## SURPRISES:
1. The ONE-SLOT fix (厄劫 slot2→slot1) flips 0%-second → 100%-second vs 小布 for FREE. All my prior games I put 厄劫 at slot2 (targeting the qi engine). Slot1 is strictly better because it ALSO front-loads the clock.
2. I won with a board that was ONLY seat-dependent pre-fix — 修为105 + luck of going first. The slot1 fix would have made it seat-INDEPENDENT. Assembly/positioning discipline again.
3. 小布's final board DID have +1s (威震四方+1/连崩+1/突+1) and STILL lost 0/0 to my slot1-厄劫 board both seats — the "+1 lobby beats me" fear is overblown for realistic partial upgrades.
4. My best-ever economy (30 rolls) came with my only WIN. 修为 discipline = seat = wins.

## NEXT-GAME RULES (sharpened):
1. R2 sidejob = 7 (命理师). ABSORB-ALL R1-R11 (0-2 rolls). Break 境5 R11-12. 修为 = seat = win.
2. ★★ MASTER BOARD (all lv1, reachable): ['厄劫缠身','诸事不宜','杯弓蛇影','杯弓蛇影','天星·牵引','星弈·断','流水无情','吉运初显']
   → 厄劫 SLOT1, 诸事不宜 SLOT2 — both POSITION-LOAD-BEARING. NEVER swap them.
3. KEEP-LIST (never roll/absorb): 厄劫缠身, 杯弓蛇影, 诸事不宜, 天星·牵引, 流水无情, 血光之灾, 命运轮回, 吉运初显, 落花有意.
4. The pre-境5 R12 shotgun: NAME-HUNT {诸事不宜, 杯弓蛇影, 厄劫缠身, 天星·牵引} only, ≤8 rolls.
5. 反震心法 = situational slot7/8 (not a hard ban). 海底捞月 still a ban (白板).
