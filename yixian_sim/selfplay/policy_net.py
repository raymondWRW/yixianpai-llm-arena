# -*- coding: utf-8 -*-
"""Card-placement POLICY net — learns WHICH cards to play each round.

The Oracle placement search is the expert: given the cards a player holds
(board+hand) it picks the best board vs the field (~200 battles). This net learns
to imitate that choice — for each candidate card it predicts P(the search plays it)
— so at play time we score the cards in ONE forward pass and take the top `slots`,
no combat search.

Encoding mirrors the value net: a context vector from scalars + character + career +
天命 talents + pooled board/hand; then each candidate card is scored by an MLP over
[context, card_embedding]. Shares the card vocab with encode.py.
"""
from __future__ import annotations

import numpy as np
import torch
import torch.nn as nn

import encode as ENC


def device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


class CardPolicyNet(nn.Module):
    def __init__(self, emb_dim: int = 48, hidden: int = 256):
        super().__init__()
        V, Vf, Vc = ENC.vocab_size(), ENC.fate_vocab_size(), ENC.char_vocab_size()
        self.emb = nn.Embedding(V, emb_dim, padding_idx=0)
        self.fate_emb = nn.Embedding(Vf, 24, padding_idx=0)
        self.career_emb = nn.Embedding(8, 8)
        self.char_emb = nn.Embedding(Vc, 16, padding_idx=0)
        ctx_in = ENC.SCALAR_DIM + 2 * emb_dim + 24 + 8 + 16
        self.ctx = nn.Sequential(nn.Linear(ctx_in, hidden), nn.ReLU(),
                                 nn.Linear(hidden, hidden), nn.ReLU())
        self.score = nn.Sequential(nn.Linear(hidden + emb_dim, hidden), nn.ReLU(),
                                   nn.Linear(hidden, 1))

    @staticmethod
    def _pool(emb, idx, mask):
        e = emb(idx); m = mask.unsqueeze(-1).float()
        return (e * m).sum(1) / m.sum(1).clamp_min(1.0)

    def context(self, b):
        board = self._pool(self.emb, b["board_idx"], b["board_mask"])
        hand = self._pool(self.emb, b["hand_idx"], b["hand_mask"])
        tal = self._pool(self.fate_emb, b["talent_idx"], b["talent_mask"])
        x = torch.cat([b["scalars"], board, hand, tal,
                       self.career_emb(b["career"]), self.char_emb(b["char"])], dim=-1)
        return self.ctx(x)                                   # (B, hidden)

    def forward(self, b, cand_idx, cand_mask):
        """cand_idx (B, C) candidate card vocab-indices → logits (B, C)."""
        ctx = self.context(b)                                # (B, hidden)
        ce = self.emb(cand_idx)                              # (B, C, emb)
        ctx_e = ctx.unsqueeze(1).expand(-1, ce.size(1), -1)  # (B, C, hidden)
        logits = self.score(torch.cat([ctx_e, ce], dim=-1)).squeeze(-1)  # (B, C)
        return logits.masked_fill(~cand_mask, -1e9)


def load(path, dev=None) -> CardPolicyNet:
    dev = dev or device()
    ck = torch.load(path, map_location=dev)
    net = CardPolicyNet(emb_dim=ck.get("emb_dim", 48), hidden=ck.get("hidden", 256)).to(dev)
    net.load_state_dict(ck["model"]); net.eval()
    return net


@torch.no_grad()
def score_cards(net, state: dict, candidates: list, dev=None) -> np.ndarray:
    """Per-candidate play-logit for one state (candidates = card ids)."""
    dev = dev or next(net.parameters()).device
    import net as NET
    b = NET.collate([ENC.encode(state)], dev)
    cidx = torch.zeros(1, len(candidates), dtype=torch.long, device=dev)
    cmsk = torch.zeros(1, len(candidates), dtype=torch.bool, device=dev)
    for j, c in enumerate(candidates):
        cidx[0, j] = ENC.card_idx(c); cmsk[0, j] = True
    return net(b, cidx, cmsk)[0].cpu().numpy()


if __name__ == "__main__":
    net = CardPolicyNet().to(device())
    print("device:", device(), " params:", f"{sum(p.numel() for p in net.parameters()):,}")
    st = {"char_id": 1000001, "round": 6, "realm": 3, "career": 2, "talents": [1],
          "board": [1, 4], "hand_ids": [5, 6, 7, 3]}
    print("card scores:", score_cards(net, st, [1, 4, 5, 6, 7, 3]))
