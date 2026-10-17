# -*- coding: utf-8 -*-
"""play.py — play yixian_sim BY HAND, one command at a time (state persists on disk).

Seat 0 is you; seats 1-7 are the Oracle-search baseline. Each round the driver deals,
lets the bots act, then waits for your commands; `end` fights the battles and opens the
next round.

    python agents/play.py new [--seed 3] [--char 1000004] [--sidejob 4]
    python agents/play.py show
    python agents/play.py roll 练笔 3       # exchange hand cards (NAME or index)
    python agents/play.py absorb 猫薄荷      # 炼化 (+1 修为, plus the card's [炼化] effect)
    python agents/play.py merge 剑劈 剑劈    # two same-level copies -> level+1 (+1 修为)
    python agents/play.py board 0 3 5 2     # set board = these cards in this cyclic order
    python agents/play.py take 1            # board slot -> hand
    python agents/play.py break [56 12]     # breakthrough; optional fate-id preferences
    python agents/play.py sim [cards…]      # Oracle: my board (or the given set) vs every alive opp's last board
    python agents/play.py order cards…      # Oracle: best cyclic order for that set (suggestion only)
    python agents/play.py card 猫薄荷        # rules text of a card
    python agents/play.py daoyun 1000044    # preference list for the R4/R14 道韵 offer
    python agents/play.py end               # battles + next round

Cards may be given by NAME instead of index in any of these (`roll 云剑·猫爪`), and names
are SAFER: indices shift whenever a merge / fate grant / [置换] effect changes the hand,
and a stale index silently acts on the wrong card.

State: agents/mygame/state.pkl, log: agents/mygame/log.txt
"""
from __future__ import annotations
import argparse, json, pickle, random, re, sys, threading
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
ROOT = _HERE.parent
for _p in (_HERE, ROOT / "selfplay", ROOT / "proxy"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import economy as E, env as EV, field as F, characters as CH, cards as C, merge as M
import fates as FA, placement as P, oracle_sim
import fate_fx

SAVE = _HERE / "mygame" / "state.pkl"
LOG = _HERE / "mygame" / "log.txt"
ME = 0

# --- FieldBank pickling (it holds a lock) ---------------------------------------
def _fb_getstate(self):
    d = dict(self.__dict__); d.pop("_lk", None); d["_buckets"] = dict(self._buckets); return d
def _fb_setstate(self, d):
    from collections import defaultdict, deque
    self.__dict__.update(d)
    b = defaultdict(lambda: deque(maxlen=self.per_round)); b.update(d["_buckets"]); self._buckets = b
    self._lk = threading.Lock()
F.FieldBank.__getstate__ = _fb_getstate
F.FieldBank.__setstate__ = _fb_setstate

# --- choosers for the env (module-level so they pickle by reference) ------------
PREFS = {"fate": [], "daoyun": [], "sidejob": 4}

def _prefs(env):
    """Preferences travel ON the env (game4 bug: unpickling can rebind these
    choosers from `__main__.*` to `play.*`, whose module-global PREFS is a
    different, never-loaded dict — which silently dropped fate/道韵 prefs)."""
    return getattr(env, "prefs", None) or PREFS

def sidejob_chooser(env, p):
    return _prefs(env)["sidejob"] if p.pid == ME else env.state.rng.randint(1, 7)

def fate_chooser(env, p, offered):
    if p.pid == ME:
        ph = getattr(env, "_pick_phase", 0) or p.realm   # crossing realm, not final
        log(f"  天命 offer @境{ph}: " + ", ".join(
            f"{f}:{FA.name(f)}[{FA.version_desc(f, ph)}]" for f in offered))
        for f in _prefs(env)["fate"]:
            if f in offered:
                log(f"  -> picked {f}:{FA.name(f)} (preference)"); return f
        f = FA.choose(offered, env.state.rng)
        log(f"  -> picked {f}:{FA.name(f)} (default scorer; set prefs with `break <ids>`)")
        return f
    return FA.choose(offered, env.state.rng)

def daoyun_chooser(env, p, opts):
    if p.pid == ME:
        log(f"  道韵 offer: {[(o, C.id_to_name(o)) if o else (0, '自在随心(draw 1 now)') for o in opts]}")
        for o in _prefs(env)["daoyun"]:
            if o in opts:
                log(f"  -> picked {o}:{C.id_to_name(o)}"); return o
        # binding user ruling baked in (offers fire inside begin_round, BEFORE any
        # prefs can be set for the round — cost 剑意激荡 in games 4 and 6):
        # take 剑意激荡 when offered, otherwise 自在随心 (draw 1 now).
        for o in opts:
            if o and C.id_to_name(o) == "剑意激荡":
                log(f"  -> picked {o}:剑意激荡 (standing rule)"); return o
        log("  -> picked 自在随心 (draw 1 now)")
    return 0

# --- persistence -----------------------------------------------------------------
def save(st):
    st["env"].prefs = st.get("prefs") or dict(PREFS)   # env carries the prefs
    SAVE.parent.mkdir(exist_ok=True)
    with open(SAVE, "wb") as f:
        pickle.dump(st, f)

def load():
    with open(SAVE, "rb") as f:
        st = pickle.load(f)
    PREFS.update(st.get("prefs", {}))
    st["env"].prefs = st.get("prefs") or dict(PREFS)
    return st

def log(msg):
    print(msg)
    LOG.parent.mkdir(exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def sync(st):
    """Append a compact EXACT-state line (`. hand=… board=… rr=…`) after an action so
    replay_viewer can reconstruct the game move-by-move without inference."""
    p = me(st); env = st["env"]
    LOG.parent.mkdir(exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write("  . hand=" + "|".join(nm(c) for c in p.hand)
                + " board=" + "|".join(nm(c) for c in p.board if c)
                + f" rr={p.rerolls} cult={p.cultivation} realm={p.realm} hp={p.battle_hp}"
                + f" destiny={p.destiny} slots={E.unlocked_slots(env.state.round)}"
                + " talents=" + "|".join(FA.name(t) for t in p.talents) + "\n")


# --- helpers ------------------------------------------------------------------------
def nm(cid):
    lv = M.card_level(cid)
    return C.id_to_name(cid) + (f"+{lv-1}" if lv > 1 else "")

def phase_of(p, cid):
    return p.bag.phase.get(C.id_to_name(cid), "?")

def avail(p):
    """Unified list: board cards (in slot order) then hand."""
    return [c for c in p.board if c] + list(p.hand)

def me(st):
    return st["env"].state.players[ME]

def opponents_fixtures(env):
    return [(pid, fx) for pid, fx in env.round_open_fixtures.items() if pid != ME
            and env.state.players[pid].alive]

def show(st):
    env = st["env"]; p = me(st); rnd = env.state.round
    slots = E.unlocked_slots(rnd)
    nxt = E.CULT_REQ.get(p.realm + 1)
    print(f"\n=== ROUND {rnd} | {CH.name(p.char_id)} 副职={p.career} | 境{p.realm} 修为={p.cultivation}"
          f"{f' (next gate {nxt})' if nxt and p.realm < E.MAX_REALM else ' (MAX realm — 修为 past here is inert)' if p.realm >= E.MAX_REALM else ''} | 命={p.destiny} HP={p.battle_hp} "
          f"| 换牌={p.rerolls} | slots={slots} | 天命={[FA.name(t) for t in p.talents]}")
    av = avail(p); nb = len([c for c in p.board if c])
    print("BOARD (cyclic order):")
    for i, c in enumerate(av[:nb]):
        print(f"  [{i}] {nm(c)}  (ph{phase_of(p,c)})")
    if nb == 0: print("  (empty)")
    print("HAND:")
    for i, c in enumerate(av[nb:], start=nb):
        left = p.bag.copies.get(C.id_to_name(c), '?')
        print(f"  [{i}] {nm(c)}  (ph{phase_of(p,c)}, pool left {left})")
    if p.pending_grants: print(f"  pending 道韵 grants: {[(ph, C.id_to_name(c)) for ph, c in p.pending_grants]}")
    print("OPPONENTS (last fielded board):")
    for q in env.state.players:
        if q.pid == ME: continue
        # fog of war (game5 bug): q.board is already THIS round's ghost board —
        # show the round-open snapshot (= their LAST fielded board), like sim.
        ofx = (env.round_open_fixtures or {}).get(q.pid) or {}
        b = [nm(c) for c in ofx.get("usedCards", []) if c]
        st_ = "DEAD" if not q.alive else f"境{q.realm} 修{q.cultivation} 命{q.destiny}"
        g = (st.get("ghosts") or {}).get(q.pid)
        tag = f" [{g['uid']}]" if g else ""
        print(f"  pid{q.pid} {CH.name(q.char_id)}{tag} {st_}: {b}")
    if st.get("last_battle"): print("LAST BATTLE: " + st["last_battle"])

def sim(st, ids=None, verbose=True, log_it=True):
    env = st["env"]; p = me(st); rnd = env.state.round; slots = E.unlocked_slots(rnd)
    board = ids if ids is not None else [c for c in p.board if c]
    if not board: print("empty board"); return
    fx = p.to_fixture(slots); fx["usedCards"] = list(board[:slots]) + [0] * max(0, slots - len(board))
    if ids is not None:                     # candidate board: hand = avail minus what's fielded
        pool = [c for c in p.board if c] + list(p.hand)
        for c in board:
            if c in pool: pool.remove(c)
        fx["handCards"] = pool              # (current-board sims keep the exact hand)
    opps = opponents_fixtures(env)
    tot = 0; wins = 0
    for pid, ofx in opps:
        # seat the pair like acts_first: higher-修为 side is p1 (first mover).
        # game3 bug: always simming as p1 flipped 猫魂庇佑's parity at R16.
        # game5 bug: use LIVE cultivation (修为 is public info), not the stale
        # last-round fixture's exp. tie = coin flip in reality; me as p1 on ties.
        if env.state.players[pid].cultivation > p.cultivation:
            r = oracle_sim.matchup(ofx, fx, rnd=rnd)
            r = dict(r, lifeDamage=-float(r.get("lifeDamage", 0) or 0),
                     hpDelta=-float(r.get("hpDelta", 0) or 0))
        else:
            r = oracle_sim.matchup(fx, ofx, rnd=rnd)
        ld = float(r.get("lifeDamage", 0) or 0); hp = float(r.get("hpDelta", 0) or 0)
        tot += ld; wins += ld > 0 or (ld == 0 and hp > 0)
        if verbose:
            cap = ""
            if ld == 0:                # turn cap: the HP margin still costs 命 (formula)
                eff = E.destiny_damage(rnd, abs(hp)) * (1 if hp > 0 else -1)
                cap = f"  [turn cap → {eff:+d} 命]"
            print(f"  vs pid{pid} {CH.name(env.state.players[pid].char_id)}: life {ld:+.0f} hp {hp:+.0f} turns {r.get('turns')}{cap}")
    n = max(1, len(opps))
    line = f"=> avg 命 margin {tot/n:+.1f}, wins {wins}/{len(opps)}   board={[nm(c) for c in board]}"
    print("  " + line)
    if log_it:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"  sim {line}\n")
    return tot / n

def order(st, ids):
    env = st["env"]; p = me(st); rnd = env.state.round; slots = E.unlocked_slots(rnd)
    fx = p.to_fixture(slots)
    opps = [ofx for _, ofx in opponents_fixtures(env)]
    out = P.best_ordering(fx, list(ids), opps, rnd=rnd)
    best = out[0] if isinstance(out, tuple) else out.get("board", out)
    print(f"  suggested order: {[nm(c) for c in best]}")
    sim(st, list(best))

_BOT = None
def _bot():
    global _BOT
    if _BOT is None:
        _BOT = EV.make_field_policy(k=6, cap=14, order=True)
    return _BOT

# --- round machinery (mirrors env.play_round, split around seat 0) --------------------
def apply_ghost(p, traj, rnd: int):
    """Set a GHOST seat's state to its recorded trajectory at round `rnd`: the sighting
    with the largest round ≤ rnd (carry-forward), else the first. Past the end of the
    record the last known state simply repeats (user rule). 命/alive stay env-tracked."""
    rounds = traj["_rounds"]
    ks = [r for r in rounds if r <= rnd]
    s = rounds[max(ks)] if ks else rounds[min(rounds)]
    board = list(s["board"])[:8]
    p.board = board + [0] * (8 - len(board))
    p.realm = s["level"]; p.cultivation = s["exp"]; p.extra_hp = s["extraMaxHp"]
    p.talents = list(s["talents"]); p.talent_phases = {}
    p.career = s["career"]; p.tipo = s["tipo"]; p.max_tipo = s["max_tipo"]
    p.hand = list(s.get("hand") or [])   # recorded kept hand — combat reads it (手牌-conditional effects)


def begin_round(st):
    env = st["env"]; env.state.round += 1
    ghosts = st.get("ghosts") or {}
    alive = env.state.alive_players()
    unlocked0 = E.unlocked_slots(env.state.round)
    env.round_open_fixtures = {p.pid: p.to_fixture(unlocked0) for p in alive}
    if env.state.round == E.SIDEJOB_ROUND:
        for p in alive:
            if p.pid not in ghosts: env.select_sidejob(p)
    env.last_daoyun = []
    if env.state.round in env.DAOYUN_ROUNDS:
        for p in alive:
            if p.pid not in ghosts: env.select_daoyun(p)
    for p in alive:
        if p.pid in ghosts:                   # recorded bot: replay its board/stats
            apply_ghost(p, ghosts[p.pid], env.state.round)
            # NO re-snapshot (user ruling, game4 review R3): you only know an
            # opponent's LAST-round board while shopping — the top-of-function
            # snapshot (taken before apply_ghost) is exactly that. sim seeing
            # the current recorded board was information the real game hides.
            continue
        p.cultivation += E.passive_cult(env.state.round)
        p.extra_hp += E.passive_hp(env.state.round)   # +2 max HP per round (all players)
        fate_fx.on_round_start(env, p)
        env.refresh_slots_rerolls(p)
        dealt = env.deal_round(p, first_exchange=True)
        if p.pid == ME:                       # the round's draw — R1 is the opening 5
            log(f"  deal {', '.join(nm(c) for c in dealt)}")
            sync(st)
    if any(p.pid != ME and p.pid not in ghosts for p in alive):
        bot = _bot()
        for p in alive:
            if p.pid != ME and p.pid not in ghosts:
                bot(env, p)
                if len(p.hand) > EV.HAND_LIMIT: p.hand = p.hand[-EV.HAND_LIMIT:]

def finish_round(st):
    env = st["env"]; alive = env.state.alive_players()
    p = me(st)
    if len(p.hand) > EV.HAND_LIMIT:               # oldest cards are dropped — SAY SO
        dropped = p.hand[:-EV.HAND_LIMIT]         # (game2 R17→R18 silently ate 御空剑阵+1)
        p.hand = p.hand[-EV.HAND_LIMIT:]
        log(f"  !! hand over {EV.HAND_LIMIT}: dropped {', '.join(nm(c) for c in dropped)}")
    env.last_round_battles = []
    st["last_battle"] = f"R{env.state.round}: (no battle logged)"
    lines = []

    def _one_battle(a, b, extra_for=None):
        """Resolve a vs b. `extra_for`: the odd-player-out's EXTRA battle (user
        ruling, game4 review R12 — there are NO byes): only that player can lose
        命 from it; if they win, the opponent loses nothing."""
        if not env.acts_first(a, b): a, b = b, a
        margin, hpm = env.resolve_pairing(a, b)
        a_won = margin > 0.5 or (abs(margin) < 0.5 and hpm > 0)
        loser = b if a_won else a
        if extra_for is None:
            env.apply_battle(a, b, margin, hpm)
            fate_fx.on_battle_end(env, a, a_won, margin); fate_fx.on_battle_end(env, b, not a_won, -margin)
            a.last_opp, b.last_opp = b.pid, a.pid
        else:
            if loser.pid == extra_for.pid:      # odd player lost → they pay normally
                env.apply_battle(a, b, margin, hpm)
            won = extra_for.pid != loser.pid
            fate_fx.on_battle_end(env, extra_for, won, margin if a.pid == extra_for.pid else -margin)
            extra_for.last_opp = b.pid if a.pid == extra_for.pid else a.pid
        if ME in (a.pid, b.pid):
            mine_first = a.pid == ME
            m = margin if mine_first else -margin
            hp_m = hpm if mine_first else -hpm
            eff = m if abs(m) >= 0.5 else hp_m      # turn cap: HP margin decides + costs 命
            cap = "" if abs(m) >= 0.5 else " (turn cap, HP margin)"
            opp = b if mine_first else a
            tag = " [extra: odd one out]" if extra_for is not None else ""
            line = (f"R{env.state.round} vs pid{opp.pid} {CH.name(opp.char_id)}{tag} "
                    f"({'I act first' if mine_first else 'they act first'}): "
                    f"{'WIN' if eff > 0 else 'LOSS' if eff < 0 else 'DRAW'} "
                    f"margin {eff:+.0f}{cap} → my 命 {p.destiny}")
            # a round can hold TWO of my battles (no-bye extras) — show them all
            st["last_battle"] = (st["last_battle"] + "  ||  " + line
                                 if st.get("last_battle", "").startswith(f"R{env.state.round} vs")
                                 else line)
        lines.append(f"  pid{a.pid} vs pid{b.pid}: margin {margin:+.0f} ({'a' if a_won else 'b'} won)"
                     + (f" [extra for pid{extra_for.pid}]" if extra_for is not None else ""))

    paired = set()
    for a, b in env._pair(alive):
        paired.add(a.pid); paired.add(b.pid)
        _one_battle(a, b)
    odd = [q for q in alive if q.pid not in paired]
    if odd:                                     # no byes: odd one fights a random opp
        solo = odd[0]
        others = [q for q in alive if q.pid != solo.pid]
        if others:
            _one_battle(solo, env.state.rng.choice(others), extra_for=solo)
    unlocked = E.unlocked_slots(env.state.round)
    import body as B
    for q in alive:
        if any(q.board):
            B.accrue(q, [c for c in q.board if c])
            env.field.add(env.state.round, q.to_fixture(unlocked))
    log(f"--- R{env.state.round} battles:\n" + "\n".join(lines))
    log("  " + st["last_battle"])
    log("  standings: " + ", ".join(f"pid{q.pid}:{q.destiny}" for q in env.state.players))

def game_over(st):
    return len(st["env"].state.alive_players()) <= 1 or not me(st).alive or st["env"].state.round >= 20

# --- commands ------------------------------------------------------------------------
def _pick_ghosts(rng) -> dict:
    """RANDOMLY seat 7 recorded-bot trajectories from the agents/ghosts.json pool
    (~30 bots, all of whom reached 境5 — user rule 2026-09-04). Seeded by the game
    seed, so a lobby is reproducible; distinct characters preferred for variety."""
    data = json.loads((_HERE / "ghosts.json").read_text(encoding="utf-8"))
    pool = list(data["trajs"])
    rng.shuffle(pool)
    chosen, seen_chars = [], set()
    for t in pool:                                # pass 1: distinct characters
        if len(chosen) >= 7:
            break
        if t["char"] not in seen_chars:
            seen_chars.add(t["char"]); chosen.append(t)
    for t in pool:                                # pass 2: fill any remainder
        if len(chosen) >= 7:
            break
        if t not in chosen:
            chosen.append(t)
    for t in chosen:                              # int-keyed sightings for apply_ghost
        t["_rounds"] = {int(k): v for k, v in t["rounds"].items()}
    return {i + 1: t for i, t in enumerate(chosen)}


def cmd_new(a):
    if LOG.exists(): LOG.unlink()
    rng = random.Random(a.seed)
    ghosts = _pick_ghosts(rng) if a.ghosts else {}
    if ghosts:
        others = [t["char"] for t in ghosts.values()]
    else:
        others = [c for c in CH.sample(8, rng) if c != a.char][:7]
    chars = [a.char] + others
    env = EV.YiXianEnv(n_players=8, characters=chars, seed=a.seed, field_bank=F.FieldBank(),
                       fate_chooser=fate_chooser, sidejob_chooser=sidejob_chooser,
                       daoyun_chooser=daoyun_chooser)
    env.reset()
    PREFS["sidejob"] = a.sidejob
    st = {"env": env, "prefs": dict(PREFS), "ghosts": ghosts}
    if ghosts:
        log(f"NEW GAME seed={a.seed} me={CH.name(a.char)} vs RECORDED BOTS: "
            + ", ".join(f"pid{pid} {CH.name(t['char'])}[{t['uid']} r{t['first']}-{t['last']} of {t['rec']}]"
                        for pid, t in ghosts.items()))
    else:
        log(f"NEW GAME seed={a.seed} me={CH.name(a.char)} vs {[CH.name(c) for c in others]}")
    begin_round(st); save(st); show(st)

def resolve(p, args):
    """Resolve command arguments to card ids.

    An argument that is a number is an avail-INDEX; anything else is a card NAME —
    exact, else unique prefix, else unique substring. Prefer names: indices shift the
    moment a merge/grant/[置换] effect changes the hand, and acting on a stale index
    silently eats the wrong card (this cost a 云剑·猫爪 and a 灵猫乱剑 in earlier games).
    Each argument consumes a DISTINCT card, so `merge 剑劈 剑劈` takes two copies."""
    av = avail(p)
    names = [nm(c) for c in av]
    used, out = set(), []
    for a in args:
        a = str(a)
        if re.fullmatch(r"-?\d+", a):
            i = int(a)
            if i < 0 or i >= len(av):
                raise SystemExit(f"bad index {i} (hand has {len(av)} cards — run `show`)")
            if i in used:
                raise SystemExit(f"index {i} given twice")
            used.add(i); out.append(av[i]); continue
        # a bare base name must NOT silently match a LEVELLED copy (game7: `roll
        # 巨鲲灵剑` ate 巨鲲灵剑+1 once the lv1 left the hand) — level-suffixed
        # cards require the '+' to be typed.
        guard = (lambda n: "+" not in n) if "+" not in a else (lambda n: True)
        for match in (lambda n: n == a,
                      lambda n: n.startswith(a) and guard(n),
                      lambda n: a in n and guard(n)):
            hits = [i for i, n in enumerate(names) if i not in used and match(n)]
            if hits:
                break
        if not hits:
            raise SystemExit(f"no card matching {a!r} — have: {', '.join(sorted(set(names)))}")
        distinct = {names[i] for i in hits}
        if len(distinct) > 1:
            raise SystemExit(f"{a!r} is ambiguous: {', '.join(sorted(distinct))}")
        used.add(hits[0]); out.append(av[hits[0]])
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd"); ap.add_argument("args", nargs="*")
    ap.add_argument("--seed", type=int, default=3); ap.add_argument("--char", type=int, default=1000004)
    ap.add_argument("--sidejob", type=int, default=4)
    ap.add_argument("--ghosts", action="store_true", help="opponents = recorded real AI bots (agents/ghosts.json)")
    a = ap.parse_args()
    if a.cmd == "new": return cmd_new(a)
    st = load(); env = st["env"]; p = me(st)
    args = list(a.args)
    ints = [int(x) for x in args if re.fullmatch(r"-?\d+", x)]
    if a.cmd == "show": show(st); return
    if a.cmd == "roll":
        for cid in resolve(p, args):
            if p.rerolls <= 0 and not (env.FREE_ROLL_FATE in p.talents and not p.free_roll_used):
                print("no 换牌 left"); break
            if cid not in p.hand: print(f"{nm(cid)} is on the board — `take` it first"); continue
            new = env.reroll(p, cid); log(f"  roll {nm(cid)} -> {nm(new) if new else '?'}")
            if getattr(env, "last_exchange_fx", None): log(f"  fx {env.last_exchange_fx}")
    elif a.cmd == "absorb":
        for cid in resolve(p, args):
            if cid in p.hand:
                env.absorb(p, cid); log(f"  absorb {nm(cid)} -> 修为 {p.cultivation}")
                if getattr(env, "last_absorb_fx", None): log(f"  fx {env.last_absorb_fx}")
            else: print(f"{nm(cid)} is on the board — `take` it first")
    elif a.cmd == "merge":
        x, y = resolve(p, args[:2])
        if x != y or not M.can_level(x) or p.hand.count(x) < 2:
            print("need two identical hand copies of a levellable card"); return
        p.hand.remove(x); p.hand.remove(x); up = M.level_up(x); p.hand.append(up)
        p.cultivation += E.MERGE_CULT; log(f"  merge -> {nm(up)} (+1 修为 = {p.cultivation})")
    elif a.cmd == "take":
        for cid in resolve(p, args):
            for i, c in enumerate(p.board):
                if c == cid: p.board[i] = 0; p.hand.append(cid); log(f"  take {nm(cid)}"); break
        p.board = [c for c in p.board if c] + [0] * (8 - len([c for c in p.board if c]))
    elif a.cmd == "board":
        ids = resolve(p, args); slots = E.unlocked_slots(env.state.round)
        if len(ids) > slots: print(f"only {slots} slots"); return
        pool = avail(p)
        for c in ids: pool.remove(c)
        p.board = ids + [0] * (8 - len(ids)); p.hand = pool
        log(f"  board = {[nm(c) for c in ids]}"); sim(st, verbose=False)
    elif a.cmd == "peek":
        # preview the fate offers a breakthrough WOULD produce, without committing
        # (game7: fate gates were picked blind from a stale preference list — the
        # offers are rng-drawn inside `break`, so this clones the whole state,
        # breaks the clone, and discards it; the real rng is untouched).
        st2 = pickle.loads(pickle.dumps(st))
        env2 = st2["env"]; p2 = env2.state.players[ME]
        env2.prefs = {"fate": [], "daoyun": [], "sidejob": PREFS["sidejob"]}
        shown = []
        def _peek_chooser(e, q, offered):
            if q.pid == ME:
                ph = getattr(e, "_pick_phase", 0) or q.realm
                shown.append((ph, [(f, FA.name(f), FA.version_desc(f, ph)) for f in offered]))
            return FA.choose(offered, e.state.rng)
        env2.fate_chooser = _peek_chooser
        if env2.try_breakthrough(p2):
            for ph, offer in shown:
                print(f"  境{ph} would offer: " + ", ".join(f"{f}:{n}[{d}]" for f, n, d in offer))
            print("  (preview only — run `break <ids ranked>` NEXT; a roll in between "
                  "advances the rng and reshuffles the offers)")
        elif p.realm >= E.MAX_REALM: print(f"cannot break: already 境{p.realm} (MAX realm)")
        else: print(f"cannot break: 修为 {p.cultivation} < {E.CULT_REQ.get(p.realm+1)}")
        return
    elif a.cmd == "break":
        PREFS["fate"] = ints; st["prefs"] = dict(PREFS)
        env.prefs = st["prefs"]      # sync NOW — the chooser fires inside try_breakthrough
        before = p.realm             # (game5 bug: stale env.prefs ignored the given ids)
        if env.try_breakthrough(p): log(f"  BREAKTHROUGH 境{before} -> 境{p.realm}; HP {p.battle_hp}; 天命 {[FA.name(t) for t in p.talents]}")
        elif p.realm >= E.MAX_REALM: print(f"cannot break: already 境{p.realm} (MAX realm)")
        else: print(f"cannot break: 修为 {p.cultivation} < {E.CULT_REQ.get(p.realm+1)}")
    elif a.cmd == "sim":
        sim(st, resolve(p, args) if args else None); return
    elif a.cmd == "order":
        order(st, resolve(p, args)); return
    elif a.cmd == "card":
        cc = json.load(open(ROOT / "vendor/yisim-master/localization/1.5.8/combined_cards.json", encoding="utf-8"))
        by = {c["card_id"]: c for c in cc}
        for cid in resolve(p, args):
            c = by.get(cid); print(f"  {nm(cid)}: {c['desc_cn'] if c else '(no text)'}" + (f"\n     {c['desc_en']}" if c else ""))
        return
    elif a.cmd == "pool":
        # remaining copies in MY draw pool (deterministic — user ruling, game4
        # review: use copy counts to pick WHICH card to roll away; sect rolls
        # burn 3 copies, sidejob rolls 2). No args → every nonzero count.
        want = ({n for n in p.bag.copies for q in args if str(q) in n} or set(map(str, args))) if args else None
        rows = [(n, k) for n, k in sorted(p.bag.copies.items())
                if (want is None and k > 0) or (want and n in want)]
        for n, k in rows:
            ph = p.bag.phase.get(n, "?")
            print(f"  {n}: {k} copies (境{ph}{', sidejob' if n in p.bag.sidejob else ''})")
        if not rows: print("  (no matching cards in pool)")
        return
    elif a.cmd == "daoyun":
        PREFS["daoyun"] = ints; st["prefs"] = dict(PREFS); env.prefs = st["prefs"]
        print("daoyun prefs", ints)
    elif a.cmd == "end":
        finish_round(st)
        if game_over(st):
            env_ = st["env"]; surv = sorted(env_.state.alive_players(), key=lambda q: -q.destiny)
            log(f"GAME OVER after R{env_.state.round}. Alive: {[(q.pid, q.destiny) for q in surv]}  me alive={p.alive} 命={p.destiny}")
            save(st); return
        begin_round(st)
    else:
        print("unknown command"); return
    sync(st); save(st); show(st)

if __name__ == "__main__":
    main()
