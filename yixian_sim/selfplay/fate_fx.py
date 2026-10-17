# -*- coding: utf-8 -*-
"""Fate EFFECT ENGINE — the non-stat fate effects and character innates.

fates.apply() handles one-time STAT deltas (HP/修为/体魄/命元/换牌). This module
handles everything else, on the right trigger:

  · on_select      — when the fate is picked (or an innate granted): card DRAWS
                     (抽N张…牌, parsed generically) + hand-coded one-offs.
  · on_round_start — per-round passives (e.g. 花沁蕊 五行润养: +命元 per element).
  · on_battle_end  — per-battle triggers (e.g. 战斗历练: +换牌 on a win).
  · on_breakthrough— per-breakthrough (e.g. 灵阵精通: gain a card).

Effects that live entirely INSIDE combat (战斗开始时加X防/灵气/状态, [无视防御], …)
stay with the Oracle via the talent id — not re-implemented here. Card GRANTS of
specific derivation cards (获得1张“云剑”牌) are approximated as a generic draw.
Hand-coded tables cover the notable/impactful fates + character innates; the long
tail of combat fates is intentionally left to the Oracle. # STUB (long tail)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import cards as C
import fates as FA

_ELEMENTS = ("金", "木", "水", "火", "土")


_physique_names = None


def _phys_names() -> set:
    """Names of [体魄]-granting cards (for 抽…加[体魄]的牌)."""
    global _physique_names
    if _physique_names is None:
        import body
        _physique_names = {C.id_to_name(cid) for cid in body._grants()}
    return _physique_names


def _allow_for(subset: str, bag):
    """A name-predicate for a fate draw's card TYPE."""
    if subset == "sidejob":
        return lambda nm: nm in bag.sidejob
    if subset == "sect":
        return lambda nm: nm not in bag.sidejob
    if subset == "phase2":                          # 筑基期 = Foundation = phase 2
        return lambda nm: bag.phase.get(nm, 1) == 2
    if subset == "element":                         # 五行: 金/木/水/火/土 灵
        return lambda nm: any(e + "灵" in nm for e in _ELEMENTS)
    if subset == "physique":
        phys = _phys_names()
        return lambda nm: nm in phys
    if subset == "yunjian":                         # “云剑”牌 (e.g. 云海连绵's grant)
        return lambda nm: nm.startswith("云剑")
    if subset == "kuangjian":                       # “狂剑”牌 (狂之执念's grant)
        return lambda nm: nm.startswith("狂剑")
    if subset == "lingjian":                        # “灵剑”牌 (灵剑传承's grant)
        return lambda nm: nm.endswith("灵剑")
    return lambda nm: True                           # any


# ── generic helpers ───────────────────────────────────────────────────────────
def _draw(env, p, n: int, subset: str = "any"):
    """Draw n cards of a given TYPE (subset) into the player's hand."""
    if n <= 0 or p.bag is None:
        return
    dealt = p.bag.deal_subset(n, p.phase, env.state.rng, _allow_for(subset, p.bag))
    p.hand.extend(C.names_to_ids(dealt))


def _distinct_elements(p) -> int:
    """Distinct 五行 (金木水火土) among the player's board+hand card names — a proxy
    for 花沁蕊's '卡组中每有1种不同五行'."""
    seen = set()
    for cid in [c for c in p.board if c] + list(p.hand):
        nm = C.id_to_name(cid)
        for e in _ELEMENTS:
            if e + "灵" in nm:
                seen.add(e)
    return len(seen)


# ── on_select: generic card-draw parse + hand-coded one-offs ──────────────────
def _subset_of(desc: str) -> str:
    """Map a draw/grant clause to a card-type subset for filtered drawing."""
    if "云剑" in desc:
        return "yunjian"
    if "狂剑" in desc:
        return "kuangjian"
    if "灵剑" in desc:
        return "lingjian"
    if "副职" in desc:
        return "sidejob"
    if "门派" in desc:
        return "sect"
    if "筑基期" in desc:
        return "phase2"
    if "体魄" in desc:
        return "physique"
    if "五行" in desc or any(e + "灵" in desc for e in _ELEMENTS):
        return "element"
    return "any"


def _select_draw(env, p, fid, desc=None):
    if desc is None:
        desc = FA.all_fates().get(int(fid), {}).get("desc", "")
    # only the clause up to the first conditional keyword is an immediate draw
    head = re.split(r"每|之后|战斗中|突破|下次|下一次", desc)[0]
    m = re.search(r"抽(\d*)张([^牌]*?)牌", head)      # 抽N张<type>牌
    if m:
        _draw(env, p, int(m.group(1) or 1), _subset_of(m.group(0)))
    g = re.search(r"(?:立刻)?获得(\d*)张([^牌]*?)牌", head)   # 获得N张<type>牌 (grant≈typed draw)
    if g and not m:
        _draw(env, p, int(g.group(1) or 1), _subset_of(g.group(0)))


def on_select(env, p, fid, desc=None):
    fx = SELECT_FX.get(int(fid))           # desc = the PHASE VERSION's resolved text
    if fx:                                 # (grant counts scale with phase)
        fx(env, p)                         # a hand-coded fx OWNS the fate's grant …
    else:
        _select_draw(env, p, fid, desc=desc)   # … otherwise parse 抽/获得N张<type>牌


