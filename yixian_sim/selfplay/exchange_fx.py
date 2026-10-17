# -*- coding: utf-8 -*-
"""[置换] EXCHANGE effects — what happens when a card is 换牌'd AWAY.

A handful of cards carry a `[置换]` clause: exchanging them away is the *point* of the
card. Per the FAQ, a card WITH an exchange effect is NOT burned from the pool (`no_penalty`
in draws.DrawBag.reroll), and its effect fires on the exchange.

Implemented (text from the live CardConfig):

  练笔      6000002  [置换]：换牌机会+2
  以画入道  6000009  [置换]：获得1张自身境界的门派牌
  触类旁通  6000010  [置换]：换牌机会+1，获得1张画师以外副职业的牌（筑基期以上）
  妙笔生花  6000015  [置换]：获得1张升级后的牌（金丹期以上）
  阵纹重绘  8000015  [置换]：获得1张持续牌（筑基期以上），换牌机会+1   (阵法师)
  玄冥之水  155      [置换]：换牌机会+2

CARDS GRANTED BY THESE EFFECTS ARE CREATED FROM NOTHING (user-confirmed): they are
appended to the hand WITHOUT decrementing the draw pool, so the card counter is
unaffected. That's what `_grant` does — contrast with fate_fx._draw, which draws from
the bag and burns a copy.

Each handler returns a short human-readable string for the log/replay.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import cards as C
import draws as D
import merge as M

PAINTER = 4                       # 画师 career id


# ── card universes (name lists, independent of the player's remaining bag) ────
def _sect_names(sect_prefix: int, lo: int, hi: int) -> list:
    pool = D.build_pool(int(sect_prefix), max_phase=5)
    return [n for n, d in pool.items() if lo <= d["phase"] <= hi]


def _sidejob_names(career: int, lo: int, hi: int) -> list:
    pool = D.sidejob_pool(int(career), max_phase=5)
    return [n for n, d in pool.items() if lo <= d["phase"] <= hi]


def _own_names(p, lo: int, hi: int) -> list:
    """Everything the player could normally draw (sect + their sidejob)."""
    pool = D.build_pool(p.sect_prefix, career=p.career or 0, max_phase=5)
    return [n for n, d in pool.items() if lo <= d["phase"] <= hi]


def _any_names(lo: int, hi: int) -> list:
    """Every drawable card in the game (all 4 sects + all 7 sidejobs) — the pool a
    '随机惊喜' (好奇心) can land on."""
    out = []
    for s in (1, 2, 3, 4):
        out += _sect_names(s, lo, hi)
    for c in range(1, 8):
        out += _sidejob_names(c, lo, hi)
    return out


_continuous_ids = None


def _continuous_names() -> set:
    """Names of [持续] cards (proxy/card_types.json)."""
    global _continuous_ids
    if _continuous_ids is None:
        f = _HERE.parent / "proxy" / "card_types.json"
        try:
            ids = set(json.loads(f.read_text(encoding="utf-8"))["continuous"])
        except Exception:
            ids = set()
        _continuous_ids = {C.id_to_name(i) for i in ids if C.id_to_name(i)}
    return _continuous_ids


# ── the "from nothing" grant ─────────────────────────────────────────────────
def _grant(env, p, names, level: int = 1):
    """Put ONE card from `names` into hand WITHOUT touching the draw pool.
    level=2 grants the upgraded (Lv2) id when one exists. Returns its display name."""
    names = [n for n in names if C.name_to_base_id(n)]
    if not names:
        return None
    nm = env.state.rng.choice(sorted(set(names)))
    cid = C.name_to_base_id(nm)
    if level > 1:
        up = M.level_up(cid)
        if up:
            cid = up
    p.hand.append(cid)                      # created from nothing: bag.copies untouched
    return nm + ("+1" if level > 1 and cid != C.name_to_base_id(nm) else "")


# ── handlers: fn(env, p) -> str ──────────────────────────────────────────────
def _lianbi(env, p):                                    # 练笔
    p.rerolls += 2
    return "练笔[置换]: 换牌机会+2"


def _yihua_rudao(env, p):                               # 以画入道
    got = _grant(env, p, _sect_names(p.sect_prefix, p.phase, p.phase))
    return f"以画入道[置换]: 获得门派牌(境{p.phase}) {got or '—'}"


def _chulei_pangtong(env, p):                           # 触类旁通
    p.rerolls += 1
    others = [c for c in range(1, 8) if c != PAINTER]
    career = env.state.rng.choice(others)
    got = _grant(env, p, _sidejob_names(career, 2, max(2, p.phase)))
    return f"触类旁通[置换]: 换牌机会+1, 获得副职牌 {got or '—'}"


def _miaobi_shenghua(env, p):                           # 妙笔生花
    if p.phase < 3:
        return "妙笔生花[置换]: 无金丹期牌可得"
    got = _grant(env, p, _own_names(p, 3, p.phase), level=2)
    return f"妙笔生花[置换]: 获得升级牌 {got or '—'}"


def _zhenwen_chonghui(env, p):                          # 阵纹重绘 (阵法师)
    p.rerolls += 1
    cont = _continuous_names()
    got = _grant(env, p, [n for n in _own_names(p, 2, max(2, p.phase)) if n in cont])
    return f"阵纹重绘[置换]: 换牌机会+1, 获得持续牌 {got or '—'}"


def _xuanming_zhishui(env, p):                          # 玄冥之水
    p.rerolls += 2
    return "玄冥之水[置换]: 换牌机会+2"


# ── the 机缘 special cards (99000001-3, granted by the 机缘造化 fate) ─────────
# 门派秘术 (secret enchantment) ids by sect prefix, {card_id: phase} — from the
# wiki's special-secret-enchantments page (user-provided, game3 review).
SECRET_ARTS = {
    1: {1000047: 1, 1000054: 1, 1000048: 2, 1000055: 2, 1000049: 3, 1000056: 3,
        1000062: 3, 1000050: 4, 1000051: 4, 1000053: 5, 1000057: 5, 1000061: 5,
        1000052: 6, 1000058: 6},
    2: {4000047: 1, 4000053: 1, 4000048: 2, 4000054: 2, 4000050: 3, 4000055: 3,
        4000051: 4, 4000056: 4, 4000064: 4, 4000049: 5, 4000057: 5, 4000065: 5,
        4000052: 6, 4000058: 6},
    3: {7000068: 1, 7000069: 1, 7000070: 1, 7000071: 1, 7000072: 1, 7000048: 2,
        7000049: 2, 7000063: 2, 7000050: 3, 7000055: 3, 7000064: 3, 7000046: 4,
        7000047: 4, 7000051: 4, 7000044: 5, 7000045: 5, 7000052: 6, 7000065: 6},
    4: {10000053: 1, 10000054: 1, 10000055: 2, 10000056: 2, 10000058: 3,
        10000061: 3, 10000057: 4, 10000060: 4, 10000067: 4, 10000062: 5,
        10000064: 5, 10000065: 6, 10000066: 6},
}


def _grant_group(env, p, pairs, label, cid):
    """Grant one random card from a special group, from nothing. The granted
    card's phase MATCHES the rolled 机缘 card's own version (its level), with a
    10% chance of one phase higher (user ruling, game4 review R6). Falls back
    down-phase when the exact tier has no cards."""
    want = ((int(cid) // 10000) % 100) + 1 if cid else int(p.phase)
    if env.state.rng.random() < 0.10:
        want += 1
    for ph in range(min(want, 6), 0, -1):
        pool = sorted(c for c, cph in pairs if cph == ph)
        if pool:
            got = _grant_id(env, p, env.state.rng.choice(pool))
            return f"{label}(境{ph}) {got}"
    return f"{label}: 无可得牌"


def _zhongbao_xianshi(env, p, cid=None):                # 重宝现世 → 法宝牌
    pairs = [(c, ph) for c, ph in _treasure_pet_ids() if c < 99000200]
    return _grant_group(env, p, pairs, "重宝现世[置换]: 获得法宝牌", cid)


def _lingchong_renzhu(env, p, cid=None):                # 灵宠认主 → 灵宠牌
    pairs = [(c, ph) for c, ph in _treasure_pet_ids() if c >= 99000200]
    return _grant_group(env, p, pairs, "灵宠认主[置换]: 获得灵宠牌", cid)


def _mishu_chuancheng(env, p, cid=None):                # 秘术传承 → 门派秘术牌
    arts = SECRET_ARTS.get(int(p.sect_prefix), {})
    return _grant_group(env, p, list(arts.items()), "秘术传承[置换]: 获得门派秘术牌", cid)


_BY_NAME = {
    "练笔": _lianbi,
    "以画入道": _yihua_rudao,
    "触类旁通": _chulei_pangtong,
    "妙笔生花": _miaobi_shenghua,
    "阵纹重绘": _zhenwen_chonghui,
    "玄冥之水": _xuanming_zhishui,
    "重宝现世": _zhongbao_xianshi,
    "灵宠认主": _lingchong_renzhu,
    "秘术传承": _mishu_chuancheng,
}


def effect_for(card_id: int):
    """The [置换] handler for a card id (any level), or None. Handlers that take
    a `cid` kwarg (the 机缘 group cards — their LEVEL sets the granted phase)
    get the concrete id bound in."""
    nm = C.id_to_name(int(card_id))
    fn = _BY_NAME.get((nm or "").replace("•", "·"))
    if fn is not None and "cid" in fn.__code__.co_varnames[:fn.__code__.co_argcount]:
        import functools
        return functools.partial(fn, cid=int(card_id))
    return fn


def has_effect(card_id: int) -> bool:
    return effect_for(card_id) is not None


# ── 好奇心 (林小月 innate, fate 129) ──────────────────────────────────────────
# 使用最后1次换牌机会时，会换到随机惊喜并加1次换牌机会（最多触发9次）.
# The "随机惊喜" table (user-specified):
#   · on the LAST curiosity charge, if 猫薄荷 hasn't been received yet → 猫薄荷 (pity)
#   · else 90%: one of the 5 cat cards, uniform 1/5 (all phase-1, start-of-game cards)
#   · else 10%: a 法宝/灵宠 (talisman or spirit-pet) card of phase ≤ your current phase
# Everything it grants is created from nothing (the draw pool is untouched).
CURIOSITY_MAX = 9
CATNIP = 34                                        # 猫薄荷
CAT_CARDS = (33, 34, 35, 36, 37)                   # 小鱼干 猫薄荷 逗猫棒 云剑·飞砂 青铜猫
CAT_RATE = 0.90
_TREASURE_RANGE = (99000100, 99000299)             # 法宝 (…1xx) + 灵宠 (…2xx);
                                                   # the 99000000-05 event cards are NOT included
_tp_cache = None


def _treasure_pet_ids() -> list:
    """[(card_id, phase)] for every 法宝/灵宠 card, from tools/card_phases.json."""
    global _tp_cache
    if _tp_cache is None:
        f = _HERE.parent / "tools" / "card_phases.json"
        out = []
        try:
            for k, v in json.loads(f.read_text(encoding="utf-8")).items():
                cid = int(k)
                if _TREASURE_RANGE[0] <= cid <= _TREASURE_RANGE[1] and v.get("phase"):
                    out.append((cid, int(v["phase"])))
        except Exception:
            pass
        _tp_cache = out
    return _tp_cache


def _grant_id(env, p, cid: int):
    """Put a specific card id in hand, created from nothing."""
    p.hand.append(int(cid))
    return C.id_to_name(int(cid))


def curiosity_surprise(env, p):
    """Roll the 随机惊喜 table. Returns (name, True) when it fired."""
    st = getattr(p, "_fx_state", None)
    if st is None:
        st = p._fx_state = {}
    used = st.get("curiosity", 0)
    if used >= CURIOSITY_MAX:
        return None, False
    st["curiosity"] = used + 1
    rng = env.state.rng

    # last charge + no catnip yet → guaranteed 猫薄荷
    if (CURIOSITY_MAX - used) == 1 and not st.get("catnip"):
        st["catnip"] = True
        p.rerolls += 1
        return _grant_id(env, p, CATNIP), True

    if rng.random() < CAT_RATE:
        cid = rng.choice(CAT_CARDS)                # uniform 1/5 among the cat cards
        if cid == CATNIP:
            st["catnip"] = True
    else:                                          # 10%: 法宝 / 灵宠 of phase ≤ current
        pool = [c for c, ph in _treasure_pet_ids() if ph <= p.phase]
        if not pool:
            cid = rng.choice(CAT_CARDS)
            if cid == CATNIP:
                st["catnip"] = True
        else:
            cid = rng.choice(sorted(pool))
    p.rerolls += 1
    return _grant_id(env, p, cid), True


if __name__ == "__main__":
    print("[置换] cards:", ", ".join(_BY_NAME))
    print("continuous names:", len(_continuous_names()))
    print("any-names @phase3:", len(_any_names(1, 3)))
