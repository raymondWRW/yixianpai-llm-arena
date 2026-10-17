# -*- coding: utf-8 -*-
"""Run one arena game: 4 LLM bots, full game, notebooks + programs persist.

    python run_arena.py --game 1 --seed 201 [--stub] [--model claude-opus-5]

--stub plays the whole game with a scripted keyless policy (harness smoke test).
Artifacts land in arena/games/gameN/: game_log.txt, battles/, result.json,
referee.md. Bot persistent state lives in arena/bots_state/<name>/.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

import bots as B
import engine as ENG
import referee as REF

GAMES_DIR = _HERE / "games"


PEAK_OK = False           # set from --peak-ok / --stub in main()


def hold_for_offpeak(game=None) -> None:
    """Called before EVERY bot turn and review: if DeepSeek peak pricing has
    started, pause here until it ends. A game spans ~1.5-2h, so a launch-time
    check alone lets later rounds run at full price. Pausing between turns is
    safe — each turn is its own fresh API conversation."""
    if PEAK_OK:
        return
    wait = offpeak_wait_seconds()
    if not wait:
        return
    import datetime as dt
    resume = dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=wait)
    msg = (f"[offpeak] peak pricing started — pausing {wait // 60} min, "
           f"resuming {resume:%H:%M} UTC")
    print(msg, flush=True)
    if game is not None:
        game.log(msg)
    time.sleep(wait)


def offpeak_wait_seconds(now=None) -> int:
    """DeepSeek pricing (verified 2026-09-26): PEAK = 01:00-04:00 and
    06:00-10:00 UTC, Mon-Fri; all other hours AND full weekends are
    off-peak at HALF price. Games only run off-peak (user directive).
    Chinese public holidays (also off-peak) aren't modeled — worst case we
    wait when we didn't need to, never the reverse. Returns seconds until
    off-peak (0 = already off-peak)."""
    import datetime as dt
    now = now or dt.datetime.now(dt.timezone.utc)
    if now.weekday() >= 5:                      # Sat/Sun: fully off-peak
        return 0
    t = now.hour + now.minute / 60.0
    if 1 <= t < 4:
        target = now.replace(hour=4, minute=0, second=0, microsecond=0)
    elif 6 <= t < 10:
        target = now.replace(hour=10, minute=0, second=0, microsecond=0)
    else:
        return 0
    return int((target - now).total_seconds()) + 60


def matchup_matrix(game) -> str:
    """Post-game baseline: every pair of final boards, both seats,
    base/base and +1/+1, 3 reps — one warm batch, ~2s, zero LLM tokens."""
    import itertools

    import fate_map as FM
    import search as SBS
    import yisim_bridge as YB

    def pay(q, ids):
        extra = FM.combat_fields(q.talents,
                                 getattr(q, "talent_phases", {}) or {},
                                 game.consumed_avatars.get(q.pid, ()))
        return YB.player_payload(q.char_id, q.cultivation, q.battle_hp,
                                 q.destiny, ids, q.tipo, q.max_tipo,
                                 round_number=game.env.state.round, extra=extra)

    ps = [q for q in game.env.state.players if any(q.board)]
    base = {q.pid: [c for c in q.board if c] for q in ps}
    up = {pid: [SBS._level_variant(c, 1) or c for c in ids]
          for pid, ids in base.items()}
    k = 3
    battles, rows = [], []
    for qa, qb in itertools.combinations(ps, 2):
        for cfg, ida, idb in (("base/base", base[qa.pid], base[qb.pid]),
                              ("+1/+1", up[qa.pid], up[qb.pid])):
            A, B = pay(qa, ida), pay(qb, idb)
            for _ in range(k):
                battles.append((A, B, True))
                battles.append((B, A, True))
            rows.append((qa, qb, cfg))
    try:
        res = YB.run_battles(battles)
    except Exception as e:
        return f"(matchup matrix unavailable: {e})"
    lines = ["MATCHUP MATRIX — final boards, win% over 3 sims each config:",
             "boards:"]
    for q in ps:
        lines.append(f"  {ENG.NAMES[q.char_id]} (pid{q.pid}): "
                     f"{[ENG.nm(c) for c in base[q.pid]]}")
    i = 0
    for qa, qb, cfg in rows:
        wa_first = wa_second = 0
        for _ in range(k):
            r1, r2 = res[i], res[i + 1]
            i += 2
            wa_first += r1.get("winner") == "a"
            wa_second += r2.get("winner") == "b"
        na, nb = ENG.NAMES[qa.char_id], ENG.NAMES[qb.char_id]
        lines.append(f"  {na} vs {nb} [{cfg}]: {na} wins "
                     f"{100*wa_first//k}% going first, "
                     f"{100*wa_second//k}% going second")
    return "\n".join(lines)


def run_reflections(game, seats, keys, model, winner):
    """Post-game review conversations (shared by run_arena and
    review_replay). Rewrites notebooks; context wiped afterwards."""
    B.snapshot_for_review()
    game.log("rival files frozen for review (all bots read the same versions)")
    matrix = matchup_matrix(game)
    game.log("matchup matrix computed for review prompts")
    # Bots used to infer the outcome from a stale start-of-round snapshot and
    # wrote the WRONG winner into permanent ledgers (g19). State it outright.
    ranked = sorted(game.env.state.players,
                    key=lambda q: (q.alive, q.destiny), reverse=True)
    standings_txt = ("FINAL STANDINGS (authoritative — the observation "
                     "snapshot is from the START of the last round and is "
                     "stale): " + "; ".join(
                         f"{ENG.NAMES[q.char_id]} (pid{q.pid}) "
                         + ("WINNER, " if q.pid in getattr(game, 'co_winners', [])
                            and q.alive else
                            ("alive, " if q.alive else "eliminated, "))
                         + f"命{q.destiny}" for q in ranked))
    game_no = getattr(next(iter(seats.values())), "game_no", None)
    for pid, seat in seats.items():
        hist = []
        for rnd_results in game.battle_results:
            for r in rnd_results:
                if pid in (r["a"], r["b"]):
                    hist.append(f"R{r['round']}: vs pid{r['b'] if r['a']==pid else r['a']} "
                                f"{'WON' if r['winner']==pid else 'LOST'} "
                                f"(-{r['destiny_loss']}命 to loser, {r['turns']} turns)")
        seat.ended = False
        seat.reflection = True
        prompt = (
            (f"This was ARENA GAME {game_no} — use that number in your "
             f"ledger.\n" if game_no is not None else "")
            + standings_txt + "\n\n"
            f"The game is over. You placed "
            + ("TIED for 1st (equal 命)"
               if len(getattr(game, "co_winners", [])) > 1
               and pid in game.co_winners else
               ("1st (WINNER)" if winner.pid == pid else "not first")) + " — "
            + f"final 命 {seat.p.destiny}.\n\nYour battles:\n"
            + "\n".join(hist) + "\n\n" + matrix + "\n\n"
            "This is your post-game review. You have plenty of turns and "
            "a search budget of 4000 evaluations (≤400 per search_board "
            "call — spend ~half broadly and concentrate the rest on your "
            "single hardest matchup). In review, simulate()/sim_matchup() "
            "accept ANY cards "
            "on your side. Work the phases IN ORDER; RNG cards make "
            "single sims lie — trust win rates.\n\n"
            "PHASE 1 — UNDERSTAND THE FIGHTS. For each battle that "
            "decided your fate, battle_log(round) and trace it turn by "
            "turn: what triggered what, where the damage actually came "
            "from, which enemy card did the work. List the key "
            "interactions — your Phase-4 constraints must cite them.\n"
            "REACHABILITY RULE for any 'I should have merged/upgraded' "
            "claim: merging needs TWO IDENTICAL-LEVEL copies (lv1+lv1->"
            "lv2, lv2+lv2->lv3, so a lv3 costs FOUR lv1 copies). Count "
            "the copies you actually held before writing the lesson, and "
            "sim the fix against the opponent's EXACT final board, 3+ "
            "reps.\n"
            "PHASE 1b — CARD AUDIT. card_stats(round) on your decisive "
            "battles: for each board slot, what did it actually provide "
            "(dmg / qi / force / star / def per the numbers) and WHICH "
            "card consumed those resources? Flag low-contribution slots, "
            "then test replacements via single-slot search_board or "
            "sim_matchup swaps.\n"
            "PHASE 1c — ROLL AUDIT. economy_history(): count your rolls "
            "per round and what they hit. Name the rounds you OVER-rolled "
            "(junk hits, grants wasted at the 25 cap) and UNDER-rolled "
            "(engine pieces you never found). Write next-game roll "
            "targets: which rounds to spend heavy hunting which key "
            "cards, and which rounds to bank.\n"
            "PHASE 1.5 — OPEN INTELLIGENCE. In review (and ONLY in review) "
            "everything is public, symmetrically: notebook(name=...), "
            "ledger(name=...), economy_history(name=...) work for every "
            "rival, and battle_log(round) returns ALL battles including "
            "fights you were not in. At minimum: read the WINNER's playbook "
            "and latest ledger entry, watch one fight between two rivals "
            "that mattered, and study the winner's economy curve. Steal "
            "what works; note that rivals are reading your notes too. Rival "
            "files are FROZEN as they stood when the game ended — every bot "
            "sees the same versions, and nobody sees what a rival writes "
            "during this review.\n"
            "PHASE 2 — AUDIT YOUR PLAYBOOK. notebook() and ledger(3), then "
            "re-test every testable claim (sim / yisim_grep / card_text) and "
            "KEEP what passes — a rule that keeps surviving audits is your "
            "most valuable possession. Delete only what demonstrably failed, "
            "citing the failing test.\n"
            "PHASE 3 — READ THE MATRIX above (precomputed — do NOT "
            "rebuild it). Note where you stand vs every rival, both "
            "seats, now and if everyone upgrades.\n"
            "PHASE 4 — SEARCH. board_db(round=N) first: it holds every "
            "board fielded near that round across ALL past games (yours "
            "and, with name='any', your rivals') with results — sim the "
            "promising ones and use the best as search seeds. Then "
            "search_board() per rival that beats you: "
            "pick the start board, LOCK what Phase 1 says is "
            "load-bearing (lock_slots pins a position, lock_cards keeps "
            "a card but lets it move), choose pools (try at least one "
            "search drawing from a DIFFERENT career 1-7), choose the "
            "objective. A CONSTRAINED search converges; an "
            "unconstrained one wastes budget. Read each TRACE — it says "
            "WHY boards improved. Verify the final board once with "
            "simulate(full_log=true) and read HOW it wins.\n"
            "PHASE 5 — MECHANICS. For the 6-10 cards your plan now "
            "depends on, verify exact behavior (card_text / yisim_grep) "
            "and note interactions/order dependencies.\n"
            "PHASE 6 — DECIDE NEXT GAME. R2 sidejob (pool_cards across "
            "careers); round schedule (R1-R6 opening, breakthrough "
            "timing vs 命 risk, 修为 pacing); one decision rule per "
            "rival for when they are your announced opponent. Also write "
            "a 天命 PRIORITY LIST per gate: A/B-test your character's "
            "传承/combat fates with simulate(my_extra_fates=[id]) — they "
            "apply in real battles — and rank them vs the generic economy "
            "fates so next-game-you passes a ranking to breakthrough() "
            "instead of taking the default.\n"
            "PHASE 7a — LEDGER. append_ledger() ONE entry for this game — "
            "your permanent, never-rewritten archive. Include: result & "
            "placement · sidejob & fates picked · final board with levels · "
            "per-rival W/L with one-line causes · your top discovery this "
            "game WITH its evidence · roll/economy numbers worth remembering "
            "· anything that surprised you. As detailed as you like; "
            "future-you reads it with ledger().\n"
            "PHASE 7b — PLAYBOOK. write_notebook() by MERGING, not from "
            "scratch: start from the previous playbook, carry forward every "
            "rule that passed the Phase-2 audit, integrate this game's "
            "findings. Deleting a rule requires citing what disproved it; "
            "superseding one requires naming its replacement. Rules that "
            "have held for 3+ games go in a CORE PRINCIPLES section at the "
            "top, tagged with their games (e.g. g6,g9,g12). NO length limit "
            "— write the most detailed playbook you would want to receive "
            "with your memory wiped; tag entries with evidence (win%, reps, "
            "source line) or GUESS. Suggested sections: CORE PRINCIPLES · "
            "MATCHUPS · RECIPES (slot-by-slot with WHY) · MECHANICS · "
            "SCHEDULE/ROLLS · FATES · MISTAKES+FIXES. Optionally "
            "save_program(). Then end_turn with a one-line lesson.")
        hold_for_offpeak(game)
        try:
            B.run_llm_turn(seat, model=model, phase_prompt=prompt,
                           api_key=keys.get(pid), max_turns=300)
        except B.InsufficientBalance:
            raise
        except Exception as e:
            game.log(f"  pid{pid} reflection crashed: {e!r}")



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", type=int, required=True)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--model", default="deepseek-chat")
    ap.add_argument("--stub", action="store_true",
                    help="scripted keyless bots (harness smoke test)")
    ap.add_argument("--peak-ok", action="store_true",
                    help="override the off-peak-only guard (full price!)")
    a = ap.parse_args()
    if sys.platform == "win32":
        # Keep the PC awake for the whole run: an idle sleep hangs the
        # in-flight DeepSeek call and there is no checkpoint (game 16 lost
        # at R18, 2026-09-26). Released automatically when the process exits.
        # Does NOT stop lid-close, manual sleep, or power loss.
        import ctypes
        ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
    global PEAK_OK
    PEAK_OK = bool(a.stub or a.peak_ok)
    if not a.stub and not a.peak_ok:
        wait = offpeak_wait_seconds()
        if wait:
            import datetime as dt
            resume = dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=wait)
            print(f"[offpeak] peak-rate hours (UTC) — waiting {wait//60} min, "
                  f"starting at {resume:%H:%M} UTC (use --peak-ok to override)",
                  flush=True)
            time.sleep(wait)
    seed = a.seed if a.seed is not None else 200 + a.game

    gdir = GAMES_DIR / f"game{a.game}"
    (gdir / "battles").mkdir(parents=True, exist_ok=True)

    game = ENG.ArenaGame(seed=seed)
    seats = {pid: B.BotSeat(game, pid) for pid in range(4)}
    for s in seats.values():
        s.game_no = a.game
    turn_fn = B.run_stub_turn if a.stub else B.run_llm_turn
    keys = {}
    if not a.stub:
        keys = {int(k): v for k, v in json.loads(
            (_HERE / "deepseek_keys.json").read_text(encoding="utf-8")).items()}
    game.log(f"ARENA GAME {a.game} seed={seed} model={'stub' if a.stub else a.model}")
    global _CURRENT
    _CURRENT = (game, gdir, a, seed)

    while not game.game_over():
        game.begin_round()
        rnd = game.env.state.round
        # act in random seat order each round (no positional advantage)
        order = [p.pid for p in game.env.state.alive_players()]
        game.env.state.rng.shuffle(order)
        for pid in order:
            seat = seats[pid]
            if not seat.p.alive:
                continue
            seat.ended = False
            seat.turn_log = []
            prompt = (
                f"Round {rnd} begins. Play your turn.\n\n"
                f"{seat.observation()}\n\n"
                "Three passes:\n"
                "1. READ: the SITREP and CARD REFERENCE above are computed "
                "for you. State only your read of the opponent's likely "
                "upgrade since their last board, and your win condition this "
                "round.\n"
                "2. EXECUTE THE PLAN: notebook() — find the sections covering "
                "THIS turn (recipe, the COUNTER for your announced opponent, "
                "the round schedule). Do the economy it prescribes "
                "(merge/absorb/roll), then the board. sim_matchup() the "
                "planned board before committing.\n"
                "3. EDGES: deviate ONLY if (a) today's sims disprove a "
                "notebook line, (b) you drew a card/fate the plan never "
                "considered, or (c) a must-win round sims to a loss on-plan. "
                "Then test 2-3 alternatives and take the best, even if "
                "unwritten.\n"
                "Never: field a board unsimmed vs the announced opponent; "
                "follow a notebook claim today's sims contradict; bank >25 "
                "exchanges.\n"
                "end_turn one-liner: 'PLAN: <section used>' or "
                "'DEVIATED: <why>'.")
            hold_for_offpeak(game)
            t0 = time.time()
            try:
                turn_fn(seat, model=a.model, phase_prompt=prompt,
                        api_key=keys.get(pid))
            except B.InsufficientBalance:
                raise
            except Exception as e:
                game.log(f"  pid{pid} turn crashed: {e!r} — turn forfeited")
            if not seat.ended:
                game.log(f"  pid{pid} hit the turn cap without end_turn")
            game.action_history.setdefault(rnd, {})[pid] = list(seat.turn_log)
            game.log(f"R{rnd} pid{pid} {seat.name} acted "
                     f"({time.time()-t0:.0f}s): {'; '.join(seat.turn_log) or '(nothing)'}")
        results = game.finish_round()
        for i, r in enumerate(results):
            (gdir / "battles" / f"r{rnd}_{i}_p{r['a']}v{r['b']}.log").write_text(
                r["log"], encoding="utf-8")
        game.log(f"R{rnd} standings: " +
                 ", ".join(f"pid{q.pid}:{q.destiny}" for q in game.env.state.players))
        game.log(f"R{rnd} rerolls: " +
                 ", ".join(f"pid{q.pid}:{q.rerolls}" for q in game.env.state.players
                           if q.alive))

    alive = game.env.state.alive_players()
    rank = lambda q: (q.alive, q.destiny)
    top = max(rank(q) for q in game.env.state.players)
    co_winners = [q for q in game.env.state.players if rank(q) == top]
    winner = co_winners[0]
    alive_now = [q for q in game.env.state.players if q.alive]
    if len(alive_now) > 1:        # only possible via the safety limit
        game.log(f"GAME VOID after R{game.env.state.round}: harness safety "
                 f"limit hit with {len(alive_now)} players alive — NOT a game "
                 f"result (the real game has no round cap).")
    elif len(co_winners) > 1:     # never break ties by seat order
        game.log(f"GAME OVER after R{game.env.state.round}. TIE for 1st: "
                 + ", ".join(f"pid{q.pid} {ENG.NAMES[q.char_id]} 命={q.destiny}"
                             for q in co_winners))
    else:
        game.log(f"GAME OVER after R{game.env.state.round}. "
                 f"Winner: pid{winner.pid} {ENG.NAMES[winner.char_id]} 命={winner.destiny}")
    game.co_winners = [q.pid for q in co_winners]

    # ── post-game reflection (notebook + programs), context wiped afterwards ──
    if not a.stub:
        run_reflections(game, seats, keys, a.model, winner)

    # ── artifacts ──
    (gdir / "game_log.txt").write_text("\n".join(game.log_lines), encoding="utf-8")
    (gdir / "result.json").write_text(json.dumps({
        "game": a.game, "seed": seed, "rounds": game.env.state.round,
        "winner": winner.pid, "winner_name": ENG.NAMES[winner.char_id],
        "tie": len(game.co_winners) > 1, "co_winners": game.co_winners,
        "unfinished": sum(1 for q in game.env.state.players if q.alive) > 1,
        "standings": game.standings(),
        "sidejobs": game.sidejobs,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    if not a.stub:
        try:
            import boards_db as BD
            n = BD.update_game(gdir, a.game)
            game.log(f"boards_db updated: {n} rows for game {a.game}")
        except Exception as e:
            game.log(f"boards_db update failed: {e!r}")
    bot_dirs = {s.name: s.dir for s in seats.values()}
    (gdir / "referee.md").write_text(REF.referee_report(game, bot_dirs),
                                     encoding="utf-8")
    print(f"\nartifacts in {gdir}")


_CURRENT = None
EXIT_OUT_OF_MONEY = 3


def _save_out_of_money(err) -> None:
    """API balance ran out (HTTP 402). Mid-game: the game is ABORTED (no
    winner — the remaining turns were never played). During reviews: the
    game result stands; only the later reviews are missing."""
    game, gdir, a, seed = _CURRENT
    over = game.game_over()
    alive = [q for q in game.env.state.players if q.alive]
    game.log(("REVIEWS STOPPED" if over else "GAME ABORTED")
             + f": DeepSeek balance exhausted ({err})")
    (gdir / "game_log.txt").write_text("\n".join(game.log_lines),
                                       encoding="utf-8")
    top = max(game.env.state.players, key=lambda q: (q.alive, q.destiny))
    (gdir / "result.json").write_text(json.dumps({
        "game": a.game, "seed": seed, "rounds": game.env.state.round,
        "winner": top.pid if over and len(alive) == 1 else None,
        "winner_name": (ENG.NAMES[top.char_id]
                        if over and len(alive) == 1 else None),
        "aborted": not over, "reviews_incomplete": over,
        "reason": "DeepSeek balance exhausted (HTTP 402)",
        "standings": game.standings(),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[out-of-money] {'reviews stopped' if over else 'game aborted'}; "
          f"artifacts in {gdir}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except B.InsufficientBalance as e:
        if _CURRENT is not None:
            _save_out_of_money(e)
        sys.exit(EXIT_OUT_OF_MONEY)
