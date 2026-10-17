# 吾行之 (五行 sect, sidejob 5 阵法师) STRATEGY v720 (after g30 R16 vs 小布).
# GAMES: g19 3rd · g20 NOT-1st · g21 LAST · g22 LAST · g23 W · g24 W · g25 LAST · g26 NOT-1st · g27 命0 · g28 命0 · g29 命0 · g30 命0

## ============ ★★★★★★★★★ CORE PRINCIPLES ★★★★★★★★★ ============
# CP1 ★★★★★ 水灵 MUST SPEND 水势 WITH ATTACKERS + HAVE A QI ENGINE.
# CP1b ★★★★★★ QI IS THE HARD BOTTLENECK. Dry engine → wasted turns. 水灵·腾浪 AS SLOT 1/2 (qi upfront) is the fix.
# CP1c ★★★★★ SEAT/修为 DECIDES near-even matchups (absorb EVERY spare). [g30 R17, g31 R13, g32 R14/R15, g30 R13/R15]
# CP2 ★★★★★ FIELD 7-8 CARDS. [g29]
# CP3 ★★★★★★ 周天剑阵 ORDER IS LOAD-BEARING: it gives +5 ATK per attack for N charges — placed LATE it burns on
#   nothing (0 dmg in g30 R16); placed SLOT 1 it lands on ALL attacks. [g29 slot3→7 vs clock; g30 slot1 vs engine]
# CP4 ★★★★★ NEVER ROLL/FIELD-WRONG A WORKING BOARD PIECE IN A MUST-WIN ROUND. [g29 R18, g30 R13/R16]
# CP5 ★★★★★ 五行 IS AN ORDER-SENSITIVE BOARD. A PURE REORDER flips 0%→100% repeatedly. ALWAYS search_order before
#   concluding a matchup is lost. [g29 (周天剑阵 3→7), g30 (周天剑阵 7→1, 潜遁 3→6)] — 9+ confirmations.
# CP6 ★★★★★★ g30 TARGET BOARD (verified 100/100 vs 谭舒雁 AND 牧逸风):
#   ['周天剑阵+1','水灵·腾浪','水灵阵','水灵·纳百川','水灵·汹涌+1','水灵·汹涌+1','水灵·潜遁','五行刺+1']
#   - 周天剑阵 SLOT 1 (charges fire from t1). 腾浪 SLOT 2 (qi). 潜遁 SLOT 6 (late -40%, covers the big late hits).
#   - KEEP 五行刺+1 (scales with any active 五行). KEEP both 汹涌+1.
# CP7 ★★★★★ 五行 HAS NO WIN-CON vs 崩拳 BURST (小布). 0%/0% vs his final board (all pools, search_board rejected).
#   PLAY FOR PLACEMENT: vs 小布, accept the loss, minimize 命, never churn the board chasing him.

## ============ ★ MATCHUPS ============
# - pid1 谭舒雁 (命理师7 内伤 clock + 诸事不宜 mitigation): 内伤 is NOT an attack (潜遁 does NOT block it).
#   ★ BEST BOARD (CP6) = 100%/100% BOTH SEATS (~12t). WINNABLE. Key: 潜遁 SLOT 6 (late), not slot 3.
#   Her clock ramps 4→8→12→14. My 水势 end-of-turn + 周天剑阵 + 汹涌 out-races it.
# - pid0 牧逸风 (云剑+阵法师5, 聚灵+回响→万法 qi-nuke): ★ BEST BOARD (CP6) = 100%/100% BOTH SEATS (~11t).
#   Key: 周天剑阵 SLOT 1 (fires from t1, out-races his 万法). His 万法 hits 50-95 dmg — KILL BEFORE IT.
# - pid3 小布 (崩拳 burst, 体魄/HP-stack 122+ maxHP): **UNWINNABLE** 0%/0% (confirmed g28 + g30). His burst 20-28/t
#   from t4 kills by t7; his HP alone out-scales. Play for a LATER clock / minimize 命 loss. Do NOT waste rolls.
# UNIVERSAL RECIPE: 周天剑阵(slot1) + 腾浪(qi) + 水灵阵 + 纳百川 + 汹涌×2 + 潜遁(slot6) + 五行刺. +须弥阵纹 = DUD.

