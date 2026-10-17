# 吾行之 — game ledger (append-only archive)

==== LEDGER ENTRY · Game 13 ====
g13 吾行之 (water/五行 sect), sidejob=5 阵法师. RESULT: LOST — placed not-first, final 命 0 (lost R14 vs 小布, -22命, self-execution after accumulating losses). 修为 ended 57, 境5, maxHP 101. Fates taken across gates: 战斗历练, 五行印记, 悠然葫芦, 五行化身, 五行传承.

FINISHED R14 BOARD (the blunder board): 水灵印+2, 水灵·波澜+1, 水灵·泉涌+1, 水灵·潜遁, 水灵·汹涌+2, 八门金锁阵, 天罡聚力阵, 木灵·复苏. Only 汹涌+2 dealt damage (21); other 7 slots ≈ 0 dmg.

PER-RIVAL W/L (this game): vs pid3 小布 (崩拳) 1W-3L (Won R12 barely, Lost R2/R4/R6 tight, Lost R14 the fatal one). vs pid1 谭舒雁 (命运/内伤 debuff) 1W-4L — she hard-counters. vs pid0 牧逸风 (云剑 burst) 1W-4L — he hard-counters.

TOP DISCOVERY (evidence): 牧逸风's cloud-sword deck is a STRUCTURAL counter to 吾行之 water — yisim search over my whole pool (careers 1/5/7, 200 evals) returns 0% BOTH seats, base AND +1. He bursts 107 HP down in 6-7 turns with 飞灵闪影剑 (7dmg×5) + 巨鲸/巨鹏/巨鲲 chase chain; water can't out-sustain or out-race. Same for 谭舒雁's 内伤 stack deck (0% both seats). ONLY 小布 is winnable: engine board 水灵印+2,水灵阵,水灵·泉涌+1,水灵·腾浪+1,水灵·潜遁,水灵·腾浪,水灵·汹涌+2,须弥阵纹 = 100%/100% vs 小布 (search-verified, 3 reps).

ECONOMY NUMBERS: rolls spent per round R1-3:0, R4:13(!), R5:4, R6:3, R7:3, R8:5, R9:3, R10:4, R11:3, R12:5, R13:0, R14:14(!!). Over-rolled R4 (13) and R14 (14) hunting junk; NEVER found the engine pieces 须弥阵纹/腾浪/纳百川/涛 despite 60 rolls. Under-hit: the draw pool has 8 copies each of 水灵阵/泉涌/腾浪/须弥阵纹 — they were findable; I just took junk rolls.

SURPRISE #1 (biggest): In R12 my 6-card pure-water board (印/波澜+1/泉涌+1/汹涌+1/汹涌/汹涌) beat 小布. In R13-R14 I took 汹涌 pieces back and MERGED three 水灵·汹涌 into one 汹涌+2, then filled the freed slots with 八门金锁阵/天罡聚力阵/木灵·复苏 — all 0-damage. VERIFIED: my R14 board = 0% going second vs 小布; the un-merged 6-card board = WIN (-26命) going second. MERGING attackers to fill with dead utility is a NET LOSS.
SURPRISE #2: 水灵·潜遁 (-40% attack taken) DOES help vs 小布 when positioned right (search moved it to slot 5 and won 100/100), even though much of 小布's damage is HP-cost/chase-based.
SURPRISE #3: 牧逸风's 飞灵闪影剑 hits 7 dmg FIVE times (chase on the card) — this is the finisher, and 防 doesn't cut it (each hit separate).

==== LEDGER ENTRY · Game 14 ====
# Game 14
g14 吾行之 (五行/金灵 board this time), sidejob=5 阵法师, 境5, 修为72, maxHP 103. RESULT: LOST — not first, final 命 0 (R15 vs pid0 牧逸风, -21命). Record 6W-9L overall; died to 牧逸风 (0% counter).

FATES taken: 战斗历练, 感悟丛生, 五行循环, 储纳灵气, 五行传承 (all generic-ish; 五行传承 taken at 境5 = economy only).

FINISHED BOARD (R15, the blunder board): 金灵阵+1, 金灵·蓄锐+1, 金灵印+1, 金灵·巨鼎落, 金灵·巨鼎落, 金灵·穿心+1, 金灵·针+1, 五行刺+1. Matrix: 0% vs EVERYONE, both seats (base AND +1). This board was structurally dead.

★ TOP DISCOVERY (corrects g13 ledger!): g13 said "water is 0% vs 牧逸风/谭舒雁 BOTH seats" — that is FALSE as a universal. This game I built metal (wrong) and lost; but a WATER board assembled from pieces I ACTUALLY HELD (水灵阵, 泉涌+1, 腾浪+1, 纳百川, 波澜+1, 汹涌, 水灵印+1, 须弥阵纹) WINS 100% first / 100% second vs 牧逸风's R15 board (~10t), verified sim + sim_matchup. Evidence: simulate full_log showed 纳百川 +32 maxHP → 156HP tank, then 汹涌 29 dmg finisher. So the correct doctrine is: WATER ENGINE ALWAYS; metal cannot beat the field. The g13 "avoid 牧逸风" claim was an artifact of a badly-assembled water deck, not a structural truth.

★ MISTAKE M1 (the fatal one): I DREW the water engine pieces across R13-R15 (须弥阵纹 R13; 水灵·腾浪×2 + 周天剑阵 R14; 水灵·涛/波澜/泉涌/纳百川 R15) and ABSORBED almost all of them for 修为 (R15: absorbed 须弥阵纹, 腾浪+1, 波澜, 泉涌 — FOUR engine pieces burned!). I was committed to metal since R11 and refused to pivot when the water pieces arrived. FIX: when 3+ water engine pieces land in hand, PIVOT THE BOARD regardless of sunk cost. The picklist cards are win-cons, not 修为.

★ MECHANICS verified: 水灵·波澜 lv2 = 3 [水势], costs 0 qi with [水灵] active — free stack builder. 水灵·涛 = 10atk +1 水势 (an attacker that also builds). 须弥阵纹 = [跳过] next card + chase if a 持续 was played; put it LAST after 水灵阵 (持续) resolves. do_force_of_water() (gamestate_full.js:3198) = 汹涌/波涛 deal force_of_water as bonus dmg. 纳百川 adds 6+水势 maxHP, so it both tanks AND feeds the next 汹涌.

ECONOMY: rolls R1:2 R2:4 R3:3 R4:5 R5:3 R6:4 R7:6 R8:2 R9:7 R10:4 R11:4 R12:6 R13:0 R14:0 R15:16(!!). R15 I burned 16 rolls at 命-critical moment finding nothing relevant while holding water pieces. Over-roll pattern: I roll heavily exactly when I've already committed to a doomed plan. Bank never exceeded 14 → grant waste minor.

PER-RIVAL: vs 牧逸风 (云剑 burst) 1W-4L — HARD; but water beats his base board 100/100 (proven). vs 谭舒雁 (内伤) 0W-3L — counters passive decks; water's big HP helps but 内伤 ignores HP volume. vs 小布 (崩拳 HP-cost burst) 3W-2L — WINNABLE if I stay ahead; his FULLY UPGRADED board (饿虎扑食 lv3 = 39dmg post-HP-cost + 磅礴之势 chase) is 0% even for optimized water going second; his BASE board is 100/100 for water. Race him before he levels.

SURPRISE: 小布's 饿虎扑食+2 does 39 damage to me on turn 7 — his HP-cost burst scales hard with level. Also 牧逸风's 巨鹏→巨虎 chase plays BOTH in one turn (清chase), the finisher.

==== LEDGER ENTRY · Game 15 ====
g15 R10 (吾行之, sidejob=5 阵法师):
- KEY DISCOVERY: reordering the water board so 水灵·波澜 fires IMMEDIATELY after 水灵阵 (2nd slot) and the 汹涌 PAYOFF fires LAST (8th slot) flipped a 50% board into 100%/100% (both seats) vs 牧逸风's known board (~8t). Original order (印→阵→波澜→涛+1→汹涌+1→涛×3) only won going-first (100%/0%). LESSON: 水势 ramp early (波澜 free 2 stacks), payoff late = max dmg. Slot order is decisive.
- Best board R10: [水灵阵, 水灵·波澜, 水灵印+1, 水灵·涛, 水灵·涛, 水灵·涛, 水灵·涛+1, 水灵·汹涌+1] = 100/100 base, 0/0 vs full +1 (his +1 out-races in 6t; unwinnable ceiling, ignored).
- Economy: started 5 exch. Rolled 木灵·暗香->碎杀阵, 龟甲阵->水灵·汹涌 (HIT, kept), then 聚灵阵->火灵·瞬燃, 浑天印->金灵·铁骨, 金灵·穿心->木灵·疏影. STOPPED on 汹涌 hit.
- Absorbed 4 junk (碎杀阵/瞬燃/铁骨/疏影) -> 修为 38->42. WHY: breaks the 38-38 seat tie vs 牧逸风 so I ACT FIRST — critical since board is seat-sensitive. Kept 水灵·汹涌 in hand (picklist, never absorb).
- Board has 1 [持续] (水灵阵) — legal.
- vs 牧逸风: his board is sword-intent burst (引气剑/点星/飞牙剑/破气剑) + 巨鹏灵剑->chase. No defense until 地煞剑 turn 7. Out-race him with water.

==== LEDGER ENTRY · Game 15 ====
==== LEDGER ENTRY · Game 16 ====
g16 吾行之 (五行 sect, WATER board), sidejob=5 阵法师, 境5, 修为76, maxHP 105. RESULT: LOST — not first, final 命 0. Record ~7W-9L. Fates: 战斗历练, 五行印记, 悠然葫芦, 五行化身, 顿悟.

FINAL BOARD (R16, the losing board): 水灵阵, 水灵·波澜, 水灵·腾浪, 水灵·涛+1, 水灵·涛+1, 水灵·汹涌+1, 水灵·汹涌, 冲击阵纹.
  Matrix: vs 牧逸风 0%/0%; vs 小布 100% first / 0% second (base), 0% both vs +1. Died R16 to 小布 (-18) then pid0 (-19 tiebreak).

★ TOP DISCOVERY (evidence): **水灵·纳百川 (Combine Rivers) is THE missing engine piece. Adding it flips my board from 0%/0% to 100%/100% vs 牧逸风's R16 board AND 100%/100% vs 小布's base (sim_matchup, 3 reps).** Full log: 纳百川 at 水势 18 gave +24 maxHP (46→70hp, 142 max), absorbing 牧逸风's 巨鹏→巨鲲 chase chain; then 汹涌+1 finished. This is the tank that survives burst. I NEVER had it on board all game, and NEVER rolled for it despite it being a 境5 五行-sect card (6 copies in pool).

CANONICAL BEST WATER BOARD (g16-verified): 水灵阵, 水灵·波澜, 水灵·纳百川, 水灵·泉涌, 水灵·腾浪, 水灵·涛+1, 水灵·涛+1, 水灵·汹涌+1 = 100%/100% vs 牧逸风 base, 100%/100% vs 小布 base, ~100%/100% vs 谭舒雁 base. ORDER: 阵 first (持续 battery), 波澜 next (free 2 水势), 纳百川 early (tank), 泉涌/腾浪 (qi+水势), 涛/汹涌 PAYOFF at end.

