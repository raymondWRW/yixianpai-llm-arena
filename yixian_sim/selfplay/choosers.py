# -*- coding: utf-8 -*-
"""Learned fate / sidejob decisions — V-lookahead choosers.

The fate pick (1-of-4 at a breakthrough) and the sidejob pick (1-of-7 at round 2)
become real decisions: for each option we build the resulting player STATE and
score it with the value net V (predicts final placement), then take the argmax.
During self-play data generation pass explore_eps>0 (ε-greedy) so the picks vary
and the NEXT V learns which fates/careers actually pay off — the same policy-
iteration loop as the placement/economy planner, now over the meta-choices.

Fate options move stats V can already see (HP/体魄/修为/命元) AND the talent id is
embedded, so V can value combat fates too. Career is embedded, so V(state, career=X)
reflects how good career X has been for this kind of player in past self-play.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import economy as E
import fates as FA
import net as NET


def _base_state(env, p) -> dict:
    slots = E.unlocked_slots(env.state.round)
    return {"round": env.state.round, "realm": p.realm, "cultivation": p.cultivation,
            "destiny": p.destiny, "unlocked": slots,
            "alive": len(env.state.alive_players()), "extra_hp": p.extra_hp,
            "tipo": p.tipo, "max_tipo": p.max_tipo, "rerolls": p.rerolls,
            "char_id": p.char_id, "career": p.career, "talents": list(p.talents),
            "board": [c for c in p.board if c], "hand_ids": list(p.hand)}


def _after_fate(env, p, fid) -> dict:
    """State if fate `fid` were taken (stat deltas + talent added) — no mutation."""
    st = _base_state(env, p)
    e = FA.all_fates().get(int(fid), {}).get("effects", {})
    st["extra_hp"] = max(0, st["extra_hp"] + e.get("hp", 0))
    st["cultivation"] = max(0, st["cultivation"] + e.get("cult", 0))
    st["tipo"] = max(0, st["tipo"] + e.get("tipo", 0))
    st["max_tipo"] = max(st["max_tipo"] + e.get("tipo_cap", 0),
                         st["tipo"] + 5 if st["tipo"] else st["max_tipo"])
    st["destiny"] = st["destiny"] + e.get("destiny", 0)
    st["rerolls"] = max(0, st["rerolls"] + e.get("rerolls", 0))
    st["talents"] = st["talents"] + [int(fid)]
    return st


def _argmax_or_explore(vals, options, rng, eps):
    if eps > 0 and rng.random() < eps:
        return options[rng.randrange(len(options))]
    return options[int(max(range(len(options)), key=lambda i: vals[i]))]


def make_fate_chooser(net, explore_eps: float = 0.0):
    """chooser(env, p, offered) → fate id maximising V(resulting state)."""
    def chooser(env, p, offered):
        if not offered:
            return 0
        states = [_after_fate(env, p, f) for f in offered]
        vals = NET.predict_values(net, states)
        return _argmax_or_explore(vals, offered, env.state.rng, explore_eps)
    return chooser


def make_sidejob_chooser(net, explore_eps: float = 0.0, careers=range(1, 8)):
    """chooser(env, p) → career maximising V(state with career=X). The career
    embedding lets V reflect how each career has performed in past self-play."""
    careers = list(careers)

    def chooser(env, p):
        states = []
        for c in careers:
            st = _base_state(env, p)
            st["career"] = c
            states.append(st)
        vals = NET.predict_values(net, states)
        return _argmax_or_explore(vals, careers, env.state.rng, explore_eps)
    return chooser