## ======================= ★ SCHEDULE / ROLLS =======================
# Grants +6 R13+ (fills to 25). Land ≤24 before a grant round.
# NAMED-TARGET ROLLS only: {纳百川,泉涌,腾浪,波澜,涛,汹涌,八门,五行刺,周天剑阵,潜遁}. ≤6/round, STOP on hit.
# ★★★ KILL THE SHOTGUN. g30 R6=21 (pre-境4), R11=13, R14=12 = 10th straight confirmation that shotgun churn is the
#   #1 economy leak. Absorb everything for 修为 instead. [g28 R15=13, g29 R13=19/R18=17, g30 R6=21/R11=13/R14=12]
# absorb burns nothing and gives 修为 → absorb EVERY spare. roll burns 3 sect/2 sidejob.

## ======================= ★ MECHANICS (verified yisim_grep) =======================
# 水势 = ONE end-of-turn hit = current stack (do_force_of_water, gamestate_full.js:3198) AND +20%/stack to
#   damage_dealt_to_hp_by_atk (line 2906) → 水势 is BOTH a passive clock AND an attack amplifier.
# 汹涌=14+#水势 (lv2=14). 涛=flat 10/13/16. 腾浪=+2qi +heal +水势. 潜遁 damping checked line 4580 (-40%, NOT vs 内伤).
# 水灵阵: 持续, +1qi per 水灵 card. 纳百川: +3水势 +heal(6+#水势). 周天剑阵: +5 ATK/attack, N charges, placement decides WHICH.
# Board ≤2 [持续]/[消耗]. 修为 = seat (tie=coinflip). Breaking 境5 @修为55 (or 体魄55).
# ★ sim_matchup "opp +1 lvl" = ALL 8 cards upgraded = pessimistic; judge realistic partial.

## ======================= ★ NAMED FIXES =======================
# M84 NEVER roll a working board piece in a must-win round.  M85 FIELD 7-8 CARDS.
# M86 ★ vs 内伤-clock: pure ramp STALLS. Need 腾浪 + attackers. WIN seat or have a both-seat board.
# M87 ★ 须弥阵纹 = DUD for me. g29: adding it dropped win to 0%. g30 R13: fielded it, lost. NEVER field it.
# M88 ★ Don't trust "opp +1 lvl" = 0% as a reason to churn. Field the proven board, absorb for 修为.
# M89 ★★★ REORDER BEFORE YOU GIVE UP. 周天剑阵 slot1 + 潜遁 slot6 flips 0%→100% both seats vs 谭/牧. VERIFY the exact slot.
# M90 ★★★ FIELD EVERY KEEP CARD YOU HOLD. g30 R16 I held 五行刺+1 in hand and left a slot weak. No exceptions at 命0.

## ======================= ★ NEXT-GAME DECISION RULES =======================
# - R2 sidejob = 5 (阵法师). Absorb spares, ≤2-4 NAMED rolls/round, LAND ≤24 pre-grant. Target 境5 by R11-12.
# - BEFORE EVERY set_board: build CP6 ORDER; sim_matchup BOTH seats vs as-is AND +1.
# - If a matchup sims 0%: FIRST try the CP6 reorder, THEN a search_board on order only (lock all cards), THEN give up.
# - 天命 priority: 水灵传承 > 五行传承/化身 > 五行循环 > economy. (A/B test next game.)
# - vs 小布 (BURST): unwinnable; minimize 命, play a longer clock, don't churn.
# - vs 谭舒雁/牧逸风: field CP6 → 100/100 both seats. This was the whole game.
# - ALWAYS try 周天剑阵 at slot 1 and 潜遁 at slot 6 as the default order.
