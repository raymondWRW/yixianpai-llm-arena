# -*- coding: utf-8 -*-
"""Per-card value net — learns WHAT CARDS TO LOOK FOR.

The economy nets failed to move winrate because game-outcome reward can't credit
"rolled chaff → drew a key card → won three rounds later". This net attacks the
credit problem directly with an ADDITIVE ATTRIBUTION model:

    board_outcome ≈ mean over board cards of  V(context, card)

where board_outcome is the board's REAL battle result vs a recorded opponent
(ghost battles, normalised margin ∈ [0,1]). Every fielded board is a labelled
bag-of-cards; over thousands of boards with varied compositions the regression
identifies which cards raise outcomes in which contexts (round/realm/character/
career via the shared context encoder). V(state, card) IS "what to look for":
the roll/hold decisions are then COMPUTED from it against the known draw pool
(econ.py) instead of learned from scratch.

Reuses CardPolicyNet (context → per-card logit); sigmoid(logit) = the card's
value in [0,1]; the board prediction is the masked mean.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import encode as ENC
import net as NET
import policy_net as PN


class CardSynergyNet(nn.Module):
    """Per-card value CONDITIONED ON THE SET it plays with. Each candidate card
    attends over the co-cards (board+hand) before scoring, so interactions are
    first-class: 镜花剑阵 alone scores low, but with 巨鲲灵剑 in the set its
    attention picks that up and the value rises; qi-gain/qi-use complements
    likewise. Context (round/realm/char/career/天命/pooled cards) as before."""

    def __init__(self, emb_dim: int = 48, hidden: int = 256, heads: int = 4):
        super().__init__()
        Vb, Vf, Vc = ENC.base_vocab_size(), ENC.fate_vocab_size(), ENC.char_vocab_size()
        V = ENC.vocab_size()
        # LEVEL AS A MODIFIER (user design): card = base identity + level shift.
        # 回守·2 = emb(回守) + lvl(2) — it inherits everything learned at L1 plus
        # a level direction trained by EVERY card's merges, so rare L2s are no
        # longer untrained strangers defaulting to neutral.
        self.emb = nn.Embedding(Vb, emb_dim, padding_idx=0)      # base identity
        self.lvl_emb = nn.Embedding(4, emb_dim, padding_idx=0)   # level 1-3 shift
        self.ctx_card_emb = nn.Embedding(V, emb_dim, padding_idx=0)  # context pool
        self.fate_emb = nn.Embedding(Vf, 24, padding_idx=0)
        self.career_emb = nn.Embedding(8, 8)
        self.char_emb = nn.Embedding(Vc, 16, padding_idx=0)
        ctx_in = ENC.SCALAR_DIM + 2 * emb_dim + 24 + 8 + 16
        self.ctx = nn.Sequential(nn.Linear(ctx_in, hidden), nn.ReLU(),
                                 nn.Linear(hidden, hidden), nn.ReLU())
        self.attn = nn.MultiheadAttention(emb_dim, heads, batch_first=True)
        self.score = nn.Sequential(nn.Linear(hidden + 2 * emb_dim, hidden), nn.ReLU(),
                                   nn.Linear(hidden, 1))

    def card_emb(self, bidx, lidx):
        return self.emb(bidx) + self.lvl_emb(lidx)

    @staticmethod
    def _pool(emb, idx, mask):
        e = emb(idx); m = mask.unsqueeze(-1).float()
        return (e * m).sum(1) / m.sum(1).clamp_min(1.0)

    def context(self, b):
        board = self._pool(self.ctx_card_emb, b["board_idx"], b["board_mask"])
        hand = self._pool(self.ctx_card_emb, b["hand_idx"], b["hand_mask"])
        tal = self._pool(self.fate_emb, b["talent_idx"], b["talent_mask"])
        x = torch.cat([b["scalars"], board, hand, tal,
                       self.career_emb(b["career"]), self.char_emb(b["char"])], dim=-1)
        return self.ctx(x)

    def forward(self, b, cand_bl, cand_mask, set_bl, set_mask):
        """cand/set as (base_idx, level_idx) tensor pairs → logits (B,C)."""
        ctx = self.context(b)
        ce = self.card_emb(*cand_bl)                         # (B,C,e)
        se = self.card_emb(*set_bl)                          # (B,S,e)
        pad = ~set_mask
        pad = pad.masked_fill(pad.all(1, keepdim=True), False)   # avoid all-pad NaN
        att, _ = self.attn(ce, se, se, key_padding_mask=pad)
        ctx_e = ctx.unsqueeze(1).expand(-1, ce.size(1), -1)
        logits = self.score(torch.cat([ctx_e, ce, att], dim=-1)).squeeze(-1)
        return logits.masked_fill(~cand_mask, -1e9)


def stakes(rnd: int) -> float:
    """Typical |battle margin| (≈ 命 at stake) by round — the round's scale.
    Grows ~linearly then saturates: late rounds decide the game."""
    return min(34.0, 4.0 + 2.2 * max(1, int(rnd)))


def margin_target(margin: float, rnd: int) -> float:
    """ROUND-RELATIVE outcome target in [0,1]. Battle margins scale with round
    (R1 ±3-5 → R14 ±25-30+): a fixed /60 normalization starves early rounds of
    gradient (targets huddle at 0.5) and clips decisive late battles — which is
    also why per-card PHASE FALLOFF (回守/小还丹 strong early, weak late) never
    got learned. Normalize by the round's typical scale instead: 0.6 now means
    'clearly winning for this round' at every round."""
    s = stakes(rnd)                                 # ≈ p80 |margin| by round
    m = max(-s, min(s, float(margin)))
    return m / (2 * s) + 0.5


def _bl_tensors(card_lists, dev):
    """List of id-lists → ((base_idx, level_idx), mask) padded tensors."""
    B = len(card_lists)
    C = max((len(c) for c in card_lists), default=1) or 1
    bidx = torch.zeros(B, C, dtype=torch.long)
    lidx = torch.zeros(B, C, dtype=torch.long)
    mask = torch.zeros(B, C, dtype=torch.bool)
    for i, ids in enumerate(card_lists):
        for j, c in enumerate(ids):
            b, l = ENC.base_level_idx(c)
            bidx[i, j] = b; lidx[i, j] = l; mask[i, j] = True
    return (bidx.to(dev), lidx.to(dev)), mask.to(dev)


def _collate(batch, dev):
    """batch: [{state, cards, target}] → context + (base,level) idx/mask (cards
    double as the attention SET at train time)."""
    ctx = NET.collate([ENC.encode(b["state"]) for b in batch], dev)
    cbl, cmsk = _bl_tensors([b["cards"] for b in batch], dev)
    y = torch.tensor([float(b["target"]) for b in batch], dtype=torch.float32,
                     device=dev)
    return ctx, cbl, cmsk, y


def train(samples, epochs=20, batch=256, lr=1e-3, val_frac=0.12, seed=0,
          emb_dim=48, hidden=256, out=None, init=None, log=print):
    """MSE on board outcome = masked-mean of per-card sigmoids, with each card's
    value computed by the SYNERGY net (attending over its co-cards). init: path
    of a previous synergy checkpoint to WARM-START from (continual training —
    fewer epochs needed per iteration)."""
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(samples))
    nval = max(1, int(len(samples) * val_frac))
    val_idx, tr_idx = idx[:nval], idx[nval:]
    dev = PN.device()
    net = CardSynergyNet(emb_dim=emb_dim, hidden=hidden).to(dev)
    if init:
        try:
            ck = torch.load(init, map_location=dev)
            if ck.get("arch") == "synergy2":
                net.load_state_dict(ck["model"])
                log(f"  warm-start from {init}")
        except Exception:
            pass
    opt = torch.optim.Adam(net.parameters(), lr=lr, weight_decay=1e-5)
    log(f"card-value(synergy): {len(samples)} boards (train {len(tr_idx)} / val {nval}), device {dev}")

    def run(ids):
        ctx, cbl, cmsk, y = _collate([samples[i] for i in ids], dev)
        logits = net(ctx, cbl, cmsk, cbl, cmsk)       # set = the board itself
        vals = torch.sigmoid(logits)
        m = cmsk.float()
        pred = (vals * m).sum(1) / m.sum(1).clamp_min(1)
        return pred, y, ((pred - y) ** 2).mean()

    best = None
    for ep in range(1, epochs + 1):
        net.train()
        perm = rng.permutation(len(tr_idx))
        for s in range(0, len(perm), batch):
            _, _, loss = run(tr_idx[perm[s:s + batch]])
            opt.zero_grad(); loss.backward(); opt.step()
        net.eval()
        with torch.no_grad():
            pred, y, vloss = run(val_idx)
            # rank quality: do predicted board values order actual outcomes?
            pr = pred.cpu().numpy(); yy = y.cpu().numpy()
            rho = float(np.corrcoef(np.argsort(np.argsort(pr)),
                                    np.argsort(np.argsort(yy)))[0, 1]) if len(pr) > 2 else 0
        if best is None or vloss.item() < best[0]:
            best = (vloss.item(), ep, rho)
            if out:
                torch.save({"model": net.state_dict(), "emb_dim": emb_dim,
                            "hidden": hidden, "arch": "synergy2"}, out)
        if ep % 4 == 0 or ep == 1:
            log(f"  ep {ep:2d}  valMSE={vloss.item():.4f}  boardSpearman={rho:.3f}")
    log(f"  BEST valMSE={best[0]:.4f} (Spearman {best[2]:.3f}) @ep{best[1]}"
        + (f" → {out}" if out else ""))
    return best


def load(path):
    """Load a card-value checkpoint — synergy2 (current) or CardPolicyNet (old)."""
    dev = PN.device()
    ck = torch.load(path, map_location=dev)
    if ck.get("arch") == "synergy2":
        net = CardSynergyNet(emb_dim=ck.get("emb_dim", 48),
                             hidden=ck.get("hidden", 256)).to(dev)
        net.load_state_dict(ck["model"]); net.eval()
        return net
    return PN.load(path)


@torch.no_grad()
def board_scores(net, state: dict, boards: list) -> np.ndarray:
    """Predicted outcome for each candidate BOARD (list of id-lists) — one
    batched forward for the synergy net. Used to PRESCREEN placement candidates
    so the Oracle only battles the top few (search speedup)."""
    if not boards:
        return np.zeros(0, dtype=np.float32)
    if not isinstance(net, CardSynergyNet):          # old arch: per-board loop
        out = []
        for b_ids in boards:
            v = card_values(net, state, b_ids)
            out.append(float(v.mean()) if len(v) else 0.0)
        return np.array(out, dtype=np.float32)
    dev = next(net.parameters()).device
    B = len(boards)
    ctx = NET.collate([ENC.encode(state)] * B, dev)
    cbl, cmsk = _bl_tensors(boards, dev)
    logits = net(ctx, cbl, cmsk, cbl, cmsk)
    vals = torch.sigmoid(logits)
    m = cmsk.float()
    pred = (vals * m).sum(1) / m.sum(1).clamp_min(1)
    return pred.cpu().numpy()


@torch.no_grad()
def card_values(net, state: dict, candidates: list, set_ids=None) -> np.ndarray:
    """V(state, card | set) ∈ [0,1] per candidate. set_ids = the cards this
    candidate would play WITH (board+hand); default = state's board+hand. Old
    (non-synergy) nets ignore the set."""
    if not candidates:
        return np.zeros(0, dtype=np.float32)
    if not isinstance(net, CardSynergyNet):
        logits = PN.score_cards(net, state, candidates)
        return 1.0 / (1.0 + np.exp(-logits))
    dev = next(net.parameters()).device
    if set_ids is None:
        set_ids = [c for c in state.get("board", []) if c] + \
                  [c for c in state.get("hand_ids", []) if isinstance(c, int)]
    set_ids = list(set_ids) or [0]
    b = NET.collate([ENC.encode(state)], dev)
    cbl, cmsk = _bl_tensors([list(candidates)], dev)
    sbl, smsk = _bl_tensors([set_ids], dev)
    logits = net(b, cbl, cmsk, sbl, smsk)[0].cpu().numpy()
    return 1.0 / (1.0 + np.exp(-logits))
