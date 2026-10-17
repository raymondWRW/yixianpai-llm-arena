# -*- coding: utf-8 -*-
"""Offline YiXianPai environment — 8-player self-play loop (MILESTONE-1 skeleton).

Structure only; the fidelity-critical rules are wired to economy.py / draws.py
(confirmed pieces) with explicit STUBs where a rule is still open (marked
`# STUB`). Runs a full game end-to-end with a trivial policy so the loop is
exercised; battle resolves via the Oracle when available, else a placeholder.

Design (see GAME_MODEL.md):
  · the agent acts only in prep; battle auto-resolves (Oracle = exact).
  · placement (the 8-slot arrangement) is a MACRO-ACTION delegated to the
    existing oracle_sim search — NOT learned here (seam: `arrange_board`).
  · draws = chance events (draws.DrawBag, seeded rng) for MCTS chance nodes.
Everything stochastic takes an explicit rng for reproducibility.
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field

import economy as E
import draws as D
import cards as C
import field as F
import placement as P
import merge as M
import fates as FA
import body as B

HAND_LIMIT = 16          # safety bound only — real hands reach 15+ (mined); the
                         # hold/absorb POLICY decides carries, not this cap


@dataclass
class PlayerState:
    pid: int
    char_id: int
    sect_prefix: int                       # char_id // 1_000_000
    cultivation: int = 0
    realm: int = 1
    extra_hp: int = 0                      # +max HP from 天命 fates
    tipo: int = 0                          # 体魄 physique (combat stat)
    max_tipo: int = 0                      # 体魄上限 physique cap
    destiny: int = 100                     # 命 pool; 0 = eliminated
    talents: list = field(default_factory=list)   # 天命 fate ids (→ Oracle combat)
    talent_phases: dict = field(default_factory=dict)  # fate id → pick phase (version)
    board: list = field(default_factory=lambda: [0] * 8)   # card ids, 0 = 普攻
    hand: list = field(default_factory=list)               # card IDS (level-1 base)
    rerolls: int = 0
    free_roll_used: bool = False           # 云雾变幻: first 换牌 each round is free
    alive: bool = True
    bag: "D.DrawBag" = None
    career: int = 0                        # 副职 sidejob (1-7), picked round 2; 0 = none yet
    last_opp: int = -1                     # pid faced last round (avoid immediate repeat)
    pending_grants: list = field(default_factory=list)  # 道韵 picks: (phase, base_id)
    # fates / derivations / sidejobs would live here too (later milestone)

    @property
    def max_hp(self) -> int:
        return E.max_hp(self.realm, self.extra_hp)

    @property
    def phase(self) -> int:
        # card phase available = realm (phases unlock with realm). Confirm exact
        # phase↔realm mapping in fidelity; realm is the working proxy. # STUB
        return self.realm

    def to_fixture(self, unlocked: int = 8) -> dict:
        """Oracle-ready side dict for this player's current board + stats.
        Under-full boards are PADDED with explicit 0s (普攻) to the unlocked slot
        count — the engine treats len(usedCards) as the CYCLE length, so an
        unpadded short board runs a phantom fast loop the real game doesn't
        (empty slots fire basic attacks). This artifact made 2-card boards
        'beat' real full boards."""
        used = list(self.board[:unlocked])     # keep the ARRANGEMENT: embedded 0s
        while len(used) < unlocked:            # are positioned 普攻 slots (the
            used.append(0)                     # ordering search moves them)
        return {"characterId": self.char_id, "level": self.realm,
                "exp": self.cultivation, "extraMaxHp": self.extra_hp,
                "usedCards": used, "unlockGrids": unlocked,
                # cards KEPT in hand — combat reads these (灵猫乱剑's +1 attack per
                # held card, and other 手牌-conditional effects). oracle_sim._player
                # passes the field through to NativeFixturePlayer.handCards.
                "handCards": [int(c) for c in self.hand],
                "career": self.career, "tipo": self.tipo, "max_tipo": self.max_tipo,
                "talents": [t + 10000 * max(0, min(3, self.talent_phases.get(t, 0) - 2))
                             for t in self.talents]}

    @property
    def battle_hp(self) -> int:
        """Max HP brought into a battle: realm base + fate extra."""
        return E.max_hp(self.realm, self.extra_hp)


@dataclass
class GameState:
    players: list
    round: int = 0
    rng: random.Random = None

    def alive_players(self):
        return [p for p in self.players if p.alive]


# ── environment ───────────────────────────────────────────────────────────────
class YiXianEnv:
    DAOYUN_ROUNDS = (4, 14)                # 道韵 offers at the START of these rounds

    def __init__(self, n_players: int = 8, characters=None, seed: int = 0,
                 field_bank: "F.FieldBank | None" = None,
                 fate_chooser=None, sidejob_chooser=None, ghost_bank=None,
                 daoyun_chooser=None):
        self.n = n_players
        self.characters = characters or [1000001] * n_players   # STUB: real char roster
        self.rng = random.Random(seed)
        self.state: GameState | None = None
        # Optional LEARNED decision hooks: fate_chooser(env,p,offered)->fate_id and
        # sidejob_chooser(env,p)->career. Default None = the bootstrap heuristics.
        self.fate_chooser = fate_chooser
        self.sidejob_chooser = sidejob_chooser
        # 道韵 chooser(env, p, options)->option: options[0]=0 (自在随心, draw 1
        # now); the rest are card BASE ids (2 phase-4 + 1 phase-5), delivered
        # when the player reaches the card's phase.
        self.daoyun_chooser = daoyun_chooser
        # Field of recently-played boards — the opponent distribution a placement
        # policy scores against. Persisted ACROSS games (pass one in) so it warms
        # up through self-play; a fresh bank cold-starts on the first game.
        self.field = field_bank if field_bank is not None else F.FieldBank()
        # GHOST mode: when set (a FieldBank of REAL recorded boards), each round
        # every player battles a sampled real board instead of each other — the
        # game becomes 8 independent single-agent runs graded against reality.
        self.ghost_bank = ghost_bank

    def reset(self) -> GameState:
        players = []
        for i in range(self.n):
            cid = self.characters[i % len(self.characters)]
            prefix = cid // 1_000_000
            bag = D.DrawBag(D.build_pool(prefix, max_phase=5))
            players.append(PlayerState(pid=i, char_id=cid, sect_prefix=prefix, bag=bag,
                                       rerolls=E.REROLL_START))
        self.state = GameState(players=players, round=0, rng=self.rng)
        for p in players:                          # 天命: each character's INNATE talent
            innate = FA.char_innate(p.char_id)
            if innate:
                FA.apply(self, p, innate, phase=1)
        return self.state

    def pick_fate(self, p: PlayerState, phase: int = 0) -> int:
        """天命: at a breakthrough (to realm 2-5) offer 4 fates — the PHASE's
        character fate (one-per-phase, talent_params field_6) + 3 from this sect +
        general — and pick one, applying its state effects and recording the id
        for the Oracle's combat effect. # STUB (fate policy — learnable)."""
        offered = FA.offer(p.char_id, p.sect_prefix, self.state.rng,
                           exclude=p.talents, phase=phase)
        self._pick_phase = phase        # the CROSSING realm — choosers display
        if self.fate_chooser is not None:   # this phase's version text (game7 bug 2)
            fid = self.fate_chooser(self, p, offered)
        else:
            fid = FA.choose(offered, self.state.rng)
        if fid:
            FA.apply(self, p, fid, phase=phase)
        else:
            p.cultivation += 2                     # declining a 天命 pays 修为
        return fid                                 # (放弃天命; value approximate)

    # ── prep-phase mechanics (the transition rules) ──────────────────────────
    SIDEJOB_PER_DEAL = 1                    # 副职 cards in each round's deal (user-confirmed)

    def deal_round(self, p: PlayerState, first_exchange: bool = True):
        """Deal this round's cards into the player's hand (draws.py sampler). The
        sampler speaks NAMES (pool fidelity); the hand is IDS, so convert here.
        Unresolvable names (e.g. 走火入魔) are dropped. # STUB (dead-card modelling)

        COMPOSITION (user-confirmed): the deal is 门派 cards + exactly ONE 副职 card —
        so R2-11's 3 cards are 2 sect + 1 sidejob, and R12+'s 4 are 3 sect + 1 sidejob
        (the sidejob share stays at 1 as the deal grows). Round 1 predates the 副职
        pick, so all 5 opening cards are sect cards."""
        n = E.deal_count(self.state.round)
        rng = self.state.rng
        side = p.bag.sidejob
        n_side = self.SIDEJOB_PER_DEAL if (p.career and any(
            c > 0 and nm in side for nm, c in p.bag.copies.items())) else 0
        n_side = min(n_side, n)
        dealt = p.bag.deal_subset(n - n_side, p.phase, rng,
                                  lambda nm: nm not in side, boost_first=first_exchange)
        if n_side:
            dealt += p.bag.deal_subset(n_side, p.phase, rng, lambda nm: nm in side)
        ids = C.names_to_ids(dealt)
        p.hand.extend(ids)
        return ids

    def _absorb_gain(self, p: PlayerState):
        """炼化 yield: +1 修为 — except 李㵘's 凡躯 (talent 204): +1 体魄 (capped)."""
        if 204 in p.talents:
            if p.tipo < p.max_tipo:
                p.tipo = min(p.tipo + E.ABSORB_CULT, p.max_tipo)
        else:
            p.cultivation += E.ABSORB_CULT

    def absorb(self, p: PlayerState, cid: int):
        """炼化: consume a hand card (id) for +1 cultivation (no pool effect).
        Cards with a [炼化] clause (小鱼干/猫薄荷/逗猫棒/丹药…) also fire their effect —
        the log line is left on `self.last_absorb_fx` (absorb_fx.py)."""
        import absorb_fx as AF
        self.last_absorb_fx = None
        if cid in p.hand:
            p.hand.remove(cid)                    # leaves hand FIRST so 猫薄荷 can't
            self._absorb_gain(p)                  # upgrade the card being absorbed
            self.last_absorb_fx = AF.fire(self, p, cid)

    def absorb_board(self, p: PlayerState, cid: int) -> bool:
        """炼化 a card OFF THE BOARD (the breakthrough-push move: eat board cards
        for the cultivation to cross a realm gate; fate grants then refill)."""
        import absorb_fx as AF
        self.last_absorb_fx = None
        for i, c in enumerate(p.board):
            if c == cid:
                p.board[i] = 0
                self._absorb_gain(p)
                self.last_absorb_fx = AF.fire(self, p, cid)
                return True
        return False

    FREE_ROLL_FATE = 18                     # 云雾变幻 (牧逸风 innate): 每轮首次换牌不消耗换牌机会
    CURIOSITY_FATE = 129                    # 好奇心 (林小月 innate): last charge → 随机惊喜 +1 charge
    CAT_SOUL_FATE = 45                      # 猫魂庇佑 (林小月): even 命元 loss is halved

    def reroll(self, p: PlayerState, cid: int):
        """换牌: spend a charge to discard a hand card (id) and draw a replacement.
        云雾变幻 makes the FIRST exchange each round free (no charge consumed) —
        modelled exactly, not as a +1 charge (which inflated the visible bank).
        Pool burn is name-keyed (sect 3 / sidejob 2), so bridge id↔name here.

        Two exchange-time mechanics ride along (exchange_fx.py):
        · [置换] cards (练笔/以画入道/触类旁通/妙笔生花/…): their effect fires and the
          card is NOT burned from the pool (FAQ).
        · 好奇心: spending the LAST charge exchanges into a RANDOM card (created from
          nothing) and refunds the charge, up to 9 times.
        The fired effect's log line is left on `self.last_exchange_fx`."""
        import exchange_fx as XF
        self.last_exchange_fx = None
        free = (self.FREE_ROLL_FATE in p.talents and not p.free_roll_used)
        if (p.rerolls <= 0 and not free) or cid not in p.hand:
            return None
        if free:
            p.free_roll_used = True
        else:
            p.rerolls -= 1
        p.hand.remove(cid)
        # ORDER (user-confirmed, review of game1 move 41): the [置换] effect resolves
        # FIRST — so rolling 练笔/触类旁通 on the last charge refills 换牌 and 好奇心
        # does NOT trigger (a normal card is drawn instead).
        fx = XF.effect_for(cid)                       # [置换] card → no pool burn
        fx_granted = False
        if fx is not None:
            before_fx = len(p.hand)
            self.last_exchange_fx = fx(self, p)       # 置换 effect (may grant cards/charges)
            # user ruling (game3 review): a card-granting [置换] (以画入道/触类旁通/
            # 妙笔生花/…) grants IN PLACE of the normal replacement — no extra draw,
            # no pool change, no cult. Charge-only ones (练笔) still draw normally.
            fx_granted = len(p.hand) > before_fx
        curious = (self.CURIOSITY_FATE in p.talents and not free and p.rerolls == 0
                   and not fx_granted)
        repl_id = None
        if fx_granted:
            return p.hand[-1]                         # the granted card IS the replacement
        if curious:
            # 换到随机惊喜: the replacement is a surprise card from nothing (the
            # discarded card still burns unless it has an exchange effect).
            if fx is None and C.id_to_name(cid) in p.bag.copies:
                burn = 2 if C.id_to_name(cid) in p.bag.sidejob else 3
                nmc = C.id_to_name(cid)
                p.bag.copies[nmc] = max(0, p.bag.copies[nmc] - burn)
            before = len(p.hand)
            got, fired = XF.curiosity_surprise(self, p)
            if fired and len(p.hand) > before:
                repl_id = p.hand[-1]
                note = f"好奇心: 随机惊喜 {got}, 换牌机会+1"
                self.last_exchange_fx = (self.last_exchange_fx + " · " + note
                                         if self.last_exchange_fx else note)
            else:
                curious = False
        if not curious:
            repl_name = p.bag.reroll(C.id_to_name(cid), p.phase, self.state.rng,
                                     no_penalty=fx is not None)
            repl_id = C.name_to_base_id(repl_name)
            if repl_id:
                p.hand.append(repl_id)
        return repl_id

    def _card_phase(self, p: PlayerState, cid: int) -> int:
        return p.bag.phase.get(C.id_to_name(cid), 1)

    def try_breakthrough(self, p: PlayerState) -> bool:
        """Advance to the highest realm the current cultivation qualifies for
        (base-HP jump + higher-phase cards unlock). Greedy catch-up — banked
        cultivation can clear more than one realm; the policy can override later."""
        target = E.realm_for_cultivation(p.cultivation)
        if target > p.realm:
            first = p.realm + 1
            p.realm = target
            import fate_fx
            for r in range(first, target + 1):     # one 天命 offer per realm crossed,
                fate_fx.on_breakthrough(self, p)   # each with ITS phase's char fate
                self.pick_fate(p, phase=r)
            self._grant_daoyun(p)                  # 道韵 cards deliver on phase-up
            return True
        return False

    # ── 道韵 (dao omen): offers at rounds 4 and 14 ────────────────────────────
    def select_daoyun(self, p: PlayerState):
        """Offer 4 options: 自在随心 (option 0 — draw 1 card NOW) + 2 random
        phase-4 pool cards + 1 phase-5 pool card. A card pick is DELIVERED the
        moment the player reaches that card's phase (user-described mechanic)."""
        def pool_cards(ph, n):
            names = [nm for nm, v in p.bag.phase.items()
                     if v == ph and p.bag.copies.get(nm, 0) > 0]
            self.state.rng.shuffle(names)
            out = []
            for nm in names:
                cid = C.name_to_base_id(nm)
                if cid:
                    out.append((cid, ph))
                if len(out) >= n:
                    break
            return out
        cards = pool_cards(4, 2) + pool_cards(5, 1)
        opts = [0] + [cid for cid, _ph in cards]
        phase_of = {cid: ph for cid, ph in cards}
        pick = 0
        if self.daoyun_chooser is not None:
            pick = int(self.daoyun_chooser(self, p, opts) or 0)
        if pick and pick in phase_of:
            p.pending_grants.append((phase_of[pick], pick))
            self._grant_daoyun(p)                  # already at that phase → now
        else:
            pick = 0
            dealt = p.bag.deal(1, p.phase, self.state.rng, first_exchange=False)
            p.hand.extend(C.names_to_ids(dealt))   # 自在随心: draw 1 immediately
        self.last_daoyun.append((p.pid, pick))
        return pick

    def _grant_daoyun(self, p: PlayerState):
        for ph, cid in list(p.pending_grants):
            if p.realm >= ph:
                p.hand.append(cid)
                p.pending_grants.remove((ph, cid))

    def select_sidejob(self, p: PlayerState):
        """副职: at round 2 the player picks ONE of the 7 sidejobs, adding that
        career's cards to their draw pool. WHICH sidejob is a strategic choice
        (synergy with sect/build) — random bootstrap here. # STUB (sidejob policy)."""
        if p.career:
            return
        if self.sidejob_chooser is not None:
            p.career = int(self.sidejob_chooser(self, p))
        else:
            p.career = self.state.rng.randint(1, 7)
        p.bag.add_cards(D.sidejob_pool(p.career), as_sidejob=True)

    def refresh_slots_rerolls(self, p: PlayerState):
        p.unlocked = E.unlocked_slots(self.state.round)
        # 换牌 charges granted per round: +3 (R1-9), +4 (R10-12), +6 (R13+).
        # Banking caps at 25 (user rule): the grant tops up to 25 at most; a
        # player at/above 25 gets nothing until they spend below the cap.
        # In-round gains ([置换], 天命 hooks) may exceed 25 freely.
        if p.rerolls < E.REROLL_CAP:
            p.rerolls = min(p.rerolls + E.reroll_grant(self.state.round),
                            E.REROLL_CAP)
        p.free_roll_used = False                # 云雾变幻's freebie resets per round

    # ── battle ───────────────────────────────────────────────────────────────
    def acts_first(self, a: PlayerState, b: PlayerState) -> bool:
        """Turn order (user-confirmed rule): the HIGHER-cultivation side acts
        first (e.g. taking 稳固根基's 修为−1 can cost you the first move); ties
        break by coin flip."""
        if a.cultivation != b.cultivation:
            return a.cultivation > b.cultivation
        return self.state.rng.random() < 0.5

    def resolve_pairing(self, a: PlayerState, b: PlayerState):
        """Battle a vs b via the Oracle (exact) if available, else a placeholder.
        `a` is the FIRST MOVER (p1 in the engine) — callers order the pair via
        acts_first. Returns (margin_a, hp_a): margin = signed 命 damage (can be
        0 — mitigation), hp = signed remaining-HP edge. TIES DON'T EXIST (user;
        real data: every round has a winerId): the winner is by 命 margin, else
        by HP edge, else coin — hp carries the tiebreak."""
        try:
            import sys
            from pathlib import Path
            root = Path(__file__).resolve().parent.parent
            for pth in (str(root / "proxy"), str(root)):
                if pth not in sys.path:
                    sys.path.insert(0, pth)
            import oracle_sim
            if oracle_sim.available():
                unlocked = E.unlocked_slots(self.state.round)
                r = oracle_sim.matchup(a.to_fixture(unlocked), b.to_fixture(unlocked),
                                       rnd=self.state.round)   # carries 体魄 + 天命 talents
                life = float(r.get("lifeDamage", 0) or 0)
                hp = float(r.get("hpDelta", 0) or 0)
                if hp == 0 and life == 0:
                    hp = 1.0 if self.state.rng.random() < 0.5 else -1.0
                return life, hp
        except Exception:
            pass
        # Placeholder (no Oracle): compare non-empty board sizes + a little noise.
        m = (sum(1 for c in a.board if c) - sum(1 for c in b.board if c)
             + self.state.rng.uniform(-0.5, 0.5))
        return m, m

    def apply_battle(self, a: PlayerState, b: PlayerState, margin_a: float,
                     hp_a: float = 0.0):
        """Destiny (命) transfer from a battle. MINED (recentBattleDatas, 181
        games): the round LOSER drops by |net| = |lifeDamage margin|; the winner's
        命 holds. Fits ~56% exactly / ~87% within {net, min(0,net)}; the ~13%
        residual is secondary 命 sources (fate/card/breakthrough) — an accepted
        approximation since the reward is ORDINAL placement and combat is exact.
        A 0-命 round still has a WINNER (hp_a tiebreak) — it just costs nothing."""
        loser = (b if margin_a > 0 else a) if abs(margin_a) >= 0.5 else \
                (b if hp_a > 0 else a)
        loss = int(round(abs(margin_a)))
        if loss <= 0:
            # TURN CAP (engine reports lifeDamage 0 with both alive): the lower-HP
            # side still LOSES and pays per the official 命元伤害 formula on the
            # final HP difference (user ruling — no more free all-DEF stalling).
            loss = E.destiny_damage(self.state.round, abs(hp_a))
        if loss <= 0:
            return                                  # can't happen post-formula; safety
        # 慈念曲 (5000006, [持续] non-stacking): 败者所受[命元]伤害减 4/6/8 by level,
        # floor 1 — applies whichever SIDE fielded it (game5 finding). Reduction
        # first, then 猫魂庇佑 parity (halving reads the damage actually received).
        red = 0
        for q in (a, b):
            for cid in q.board:
                if cid and cid - 10000 * ((cid // 10000) % 100) == 5000006:
                    red = max(red, 4 + 2 * ((cid // 10000) % 100))
        if red:
            loss = max(1, loss - red)
        if self.CAT_SOUL_FATE in loser.talents and loss % 2 == 0:
            loss //= 2                              # 猫魂庇佑 (林小月): 战败受到的[命元]
        loser.destiny -= loss                       # 伤害为偶数时，伤害减半
        if loser.destiny <= 0:
            loser.destiny = 0
            loser.alive = False

    # ── one full round ───────────────────────────────────────────────────────
    def play_round(self, policy):
        """Advance one round: deal → policy acts (economy + board) → pair → battle.
        `policy(env, player)` mutates the player (absorb/reroll/board/breakthrough).
        Pairing (mined, 181 games): random among the living, AVOIDING the
        immediate-previous opponent when possible (consecutive repeats are only
        ~7% in real games); repeats grow naturally as the field shrinks."""
        self.state.round += 1
        alive = self.state.alive_players()
        # Snapshot every player's fixture AS THE ROUND OPENS (= their last fielded
        # board). Policies run sequentially, so without this a later-acting player
        # would "see" an earlier player's already-rebuilt board — in the real game
        # you know the opponent's LAST board, not their new one. Opponent-aware
        # placement scores against these snapshots.
        unlocked0 = E.unlocked_slots(self.state.round)
        self.round_open_fixtures = {p.pid: p.to_fixture(unlocked0) for p in alive}
        if self.state.round == E.SIDEJOB_ROUND:
            for p in alive:
                self.select_sidejob(p)
        self.last_daoyun = []
        if self.state.round in self.DAOYUN_ROUNDS:  # 道韵 at the START of R4/R14
            for p in alive:
                self.select_daoyun(p)
        import fate_fx
        for p in alive:
            p.cultivation += E.passive_cult(self.state.round)   # ramped, 0 at R1
            p.extra_hp += E.passive_hp(self.state.round)        # +2 max HP per round (all players)
            fate_fx.on_round_start(self, p)     # per-round fate passives (e.g. 五行润养)
            self.refresh_slots_rerolls(p)
            self.deal_round(p, first_exchange=True)
            policy(self, p)                     # prep decisions incl. breakthrough
            # Cards left unplaced/unabsorbed don't hoard indefinitely — keep the
            # hand bounded (keeps state finite + search cheap). Exact carry/discard
            # rule between rounds is unconfirmed. # STUB (hand-carry)
            if len(p.hand) > HAND_LIMIT:
                p.hand = p.hand[-HAND_LIMIT:]
        self.last_round_battles = []
        if self.ghost_bank is not None:
            self._ghost_battles(alive)
        else:
            for a, b in self._pair(alive):
                if not self.acts_first(a, b):       # a = first mover (higher 修为)
                    a, b = b, a
                margin, hpm = self.resolve_pairing(a, b)
                self.apply_battle(a, b, margin, hpm)
                a_won = margin > 0.5 or (abs(margin) < 0.5 and hpm > 0)
                self.last_round_battles.append({
                    "a": a.pid, "b": b.pid, "margin": margin, "hp_margin": hpm,
                    "a_won": a_won,
                    "a_board": [c for c in a.board if c], "b_board": [c for c in b.board if c],
                    "a_hp": a.battle_hp, "b_hp": b.battle_hp,
                    "a_cult": a.cultivation, "b_cult": b.cultivation,
                    "a_tipo": a.tipo, "b_tipo": b.tipo})
                fate_fx.on_battle_end(self, a, a_won, margin)   # per-battle fate triggers
                fate_fx.on_battle_end(self, b, not a_won, -margin)
                a.last_opp, b.last_opp = b.pid, a.pid
        # 体魄: body-cultivation cards on the board accrue physique this battle,
        # carrying into the next (the Oracle used the pre-battle 体魄; the gain
        # persists). Feed the field AFTER so opponent samples reflect it.
        unlocked = E.unlocked_slots(self.state.round)
        for p in alive:
            if any(p.board):
                B.accrue(p, [c for c in p.board if c])
                if self.ghost_bank is None:        # ghost mode: field = REAL boards,
                    self.field.add(self.state.round, p.to_fixture(unlocked))   # keep pristine

    def _ghost_battles(self, alive):
        """GHOST mode: each alive player fights a REAL board sampled from
        ghost_bank at this round (batched through the Oracle pool). Only the
        player's destiny moves — a ghost is a snapshot, not a participant. A win
        also grants the winner's margin as destiny gain? No — matching apply_battle:
        the loser drops |margin|, a winner just holds (destiny gain sources are
        secondary and unmodelled)."""
        import fate_fx
        import oracle_sim
        unlocked = E.unlocked_slots(self.state.round)
        ghosts = [self.ghost_bank.sample(self.state.round, 1, self.state.rng)[0]
                  for _ in alive]
        pairs, flipped = [], []
        for p, g in zip(alive, ghosts):             # first mover = higher 修为
            me = p.to_fixture(unlocked)
            ghost_first = (g.get("exp", 0) > p.cultivation or
                           (g.get("exp", 0) == p.cultivation and
                            self.state.rng.random() < 0.5))
            pairs.append((g, me) if ghost_first else (me, g))
            flipped.append(ghost_first)
        try:
            results = oracle_sim.batch_matchup(pairs, rnd=self.state.round)
        except Exception:
            results = [None] * len(pairs)
        for p, g, r, fl in zip(alive, ghosts, results, flipped):
            margin = float((r or {}).get("lifeDamage", 0) or 0)
            hpm = float((r or {}).get("hpDelta", 0) or 0)
            if fl:
                margin, hpm = -margin, -hpm         # back to the player's perspective
            if hpm == 0 and margin == 0:
                hpm = 1.0 if self.state.rng.random() < 0.5 else -1.0
            won = margin > 0.5 or (abs(margin) < 0.5 and hpm > 0)
            if margin < -0.5:                       # player lost: drop |margin| 命
                p.destiny -= int(round(abs(margin)))
                if p.destiny <= 0:
                    p.destiny, p.alive = 0, False
            self.last_round_battles.append({
                "a": p.pid, "b": -1, "margin": margin, "hp_margin": hpm,
                "a_won": won,
                "a_board": [c for c in p.board if c], "b_board": list(g["usedCards"]),
                "a_hp": p.battle_hp, "b_hp": 0,
                "a_cult": p.cultivation, "b_cult": g.get("exp", 0),
                "a_tipo": p.tipo, "b_tipo": g.get("tipo", 0)})
            fate_fx.on_battle_end(self, p, won, margin)

    def _pair(self, alive):
        """Yield (a, b) pairs: shuffle, then greedily match avoiding each player's
        immediate-previous opponent where the remaining pool allows."""
        pool = list(alive)
        self.rng.shuffle(pool)
        pairs = []
        while len(pool) >= 2:
            a = pool.pop(0)
            # prefer an opponent that isn't a's last, if one exists
            j = next((k for k, b in enumerate(pool) if b.pid != a.last_opp), 0)
            b = pool.pop(j)
            pairs.append((a, b))
        return pairs

    def play_game(self, policy, max_rounds: int = 20):
        """Run to a winner (or max_rounds). Returns placement order (pid list,
        1st→last) by elimination order + final destiny."""
        self.reset()
        elim_order = []
        prev_alive = set(p.pid for p in self.state.alive_players())
        for _ in range(max_rounds):
            if len(self.state.alive_players()) <= 1:
                break
            self.play_round(policy)
            now = set(p.pid for p in self.state.alive_players())
            for pid in (prev_alive - now):
                elim_order.append(pid)
            prev_alive = now
        survivors = sorted(self.state.alive_players(), key=lambda p: -p.destiny)
        placement = [p.pid for p in survivors] + list(reversed(elim_order))
        return placement


# ── shared economy (bootstrap heuristic; the RL policy will replace this) ────
def reroll_weak(env: "YiXianEnv", p: PlayerState, budget: int = 2):
    """换牌: spend up to `budget` charges fishing away OUTDATED chaff — cards below
    the current realm's tier that aren't merge candidates — to draw current-tier
    cards for the board search. A bootstrap heuristic; reroll STRATEGY (which/when)
    is a learnable decision like the economy. # STUB (reroll policy)."""
    from collections import Counter
    budget = min(budget, p.rerolls)
    if budget <= 0 or not p.hand:
        return
    board = [c for c in p.board if c]
    cnt = Counter(p.hand)
    cands = [c for c in set(p.hand)
             if c not in board and cnt[c] < 2 and env._card_phase(p, c) < p.realm]
    cands.sort(key=lambda c: env._card_phase(p, c))     # worst (lowest tier) first
    for c in cands[:budget]:
        env.reroll(p, c)


def absorb_leftovers(env: "YiXianEnv", p: PlayerState, reserve: int = 0):
    """Absorb (炼化) hand cards the board didn't take → +cultivation toward
    breakthroughs. Keeps `reserve` cards in hand (0 = absorb everything unplaced).
    This is the ONLY cultivation source modelled, so it's what drives realms; a
    fixed heuristic here isolates PLACEMENT as the only difference between policies
    until the learned economy lands. # STUB (economy = the learnable core)."""
    leftover = list(p.hand)[reserve:] if reserve else list(p.hand)
    for nm in leftover:                   # absorb every round incl. R1 (confirmed
        env.absorb(p, nm)                 # accounting: R1 full board = 2 cult)


# ── a trivial policy for the skeleton smoke test ────────────────────────────
def greedy_policy(env: "YiXianEnv", p: PlayerState):
    """Baseline: keep the board you already have (it persists across rounds) and
    top it up from hand — in hand order — to the unlocked slot count, playing REAL
    card ids so the Oracle battle is exact. Placed cards leave the hand.

    This is deliberately un-clever: WHICH cards and in WHAT order (sequencing
    matters) is exactly the decision the learned policy / oracle_sim placement
    search will own. Board legality (≤2 消耗 / ≤2 持续) and merges are not yet
    enforced here. # STUB (policy quality)"""
    slots = E.unlocked_slots(env.state.round)
    placed = [c for c in p.board if c]            # persists across rounds
    need = slots - len(placed)
    if need > 0 and p.hand:
        take = p.hand[:need + 1]                    # +1 so a duplicate pair can merge
        for cid in take:
            p.hand.remove(cid)
        placed += take
    merged = M.apply_merges(placed)                  # merge duplicate pairs
    while len(merged) > slots and placed:            # over-full: the extra didn't
        p.hand.append(placed.pop())                  # merge — back to hand (absorbed
        merged = M.apply_merges(placed)              # below), never silently dropped
    p.cultivation += (len(placed) - len(merged)) * E.MERGE_CULT   # +1 cult per merge
    p.board = merged + [0] * (8 - len(merged))
    absorb_leftovers(env, p)                        # cultivation from unplaced cards
    env.try_breakthrough(p)                         # break greedily when able


def decision_state(env: "YiXianEnv", p: PlayerState) -> dict:
    """The pre-placement state (what the policy net sees to pick cards)."""
    slots = E.unlocked_slots(env.state.round)
    return {"round": env.state.round, "realm": p.realm, "cultivation": p.cultivation,
            "destiny": p.destiny, "unlocked": slots,
            "alive": len(env.state.alive_players()), "extra_hp": p.extra_hp,
            "tipo": p.tipo, "max_tipo": p.max_tipo, "rerolls": p.rerolls,
            "char_id": p.char_id, "career": p.career, "talents": list(p.talents),
            "board": [c for c in p.board if c], "hand_ids": list(p.hand)}


def learned_board(env: "YiXianEnv", p: PlayerState, place_net, slots: int) -> tuple:
    """Pick the board with the POLICY NET (no Oracle search): score every available
    card, greedily take the highest-scored while keeping the board legal (≤2 消耗 /
    ≤2 持续) until `slots` filled (after merges). Returns (merged_board, raw_used)."""
    import policy_net as PN
    import oracle_sim as O
    board_ids = [c for c in p.board if c]
    avail = board_ids + list(p.hand)
    if not avail:
        return [], []
    scores = PN.score_cards(place_net, decision_state(env, p), avail)
    order = sorted(range(len(avail)), key=lambda i: -scores[i])
    caps = (2, 2, 2)          # strict: 消耗/持续 COMBINED ≤2 (no self-calibration
                              # from our own board — a bug would ratchet the cap)
    picked = []
    for i in order:
        trial = M.apply_merges(picked + [avail[i]])
        if caps is None or O._concon_ok(trial, caps):
            picked.append(avail[i])
        if len(M.apply_merges(picked)) >= slots:
            break
    return M.apply_merges(picked)[:slots], picked


def make_field_policy(k: int = 8, cap: int = 16, window: int = 1, order: bool = False,
                      scorer=None, pol_record=None, place_net=None):
    """Placement policy. Default: play the BEST board vs a `k`-sample of the field
    (placement.best_board, Oracle search; order=True also optimises sequence).

    place_net (a policy_net.CardPolicyNet): use the LEARNED policy to pick cards in
    one forward pass instead of the search — this is the trained board policy.
    pol_record (a list): while using the SEARCH, append each decision
    {state, available, chosen} to imitation-train the policy net on."""
    def policy(env: "YiXianEnv", p: PlayerState):
        slots = E.unlocked_slots(env.state.round)
        reroll_weak(env, p)                             # fish chaff before placing
        board_ids = [c for c in p.board if c]
        if pol_record is not None:                      # capture the decision context
            decision = {"pid": p.pid, "state": decision_state(env, p),
                        "available": board_ids + list(p.hand)}
        if place_net is not None:                       # learned policy (fast, no search)
            board, raw_used = learned_board(env, p, place_net, slots)
        else:                                           # Oracle search (the expert)
            me = p.to_fixture(slots)
            opps = env.field.sample(env.state.round, k, env.state.rng, window=window)
            out = P.best_board(me, board_ids, p.hand, slots,
                               opps, rnd=env.state.round, cap=cap, order=order, scorer=scorer)
            board, raw_used = out["board"], out["raw_used"]
        if pol_record is not None:                      # record the chosen cards (either path)
            decision["chosen"] = list(raw_used)
            pol_record.append(decision)
        p.board = board + [0] * (8 - len(board))
        p.cultivation += M.merge_gain(raw_used) * E.MERGE_CULT   # +1 cult per merge
        consumed = list(raw_used)                       # consume hand cards played
        for c in board_ids:
            if c in consumed:
                consumed.remove(c)
        for cid in consumed:
            if cid in p.hand:
                p.hand.remove(cid)
        displaced = list(board_ids)                 # dropped board cards → hand
        for c in raw_used:                          # (nothing vanishes; absorbed
            if c in displaced:                      # below like any leftover)
                displaced.remove(c)
        p.hand.extend(displaced)
        absorb_leftovers(env, p)                    # cultivation from unplaced cards
        env.try_breakthrough(p)                     # break greedily when able
    return policy


if __name__ == "__main__":
    env = YiXianEnv(n_players=8, seed=7)
    placement = env.play_game(greedy_policy, max_rounds=20)
    st = env.state
    print(f"game ran {st.round} rounds; survivors "
          f"{[p.pid for p in st.alive_players()]}")
    print("placement (1st→last):", placement)
    print("sample player after game:",
          f"pid0 realm={st.players[0].realm} cult={st.players[0].cultivation} "
          f"destiny={st.players[0].destiny} hand={len(st.players[0].hand)}")
