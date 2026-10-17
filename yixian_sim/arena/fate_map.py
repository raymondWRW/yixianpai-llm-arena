# -*- coding: utf-8 -*-
"""fate_map — forward combat-side 天命 effects into yisim battle payloads.

yisim expresses fate effects as input fields:
  * tiered fates:  p{pick_phase}_{slug}_stacks  (magnitude scales with the
    phase the fate was picked at; picking the same fate at two gates yields
    two different fields, matching the real game's stacking)
  * untiered fates (character lines): a single {slug}_stacks field
  * the 化身/keep-1-命 family is applied by yisim itself inside
    apply_destiny_damage — the engine consumes the stack economy-side when a
    battle log shows the save fired.

Verified against gamestate_full.js apply_p{2..5}_fates_setup / reset().
Fates NOT listed here either have pure economy effects (already applied by the
env: hp/cult/命/rolls/card grants) or are flagged UNIMPLEMENTED in the referee
report when a seat holds them.
"""

# our fate id -> yisim tiered slug (field = f"p{phase}_{slug}_stacks")
TIERED = {
    16: "sword_rhyme_cultivate",     # 剑韵修炼
    30: "divination",                # 卜卦
    31: "stargaze",                  # 观星
    57: "sword_formation_guard",     # 剑阵守护
    69: "rule_of_the_cloud",         # 云之道
    70: "mad_obsession",             # 狂之执念 (p4/p5 only in yisim)
    71: "post_strike",               # 后发制人
    102: "cycle_of_five_elements",   # 五行循环
    103: "astral_eclipse",           # 星蚀
    120: "rejuvenation",             # 妙手回春
    127: "mutual_growth",            # 相生相成
    128: "concentrated_element",     # 五行专一
    13: "store_qi",                  # 储纳灵气
    145: "full_of_force",            # 气势充沛
    149: "regenerating_body",        # 再生之躯
    150: "mark_of_dark_heart",       # 冥心烙印
    176: "firmness_body",            # 筋骨健壮
}

# our fate id -> yisim untiered field
UNTIERED = {
    66: "sword_in_sheathed_stacks",        # 剑不出鞘 (牧逸风 境2)
    14: "endurance_as_cloud_sea_stacks",   # 云海连绵 (牧逸风 境3)
    64: "birdie_wind_stacks",              # 雪羽清风 (谭舒雁 境3)
    82: "mark_of_five_elements_stacks",    # 五行印记 (吾行之 境2)
    153: "unbounded_qi_stacks",            # 灵涌不竭 (小布 境3)
    177: "unwavering_soul_stacks",         # 修玄不泯 (小布 境5)
    45: "cat_soul_bless_stacks",           # 猫魂庇佑 (completeness)
    # 化身 family — yisim's apply_destiny_damage honors these:
    7: "shade_of_cloud_stacks",            # 云影化身 (牧逸风 境4)
    65: "avatar_of_bird_shade_stacks",     # 雁影化身 (谭舒雁 境4)
    83: "avatar_of_five_elements_stacks",  # 五行化身 (吾行之 境4)
    154: "undying_body_stacks",            # 生机不灭 (小布 境4)
}

AVATAR_FATES = {7, 65, 83, 154}

# fates whose effects are handled by the ARENA ENGINE (economy hooks), so a
# missing yisim mapping is fine:
ENGINE_HOOKS = {
    80,    # 战斗历练: win -> +2 rolls (fate_fx BATTLE_FX)
    72,    # 易数化劫: loss -> +1 roll
    175,   # 历战不屈: loss -> +1 max HP (permanent)
    151,   # 磨砺不止: per 7 命 lost -> +1 roll (小布 innate)
    29,    # 勤学苦练: per 8 absorbs -> draw 1 (谭舒雁 innate)
    18,    # 云雾变幻: first roll each round free (env.reroll, 牧逸风 innate)
    129,   # 好奇心 (not in this lobby; env.reroll)
}

# pure-economy fates the env already applies (stats / card grants / pools):
ECONOMY_OK = {1, 4, 5, 6, 8, 9, 12, 17, 42, 53, 54, 55, 56, 58, 59, 63, 73, 74,
              75, 76, 77, 81, 116, 117, 118, 119, 123, 143, 144, 146, 152, 188}


def combat_fields(talents, talent_phases, consumed_avatars=()) -> dict:
    """Build the extra yisim input fields for a player's fate list."""
    fields = {}
    for fid in talents:
        fid = int(fid)
        if fid in AVATAR_FATES and fid in consumed_avatars:
            continue
        if fid in TIERED:
            ph = int(talent_phases.get(fid, 0) or 0)
            ph = min(max(ph, 2), 5)
            key = f"p{ph}_{TIERED[fid]}_stacks"
            fields[key] = fields.get(key, 0) + 1
        elif fid in UNTIERED:
            key = UNTIERED[fid]
            fields[key] = fields.get(key, 0) + 1
    return fields


def unimplemented(talents) -> list:
    """Fate ids a seat holds that neither yisim nor the engine covers."""
    known = set(TIERED) | set(UNTIERED) | ENGINE_HOOKS | ECONOMY_OK
    return [int(f) for f in talents if int(f) not in known]
