# 谭舒雁 (命理师7) PLAYBOOK v66 — post-g30. 境4→(aiming 境5). Carries v65 rules + R8 leak fix.
# ★ g30 = best game (FIRST PLACE, 命10, 修为105, 境5). v66 adds the R8 ROLL-FUEL lesson (see M8).

# ============================================================
# ★★★★★★★ CORE PRINCIPLES ★★★★★★★
# ============================================================
# [CP1] 修为 = SEAT = WINS. (g28,g29,g30) Absorb EVERY non-keep card for 修为.
# [CP2] 内伤 CLOCK is the win-con (bypasses 防, permanent, ticks at FOE turn-start).
#       Clock cards = 血光之灾, 杯弓蛇影, 厄劫缠身, 流水无情, 诸事不宜(mitig), 命运轮回(sustain+retrigger).
# [CP3] POSITION IS THE WHOLE GAME. sim BOTH seats at multiple orderings.
# [CP4] BUILD A BOTH-SEAT BOARD. Do NOT trust a 修为 lead (opp absorbs in-round).
# [CP5] NEVER roll/absorb a KEEP-LIST card. KEEP: 厄劫缠身, 杯弓蛇影, 诸事不宜, 天星·牵引, 流水无情,
#       血光之灾, 命运轮回, 吉运初显, 落花有意.  ★★★ THIS INCLUDES ROLLING THEM AS FUEL. (g33 violation!)
# [CP6] R1-R11 = ABSORB-ALL, 0-2 rolls/round. Break 境5 R11-R12.
# [CP7] COMBAT/传承 FATES ARE COMBAT-IRRELEVANT for the 内伤 kit. Take economy fates.

# ============================================================
# ★★★★★★★ THE MASTER BOARD (g30 — current best) ★★★★★★★
# ============================================================
#   ['厄劫缠身','诸事不宜','杯弓蛇影','杯弓蛇影','天星·牵引','星弈·断','流水无情','吉运初显']
#   SLOT RULES: slot1=厄劫(engine-starve/clock-front). slot2=诸事不宜(mitig keystone; MUST be slot2 or lose 2nd seat).
#   slot3-4=杯弓×2. slot5=天星·牵引(retrigger openings). slot6=星弈·断. slot7-8=sustain/clock.
#   NOT all available pre-境5: 厄劫/命运轮回/星弈·断 are 境5-LOCKED. Pre-境5 usable: 诸事不宜,杯弓蛇影,
#   天星·牵引,流水无情,血光之灾,吉运初显,反震心法,落花有意. → Build a PRE-境5 clock board with these!

# ============================================================
# ★ MATCHUPS ★
# ============================================================
# pid3 小布 — 崩拳 BURST + 气势 + 身法 auto-chase, 阵法师5. Kill window t5-t9. 破空爪(16atk) + 崩拳 burst ~34.
#   His as-is board: a 3-card clock board (血光+流水+吉运初显) WINS 100% (9t). A 2-card board LOSES (0-2 HP gap).
#   ★ KEY: vs 小布 I NEED SUSTAIN (吉运初显/+11HP) to survive his burst until my clock kills him t9.
#   Without sustain I lose by ~2-3 HP. His +1-lobby beats 3-card board 0/0 → win the realistic case.

# ============================================================
# MECHANICS ============================================================
# (same as v65: 厄劫 downgrade, 杯弓 burst-tick, 诸事不宜 mitigation, 天星·牵引 retrigger, 内伤 at victim turn-start)

# ============================================================
# ★ SCHEDULE / ROLLS ★
# ============================================================
# R1-R11: ABSORB-ALL non-keep. 0-2 rolls/round. Break 境5 by R11-R12 (境5@55 修为).
# ★ ONLY roll NAMED targets {诸事不宜 > 杯弓蛇影 > 厄劫缠身 > 天星·牵引}, CAP ≤8, and KEEP 1 junk card as roll fuel.
#   If hand is EMPTY you CANNOT roll — so DON'T absorb the last card if you plan to roll.
# R12+: once board set, STOP rolling. Bank ≤24 pre-grant.

# ============================================================
# MISTAKES + FIXES
# ============================================================
# [M1] ★ 厄劫 at slot1 (engine-starve AND clock front-load).
# [M2] ★ 诸事不宜 MUST be slot2 (else lose 2nd seat).
# [M3] NEVER roll/absorb a KEEP-LIST card. (5+ games)
# [M4] NEVER field 星弈/落雷 pile (no clock = lose). BAN-field: 海底捞月.
# [M5] Pre-境5 shotgun cap ≤8 NAMED rolls.
# [M6] Build a BOTH-SEAT board; don't trust 修为 lead.
# [M7] 反震心法 situational slot7/8 filler (not banned).
# [M8] ★★★ R8 LEAK (this game): absorbed ALL 3 dealt cards → EMPTY HAND → had to TAKE BACK a keep-list
#      card (吉运初显) to roll → violated CP5, LOST my sustain → 2-card board LOST to 小布 0-2HP.
#      FIX: (a) keep ≥1 junk card as roll fuel; (b) NEVER take back a keep-list card just to roll it —
#      instead eat the empty hand and go to next round's deal; (c) 6 straight rolls whose every result was
#      junk shows the roll pool is huge — pre-境5 rolling is a losing bet. ABSORB and move on.
# [M9] vs burst opponents (小布), SUSTAIN (吉运初显 +11HP) is LOAD-BEARING — prioritize keeping it.

# ============================================================
# RECIPES ============================================================
# TURN RECIPE: 1) absorb non-keep hand (but keep 1 junk as roll fuel if rolling). 2) determine seat.
#   3) set board (pre-境5: 诸事不宜/杯弓/血光/流水/吉运初显 + 反震/落花). 4) sim_matchup BOTH seats vs announced
#   opp EXACT last board AND +1. 5) win the realistic (0-2 upgrade) case. 6) named rolls only, ≤8.
# PRE-境5 CLOCK BOARD (fallback, all 境4-): 血光之灾 · 流水无情 · 吉运初显 · 杯弓蛇影 · 诸事不宜 · 反震心法 ...
