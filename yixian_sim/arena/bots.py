# -*- coding: utf-8 -*-
"""Arena bots — each seat is an LLM playing through a tool interface.

Per round, a bot gets a fresh conversation (context wiped between GAMES, and
each round is one tool-runner session): an observation (its private state +
every opponent's LAST-round public state), plus tools to study cards, read
yisim source, run yisim battle sims, consult its persistent notebook/programs,
and act (roll/absorb/merge/take/set_board/breakthrough/end_turn).

Persistent state per bot lives in arena/bots_state/<name>/:
  notebook.md   — the bot's own strategy notes (it rewrites these post-game)
  programs/     — helper scripts the bot wrote (run in a subprocess, cwd-jailed)
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
import traceback
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent / "selfplay"))

import cards as C
import draws as D
import oracle_bridge as OB
import search as SB
import economy as E
import fates as FA
import engine as ENG
import fate_map as FM
import yisim_bridge as YB

STATE_DIR = _HERE / "bots_state"


class InsufficientBalance(Exception):
    """DeepSeek HTTP 402. Must abort the whole game: catching it as a normal
    turn error would forfeit every remaining turn and score a fake result."""


LEDGER_MARK = "==== LEDGER ENTRY ·"   # harness-only entry boundary
REVIEW_SNAPSHOT_DIR = _HERE / "review_snapshot"
REVIEW_SNAPSHOT = None                 # set by snapshot_for_review()


def snapshot_for_review() -> Path:
    """Freeze every bot's playbook + ledger at game end, BEFORE any review.
    Reviews run one after another, so without this the last reviewer read
    rivals' freshly updated files while the first read stale ones — an
    advantage that always went to the same seat. Rivals now read this frozen
    copy; each bot still reads and writes its OWN live files."""
    import shutil
    global REVIEW_SNAPSHOT
    if REVIEW_SNAPSHOT_DIR.exists():
        shutil.rmtree(REVIEW_SNAPSHOT_DIR)
    for d in STATE_DIR.iterdir():
        if not d.is_dir():
            continue
        out = REVIEW_SNAPSHOT_DIR / d.name
        out.mkdir(parents=True, exist_ok=True)
        for fn in ("notebook.md", "ledger.md"):
            if (d / fn).exists():
                shutil.copy2(d / fn, out / fn)
    REVIEW_SNAPSHOT = REVIEW_SNAPSHOT_DIR
    return REVIEW_SNAPSHOT_DIR
MAX_TOOL_TURNS = 60          # per bot-round safety cap on runner iterations
PROGRAM_TIMEOUT = 30

RULES = """You are playing 弈仙牌 (YiXianPai), a 4-player cultivation auto-battler.
GOAL: be the LAST PLAYER STANDING (destiny 命 > 0 when everyone else is at 0).

Round flow: everyone gets dealt cards, takes economy actions (this is your turn
now), then the matchups auto-battle. Matchups are ANNOUNCED at round start —
your observation's NEXT BATTLE line says exactly who you fight, so tune your
board for that opponent (their current board is still hidden; you see their
LAST-round board). The battle loser loses 命 per the destiny formula. With an
odd number alive, the unpaired player fights a GHOST — a copy of a random
opponent's board, marked (GHOST) — and only the ghost-fighter risks 命 there.

Your action tools this turn (call them in any order, then end_turn):
- roll(card): spend 1 exchange to replace a HAND card with a random draw.
  Sect-card rolls delete 3 copies of that card from your future draw pool,
  sidejob rolls delete 2 ([置换] cards instead fire their effect, no deletion).
- absorb(card): consume a card (hand or board) for +1 修为 (cultivation);
  [炼化] effects fire.
- merge(card): combine two identical HAND copies into +1 level (+1 修为).
- take(card): move a board card back to hand.
- set_board([cards...]): field your board in CYCLIC play order (slot count is
  round-limited; unfielded slots fight as Normal Attack 3-atk turns).
  Economy-only cards ([炼化] herbs, elixirs, [置换] utility like 练笔) have no
  combat effect and CANNOT be fielded — absorb or roll them. LEGALITY: a board
  may hold at most 2 cards with [消耗] or [持续] (combined count).
- peek_breakthrough(): preview the fate (天命) offers a breakthrough would give
  (also shown in SITREP when a breakthrough is available).
- breakthrough([fate_ids ranked]): break through realm gate(s); your ranking
  picks from each gate's offer. More realm = more HP, higher-phase card draws.
  ALWAYS pass a ranking — an empty one falls back to a generic economy pick
  that ignores your 传承/combat fates. Character/combat fates ARE forwarded
  into battles and sims; A/B-test one with simulate(my_extra_fates=[id]).
- choose_sidejob(career): ROUND 2 ONLY, one-time — adds that career's cards to
  your draw pool for the rest of the game
  (1=炼丹师 2=符咒师 3=琴师 4=画师 5=阵法师 6=灵植师 7=命理师).
- sim_matchup(my_cards, opp_pid): ONE call checks your board both seats vs
  the opponent's last board AND its +1 upgrade. Use before every set_board.
- simulate(...): one exact yisim battle (full turn log available) for
  digging into a specific line.
