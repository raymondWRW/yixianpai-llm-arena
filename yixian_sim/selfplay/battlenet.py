# -*- coding: utf-8 -*-
"""Battle-net: a fast neural approximation of the Oracle combat engine.

Predicts a matchup outcome — lifeDamage (the destiny margin the search actually
uses), hpDelta, and win — from both sides' ORDERED boards + stats, WITHOUT running
the ~5ms Oracle sim. This is the piece that unblocks scale: ordering search / MCTS
/ large self-play evaluate boards through a batched GPU forward pass instead.

Order-aware by construction: each side's ≤8 board slots get card embeddings + slot
POSITIONAL embeddings through a small Transformer encoder (order changes combat —
that's the whole point), masked-mean pooled to a side vector; concatenated with the
opponent side + both stat blocks → MLP → three heads.

Card vocab is shared with encode.py (all card_id_map ids, incl. leveled/merged ids).
"""
from __future__ import annotations

import numpy as np
import torch
import torch.nn as nn

import encode as ENC

MAX_SLOTS = 8


def device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ── fixture → tensors ─────────────────────────────────────────────────────────
def side_features(fx: dict) -> dict:
    """One side: ordered board vocab-indices (≤8), sect index, normed stats."""
    board = [ENC.card_idx(c) for c in fx.get("usedCards", []) if c][:MAX_SLOTS]
    sect = int(fx.get("characterId", 0)) // 1_000_000
    stats = np.array([
        float(fx.get("level", 1)) / 5.0,
        float(fx.get("exp", 0)) / 75.0,
        float(fx.get("extraMaxHp", 0)) / 100.0,
        float(fx.get("unlockGrids", 8)) / 8.0,
    ], dtype=np.float32)
    return {"board": board, "sect": min(max(sect, 0), 7), "stats": stats}


def encode_sample(s: dict) -> dict:
    return {"a": side_features(s["a"]), "b": side_features(s["b"]),
            "round": float(s.get("round", 8)) / 20.0}


