"""g30 MASTER BOARD + slot rules for 谭舒雁 命理师 内伤-clock. Print with run_program.
g30 = my first-place WIN (命10, 修为105 highest in lobby)."""

# ★★★★★ g30 MASTER BOARD (yisim 100/100 vs ALL 3 rivals, both seats, ~7-9t kill):
MASTER = ["厄劫缠身", "诸事不宜", "杯弓蛇影", "杯弓蛇影",
          "天星·牵引", "星弈·断", "流水无情", "吉运初显"]

# SLOT RULES (LOAD-BEARING — do NOT swap):
SLOT_RULES = {
    0: "厄劫缠身 — [开局] downgrades OPPONENT'S SAME-SLOT card. slot1 => starves 牧逸风's 聚灵心法 qi-engine AND front-loads the clock vs 小布.",
    1: "诸事不宜 — mitigation keystone. MUST be slot2 (slot3 => board becomes 100%-first/0%-second).",
    2: "杯弓蛇影 — 2 内伤 + immediate tick.",
    3: "杯弓蛇影 — 2 内伤 + immediate tick.",
    4: "天星·牵引 — +2 qi, retrigger the 2 [开局] AFTER it (re-fires 厄劫/诸事 openings).",
    5: "星弈·断 — 16atk closer; [星位] skip a foe card.",
    6: "流水无情 — 6atk + 2 内伤 (always fires: my clock is a debuff).",
    7: "吉运初显 — sustain (+7 HP, opening +4 HP/+4 max).",
}

FLEX_7_8 = ["流水无情", "反震心法", "命运轮回", "落花有意", "探灵", "吉运初显"]  # all give 100/100 vs 小布

KEEP = ["厄劫缠身", "杯弓蛇影", "诸事不宜", "天星·牵引", "流水无情",
        "血光之灾", "命运轮回", "吉运初显", "落花有意"]

ROLL_TARGETS = ["诸事不宜", "杯弓蛇影", "厄劫缠身", "天星·牵引",
                "流水无情", "血光之灾", "吉运初显"]  # priority order

UPGRADE_ORDER = ["厄劫缠身", "杯弓蛇影", "天星·牵引", "星弈·断"]

RULES = """
CORE: 修为=seat=wins. 内伤 clock (not attacks). POSITION is the whole game. Build BOTH-seat boards.
ECONOMY: R1-R11 absorb-all (0-2 rolls). Break 境5 R11-12. Pre-境5 shotgun cap <=8 NAMED rolls.
FATES: combat/传承 fates useless (21 confirmations). Rank economy fates first: 勤学苦练 > 妙手回春 > misc.
g30 KEY: 厄劫 at SLOT 1 (not 2). This ONE move flipped 小布 0%-second -> 100%-second for FREE.
"""

if __name__ == "__main__":
    print("=== g30 MASTER BOARD ===")
    for i, c in enumerate(MASTER):
        print(f"  slot{i+1}: {c:12s} {SLOT_RULES.get(i,'')}")
    print()
    print("FLEX slots 7-8 (any of):", FLEX_7_8)
    print("KEEP (never roll/absorb):", KEEP)
    print("ROLL priority:", " > ".join(ROLL_TARGETS))
    print("UPGRADE priority:", " > ".join(UPGRADE_ORDER))
    print()
    print(RULES)
