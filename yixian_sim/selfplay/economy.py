# -*- coding: utf-8 -*-
"""Confirmed prep-economy transition rules for the offline YiXianPai model.

These are the pieces we have established exactly (from the game's own config
tables + recorded-game mining, cross-checked against the live counter). The
stochastic deal/reroll sampler lives in draws.py; the full step() loop in env.py.
See GAME_MODEL.md for provenance and open items.
"""
from __future__ import annotations

import struct
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
_CONFIGS = _REPO / "oracle" / "data" / "extracted" / "configs"


# ── Realm / breakthrough — EXACT (configs/LevelConfig.dat) ────────────────────
# realm -> (cultivation required to be AT this realm, base HP). Loaded from the
# config at import so it can never drift from the game; the literal below is the
# validated fallback (matches proxy_view._REALM_BASE_HP and live HP 17/18 rounds).
_REALM_FALLBACK = {
    1: (0, 40), 2: (9, 45), 3: (21, 52), 4: (36, 62), 5: (55, 75), 6: (75, 100),
}


def _load_realm_table() -> dict:
    """Parse LevelConfig.dat (protobuf) → {realm: (cult_req, base_hp)}.
    Falls back to the validated literal if the config isn't present/parseable."""
    try:
        import blackboxprotobuf
        msg, _ = blackboxprotobuf.decode_message((_CONFIGS / "LevelConfig.dat").read_bytes())
        rows = None
        for v in msg.values():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "1" in v[0]:
                rows = v
                break
            if isinstance(v, dict):
                for v2 in v.values():
                    if isinstance(v2, list) and v2 and isinstance(v2[0], dict) and "1" in v2[0]:
                        rows = v2
                        break
        out = {}
        for r in rows or []:
            realm = int(r.get("1"))
            out[realm] = (int(r.get("2", 0) or 0), int(r.get("3", 0) or 0))
        # sanity: must contain realms 1..5 with the known base HPs
        if all(k in out for k in (1, 2, 3, 4, 5)) and out[1][1] == 40:
            return out
    except Exception:
        pass
    return dict(_REALM_FALLBACK)


REALM_TABLE = _load_realm_table()
CULT_REQ = {r: c for r, (c, _hp) in REALM_TABLE.items()}      # realm -> cultivation needed
BASE_HP = {r: hp for r, (_c, hp) in REALM_TABLE.items()}      # realm -> base max HP
MAX_REALM = 5                                                 # game caps play at 境5


def realm_for_cultivation(cult: int) -> int:
    """Highest realm a given cultivation *qualifies* for (the player may choose to
    break up to this). Capped at MAX_REALM."""
    realm = 1
    for r in sorted(CULT_REQ):
        if cult >= CULT_REQ[r]:
            realm = r
    return min(realm, MAX_REALM)


def can_break_through(cult: int, current_realm: int) -> bool:
    """True if cultivation is enough to advance past the current realm."""
    nxt = current_realm + 1
    return nxt <= MAX_REALM and cult >= CULT_REQ.get(nxt, 1 << 30)


def max_hp(realm: int, extra_max_hp: int = 0) -> int:
    """Battle max HP = realm base + extra (HP fates add extra at battle time)."""
    return BASE_HP.get(realm, 40) + max(0, int(extra_max_hp))


# ── Board slots — mined (n=103 games), clean rule ────────────────────────────
def unlocked_slots(round_num: int) -> int:
    """Usable board slots this round: 3 at R1 rising to the 8-slot cap by R6."""
    return min(8, max(3, int(round_num) + 2))


# ── Sidejob (副职) ────────────────────────────────────────────────────────────
SIDEJOB_ROUND = 2        # the player picks one of the 7 sidejobs at round 2


# ── 换牌 rerolls — authoritative schedule (user-confirmed) ────────────────────
# Exchange chances granted at each round start: +3 for rounds 1-9, +4 for rounds
# 10-12, +6 from round 13 on. Banking caps at 25 (user rule 2026-09-17): the
# round grant tops up to 25 at most, and a player sitting at/above 25 (pushed
# past by [置换]/天命 gains, which are NOT capped) gets no grant until they
# spend back below the cap. (Mined: real players bank to ~17 by R10 and dump
# the bank R10-14 fishing newly-unlocked phase-3/4 key cards.)
REROLL_START = 0         # seeded at reset; the R1 grant (+3) brings it to 3
REROLL_CAP = 25          # max banked 换牌 the round grant will fill up to


def reroll_grant(round_num: int) -> int:
    r = int(round_num)
    return 3 if r <= 9 else (4 if r <= 12 else 6)


