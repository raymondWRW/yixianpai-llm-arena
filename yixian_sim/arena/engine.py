# -*- coding: utf-8 -*-
"""Arena engine — a 4-player YiXianPai game where every seat is an LLM bot.

Economy (deals, rolls, merges, absorbs, breakthroughs, fates, sidejobs) runs on
the existing selfplay env; combat resolves through yisim (see yisim_bridge),
whose full turn logs are also what the bots use to reason.

Seats (fixed, user spec): 牧逸风(1000001) 谭舒雁(2000001) 吾行之(3000001) 小布(4000001).
Bots choose their own sidejob at round 2. Standard info rules apply: a bot sees
its own private state and every opponent's LAST-round public state only.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for p in (str(_HERE.parent / "selfplay"), str(_HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import cards as C
import economy as E
import env as EV
import fates as FA
import field as F
import fate_fx
import fate_map as FM
import yisim_bridge as YB

CHARS = [1000001, 2000001, 3000001, 4000001]
NAMES = {1000001: "牧逸风", 2000001: "谭舒雁", 3000001: "吾行之", 4000001: "小布"}
# There is NO round cap in the real game (user ruling 2026-09-27): play
# continues until one player is left. This is only a runaway-cost guard for
# harness bugs — hitting it voids the game (no winner scored), it never ends a
# game "normally". Termination is guaranteed anyway: every battle's loser
# loses >= 1 命, growing with the round.
SAFETY_ROUND_LIMIT = 60


def nm(cid):
    lv = 0
    try:
        import merge as M
        lv = M.card_level(cid) - 1
    except Exception:
        pass
    n = C.id_to_name(cid) or str(cid)
    return n + (f"+{lv}" if lv > 0 else "")


class ArenaGame:
    def __init__(self, seed: int = 1):
        self.env = EV.YiXianEnv(n_players=4, characters=CHARS, seed=seed,
                                field_bank=F.FieldBank(),
                                fate_chooser=self._fate_chooser,
                                sidejob_chooser=self._sidejob_chooser,
                                daoyun_chooser=self._daoyun_chooser)
        self.env.reset()
        self.seed = seed
        self.log_lines = []
        self.round_open = {}          # pid -> public snapshot at round open (fog)
        self.fate_rankings = {}       # pid -> [fate ids] current preference ranking
        self.daoyun_rankings = {}     # pid -> [card ids]
        self.sidejobs = {}            # pid -> career int (chosen at R2)
        self.battle_results = []      # per round list
        self.pairings = []            # this round's announced matchups [(a,b)]
        self.ghost_pair = None        # (solo_pid, ghost_source_pid) or None
        self.hand_history = {}        # rnd -> {pid: [names]} at battle time
        self.deal_history = {}        # rnd -> {pid: [names]} dealt that round
        self.action_history = {}      # rnd -> {pid: [action strings]}
        self.rr_history = {}          # rnd -> {pid: rerolls at round end}
        self.consumed_avatars = {i: set() for i in range(4)}   # used 化身 saves
        self.absorb_counts = {i: 0 for i in range(4)}          # 勤学苦练 (29)
        self.destiny_paid = {i: 0 for i in range(4)}           # 磨砺不止 (151)
        for q in self.env.state.players:
            q.max_tipo = max(q.max_tipo, 6)   # base 体魄上限 6 (recordings)

    # ── choosers routed to bot decisions ────────────────────────────────────
    def _fate_chooser(self, env, p, offered):
        ph = getattr(env, "_pick_phase", 0) or p.realm
        for f in self.fate_rankings.get(p.pid, []):
            if f in offered:
                self.log(f"  pid{p.pid} 天命@境{ph} picked {f}:{FA.name(f)} "
                         f"from {[(x, FA.name(x)) for x in offered]}")
                return f
        f = FA.choose(offered, env.state.rng)
        self.log(f"  pid{p.pid} 天命@境{ph} default {f}:{FA.name(f)} "
                 f"from {[(x, FA.name(x)) for x in offered]}")
        return f

    def _sidejob_chooser(self, env, p):
        return self.sidejobs.get(p.pid, 0) or env.state.rng.randint(1, 7)

    def _daoyun_chooser(self, env, p, opts):
        for o in self.daoyun_rankings.get(p.pid, []):
            if o in opts:
                return o
        return 0

    def log(self, msg):
        self.log_lines.append(msg)
        print(msg, flush=True)

    # ── round flow ───────────────────────────────────────────────────────────
    def begin_round(self):
        env = self.env
        env.state.round += 1
        alive = env.state.alive_players()
        # fog snapshot: last-round public state (board as last fielded)
        self.round_open = {p.pid: self.public_state(p) for p in env.state.players}
        env.last_daoyun = []
        if env.state.round in env.DAOYUN_ROUNDS:
            for p in alive:
                env.select_daoyun(p)
        for p in alive:
            if env.state.round >= 2:
                p.max_tipo += 5          # 保留上限: starts 6, +5 per round (user rule)
            # NOTE: sidejob is chosen by the BOT via choose_sidejob during its
            # R2 turn (which adds that career's pool); no env auto-pick here —
            # the old auto-pick added a RANDOM career's cards (game1-4 bug).
            p.cultivation += E.passive_cult(env.state.round)
            p.extra_hp += E.passive_hp(env.state.round)
            fate_fx.on_round_start(env, p)
            env.refresh_slots_rerolls(p)
            dealt = env.deal_round(p, first_exchange=True)
            self.deal_history.setdefault(env.state.round, {})[p.pid] = \
                [nm(c) for c in dealt]
            self.log(f"R{env.state.round} pid{p.pid} dealt: {', '.join(nm(c) for c in dealt)}")
        # Matchups are decided AND revealed at round start (user rule
        # 2026-09-17): every player knows who they fight this round. With an
        # odd count alive, the unpaired player fights a GHOST — a copy of a
        # random opponent's board; only the ghost-fighter risks 命 there.
        pairs = list(env._pair(alive))
        self.pairings = [(a.pid, b.pid) for a, b in pairs]
        paired = {pid for ab in self.pairings for pid in ab}
        self.ghost_pair = None
        odd = [q for q in alive if q.pid not in paired]
        if odd and len(alive) > 1:
            solo = odd[0]
            others = [q for q in alive if q.pid != solo.pid]
            self.ghost_pair = (solo.pid, env.state.rng.choice(others).pid)
        msg = "; ".join(f"pid{a} vs pid{b}" for a, b in self.pairings)
        if self.ghost_pair:
            msg += ("; " if msg else "") + \
                   f"pid{self.ghost_pair[0]} vs pid{self.ghost_pair[1]}(ghost)"
        self.log(f"R{env.state.round} matchups: {msg}")

    def public_state(self, p) -> dict:
        return {"pid": p.pid, "name": NAMES.get(p.char_id, str(p.char_id)),
                "alive": p.alive, "destiny": p.destiny, "realm": p.realm,
                "cultivation": p.cultivation, "max_hp": p.battle_hp,
                "career": p.career, "physique": p.tipo, "max_physique": p.max_tipo,
                "board": [nm(c) for c in p.board if c],
                "board_ids": [c for c in p.board if c],
                "talents": [FA.name(t) for t in p.talents],
                "talent_ids": list(p.talents),
                "talent_phases": dict(getattr(p, "talent_phases", {}) or {})}

    def finish_round(self):
        """Pair and fight via yisim; apply destiny; return battle summaries."""
        env = self.env
        rnd = env.state.round
        self.hand_history[rnd] = {}
        for q in env.state.alive_players():
            hand = [nm(c) for c in q.hand]
            self.hand_history[rnd][q.pid] = hand
            self.log(f"R{rnd} pid{q.pid} hand: {', '.join(hand) or '(empty)'}")
        if env.state.round == E.SIDEJOB_ROUND:
            for q in env.state.alive_players():
                if not q.career:            # bot never chose: random fallback
                    env.select_sidejob(q)
                    self.sidejobs[q.pid] = q.career
                    self.log(f"  pid{q.pid} did not choose a sidejob — "
                             f"random fallback -> {q.career}")
        results = []
        by_pid = {q.pid: q for q in env.state.players}
        # fight the matchups announced at round start
        for a_pid, b_pid in self.pairings:
            results.append(self._battle(by_pid[a_pid], by_pid[b_pid],
                                        extra_for=None))
        if self.ghost_pair:
            solo, ghost = self.ghost_pair
            results.append(self._battle(by_pid[solo], by_pid[ghost],
                                        extra_for=by_pid[solo]))
        self.battle_results.append(results)
        self.rr_history[env.state.round] = \
            {q.pid: q.rerolls for q in env.state.alive_players()}
        for q in env.state.players:
            if q.alive and q.destiny <= 0:
                q.destiny = 0
                q.alive = False
                self.log(f"  pid{q.pid} {NAMES.get(q.char_id)} ELIMINATED")
        return results

    def _payload(self, p):
        extra = FM.combat_fields(p.talents,
                                 getattr(p, "talent_phases", {}) or {},
                                 self.consumed_avatars.get(p.pid, ()))
        return YB.player_payload(p.char_id, p.cultivation, p.battle_hp, p.destiny,
                                 [c for c in p.board if c],
                                 physique=p.tipo, max_physique=p.max_tipo,
                                 round_number=self.env.state.round, extra=extra)

    def _battle(self, a, b, extra_for=None):
        env = self.env
        # higher cultivation acts first; ties coin-flip (house rule)
        if b.cultivation > a.cultivation or (b.cultivation == a.cultivation
                                             and env.state.rng.random() < 0.5):
            a, b = b, a
        r = YB.run_battle(self._payload(a), self._payload(b), a_first=True)
        loser = a if r["loser"] == "a" else (b if r["loser"] == "b" else None)
        winner = b if loser is a else (a if loser is b else None)
        loss = r["destiny_loss"]
        applied = False
        if loser is not None and loss > 0:
            if extra_for is None or loser.pid == extra_for.pid:
                before = loser.destiny
                # adopt yisim's post-battle destiny: it applies 化身 saves,
                # 慈念曲, 猫魂庇佑, 生之焰 internally
                after = r["destiny_after"]
                if after is None:
                    after = before - loss
                loser.destiny = max(0, after)
                applied = True
                paid = before - loser.destiny
                # a 化身 keep-1-命 save fired? consume it + its economy cost.
                # yisim reports the CLIPPED loss (= before-1) when it prevents
                # exhaustion, so landing on exactly 1 with an avatar held is
                # treated as consumption (rare false positive accepted).
                if loser.destiny == 1 and before > 1 and loss >= before - 1:
                    for fid, cost in ((7, 0), (65, 1), (83, 5), (154, 0)):
                        if fid in loser.talents and \
                                fid not in self.consumed_avatars[loser.pid]:
                            self.consumed_avatars[loser.pid].add(fid)
                            loser.cultivation = max(0, loser.cultivation - cost)
                            if fid == 154:   # 生机不灭: permanent +4 HP/体魄上限
                                loser.extra_hp += 4
                                loser.max_tipo += 4
                            self.log(f"  pid{loser.pid} 化身 {FA.name(fid)} consumed"
                                     f" (kept 1 命, cost {cost} 修为)")
                            break
                # engine-hook fates on the loser
                self.destiny_paid[loser.pid] += paid
                if 151 in loser.talents:    # 磨砺不止: +1 roll per 7 命 lost
                    gained = (self.destiny_paid[loser.pid] // 7) - \
                             ((self.destiny_paid[loser.pid] - paid) // 7)
                    if gained:
                        loser.rerolls += gained
                if 72 in loser.talents:      # 易数化劫: loss -> +1 roll
                    loser.rerolls += 1
                if 175 in loser.talents:     # 历战不屈: loss -> +1 max HP
                    loser.extra_hp += 1
        if winner is not None and loser is not None and applied:
            fate_fx.on_battle_end(self.env, winner, True, loss)
            fate_fx.on_battle_end(self.env, loser, False, -loss)
        fp = r.get("final_physique") or {}
        for side, q in (("a", a), ("b", b)):
            v = fp.get(side)
            if v is not None:            # 跨回合保留: keep physique up to the cap
                q.tipo = max(0, min(int(v), q.max_tipo))
        a.last_opp, b.last_opp = b.pid, a.pid
        tag = f" [extra for pid{extra_for.pid}]" if extra_for is not None else ""
        log_h = YB.humanize_log(r["log"],
                                f"{NAMES.get(a.char_id)}(pid{a.pid})",
                                f"{NAMES.get(b.char_id)}(pid{b.pid})")
        summary = {"round": env.state.round, "a": a.pid, "b": b.pid,
                   "winner": (a.pid if r["winner"] == "a" else b.pid) if r["winner"] else None,
                   "loser": loser.pid if loser else None, "destiny_loss": loss,
                   "applied": applied, "turns": r["turns"], "log": log_h}
        self.log(f"  battle pid{a.pid}(first) vs pid{b.pid}: winner pid{summary['winner']}"
                 f" loser pid{summary['loser']} -{loss}命{'' if applied else ' (not applied)'}"
                 f" turns={r['turns']}{tag}")
        return summary

    def game_over(self):
        alive = self.env.state.alive_players()
        return (len(alive) <= 1
                or self.env.state.round >= SAFETY_ROUND_LIMIT)

    def standings(self):
        return {p.pid: p.destiny for p in self.env.state.players}

    # ── bot-facing actions (validated) ──────────────────────────────────────
    def _find(self, p, name, where="any"):
        pools = ([("hand", i, c) for i, c in enumerate(p.hand)] if where in ("any", "hand") else []) + \
                ([("board", i, c) for i, c in enumerate(p.board) if c] if where in ("any", "board") else [])
        exact = [t for t in pools if nm(t[2]) == name]
        if exact:
            return exact[0]
        base = [t for t in pools if nm(t[2]).split("+")[0] == name and "+" not in name]
        if len({nm(t[2]) for t in base}) == 1 and base:
            return base[0]
        raise ValueError(f"no unique card {name!r}; have "
                         f"{sorted({nm(t[2]) for t in pools})}")

    def act_roll(self, p, name):
        where, i, cid = self._find(p, name, "hand")
        rid = self.env.reroll(p, cid)
        fx = self.env.last_exchange_fx
        return f"rolled {name} -> {nm(rid) if rid else '(nothing)'}" + (f" | {fx}" if fx else "")

    def act_absorb(self, p, name):
        where, i, cid = self._find(p, name)
        if where == "board":
            p.board[i] = 0
            p.hand.append(cid)
        before = p.cultivation
        self.env.absorb(p, cid)          # canonical path: [炼化] effects fire
        fx = getattr(self.env, "last_absorb_fx", None)
        notes = []
        self.absorb_counts[p.pid] += 1
        if 29 in p.talents and self.absorb_counts[p.pid] % 8 == 0:   # 勤学苦练
            got = p.bag.deal(1, p.phase, self.env.state.rng, first_exchange=False)
            ids = [C.name_to_base_id(n) if isinstance(n, str) else n
                   for n in (got or [])]
            ids = [c for c in ids if c]
            p.hand.extend(ids)
            if ids:
                notes.append(f"勤学苦练 drew {[nm(c) for c in ids]}")
        return (f"absorbed {name}: 修为 {before}->{p.cultivation}"
                + (f" | {fx}" if fx else "")
                + ((" | " + ", ".join(notes)) if notes else ""))

    def act_merge(self, p, name):
        import merge as M
        matches = [c for c in p.hand if nm(c) == name]
        if len(matches) < 2:
            raise ValueError(f"need two identical HAND copies of {name!r} "
                             f"(use take() first if one is on the board)")
        cid = matches[0]
        if not M.can_level(cid):
            raise ValueError(f"{name} cannot level further")
        p.hand.remove(cid); p.hand.remove(cid)
        up = M.level_up(cid)
        p.hand.append(up)
        p.cultivation += E.MERGE_CULT
        return f"merged -> {nm(up)} (+1 修为 = {p.cultivation})"

    def act_take(self, p, name):
        where, i, cid = self._find(p, name, "board")
        p.board[i] = 0
        p.hand.append(cid)
        return f"took back {name}"

    def act_board(self, p, names):
        slots = E.unlocked_slots(self.env.state.round)
        if len(names) > slots:
            raise ValueError(f"only {slots} slots unlocked this round")
        avail = [c for c in p.board if c] + list(p.hand)
        ids = []
        pool = list(avail)
        for n in names:
            hit = next((c for c in pool if nm(c) == n), None)
            if hit is None:
                hit = next((c for c in pool if nm(c).split('+')[0] == n and '+' not in n), None)
            if hit is None:
                raise ValueError(f"card {n!r} not available; have {sorted({nm(c) for c in pool})}")
            pool.remove(hit)
            ids.append(hit)
        bad = [nm(c) for c in ids if not YB.combat_ok(c)]
        if bad:
            raise ValueError(
                f"cannot field {bad}: economy-only card(s) with no combat "
                f"implementation ([炼化] herbs/elixirs/[置换] utility). "
                f"Absorb or roll them instead.")
        limited = [nm(c) for c in ids if YB.limited_kw(c)]
        if len(limited) > 2:
            raise ValueError(
                f"board illegal: {len(limited)} [消耗]/[持续] cards "
                f"({', '.join(limited)}) — a board may hold at most 2.")
        p.board = ids + [0] * (8 - len(ids))
        p.hand = pool
        return f"board = {[nm(c) for c in ids]}"

    PHYS_REQ = {2: 9, 3: 21, 4: 36, 5: 55}   # 体魄 breakthrough gates (user rule)

    def _realm_for_physique(self, tipo):
        realm = 1
        for r in sorted(self.PHYS_REQ):
            if tipo >= self.PHYS_REQ[r]:
                realm = r
        return realm

    def act_breakthrough(self, p, fate_ranking):
        self.fate_rankings[p.pid] = [int(x) for x in fate_ranking or []]
        before = p.realm
        if self.env.try_breakthrough(p):
            return (f"BREAKTHROUGH 境{before}->境{p.realm}; HP {p.battle_hp}; "
                    f"体魄 {p.tipo}/{p.max_tipo}; "
                    f"天命 {[FA.name(t) for t in p.talents]}")
        # 体魄 gates (user rule): 9/21/36/55 体魄 break through even without 修为
        target = self._realm_for_physique(p.tipo)
        if target > p.realm:
            first = p.realm + 1
            p.realm = target
            for r in range(first, target + 1):
                fate_fx.on_breakthrough(self.env, p)
                self.env.pick_fate(p, phase=r)
            self.env._grant_daoyun(p)
            return (f"BREAKTHROUGH via 体魄 境{before}->境{p.realm}; "
                    f"HP {p.battle_hp}; 体魄 {p.tipo}/{p.max_tipo}; "
                    f"天命 {[FA.name(t) for t in p.talents]}")
        gate = E.CULT_REQ.get(p.realm + 1)
        if p.realm >= E.MAX_REALM:
            raise ValueError(f"already 境{p.realm} (max)")
        raise ValueError(f"cannot break: 修为 {p.cultivation} < {gate} and "
                         f"体魄 {p.tipo} < {self.PHYS_REQ.get(p.realm + 1)}")

    def peek_fates(self, p):
        """Preview fate offers WITHOUT touching real state: clone the RNG and
        replay the offer draws. (The old pickle-the-env version threw on the
        FieldBank lambda — broken since game 1, which is why bots never saw
        fate ids and 85-94% of picks fell to the economy default.)"""
        import random
        cult_target = E.realm_for_cultivation(p.cultivation)
        phys_target = self._realm_for_physique(p.tipo)
        target = min(max(cult_target, phys_target), E.MAX_REALM)
        if target <= p.realm:
            raise ValueError("breakthrough not possible yet")
        rng = random.Random()
        rng.setstate(self.env.state.rng.getstate())
        shown, exclude = [], list(p.talents)
        for r in range(p.realm + 1, target + 1):
            offered = FA.offer(p.char_id, p.sect_prefix, rng,
                               exclude=exclude, phase=r)
            shown.append((r, [(f, FA.name(f), FA.version_desc(f, r))
                              for f in offered]))
        return shown
