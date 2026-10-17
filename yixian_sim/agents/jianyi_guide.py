# -*- coding: utf-8 -*-
"""jianyi_guide — the 剑意 (Sword Intent) 云灵剑宗 archetype from the TapTap guide
https://www.taptap.cn/moment/450813793417563244  ("新手剑意教学 — 猫画师剑意").

Encoded rules (see agents/README.md for the prose):
  * 副职 = 画师 (Painter).
  * 练气 (realm 1) "拖d": DON'T break through; spend every 换牌 fishing the core —
      剑劈×3, 剑挡×3 (2×lv2 ok), 灵气灌注 lv2, 飞牙剑×2, 震雷剑≥1 — while banking 修为
    ("1修等于1牌"), then jump straight up the realms around R7-9 (元婴 by ~R8).
  * 筑基→元婴 (realms 2-4): minimise rolling — bank charges for 化神. Keep 凝意诀/云舞诀
    ("凝意云舞"), 灵气灌注, 水月剑阵/镜花剑阵 ("水月镜花").
  * 天命: 修为 fates first (顿悟 12, 剑韵修炼 16, 道韵传承 10, 副职兼修 188); 林小月 takes
    猫爪 (44) at phase 2 and MUST take 灵猫乱剑 (46) at phase 4; at 化神 斩道 (56) > 修为.
  * 化神 (realm 5): dump the bank chasing 剑意激荡 (1000044, the finisher; lv2 first),
    御空剑阵, 运笔如飞, 飞灵闪影剑, 万法归灵剑, 画龙点睛; the cat cards (青铜猫/猫爪) come off
    the board and 猫薄荷 gets eaten once the burst is online.
  * "一定要多算伤害" → the Oracle search decides the actual board; the template only
    steers rolls / holds / breakthrough timing and is force-offered as a candidate.
"""
from __future__ import annotations

# ---- card ids (base, level 1) ------------------------------------------------
JIANPI, JIANDANG, GUANZHU, FEIYA, ZHENLEI = 1000010, 1000012, 1000006, 1000021, 1000009
NINGYI, YUNWU, SHUIYUE, JINGHUA = 1000017, 1000031, 1000041, 1000046
JIDANG, YUKONG, LIANHUAN, YUNBI, FEILING, WANFA, HUALONG = (
    1000044, 1000025, 1000064, 6000012, 1000043, 1000045, 6000013)
MAOBOHE, LIANBI, QINGTONGMAO, MAOZHUA, LINGMAO_JIAN = 34, 6000002, 37, 8, 9

CORE_R1 = {JIANPI: 3, JIANDANG: 3, GUANZHU: 2, FEIYA: 2, ZHENLEI: 1}   # copies wanted (lv2 = 2)
KEEP_MID = {NINGYI, YUNWU, GUANZHU, SHUIYUE, JINGHUA, JIANPI, JIANDANG, FEIYA, ZHENLEI, LINGMAO_JIAN}
WANT_R5 = [JIDANG, YUKONG, YUNBI, FEILING, WANFA, HUALONG, LIANHUAN]     # priority order
CAT_CARDS = {QINGTONGMAO, MAOZHUA, MAOBOHE, LIANBI}

# ---- fates -------------------------------------------------------------------
CULT_FATES = {12: 3.0, 16: 2.5, 10: 2.0, 188: 2.0}      # 顿悟, 剑韵修炼, 道韵传承, 副职兼修
ZHANDAO = 56                                            # 斩道: 修为-6/-10, 抽 6/9 牌
LIN_XIAOYUE = 1000004
CHAR_MUST = {LIN_XIAOYUE: {2: 44, 4: 46}}               # 猫爪 @phase2, 灵猫乱剑 @phase4

SIDEJOB = 4                                             # 画师 Painter
STALL_UNTIL = 7                                         # hold 练气 through R6 unless core done
JUMP_BY = 9                                             # ...but never past R8

CLOUD_SECT = 1


def applies(p) -> bool:
    return p.sect_prefix == CLOUD_SECT


def base(cid: int) -> int:
    return cid % 10000 if cid >= 10000 else cid


def level(cid: int) -> int:
    return (cid // 10000) % 100 + 1 if cid >= 10000 else 1


def copies_of(cards, b: int) -> int:
    """Copies of base card b counting a lvK card as 2^(K-1) copies."""
    return sum(2 ** (level(c) - 1) for c in cards if base(c) == b)


def core_done(cards) -> bool:
    return all(copies_of(cards, b) >= n for b, n in CORE_R1.items())


def core_progress(cards) -> float:
    return sum(min(copies_of(cards, b), n) for b, n in CORE_R1.items()) / sum(CORE_R1.values())


def wanted(p, rnd: int) -> set:
    """Base ids the archetype never rolls / absorbs at this stage."""
    if p.realm <= 1:
        w = set(CORE_R1) | {MAOBOHE, LIANBI} if p.char_id == LIN_XIAOYUE else set(CORE_R1)
        return w
    if p.realm < 5:
        return set(KEEP_MID)
    return set(KEEP_MID) | set(WANT_R5)


def template_sets(p, slots: int) -> list:
    """Candidate boards to force-offer to the Oracle search (it decides honestly)."""
    have = [c for c in p.board if c] + list(p.hand)
    pri = ([JIDANG, YUKONG, YUNBI, FEILING, WANFA, HUALONG, LIANHUAN] if p.realm >= 5 else []) \
        + [JIANPI, JIANDANG, FEIYA, ZHENLEI, GUANZHU, YUNWU, NINGYI, SHUIYUE, JINGHUA, LINGMAO_JIAN]
    picked = []
    for b in pri:
        for c in sorted((c for c in have if base(c) == b), key=lambda c: -level(c)):
            if len(picked) < slots and c not in picked:
                picked.append(c)
    return [picked] if len(picked) >= min(3, slots) else []


def should_break(p, rnd: int, cards) -> bool:
    """练气 stall: hold realm 1 until the core is assembled or the clock runs out."""
    if p.realm >= 2:
        return True
    if rnd >= JUMP_BY - 1:
        return True
    if rnd >= STALL_UNTIL and core_progress(cards) >= 0.6:
        return True
    return core_done(cards)


def roll_budget(p, rnd: int, rerolls: int) -> int:
    if p.realm <= 1:
        return rerolls                                  # fish the core with everything
    if p.realm < 5:
        return max(0, rerolls - 40)                     # bank (effectively no rolling)
    return rerolls                                      # 化神: dump the bank


def fate_chooser(env, p, offered):
    """修为 fates first; 林小月's must-picks; 斩道 at 化神."""
    import fates as FA
    F = FA.all_fates()
    phase = p.realm                                     # offer happens after realm bump
    must = CHAR_MUST.get(p.char_id, {}).get(phase)
    if must in offered:
        return must

    def score(fid):
        s = 0.0
        if fid == ZHANDAO and p.realm >= 5:
            s += 4.0
        s += CULT_FATES.get(fid, 0.0)
        e = F.get(fid, {}).get("effects", {}) or {}
        s += e.get("cult", 0) * 1.5 + e.get("hp", 0) * 0.5 + e.get("destiny", 0) * 0.3 \
            + e.get("rerolls", 0) * 0.4
        if fid == 16:                                   # 剑韵修炼: +剑意 at battle start
            s += 1.0
        return s
    return max(offered, key=score)