# ── Cultivation ──────────────────────────────────────────────────────────────
# Sources: a flat +2 PASSIVE every round from round 2, +1 per card 炼化'd (absorb),
# and +1 per MERGE. Calibrated to the real per-round median (128 games): R1=0, R2=2,
# R3=6, R4=10, R5=15, R6=22. Round 1 grants nothing (build round) and rounds 1-2 do
# no 炼化 (real R2 median is exactly the +2 passive) — absorb kicks in from round 3,
# so the FLOOR is +2/round: min cult is 2 at R2, 4 at R3, 6 at R4 (a player can only
# ever be at-or-above passive×(round-1)).
ABSORB_CULT = 1          # +1 cultivation per card absorbed (炼化) — confirmed
MERGE_CULT = 1           # +1 cultivation per merge (two copies → next level)
PASSIVE_CULT = 2         # +2 cultivation every player gets each round (from round 2)


def passive_cult(round_num: int) -> int:
    """Flat +2 every round from round 2 (0 in round 1, the build round). This is the
    cultivation FLOOR — a player with no 炼化/merge is at 2·(round−1)."""
    return PASSIVE_CULT if int(round_num) >= 2 else 0


PASSIVE_HP = 2           # +2 max HP for EVERY player at each round start from round 2
                         # (user-confirmed): R1 = realm base 40, R2 = 42, R3 = 44, …


def passive_hp(round_num: int) -> int:
    """Flat +2 max HP every round from round 2 (round 1 is the realm base alone).
    Cumulative and realm-independent — it rides `extra_hp` so a breakthrough's base-HP
    jump keeps the accrued bonus."""
    return PASSIVE_HP if int(round_num) >= 2 else 0


# ── 命元伤害 destiny damage — OFFICIAL FAQ formula (user-supplied) ────────────
# diff = final HP difference (in a kill that IS the winner's remaining HP):
#   diff ≤ 20:  dmg = round + 1 + ceil(diff / 5)
#   diff > 20:  dmg = round + 5 + min(ceil((diff − 20) / 10), 2 + round/2)
# Immortal Relic season (active): rounds 1-9 take 1 LESS.
# The Oracle engine already computes this for DECIDED battles (its lifeDamage
# matches, e.g. R19 hpΔ 107 → 19+5+ceil(87/10) = 33 = engine output); this
# function exists for the TURN-CAP case, where the engine reports lifeDamage 0
# but the lower-HP side still loses and pays (user ruling).
def destiny_damage(round_num: int, hp_diff: float) -> int:
    import math
    r = int(round_num)
    d = max(0.0, float(hp_diff))
    if d <= 20:
        dmg = r + 1 + math.ceil(d / 5)
    else:
        extra = min(math.ceil((d - 20) / 10), 2 + r / 2)
        dmg = r + 5 + extra
    if r <= 9:
        dmg -= 1                     # Immortal Relic season adjustment
    return max(0, int(dmg))


# ── Deal count per round — mined (n=105 games, non-capture-miss observations) ─
# Cards freely dealt at the start of each prep round: 5 opening, 3 early, 4 late.
# ~20% of rounds show +1 (likely a breakthrough/grant round extra draw) — to be
# pinned during fidelity validation; the base rule below fits ~75-90% cleanly.
def deal_count(round_num: int) -> int:
    r = int(round_num)
    if r <= 1:
        return 5
    return 3 if r <= 11 else 4


# ── Deck pool composition ────────────────────────────────────────────────────
# The authoritative copy-count model already lives in proxy_view.Counter
# (DEFAULT_COPIES=8, PHASE5_COPIES=6, SPECIAL_COPIES, sidejob/derivation pools,
# reroll burn = 3). draws.py builds its sampler prior from that, rather than
# duplicating the tables here.
REROLL_BURN = 3          # copies of a rerolled-away card removed from the pool


# ── Merge map — configs/CardCombineConfig.dat ────────────────────────────────
def load_merge_map() -> dict:
    """base card id -> upgraded (next-level) card id. 3 copies at level L merge
    into 1 at level L+1 (one level per round). Empty dict if unparseable."""
    out = {}
    try:
        import blackboxprotobuf
        msg, _ = blackboxprotobuf.decode_message((_CONFIGS / "CardCombineConfig.dat").read_bytes())
        rows = None
        for v in msg.values():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                rows = v
                break
            if isinstance(v, dict):
                for v2 in v.values():
                    if isinstance(v2, list) and v2 and isinstance(v2[0], dict):
                        rows = v2
                        break
        for r in rows or []:
            src = r.get("101")
            res = r.get("2")
            if isinstance(src, int) and isinstance(res, int):
                out[src] = res
    except Exception:
        pass
    return out


if __name__ == "__main__":
    print("REALM_TABLE (realm: cult_req, base_hp):")
    for r in sorted(REALM_TABLE):
        print(f"  {r}: cult>={REALM_TABLE[r][0]:>3}  hp={REALM_TABLE[r][1]}")
    print("slots by round 1..8:", [unlocked_slots(r) for r in range(1, 9)])
    print("realm_for_cultivation @ 0/9/21/36/55/80:",
          [realm_for_cultivation(c) for c in (0, 9, 21, 36, 55, 80)])
    mm = load_merge_map()
    print(f"merge map entries: {len(mm)}  sample: {list(mm.items())[:3]}")