class BattleNet(nn.Module):
    def __init__(self, vocab_size: int | None = None, emb: int = 64, nhead: int = 4,
                 layers: int = 2, hidden: int = 256, n_sect: int = 8):
        super().__init__()
        V = vocab_size or ENC.vocab_size()
        self.emb = nn.Embedding(V, emb, padding_idx=0)
        self.pos = nn.Embedding(MAX_SLOTS, emb)
        enc_layer = nn.TransformerEncoderLayer(emb, nhead, dim_feedforward=2 * emb,
                                               batch_first=True, dropout=0.0)
        self.enc = nn.TransformerEncoder(enc_layer, layers)
        self.sect_emb = nn.Embedding(n_sect, 8)
        side_dim = emb + 8 + 4                      # board + sect + stats
        self.trunk = nn.Sequential(
            nn.Linear(2 * side_dim + 1, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU(),
        )
        self.life = nn.Linear(hidden, 1)
        self.hp = nn.Linear(hidden, 1)
        self.win = nn.Linear(hidden, 1)

    def _side(self, board_idx, mask, sect, stats):
        pos = torch.arange(MAX_SLOTS, device=board_idx.device).unsqueeze(0)
        e = self.emb(board_idx) + self.pos(pos)
        z = self.enc(e, src_key_padding_mask=~mask)          # ignore PAD slots
        m = mask.unsqueeze(-1).float()
        pooled = (z * m).sum(1) / m.sum(1).clamp_min(1.0)
        return torch.cat([pooled, self.sect_emb(sect), stats], dim=-1)

    def forward(self, batch):
        sa = self._side(batch["a_board"], batch["a_mask"], batch["a_sect"], batch["a_stats"])
        sb = self._side(batch["b_board"], batch["b_mask"], batch["b_sect"], batch["b_stats"])
        h = self.trunk(torch.cat([sa, sb, batch["round"].unsqueeze(-1)], dim=-1))
        return self.life(h).squeeze(-1), self.hp(h).squeeze(-1), self.win(h).squeeze(-1)


def collate(samples: list, dev=None) -> dict:
    """Encoded samples → padded tensors on `dev`. Accepts raw samples (dicts with
    'a'/'b' fixtures) or already-encoded ones."""
    dev = dev or device()
    enc = [s if "round" in s and isinstance(s["a"], dict) and "board" in s["a"]
           else encode_sample(s) for s in samples]
    B = len(enc)

    def side(key):
        bidx = torch.zeros(B, MAX_SLOTS, dtype=torch.long)
        bmsk = torch.zeros(B, MAX_SLOTS, dtype=torch.bool)
        sect = torch.zeros(B, dtype=torch.long)
        stats = torch.zeros(B, 4, dtype=torch.float32)
        for i, s in enumerate(enc):
            sd = s[key]
            for j, c in enumerate(sd["board"][:MAX_SLOTS]):
                bidx[i, j] = c; bmsk[i, j] = True
            if not sd["board"]:
                bmsk[i, 0] = True                    # avoid all-masked row (NaN)
            sect[i] = sd["sect"]
            stats[i] = torch.from_numpy(sd["stats"])
        return bidx.to(dev), bmsk.to(dev), sect.to(dev), stats.to(dev)

    ab, am, asc, ast = side("a")
    bb, bm, bsc, bst = side("b")
    rnd = torch.tensor([s["round"] for s in enc], dtype=torch.float32, device=dev)
    return {"a_board": ab, "a_mask": am, "a_sect": asc, "a_stats": ast,
            "b_board": bb, "b_mask": bm, "b_sect": bsc, "b_stats": bst, "round": rnd}


def pack(samples: list, dev=None) -> dict:
    """Pre-build contiguous tensors for the WHOLE dataset once (so training batches
    by tensor INDEXING, not a per-batch Python collate loop — that Python loop, not
    GPU compute, is the real bottleneck). Returns tensors kept on CPU; move batch
    slices to the device in the train loop. Keys mirror collate() + per-side, plus
    'round'."""
    n = len(samples)
    a_board = np.zeros((n, MAX_SLOTS), np.int64); a_mask = np.zeros((n, MAX_SLOTS), bool)
    a_sect = np.zeros(n, np.int64); a_stats = np.zeros((n, 4), np.float32)
    b_board = np.zeros((n, MAX_SLOTS), np.int64); b_mask = np.zeros((n, MAX_SLOTS), bool)
    b_sect = np.zeros(n, np.int64); b_stats = np.zeros((n, 4), np.float32)
    rnd = np.zeros(n, np.float32)
    for i, s in enumerate(samples):
        for key, bd, mk, sc, st in (("a", a_board, a_mask, a_sect, a_stats),
                                    ("b", b_board, b_mask, b_sect, b_stats)):
            sd = side_features(s[key])
            cards = sd["board"][:MAX_SLOTS]
            for j, c in enumerate(cards):
                bd[i, j] = c; mk[i, j] = True
            if not cards:
                mk[i, 0] = True
            sc[i] = sd["sect"]; st[i] = sd["stats"]
        rnd[i] = float(s.get("round", 8)) / 20.0
    t = lambda x: torch.from_numpy(x)
    return {"a_board": t(a_board), "a_mask": t(a_mask), "a_sect": t(a_sect), "a_stats": t(a_stats),
            "b_board": t(b_board), "b_mask": t(b_mask), "b_sect": t(b_sect), "b_stats": t(b_stats),
            "round": t(rnd)}


def slice_batch(packed: dict, idx, dev) -> dict:
    """Index the packed tensors for a batch and move to device."""
    return {k: v[idx].to(dev, non_blocking=True) for k, v in packed.items()}


def load(path: str, dev=None) -> BattleNet:
    dev = dev or device()
    ck = torch.load(path, map_location=dev)
    net = BattleNet(vocab_size=ck.get("vocab"), **ck.get("arch", {})).to(dev)
    net.load_state_dict(ck["model"]); net.eval()
    return net


if __name__ == "__main__":
    dev = device()
    net = BattleNet().to(dev)
    print("device:", dev, " params:", f"{sum(p.numel() for p in net.parameters()):,}")
    s = [{"a": {"characterId": 1000001, "level": 3, "exp": 20, "usedCards": [5, 6, 7], "unlockGrids": 6},
          "b": {"characterId": 1000001, "level": 3, "exp": 20, "usedCards": [1, 4], "unlockGrids": 6},
          "round": 8}]
    b = collate(s, dev)
    life, hp, win = net(b)
    print("life", float(life[0]), "hp", float(hp[0]), "win", float(torch.sigmoid(win[0])))
