# -*- coding: utf-8 -*-
"""天命 / 仙命 (Immortal Fates) — selection + effects.

Fates are picked at game start (a mandatory first fate) and at each breakthrough
(pick-1-of-N offer), per the design docs. Each fate (vendor yisim immortal_fates.json,
306 of them) modifies player state and/or combat:

  · STATE effects — 生命上限(max HP) / 修为(cultivation) / 体魄(physique) + 体魄上限(cap)
    / 命元(destiny) / 换牌(rerolls) — parsed here and applied to the PlayerState, so
    the Oracle fixture (extraMaxHp/exp/tipo/…) reflects them.
  · COMBAT effects — the fate id is passed to the Oracle fixture's `talents`; the
    engine applies the in-battle effect (verified: 炽火炎刃 shifts the outcome, while
    a pure +HP fate does not — confirming stat boosts must be applied to state).

We use each fate's base (version-0) params. Which fate is OFFERED and which VERSION
is a game rule not in our data yet — offers are a random sample (bootstrap; the
pick is a strategic/learnable choice). # STUB (offer/version rules)
"""
from __future__ import annotations

import json
import re
from pathlib import Path

_FILE = (Path(__file__).resolve().parent.parent / "vendor" / "yisim-master" /
         "localization" / "1.5.8" / "immortal_fates.json")

# (regex for the stat token, PlayerState delta key). The sign (+/加/减) and number
# are captured after the token, so 体魄上限 (its sign follows 上限) never matches the
# bare 体魄 pattern, and 体魄/[体魄] with brackets both parse.
# tokens are bracket-tolerant (\[?...\]?) — descs write [命元]+14, [体魄]+5, etc.
_STAT_PATTERNS = [
    (r"生命上限", "hp"),
    (r"体魄上限", "tipo_cap"),
    (r"修为", "cult"),
    (r"\[?命元\]?", "destiny"),
    (r"换牌机会", "rerolls"),
    (r"\[?体魄\]?", "tipo"),
]

_fates_cache = None


def _parse_effects(desc: str) -> dict:
    """Parse the one-time UNCONDITIONAL stat deltas from a fate desc:
    '生命上限+5；修为减1；[命元]+14；[体魄]+5' → {'hp':5,'cult':-1,'destiny':14,'tipo':5}.
    Only the head before the first conditional/trigger keyword (每/若/当/战斗/累积/…)
    is scanned — ongoing/conditional clauses are the effect engine's job (fate_fx.py)."""
    eff: dict = {}
    cut = re.search(r"每|若|当|战斗|每轮|累积|下次|回合|突破|胜利|战败", desc or "")
    head = desc[:cut.start()] if cut else (desc or "")
    for token, key in _STAT_PATTERNS:
        m = re.search(token + r"([\+加减])\s*(\d+)", head)
        if m:
            eff[key] = int(m.group(2)) * (-1 if m.group(1) == "减" else 1)
    return eff


def all_fates() -> dict:
    """{id: {'name','desc','effects','combat'(bool)}} from version-0 of each fate."""
    global _fates_cache
    if _fates_cache is not None:
        return _fates_cache
    out = {}
    for f in json.loads(_FILE.read_text(encoding="utf-8")):
        vers = f.get("versions") or [{}]
        desc = vers[0].get("desc_cn", "") or ""
        # Fates come in 4 id tiers (id, 10000+id, 20000+id, 30000+id = versions 0-3).
        # Only the BASE entry has RESOLVED params; the tier variants are unresolved
        # "{otherParams}" templates — skip them (we use the base fate at tier 0).
        if not desc or "{" in desc:
            continue
        eff = _parse_effects(desc)
        out[int(f["id"])] = {
            "name": f.get("name_cn", ""), "desc": desc, "effects": eff,
            "combat": not eff,          # no parsed stat delta ⇒ treat as combat-only
        }
    _fates_cache = out
    return out


_POOLS_FILE = Path(__file__).resolve().parent / "fate_pools.json"
_pools_cache = None


def _pools() -> dict:
    """{'general':[ids], 'sect':{s:[ids]}, 'character':{charId:[ids]}} — fates split
    into general / sect-specific / character-specific (build_fate_pools.py)."""
    global _pools_cache
    if _pools_cache is None:
        _pools_cache = json.loads(_POOLS_FILE.read_text(encoding="utf-8"))
    return _pools_cache


def offer(char_id: int, sect: int, rng, exclude=(), phase: int = 0) -> list:
    """The 4 fates offered at a breakthrough (realm 2-5): slot 0 is the character
    fate FOR THIS PHASE — char fates are one-per-phase (talent_params field_6:
    牧逸风's 剑不出鞘 only in the realm-2 offer, 云海连绵 at realm-3, …) — and the
    other 3 draw from this sect's + the general pool. Excludes already-taken.
    phase=0 (unknown) falls back to a random unowned character fate."""
    P = _pools()
    ex = set(exclude)
    offered = []
    slot = P.get("char_phase", {}).get(str(int(char_id)), {}).get(str(int(phase)))
    if slot is not None:
        if slot not in ex:
            offered.append(slot)                     # the phase's char fate
    else:
        char_pool = [i for i in P["character"].get(str(int(char_id)), []) if i not in ex]
        if char_pool:
            offered.append(rng.choice(char_pool))    # unknown phase: legacy sample
    sg_pool = [i for i in P["sect"].get(str(int(sect)), []) + P["general"] if i not in ex]
    rest = [i for i in sg_pool if i not in offered]
    rng.shuffle(rest)
    offered += rest[:4 - len(offered)]
    return offered


