# -*- coding: utf-8 -*-
"""Value/policy network for the offline model.

CardValueNet: embeds board + hand card ids (shared table, masked-mean pooled),
concatenates the scalar features, and an MLP produces a scalar VALUE = predicted
final-placement reward in [0,1] (1.0 = 1st of 8, 0.0 = last). Optional policy head
over a small economy action set (added when the planner needs priors).

Device-agnostic: `device()` picks CUDA when a CUDA torch build is present, else
CPU. The prototype runs fine on CPU (tiny net, Oracle-bottlenecked data); the same
code moves to the RTX 3060 once a CUDA torch is installed for the scaling phase.
"""
from __future__ import annotations

import numpy as np
import torch
import torch.nn as nn

import encode as ENC


def device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


class CardValueNet(nn.Module):
    def __init__(self, vocab_size: int | None = None, emb_dim: int = 48,
                 hidden: int = 256, n_actions: int = 0):
        super().__init__()
        V = vocab_size or ENC.vocab_size()
        Vf = ENC.fate_vocab_size()
        Vc = ENC.char_vocab_size()
        fate_dim, career_dim, char_dim = 24, 8, 16
        self.emb = nn.Embedding(V, emb_dim, padding_idx=0)            # cards
        self.fate_emb = nn.Embedding(Vf, fate_dim, padding_idx=0)    # 天命 talents
        self.career_emb = nn.Embedding(8, career_dim)               # 副职 (0-7)
        self.char_emb = nn.Embedding(Vc, char_dim, padding_idx=0)   # character (who)
        feat = ENC.SCALAR_DIM + 2 * emb_dim + fate_dim + career_dim + char_dim
        self.trunk = nn.Sequential(
            nn.Linear(feat, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU(),
        )
        self.value_head = nn.Linear(hidden, 1)
        self.policy_head = nn.Linear(hidden, n_actions) if n_actions > 0 else None

    @staticmethod
    def _pool_emb(emb, idx, mask):
        e = emb(idx)                                       # (B, L, D)
        m = mask.unsqueeze(-1).float()
        return (e * m).sum(dim=1) / m.sum(dim=1).clamp_min(1.0)

    def _pool(self, idx, mask):
        return self._pool_emb(self.emb, idx, mask)

    def forward(self, scalars, board_idx, board_mask, hand_idx, hand_mask,
                talent_idx, talent_mask, career, char):
        b = self._pool(board_idx, board_mask)
        h = self._pool(hand_idx, hand_mask)
        t = self._pool_emb(self.fate_emb, talent_idx, talent_mask)
        c = self.career_emb(career)
        ch = self.char_emb(char)
        x = torch.cat([scalars, b, h, t, c, ch], dim=-1)
        z = self.trunk(x)
        v = torch.sigmoid(self.value_head(z)).squeeze(-1)  # (B,) in [0,1]
        if self.policy_head is not None:
            return v, self.policy_head(z)
        return v


# ── batching ─────────────────────────────────────────────────────────────────
def collate(samples: list, dev: torch.device | None = None) -> dict:
    """List of encode.encode() dicts → padded tensors on `dev`."""
    dev = dev or device()
    B = len(samples)
    sc = torch.from_numpy(np.stack([s["scalars"] for s in samples])).to(dev)
    bl = max((len(s["board"]) for s in samples), default=0) or 1
    hl = max((len(s["hand"]) for s in samples), default=0) or 1
    tl = max((len(s.get("talents", [])) for s in samples), default=0) or 1
    bidx = torch.zeros(B, bl, dtype=torch.long)
    bmsk = torch.zeros(B, bl, dtype=torch.bool)
    hidx = torch.zeros(B, hl, dtype=torch.long)
    hmsk = torch.zeros(B, hl, dtype=torch.bool)
    tidx = torch.zeros(B, tl, dtype=torch.long)
    tmsk = torch.zeros(B, tl, dtype=torch.bool)
    career = torch.zeros(B, dtype=torch.long)
    char = torch.zeros(B, dtype=torch.long)
    for i, s in enumerate(samples):
        for j, c in enumerate(s["board"]):
            bidx[i, j] = c; bmsk[i, j] = True
        for j, c in enumerate(s["hand"]):
            hidx[i, j] = c; hmsk[i, j] = True
        for j, c in enumerate(s.get("talents", [])):
            tidx[i, j] = c; tmsk[i, j] = True
        career[i] = int(s.get("career", 0) or 0)
        char[i] = int(s.get("char", 0) or 0)
    return {"scalars": sc, "board_idx": bidx.to(dev), "board_mask": bmsk.to(dev),
            "hand_idx": hidx.to(dev), "hand_mask": hmsk.to(dev),
            "talent_idx": tidx.to(dev), "talent_mask": tmsk.to(dev),
            "career": career.to(dev), "char": char.to(dev)}


def load(path: str, dev: torch.device | None = None) -> CardValueNet:
    """Rebuild a CardValueNet from a train_value.py checkpoint."""
    dev = dev or device()
    ck = torch.load(path, map_location=dev)
    net = CardValueNet(vocab_size=ck.get("vocab"), emb_dim=ck["emb_dim"],
                       hidden=ck["hidden"]).to(dev)
    net.load_state_dict(ck["model"])
    net.eval()
    return net


@torch.no_grad()
def predict_values(net: CardValueNet, states: list, dev=None) -> np.ndarray:
    """Value in [0,1] for a list of raw state dicts."""
    dev = dev or next(net.parameters()).device       # match the net's device
    net.eval()
    batch = collate([ENC.encode(s) for s in states], dev)
    out = net(batch["scalars"], batch["board_idx"], batch["board_mask"],
              batch["hand_idx"], batch["hand_mask"],
              batch["talent_idx"], batch["talent_mask"], batch["career"], batch["char"])
    v = out[0] if isinstance(out, tuple) else out
    return v.detach().cpu().numpy()


if __name__ == "__main__":
    dev = device()
    print("device:", dev, " vocab:", ENC.vocab_size())
    net = CardValueNet().to(dev)
    n_params = sum(p.numel() for p in net.parameters())
    print(f"params: {n_params:,}")
    states = [
        {"round": 8, "realm": 3, "cultivation": 24, "destiny": 80, "unlocked": 6,
         "alive": 5, "board": [1, 4, 5, 6], "hand_ids": [7, 3]},
        {"round": 2, "realm": 1, "cultivation": 2, "destiny": 100, "unlocked": 4,
         "alive": 8, "board": [1], "hand_ids": []},
    ]
    print("values:", predict_values(net, states))
