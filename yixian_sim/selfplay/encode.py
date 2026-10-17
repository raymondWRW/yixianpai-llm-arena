# -*- coding: utf-8 -*-
"""State → features for the value/policy net.

A decision state is one player's prep situation. We encode it as:
  · scalars   — round, realm, cultivation, destiny, slots, alive-count, … (normed)
  · board     — the card ids currently placed (→ vocab indices, embedded+pooled)
  · hand      — the card ids held           (→ vocab indices, embedded+pooled)

The net learns board/hand STRENGTH from the card embeddings + stats, so V is a
pure function of features — NO Oracle call at inference (that's the whole point:
a fast value for planning). Combat strength that the Oracle computes exactly is
what the embeddings must learn to approximate for THIS purpose (final-placement
value), which is a much easier target than exact lifeDamage.

Card vocabulary = every id in proxy/card_id_map.json (+ 0 = empty/普攻 = index 0).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

_REPO = Path(__file__).resolve().parent.parent
for _p in (str(_REPO / "proxy"), str(_REPO)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

_ID_MAP_FILE = _REPO / "proxy" / "card_id_map.json"

# ── card vocabulary ──────────────────────────────────────────────────────────
_vocab = None          # id -> index


def vocab() -> dict:
    global _vocab
    if _vocab is None:
        raw = json.loads(_ID_MAP_FILE.read_text(encoding="utf-8"))
        ids = sorted(int(k) for k in raw.keys())
        # index 0 reserved for pad/empty; real ids start at 1
        _vocab = {0: 0}
        for i in ids:
            if i not in _vocab:
                _vocab[i] = len(_vocab)
    return _vocab


def vocab_size() -> int:
    return len(vocab())


def card_idx(cid: int) -> int:
    return vocab().get(int(cid), 0)


# ── base-id vocabulary (level-agnostic) + level split ─────────────────────────
# A leveled card = base identity + level (id + 10000·(level−1)). Nets that model
# level as a learned MODIFIER on the base embedding use (base_idx, level) so an
# L2 inherits everything learned at L1 plus a shared "level direction".
_base_vocab = None


def base_vocab() -> dict:
    global _base_vocab
    if _base_vocab is None:
        _base_vocab = {0: 0}
        for i in sorted(vocab()):
            if i:
                lv = ((int(i) // 10000) % 100)
                b = int(i) - lv * 10000
                _base_vocab.setdefault(b, len(_base_vocab))
    return _base_vocab


def base_vocab_size() -> int:
    return len(base_vocab())


def base_level_idx(cid: int) -> tuple:
    """(base_index, level 1-3) for a card id; (0, 0) for pad/empty."""
    cid = int(cid)
    if not cid:
        return 0, 0
    lv = ((cid // 10000) % 100) + 1
    b = cid - (lv - 1) * 10000
    return base_vocab().get(b, 0), min(lv, 3)


# ── fate vocabulary (天命 ids → index, for talent embedding) ───────────────────
_fate_vocab = None


def fate_vocab() -> dict:
    global _fate_vocab
    if _fate_vocab is None:
        import fates as FA
        ids = sorted(FA.all_fates())
        _fate_vocab = {0: 0}
        for i in ids:
            _fate_vocab.setdefault(i, len(_fate_vocab))
    return _fate_vocab


def fate_vocab_size() -> int:
    return len(fate_vocab())


def fate_idx(fid: int) -> int:
    return fate_vocab().get(int(fid), 0)


# ── scalar features ──────────────────────────────────────────────────────────
# order is fixed — net input width depends on it. Keep in sync with SCALAR_DIM.
SCALAR_DIM = 14


def scalars(st: dict) -> np.ndarray:
    """st keys: round, realm, cultivation, destiny, unlocked, alive, extra_hp, tipo,
    max_tipo, rerolls, board (ids), hand (ids), talents. Missing keys default."""
    board = [c for c in st.get("board", []) if c]
    hand = st.get("hand_ids", st.get("hand", []))
    hand = [c for c in hand if isinstance(c, int)]
    rnd = float(st.get("round", 0))
    realm = float(st.get("realm", 1))
    return np.array([
        rnd / 20.0,
        realm / 5.0,
        float(st.get("cultivation", 0)) / 75.0,
        float(st.get("destiny", 100)) / 100.0,
        float(st.get("unlocked", 8)) / 8.0,
        float(st.get("alive", 8)) / 8.0,
        float(st.get("extra_hp", 0)) / 100.0,
        float(st.get("tipo", 0)) / 100.0,             # 体魄 physique
        float(st.get("max_tipo", 0)) / 100.0,         # 体魄上限
        float(st.get("rerolls", 0)) / 5.0,
        len(st.get("talents", [])) / 5.0,             # 天命 count
        len(board) / 8.0,
        min(len(hand), 20) / 20.0,
        # realm-vs-round tempo: >0 = ahead of the round's baseline realm curve
        (realm - (1.0 + rnd / 5.0)) / 5.0,
    ], dtype=np.float32)


def board_indices(st: dict) -> list:
    return [card_idx(c) for c in st.get("board", []) if c]


def hand_indices(st: dict) -> list:
    hand = st.get("hand_ids", st.get("hand", []))
    return [card_idx(c) for c in hand if isinstance(c, int)]


def char_index(cid) -> int:
    import characters as CH
    return CH.char_index(cid)


def char_vocab_size() -> int:
    import characters as CH
    return CH.char_vocab_size()


def encode(st: dict) -> dict:
    """One sample: scalars + board/hand card indices + character + career (0-7) +
    talent (fate) indices — everything the value net needs, incl. WHO the player is
    (character), 副职, and 天命 identity (so picks can be character-specific)."""
    return {"scalars": scalars(st), "board": board_indices(st), "hand": hand_indices(st),
            "char": char_index(st.get("char_id", 0)),
            "career": int(st.get("career", 0) or 0),
            "talents": [fate_idx(t) for t in st.get("talents", [])]}


if __name__ == "__main__":
    print("vocab size:", vocab_size(), " scalar dim:", SCALAR_DIM)
    s = {"round": 8, "realm": 3, "cultivation": 24, "destiny": 80, "unlocked": 6,
         "alive": 5, "board": [1, 4, 5, 6], "hand_ids": [7, 3]}
    e = encode(s)
    print("scalars:", e["scalars"])
    print("board idx:", e["board"], " hand idx:", e["hand"])
