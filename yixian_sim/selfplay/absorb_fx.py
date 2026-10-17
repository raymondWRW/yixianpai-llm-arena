# -*- coding: utf-8 -*-
"""[炼化] ABSORB effects — what a card does when it is 炼化'd (absorbed).

Absorbing normally yields +1 修为 (env._absorb_gain). A number of cards carry a
`[炼化]` clause that fires INSTEAD OF/ON TOP OF that — for 林小月 the cat package is
the whole point of 好奇心, since every cat card is absorb-value:

  小鱼干   33  [炼化]：生命上限+1/2/4，[命元]+2/4/8
  猫薄荷   34  [炼化]：随机升级手牌或卡组中N张L级牌（优先升级名字含“猫”的牌）
  逗猫棒   35  [炼化]：换牌机会+1/2/4

Also implemented (same mechanism, clean prep-phase effects):
  七星灯     4       [命元] becomes 50
  玄冥之水   155     生命上限+3
  锻体丹     2000006 生命上限永久+1/2/4      还魂丹   2000009  [命元]+2/4/8
  洗髓丹     2000012 额外加1/2/4 [修为]      悟道丹   2000015  升级1/2/4张1级牌
  锻体玄丹   2000014 生命上限永久+2/4/8      灵草药浴 10000058 [体魄上限]/[体魄]+N

Per-level numbers are READ FROM THE GAME DATA (combined_cards.json `otherParams`),
never hardcoded, so a card's numbers can't drift from the config. Effects that resolve
inside combat ("下场战斗开始时…", the 灵植 [成长] line) and the roguelike 通宝/体力
economy are deliberately left out — the Oracle fixture can't express them. # STUB
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import cards as C
import merge as M

_CARD_FILE = (_HERE.parent / "vendor" / "yisim-master" / "localization" / "1.5.8" /
              "combined_cards.json")
_params_cache = None


def _card_data() -> dict:
    global _params_cache
    if _params_cache is None:
        try:
            _params_cache = {c["card_id"]: c for c in
                             json.loads(_CARD_FILE.read_text(encoding="utf-8"))}
        except Exception:
            _params_cache = {}
    return _params_cache


def params(cid: int) -> list:
    """This card LEVEL's otherParams (the numbers in its own text)."""
    return list((_card_data().get(int(cid)) or {}).get("otherParams") or [])


def _p(cid: int, i: int, default: int = 0) -> int:
    ps = params(cid)
    return int(ps[i]) if i < len(ps) else default


def _physique(cid: int, default: int = 0) -> int:
    return int((_card_data().get(int(cid)) or {}).get("physique") or default)


# ── the upgrade effect (猫薄荷 / 悟道丹) ──────────────────────────────────────
def _upgrade(env, p, n: int, level: int, prefer: str = "") -> list:
    """Randomly upgrade n cards of `level` held in hand OR fielded on the board
    (卡组), preferring names containing `prefer`. Returns the upgraded names."""
    def eligible(seq):
        return [(i, c) for i, c in enumerate(seq)
                if c and M.card_level(c) == level and M.level_up(c)]
    done = []
    for _ in range(max(0, n)):
        pool = [("hand", i, c) for i, c in eligible(p.hand)] + \
               [("board", i, c) for i, c in eligible(p.board)]
        if not pool:
            break
        favored = [x for x in pool if prefer and prefer in (C.id_to_name(x[2]) or "")]
        pick = env.state.rng.choice(favored or pool)
        where, idx, cid = pick
        up = M.level_up(cid)
        if where == "hand":
            p.hand[idx] = up
        else:
            p.board[idx] = up
        done.append(C.id_to_name(cid))
    return done


# ── handlers: fn(env, p, cid) -> str (cid is the ABSORBED card's level id) ────
def _xiaoyugan(env, p, cid):                        # 小鱼干
    hp, de = _p(cid, 0, 1), _p(cid, 1, 2)
    p.extra_hp += hp
    p.destiny += de
    return f"小鱼干[炼化]: 生命上限+{hp}, 命元+{de} (命 {p.destiny})"


def _maobohe(env, p, cid):                          # 猫薄荷
    n, lv = _p(cid, 0, 1), _p(cid, 1, 1)
    got = _upgrade(env, p, n, lv, prefer="猫")
    return f"猫薄荷[炼化]: 升级{lv}级牌 {', '.join(got) if got else '—'}"


def _doumaobang(env, p, cid):                       # 逗猫棒
    n = _p(cid, 0, 1)
    p.rerolls += n
    return f"逗猫棒[炼化]: 换牌机会+{n}"


def _qixingdeng(env, p, cid):                       # 七星灯
    to = _p(cid, 0, 50)
    p.destiny = to
    return f"七星灯[炼化]: 命元变为{to}"


def _hp_cap(env, p, cid, name):                     # 锻体丹 / 锻体玄丹 / 玄冥之水
    n = _p(cid, 0, 1)
    p.extra_hp += n
    return f"{name}[炼化]: 生命上限+{n}"


def _huanhundan(env, p, cid):                       # 还魂丹
    n = _p(cid, 0, 2)
    p.destiny += n
    return f"还魂丹[炼化]: 命元+{n} (命 {p.destiny})"


def _xisuidan(env, p, cid):                         # 洗髓丹
    n = _p(cid, 0, 1)
    p.cultivation += n
    return f"洗髓丹[炼化]: 额外+{n} 修为 (修为 {p.cultivation})"


def _wudaodan(env, p, cid):                         # 悟道丹
    n = _p(cid, 0, 1)
    got = _upgrade(env, p, n, 1)
    return f"悟道丹[炼化]: 升级 {', '.join(got) if got else '—'}"


def _yaoyu(env, p, cid):                            # 灵草药浴
    n = _physique(cid, 4)
    p.max_tipo += n
    p.tipo = min(p.tipo + n, p.max_tipo)
    return f"灵草药浴[炼化]: 体魄上限+{n}, 体魄+{n} (体魄 {p.tipo}/{p.max_tipo})"


_BY_NAME = {
    "小鱼干": _xiaoyugan,
    "猫薄荷": _maobohe,
    "逗猫棒": _doumaobang,
    "七星灯": _qixingdeng,
    "还魂丹": _huanhundan,
    "洗髓丹": _xisuidan,
    "悟道丹": _wudaodan,
    "灵草药浴": _yaoyu,
    "锻体丹": lambda env, p, cid: _hp_cap(env, p, cid, "锻体丹"),
    "锻体玄丹": lambda env, p, cid: _hp_cap(env, p, cid, "锻体玄丹"),
    "玄冥之水": lambda env, p, cid: _hp_cap(env, p, cid, "玄冥之水"),
}


def effect_for(card_id: int):
    """The [炼化] handler for a card id (any level), or None."""
    nm = (C.id_to_name(int(card_id)) or "").replace("•", "·")
    return _BY_NAME.get(nm)


def fire(env, p, card_id: int):
    """Run the absorbed card's [炼化] effect. Returns a log line or None.
    Call AFTER the card has left the hand so it can't upgrade itself."""
    fx = effect_for(card_id)
    return fx(env, p, int(card_id)) if fx else None


if __name__ == "__main__":
    print("[炼化] cards:", ", ".join(_BY_NAME))
    for cid in (33, 10033, 20033, 34, 10034, 20034, 35, 10035, 20035):
        print(f"  {cid} {C.id_to_name(cid)} params={params(cid)}")
