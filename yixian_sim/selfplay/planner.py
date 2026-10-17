# -*- coding: utf-8 -*-
"""V-guided economy planning — the non-myopic policy (AlphaZero policy-iteration).

The board is still chosen by the placement search (macro-action). What the planner
adds is a NON-MYOPIC economy decision: after the board is set, how to handle the
leftover hand cards — absorb them for cultivation NOW, or HOLD ones that could
merge later. Each choice yields a different resulting state; the value net V scores
each (V predicts final placement), and the planner picks the best.

Actions (all share the same searched board, so only ONE board search per round):
  · absorb_all  — 炼化 every leftover (max cultivation / realm tempo)
  · hold_merge  — hold leftovers that are merge candidates (id already on board, or
                  a duplicate within the hand), absorb the rest
  · hold_all    — absorb nothing (max future flexibility)
Then break through greedily (breaking has no modelled downside).

Exploration: during SELF-PLAY data generation pass explore_eps>0 (ε-greedy) so the
policy tries hold-merge even when the current V — trained on absorb-everything data
— hasn't learned to value it yet. That fresh data is what teaches the NEXT V that
holding pairs pays off. At evaluation time explore_eps=0 (pure argmax = exploit).
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import economy as E
import placement as P
import merge as M
import net as NET


def _merge_candidates(leftover: list, board_ids: list) -> list:
    """Leftover cards worth holding for a future merge: id already on the board
    (draw/hold another → level up) or ≥2 copies within the leftover itself. Only
    cards that CAN level up (some have no upgrade) are worth holding."""
    cnt = Counter(leftover)
    bset = set(board_ids)
    return [c for c in leftover
            if M.can_level(c) and (c in bset or cnt[c] >= 2)]


def _sub(multiset: list, remove: list) -> list:
    """Multiset difference: multiset − remove."""
    cnt = Counter(multiset)
    for c in remove:
        if cnt[c] > 0:
            cnt[c] -= 1
    out = []
    for c, n in cnt.items():
        out += [c] * n
    return out


def _resulting_state(env, p, board, hold: list, absorb: list) -> dict:
    """The post-prep state if we absorb `absorb` and hold `hold` (with greedy
    breakthrough), as encode.py consumes it. Pure — does not mutate p. Carries WHO
    the player is (char/career/天命/体魄) so V evaluates character-specifically."""
    body = 204 in p.talents                            # 李㵘 凡躯: 炼化 → 体魄, not 修为
    cult = p.cultivation + (0 if body else len(absorb) * E.ABSORB_CULT)
    tipo = p.tipo + (min(len(absorb), max(0, p.max_tipo - p.tipo)) if body else 0)
    realm = E.realm_for_cultivation(cult)              # greedy breakthrough
    return {"round": env.state.round, "realm": realm, "cultivation": cult,
            "destiny": p.destiny, "unlocked": E.unlocked_slots(env.state.round),
            "alive": len(env.state.alive_players()), "extra_hp": p.extra_hp,
            "tipo": tipo, "max_tipo": p.max_tipo, "rerolls": p.rerolls,
            "char_id": p.char_id, "career": p.career, "talents": list(p.talents),
            "board": board, "hand_ids": hold}


def make_planning_policy(net, place_net=None, k: int = 5, cap: int = 14,
                         explore_eps: float = 0.0, window: int = 1, margin: float = 0.0):
    """Policy = the (learned or searched) board + a NON-MYOPIC economy decision:
    absorb the leftovers now (修为/tempo) or HOLD merge candidates (stronger board +
    — now that merges grant cult — future 修为 too). V scores each resulting state.

    net: loaded CardValueNet. place_net: a CardPolicyNet → learned placement (fast,
    consistent with the showcase); None → Oracle search. explore_eps>0 → ε-greedy
    (self-play). margin>0: deviate from the absorb_all prior only if an alternative
    beats it by >margin in V (hysteresis against 1-ply greedy amplifying V noise)."""
    import env as EV
    def policy(env, p):
        slots = E.unlocked_slots(env.state.round)
        board_ids = [c for c in p.board if c]
        if place_net is not None:                       # learned placement (fast)
            board, raw_used = EV.learned_board(env, p, place_net, slots)
        else:                                           # Oracle search
            me = p.to_fixture(slots)
            opps = env.field.sample(env.state.round, k, env.state.rng, window=window)
            out = P.best_board(me, board_ids, p.hand, slots, opps,
                               rnd=env.state.round, cap=cap)
            board, raw_used = out["board"], out["raw_used"]
        p.board = board + [0] * (8 - len(board))
        p.cultivation += M.merge_gain(raw_used) * E.MERGE_CULT   # +1 cult per merge
        # consume raw_used from hand (board cards persist; the rest came from hand)
        consumed = list(raw_used)
        for c in board_ids:
            if c in consumed:
                consumed.remove(c)
        for cid in consumed:
            if cid in p.hand:
                p.hand.remove(cid)

        # rounds 1-2 are build rounds (no 炼化, matches env.absorb_leftovers); the
        # absorb-vs-hold economy decision only exists once absorb kicks in (round 3+).
        leftover = list(p.hand)
        if env.state.round <= 2 or not leftover:
            if env.state.round <= 2:
                p.hand.clear()
            env.try_breakthrough(p)
            return
        board = [c for c in p.board if c]
        merge_hold = _merge_candidates(leftover, board)
        options = {
            "absorb_all": [],
            "hold_merge": merge_hold,
            "hold_all": list(leftover),
        }
        # score each option by V of its resulting state
        names = list(options)
        states = [_resulting_state(env, p, board, hold, _sub(leftover, hold))
                  for hold in (options[n] for n in names)]
        vals = NET.predict_values(net, states)
        # choose: ε-greedy explore vs (margin-gated) argmax exploit. names[0] =
        # absorb_all is the default prior; alternatives must beat it by `margin`.
        if explore_eps > 0 and env.state.rng.random() < explore_eps:
            ci = env.state.rng.randrange(len(names))
        else:
            ci = 0
            best = vals[0] + margin
            for i in range(1, len(names)):
                if vals[i] > best:
                    ci, best = i, vals[i]
        hold = options[names[ci]]
        absorb = _sub(leftover, hold)
        for cid in absorb:
            env.absorb(p, cid)                          # p.hand becomes `hold`
        env.try_breakthrough(p)
    return policy


def load_policy(path: str, **kw):
    """Convenience: load a value-net checkpoint and wrap it as a planning policy."""
    return make_planning_policy(NET.load(path), **kw)
