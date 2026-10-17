# -*- coding: utf-8 -*-
"""A fast `scorer` (battle-net) that drops into placement in place of the Oracle.

placement.best_board / best_ordering call `scorer(pairs, rnd) -> [{lifeDamage,
hpDelta, win}]`. The Oracle scorer runs ~5ms/battle across a worker pool; this one
runs the whole batch of pairs through ONE battle-net forward pass — no combat sim —
so ordering search / MCTS / large self-play stop being Oracle-bound.
"""
from __future__ import annotations

import sys
from pathlib import Path

import torch

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import battlenet as BN


def net_scorer(net, dev=None, chunk: int = 8192):
    """Wrap a loaded BattleNet as a placement scorer."""
    dev = dev or BN.device()
    net.eval()

    def score(pairs, rnd):
        if not pairs:
            return []
        out = []
        for s in range(0, len(pairs), chunk):
            chunk_pairs = pairs[s:s + chunk]
            samples = [{"a": a, "b": b, "round": rnd} for a, b in chunk_pairs]
            batch = BN.collate(samples, dev)
            with torch.no_grad():
                life, hp, win = net(batch)
            life = life.cpu().numpy(); hp = hp.cpu().numpy()
            win = torch.sigmoid(win).cpu().numpy()
            for i in range(len(chunk_pairs)):
                out.append({"lifeDamage": float(life[i]), "hpDelta": float(hp[i]),
                            "win": bool(win[i] > 0.5)})
        return out
    return score


def load_scorer(path: str, dev=None):
    return net_scorer(BN.load(path, dev), dev)
