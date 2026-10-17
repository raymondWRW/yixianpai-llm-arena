# -*- coding: utf-8 -*-
"""The stochastic deal / reroll sampler for the offline model.

Two concerns, deliberately separated:

  1. SAMPLING MECHANICS (fully specified by the official FAQ + mining) — the
     `DrawBag` below: uniform weighted-bag draw over remaining copies, with the
     first-exchange current-phase 2x boost, phase-≤-current gating, reroll burn
     (sect 3 / sidejob 2 this season), and the "Deviation Syndrome" empty-pool
     fallback. This part is exact and unit-testable.

  2. POOL MEMBERSHIP (fidelity-critical, refined against replays) — `build_pool`
     constructs the drawable deck for a character. Best-effort from
     card_phases.json; the exact sect mapping + generic/derivation exclusions are
     flagged and validated in fidelity.py, NOT trusted blindly.

Determinism: every stochastic call takes an explicit `rng` (random.Random) so
MCTS chance nodes and self-play are reproducible.
"""
from __future__ import annotations

import json
from pathlib import Path

from economy import ABSORB_CULT  # noqa: F401 (re-export convenience)

_REPO = Path(__file__).resolve().parent.parent
_PHASES_FILE = _REPO / "tools" / "card_phases.json"

DEVIATION_SYNDROME = "走火入魔"      # dealt when no eligible pool card remains
DEFAULT_COPIES = 8
INCARNATION_COPIES = 6               # phase-5 (Incarnation) cards
ELIXIR_SPECIAL_COPIES = 3           # 炼丹师 Talent/Body/Enlightenment elixirs
# character id prefix (char_id // 1_000_000) -> card_phases.json "sect" field.
# IDENTITY — validated by fidelity.py: characters with prefix 1/2/3/4 draw from
# card-sects 1/2/3/4 respectively (the card-id prefixes 1M/4M/7M/10M are a
# separate scheme and do NOT enter here). Extend if more sects appear.
SECT_PREFIX_TO_FIELD = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
_ELIXIR_SPECIALS = {"天赋丹", "大炼体丹", "顿悟丹"}


def _norm(s: str) -> str:
    return (s or "").replace("•", "·")   # • → · (match runtime names)


_phase_sect_cache = None


def _phase_sect_map():
    """{name: (phase, sect)} from card_phases.json (name-keyed; highest phase
    kept, matching proxy_view._name_to_phase)."""
    global _phase_sect_cache
    if _phase_sect_cache is not None:
        return _phase_sect_cache
    out = {}
    try:
        data = json.loads(_PHASES_FILE.read_text(encoding="utf-8"))
        for info in data.values():
            nm = _norm(info.get("name", ""))
            if not nm:
                continue
            ph = int(info.get("phase", 0) or 0)
            sect = int(info.get("sect", 0) or 0)
            prev = out.get(nm)
            if prev is None or ph > prev[0]:
                out[nm] = (ph, sect)
    except Exception:
        out = {}
    _phase_sect_cache = out
    return out


def default_copies(name: str, phase: int) -> int:
    if name in _ELIXIR_SPECIALS:
        return ELIXIR_SPECIAL_COPIES
    return INCARNATION_COPIES if phase == 5 else DEFAULT_COPIES


# Derivation / event card families (云剑•X 幻•X 狂剑• …) enter the deck ONLY via
# a 天衍 pick — never the normal draw (user-confirmed: e.g. 云剑•晚霞). They share
# the sect id-range so id math won't catch them; exclude by the "•/·" derivation
# prefix. FIDELITY: refine this set against recorded games in fidelity.py.
# Validated against recorded games (fidelity.py): 78 names across these three
# families, all correctly not-drawn (they enter via 天衍). No real sect card
# starts with these, so no over-exclusion.
_DERIVATION_PREFIXES = ("云剑·", "幻·", "狂剑·")


def _is_drawable_name(nm: str, is_base) -> bool:
    if any(nm.startswith(p) for p in _DERIVATION_PREFIXES):
        return False                              # derivation/event-only
    return bool(is_base(nm))                       # excludes 梦· dream + personal-fate


# ── authoritative draw pool (selfplay/card_pool.json, from build_card_pool.py) ──
# Cards are classified per vendor yisim's classify_cards.py (the yxp_wiki source):
# sect decks by base-id range (1M/4M/7M/10M → sects 1/2/3/4) and the 7 sidejobs
# (2M/3M/5M/6M/8M/9M/11M), EXCLUDING field_104 specials (气势不绝 = sect_secret_
# enchantment), character-specific fate cards (id 1..999), vouchers/talismans.
_POOL_FILE = Path(__file__).resolve().parent / "card_pool.json"
_card_pool_cache = None


def _card_pool() -> dict:
    global _card_pool_cache
    if _card_pool_cache is None:
        _card_pool_cache = json.loads(_POOL_FILE.read_text(encoding="utf-8"))
    return _card_pool_cache


def _pool_from(cards: dict, max_phase: int) -> dict:
    out = {}
    for nm, ph in cards.items():
        ph = int(ph)
        if 1 <= ph <= max_phase:
            out[nm] = {"copies": default_copies(nm, ph), "phase": ph}
    return out


def build_pool(char_sect_prefix: int, career: int = 0, max_phase: int = 5) -> dict:
    """Drawable deck {name: {'copies','phase'}} for a character's SECT (1-4),
    plus the ONE selected sidejob CAREER (1-7) if given. The sidejob is picked at
    round 2 — until then career=0 (sect cards only). Authoritative membership from
    card_pool.json; other sects, the other 6 sidejobs, sect-secret enchantments and
    fate/character cards are NOT in the pool."""
    cp = _card_pool()
    pool = _pool_from(cp["sects"].get(str(int(char_sect_prefix)), {}), max_phase)
    if career:
        pool.update(sidejob_pool(int(career), max_phase))
    return pool


