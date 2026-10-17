# -*- coding: utf-8 -*-
"""search.py — mini-batch hill-climb over board composition, ORDER and levels.

The bot steers (target, pools, start board, locks, objective); this grinds.
One "evaluation" = one candidate board scored over both seats × `repeats`
battles, all sims routed through yisim's warm batch runner.

Locks:
  lock_slots {idx: name} — that card fixed at that position.
  lock_cards [names]     — card must be somewhere on the board, position free.
Moves: reorder (move a card to another slot), swap-in from pool, level ±1.
Legality: every candidate obeys combat_ok + the ≤2 [消耗]/[持续] rule.
"""
from __future__ import annotations

import random

import yisim_bridge as YB


def _level_variant(cid: int, delta: int):
    v = int(cid) + 10000 * delta
    return v if v in YB._names() and YB.combat_ok(v) else None


def _legal(ids) -> bool:
    if any(not YB.combat_ok(c) for c in ids):
        return False
    return sum(1 for c in ids if YB.limited_kw(c)) <= 2


def _satisfies_locks(ids, lock_slots, lock_card_ids, nm):
    for idx, name in lock_slots.items():
        if idx >= len(ids) or nm(ids[idx]) != name:
            return False
    names = [nm(c) for c in ids]
    for name in lock_card_ids:
        if name not in names:
            return False
    return True


def _score(results, objective):
    """results: list of (seat, win_bool, turns). Higher tuple = better."""
    firsts = [r for r in results if r[0] == "first"]
    seconds = [r for r in results if r[0] == "second"]
    wf = sum(r[1] for r in firsts) / max(1, len(firsts))
    ws = sum(r[1] for r in seconds) / max(1, len(seconds))
    wturns = [r[2] for r in results if r[1] and r[2]]
    avg_t = sum(wturns) / len(wturns) if wturns else 64
    if objective == "first":
        return (wf, ws, -avg_t)
    if objective == "second":
        return (ws, wf, -avg_t)
    if objective == "fast":
        return (wf + ws, -avg_t, 0)
    return (wf + ws, min(wf, ws), -avg_t)          # "both" (default)


def hillclimb(me_payload_fn, opp_payload, start_ids, pool_ids, lock_slots,
              lock_cards, objective, evals, repeats, nm, rng=None,
              batch_size=10, eval_many=None, topk=6):
    """Returns dict(best_ids, best_detail, evals_used, trace, finalists).

    me_payload_fn(ids) -> yisim player payload for MY side with those cards.
    `eval_many(cands) -> [[(seat, won, turns), ...], ...]` overrides the yisim
    evaluator (the Oracle pre-filter passes one in); `finalists` are the best
    distinct boards seen, for the arbiter engine to re-rank."""
    rng = rng or random.Random()
    lock_slots = {int(k): v for k, v in (lock_slots or {}).items()}
    lock_cards = list(lock_cards or [])
    pool_ids = [c for c in pool_ids if YB.combat_ok(c)]

    def evaluate_many(cands):
        if eval_many is not None:
            return eval_many(cands)
        battles = []
        for ids in cands:
            me = me_payload_fn(ids)
            for _ in range(repeats):
                battles.append((me, opp_payload, True))       # me first
                battles.append((opp_payload, me, True))       # me second
        res = YB.run_battles(battles)
        per, i = [], 0
        for ids in cands:
            rr = []
            for _ in range(repeats):
                r1, r2 = res[i], res[i + 1]
                i += 2
                rr.append(("first", r1.get("winner") == "a", r1.get("turns")))
                rr.append(("second", r2.get("winner") == "b", r2.get("turns")))
            per.append(rr)
        return per

    def detail(results):
        f = [r for r in results if r[0] == "first"]
        s = [r for r in results if r[0] == "second"]
        return (f"win {100*sum(r[1] for r in f)//max(1,len(f))}% first / "
                f"{100*sum(r[1] for r in s)//max(1,len(s))}% second")

    def propose(cur):
        ids = list(cur)
        free = [i for i in range(len(ids)) if i not in lock_slots]
        kind = rng.random()
        if kind < 0.35 and len(free) >= 2:                    # reorder
            i, j = rng.sample(free, 2)
            card = ids.pop(i)
            ids.insert(j, card)
            move = f"move {nm(card)} slot{i+1}->slot{j+1}"
        elif kind < 0.75 and free and pool_ids:               # swap-in
            i = rng.choice(free)
            if nm(ids[i]).split("+")[0] in [c.split("+")[0] for c in lock_cards]:
                return None
            new = rng.choice(pool_ids)
            move = f"swap {nm(ids[i])} -> {nm(new)} @slot{i+1}"
            ids[i] = new
        elif free:                                            # level bump
            i = rng.choice(free)
            v = _level_variant(ids[i], rng.choice((1, 1, -1)))
            if v is None:
                return None
            move = f"level {nm(ids[i])} -> {nm(v)}"
            ids[i] = v
        else:
            return None
        # re-pin locked slots (reorder may have shifted them)
        for idx, name in lock_slots.items():
            if idx < len(ids) and nm(ids[idx]) != name:
                hit = next((k for k, c in enumerate(ids) if nm(c) == name), None)
                if hit is None:
                    return None
                ids[idx], ids[hit] = ids[hit], ids[idx]
        if not _legal(ids) or not _satisfies_locks(ids, lock_slots, lock_cards, nm):
            return None
        return ids, move

    if not _legal(start_ids):
        raise ValueError("start board is illegal (combat/[消耗][持续] rule)")
    if not _satisfies_locks(start_ids, lock_slots, lock_cards, nm):
        raise ValueError("start board does not satisfy the locks")

    used = 1
    cur = list(start_ids)
    cur_res = evaluate_many([cur])[0]
    cur_score = _score(cur_res, objective)
    trace = [f"start: {detail(cur_res)}"]
    seen = {tuple(cur)}
    ranked = [(cur_score, list(cur))]        # every distinct board scored
    stall = 0
    while used < evals and stall < 2:
        cands, moves = [], []
        tries = 0
        while len(cands) < min(batch_size, evals - used) and tries < 60:
            tries += 1
            p = propose(cur)
            if p is None or tuple(p[0]) in seen:
                continue
            seen.add(tuple(p[0]))
            cands.append(p[0])
            moves.append(p[1])
        if not cands:
            break
        used += len(cands)
        scored = [(_score(r, objective), ids, mv, r) for ids, mv, r in
                  zip(cands, moves, evaluate_many(cands))]
        ranked.extend((sc, list(ids)) for sc, ids, _mv, _r in scored)
        best = max(scored, key=lambda x: x[0])
        if best[0] > cur_score:
            cur, cur_score = best[1], best[0]
            trace.append(f"{best[2]}: {detail(best[3])}")
            stall = 0
        else:
            stall += 1
    ranked.sort(key=lambda x: x[0], reverse=True)
    finalists, seen_f = [], set()
    for _sc, ids in ranked:
        key = tuple(ids)
        if key not in seen_f:
            seen_f.add(key)
            finalists.append(ids)
        if len(finalists) >= topk:
            break
    return {"best_ids": cur, "best_detail": trace[-1].split(": ", 1)[-1],
            "evals_used": used, "trace": trace, "finalists": finalists}