★ MISTAKE M1 (fatal, repeats g14's M1): UNDER-rolled at 境5. Economy: R13:0, R14:0, R15:2, R16:2 rolls — exactly when I was ONE piece (纳百川) from a 100% board. I BANKED instead (R15 ended at 25 = CAP, wasting the R16 grant; R16 ended 23). The 25-cap rule: at/above 25 you get NOTHING at round start. FIX: at 境5 with a near-complete board, spend 5-8 rolls/round hunting the last picklist pieces; NEVER bank to 25.
★ MISTAKE M2 (repeats CP6): absorbed 水灵·泉涌 at R15 for +1 修为 (an engine piece!). FIX stands.
★ MISTAKE M3 (CP2): padded board with 冲击阵纹 (6atk, weak) instead of fielding more water attackers / empty slots.

PER-RIVAL: vs 牧逸风 (云剑/巨剑 burst, 巨鹏→巨鲲→chase): HARD but BEATABLE with 纳百川 tank (0%→100% once added). Lost R5,R8,R10,R12. vs 小布 (崩拳 HP-cost burst + permanent 内伤 via 血光之灾/修罗吼): WINNABLE, won R3,R4,R6; lost R9,R14,R16 by TINY margins (R14 died at 8a with 2hp; R16 with 8hp) — 纳百川's HP tank flips these. vs 谭舒雁 (命运/内伤 clock): won R15 (raced her, 汹涌 killed her turn 11), lost R2,R11.

SURPRISE: 水灵·纳百川 HP scales with 水势 stacks — at high 水势 it's +20-32 maxHP, a MASSIVE combined tank+attacker-feed. Water's whole identity is 水势: 纳百川 converts 水势→HP, 汹涌 converts 水势→damage. Both are needed; I only had 汹涌.

ECONOMY NOTES: rolls R1:0 R2:7 R3:4 R4:3 R5:6 R6:1 R7:6 R8:7 R9:2 R10:5 R11:0 R12:0 R13:0 R14:0 R15:2 R16:2. Pattern: I rolled heavy R2-R10 then STOPPED rolling R11-R16 exactly when the 境5 pool (with 纳百川/须弥阵纹) opened. Banked to 25 cap at R15 = wasted grant.

==== LEDGER ENTRY · Game 16 ====
g17 (吾行之, sidejob 5 阵法师) — R7 vs 谭舒雁 (pid1, 命运/内伤 clock).
STATE: 命90, 修为25, 境3, HP64. Board metal (never drew a water engine: only 水灵印/波澜/涛+1 in hand; NO 水灵阵, NO 纳百川/泉涌/腾浪/汹涌). Rolls R7: burned 5 exchanges -> all junk (五行流转,疗愈阵纹,引雷阵,辟邪阵纹,火灵·聚炎). No water generator found.
BOARD FIELDED: ['金灵·穿心+1','金灵·穿心','金灵·针','五行刺+1','土灵印+1','金灵印','引雷阵','疗愈阵纹'].
SIM RESULTS (repeat=4): best 8-card order wins ~25-75% going FIRST, 0% going SECOND vs her base. +1 upgrade 0%/0%. Dropping EITHER 引雷阵 or 疗愈阵纹 (7-card) -> loses even first seat. 6-card -> loses.
ROOT CAUSE of loss: her permanent 内伤 (落花有意 1 + 流水无情 2 = 3/turn) + 枯木逢春(Revitalized) 10dmg finisher out-races my ~5-7 dmg/turn by ~1 turn; she always ends at 2-14 hp while I die to the clock at t9-11.
ECONOMY: absorbed 辟邪阵纹 -> 修为 25 to TIE her (tie=coin-flip seating) since I'm 修为24 vs her 25 (act second). No merge pairs existed; max reachable 修为 without dropping a board slot = 25.
MECHANIC VERIFIED: 辟邪/hexproof does NOT block 内伤 (gamestate_full.js:4276-4280 excludes x==="internal_injury" from the ruthless_water->injury conversion, and debuff adds like 落花/流水 apply 内伤 directly). Do NOT tech 辟邪 vs 内伤 clocks.
TOP LESSON: the WATER ENGINE notebook says metal board is bad vs 谭舒雁 — CONFIRMED. But this game I never got water pieces; metal + 引雷阵 + 疗愈阵纹 is the fallback and it's ~coin-flip at best. MUST roll harder R3-R8 for water generators (水灵阵, 波澜, 涛, 泉涌).

==== LEDGER ENTRY · Game 16 ====
## Game 17 (g17-ledger call it gN+1)
吾行之 (五行/水灵), sidejob=5 阵法师, 境5, 修为60, maxHP 99. RESULT: 3rd/4th — final 命 0 (never first). Record ~5W-8L. Fates: 战斗历练, 水灵传承, 悠然葫芦, 五行循环, 五行传承.
FINAL BOARD (R13, the losing board): ['水灵印','木灵印+1','水灵·波澜','周天剑阵+1','水灵·涛+1','水灵·涛+1','五行刺+1','疗愈阵纹+1'] — a GENERATOR-HEAVY board with NO 水势 PAYOFF and NO 纳百川 tank.

★★ TOP DISCOVERY (evidence, yisim 6 reps): The CORRECTED board
  ['水灵阵','水灵·纳百川','水灵·波澜+1','水灵·泉涌','水灵·腾浪+1','水灵·涛+1','水灵·涛+1','水灵·汹涌']
  wins **100%/100% BOTH SEATS vs 小布's final board** AND **100%/100% vs 谭舒雁's final board**.
  In the winning log (I concede seat to 小布): 纳百川 at t9 with 17 水势 gave +23 maxHP (heal 11→34), absorbing
  his 磅礴之势 40-burst; the cycle rebuilt 水势 to 20 and 汹涌 hit for 19-20 by t10-11 — a WIN, not a loss.
  ROOT CAUSE of my actual loss: my R13 board had FOUR 水势 GENERATORS (水灵印/波澜/涛x2) but only 涛 (13 dmg) as
  payoff — 水势 never exceeded ~4 because I had no 泉涌 (dmg→水势) and no 纳百川 (水势→HP). Generators without a
  converter do nothing. 周天剑阵/疗愈阵纹/五行刺 were FILLERS that don't feed 水势.

★ MISTAKE M-A (fatal): NEVER DREW 纳百川/泉涌/腾浪 ALL GAME despite 25 rolls in R13 alone. 纳百川=境5/6 copies,
  泉涌=境3/8 copies, 腾浪=境4/8 copies. I rolled R13 in a PANIC (25 rolls) at a board that was already winning-adjacent,
  instead of rolling R13-16 SELECTIVELY with the engine in mind. My R8 roll found 水灵阵 and I ABSORBED it (修为 bump)!
  \u2192 MISTAKE: absorbed 水灵阵 (a #1 picklist battery) for +1 修为 at R8. FIX: NEVER absorb an engine piece (CP6).

★ MISTAKE M-B (structural, the real killer): SEAT/修为 RACE LOST ALL GAME. Final 修为: me 60, 小布 89, 牧逸风 90.
  小布's economy: ZERO rolls R1-R5/R7-R9, absorbed EVERYTHING, hit each gate EARLIEST (境2@R3, 境3@R6, 境4@R9, 境5@R12),
  reached 112 HP by R12. I was 境4 with 78 HP at R12 (境5 only at R12). 牧逸风 same pattern (absorb-dump to gates).
  I BANKED to 22-23 and rolled junk for most of R5-R12. FIX: ABSORB-HEAVY is correct early; the 60-vs-89 修为 gap
  meant I acted SECOND vs everyone for most of the late game.
  ALSO wasted grants at the cap: R10 ended 22, R11 ended 23, R12 ended 23 (grant fills to 25 only; 23+3=25 anyway).

ECONOMY: rolls R1:0 R2:0 R3:5 R4:5 R5:0 R6:5 R7:0 R8:2 R9:0 R10:0 R11:2 R12:2 R13:25(!). 
  The R13 25-roll panic found 涛+1 (2nd copy) + 周天剑阵+1 but NOT 纳百川/泉涌/腾浪 — pool had them but RNG cruel.

★ TOP DISCOVERY #2: 牧逸风's 万法归灵剑 qi-nuke is UNWINNABLE for any water board (0%/0%, search found nothing).
  His board ramps qi (聚灵心法+百鸟+引气剑+点星) then 万法 exhausts ALL qi for 5-6/qi = 70-98 dmg at t6-7. 
  My water ramp payoff (水势) doesn't come online until t9-11 — too slow. Per matrix he beats EVERYONE 100%.
  REALISTIC PATH TO WIN: beat 小布+谭舒雁 (both 100% with corrected board), out-survive 牧逸风 (he kills himself 
  to 命-loss eventually, or I place 2nd). I DID have a 100%-win board for 2 of my 3 rivals and didn't build it.

SURPRISE: 五行刺+1/周天剑阵/天罡聚力阵 are the wrong CHOICE vs the water engine — every board slot must FEED 水势
  (generator) or CONVERT 水势 (纳百川→HP, 汹涌→dmg) or pay 涛's 2qi. Filler dmg cards dilute the engine.

==== LEDGER ENTRY · Game 17 ====
# Game 18 (g18) — 吾行之/pid2, 五行 sect + sidejob 5 阵法师.
# RESULT: NOT 1st (died to 0命). Winner = 谭舒雁 (pid1, 命1); 小布 (pid3) runner-up (命21); 牧逸风 (pid0) died.
# W/L: L R1(pid1) L R2(pid3) L R3(pid0) | W R4 W R5 W R6 | L R7 L R8 L R9 | W R10 W R11 W R12 W R13 | L R14 L R15 L R16 L R16 | W R17 | L R18(double-round). 8W-11L. 命 bleed was relentless; I had 2 games (R16/R18) with double matchups.
# FATES (境2→境5): 战斗历练, 水灵传承, 悠然葫芦, 五行化身, 五行传承. 境2@R3, 境3@R5, 境4@R8, 境5@R12. Ended 修为87, maxHP109.

## FINAL BOARD (R18 fielded, the LOSING order):
# ['水灵阵+1','水灵·纳百川+1','五行天髓诀','水灵·波澜','水灵·腾浪','水灵·泉涌','水灵·涛+2','水灵·汹涌+1']
#   -> 五行天髓诀 at SLOT 3, 汹涌 at SLOT 8. Wins 100% FIRST, 0% SECOND vs 小布 (sim_matchup 5 reps).

### ★★★ THE GAME-DECIDING DISCOVERY (search_board + sim_matchup, 5-6 reps, THIS game) ★★★
# ONE ORDER FIX flips 0%→100% BOTH SEATS vs 小布. Correct order:
#   ['五行天髓诀','水灵阵+1','水灵·波澜+1','水灵·纳百川+1','水灵·汹涌+1','水灵·腾浪','水灵·泉涌','水灵·涛+2']
#   = 100% first / 100% second vs 小布 base (~9t), 100%/100% vs 谭舒雁 base AND +1, 100%/100% vs 牧逸风 base AND +1.
#   = a board that beats ALL THREE rivals 100% both seats. (Vs 小布 FULLY +1 it's still 100% first / 0% second — need the seat.)
#   WHY (full log, I go 2nd): 五行天髓诀 at SLOT 1 means the chase chain starts on turn 1, not turn 3. 水势 ramps
#   ~1 cycle faster: by t8 纳百川 gives +29 maxHP (heal 32→61) absorbing 小布's t7 32-burst, then 汹涌 (moved
#   8→4) lands for 27+21=48 dmg at t9 and KILLS him. With 汹涌 at slot 8 it only fires ONCE per battle (cycle
#   never laps) — the payoff never overlaps peak 水势. ORDER IS THE WHOLE BALLGAME.
#   NOTE: this SUPERSEDES notebook CP1g ("五行天髓诀 placed AFTER 纳百川"). That rule was WRONG.
#   search_board trace: "move 五行天髓诀 slot3->slot1: win 100% first / 100% second" — single winning move.

### #1 ROOT CAUSE OF LOSS: I never re-ordered. I fielded 五行天髓诀 slot3 all game (my notebook told me to).
#    My board QUALITY was fine (it beats everyone both seats re-ordered). My ORDER lost the game. ALWAYS
#    search_board/sim_matchup BEFORE the final set_board, not after — one move was worth the whole lobby.

### #2 ROOT CAUSE: 修为/SEAT LAG. Me 87, 小布 96, 谭舒雁 101, 牧逸风 57. I went SECOND all late game.
#    With the CORRECT order seat doesn't matter — but I never fixed the order, so seat decided my losses.
#    小布 & 牧逸风 & 谭舒雁 all confirm independently: "seat is half the game" (their playbooks CP3/CP3).
#    With the OLD order vs 小布's FULLY +1 board, best = 100% first / 0% second -> must win the seat.

### ECONOMY / ROLL AUDIT (my rolls: R3:5 R4:8 R5:9 R7:10 R8:3 R9:3 R11:7 R14:5 R15:23; ~73 total)
#   LEAK A (early shotgun): R3-R7 = 32 rolls, nearly all junk (R4 netted nothing: 汹涌→浑天印→…→土灵·碎;
#     R7's 10 rolls found only 水灵·泉涌). 小布 did R1-R6 = 0 rolls, absorbing everything. My early rolls
#     cost me 修为 AND found little. ROLL TARGETS should be NAMED (水灵阵/纳百川/泉涌/腾浪/汹涌) from R5+, else STOP.
#   LEAK B (R15 23-roll panic): found 纳百川 (the key tank!) + 腾浪 + 涛, GOOD hits — but I was already at 3命.
#     The correct play was to roll hard R11-R13 (when I had bank) not R15 (desperation).
#   LEAK C: banked to 22 at R18 end (wasted grant). Spend below 25.
#   BRIGHT SPOT: R18 merges (纳百川+1/汹涌+1/水灵阵+1/涛+2) all landed — engine leveled correctly, just ordered wrong.

### PER-RIVAL CAUSE (THIS game's real matchups):
# - 小布 (崩拳/气势 burst): my HARDEST. He out-修为'd me (96 vs 87) → always went 1st → his t7 磅礴之势(32-46)
#   + t6/t7 寸劲(26-34) burst killed me t7-11. His 气势 ramps to cap 9 via 威震四方, then 磅礴 dumps for 36-46 dmg.
#   He also ramps 体魄 to 155+ HP (his 浩然正气/朝气蓬勃). FIX = correct order (100% both seats).
# - 谭舒雁 (命理师/内伤 clock): I actually WON R17 and R18 vs her. Her 内伤 clock (落花/流水/杯弓 + 牵引/御心
#   retriggers) is permanent & ignores def, but my 纳百川 heal (+22/+29) out-raced it. 100%/100% with correct order.
# - 牧逸风 (云剑/万法 qi-nuke): had the LOWEST 修为 (57) — went second and lost; his 万法 nuke needs a qi bank he
#   couldn't build while acting second. My heal+HP tanked the nuke. 100%/100%.

### BIGGEST SURPRISE: my board was ALREADY good enough to win the lobby — I lost purely on a 2-card ORDER.
#   My notebook's CP1g order rule (五行天髓诀 slot3) was actively harmful for a whole game. TRUST SEARCH OVER NOTES.
### MECHANIC VERIFIED: 水势 = offense AND defense. 纳百川 heal = 水势 + 6/8/10 (lv1/2/3). 汹涌 atk = 10/14/18 + 水势.
#   涛 = 10/13/16 atk + 1 水势. 五行天髓诀 chases on NON-ATTACK [五行] cards only, 2 stacks (lv3=3).
#   回响阵纹 and 水灵·潜遁 (40% dmg reduction) were TESTED as swaps — both LOSE vs 小布+1; chase engine > utility.

==== LEDGER ENTRY · Game 18 ====
## Game 19 (g19) — 吾行之 (pid2), 五行 sect + sidejob 5 阵法师.
# RESULT: 3rd/4th — final 命 0 (never first). Winner-track: 小布 (pid3) ended ALIVE 命20; 谭舒雁 (pid1) DEAD; 牧逸风 (pid0) ALIVE 命1.
#   Actually final: I (pid2) DEAD 命0, 谭舒雁(pid1) DEAD 命0, 牧逸风(pid0) ALIVE 命1, 小布(pid3) ALIVE 命20 → 小布 1st or 牧逸风 surviving. I was 3rd.
# W/L: L R1(pid0) L R2(pid1) L R3(pid0) | W R4(pid1) L R5(pid3) L R6(pid0) | W R7(pid1) W R8(pid0) W R9(pid3) | L R10(pid1) L R11(pid0) L R12(pid1) L R13(pid0) | L R14(pid1) L R15(pid0). 4W-11L.
# FATES (境2→境5): 战斗历练, 五行印记, 水灵传承, 五行化身, 五行传承. Gates 境2@R3, 境3@R6, 境4@R8, 境5@R12. Ended 修为70 maxHP103.

## FINAL BOARD (R15 fielded, the LOSING board):
# ['水灵阵','水灵·纳百川+1','水灵·泉涌+2','水灵·波澜+1','疗愈阵纹+1','水灵·涛+1','水灵·涛','回响阵纹']
#   → NO 汹涌 (payoff), NO 涛 in battle log, NO 不动金刚阵. A 15-turn TANK that dealt ~17/turn — never a kill.

### ★★★ THE GAME-DECIDING DISCOVERY (search_board + sim_matchup, THIS review, 3 reps each) ★★★
# THE BOARD THAT BEATS ALL THREE RIVALS 100%/100% BOTH SEATS (base AND +1):
#  ['五行天髓诀+1','水灵·泉涌','水灵·腾浪+1','水灵·纳百川+2','水灵·波澜+2','水灵·涛+2','不动金刚阵','水灵·汹涌+1']
#   - vs 小布 (matrix board): WIN 100%/100% (deterministic, ends 8/138 HP). vs 小布 fully-upgraded: 100%/100%.
#   - vs 牧逸风 base AND +1: 100%/100%. vs 谭舒雁 base AND +1: 100%/100%.
#   WHY IT WINS (full log): 不动金刚阵 at slot7 is [+7 防 AND +7 maxHP/heal at turn-end, 2 turns] — a SURVIVAL
#     card that does NOT break 天髓诀 (阵 is not 水灵, so it doesn't trigger the chase). It held me at 1 HP through
#     小布's t5 寸劲 (47 dmg) — WITHOUT it his burst kills me t5. 汹涌 at LAST slot pays off after 水势 ramps.
#     Earlier 泉涌(slot2) converts dmg->水势 so 纳百川(+HP) is live by t3.
#   This SUPERSEDES the g18 "corrected order" — that board beats 牧逸风/谭舒雁 but LOSES 0%/0% to 小布's real final
#     board. My g18 board was NOT actually lobby-winning.

### #1 ROOT CAUSE: I ABSORBED 水灵·汹涌 AT R12 (修为 54→55). 汹涌 = the ONLY 水势→dmg converter = THE WIN CONDITION.
#   economy_history R12: dealt ['土灵·流沙','土灵·断崖','水灵·汹涌','辟邪阵纹'] → rolled 2, then "absorbed 水灵·汹涌".
#   Result: my R13-R15 boards had ZERO payoff. 泉涌/波澜/纳百川 generate 水势; WITHOUT 汹涌 (or 涛) it does nothing.
#   FIX (extends CP6/CP1e): 汹涌 and 涛 are CONVERTER / semi-converter — NEVER absorb them. Absorbing your own
#   win-condition for +1 修为 is the single worst trade in this deck. (Same class as g17 "absorbed 水灵阵".)

### #2 ROOT CAUSE: NEVER DREW 不动金刚阵 despite it being in MY OWN 阵法师 pool (境4, 8 copies). 15 rounds, 0 drew.
#   I under-rolled (R12-R14 = 4-6 rolls each, no named target) AND my notebook WRONGLY listed 不动金刚阵 as
#   "ILLEGAL (3 持续)". It is LEGAL if you DROP 水灵阵 (天髓诀 + 不动金刚阵 = exactly 2 持续). That bad rule cost a game.
#   FIX: the 阵法师 sidejob is chosen FOR 不动金刚阵 (survival vs burst). Add it to the named roll targets.

### #3 ROOT CAUSE: 修为/seat lag AGAIN. Me 70, 小布 79, 谭舒雁 77, 牧逸风 67. 小布's economy = absorb EVERYTHING,
#   roll only in TARGETED burst rounds (R5 15 rolls, R11 18 rolls). He hit 修为 84. I rolled 4-13 in MANY rounds
#   (R4:4 R5:2 R6:4 R7:5 R8:13 R9:5 R10:6 R11:4 R12:4 R13:6 R14:5 R15:7 ≈ 65 rolls, near-zero targeted) and
#   ended 修为 70. Same lesson 3rd game running.

### ECONOMY (mine, rolls/round): R1:0 R2:0 R3:0 R4:4 R5:2 R6:4 R7:5 R8:13 R9:5 R10:6 R11:4 R12:4 R13:6 R14:5 R15:7 (~65).
#   R12 dealt 汹涌 and I ABSORBED it. R13 dealt 纳百川 (kept, correct). Never saw 不动金刚阵/汹涌 again.
#   LEAK: zero NAMED targets after R8; shotgun rolls at R8(13)/R15(7). Contrast 小布: 2 targeted mega-dumps.

### PER-RIVAL CAUSE:
# - 牧逸风 (pid0) — my MOST FREQUENT foe (7 of my 15 rounds; L R1,R3,R6,R11,R13,R15; W R8). His 巨鲲灵剑(追)+白鹭灵剑
#   (5+3/qi) chip + 云剑 chases ground me down t5-11. Base board: I tank-win (15t). His +1/+万法 board: 0%/0% for my
#   real board. The winning board beats even his +1 100% (早 泉涌 → 34+26 dmg payoff t6-10 outpaced his ramp).
# - 小布 (pid3) — THE WALL. His matrix board (气势-ramp + 崩拳·寸劲 double-force 58 + 磅礴 dump) kills t5-6. My
#   real board = 0%/0%. ONLY the 不动金刚阵 board survives his burst (1 HP, wins t6). 3rd+ game he is my structural loss.
# - 谭舒雁 (pid1) — I was 2W-5L, but the winning board beats her 100%/100% base AND +1. Her 内伤 clock out-races
#   a pure tank; my payoff (汹涌) kills her t8 before her clock matures.

### SURPRISE: 不动金刚阵 — I had classified it REJECTED ("3 持续 illegal") for 3 games. It is THE anti-burst survival
#   card in my own sidejob. The lesson repeats: my NOTEBOOK's rejection rules are the most dangerous thing I own.
# MECHANIC VERIFIED: 天髓诀 chase fires only if played card is 水/木/火/土/金-spirit AND did NOT attack AND no chase
#   yet this turn (gamestate_full.js:3009-3019). 阵-cards (不动金刚阵/辟邪) do NOT trigger it → 不动金刚阵's
#   "+7HP if no chase this turn" clause can fire. 不动金刚阵 = +7 防 AND +7 maxHP/heal (2 turns, lv1).
#   泉涌 lv2 = +3qi; 纳百川 lv2 = +4 水势, +8/水势 HP. 汹涌 lv2 = 14 atk +水势. 涛 lv2 = 13 atk +1 水势.

==== LEDGER ENTRY · Game 19 ====
## Game 20 (g20) — 吾行之 (pid2), 五行 sect + sidejob 5 阵法师.
# RESULT: **1st PLACE (WINNER), 命 31**. Lobby: pid0 牧逸风 云剑 (DEAD 命0), pid1 谭舒雁 命理/内伤 (DEAD 命0), pid3 小布 崩拳 (ALIVE 命1).
# Record: W R1(pid3) W R2(pid0) L R3(pid3) W R4(pid1) W R5(pid0) W R6(pid1) W R7(pid0) L R8(pid3) L R9(pid0)
#         W R10(pid1) L R11(pid0) L R12(pid1) W R13(pid3) W R14(pid1)+W R14(pid3) W R15(pid1)+W R15(pid3)
#         W R16(pid1) L R16(pid3) W R17(pid3). Final: won R17 vs 小布 (-24命) → 小布 to 命1, I survived.
# FATES (境2→境5): 战斗历练, 五行印记, 悠然葫芦, 五行循环, 五行传承. Gates 境3@R6, 境4@R9, 境5@R13. Ended 修为78 境5 maxHP107.
# SIDEJOB: 5 (阵法师) — chosen to hunt 不动金刚阵; used it (barely) but absorbed TWO copies (see MISTAKES).

## FINAL BOARD (R17 fielded — THE WINNER):
# ['万花迷魂阵','回响阵纹','水灵·泉涌+1','水灵·波澜+1','水灵·纳百川','水灵·汹涌+1','金灵·巨鼎落','金灵·铁骨']
#   This board beat 小布's burst 100% (his own notebook's burst skeleton). Why: 万花迷魂阵 [持续] applies 1
#   [减攻]/turn-end AND drains 1HP per 减攻 stack; 回响阵纹 (slot2) RETRIGGERS slot-1 万花 → ~2 drain events/turn,
#   and the drain BYPASSES 防/气势. Meanwhile 纳百川 heals me and 减攻 blunts his force-scaled burst.
#   R17 log: by t9b I had 7 减攻 stacks → 7+ drain/turn; 小布's 寸劲/连崩 hit for far less under 减攻.

### ★★★ THE GAME-DECIDING DISCOVERY (search_board + sim_matchup, 5-8 reps each) ★★★
# THE UNIVERSAL LOBBY-WINNER (beats ALL 3 rivals, base AND +1, BOTH seats, ~100%):
#  ['万花迷魂阵+1','回响阵纹','水灵·泉涌+1','不动金刚阵+2','水灵·波澜+1','水灵·纳百川','水灵·汹涌+1','辟邪阵纹']
#   - vs 牧逸风: 100%/100% base, +1, AND vs his RECIPE-B ceiling (万法 lv2 55dmg). ✓
#   - vs 谭舒雁: 100%/100% base AND +1. ✓  - vs 小布: 100%/100% base AND +1. ✓
#   WHY (full logs): 不动金刚阵+2 = [+7 防 + 7 maxHP/heal at turn-end over 3 turns] = the anti-BURST survival card
#     (holds me vs 牧逸风 55-dmg 万法 and 小布's 寸劲). 辟邪阵纹 = 3 辟邪 (blanks 谭舒雁's 内伤 ticks — her whole win-con).
#     万花+回响 = the drain engine (2 events/turn). 纳百川 = HP/heal. Four 持续-free (万花+不动 = 2 持续, legal).
#   REACHABILITY: 万花+1 = 2 copies (4 in pool); 不动+2 = 4 copies (5 in pool, stretch); others common.
#   FALLBACK TIERS (each still beats someone):
#     - 万花+1 + 不动金刚阵(lv1) + 辟邪 = beats 谭舒雁 & 牧逸风 base/+1 (100%), vs 小布 base 100% but 0% vs his +1-board.
#     - 万花+1 + 不动+2 + 辟邪 = beats EVERYONE (my target).
#     - WITHOUT 辟邪 (use 水灵·腾浪 slot7): still 100% vs 小布/牧逸风 but vs 谭舒雁 +1 second seat drops to 20%.

### ★★★ KEY MECHANICS VERIFIED (gamestate_full.js) ★★★
# - do_anthomania_formation (3158): at owner's turn-end, +1 减攻 to foe, then reduce foe HP by foe.decrease_atk, heal self same, -1 stack.
# - do_echo_formation_thing (5552): 回响 at slot2 retriggers slot-1 CARD if is_continuous, UPGRADED by 1 lv (caps lv3).
#   → 回响 next to 万花 = a SECOND drain/turn (and the retrigger is one level higher). 回响 is a 万花 DOUBLER.
# - do_motionless_tutelary_formation (3167): +7 防 EVERY turn-end for its duration; +7 maxHP&heal if no chase that turn.
#   不动金刚阵 is NOT a 水灵 card → does NOT break a 水灵 chase chain, and its heal clause fires freely.
# - [减攻] is PERMANENT-ish and reduces foe ATK (×0.6-style / flat), so it hard-counters force/气势-scaled burst (小布).

### #1 MISTAKE: I ABSORBED 万花迷魂阵 (R15, 修为 70→71) AND 不动金刚阵 TWICE (R12,R14). ALL are core engine/survival cards.
#   economy_history confirms: R12 "absorbed 不动金刚阵"; R14 "absorbed 不动金刚阵" + "absorbed 混元无极阵"; R15 "absorbed 万花迷魂阵".
#   I got LUCKY: R16 deal gave 不动金刚阵 again, R17 deal gave 万花迷魂阵 again → rebuilt. FIX: add 万花迷魂阵, 不动金刚阵,
#   回响阵纹, 辟邪阵纹 to the DO-NOT-ABSORB core list (they are the 阵法师 survival/engine kit).

### #2 MISTAKE: I never fielded 不动金刚阵 or 辟邪阵纹 in a winning board until the sim said so — I was fixated on 水灵-only boards.
#   不动金刚阵 (my OWN sidejob card) is the single most valuable card vs burst; 辟邪 vs the 内伤 clock. Two slots of
#   "阵" tech > 2 more 水灵 fillers. ROOT of 3 games of losing to 小布.

### #3 ECONOMY: me 78 vs 小布 83 vs 谭舒雁 82 vs 牧逸风 58. I was 2nd — I WON the seat vs everyone but 小布.
#   rolls/round: R1-3:0, R4:0, R5:0, R6:3, R7:7, R8:0, R9:15, R10:0, R11:4, R12:2, R13:5, R14:2, R15:3, R16:6, R17:12 (~59).
#   R9(15) and R17(12) were SHOTGUNS. R9 DID land 泉涌 (real target); R17 landed 回响/巨鼎落/铁骨 (the win board).
#   Banked to 27 at R14 (over 25 cap → WASTED the R15 grant). FIX: land ≤24 before a grant round.
#   LEAK: never had a NAMED target list. Next game NAME one of: 万花迷魂阵 / 不动金刚阵 / 回响阵纹 / 辟邪阵纹 / 水灵·泉涌.

### PER-RIVAL CAUSE:
# - 小布 (pid3) — THE WALL 4 games running. Beaten ONLY by the 万花/回响 DRAIN board (bypasses his 防 + 减攻 blunts his force).
#   Matrix says my board beats his FINAL board 100%/100%; I lost R3/R8/R16 (mid-game, board not online) and WON R13/R14/R15/R17.
# - 牧逸风 (pid0) — my most frequent foe; he won R9/R11/R12 (his 云剑 chase ramped faster than my tank). LATE I outsustained.
#   New board beats his RECIPE-A and even RECIPE-B (万法 lv2) 100%.
# - 谭舒雁 (pid1) — her notebook claims her 内伤 recipe beats "吾行之" 100%; MY new board with 辟邪阵纹 beats HER 100%/100% both seats.
#   Her 内伤 clock is fully blanked by 3 辟邪 stacks; 万花 drain out-races her at t12.

### SURPRISE: 回响阵纹 is a 万花迷魂阵 DOUBLER (retriggers + upgrades slot-1 continuous). I had it on the board but
#   never understood its value until this review. It turned a chip drain into a 2-stack/turn snowball.
### TOP DISCOVERY RECAP: the 阵-tech survival kit (不动金刚阵 + 辟邪阵纹) + 万花/回响 drain = beats the burst lobby.

==== LEDGER ENTRY · Game 20 ====
## Game 20 (ARENA g20) — 吾行之 (pid2), 五行 sect + sidejob 5 阵法师.
# RESULT: **NOT 1st — final 命 0 (3rd/4th)**. WINNER = 小布 (pid3, 命49). 牧逸风(pid0)/谭舒雁(pid1)/me all dead.
# Record: L R1(pid3) W R2(pid1) L R3(pid0) L R4(pid1) W R5(pid0) L R6(pid3) W R7(pid0) L R8(pid3) L R9(pid1)
#         W R10(pid3) L R11(pid1) W R12(pid0) L R13(pid3) L R14(pid1) L R15(pid3,→0命). 5W-10L. DIED R15.
# FATES (境2→境5): 战斗历练, 水灵传承, 悠然葫芦, 五行化身, 五行传承. Gates 境2@R3, 境3@R6, 境4@R8, 境5@R12.
# Ended 修为68 境5 maxHP103. SIDEJOB 5 (阵法师) — correct pick, but I only reached 境5 at R12 and never drew the engine.

## FINAL BOARD (R15 fielded — THE LOSING BOARD, 0 payoff):
# ['不动金刚阵+1','辟邪阵纹+1','水灵·泉涌+1','水灵·波澜','须弥阵纹','水灵·腾浪','水灵·汹涌','水灵·涛+1']
#   card_stats: 不动金刚阵 0dmg, 辟邪 0dmg, 泉涌 0dmg, 波澜 0dmg, 须弥 0dmg, 腾浪 0dmg, 汹涌 10dmg, 涛 10dmg.
#   ★ WHOLE BOARD DEALT 20 DAMAGE OVER 10 TURNS. No 万花/回响/纳百川 = NO 水势 payoff, NO drain = a tank that cannot kill.

### ★★★ THE GAME-DECIDING DISCOVERY (search_board + simulate, 5-10 reps, THIS review) ★★★
# A board built from cards I ALREADY HELD beats 小布's actual final board 100% GOING SECOND:
#   ['八门金锁阵','辟邪阵纹+1','水灵·泉涌+1','水灵·波澜+1','须弥阵纹','水灵·腾浪','水灵·汹涌','水灵·涛+1']
#   - vs 小布 base final board: **100% going second (~11t), 0% going first** (sim_matchup, 10 reps, verified 2x).
#   - R15 I was SECOND seat vs 小布 (he went first, out-修为 me 86 vs 68) → THIS BOARD WOULD HAVE WON R15.
#   - WHY: 八门金锁阵 = deal 8 dmg BEFORE EVERY OPPONENT CHASE. 小布's whole engine IS chases (踏破九霄/冲霄破浪
#     gen 身法 → auto-chase; 寸劲 chain). His tempo literally feeds my 八门金锁阵. The ONLY card in my pool that
#     turns a chase-burst opponent's speed against him.
#   - vs his +1 board: still 0%/0% (structural — accept, but he hadn't upgraded via R15).
#   - REACHABILITY: 八门金锁阵 = career-5 境4 card, 5 copies left in my pool; I got it in my R10 AND R16 deals and
#     absorbed/ignored it. 100% reachable.

### #1 ROOT CAUSE: NO PAYOFF ENGINE. I fielded a tank with no win-con. 水势 generated (泉涌/波澜/腾浪/涛) but the
#   ONLY converter (汹涌) sat at ONE stack → 10 dmg. 纳百川 (水势→HP/heal) NEVER DREW. 万花/回响 (the drain engine,
#   career-5 境5) NEVER DREW because I hit 境5 at R12 (only ~4 rounds of post-境5 draws). A board that deals 20 total
#   damage across 10 turns vs a burst opponent = guaranteed loss.
### #2 ROOT CAUSE: SAME economy leak for the 4th game running. Me 修为 68 vs 小布 86, 谭舒雁 91, 牧逸风 75. I lost
#   every late seat race. My rolls (~58) were near-target-less churn (R6:17, R9:10, R10:8, R12:8, R13:7, R15:8).
#   I NEVER NAMED 万花迷魂阵 / 回响阵纹 / 水灵·纳百川 / 八门金锁阵 as targets.
### #3 ROOT CAUSE: I ABSORBED 水灵·泉涌 at R12 (54→55修为). 泉涌 is a 水势 GENERATOR — same class as g19's 汹涌 absorb.
#   Add 泉涌 to the DO-NOT-ABSORB list.

### PER-RIVAL CAUSE:
# - pid3 小布 (崩拳/气势 burst, WINNER): beat me R1,R6,R8,R13,R15. Killed me R15 (10t). The WINNING answer vs him =
#   八门金锁阵 anti-chase board (100% going second). I had the cards.
# - pid1 谭舒雁 (命理/内伤 clock): beat me R4,R9,R11,R14 — she out-raced my tank. The 万花/回响 drain board would
#   beat her (g20 winner-board had it); my fielded board 0%.
# - pid0 牧逸风 (云剑/qi): I beat him R5,R7,R12. Lowest 修为 — went second, lost the seat race to me.

### ECONOMY (mine, rolls/round): R1-5:0, R6:17, R7:0, R8:0, R9:10, R10:8, R11:4, R12:8, R13:7, R14:5, R15:8 (~58).
#   R6 (17 rolls) landed only 泉涌+1 (the rest junk churn). Contrast 小布: absorb-EVERYTHING R1-R10, ~1 targeted dump.
#   BANKED over: R8 ended 13, fine. No >25 waste this game (improvement).
#   LEAK: no named targets, AND I absorbed engine pieces (泉涌 R12).

### SURPRISE: 八门金锁阵 (anti-chase, career-5 境4, cheap) is a HARD COUNTER to 小布's chase-burst and I had it in
#   hand twice. I never considered it because my notebook only ever listed 不动金刚阵 as "the" 阵 skill.
### SURPRISE 2: My g20-winning "universal board" from last game (万花+回响+不动+纳百川+辟邪) is EXACTLY the right
#   target — but it NEEDS the 境5 sidejob cards (万花/回响) which I unlocked too late to draw. The lesson: hit 境5
#   EARLIER (absorb more, roll less) OR have an 境4 fallback (八门金锁阵 board).
### MECHANIC VERIFIED: 八门金锁阵 lv1 = 8 dmg + [持续]2: deal 8 dmg before EVERY opponent chase (card_text).
#   万花迷魂阵 = turn-end +1 减攻 + drain 1HP/减攻-stack, heals self (gamestate_full.js:3158-3164). 减攻 subtracts
#   FLAT dmg per attack (line 4572-4573). 回响阵纹 retriggers slot-1 持续 (upgraded +1 lv) → 万花 DOUBLER (5552).

==== LEDGER ENTRY · Game 21 ====
==== LEDGER ENTRY · Game 21 (ARENA g21) ====
## Game 21 (g21) — 吾行之 (pid2), 五行 sect + sidejob 5 阵法师.
# RESULT: **LAST (4th/4) — final 命 0**. WINNER = 牧逸风 (pid0, 命48). 谭舒雁(pid1)/小布(pid3)/me all dead 命0.
# Record: L R1(pid3) L R2(pid0) L R3(pid1) L R4(pid3) L R5(pid1) L R6(pid0) L R7(pid3) W R8(pid1) W R9(pid3)
#         L R10(pid0) L R11(pid1) L R12... W R12(pid3) L R13(pid1) L R14(pid0→died). 3W-11L. DIED R14.
# FATES (境2→境5): 战斗历练, 五行印记, 悠然葫芦, 水灵传承, 五行传承. Gates 境3@R6, 境4@R9, 境5@R12.
# Ended 修为67 境5 maxHP101. SEAT LOSS: 牧逸风 修为90, 谭舒雁 94, 小布 82. I was LOWEST → lost most seats.

## FINAL BOARD (R14 fielded — THE LOSING BOARD):
# ['水灵阵','水灵·腾浪','水灵·泉涌','水灵·涛+2','水灵·涛','水灵·汹涌','混元碎击','木灵·疏影']
#   card_stats R14: dealt only ~84 dmg over 8-11 turns. Generators (阵/腾浪/泉涌) = 0 dmg; converters thin.
#   NO 万花, NO 回响, NO 不动金刚阵, NO 辟邪, NO 纳百川 → a generator-heavy board with no drain/survival tech.

### ★★★ THE GAME-DECIDING FINDINGS (this review, yisim-verified) ★★★
## F1 [BIGGEST] SEAT(修为) IS THE MATCHUP vs a 万法/qi battery. My 67 vs 牧逸风's 90 → he ALWAYS went first.
#   SAME BOARD: "万花/回响/泉涌+1/不动金刚阵+2/波澜+1/汹涌+1/辟邪/纳百川"
#     - vs 牧逸风 going FIRST:  WIN (t12; survive his t8 万法 94-dmg dump at 6 HP, out-heal via 纳百川).
#     - vs 牧逸风 going SECOND: LOSE (t8; his 万法 77-94 comes before my heal, I'm at -7).
#   Full log confirmed both. **The board was ALREADY a win — I lost on SEAT, i.e. on ECONOMY/修为.**
## F2 THE 万花/回响 DRAIN-SUSTAIN BOARD is near-universal (g21 sims, 5-6 reps):
#   ["万花迷魂阵","回响阵纹","水灵·泉涌+1","不动金刚阵+2","水灵·波澜+1","水灵·汹涌+1","辟邪阵纹","水灵·纳百川"]
#     - vs 小布 (崩拳 burst): 100% BOTH seats, base AND +1. (re-order 不动金刚阵+2 to slot3 → 100%/100% too)
#     - vs 谭舒雁 (内伤 clock): 100%/100% BASE with 辟邪 at slot3; vs her +1 board → 0% (use 汹涌+2 version).
#     - vs 牧逸风 (万法): 100% first / 0% second. SEAT decides.
#   WHY: 万花 drains 1HP/减攻-stack bypassing 防; 回响 doubles it; 不动金刚阵+2 = +7防+7maxHP/turn-end x3
#     (anti-burst); 辟邪 blanks 内伤 (NOT attack dmg — source-verified via 谭舒雁's notebook too).
#   REACHABILITY: all in 阵法师(5) pool, 6-8 copies each. THIS is the board to build next game.

### #1 ROOT CAUSE: 修为/seat lag — 3rd+ game running. I over-rolled (R9=24!, R13=20) and under-absorbed.
#   economy_history me: R1-6=0 rolls, R7=4, R8=0, R9=24(!! SHOTGUN at 境4, wasted 25 exch), R10=0,
#     R11=3, R12=0, R13=20(!! SHOTGUN), R14=6 (~57 rolls, near-zero named) → ended 修为67.
#   Winner 牧逸风: R1-7=0, R8=15, R10=13, R11=6 (named 万法 hunt right after 境5@R11), R13=7 (found 万法+1),
#     then 0 → ended 修为90. SAME lesson as g20/g19: absorb-all early, ONE targeted dump right after 境5.
#   M29 CONFIRMED AGAIN: R9 24-roll shotgun was pre-境5 → 境5 cards LOCKED → near-100% wasted exchanges.

### #2 ROOT CAUSE: Breakthrough too LATE + under-absorb. I hit 境5 at R12; winner 牧逸风 hit it R11 (R10-11 target).
#   R9 I had 修为36 = exactly the 境4 gate; I should have been pushing for 境5 gate 55 by R10.

### #3 ROOT CAUSE: My board had 5 generators + 2 thin converters + 0 drain/survival — the SAME "engine without payoff"
#   trap flagged in my own notebook (CP1e). I never fielded 万花/回响/不动金刚阵/辟邪 despite them being common in my pool.

### PER-RIVAL (final standings):
# - 牧逸风 (pid0) WINNER 命48 — 万法 battery, 修为90, won the seat vs everyone. I was 0W-4L (R2,R6,R10,R14). Board
#   BEATS him if I go first (F1) — I never did. BEAT HIM BY OUT-ABSORBING (修为).
# - 谭舒雁 (pid1) — 内伤 clock, 修为94 (highest). I was 1W-4L (W R8). 辟邪-early board beats her base 100%/100%.
# - 小布 (pid3) — 崩拳 burst. I was 2W-2L. The drain board beats him 100%/100% base AND +1.
# - FINAL STANDINGS: I was LAST. My board was a win vs 小布 and first-seat vs 牧逸风 — I died to SEAT + wrong board.

### ECONOMY NUMBERS WORTH REMEMBERING (mine): rolls/round ≈ [0,0,1,0,0,0,4,0,24,0,3,0,20,6] ≈ 58.
#   R9(24) and R13(20) were both shotguns; R9 was PRE-境5 (double waste — wrong phase AND shotgun).
#   NEXT-GAME ROLL PLAN: R1-R9 absorb EVERYTHING (0-2 rolls), land ≤24 before grant rounds; break 境5 by R10-11;
#     R11+ EVERY roll NAMED (万花迷魂阵 / 回响阵纹 / 不动金刚阵 / 辟邪阵纹 / 水灵·泉涌), set budget ≤8 then stop.
### SURPRISE: My own notebook's g19/g20 "universal win board" was a 水灵-chase board needing 五行天髓诀+1/汹涌+2 —
#   but the SIMPLER, more-reachable 万花/回响 drain board beats the same lobby. Drain > damage-scaling for reachability.

==== LEDGER ENTRY · Game 22 ====
## Game 22 (ARENA g22) — 吾行之 (pid2), 五行 sect + sidejob 5 阵法师.
# RESULT: **LAST (4th/4) — final 命 0**. WINNER = 小布 (pid3, 命100). 牧逸风(pid0)/谭舒雁(pid1)/me all dead.
# Record: L R1(pid3) L R2(pid0) W R3(pid1) L R4(pid3) W R5(pid1) L R6(pid3) W R7(pid1) W R8(pid0) L R9(pid1)
#         L R10(pid0) L R11(pid3) L R12(pid0) L R13(pid1) L R14(pid3→died). 4W-10L. DIED R14 (killed by winner).
# FATES (境2→境5): 战斗历练, 五行印记, 水灵传承, 五行化身, 五行传承. Gates 境2@R3, 境3@R6, 境4@R8, 境5@R12.
# Ended 修为64 境5 maxHP101 — LOWEST-but-one (小布 74, 谭舒雁 71, 牧逸风 68). Lost most seat races.

## FINAL BOARD (R14 fielded — JUNK, NO ENGINE):
# ['金灵·蓄锐+1','金灵·穿心','周天剑阵','土灵·碎+1','土灵·流沙+1','不动金刚阵+1','火灵·灼心','土灵·合八荒']
#   card_stats R14: 蓄锐=0dmg(+12def), 穿心=30dmg, 周天剑阵=0, 碎=19dmg, 流沙=7, 不动=0, 灼心=0, 合八荒=0.
#   → a scattered 金/土/火/阵 attacker pile. NO 万花, NO 回响, NO 汹涌 payoff, NO 纳百川. Same "engine w/o payoff" trap.

### ★★★ THE GAME-DECIDING FINDING (yisim-verified THIS review) ★★★
## F1 THE 万花/回响 DRAIN BOARD WAS 100% REACHABLE AND WINS THIS LOBBY.
#   board = ['万花迷魂阵','回响阵纹','水灵·泉涌','不动金刚阵+1','水灵·波澜','水灵·汹涌','辟邪阵纹','水灵·纳百川']
#   sim_matchup (5 reps each, BASE boards as actually fielded by rivals — NO rival upgraded in g22):
#     vs 小布 (WINNER): 100% going first AND 100% going second (~15t).
#     vs 牧逸风 (万法): 100% first / 0% second (~13t).
#     vs 谭舒雁 (内伤): 100% first / 0% second (~17t).
#     vs 小布 +1 board: 100%/100% (verified again via search_board, locks 万花+回响).
#   → THIS BOARD WINS THE R14 FIGHT I DIED IN, EVEN GOING SECOND (full-log: I win at t15, 小布 to -2).
#   REACHABILITY: 万花迷魂阵 ×6, 回响阵纹 ×6, 不动金刚阵 ×6, 辟邪阵纹 ×6 — ALL in 阵法师(5) 境5/境4 pool, seen in
#     my R12/R13/R14 deals (万花 was in my R13/R14 pool; I rolled 回响 away in R13 without noticing!). 100% reachable.
## F2 MECHANIC CONFIRM (full log): 万花 end-turn drains 1HP/减攻-stack BYPASSING 防 and HEALS me; 回响 retriggers
#   slot-1 万花 → 2 drain events/turn. 不动金刚阵 +7防/turn-end + 7hp/maxhp if no chase = anti-burst. 辟邪 gives
#   [辟邪] stacks (blanks debuff stacks, NOT attack dmg) + 10防 if a 持续 was played.

### #1 ROOT CAUSE: STILL FIELDED A NO-PAYOFF PILE INSTEAD OF THE DRAIN ENGINE (CP1e violated for the 4th game).
#   The correct board was in my pool and I never assembled it. No excuse — 万花/回响 are my KIT and were dealt to me.
### #2 ROOT CAUSE: 修为/SEAT lag yet again (64 = near lowest). Same economy leak as g19/g20/g21.
#   my rolls/round g22 ≈ R8:5, R9:1, R10:6, R11:5, R12:22(!!), R13:4, R14:8 → ~51 total.
#   R12 = 22-roll SHOTGUN right after breaking 境5 in the SAME round — landed 不动金刚阵+1 (good) then kept churning.
#   NEUTRAL-OR-WASTE. 小布 rolled ~[0,0,2,0,0,1,0,0,8,0,0,0,4,5,3] and had a COHERENT board every round.
### #3 ROOT CAUSE: I ABSORBED engine pieces AGAIN — R14 I absorbed 水灵·泉涌, 水灵·汹涌, 五行天髓诀, AND BOTH
#   辟邪阵纹 copies I drew. Those were the drain board's slots! (M22 recurrence — had the winning cards, absorbed them.)
#   Wait-correct: absorbed because I had NO board plan. Without a NAMED target list I absorb the kit itself.
### PER-RIVAL: pid3 小布 WINNER — beat me R1,R4,R6,R11,R14 (5 of my 10 losses). Killed me R14. Beat by drain board.
#   pid1 谭舒雁 — beat me R9,R13 (内伤 clock out-races my pile; drain+辟邪 beats her base 100% first-seat).
#   pid0 牧逸风 — I went 1W-3L; drain board beats his base board IF I go first (seat race).
### ECONOMY NUMBERS: my rolls ≈ 51 (R12=22 the big shotgun). Ended 修为 64 vs 小布 74. Same lesson as g19-g21:
#   absorb ALL R1-R9, land ≤24 before grants, break 境5 R10-11, then ONE NAMED post-境5 dump for the drain kit, STOP.
### SURPRISE: The winner 小布 ABSORBED 回响阵纹 and 不动金刚阵 (R13/R12) — MY kit cards — because they're dead for him.
#   Rivals are feeding my pool with my own engine. The only reason I lost: I never named them as my target.

==== LEDGER ENTRY · Game 23 ====
## ARENA Game 23 (g23) — 吾行之 (五行 sect + sidejob 5 阵法师, pid2).
# RESULT: **1st PLACE / WINNER, final 命 1**. 牧逸风(pid0)/谭舒雁(pid1)/小布(pid3) all dead 命0.
# Record: L R1(pid1) L R2(pid3) L R3(pid1) L R4(pid0) L R5(pid1) W R6(pid3) L R7(pid0) W R8(pid1) L R9(pid0)
#   W R10(pid1) L R11(pid3) L R12(pid0) W R13(pid3) W R14(pid0) W R15(pid0)+W R15(pid3) W R16(pid0) L R17(pid3)
#   W R18(pid3, KILL). 9W-9L but SURVIVED: the late board won every must-win.
# FATES (境2→境5): 战斗历练, 五行印记, 悠然葫芦, 五行化身, 五行传承. Gates 境2@R3, 境3@R5, 境4@R9, 境5@R13.
#   Ended 修为86 境5 maxHP109 体魄0. (小布 100, 牧逸风 79, 谭舒雁 64 — I was 2nd but not lowest.)

## FINAL BOARD (R17-R18 fielded — THE WINNER):
# ['不动金刚阵','回响阵纹','水灵阵','水灵·纳百川','水灵·纳百川','水灵·波澜+1','水灵·波澜','五行刺+2']
#   (R17 I merged 波澜→+1. R18 note the board I ACTUALLY fielded shows 纳百川×2 BEFORE 波澜 — 波澜 later.)

### ★★★★★★ THE GAME-DECIDING DISCOVERY THIS REVIEW: 回响阵纹 MUST GO IN THE **LAST** SLOT, NOT SLOT 2. ★★★★★★
# 回响阵纹 retriggers SLOT-1's effect IF slot1 is [持续]. 不动金刚阵 (slot1, [持续]2) = +7def/+7maxHP end-of-turn.
#   WITH 回响 in slot2 (my fielded order): board wins 100% FIRST but 0% SECOND vs 小布's final board (loses ~t15 to 磅礴之势+寸劲).
#   WITH 回响 in the LAST slot: it retriggers 不动金刚阵 LATE in the cycle (AFTER 纳百川 raised 水势) →
#     the +7maxHP/+7def heal lands in the t10-t13 BURST window, keeping me alive → I win 100%/100%.
#   yisim-verified: ['不动金刚阵','水灵阵','水灵·纳百川','水灵·纳百川','水灵·波澜+1','水灵·波澜','五行刺+2','回响阵纹']
#     vs 小布 final: 100% first / 100% second (~14t). vs 牧逸风 final: 100%/100% (~17t). vs 谭舒雁 final: 100%/100% base AND +1.
#   → WHY: timing the sustain burst to land in the enemy's damage window. A 1-slot move turned a 50% board into a 100% board.
#   The old notebook board had 回响 at slot 2 and I WON R18 anyway on RNG (~coin flip going second). THIS is the robust fix.

## ★ 2ND DISCOVERY: SEAT IS DECISIVE VS 小布 (崩拳 burst) — his OWN notebook confirms it:
#   "vs pid2 水灵 tank: WIN 100% IF first, 0% if second. Seat is everything." (小布 notebook frozen at game end).
#   My R18: 小布 went FIRST yet I won — because 回响 was later in his real board order? No — because of RNG on 寸劲 force rolls
#   (his 寸劲 hit 37/27/33 in the real log vs sim's 50). Genuinely a coin-flip going second UNLESS 回响 is last (then 100%).
#   牧逸风's notebook also says the same: seat decides vs my tank. So my tank board is the matchup-dominant win.

## ★ WHAT DROVE MY DAMAGE (card_stats R16/R18): 五行刺+2 = the finisher (14 + 22 extra = ~36 on the last hit).
#   水灵·波澜 dmg = force_of_water stacks (grows +3/play; ~18-22 late). 纳百川 = +maxHP/heal (the sustain).
#   不动金刚阵+回响 = the +7/+7 per cycle engine. 水灵阵/水灵·波澜 = qi. Generators = 0 dmg by design (that's fine).

### ECONOMY AUDIT (rolls/round): R1-5=0, R6=9, R7-10=0, R11=3, R12=0, R13=25(!!), R14=7, R15=8, R16=0, R17=1 ≈ 53 rolls.
#   R6(9 rolls) was PRE-境5 (境3, board was a transitional 五行 pile) → near-wasted. R13(25) was right after 境5@R13 and
#   LANDED the kit (回响×2, 纳百川, 波澜, 不动金刚阵 was already in hand from ... ) — a justified NAMED hunt, but 25 is a lot.
#   R14(7)+R15(8) landed 回响/纳百川/不动金刚阵 → the winning board. No 25-cap waste (banked 24 at R11, 25 at R12).
#   LESSON: R6 pre-境5 9-roll shotgun was waste (M29 again). Break 境5 EARLIER (R11 not R13) so post-境5 rolls are in-pool.
#   I broke 境5 at R13 (late). 小布 broke R11, 牧逸风 R11. NEXT GAME: target 境5 by R11.

### PER-RIVAL (final boards as actually fielded):
# - pid3 小布 (崩拳 burst): W R6,R10,R13,R15,R18 | L R2,R11,R17. Beat by 不动金刚阵+回响 maxHP engine (out-sustain his burst).
#   His real board ['气若悬河','崩天步','威震四方','冲霄破浪','崩拳·寸劲+1','踏破九霄+1','崩拳·寸劲','磅礴之势']. I killed him R18.
# - pid0 牧逸风 (云剑/万法 qi battery): W R14,R15,R16 | L R4,R7,R9,R12. My maxHP grind out-scaled his chip; he never rammed 万法 hard.
# - pid1 谭舒雁 (命理/内伤 clock): W R8,R10 | L R1,R3,R5. Clock vs my ramp — I won when the engine was online.
### SURPRISE: I went 9W-9L and still WON — the game is about the LAST board, not the round-by-round record.
#   My mid-game transitional boards lost a lot; the moment I assembled 不动金刚阵+回响+纳百川+波澜 I won out. Never panic-fix mid.
### TOP LESSON: the 水灵 maxHP-grind board WINS THIS LOBBY; 回响 must be LAST; break 境5 by R11; name the kit when rolling.

==== LEDGER ENTRY · Game 24 ====
## ARENA Game 24 (g24) — 吾行之 (五行 sect, sidejob 5 阵法师, pid2).
# RESULT: **1st PLACE / WINNER, final 命 18**. 牧逸风(pid0)/谭舒雁(pid1)/小布(pid3) all dead 命0.
# Record (19 rounds, 10W-9L): L R1(pid3) L R2(pid0) W R3(pid1) L R4(pid3) L R5(pid1) W R6(pid0)
#   L R7(pid1) L R8(pid0) W R9(pid3) W R10(pid0) W R11(pid1) L R12(pid0) W R13(pid1) L R14(pid3)
#   W R15(pid0) W R16(pid3) W R17(pid0) L R17(pid3) W R18(pid0) W R19(pid0). Two 命-wars both won by WINNING the must-win round.
# FATES (境2→境5): 战斗历练, 五行印记, 悠然葫芦, 五行化身, 储纳灵气 (generic economy; no change tested).
# Ended 修为97 境5 maxHP111 体魄0. Gates: 境2@R3, 境3@R6, 境4@R9, 境5@R12.

## FINAL BOARD (R16-R19 fielded — THE WINNER):
# ['不动金刚阵+1','水灵阵+1','水灵·纳百川','水灵·纳百川','水灵·波澜','水灵·腾浪','水灵·潜遁','五行刺+1']
#   card_stats R19: 不动金刚阵 0dmg; 水灵阵 +3qi; 纳百川 4x +66 maxHP/heal (the sustain); 波澜 2x (dmg=水势);
#   腾浪 +3qi+2maxHP; 潜遁 +1qi+2maxHP; 五行刺+2 11dmg (finisher). maxHP ramp 111→202. WON going first R17/R18/R19.

### ★★★★★ THE GAME-DECIDING DISCOVERY (yisim-verified THIS review) ★★★★★
## THE 潜遁↔腾浪 SLOT SWAP IS WORTH 50% vs 小布 (崩拳 burst). Put 潜遁 BEFORE 腾浪, NOT after.
#   board A ['不动金刚阵+1','水灵阵+1','纳百川','纳百川','波澜','腾浪','潜遁','五行刺+1'] (腾浪@6,潜遁@7 — what I fielded):
#     vs 小布 EXACT final = 100% first / 0% SECOND. ← this is why I lost R17 to him.
#   board B ['不动金刚阵+1','水灵阵+1','纳百川','纳百川','波澜','潜遁','腾浪','五行刺+1'] (潜遁@6,腾浪@7):
#     vs 小布 EXACT final = 100% first / 100% second (~12t). search_board found it in 1 move (腾浪 slot6→7).
#   WHY: 潜遁 = take 40% less ATK for 2 turns. Placed at slot 6 it lands its -40% shield EXACTLY on 小布's
#     t11-t12 寸劲/连崩 burst window (his 寸劲 hit for 55 raw → reduced enough to survive at 3-7 HP with 204 maxHP).
#   Going second (simulate, i_go_first=False) I win t12 at 3 HP → the swap converts a 命-loss round into a win.
#   VERIFIED: sim_matchup 6 reps → 100%/100%. simulate going-second full_log → I win t12.
#   NOTE: 4 五行/水灵 pieces do the same thing at either slot; the ONLY delta was 潜遁 vs 腾浪 order.

## ★★ 2ND FINDING: 回响阵纹@LAST is an ALTERNATIVE (not this game's fix). board
#   ['不动金刚阵+1','水灵阵+1','纳百川','纳百川','波澜','潜遁','腾浪','回响阵纹'] → vs 小布 100%/100%, vs 牧逸风 100%first.
#   (回响 retriggers slot-1 不动金刚阵: +7def/+7maxHP again late in cycle.) I had 回响 6 copies in pool (4.5%/roll),
#   drew & ABSORBED 万花迷魂阵 R17 and never chased 回响 — same M22 leak. But the 潜遁-swap fix needs no new card.

### ★ MATCHUPS (EXACT final boards, yisim, 5-6 reps) — MY FINAL BOARD board B:
# - pid3 小布 崩拳 burst: 100%first/100%second BASE. His +1 board = 0%first/0%second (structural wall, unreachable ~1 round).
#   search_board vs his FULLY +1 board: best reachable = 100%first/0%second (need 纳百川+1 to even get 0%→100% second).
# - pid0 牧逸风 云剑/万法 battery: 100%first/100%second BASE. His +1 = 100%first/0%second. He CANNOT win vs my tank (his
#   own g29 notebook: "吾行之 水灵 WALL = HARD COUNTER, wins ~0% of my pool"). R19 he went full distance: his 万法 41 +
#   巨鹏+巨鲸 25 + 巨虎 came; I out-healed to 202 maxHP and killed t11. No 万法 one-shot is lethal through 纳百川 ramp.
# - pid1 谭舒雁 命理师 内伤 clock: 100%first/100%second BASE AND +1. She CLAIMS (notebook) her C4 内伤 clock is
#   100%/100% vs my tank base — but her ACTUAL R-final board (血光/紫气/星弈立/断/螳螂/流水/诸事不宜/静气) sims 100% ME
#   both seats. She never assembled the C4 clock. My maxHP ramp + 内伤 3/turn = ramp wins the race.

### ECONOMY (rolls/round): R1-6=0, R7=1, R8=2, R9=2, R10=4, R11=4, R12=25(!!), R13=6, R14=8, R15=6, R16=5, R17=5, R18=8, R19=10 ≈ 86 rolls.
#   R12 = a 25-roll SHOTGUN — 境5 broke the SAME round, and most landings were junk absorbed for 修为 (ended 修为97 = HIGHEST,
#   so the absorbs weren't wasted) but the rolls were near-nameless. This is BETTER than g21-g23 (I broke 境5 at R12, ok-ish)
#   but the R12 shotgun is the same M29/M40 leak. R17-R19 rolls = ~5-10 each NAMED (looking for 回响/纳百川 — but I ABSORBED
#   万花 and never named 回响, so they mostly missed). Winner-grade 修为 (97) came from absorb-all early, NOT from rolls.
#   NEXT-GAME ROLL PLAN: absorb ALL R1-11 (≤2 rolls), break 境5 by R11, land ≤24 before grant rounds; R12+ EVERY roll NAMED
#   at {回响阵纹, 水灵·纳百川, 水灵·波澜, 水灵·潜遁, 不动金刚阵}, budget ≤8, STOP once the tank is fielded.

### PER-RIVAL (final boards as fielded):
# - pid3 小布 (崩拳 burst): W R9,R16 | L R1,R4,R14,R17. R14 loss = board was a MID transitional pile (混元碎击, no 水灵阵,
#   only +27 maxHP from 纳百川×2, no ramp) → out-burst. R17 loss = fielding order (潜遁 last) → 0% going second. FIX: board B.
# - pid0 牧逸风 (云剑/万法 battery): W R6,R10,R15,R17,R18,R19 | L R2,R8,R12. NEVER lost a late round to him once the tank
#   was online. He is hard-countered by my 水灵 tank (his own notebook confirms).
# - pid1 谭舒雁 (内伤 clock): W R3,R11,R13 | L R5,R7. Won every late round; her clock never assembled.
### SURPRISE: My own dmg is TINY (五行刺 ~11, 波澜 ~20 late). I win EVERY long fight by MAXHP SUSTAIN (111→202), not damage.
#   The build's real engine is 纳百川 (heal grows with 水势: +12/+21/+24...) + 潜遁 -40% + 不动金刚阵 +7def/+7maxHP/cycle.
#   Damage is almost incidental. The WIN CONDITION is "outlast", not "out-burst" — field it and the seat barely matters.

==== LEDGER ENTRY · Game 25 ====
==== LEDGER ENTRY · Game 25 (ARENA g25) ====
## Game 25 (ARENA g25) — 吾行之/pid2, 五行 sect + sidejob 5 阵法师. RESULT: **NOT 1st — final 命 0 (eliminated)**.
# Winner = 谭舒雁 (pid1, 命40). 牧逸风(pid0)/我(pid2)/小布(pid3) all dead 命0.
# W/L: L R1(pid1) L R2(pid0) L R3(pid3) L R4(pid1) L R5(pid0) W R6(pid1) W R7(pid3) W R8(pid0) W R9(pid3)
#      L R10(pid0) W R11(pid3) L R12(pid0) L R13(pid3) L R14(pid1). 5W-9L. DIED R14 to the winner.
# FATES (境2→境5): 战斗历练, 机缘造化, 悠然葫芦, 水灵传承, 储纳灵气. Gates: 境2@R3, 境3@R5, 境4@R9, 境5@R11. Ended 修为63 境5 maxHP101 (2nd-LOWEST seat).
#
## FINAL BOARD (R14 fielded — ★ NO-PAYOFF PILE, the 5th recurrence of the SAME mistake ★):
# ['邪蛊阵','不动金刚阵','辟邪阵纹','水灵·潜遁','水灵·纳百川','水灵·泉涌','木灵印','疗愈阵纹']
#   card_stats(R14): EVERY card 0 dmg. 辟邪 4x(+40def), 潜遁 +6maxHP, 纳百川 +36maxHP, 泉涌 +6qi, 木灵印 +3qi, 疗愈 +18maxHP.
#   → ZERO attackers except 邪蛊阵's 内伤 1/turn. I "won" the sustain war vs nobody — I dealt ~0 damage and lost the 内伤 race.
#
## ★★★★★ THE GAME-DECIDING DISCOVERY (yisim-verified THIS review) ★★★★★
## THE WIN BOARD FOR g26 IS THE g24 TANK, RE-ORDERED WITH TWO SPARE ATTACKERS IN BACK:
#  board W = ['水灵阵','水灵·纳百川','水灵·纳百川','水灵·波澜','水灵·腾浪','木灵·巡林','五行刺','金灵·穿心']
#  sim_matchup 4 reps vs the ACTUAL final boards:
#    vs pid3 小布 (崩拳 burst — my OLD 0%/0% WALL):  **100% first / 100% second** ← breaks the wall!
#    vs pid1 谭舒雁 (THE WINNER, 内伤 clock):       **100% first / 100% second**
#    vs pid0 牧逸风 (云剑/万法 qi battery):          **100% first / 0% second** (seat race)
#  (all three = 0%/0% at their +1 boards — the wall is their UPGRADES, not their base boards; at R14 nobody was fully +1.)
#  vs base everyone-else-boards this board wins BOTH seats vs 小布 & 谭舒雁 — only 牧逸风 is seat-dependent.
## WHY IT WORKS (full_log vs 小布 going SECOND, win t10): the delta vs the g24 board is defense→OFFENSE.
#   Swapped 不动金刚阵/潜遁 (0 dmg) for 木灵·巡林(1×2+[碎防]+CHASE if HP gained) & 金灵·穿心(7攻+无视防御).
#   The extra 五行-刺/穿心/巡林 chip DOWN 小布 before his t9-t10 崩拳/磅礴 burst; 纳百川+波澜 ramp maxHP 122→167 as a
#   backstop. 波澜 (=force_of_water stacks) is the finisher (~16-19). Wins the burst race WITH OFFENSE, not with walls.
## REACHABILITY: I HELD EVERY PIECE. g25 economy shows I drew & even FIELDED 水灵阵, 纳百川, 潜遁, 五行刺+1, 波澜.
#   木灵·巡林/金灵·穿心 were in-pool (巡林 4 copies, 穿心 3). I had the win board in hand by R14 and fielded a 0-dmg pile.
#
### #1 ROOT CAUSE (5th straight game, SAME failure — M22/M29/M40/M51/M63 recurrence): FIELDED A NO-PAYOFF PILE.
#   A board of pure DEF/qi/maxHP generators with ZERO attackers cannot kill anyone. Every slot must either attack OR
#   feed a named attacker. My R11 board was literally 3 cards + 5 empty Normal-Attack slots (card_stats R11: 9x Normal Attack).
### #2 ROOT CAUSE: 修为/SEAT lag — ended 修为63 (2nd lowest). Lost most seat races; my tank needs the first seat vs 牧逸风.
### #3 ROOT CAUSE: R11 = a 24-roll SHOTGUN right after breaking 境5, rolling THROUGH 万花迷魂阵, 辟邪阵纹, 混元碎击,
#   水灵·纳百川 and more — NAMELESS churn. Winner 谭舒雁 rolled 0,0,0,0,0,13(R6),5(R7),3,3,4,4,3,7,2,4 over 17 rounds: absorb-all early, ONE targeted dump, STOP.
## ECONOMY (my rolls/round): R1-9=0 except R3/4/5=1 each, R9=1, R10=8(named-ish), R11=24(SHOTGUN!), R12=6, R13=6, R14=6.
#   R11 shotgun (24) is the worst leak: fired the INSTANT 境5 broke, turned over the whole deck, landed 潜遁/纳百川/泉涌 only.
#   Landed ≤24 before grants most rounds (banked 22@R7, 27@R8 — slight over-cap waste at R8). Broken 境5@R11 (good pacing).
## PER-RIVAL (actual final boards, from the matrix + sims):
# - pid1 谭舒雁 (WINNER, 内伤 clock): beat me R1,R4,R14. My board W beats her EXACT final 100%/100%. I lost because I fielded the pile.
# - pid0 牧逸风 (云剑/万法): beat me R2,R5,R10,R12. Board W beats his base 100% first-seat / 0% second. Seat race.
# - pid3 小布 (崩拳 burst): beat me R3,R13. Board W beats his EXACT final 100%/100% (my OLD g24 board was 0%/0% — the ATTACKER swap fixed it).
## TOP DISCOVERY: the 水灵 tank does NOT need to be pure-defense. Replacing 不动金刚阵+潜遁 with 木灵·巡林+金灵·穿心
#   converts a 0%/0% matchup vs 崩拳 into 100%/100%. OFFENSE IN THE BACK HALF wins the burst race.
## SURPRISE: The winner was the SLOW 内伤 clock AGAIN — and my OFFENSIVE tank now beats her 100%/100%. I had the answer the whole time.
## MECHANICS CONFIRMED: 木灵·巡林 [木灵] chase triggers if HP was added earlier (纳百川 qualifies) → 2 attacks + a chase card.
#   金灵·穿心 [金灵] gives next attack 无视防御 (through 小布's 磅礴之势 def). 辟邪 stacks are EATEN per-debuff and 命运轮回 skips my plays — pure def loses to the clock.

==== LEDGER ENTRY · Game 26 ====
## ARENA Game 26 (g26) — 吾行之 (五行 sect, sidejob 5 阵法师, pid2). RESULT: **NOT 1st — final 命 0 (eliminated)**.
# Winner = 小布 (pid3, 命17). 牧逸风(pid0)/谭舒雁(pid1)/我(pid2) all dead 命0.
# W/L (20 battles): L,R1(1) W,R2(3) L,R3(1) L,R4(3) W,R5(0) L,R6(1) L,R7(0) L,R8(1) W,R9(0) L,R10(3) W,R11(0) L,R12(1) L,R13(0) W,R14(1) W,R15(3) W,R16(0) L,R16(3) L,R17(0) W,R18(0) L,R19(3). 7W-12L.
# FATES (境2→境5): 战斗历练, 五行印记, 悠然葫芦, 五行化身, 五行传承. Ended 修为85 境5 maxHP111 体魄0. Gates: 境2@R3, 境3@R6, 境4@R9, 境5@R13 (LATE — see M).

## FINAL BOARD (R19 fielded — ★ THE MISTAKE ★):
# ['周天剑阵','水灵·纳百川','水灵·泉涌','水灵·腾浪','水灵·涛','木灵·柳纷飞+1','水灵·汹涌+1','五行刺+1']
#   = a DAMAGE/QI pile, NOT the proven tank. card_stats: NO 潜遁, NO 不动金刚阵, NO 水灵阵. Lost t7 to 小布's burst.

## ★★★★★ THE GAME-DECIDING DISCOVERY (yisim-verified THIS review) ★★★★★
## THE g24 WINNER TANK WAS ~95% REACHABLE FROM MY R19 HAND AND BEATS ALL 3 RIVALS' FINAL BOARDS 100%/100%.
#   board W = ['不动金刚阵+1','水灵阵+1','水灵·纳百川','水灵·纳百川','水灵·波澜','水灵·潜遁','水灵·腾浪','五行刺+1']
#   sim_matchup (3-4 reps): vs 牧逸风 final = **100%/100%**; vs 谭舒雁 final = **100%/100% even vs her +1**;
#     vs 小布 final = **100% going first / 0% going second** (SEAT-dependent burst race).
#   R19 HAND had: 辟邪阵纹+1, 水灵·潜遁, 混元无极阵, 水灵阵, 不动金刚阵, 金灵·锋芒, 引雷阵; BOARD had 纳百川/腾浪/五行刺+1.
#   → I held 6-7 of the 8 g24 pieces. Only 波澜 was missing (substitute 泉涌 or 辟邪阵纹+1). I FIELDED A PILE INSTEAD.
#   full_log (going second vs 牧逸风): tank ramps 122→200 maxHP, 五行刺 finishes t12; 万法 41/65 hits are out-healed.
## WHY I LOST THE FIGHTS THAT MATTERED:
#  R17 vs 牧逸风 LOST by 3命 (命1→-2): fielded a 水灵 pile with only 2 attackers (五行刺 25dmg over 13t, 柳纷飞/Hexproof 0dmg).
#    His 万法归灵剑 (12qi → 65 dmg) one-shot my 149 maxHP. Tank board would have won BOTH seats.
#  R19 vs 小布 LOST by 31: fielded the 周天剑阵 damage pile going SECOND (修为 85 < 小布 93). Burst killed me t7.
#    The tank board wins going FIRST (100%). I trailed 修为 → I acted second → the burst race was unwinnable.

### #1 ROOT CAUSE (6th straight game, SAME failure — M22/M29/M40/M51/M63 recurrence): FIELDED A NON-TANK BOARD / DEVIATED.
#   I had the 水灵 tank pieces in hand and fielded a qi/damage pile with NO 潜遁, NO 不动金刚阵, NO 水灵阵.
#   The g24 board is my PROVEN WINNER and it still beats this lobby 100%. CP1 + CP1h violated.
### #2 ROOT CAUSE: 修为/SEAT lag (85 vs 小布 93) — lost the seat in the decisive R19 burst race. Must absorb HARDER.
### #3 ROOT CAUSE: LATE breakthrough — 境5 at R13 (vs g24's R12, winner 小布 broke R12). One round late = fewer phase-5 draws.

## ECONOMY (my rolls/round): R1-3=0, R4=1, R5-7=0, R8=2, R9=4, R10=6, R11=0, R12=1, R13=2, R14=25(SHOTGUN!), R15=0, R16=5, R17=0, R18=5, R19=17(SHOTGUN!). ≈68 rolls.
#   R14 (25) and R19 (17) were the 2 SHOTGUNS — nameless churn fired the round 境5 broke and again at R19. M29/M40/M65 recurrence.
#   Winner 小布 rolled 0,0,0,0,0,0,0,0,0,5,4,8,9,2,0,0,0,0,0 ≈28 rolls TOTAL — HALF mine — and assembled via MERGES (威震四方+1,
#   崩拳·连崩+1) + absorb-all. He rolled NOTHING after R13. Contrast: I shotgunned 42 rolls in R14+R19 alone and assembled nothing extra.
#   NEXT-GAME ROLL PLAN: absorb ALL R1-12 (≤2 rolls/round), break 境5 by R11, land ≤24 pre-grant.
#   R13+ EVERY roll NAMED at {水灵·波澜, 水灵·纳百川, 不动金刚阵, 水灵·潜遁, 水灵阵}, budget ≤8, STOP once tank fielded.

### PER-RIVAL (final boards as fielded):
# - pid3 小布 (崩拳 burst, WINNER): L R1,R4,R10,R16,R19 | W R2,R15. He assembled 威震四方+1 (force cap 10) + 连崩+1 by R18.
#   Tank board beats him 100% going FIRST. R19 loss = wrong board + second seat. His force cap +4 makes 寸劲/惊触 hit 30-50.
# - pid0 牧逸风 (云剑/万法 battery): L R7,R13,R17 | W R5,R9,R11,R16,R18. Tank board beats him 100%/100%. His 万法 (12qi→65dmg)
#   is the threat; only the maxHP ramp (200) survives it. My R17 pile had 149 maxHP and got one-shot.
# - pid1 谭舒雁 (内伤 clock): L R3,R6,R8,R12 | W R14. Tank board beats her 100%/100% incl her +1. She rolled 25@R11 (shotgun).
### SURPRISE: The g24 board is so strong it beats this lobby's EXACT final boards 100% BOTH SEATS vs 2 of 3 rivals — I simply
#   didn't field it. Winning this game required ONLY: (1) field the 水灵 tank, (2) secure FIRST seat vs 小布.
### MECHANICS CONFIRMED: 潜遁 -40% ATK is the anti-burst key (going-second vs 小布 still loses because burst lands t5-7 before 潜遁).
#   波澜 (2水势, no qi cost) is the ramp accelerator the g24 board has and mine lacked. 纳百川 heal grows with 水势 (12→20+).

==== LEDGER ENTRY · Game 27 ====
## ARENA Game 27 (the arena calls it g27; my counter counted it g26=prev) — 吾行之 (五行 sect, sidejob 5 阵法师, pid2). RESULT: **NOT 1st — final 命 0 (eliminated R16)**.
# Winner = 牧逸风 (pid0, 命59). 谭舒雁(pid1)/我(pid2)/小布(pid3) all dead 命0.
# W/L: W R1(0) W R2(1) L R3(0) W R4(1) L R5(0) W R6(3) W R7(1) W R8(3) W R9(1) L R10(3) L R11(0) L R12(3) L R13(1) L R14(3) W R15(1) L R16(0) L R16(3). 8W-9L. Died R16 on a DOUBLE loss (0 and 3).
# FATES: 战斗历练, 五行印记, 五行循环, 五行化身, 五行传承. 修为 73 境5 maxHP105 (LOWEST in lobby — lost every seat race).

## FINAL BOARD (R16 fielded — ★ THE SAME MISTAKE FOR THE 7TH STRAIGHT GAME ★): ['不动金刚阵','水灵·纳百川'×3,'水灵·波澜'×2,'水灵·泉涌'×2]
#   card_stats(R16): ONLY 2 cards ever played over 10 turns; 0 damage from ANY card. A pure qi-starved sustain pile. I LOST to 牧逸风 (his 万法 t6=110dmg) AND 小布 (burst t5-7).
#   R13/R14 boards were the SAME: 0-dmg sustain piles (card_stats: R13 7 cards all 0 dmg; R14 4 cards all 0 dmg; R11 board = 5 cards + Normal Attacks, 31 dmg total).

## ★★★★★ THE GAME-DECIDING DISCOVERY (yisim-verified THIS review) ★★★★★
## 水势 (force_of_water) IS A DIRECT-DAMAGE ENGINE: every [水灵] card played deals DIRECT DAMAGE = current 水势 stacks (up to 13-20 per card). I built 水势 with 波澜/纳百川 but NEVER spent it on attackers — so it did ~0.
## THE WINNING BOARD (search_board + sim, beats 牧逸风 base 100%/100% AND his +1 board 100% FIRST; beats 谭舒雁 base 100% first):
#   board W = ['水灵·泉涌','水灵·波澜','五行刺+1','水灵·腾浪','水灵·潜遁','水灵·汹涌+1','水灵·纳百川','八门金锁阵']
#   KEY: 泉涌(+2qi) + 腾浪(+2qi) = 4 qi/turn so I stop "gaining qi instead of playing." 波澜 builds 水势 early (slot2). 汹涌/涛/五行刺/八门金锁阵 deal damage EVERY turn.
#   sim vs 牧逸风 FINAL +1 board: 100% going FIRST (22命 win), 0% going second. vs 小布 base: 100% first / 0% second. vs 谭舒雁 base: 100% first.
## *** THE REAL DECIDER: SEAT / 修为. ***
#   My board BEATS 牧逸风's +1 board 100% FROM THE FIRST SEAT, 0% from second. His 万法+1 fires t6 for 107 dmg; my ramp reaches ~125 maxHP + 16 水势 by t10-11 to win ONLY if I act first by one turn.
#   I ended 修为 73 = LOWEST (牧逸风 83, 小布 85, 谭舒雁 66). I went SECOND in every decisive fight → lost them all. THE FIX: absorb MORE junk (修为 = seat = win), spend NOTHING on shotgun rolls.

## ECONOMY (my rolls/round): R1-10 = 0,0,0,0,0,1,3,2,2,3; R11=20 (SHOTGUN right after 境5); R12=9; R13=6; R14=6; R15=5; R16=9. ≈78 rolls.
#   R11 (20) fired the instant 境5 broke — turned over the whole deck, landed only 潜遁/纳百川/泉涌/火灵印. R16=9 (a 2nd shotgun). Both nameless churn. M-s recurrences.
#   Winner 牧逸风: 0 rolls R1-R11(!), then ONE 26-roll dump at R12 (post-境5), then STOP. 小布: absorb-all R1-9, R10-13 named dumps, STOP. Both ≈31-40 rolls total, ALL named.
#   I rolled 78 with no named target and assembled nothing; they rolled ~half that with named targets and won. NAMED-TARGET DISCIPLINE >> volume (7th confirmation).

### PER-RIVAL (final boards, matrix + my sims):
# - pid0 牧逸风 (WINNER, 云剑 double-qi engine 聚灵心法+回响, 万法 slot6): L R3,R5,R11,R16. His 万法 one-shots my low-HP board t6-t10. Board W beats him 100% FIRST (incl his +1) / 0% second. PURE SEAT RACE.
# - pid3 小布 (崩拳 burst, 威震四方+1 force-cap-10): L R10,R12,R14,R16. His t5-7 double-崩拳 hits 26-39. Board W = 100% first / 0% second vs base; 0% vs his +1. Fastest kill in lobby. SEAT + faster kill needed.
# - pid1 谭舒雁 (内伤 clock): W R2,R4,R7,R9,R15. Board W beats her base 100% first (races her 9-14/turn clock). L R13 (fielded a pile).
# ★ All three: my board wins FROM THE FIRST SEAT and loses from the second. 修为/seat was the whole game and I was LAST.

## TOP DISCOVERY: 水势 = direct damage per [水灵] card (snowballs to 13-20/card). This is the OFFENSE my 水灵 deck always lacked. My pure-sustain piles did 0 dmg for 7 straight games; the fix is 泉涌/腾浪 qi batteries + 波澜 ramp + a damaging 水灵/五行 card EVERY slot.
## SURPRISE: 牧逸风's 万法 grows FASTER than my maxHP ramp (21 qi by t6 = 110 dmg; my ramp = +10/turn). I cannot out-tank him — I must either out-race from first seat or win the 修为 race.
## SECOND SURPRISE: I was DEAD LAST in 修为 (73) while running the most rolls (78). Rolling ≠ power; absorbing junk for 修为 literally buys the first seat that decides every matchup.
## MECHANICS CONFIRMED: 水势 damage = stacks per 水灵 card played. 泉涌/腾浪 = the +2qi batteries. 波澜 = free 2水势. 潜遁 = -40% dmg 2turns (anti-burst, but must be timed to the burst turn). 八门金锁阵 = 8+8/chase, a cheap [持续] damage source (only ≤2 [持续]/[消耗] legal).

==== LEDGER ENTRY · Game 28 ====
## ARENA Game 28 (the arena labels it g28) — 吾行之 (五行 sect, sidejob 5 阵法师, pid2). RESULT: **NOT 1st — final 命 0 (eliminated)**.
# Winner = 牧逸风 (pid0, 命1). 谭舒雁(pid1)/我(pid2)/小布(pid3) all eliminated 命0. MARGIN = 1 命 — extremely close.
# W/L: W R1(3) W R2(0) W R3(1) W R4(3) W R5(0) L R6(1) W R7(3) L R8(1) W R9(3) W R10(1) W R11(0) W R12(1) L R13(0) L R14(3) W R15(0) L R16(0) L R17(3). 12W-5L.
# FATES: 战斗历练, 五行印记, 悠然葫芦, 五行循环, 五行传承. 修为 83 境5 maxHP107 (LOWEST in lobby: 牧逸风91, 小布90, 谭舒雁68). BROKE 境5 @R13.

## FINAL BOARD (R16/R17 fielded — ★ THE MISTAKE, 8th recurrence ★):
# ['水灵·腾浪','水灵·腾浪','水灵·泉涌','水灵·波澜','水灵·汹涌+1','水灵·涛+1','木灵·巡林','八门金锁阵']
#   = 4 qi-batteries/ramp + only **2 REAL ATTACKERS** (汹涌+1, 涛+1). card_stats(R17): 腾浪×3 = 0 dmg, 泉涌 0 dmg, 波澜 0 dmg, 巡林 0 dmg, 八门 0 dmg; ONLY 汹涌+1 (18) + 涛+1 (7) dealt damage. Total ≈25 dmg over 9 turns.
#   R15 I fielded 5 attackers (added 五行刺+1, dropped a redundant 2nd 腾浪) and WON vs pid0 (-19). Then I swapped BACK to the 2-attacker pile for R16/R17 and lost both.

## ★★★★★ THE GAME-DECIDING DISCOVERY (yisim-verified THIS review) ★★★★★
## MY g28 NOTEBOOK CLAIM WAS **FALSE**: "every [水灵] card deals direct damage = current 水势" is WRONG.
#   ENGINE FACT (gamestate_full.js:3198 do_force_of_water, called ONCE at line 3614 = END of player turn):
#   水势 (force_of_water) pays out as **ONE hit at end of turn = current stack count**, NOT per-card.
#   So 腾浪/泉涌/波澜/纳百川 (the ramp cards) deal ZERO direct damage; 水势 only converts via the end-of-turn lump AND via 汹涌 (10+水势 atk) / 涛 (flat 10).
#   → My ramp did nothing on turns where it wasn't backed by an ATTACKER. The tank must SPEND 水势 with attackers, not just build it.
## ★★★★★ THE MATCHUP WALL (yisim + matrix, 3+ reps each): **NO reachable 五行 board beats either finalist's FINAL board — 0%/0% both seats.**
#   - vs 牧逸风 final (聚灵心法+1/回响阵纹 qi-ramp → 万法归灵剑 one-shot): his t7 万法 fired for **95 dmg** (18 qi × 5 + 5) after my board only reached ~118-137 HP and dealt ~64.
#   - vs 小布 final (崩拳 burst, 46 体魄 → **173 maxHP**): his 崩拳·惊触+1/Shocked burst = 32-34 dmg/turn sustained; his HP alone out-scales my ramp. My tank survives to t11 but loses by HP.
#   search_board with ~1000 evals across pools 5,4,6,1 returned NO improvement (stopped at 21 evals = pre-filter found nothing) vs both. 五行 has NO 万法-class win-condition.
#   MATRIX transitive order: 牧逸风 > 小布 > 吾行之 > 谭舒雁; 牧逸风 > all, 100% every seat. My ceiling this lobby was 3rd.

### ROOT CAUSES (honest, ranked):
# #1 FIELDED A 2-ATTACKER RAMP PILE (M-recurrence #8). I literally fielded the 5-attacker board (R15, WON) then reverted to the 2-attacker pile (R16/R17, LOST). REACHABILITY: I held 五行刺+1 the whole time — a 1-card swap.
# #2 SEAT/修为 LOWEST (83). Lost the seat in R16 (vs 牧逸风 90) and R17 (vs 小布 90) — both decisive losses. But note: even going FIRST the board is 0%, so seat alone ≠ the fix; board was the fix.
# #3 NO WIN-CONDITION. 五行 pool has no 万法-class finisher. I needed to either (a) field more attackers earlier, or (b) accept ~3rd and play for survival (bank 命, dodge risk). I did neither — I never built offense.

## ECONOMY (my rolls/round): R1-6=0, R7=5, R8=0, R9=2, R10=0, R11=3, R12=1, R13=0, R14=3, R15=13, R16=3, R17=5 ≈ **35 rolls total**.
#   ★ This was NOT an over-roll — I rolled LESS than the winner. R15's 13-roll dump was the only big one and it landed junk (火灵 stuff absorbed). Discipline was fine; the problem was BOARD CONSTRUCTION and 修为, not roll volume.
#   Winner 牧逸风: 0 rolls R1-R8, then named dumps R9(13)/R11(10)/R13(23)/R17(23). He found 万法 at R17 (24 rolls into that hunt). 小布: absorb-all early, named dumps R9/R11/R12/R15/R18. BOTH had a NAMED late-game win-condition hunt; I never hunted a win-condition because 五行 has none.

### PER-RIVAL:
# - pid0 牧逸风 (WINNER, qi-ramp→万法): W R2,R5,R11,R15 (early, before his engine assembled) | L R16. His 万法 assembled R17 and became unbeatable. 万法 = exhaust qi, 5+5×qi dmg. Beats EVERYONE.
# - pid3 小布 (崩拳 burst, 威震四方+1, 46 体魄): W R1,R4,R7,R9 | L R14,R17. His 173 maxHP + sustained 32-dmg burst out-scales my ramp. Beats 谭舒雁 100%, loses to 牧逸风 first-seat.
# - pid1 谭舒雁 (命理师 内伤 clock): W R3,R6?no(L R6),W R10,R12 | L R6,R8. I beat her overall (she ended weakest, 修为 68).
### SURPRISE: I went 12W-5L yet still died at 命0 with the winner at 命1. The 5 late losses (R13,R14,R16,R17 + R6/R8) were each "expensive" (-19 to -25命). Early dominance doesn't matter if you lose the high-stakes late rounds.
### MECHANICS CONFIRMED: 水势 = ONE end-of-turn hit (gamestate_full.js:3614). 八门金锁阵 = 8 dmg when OPP chases (deal_damage_inner(8), index 3051-3055) + 持续. 木灵·巡林 chase = if HP was added (纳百川/腾浪 qualify). 万法归灵剑 = exhaust all qi, 5+5×qi ATK. 聚灵心法+回响阵纹 = slot1 continuous qi retriggered.

==== LEDGER ENTRY · Game 29 ====
==== LEDGER ENTRY · Game 29 ====
## ARENA Game 29 (g29) — 吾行之 (五行 sect, sidejob 5 阵法师, pid2). RESULT: **NOT 1st — final 命 0 (eliminated R18 vs the winner)**.
# Winner = 谭舒雁 (pid1, 命87). 牧逸风(pid0)/我(pid2)/小布(pid3) all dead 命0.
# W/L (18 battles): L R1(3) L R2(1) L R3(0) W R4(3) L R5(1) W R6(3) W R7(1) L R8(0) L R9(1) L R10(3) W R11(0) L R12(3) W R13(1) W R14(0) L R15(1) W R16(1) L R17(1) L R18(1... actually pid1 first). 7W-11L, died R18.
# FATES: 战斗历练, 五行印记, 悠然葫芦, 五行化身, 五行传承. 修为 ended 89 (谭舒雁 92, 牧逸风 74, 小布 79). Broke 境5 @R13.

## FINAL BOARD FIELDED R18 (★ THE MISTAKE ★): ['水灵·泉涌+1','周天剑阵+1','水灵·纳百川','辟邪阵纹']
#   = I DESTROYED MY OWN BOARD. At R18 I had 8 exchanges and a 8-card hand; I ROLLED AWAY 五行刺+1, 水灵·涛+1,
#   水灵阵, 水灵·汹涌, 水灵·汹涌+1, 水灵·纳百川 (the ENTIRE winning board) to farm 修为, and fielded 4 cards.
#   card_stats(R18): 泉涌 +6qi/0dmg, 周天剑阵 0 dmg, 纳百川 0 dmg, 辟邪 0 dmg, Normal Attack 14 dmg. LOST -29.

## ★★★★★ THE GAME-DECIDING DISCOVERY (yisim-verified THIS review) ★★★★★
## 周天剑阵 PLACEMENT WAS MY FATAL BUG. It is a [持续]N: EVERY card with ATK gets an EXTRA +5 ATK hit for N charges.
#   Placed EARLY (slot 3) its charges burn on small early hits; placed LATE (slot 7) they land on the BIG
#   late-game 水势-scaled attacks (汹涌/涛/五行刺) = +15 dmg exactly when it decides the fight.
#   ENGINE: gamestate_full.js:1937 do_endless_sword_formation() fires when this_card_directly_attacked; 3 charges @lv2.
## THE BOARD THAT BEATS THE WINNER 100%/100% (both seats), verified via sim_matchup + search_board:
#   ['水灵·泉涌+1','水灵阵','水灵·纳百川','水灵·汹涌+1','水灵·汹涌','水灵·涛+1','周天剑阵+1','五行刺+1']
#   vs 谭舒雁's EXACT final board ['天星·牵引','血光之灾','杯弓蛇影'×2,'诸事不宜'×2,'星弈·断','反震心法+1']: **100% FIRST / 100% SECOND**.
#   (The ONLY change from the fielded pile = 周天剑阵 slot3→slot7 and fielding 8 cards not 4.)
#   vs same board with 周天剑阵 at SLOT 3: 100% first / **0% second** — a pure-reorder flip from coin-flip to 100/100.
#   I HAD EVERY CARD. My matrix board was 4 cards. THE MISTAKE WAS R18 BOARD DESTRUCTION, not reachability.
## vs 牧逸风: also 100first/0second; search found 100/100 by swapping IN 须弥阵纹 (@slot8, [跳过]+[再次行动] if 持续 played)
#     → the extra chase-tempo kills him 1 turn before 万法 fires.
## vs 小布: 0first/100second with the plain board; search (with 汹涌+2/纳百川+2 upgrades, or moving 周天剑阵 to SLOT 1)
#     reaches 100/100. Fast-burst race → 周天剑阵 wants SLOT 1 vs him (charges every attack from turn 1), SLOT 7 vs the clock.

## ROOT CAUSES (ranked):
# #1 ★ R18 BOARD DESTRUCTION: rolled my own winning board pieces (五行刺+1, 涛+1, 汹涌/汹涌+1, 纳百川, 水灵阵) into
#   junk at 命0 chasing 修为 — when I was ALREADY at 修为 89 vs her 88 (I led the seat)! Absolute own-goal. Never
#   roll a functioning board piece in a MUST-WIN round; the board wins the fight, 修为 is only a tiebreak.
# #2 ★ 周天剑阵 MISPLACED at slot 3 instead of 7 — the single reorder that flips 0%→100% going second vs the winner.
# #3 Late 境5 (R13) — one round behind 谭舒雁 (R12), fewer phase-5 draws (but I still had the pieces).
# #4 I went SECOND in R18 (her 勤学苦练 + absorbs pushed her past 89). Even so the slot-7 board wins from either seat.

### ECONOMY (my rolls/round): R1=1,R2=0,R3=0,R4=2,R5=0,R6=7,R7=0,R8=0,R9=0,R10=7,R11=0,R12=2,R13=**19**,R14=0,R15=0,R16=3,R17=0,R18=**17**. ≈58 rolls.
#   R6=7 (pre-境5 leak, hit 周天剑阵+1 merge), R10=7 (post-境4, landed the 汹涌 set), R13=19 (POST-境5 SHOTGUN — churned
#   through 纳百川, 不动金刚阵, 水灵·潜遁, 回响阵纹; landed 纳百川 & merged 泉涌+1 but threw away 潜遁/不动金刚阵).
#   R18=17 (FATAL shotgun at 命0 — rolled away the whole board). Winner 谭舒雁 rolled ≈72 but ALL NAMED at her kit
#   (R9=21 landing 反震/血光/诸事/天星; R12=15; R15=8 landing 诸事不宜+杯弓蛇影). NAMED DUMPS >> shotgun churn (8th confirm).

### PER-RIVAL:
# - pid1 谭舒雁 (WINNER, 命理师 内伤 clock + 反震心法): L R2,R5,R9,R10,R12,R15,R17,R18 | W R7,R13,R14,R16. My board BEATS
#   her final board 100/100 with 周天剑阵 at slot 7; I kept fielding wrong/4-card boards. 内伤 ticks ~9-13/turn by t12.
# - pid0 牧逸风 (云剑): W R11,R14 | L R1,R3,R8. 100first/0second plain; 须弥阵纹 variant = 100/100.
# - pid3 小布 (崩拳 burst): W R4,R6 | L R10,R12 (and R1 ghost). Fast race; needs upgrades or 周天剑阵 slot1.
### SURPRISES: (1) A PURE REORDER (周天剑阵 slot3→7) flips a seat-dependent coin-flip into a 100/100 both-seat win vs the
#   eventual champion. (2) I had the winner's kryptonite fully assembled and threw it away at 命0 for 修为 I didn't need.
#   (3) 反震心法 (2 dmg/attack received) does NOT hurt me much — my big 汹涌 hits are few, not many small ones.
### MECHANICS CONFIRMED: 周天剑阵 = +5 ATK per attack, N charges, placement decides which attacks it buffs. 水灵阵 = [持续]
# +1qi per 水灵 card (the qi engine). 泉涌/腾浪 = qi batteries. 须弥阵纹 = [跳过]next + [再次行动] if 持续 played.
# 内伤 = permanent hp loss at victim's turn start. 天星·牵引 triggers 2 opening effects after it (her clock ramp).

==== LEDGER ENTRY · Game 30 ====
## ARENA Game 30 (g30) — 吾行之 (五行 sect, sidejob 5 阵法师, pid2). RESULT: **NOT 1st — final 命 0 (eliminated R16)**.
# Winner = 谭舒雁 (pid1, 命10). 牧逸风(pid0)/我(pid2)/小布(pid3) all eliminated 命0.
# W/L (16 battles): W R1 W R2 W R3 | L R4 W R5?no(L) — actual: W R1,R2,R3,R7,R8,R9,R11,R12,R14 = 9W, L R4,R5,R6,R10,R13,R15,R16 = 7L. Final 命0.
# FATES: 战斗历练, 五行印记, 水灵传承, 五行循环, 五行传承. 修为 ended 80 (谭舒雁 98, 牧逸风 86, 小布 91) = LOWEST-ish. Broke 境5 @R12.

## FINAL BOARD fielded R16: ['水灵·腾浪','木灵·柳纷飞','水灵阵','水灵·潜遁','水灵·纳百川','水灵·汹涌+1','水灵·汹涌+1','周天剑阵+1']
#   ★ MISTAKE: I held 五行刺+1 in hand and fielded only 7 slots worth (五行刺 stayed in hand). Also 木灵·柳纷飞 (a chase filler) and 周天剑阵 LAST (→ 0 charges, per card_stats it dealt 0 dmg).

## ★★★★★★★★★★ THE GAME-DECIDING DISCOVERY (yisim-verified THIS review) ★★★★★★★★★★
## A PURE REORDER OF MY PROVEN 8-CARD BOARD BEATS **BOTH** 谭舒雁 AND 牧逸风 100%/100% BOTH SEATS.
#   BEST BOARD: ['周天剑阵+1','水灵·腾浪','水灵阵','水灵·纳百川','水灵·汹涌+1','水灵·汹涌+1','水灵·潜遁','五行刺+1']
#     vs 谭舒雁 FINAL: 100% first / 100% second (~12t).  vs 牧逸风 FINAL: 100% first / 100% second (~11t).
#     vs 小布 FINAL: 0%/0% (unwinnable — hard ceiling, confirmed).
#   vs my R16 fielded board going FIRST: 0% vs 小布, and I also flubbed R13/R15.
#   ★★ TWO REORDER FIXES (each verified by search_board trace):
#     (1) 周天剑阵+1 → SLOT 1 (was slot 7/8). Trace: "move 周天剑阵 slot7->slot1: 100% first / 100% second vs 牧逸风".
#         WHY: charges must fire from turn 1 so they land on ALL attacks incl. the big late ones; at slot 7 they
#         burned on nothing (0 dmg in R16 card_stats).
#     (2) 水灵·潜遁 → SLOT 6 (was slot 3). Trace: "move 水灵·潜遁 slot3->slot6: 100% first / 100% second vs 谭舒雁".
#         WHY: -40% dmg reduction is wasted on early small hits; at slot 6 it covers her late 星弈·断 / 内伤 ticks.
#     ★ THIS IS THE SAME CLASS OF FIX AS g29's 周天剑阵 slot3→7 flip — ORDER, not composition. 9th confirm: 五行 board
#        is entirely ORDER-SENSITIVE and a pure reorder flips 0%→100%.
## vs the same board WITH 潜遁 at slot 3 (my R15 fielding): 100% first / 0% second vs 谭舒雁 — exactly the coin-flip
#   I lost in R13/R15 (she went first both times → my 0% seat). The reorder makes it seat-independent.

## ROOT CAUSES (ranked, honest):
# #1 ★ FIELDED A SUBOPTIMAL/UNUPGRADED BOARD AT THE DECISIVE MOMENTS. R13 fielded [水灵阵,须弥阵纹,潜遁,纳百川,...]
#    (须弥阵纹 is a proven DUD for me — M87; and no 腾浪 qi engine). R16 fielded 木灵·柳纷飞 filler + 周天剑阵 last.
#    The OPTIMAL board existed in my hand/board from ~R13 onward; I just ordered/mixed it wrong.
# #2 SEAT: lost the 修为 race late (80 vs 98/86/91). But the reorder makes my board BOTH-SEAT vs 谭/牧, so seat is
#    no longer decisive — board construction was the fix, not 修为.
# #3 ✓ SMALLER LEAK (real this game): 须弥阵纹 fielded at R13/R14 — 0%/hurt (M87 reconfirmed: adding it dropped win to 0%).

## ECONOMY (my rolls/round): R1-5=0, R6=21(!!), R7-9=0, R10=3, R11=13, R12=2, R13=5, R14=12, R15=0, R16=2 ≈ 58.
#   ★ R6=21 was a PRE-境4 SHOTGUN (境4) — mostly waste, landed 水灵阵/汹涌 merges but burned 21 exchanges that
#     should have been 修为. R11=13 and R14=12 same class (post-境5 churn). NAMED discipline would've won ~2
#     more seats. Winner 谭舒雁: 73 rolls but nearly ALL NAMED at her exact kit, + her 勤学苦练 fate drew cards on every absorb.
#   ★ The 21-roll R6 shotgun is the 10th consecutive confirmation of the #1 economy leak: shotgun churn >> nothing.

## PER-RIVAL (final board, sim-verified):
# - pid1 谭舒雁 (WINNER, 命理师7 内伤 clock + 诸事不宜): I went W R3,R7,R14 / L R5,R13,R15. FINAL BOARD FIX beats her
#   100/100 both seats (潜遁 slot 6). R15 I had the 潜遁@3 board and lost purely on seat. Her clock ticks 4→8→12→14.
# - pid0 牧逸风 (云剑+阵法师5, 万法 qi-nuke): W R2,R8,R12 / L R4,R10. FINAL BOARD FIX beats him 100/100 both seats
#   (周天剑阵 slot 1). His 万法 fired 50-95 dmg; my reorder out-races it.
# - pid3 小布 (崩拳 burst, 体魄 9, 122 maxHP): W R1,R9,R11,R14 / L R6,R16. **UNWINNABLE — 0%/0% vs his final board,
#   confirmed by search_board (all pools, 21 evals, pre-filter rejects) + matrix (吾行之 0/0).** His 崩拳·寸击/连崩/
#   惊触 burst = 20-28/attack from t4, kills by t7; I end him at 22-30 HP but die. Play for LATER clock / minimize 命.
## SURPRISE: The reorder (周天剑阵 slot1 + 潜遁 slot6) is a UNIVERSAL both-seat fix vs the two bosses I could beat —
#   and I literally held every card. Same lesson as g28/g29: I never lose on reachability, only on FIELDING.
### MECHANICS CONFIRMED (yisim_grep): do_force_of_water() (gamestate_full.js:3198) = ONE end-of-turn hit = current
#   水势 stack, AND (line 2906) 水势 gives +20%/stack to damage_dealt_to_hp_by_atk → 水势 is BOTH a passive clock AND
#   an attack amplifier. 潜遁 damping checked at 4580. 周天剑阵 charges = +5 ATK per attack, N charges, placement decides WHICH attacks.
# ★ NEXT-GAME TARGET BOARD = the BEST BOARD above. KEEP 五行刺+1, KEEP 周天剑阵+1, NEVER field 须弥阵纹.