- battle_log(round): the real log of a battle you already fought this game.
- card_text(names), yisim_grep(pattern): card rules; engine source lookup.
  (Your hand/board/opponent cards' effects are already in CARD REFERENCE.)
- notebook(): your own notes from previous games. Trust them; refine later.
- run_program(name, args): run a helper program you wrote in a past game.
- get_observation(): refresh your view after actions.
- end_turn(summary): REQUIRED to finish. Cards left unfielded stay in hand
  (hand cap 16, oldest dropped).

COMBAT MECHANICS (verified against the engine source — trust these over
intuition):
TEMPO — the third scaling axis besides damage and sustain: a turn plays 1
card, but [再次行动] (chase) plays a SECOND card the same turn. Hard cap
+1 chase/turn (only rare 龙 effects raise it); any number of chase triggers
on one card still = +1. If a card didn't chase itself and you have ≥10
[身法], 10 身法 is AUTO-SPENT to chase. [困缚] on you cancels a chase
(spends 1 stack, decays 1/turn). A working 身法/chase engine nearly doubles
your cards per turn.
TURN-START TIMING (your turn): your 防 halves (round up), [内伤] deals its
stacks to you, [恢复] heals you, then you act.
KEYWORD GLOSSARY:
- [灵气] qi pays card costs; if you can't pay, the turn is spent gaining
  1 qi instead of playing.
- [剑意] sword intent: +1 dmg per point on EVERY hit of a card; the bank is
  exhausted at the end of that card (generators that never attack keep it).
- [气势] force: +10% dmg per point, 1 point spent per attack; cap 6 by
  default (some cards raise the cap; excess over cap is lost).
- [星力] star power: flat +dmg on every attack while the played card sits on
  a [星位] slot. Slots 3 and 6 are 星位 BY DEFAULT — free real estate.
- [体魄] physique: +1 max HP per point; persists across rounds up to the cap.
- [防] def: damage shield, halves at your turn start. [碎防] destroys 防 at
  2x rate. [无视防御]: one attack ignores 防 (1 stack per attack).
- [护体] guard_up: negates ONE whole hp-damage hit (not hp costs).
- [锋锐] penetrate: flat bonus added to hp damage on [击伤], then fully
  consumed.
- [击伤] "injured" triggers only if the attack got HP DAMAGE THROUGH —
  防-blocked hits do not count. [外伤] wound: added to every 击伤 you take,
  permanent.
- [内伤] internal injury: hp loss at the VICTIM's turn start, permanent — a
  clock that kills through any 防 or heal-per-hit defense.
- [虚弱] your dmg x0.6; [破绽] dmg you take x1.4 (each decays 1/turn).
  [加攻]/[减攻]: permanent flat attack change.
- [消耗]: after its first play the slot is REMOVED from the cycle for the
  rest of the battle. [持续]: same removal, but the effect persists as an
  aura. (Board legality: ≤2 such cards total.)
- [开局]: fires before turn 1 for both players. [后招]: does NOTHING on the
  slot's first play; fires from its second cycle onward.
- [连云] cloud-hit: true only if the PREVIOUS card you played was also a
  云剑 — the chain resets on any non-云剑 card, so the first 云剑 of a run
  never has it.
- [五行] element gating: active iff your previous card was that element or
  GENERATES it (木→火→土→金→水→木); any off-element card breaks the chain.
- 剑阵 is a card-name class (some cards count or retrigger 剑阵 plays), not
  a mechanic by itself. [卦象] hexagram: Heptastar resource; also zeroes
  certain percent rolls.

DRAWS & ROLLS (how your deck works — verified against the engine):
- PHASE GATING: a phase-N card can only be drawn once you are at 境N or
  higher. Phase-5 cards (e.g. the big finishers) are UNREACHABLE until you
  break to 境5.
- DEALS each round: R1 = 5 sect cards; R2-R11 = 2 sect + 1 sidejob;
  R12+ = 3 sect + 1 sidejob. The first card of each round's deal counts
  current-phase cards double.
- A ROLL draws ONE random card from your WHOLE remaining deck (sect +
  sidejob, every phase you can reach), weighted by copies left. You CANNOT
  aim a roll at a card — deciding what to throw away is your only control.
- BURN: rolling a card away also destroys copies of it left in your deck —
  3 for a sect card, 2 for a sidejob card, 0 for [置换] cards (a merged card
  burns its base card's copies). Absorbing and merging burn nothing. Burning
  junk permanently THINS the deck, so every later draw is more likely to be
  a card you want.
- RARITY: a single phase-5 card is typically ~6 copies in a deck of several
  hundred — expect about ONE copy per game after reaching 境5, even rolling
  hard. A plan that needs one specific phase-5 card is a coin flip; keep a
  backup plan. pool_cards() shows your live copy counts and odds.

Key facts: exchanges (换牌) bank between rounds, but the round-start grant
(+3 R1-9, +4 R10-12, +6 R13+) only fills you up to 25 — at/above 25 banked you
get NOTHING at round start until you spend back below 25 ([置换]/天命 gains can
still push you past 25). Don't hoard past the cap; spend before you waste
grants. Cultivation 修为 also decides battle seat (higher acts first, tie =
coin flip). Realm gates: 境2@9 境3@21 境4@36 境5@55 修为 — OR by 体魄
(physique): 9/21/36/55 体魄 lets you break through without the 修为.
体魄 rules: every 体魄 point = +1 max HP in battle (生命转化). Physique your
cards build IN battle persists to later rounds (跨回合保留), clamped after the
battle to a retention cap that starts at 6 and grows +5 every round; in-battle
you may exceed the cap freely. Merging/absorbing gives 修为. You keep at most 8 board slots; slots unlock 3/4/5/6/7/8/8/8 by
round. Battles cap at 64 turns (higher HP wins). Play to WIN the lobby, not
each round: losing a cheap round early can be right if it buys economy."""


_card_idx_cache = None


def _card_index() -> dict:
    """name_cn -> [card rows, all levels] from the localization DB."""
    global _card_idx_cache
    if _card_idx_cache is None:
        raw = json.loads((YB.YISIM_DIR / "localization" / "1.5.9" /
                          "combined_cards.json").read_text(encoding="utf-8"))
        idx = {}
        for c in (raw if isinstance(raw, list) else raw.values()):
            n = (c.get("name_cn") or "").replace("•", "·").strip()
            if n:
                idx.setdefault(n, []).append(c)
        _card_idx_cache = idx
    return _card_idx_cache


def _desc_for(name: str) -> str:
    """One-line effect text for a (possibly levelled) card name."""
    base, _, lv = name.partition("+")
    rows = _card_index().get(base.replace("•", "·"))
    if not rows:
        return "(?)"
    want = int(lv or 0) + 1
    row = next((r for r in rows if r.get("level") == want), rows[0])
    return (row.get("desc_cn") or "").replace("\\n", " ｜ ")


_card_names_by_len = None


def _cards_in_text(text: str) -> list:
    """Card names referenced inside a text (e.g. a card-granting fate's
    description), longest match first, no overlapping submatches."""
    global _card_names_by_len
    if _card_names_by_len is None:
        _card_names_by_len = sorted((n for n in _card_index() if len(n) >= 3),
                                    key=len, reverse=True)
    found = []
    for n in _card_names_by_len:
        if n in text and not any(n in f for f in found):
            found.append(n)
    return found


def _fate_offer_text(shown) -> str:
    """Format peeked fate offers; card-granting fates get the granted card's
    own text appended so the bot knows what it actually does."""
    lines = []
    for ph, offer in shown:
        lines.append(f"境{ph} offers (rank by id in breakthrough([...])):")
        for f, n, d in offer:
            lines.append(f"  {f}: {n} [{d}]")
            for cn in _cards_in_text(d):
                lines.append(f"      ↳ granted card {cn}: {_desc_for(cn)}"
                             " (sim it by adding the card to my_cards)")
    return "\n".join(lines)


def bot_dir(name: str) -> Path:
    d = STATE_DIR / name
    (d / "programs").mkdir(parents=True, exist_ok=True)
    nb = d / "notebook.md"
    if not nb.exists():
        nb.write_text(f"# {name} — strategy notebook\n\n(empty — first game)\n",
                      encoding="utf-8")
    lg = d / "ledger.md"
    if not lg.exists():
        lg.write_text(f"# {name} — game ledger (append-only archive)\n",
                      encoding="utf-8")
    return d


class BotSeat:
    """Everything one seat needs: engine handle + persistent dirs + tool impls."""

    def __init__(self, game: ENG.ArenaGame, pid: int):
        self.game = game
        self.pid = pid
        self.p = game.env.state.players[pid]
        self.name = ENG.NAMES[self.p.char_id]
        self.dir = bot_dir(self.name)
        self.turn_log = []
        self.ended = False
        self.end_summary = ""
        self.reflection = False      # post-game review mode: free-card sims
        self.search_evals_left = 1200    # review search budget (evaluations)
        self.search_seconds = 0.0        # review search wall-clock spent
        self._oracle_budget_set = False  # raised once if the Oracle drives

    # ── observation ──────────────────────────────────────────────────────────
    def observation(self, include_cards: bool = True) -> str:
        g, p = self.game, self.p
        rnd = g.env.state.round
        slots = E.unlocked_slots(rnd)
        lines = [f"ROUND {rnd} — you are {self.name} (pid{self.pid})",
                 f"命(destiny)={p.destiny}  修为={p.cultivation}  境={p.realm}  "
                 f"maxHP={p.battle_hp}  体魄={p.tipo}/{p.max_tipo}  "
                 f"exchanges left={p.rerolls}  slots unlocked={slots}  "
                 f"sidejob={p.career}",
                 f"天命 fates: {[FA.name(t) for t in p.talents] or '(none)'}",
                 f"BOARD (cyclic order): {[ENG.nm(c) for c in p.board if c] or '(empty)'}",
                 f"HAND: {[ENG.nm(c) for c in p.hand] or '(empty)'}",
                 "",
                 "OPPONENTS (their LAST-round boards — current boards are hidden):"]
        for pid, snap in sorted(g.round_open.items()):
            if pid == self.pid:
                continue
            s = snap
            lines.append(f"  pid{pid} {s['name']}: {'ALIVE' if s['alive'] else 'DEAD'} "
                         f"命={s['destiny']} 境={s['realm']} 修为={s['cultivation']} "
                         f"maxHP={s['max_hp']} sidejob={s['career']} "
                         f"体魄={s['physique']}/{s['max_physique']}")
            lines.append(f"        last board: {s['board'] or '(unknown)'}")
            lines.append(f"        天命: {s['talents']}")
        opp, ghost = None, False
        for a, b in getattr(g, "pairings", []):
            if self.pid == a:
                opp = b
            elif self.pid == b:
                opp = a
        gp = getattr(g, "ghost_pair", None)
        if opp is None and gp and gp[0] == self.pid:
            opp, ghost = gp[1], True
        if opp is not None:
            lines.append(f"\nNEXT BATTLE: you fight pid{opp} "
                         f"{g.round_open[opp]['name']}"
                         + (" (GHOST — you fight a copy of their board; only "
                            "YOU risk 命 in this battle)" if ghost else ""))
            lines.append(self._sitrep(opp))
        if g.env.state.round == E.SIDEJOB_ROUND and self.pid not in g.sidejobs:
            lines.append("\n** You must choose_sidejob(career) this round. **")
        if include_cards:
            lines.append(self._card_reference(opp))
        return "\n".join(lines)

    def _sitrep(self, opp_pid: int) -> str:
        """Computed situational read — arithmetic the LLM should not re-derive."""
        g, p = self.game, self.p
        rnd = g.env.state.round
        snap = g.round_open[opp_pid]
        sub = 1 if rnd <= 9 else 0
        lo = rnd + 2 - sub
        hi = rnd + 5 + 2 + rnd // 2 - sub
        risk_me = "MUST-WIN for you" if p.destiny <= hi else \
                  ("close for you" if p.destiny <= hi * 2 else "safe for you")
        risk_op = "lethal-range for them" if snap["destiny"] <= hi else ""
        gap = p.cultivation - snap["cultivation"]
        seat = ((f"you LEAD by {gap} 修为 — but that is their START-of-round "
                 f"value; they can absorb/merge this turn too, so you act "
                 f"first only if they gain fewer than {gap} more")
                if gap > 0 else
                (f"you TRAIL by {-gap} 修为 vs their start-of-round value — "
                 f"you act second unless you gain more than {-gap} beyond "
                 f"what they add this turn") if gap < 0 else
                "TIED with their start-of-round 修为 — whoever gains more "
                "this turn acts first; still tied = coin flip")
        parts = [f"SITREP: loser this round pays ~{lo}-{hi}命 — {risk_me}"
                 f" (命{p.destiny})" + (f"; {risk_op} (命{snap['destiny']})"
                                        if risk_op else "") + ".",
                 f"Seat: {seat} (修为 {p.cultivation} vs {snap['cultivation']}).",
                 f"Exchanges: {p.rerolls} banked"
                 + (" — OVER the 25 cap, no grant next round until you spend"
                    if p.rerolls > 25 else
                    (" — near the 25 cap, spend or waste next grant"
                     if p.rerolls >= 20 else "") ) + "."]
        gate = p.realm + 1
        if gate > E.MAX_REALM:
            parts.append("Breakthrough: none — 境5 is the max realm.")
            return "\n".join(parts)
        creq = E.CULT_REQ.get(gate)
        preq = self.game.PHYS_REQ.get(gate) if hasattr(self.game, "PHYS_REQ") \
            else None
        if creq is not None:
            avail = p.cultivation >= creq or (preq and p.tipo >= preq)
            parts.append(
                f"Breakthrough 境{gate}: " +
                ("AVAILABLE NOW" if avail else
                 f"needs 修为{creq} (you {p.cultivation})"
                 + (f" or 体魄{preq} (you {p.tipo})" if preq else "")) + ".")
            if avail:
                offers = self.t_peek_breakthrough()
                parts.append("Fate offers if you break now (rank the ids you "
                             "want in breakthrough([...]) — 传承/combat fates "
                             "power your engine and DO apply in battles):\n"
                             + offers)
        return "\n".join(parts)

    def _card_reference(self, opp_pid=None) -> str:
        names = []
        for c in list(self.p.hand) + [c for c in self.p.board if c]:
            names.append(ENG.nm(c))
        if opp_pid is not None:
            names += self.game.round_open[opp_pid]["board"]
        seen, lines = set(), ["", "CARD REFERENCE (effects of every card in "
                                 "your hand/board + opponent's last board):"]
        for n in names:
            if n in seen:
                continue
            seen.add(n)
            lines.append(f"  {n}: {_desc_for(n)}")
        return "\n".join(lines)

    # ── tool implementations (called by the runner) ──────────────────────────
    def t_get_observation(self) -> str:
        return self.observation()

    def t_card_text(self, names: list) -> str:
        idx = _card_index()
        out = []
        for q in names:
            base = q.split("+")[0].replace("•", "·")
            hits = idx.get(base)
            if not hits:
                out.append(f"{q}: (no card text found)")
                continue
            for c in sorted(hits, key=lambda c: c.get("level") or 0):
                out.append(f"{base} lv{c.get('level')}: {c.get('desc_cn')} "
                           f"| {c.get('desc_en')}")
        return "\n".join(out)

    def t_yisim_grep(self, pattern: str, max_lines: int = 40) -> str:
        try:
            proc = subprocess.run(
                ["grep", "-rn", "-m", "200", pattern, "gamestate_full.js",
                 "card_actions.js", "notes.txt"],
                capture_output=True, cwd=str(YB.YISIM_DIR), timeout=20)
            lines = proc.stdout.decode("utf-8", "replace").splitlines()
            return "\n".join(lines[:max_lines]) or "(no matches)"
        except Exception as e:
            return f"grep failed: {e}"

    def t_simulate(self, my_cards: list, opp_pid: int, opp_cards: list = None,
                   i_go_first: bool = None, full_log: bool = False,
                   my_extra_fates: list = None) -> str:
        g, p = self.game, self.p
        snap = g.round_open.get(int(opp_pid))
        if not snap:
            return f"no such opponent pid{opp_pid}"
        try:
            my_ids = self._my_ids(my_cards)
            opp_names = opp_cards if opp_cards is not None else snap["board"]
            opp_ids = snap["board_ids"] if opp_cards is None else \
                [self._any_name_to_id(n) for n in opp_names]
            talents = list(p.talents)
            phases = dict(getattr(p, "talent_phases", {}) or {})
            for f in (my_extra_fates or []):     # A/B-test a fate pick
                f = int(f)
                if f not in talents:
                    talents.append(f)
                    phases[f] = max(2, min(5, p.realm + 1))
            my_extra = FM.combat_fields(talents, phases,
                                        g.consumed_avatars.get(self.pid, ()))
            me_pl = YB.player_payload(p.char_id, p.cultivation, p.battle_hp,
                                      p.destiny, my_ids, p.tipo, p.max_tipo,
                                      round_number=g.env.state.round,
                                      extra=my_extra)
            opp_pl = YB.player_payload(
                g.env.state.players[int(opp_pid)].char_id, snap["cultivation"],
                snap["max_hp"], snap["destiny"], opp_ids,
                snap["physique"], snap["max_physique"],
                round_number=g.env.state.round,
                extra=FM.combat_fields(snap.get("talent_ids", []),
                                       snap.get("talent_phases", {}),
                                       g.consumed_avatars.get(int(opp_pid), ())))
            for side, idlist in (("my_cards", my_ids), ("opp_cards", opp_ids)):
                lim = [ENG.nm(c) for c in idlist if YB.limited_kw(c)]
                if len(lim) > 2:
                    return (f"ILLEGAL BOARD ({side}): {len(lim)} [消耗]/[持续] "
                            f"cards ({', '.join(lim)}) — a board may hold at "
                            f"most 2")
            first = i_go_first if i_go_first is not None \
                else p.cultivation >= snap["cultivation"]
            r = YB.run_battle(me_pl if first else opp_pl,
                              opp_pl if first else me_pl, a_first=True)
            r["log"] = YB.humanize_log(r["log"],
                                       "ME" if first else "OPP",
                                       "OPP" if first else "ME")
            me_side = "a" if first else "b"
            verdict = ("I WIN" if r["winner"] == me_side else
                       "I LOSE" if r["winner"] else "no result")
            head = (f"{verdict}; loser pays {r['destiny_loss']}命; "
                    f"turns={r['turns']}; me_first={first}")
            if full_log:
                return head + "\n" + r["log"][-6000:]
            tail = "\n".join(r["log"].splitlines()[-25:])
            return head + "\n...\n" + tail
        except Exception as e:
            return f"simulate failed: {e}"

    def _names_to_ids(self, names, p):
        pool = [c for c in p.board if c] + list(p.hand)
        out = []
        for n in names:
            hit = next((c for c in pool if ENG.nm(c) == n), None)
            if hit is None and "+" not in n:
                hit = next((c for c in pool if ENG.nm(c).split("+")[0] == n), None)
            if hit is None:
                raise ValueError(f"you don't have {n!r}")
            pool.remove(hit)
            out.append(hit)
        return out

    def _any_name_to_id(self, n):
        base, _, lv = n.partition("+")
        cid = C.name_to_base_id(base)
        if not cid:
            raise ValueError(f"unknown card {n!r}")
        return cid + 10000 * int(lv or 0)

    def _my_ids(self, my_cards):
        """Resolve my-side card names; free cards allowed in reflection."""
        if self.reflection:
            ids, pool = [], [c for c in self.p.board if c] + list(self.p.hand)
            for n in my_cards:
                hit = next((c for c in pool if ENG.nm(c) == n), None)
                if hit is not None:
                    pool.remove(hit)
                    ids.append(hit)
                else:
                    ids.append(self._any_name_to_id(n))
            return ids
        return self._names_to_ids(my_cards, self.p)

    def _opp_payload(self, opp_pid, opp_cards=None, bump=0):
        g = self.game
        snap = g.round_open[int(opp_pid)]
        ids = snap["board_ids"] if opp_cards is None else \
            [self._any_name_to_id(n) for n in opp_cards]
        if bump:
            ids = [SB._level_variant(c, bump) or c for c in ids]
        return YB.player_payload(
            g.env.state.players[int(opp_pid)].char_id, snap["cultivation"],
            snap["max_hp"], snap["destiny"], ids,
            snap["physique"], snap["max_physique"],
            round_number=g.env.state.round,
            extra=FM.combat_fields(snap.get("talent_ids", []),
                                   snap.get("talent_phases", {}),
                                   g.consumed_avatars.get(int(opp_pid), ())))

    def _me_payload(self, ids):
        g, p = self.game, self.p
        return YB.player_payload(
            p.char_id, p.cultivation, p.battle_hp, p.destiny, ids,
            p.tipo, p.max_tipo, round_number=g.env.state.round,
            extra=FM.combat_fields(p.talents,
                                   getattr(p, "talent_phases", {}) or {},
                                   g.consumed_avatars.get(self.pid, ())))

    # ── Oracle (game-code) fixtures: fast outcome-only search pre-filter ────
    def _me_side(self, ids):
        p = self.p
        return OB.side_fixture(p.char_id, p.realm, p.battle_hp, ids,
                               talents=p.talents, career=p.career or 0,
                               physique=p.tipo, max_physique=p.max_tipo)

    def _opp_side(self, opp_pid, opp_cards=None):
        snap = self.game.round_open[int(opp_pid)]
        ids = snap["board_ids"] if opp_cards is None else \
            [self._any_name_to_id(n) for n in opp_cards]
        return OB.side_fixture(
            self.game.env.state.players[int(opp_pid)].char_id, snap["realm"],
            snap["max_hp"], ids, talents=snap.get("talent_ids", []),
            career=snap.get("career") or 0, physique=snap["physique"],
            max_physique=snap["max_physique"])

    def _verify_yisim(self, finalists, opp_payload, objective, reps=3):
        """Re-rank Oracle finalists in yisim — the engine that resolves the
        arena's real battles gets the final say."""
        battles = []
        for ids in finalists:
            me = self._me_payload(ids)
            for _ in range(reps):
                battles.append((me, opp_payload, True))
                battles.append((opp_payload, me, True))
        try:
            res = YB.run_battles(battles)
        except Exception:
            return None, ""
        best, best_score, best_detail, i = None, None, "", 0
        for ids in finalists:
            rr = []
            for _ in range(reps):
                r1, r2 = res[i], res[i + 1]
                i += 2
                rr.append(("first", r1.get("winner") == "a", r1.get("turns")))
                rr.append(("second", r2.get("winner") == "b", r2.get("turns")))
            sc = SB._score(rr, objective)
            if best_score is None or sc > best_score:
                f = [x for x in rr if x[0] == "first"]
                s = [x for x in rr if x[0] == "second"]
                best_score, best = sc, list(ids)
                best_detail = (f"win {100*sum(x[1] for x in f)//len(f)}% first"
                               f" / {100*sum(x[1] for x in s)//len(s)}% second"
                               f" ({reps} reps)")
        return best, best_detail

    @staticmethod
    def _limit_check(ids, label):
        lim = [ENG.nm(c) for c in ids if YB.limited_kw(c)]
        if len(lim) > 2:
            return (f"ILLEGAL BOARD ({label}): {len(lim)} [消耗]/[持续] cards "
                    f"({', '.join(lim)}) — a board may hold at most 2")
        return None

    def t_sim_matchup(self, my_cards: list, opp_pid: int,
                      repeats: int = 3) -> str:
        """Both seats × (opp as-is, opp +1 level) in ONE call."""
        try:
            repeats = max(1, min(int(repeats), 5))
            my_ids = self._my_ids(my_cards)
            err = self._limit_check(my_ids, "my_cards")
            if err:
                return err
            me = self._me_payload(my_ids)
            battles, plan = [], []
            for bump, tag in ((0, "opp as-is"), (1, "opp +1 lvl")):
                opp = self._opp_payload(opp_pid, bump=bump)
                for _ in range(repeats):
                    battles.append((me, opp, True))
                    battles.append((opp, me, True))
                plan.append(tag)
            res = YB.run_battles(battles)
            out, i = [f"sim_matchup vs pid{opp_pid} ({repeats} reps):"], 0
            for tag in plan:
                wf = ws = 0
                tf, ts = [], []
                for _ in range(repeats):
                    r1, r2 = res[i], res[i + 1]
                    i += 2
                    wf += r1.get("winner") == "a"
                    ws += r2.get("winner") == "b"
                    tf.append(r1.get("turns") or 64)
                    ts.append(r2.get("turns") or 64)
                out.append(f"  {tag}: I win {100*wf//repeats}% going first "
                           f"(~{sum(tf)//len(tf)}t), {100*ws//repeats}% going "
                           f"second (~{sum(ts)//len(ts)}t)")
            return "\n".join(out)
        except Exception as e:
            return f"sim_matchup failed: {e}"

    def t_battle_log(self, round: int) -> str:
        """The recorded log of your battle that round. In post-game review,
        ALL of the round's battles are returned — including fights you were
        not in (open-review rule)."""
        out = []
        for rnd_results in self.game.battle_results:
            for r in rnd_results:
                if r.get("round") != int(round):
                    continue
                mine = self.pid in (r["a"], r["b"])
                if not mine and not self.reflection:
                    continue
                log = r["log"]
                hands = self.game.hand_history.get(int(round), {})
                if mine:
                    hand_line = f"Your hand that round: {hands.get(self.pid)}\n"
                elif self.reflection:
                    hand_line = "".join(
                        f"pid{p} hand: {hands.get(p)}\n"
                        for p in (r["a"], r["b"]) if hands.get(p) is not None)
                else:
                    hand_line = ""
                head = (f"R{round}: pid{r['a']}(first) vs pid{r['b']} — "
                        f"winner pid{r['winner']}, -{r['destiny_loss']}命, "
                        f"{r['turns']} turns\n" + hand_line)
                if len(log) > 11000:
                    log = log[:3000] + "\n...[middle truncated]...\n" + log[-7500:]
                out.append(head + log)
        if not out:
            return f"(no battle of yours found in round {round})"
        return "\n\n════════════════\n\n".join(out)

    def t_search_board(self, opp_pid: int = None, start: list = None,
                       pool_careers: list = None, lock_slots: dict = None,
                       lock_cards: list = None, objective: str = "both",
                       evals: int = 120, opp_cards: list = None) -> str:
        """Hill-climb search (review only): bot steers, script grinds."""
        if not self.reflection:
            return "search_board is available in the post-game review only"
        if self.search_evals_left <= 0:
            return "SEARCH BUDGET SPENT (1200 evals) — write up what you have"
        if self.search_seconds > 480:
            return "SEARCH WALL-CLOCK SPENT (8 min) — write up what you have"
        try:
            use_oracle = False
            try:
                use_oracle = OB.available()
            except Exception:
                use_oracle = False
            if use_oracle and not self._oracle_budget_set:
                self._oracle_budget_set = True
                self.search_evals_left = max(self.search_evals_left, 4000)
            cap = 400 if use_oracle else 120
            evals = min(max(1, int(evals)), cap, self.search_evals_left)
            start_ids = self._my_ids(list(start or []))
            if not start_ids:
                return "give a non-empty start board"
            opp = self._opp_payload(opp_pid, opp_cards=opp_cards)
            err = self._limit_check(
                [self._any_name_to_id(n) for n in (opp_cards or [])]
                if opp_cards else [], "opp_cards")
            if err:
                return err
            p = self.p
            pool_ids = [C.name_to_base_id(n) for n in
                        D.build_pool(p.char_id // 1000000, p.career or 0)]
            for c in (pool_careers or []):
                pool_ids += [C.name_to_base_id(n) for n in D.sidejob_pool(int(c))]
            pool_ids = [c for c in set(pool_ids) if c]
            eval_many = None
            if use_oracle:
                eval_many = OB.evaluator(self._me_side, self._opp_side(opp_pid,
                                                                      opp_cards),
                                         self.game.env.state.round, repeats=1)
            t0 = time.time()
            out = SB.hillclimb(self._me_payload, opp, start_ids, pool_ids,
                               lock_slots, lock_cards, objective, evals,
                               repeats=2, nm=ENG.nm, eval_many=eval_many)
            verdict = ""
            if use_oracle:
                # ARBITER: yisim resolves the real battles, so it ranks the
                # Oracle's finalists (the engines disagree on ~17% of matchups).
                best, detail = self._verify_yisim(out.get("finalists") or
                                                  [out["best_ids"]], opp,
                                                  objective, reps=3)
                if best is not None:
                    if tuple(best) != tuple(out["best_ids"]):
                        verdict = (f"\nNOTE: yisim (the engine that resolves "
                                   f"real battles) preferred a different "
                                   f"finalist — reporting ITS pick.")
                    out["best_ids"] = best
                    out["best_detail"] = detail + " [yisim-verified]"
            self.search_seconds += time.time() - t0
            self.search_evals_left -= out["evals_used"]
            self.game.log(
                f"  [review pid{self.pid}] search_board opp=pid{opp_pid}"
                + (" (opp_cards override)" if opp_cards else "")
                + f" pools={pool_careers or []} lock_slots={lock_slots or {}}"
                  f" lock_cards={lock_cards or []} obj={objective}"
                  f" evals={out['evals_used']} -> {out['best_detail']}")
            lines = [f"BEST BOARD ({out['best_detail']}):",
                     "  " + ", ".join(ENG.nm(c) for c in out["best_ids"]),
                     f"engine: {'oracle pre-filter + yisim verdict' if use_oracle else 'yisim'}"
                     f"; evals used {out['evals_used']}; budget left "
                     f"{self.search_evals_left}",
                     "TRACE (accepted improvements, search engine's view):"]
            lines += ["  " + t for t in out["trace"]]
            return "\n".join(lines) + verdict
        except Exception as e:
            return f"search_board failed: {e}"

    def t_economy_history(self, name: str = None) -> str:
        """Per-round economy record: deals, actions, banked rolls. Yours, or
        (in review) any rival's by name."""
        pid = self.pid
        if name and name != self.name:
            if not self.reflection:
                return ("rival economy is private DURING the game — open "
                        "only in post-game review")
            match = [q.pid for q in self.game.env.state.players
                     if ENG.NAMES.get(q.char_id) == name]
            if not match:
                return f"no such bot {name!r}"
            pid = match[0]
        g = self.game
        who = "YOUR" if pid == self.pid else f"{name}'s"
        lines = [f"{who} ECONOMY, round by round (rolls cost 1 exchange "
                 "each; grant +3 R1-9/+4 R10-12/+6 R13+, bank caps at 25):"]
        for rnd in sorted(g.deal_history):
            deal = g.deal_history[rnd].get(pid)
            if deal is None:
                continue
            acts = g.action_history.get(rnd, {}).get(pid, [])
            rolls = sum(a.count("rolled ") for a in acts)
            rr = g.rr_history.get(rnd, {}).get(pid)
            lines.append(f"R{rnd}: dealt {deal}")
            for a in acts:
                lines.append(f"    {a}")
            lines.append(f"    -> rolls spent {rolls}; banked at round end: "
                         f"{rr if rr is not None else '?'}")
        return "\n".join(lines)

    def t_board_db(self, round: int, window: int = 1, name: str = None,
                   limit: int = 20) -> str:
        """Boards fielded around a round across ALL past games."""
        import boards_db as BD
        who = name or self.name
        rows = BD.query(int(round), int(window), who, int(limit))
        if not rows:
            return (f"no boards for {who} near R{round} in the DB "
                    f"(try name='any')")
        out = [f"past boards near R{round} ({who}):"]
        for r in rows:
            out.append(f"  g{r['game']} R{r['round']} 境{r['realm']} "
                       f"修为{r['cult']} [{r['result']}]:")
            out.append(f"    {', '.join(r['board'])}")
        return "\n".join(out)

    def t_card_stats(self, round: int) -> str:
        """Per-card contribution in YOUR battle that round, parsed from the
        real log: plays, damage dealt, resources generated, hp spent."""
        me = f"{self.name}(pid{self.pid})"
        for rnd_results in self.game.battle_results:
            for r in rnd_results:
                if r.get("round") == int(round) and self.pid in (r["a"], r["b"]):
                    return self._card_contrib(r["log"], me)
        return f"(no battle of yours found in round {round})"

    @staticmethod
    def _card_contrib(log: str, me: str) -> str:
        stats, cur = {}, None
        res_pat = re.compile(r"gained (\d+) (qi|force|star_power|sword_intent|"
                             r"def|max_hp|physique|agility|hexagram)\b")
        for line in log.splitlines():
            s = line.strip()
            m = re.match(rf"{re.escape(me)} (?:is playing|spent (\d+) (hp|qi) "
                         rf"to play) (.+?) \(level (\d+)\)", s)
            if m:
                cur = f"{m.group(3)} lv{m.group(4)}"
                d = stats.setdefault(cur, {"plays": 0, "dmg": 0, "hp_spent": 0,
                                           "qi_spent": 0, "res": {}})
                d["plays"] += 1
                if m.group(1):
                    d[f"{m.group(2)}_spent"] += int(m.group(1))
                continue
            if cur is None:
                continue
            if s.startswith(f"{me} finished playing"):
                cur = None
                continue
            if "Spent 10 agility to chase" in s or s == "chase!!":
                d = stats[cur]
                d["res"]["extra_actions"] = d["res"].get("extra_actions", 0) + 1
                continue
            m = re.search(r"reduced (?!" + re.escape(me) + r")\S+ hp by (\d+)", s)
            if m:
                stats[cur]["dmg"] += int(m.group(1))
            m = res_pat.search(s)
            if m:
                d = stats[cur]["res"]
                d[m.group(2)] = d.get(m.group(2), 0) + int(m.group(1))
        if not stats:
            return "(none of your card plays found in that log)"
        out = ["your per-card contribution that battle:"]
        for c, d in stats.items():
            res = ", ".join(f"+{v} {k}" for k, v in d["res"].items())
            cost = (f"; spent {d['hp_spent']}hp" if d["hp_spent"] else "") + \
                   (f"; spent {d['qi_spent']}qi" if d["qi_spent"] else "")
            out.append(f"  {c}: {d['plays']}x, {d['dmg']} dmg"
                       + (f", {res}" if res else "") + cost)
        return "\n".join(out)

    def t_pool_cards(self, career: int = None) -> str:
        p = self.p
        if career:
            pool = D.sidejob_pool(int(career))
            head = f"sidejob {career} pool:"
        else:
            return self._live_deck()
        by_ph = {}
        for n, d in pool.items():
            by_ph.setdefault(d["phase"], []).append(
                f"{n}×{d['copies']} — {_desc_for(n)[:60]}")
        lines = [head]
        for ph in sorted(by_ph):
            lines.append(f"境{ph}:")
            lines.extend(f"  {s}" for s in sorted(by_ph[ph]))
        return "\n".join(lines)

    def _live_deck(self) -> str:
        """Your ACTUAL remaining deck (after draws and roll burns), with the
        chance each card comes up on your next roll / deal draw."""
        p, bag = self.p, self.p.bag
        side = bag.sidejob
        reach = p.realm
        live = {n: c for n, c in bag.copies.items() if c > 0}
        elig = {n: c for n, c in live.items() if bag.phase.get(n, 1) <= reach}
        tot = sum(elig.values()) or 1
        sect_tot = sum(c for n, c in elig.items() if n not in side) or 1
        side_tot = sum(c for n, c in elig.items() if n in side) or 1
        lines = [f"YOUR LIVE DECK (境{reach}; {tot} drawable copies left: "
                 f"{tot - (side_tot if side else 0)} sect, "
                 f"{side_tot if side else 0} sidejob). Odds = chance per ROLL "
                 f"(whole deck) / per DEAL draw (its own sect-or-sidejob "
                 f"pool):"]
        by_ph = {}
        for n, c in live.items():
            ph = bag.phase.get(n, 1)
            if ph <= reach:
                sub = side_tot if n in side else sect_tot
                tag = (f"{c} left, {100 * c / tot:.1f}%/roll, "
                       f"{100 * c / sub:.1f}%/deal")
            else:
                tag = f"{c} left, LOCKED until 境{ph}"
            kind = "sidejob" if n in side else "sect"
            by_ph.setdefault(ph, []).append(
                f"{n} [{kind}] — {tag} — {_desc_for(n)[:50]}")
        for ph in sorted(by_ph):
            lines.append(f"境{ph}:")
            lines.extend(f"  {s}" for s in sorted(by_ph[ph]))
        return "\n".join(lines)

    def _peer_dir(self, name):
        """Cross-bot state access — POST-GAME REVIEW ONLY (open-review rule
        2026-09-26: in-game strategy stays private; in review everything is
        open to everyone, symmetrically)."""
        if not name or name == self.name:
            return self.dir, None
        if not self.reflection:
            return None, ("rival files are private DURING the game — "
                          "open only in post-game review")
        d = (REVIEW_SNAPSHOT or STATE_DIR) / name
        if not d.exists():
            return None, f"no such bot {name!r}"
        return d, None

    def t_notebook(self, name: str = None) -> str:
        d, err = self._peer_dir(name)
        return err or (d / "notebook.md").read_text(encoding="utf-8")

    def t_append_ledger(self, entry: str) -> str:
        """Append this game's permanent record; never rewritten."""
        if not self.reflection:
            return ("ACTION REFUSED: the ledger is written once per game, in "
                    "the post-game review. For in-game notes use "
                    "write_notebook.")
        g = getattr(self, "game_no", None)
        head = f"\n{LEDGER_MARK} Game {g if g is not None else '?'} ====\n"
        with open(self.dir / "ledger.md", "a", encoding="utf-8") as f:
            f.write(head + entry.strip() + "\n")
        return f"ledger entry appended ({len(entry)} chars)"

    def t_ledger(self, last_n: int = 3, name: str = None) -> str:
        """Read last N ledger entries (yours, or any bot's in review)."""
        d, err = self._peer_dir(name)
        if err:
            return err
        text = (d / "ledger.md").read_text(encoding="utf-8")
        # split ONLY on the harness marker — bots write their own "## ..."
        # headings inside entries, which used to fake entry boundaries
        parts = text.split("\n" + LEDGER_MARK)
        if len(parts) <= 1:
            return "(ledger empty — no past games recorded yet)"
        n = max(1, int(last_n))
        return ("\n" + LEDGER_MARK).join([parts[0].strip()] + parts[-n:])

    def t_write_notebook(self, content: str) -> str:
        (self.dir / "notebook.md").write_text(content, encoding="utf-8")
        return f"notebook saved ({len(content)} chars)"

    def t_list_programs(self) -> str:
        progs = sorted((self.dir / "programs").glob("*.py"))
        return "\n".join(f.name for f in progs) or "(no programs yet)"

    def t_read_program(self, name: str) -> str:
        f = self.dir / "programs" / Path(name).name
        return f.read_text(encoding="utf-8") if f.exists() else "(not found)"

    def t_save_program(self, name: str, code: str) -> str:
        f = self.dir / "programs" / Path(name).name
        f.write_text(code, encoding="utf-8")
        return f"saved {f.name} ({len(code)} chars) — will be audited by the referee"

    def t_run_program(self, name: str, args: list = None) -> str:
        f = self.dir / "programs" / Path(name).name
        if not f.exists():
            return "(program not found)"
        try:
            import os
            env = dict(os.environ)
            env["YISIM_DIR"] = str(YB.YISIM_DIR)   # sanctioned yisim source access
            proc = subprocess.run([sys.executable, str(f)] + [str(a) for a in args or []],
                                  capture_output=True, cwd=str(self.dir),
                                  timeout=PROGRAM_TIMEOUT, env=env)
            out = proc.stdout.decode("utf-8", "replace")[-4000:]
            err = proc.stderr.decode("utf-8", "replace")[-1000:]
            return out + (("\nSTDERR:\n" + err) if err.strip() else "")
        except subprocess.TimeoutExpired:
            return f"(timed out after {PROGRAM_TIMEOUT}s)"

    # actions
    def _act(self, fn, *a):
        try:
            msg = fn(self.p, *a)
            self.turn_log.append(msg)
            p = self.p
            status = (f"[命{p.destiny} 修为{p.cultivation} 境{p.realm} "
                      f"体魄{p.tipo}/{p.max_tipo} 换牌{p.rerolls} | "
                      f"board {[ENG.nm(c) for c in p.board if c]} | "
                      f"hand {[ENG.nm(c) for c in p.hand]}]")
            return msg + "\n" + status
        except Exception as e:
            return f"ACTION REFUSED: {e}"

    def t_roll(self, card: str) -> str: return self._act(self.game.act_roll, card)
    def t_absorb(self, card: str) -> str: return self._act(self.game.act_absorb, card)
    def t_merge(self, card: str) -> str: return self._act(self.game.act_merge, card)
    def t_take(self, card: str) -> str: return self._act(self.game.act_take, card)
    def t_set_board(self, cards: list) -> str: return self._act(self.game.act_board, cards)

    def t_peek_breakthrough(self) -> str:
        if self.p.realm >= E.MAX_REALM:
            return "already at 境5 — the max realm; no further breakthroughs"
        try:
            shown = self.game.peek_fates(self.p)
            return _fate_offer_text(shown)
        except Exception as e:
            return f"peek failed: {e}"

    def t_breakthrough(self, fate_ranking: list) -> str:
        return self._act(lambda p, r: self.game.act_breakthrough(p, r), fate_ranking)

    def t_choose_sidejob(self, career: int) -> str:
        if self.game.env.state.round != E.SIDEJOB_ROUND:
            return "ACTION REFUSED: sidejob is chosen at round 2 only"
        if self.pid in self.game.sidejobs or self.p.career:
            return f"ACTION REFUSED: sidejob already set ({self.p.career})"
        c = int(career)
        if not 1 <= c <= 7:
            return "ACTION REFUSED: career must be 1..7"
        self.game.sidejobs[self.pid] = c
        self.p.career = c
        self.p.bag.add_cards(D.sidejob_pool(c), as_sidejob=True)
        self.turn_log.append(f"sidejob -> {c}")
        return f"sidejob set to {c}; its cards joined your draw pool"

    def t_end_turn(self, summary: str = "") -> str:
        self.ended = True
        self.end_summary = summary
        return "turn ended"


# ── LLM driver (DeepSeek, OpenAI-compatible function calling) ────────────────

DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
MAX_TOOL_RESULT = 12000       # chars per tool result kept in context
API_TIMEOUT = 180             # seconds per completion request

def _s(desc, **props):
    """Small helper: OpenAI function schema with all props required unless
    they carry a ('optional', schema) marker."""
    required = [k for k, v in props.items() if not (isinstance(v, tuple))]
    properties = {k: (v[1] if isinstance(v, tuple) else v) for k, v in props.items()}
    return {"description": desc,
            "parameters": {"type": "object", "properties": properties,
                           "required": required}}

_STR = {"type": "string"}
_INT = {"type": "integer"}
_BOOL = {"type": "boolean"}
_STRS = {"type": "array", "items": {"type": "string"}}
_INTS = {"type": "array", "items": {"type": "integer"}}

TOOL_DEFS = {
    "get_observation": _s("Refresh your current view of the game (your state + "
                          "opponents' last-round state)."),
    "card_text": _s("Full rules text (CN+EN, all levels) for the named cards.",
                    names=_STRS),
    "yisim_grep": _s("Search the yisim battle-engine source (gamestate_full.js "
                     "etc.) to learn EXACT mechanics.", pattern=_STR),
    "economy_history": _s("Per-round economy record this game: cards dealt, "
                          "every roll/absorb/merge, rolls banked per round. "
                          "Yours by default; in POST-GAME REVIEW pass a "
                          "rival's name to study THEIR economy. Audit: "
                          "over-rolling into junk, under-rolling for engine "
                          "pieces, grants wasted at the 25 cap.",
                          name=("optional", _STR)),
    "board_db": _s("Database of boards fielded in ALL past games, filtered "
                   "near a round (similar power level). Defaults to your own "
                   "character's boards; name='any' or a rival's name for "
                   "theirs. Each row shows game, round, realm, 修为 and that "
                   "round's battle result — sim promising ones as candidate "
                   "starts or search_board seeds.",
                   round=_INT, window=("optional", _INT),
                   name=("optional", _STR), limit=("optional", _INT)),
    "card_stats": _s("Per-card contribution in YOUR battle of a given round, "
                     "parsed from the real log: times played, damage dealt, "
                     "resources generated (qi/force/star/sword/def/maxhp), "
                     "hp/qi spent. Use it to judge what each board slot "
                     "actually provides and which slots underperform.",
                     round=_INT),
    "pool_cards": _s("Your LIVE deck: every card with copies left (after "
                     "draws and roll burns), grouped by phase, with the "
                     "chance it comes up on your next roll and next deal "
                     "draw; cards above your realm show as LOCKED. Pass "
                     "career 1-7 to browse another sidejob's full pool "
                     "instead — e.g. to evaluate a different R2 pick.",
                     career=("optional", _INT)),
    "sim_matchup": _s("ONE call = the full check: your candidate board vs the "
                      "named opponent, both seats, at their last-known board "
                      "AND a +1-level upgrade of it, N repeats each. Use this "
                      "before committing a board instead of many simulate calls.",
                      my_cards=_STRS, opp_pid=_INT,
                      repeats=("optional", _INT)),
    "battle_log": _s("The ACTUAL turn-by-turn yisim log of a round's "
                     "battle(s), with real player names, per-turn STATE "
                     "lines and hands. During the game: your own battles "
                     "only. In POST-GAME REVIEW: ALL battles of that round, "
                     "including fights you were not in — study how rivals "
                     "beat each other.", round=_INT),
    "search_board": _s("POST-GAME REVIEW ONLY. Automated hill-climb board "
                       "search: you steer, the script grinds (token-free). "
                       "Searches composition + ORDER + levels from your pools. "
                       "start = starting board (any cards); pool_careers = "
                       "extra sidejob pools 1-7 to draw candidates from; "
                       "lock_slots = {\"0\": \"天元心法\"} pins a card AT a "
                       "position; lock_cards = [names] must be on the board "
                       "but may move; objective = both|first|second|fast; "
                       "ENGINES: it explores with the game's own combat code "
                       "(fast), then yisim — the engine that resolves your "
                       "real battles — re-ranks the finalists, and yisim's "
                       "verdict is what you get. "
                       "evals ≤400 per call, review budget 4000 total — a "
                       "CONSTRAINED search converges, an unconstrained one "
                       "wastes your budget. Returns the best board found and "
                       "the trace of accepted improvements (read the trace: "
                       "it tells you WHY).",
                       opp_pid=_INT, start=_STRS,
                       pool_careers=("optional", _INTS),
                       lock_slots=("optional", {"type": "object"}),
                       lock_cards=("optional", _STRS),
                       objective=("optional", _STR),
                       evals=("optional", _INT),
                       opp_cards=("optional", _STRS)),
    "simulate": _s("Exact battle sim via yisim. Uses live stats for you, "
                   "last-known stats for the opponent. my_cards = your candidate "
                   "board in cyclic order (names from your hand/board; during "
                   "POST-GAME REVIEW any card names are allowed, so you can "
                   "theorycraft boards from pool_cards you never drew); opp_cards "
                   "optionally overrides the opponent board; i_go_first overrides "
                   "seating (default: by cultivation); full_log = whole turn log.",
                   my_cards=_STRS, opp_pid=_INT,
                   opp_cards=("optional", _STRS),
                   i_go_first=("optional", _BOOL),
                   full_log=("optional", _BOOL),
                   my_extra_fates=("optional", _INTS)),
    "notebook": _s("Read a strategy PLAYBOOK — yours by default; in "
                   "POST-GAME REVIEW pass a rival's name (牧逸风/谭舒雁/"
                   "吾行之/小布) to read THEIRS (open-review rule: after the "
                   "game everything is public, symmetrically — they read "
                   "yours too).", name=("optional", _STR)),
    "append_ledger": _s("Append this game's entry to your permanent LEDGER — "
                        "an append-only per-game archive that is NEVER "
                        "rewritten or trimmed. Write what future-you needs "
                        "about THIS game: result, sidejob/fates, final board "
                        "with levels, per-rival outcomes with causes, top "
                        "discovery with evidence, economy stats, surprises. "
                        "No length limit.", entry=_STR),
    "ledger": _s("Read last N ledger entries — the permanent per-game "
                 "archive. Yours by default; in POST-GAME REVIEW pass a "
                 "rival's name to read theirs (open-review rule).",
                 last_n=("optional", _INT), name=("optional", _STR)),
    "write_notebook": _s("Overwrite your persistent notebook.", content=_STR),
    "list_programs": _s("List helper programs you saved in previous games."),
    "read_program": _s("Read one of your saved programs.", name=_STR),
    "save_program": _s("Save a Python helper program for future games "
                       "(audited by the referee). name must end in .py. "
                       "SANDBOX RULE: programs run with cwd = your own directory "
                       "and may only touch files there, plus read the yisim "
                       "source via os.environ['YISIM_DIR']. Touching any other "
                       "path (drive crawling, other bots' dirs, the harness) is "
                       "foul play and the referee deletes the program.",
                       name=_STR, code=_STR),
    "run_program": _s("Run one of your saved programs (subprocess, 30s timeout).",
                      name=_STR, args=("optional", _STRS)),
    "roll": _s("Exchange a hand card for a random new one (costs 1 exchange). "
               "card e.g. \"剑劈\" or \"剑劈+1\".", card=_STR),
    "absorb": _s("Absorb a card for +1 cultivation ([炼化] effects fire).",
                 card=_STR),
    "merge": _s("Merge two identical hand copies into a +1 level copy "
                "(+1 cultivation).", card=_STR),
    "take": _s("Take a board card back into hand.", card=_STR),
    "set_board": _s("Field your board in cyclic order (replaces the whole board).",
                    cards=_STRS),
    "peek_breakthrough": _s("Preview the fate offers a breakthrough right now "
                            "would produce (no commitment)."),
    "breakthrough": _s("Break through realm gate(s) now; fate_ranking picks from "
                       "each gate's offer (fate ids, most preferred first).",
                       fate_ranking=_INTS),
    "choose_sidejob": _s("ROUND 2 ONLY: choose your sidejob for the whole game. "
                         "1=炼丹师 2=符咒师 3=琴师 4=画师 5=阵法师 6=灵植师 7=命理师.",
                         career=_INT),
    "end_turn": _s("Finish your turn. Give a one-line summary of your plan.",
                   summary=("optional", _STR)),
}

TOOLS_PAYLOAD = [{"type": "function",
                  "function": {"name": n, **d}} for n, d in TOOL_DEFS.items()]


def _dispatch(seat: BotSeat, name: str, args: dict) -> str:
    fn = getattr(seat, "t_" + name, None)
    if fn is None:
        return f"unknown tool {name!r}"
    if seat.reflection:           # measure how reviews are spent (incl.
        who = args.get("name")    # open-review reads of rival files)
        seat.game.log(f"  [review pid{seat.pid}] {name}"
                      + (f"(name={who})" if who else "")
                      + (f"(round={args['round']})" if "round" in args else ""))
    try:
        return str(fn(**args))
    except TypeError as e:
        return f"BAD ARGUMENTS for {name}: {e}"
    except Exception as e:
        return f"TOOL ERROR in {name}: {e!r}\n{traceback.format_exc(limit=2)}"


def _chat(api_key: str, model: str, messages: list) -> dict:
    import requests
    import time as _t
    body = {"model": model, "messages": messages, "tools": TOOLS_PAYLOAD,
            "tool_choice": "auto", "max_tokens": 8192}
    for attempt in range(4):
        try:
            resp = requests.post(
                DEEPSEEK_URL, json=body, timeout=API_TIMEOUT,
                headers={"Authorization": f"Bearer {api_key}",
                         "Content-Type": "application/json"})
        except requests.RequestException as e:
            if attempt == 3:
                raise
            _t.sleep(5 * (attempt + 1))
            continue
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (429, 500, 503) and attempt < 3:
            _t.sleep(10 * (attempt + 1))
            continue
        if resp.status_code == 402:          # out of API money: never forfeit
            raise InsufficientBalance(resp.text[:200])   # turns silently
        raise RuntimeError(f"DeepSeek HTTP {resp.status_code}: {resp.text[:400]}")
    raise RuntimeError("DeepSeek: retries exhausted")


def run_llm_turn(seat: BotSeat, model: str, phase_prompt: str,
                 api_key: str = None, max_turns: int = None) -> None:
    """One function-calling conversation for one bot-round (or post-game phase).
    DeepSeek OpenAI-compatible endpoint; one API key per seat."""
    if not api_key:
        raise RuntimeError("no api_key for this seat")
    messages = [{"role": "system", "content": RULES},
                {"role": "user", "content": phase_prompt}]
    nudges = 0
    for _ in range(max_turns or MAX_TOOL_TURNS):
        data = _chat(api_key, model, messages)
        msg = data["choices"][0]["message"]
        # keep the assistant message verbatim (tool_calls included)
        messages.append({k: v for k, v in msg.items()
                         if k in ("role", "content", "tool_calls") and v is not None})
        calls = msg.get("tool_calls") or []
        if not calls:
            if seat.ended:
                return
            nudges += 1
            if nudges > 2:
                return                      # gave up without end_turn; forfeit
            messages.append({"role": "user", "content":
                             "You must act through tool calls. Call end_turn "
                             "when you are done."})
            continue
        for call in calls:
            fname = call.get("function", {}).get("name", "")
            try:
                args = json.loads(call.get("function", {}).get("arguments") or "{}")
                if not isinstance(args, dict):
                    raise ValueError("arguments not an object")
            except Exception as e:
                result = f"COULD NOT PARSE ARGUMENTS: {e}"
            else:
                result = _dispatch(seat, fname, args)
            messages.append({"role": "tool", "tool_call_id": call.get("id"),
                             "content": result[:MAX_TOOL_RESULT]})
        if seat.ended:
            return


# ── scripted stub (keyless smoke tests) ──────────────────────────────────────

def run_stub_turn(seat: BotSeat, model=None, phase_prompt="", api_key=None) -> None:
    """Minimal legal policy: R2 pick a sidejob, keep hand attackers on board,
    absorb one junk card late, breakthrough when possible, end."""
    g, p = seat.game, seat.p
    rnd = g.env.state.round
    if rnd == E.SIDEJOB_ROUND and seat.pid not in g.sidejobs:
        seat.t_choose_sidejob(1 + (seat.pid % 7))
    try:
        seat.t_breakthrough([])
    except Exception:
        pass
    avail = [c for c in p.board if c] + list(p.hand)
    avail = [c for c in avail if YB.combat_ok(c)]
    slots = E.unlocked_slots(rnd)
    picked, lim = [], 0
    for c in avail:
        if YB.limited_kw(c):
            if lim >= 2:
                continue
            lim += 1
        picked.append(c)
        if len(picked) == slots:
            break
    board = [ENG.nm(c) for c in picked]
    if board:
        seat.t_set_board(board)
    if rnd >= 3 and p.hand:
        seat.t_absorb(ENG.nm(p.hand[0]))
    seat.t_end_turn("stub policy")