def choose(offered: list, rng) -> int:
    """Bootstrap pick: greedily prefer the fate with the best net beneficial stats
    (+HP/+体魄/+修为/+命元/+换牌), with combat-only fates given a moderate baseline and
    a little noise for variety. A learned policy (value by board archetype) replaces
    this. # STUB (fate policy)"""
    if not offered:
        return 0
    F = all_fates()

    def score(fid):
        e = F[fid]["effects"]
        if not e:
            return 1.5 + rng.random()          # combat-only fate: modest baseline
        s = (e.get("hp", 0) * 1.0 + e.get("tipo", 0) * 1.6 + e.get("tipo_cap", 0) * 0.8
             + e.get("cult", 0) * 2.0 + e.get("destiny", 0) * 1.0 + e.get("rerolls", 0) * 0.5)
        return s + rng.random() * 0.6
    return max(offered, key=score)


_innates_cache = None


def char_innate(char_id: int) -> int:
    """The character's INNATE fate id (auto-granted at game start), or 0."""
    global _innates_cache
    if _innates_cache is None:
        f = Path(__file__).resolve().parent / "char_innates.json"
        _innates_cache = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    return int(_innates_cache.get(str(int(char_id)), 0) or 0)


_version_descs = None       # base_id -> [resolved desc_cn for versions 0..3]


def version_desc(fate_id: int, phase: int) -> str:
    """The RESOLVED desc of the fate's per-phase VERSION (v0=phase2 … v3=phase5).
    Fates scale with the breakthrough phase they're offered at — 稳固根基 is
    修为−1 at phase 2 but 修为−2 at phase 4; 云剑传承 grants 1 card at phase 2
    and 3 at phase 5 (user-audited). Falls back to the base desc."""
    global _version_descs
    if _version_descs is None:
        _version_descs = {}
        try:
            raw = json.loads(_FILE.read_text(encoding="utf-8"))
            for v in raw:
                fid = v.get("id")
                vers = v.get("versions") or []
                if fid is not None and vers:
                    _version_descs[int(fid)] = [
                        (x.get("desc_cn") or "") for x in
                        sorted(vers, key=lambda x: x.get("version", 0))]
        except Exception:
            _version_descs = {}
    descs = _version_descs.get(int(fate_id))
    base = all_fates().get(int(fate_id), {}).get("desc", "")
    if not descs or phase < 2:
        return base
    return descs[min(len(descs) - 1, max(0, int(phase) - 2))] or base


def apply(env, player, fate_id: int, phase: int = 0) -> dict:
    """Apply a fate to a PlayerState: one-time STAT deltas + record the id in
    player.talents (Oracle combat) + dispatch non-stat one-offs (card draws, innate
    effects) via the effect engine. `phase` = the breakthrough realm the fate was
    picked at — its VERSION's magnitudes apply (v0=phase2 … v3=phase5). Returns
    the parsed stat effects for logging."""
    info = all_fates().get(int(fate_id))
    if not info:
        return {}
    desc = version_desc(fate_id, phase) if phase >= 2 else info["desc"]
    e = _parse_effects(desc) if phase >= 2 else info["effects"]
    player.extra_hp = max(0, player.extra_hp + e.get("hp", 0))
    player.cultivation = max(0, player.cultivation + e.get("cult", 0))
    player.tipo = max(0, player.tipo + e.get("tipo", 0))
    player.max_tipo = max(0, player.max_tipo + e.get("tipo_cap", 0))
    if player.tipo:                               # cap floats just above physique
        player.max_tipo = max(player.max_tipo, player.tipo + 5)
    player.destiny = player.destiny + e.get("destiny", 0)
    player.rerolls = max(0, player.rerolls + e.get("rerolls", 0))
    if int(fate_id) not in player.talents:
        player.talents.append(int(fate_id))
    if hasattr(player, "talent_phases"):
        player.talent_phases[int(fate_id)] = int(phase)
    try:                                            # non-stat one-offs (draws, innate)
        import fate_fx
        fate_fx.on_select(env, player, int(fate_id), desc=desc)
    except Exception:
        pass
    return e


def name(fate_id: int) -> str:
    return all_fates().get(int(fate_id), {}).get("name", str(fate_id))


if __name__ == "__main__":
    F = all_fates()
    print(f"{len(F)} fates loaded")
    with_stat = [i for i, v in F.items() if v["effects"]]
    print(f"  with parsed stat effects: {len(with_stat)}  combat-only: {len(F)-len(with_stat)}")
    for i in (1, 118, 146, 12, 59, 6):
        print(f"  {i} {F[i]['name']}: {F[i]['desc']}  -> {F[i]['effects']}")