# ── trigger dispatch ──────────────────────────────────────────────────────────
def on_round_start(env, p):
    for fid in list(p.talents):
        fx = ROUND_FX.get(int(fid))
        if fx:
            fx(env, p)


def on_battle_end(env, p, won: bool, margin: float):
    for fid in list(p.talents):
        fx = BATTLE_FX.get(int(fid))
        if fx:
            fx(env, p, won, margin)


def on_breakthrough(env, p):
    for fid in list(p.talents):
        fx = BREAK_FX.get(int(fid))
        if fx:
            fx(env, p)


# ── hand-coded effect tables (base fate ids) ──────────────────────────────────
def _swap_talent(p, old, new):
    if old in p.talents:
        p.talents[p.talents.index(old)] = new
    p._fx_state = getattr(p, "_fx_state", {})


def _wuxing_runyang(env, p):                        # 花沁蕊 五行润养 (133)
    """Round start: +命元 per distinct 五行 in deck; at 15 accrued → +1 修为 and
    become 桃枝如意 (134)."""
    st = getattr(p, "_fx_state", None)
    if st is None:
        st = p._fx_state = {}
    gain = _distinct_elements(p)
    p.destiny += gain
    st["runyang"] = st.get("runyang", 0) + gain
    if st["runyang"] >= 15 and 133 in p.talents:
        p.cultivation += 1
        _swap_talent(p, 133, 134)                   # 桃枝如意 = combat (Oracle handles)


def _zhandou_lilian(env, p, won, margin):           # 战斗历练: +2 换牌 on a win
    if won:
        p.rerolls += 2


def _lingzhen_jingtong(env, p):                     # 灵阵精通: gain a 五行阵 card each breakthrough
    _draw(env, p, 1)


def _grant_card(env, p, base_id):
    """A fate that puts a SPECIFIC card in hand (龙瑶's 唤雨/九霄玲珑镯)."""
    p.hand.append(int(base_id))


# Tables are keyed by fate NAME then resolved to the live base id (robust to id
# shifts). fn signatures: SELECT/ROUND (env,p); BATTLE (env,p,won,margin); BREAK (env,p).
def _lingmao_tayun(env, p):
    """林小月 phase-5 灵猫踏云: 修为减1 (fates.apply), 获得1张“云剑”牌（金丹期以上）;
    the in-battle '每次使用云剑加1灵气' rides the talent id into the Oracle."""
    lo = 3
    hi = max(lo, p.phase)
    names = [nm for nm, ph in p.bag.phase.items()
             if lo <= ph <= hi and nm.replace("•", "·").startswith("云剑")]
    if names:                                        # granted, not drawn: no pool burn
        cid = C.name_to_base_id(env.state.rng.choice(sorted(names)))
        if cid:
            p.hand.append(cid)


_SELECT_BY_NAME = {
    "铸剑师": lambda env, p: _draw(env, p, 1),      # 陆剑心 innate: start with a card
    # 龙瑶 phase-4/5 char fates add their SPECIAL CARD to hand (user-confirmed):
    "唤雨": lambda env, p: _grant_card(env, p, 15),        # 云剑•唤雨
    "九霄玲珑镯": lambda env, p: _grant_card(env, p, 16),  # 九霄玲珑镯
    # 林小月's cat line — each grants its named card (ids 8/9 are event cards, never
    # in the draw pool). 好奇心 (innate) lives in env.reroll; 猫魂庇佑 in env.apply_battle.
    # 机缘造化: grants ONE random 机缘 special card (user rulings, game3+4 reviews) —
    # 重宝现世/灵宠认主/秘术传承 at the PICK PHASE's version (level = phase), each a
    # [置换] card that rolls into its group at that same phase (10% one higher).
    "机缘造化": lambda env, p: _grant_card(
        env, p, env.state.rng.choice((99000001, 99000002, 99000003))
        + 10000 * (min(int(p.phase), 6) - 1)),
    "猫爪": lambda env, p: _grant_card(env, p, 8),         # 云剑•猫爪
    "灵猫乱剑": lambda env, p: _grant_card(env, p, 9),     # 灵猫乱剑
    "灵猫踏云": _lingmao_tayun,
}
_ROUND_BY_NAME = {"五行润养": _wuxing_runyang}   # 云雾变幻 = exact free-roll in env.reroll
_BATTLE_BY_NAME = {"战斗历练": _zhandou_lilian}
_BREAK_BY_NAME = {"灵阵精通": _lingzhen_jingtong}

SELECT_FX: dict = {}
ROUND_FX: dict = {}
BATTLE_FX: dict = {}
BREAK_FX: dict = {}


def _bind():
    byname = {v["name"]: i for i, v in FA.all_fates().items()}
    for tbl, by in ((SELECT_FX, _SELECT_BY_NAME), (ROUND_FX, _ROUND_BY_NAME),
                    (BATTLE_FX, _BATTLE_BY_NAME), (BREAK_FX, _BREAK_BY_NAME)):
        tbl.clear()
        for nm, fn in by.items():
            if nm in byname:
                tbl[byname[nm]] = fn


_bind()


if __name__ == "__main__":
    print("SELECT_FX:", list(SELECT_FX), " ROUND_FX:", list(ROUND_FX),
          " BATTLE_FX:", list(BATTLE_FX), " BREAK_FX:", list(BREAK_FX))