def sidejob_pool(career: int, max_phase: int = 5) -> dict:
    """The drawable cards {name: {'copies','phase'}} for one sidejob career (1-7)."""
    return _pool_from(_card_pool()["sidejobs"].get(str(int(career)), {}), max_phase)


def sidejob_card_names(career: int) -> set:
    return set(_card_pool()["sidejobs"].get(str(int(career)), {}))


class DrawBag:
    """Remaining drawable deck for one player. Weighted-bag sampling per the FAQ.

    `pool`: {name: {'copies': int, 'phase': int}}. Copies decrement as cards are
    drawn; reroll burns extra copies. `sidejob_names` marks which names are
    sub-profession cards (reroll burn 2 vs sect 3)."""

    def __init__(self, pool: dict, sidejob_names=None):
        self.copies = {n: int(d["copies"]) for n, d in pool.items()}
        self.phase = {n: int(d["phase"]) for n, d in pool.items()}
        self.sidejob = set(sidejob_names or ())

    def add_cards(self, pool: dict, as_sidejob: bool = True):
        """Add a pool of cards (e.g. the picked sidejob at round 2) to the bag.
        New names get their copy count + phase; sidejob names are tracked for the
        reduced reroll burn (2 vs 3)."""
        for n, d in pool.items():
            if n not in self.copies:
                self.copies[n] = int(d["copies"])
                self.phase[n] = int(d["phase"])
            if as_sidejob:
                self.sidejob.add(n)

    # ── availability + weighting ─────────────────────────────────────────────
    def _weights(self, current_phase: int, boost: bool):
        """(names, weights): each remaining copy = weight 1, ×2 for current-phase
        cards when `boost` (the first exchange of Foundation/Virtuoso/Immortality
        rounds). Only cards of phase ≤ current_phase are eligible."""
        names, weights = [], []
        for n, c in self.copies.items():
            if c <= 0:
                continue
            ph = self.phase.get(n, 1)
            if ph > current_phase:
                continue
            w = c * (2 if (boost and ph == current_phase) else 1)
            names.append(n)
            weights.append(w)
        return names, weights

    def draw_one(self, current_phase: int, rng, boost: bool = False) -> str:
        names, weights = self._weights(current_phase, boost)
        if not names:
            return DEVIATION_SYNDROME              # empty eligible pool → 走火入魔
        pick = rng.choices(names, weights=weights, k=1)[0]
        self.copies[pick] -= 1
        return pick

    def deal(self, n: int, current_phase: int, rng, first_exchange: bool = False) -> list:
        """Deal n cards. The first-exchange 2x current-phase boost applies to the
        FIRST draw only (per the exact rule); the rest are unboosted."""
        out = []
        for i in range(n):
            out.append(self.draw_one(current_phase, rng, boost=(first_exchange and i == 0)))
        return out

    def deal_subset(self, n: int, current_phase: int, rng, allow,
                    boost_first: bool = False) -> list:
        """Draw n cards restricted to names where allow(name) is True (weighted by
        remaining copies, phase-gated) — for fate draws of a specific card TYPE
        (门派/副职/筑基期/五行/体魄…) and for the sect/sidejob split of the round deal.
        boost_first applies the first-exchange 2x current-phase weighting to the FIRST
        card only. Falls back to 走火入魔 when nothing matches."""
        out = []
        for i in range(n):
            boost = boost_first and i == 0
            names, weights = [], []
            for nm, c in self.copies.items():
                if c <= 0 or self.phase.get(nm, 1) > current_phase:
                    continue
                if not allow(nm):
                    continue
                ph = self.phase.get(nm, 1)
                names.append(nm)
                weights.append(c * (2 if (boost and ph == current_phase) else 1))
            if not names:
                out.append(DEVIATION_SYNDROME)
                continue
            pick = rng.choices(names, weights=weights, k=1)[0]
            self.copies[pick] -= 1
            out.append(pick)
        return out

    def reroll(self, discard_name: str, current_phase: int, rng,
               no_penalty: bool = False) -> str:
        """Exchange a card away and draw a replacement. Burn (beyond the already-
        drawn copy): sect 3 / sidejob 2 this season; 0 for Exchange-effect cards
        (`no_penalty`). Returns the replacement card name."""
        if not no_penalty and discard_name in self.copies:
            burn = 2 if discard_name in self.sidejob else 3
            self.copies[discard_name] = max(0, self.copies[discard_name] - burn)
        return self.draw_one(current_phase, rng)

    def total_remaining(self, current_phase: int = 5) -> int:
        return sum(c for n, c in self.copies.items()
                   if c > 0 and self.phase.get(n, 1) <= current_phase)


if __name__ == "__main__":
    import random
    pool = build_pool(char_sect_prefix=1, max_phase=5)
    print(f"pool(sect-prefix 1): {len(pool)} card names, "
          f"{sum(d['copies'] for d in pool.values())} total copies")
    bag = DrawBag(pool)
    rng = random.Random(42)
    # a realm-2 (phase-2) player's round: deal 3, first-exchange boost on
    hand = bag.deal(3, current_phase=2, rng=rng, first_exchange=True)
    print("dealt (phase≤2):", hand)
    print("all drawn phases ≤ 2:", all(bag.phase.get(h, 1) <= 2
                                        for h in hand if h != DEVIATION_SYNDROME))
    # exhaust a phase-1 pool to see Deviation Syndrome
    small = DrawBag({"A": {"copies": 1, "phase": 1}})
    print("draw1:", small.draw_one(1, rng), "draw2 (empty):", small.draw_one(1, rng))
