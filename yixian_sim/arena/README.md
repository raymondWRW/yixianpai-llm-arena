# Arena — 4 LLM bots play YiXianPai against each other

Built 2026-09-16 per the user's spec. Four fixed seats, one per sect:
**牧逸风** (云灵剑宗) · **谭舒雁** (七星阁) · **吾行之** (五行道盟) · **小布** (锻玄宗).
Each seat is an LLM that plays the whole game through tools, with a persistent
notebook and self-written helper programs that survive between games (its
conversation context does not). Goal: last one standing.

## Architecture

- `engine.py` — 4-player game on the selfplay economy env; combat resolves
  through **yisim** (`yisim_bridge.py`, bun subprocess), which returns a full
  turn-by-turn log per battle. yisim is ground truth here — the same engine
  bots use for their sims, so a bot can understand exactly why a fight went
  the way it did. Destiny transfer uses yisim's own formula (round_number is
  passed in). No byes: odd player out fights an extra battle, only they risk 命.
- `bots.py` — the tool interface. Per round each living bot gets ONE fresh
  tool-runner conversation: observation (own private state + every opponent's
  LAST-round public state — standard fog), tools for card text, yisim source
  grep, exact battle sims, notebook/programs, and the game actions
  (roll/absorb/merge/take/set_board/peek_breakthrough/breakthrough/
  choose_sidejob at R2/end_turn). Model default `claude-opus-5`.
- `referee.py` — hard legality is enforced inside the engine actions; soft
  checks (qi-stall counts per battle, program audits for filesystem/network
  reach) go into `games/gameN/referee.md` for Claude's per-game review.
- `run_arena.py` — one game per invocation:
  `python run_arena.py --game N [--seed S] [--model M] [--stub]`.
  `--stub` = scripted keyless bots (harness smoke test; game0 passed 2026-09-16).
  After a real game, each bot gets a reflection conversation: rewrite its
  `notebook.md`, optionally `save_program()` helpers; then its context is gone.

## Persistent bot state

    bots_state/<name>/notebook.md    — the bot's own strategy notes
    bots_state/<name>/programs/*.py  — helper programs (subprocess, 30s cap,
                                       cwd = bot dir; audited every game)

## The iteration protocol (user spec)

1. Run a game. 2. Bots reflect (notebook + programs). 3. Claude writes the
referee review AND `reports/gameN_learning.md` — what each bot learned, how it
changed its notebook/programs, and any foul-play findings. 4. Next game starts
with wiped context + surviving notebooks/programs.

## Fate forwarding (v2, done 2026-09-16)

`fate_map.py` forwards combat-side 天命 into yisim payloads (both for real
battles and for bots' `simulate` calls, both sides — talents are public info):

- Tiered fates -> `p{pick_phase}_{slug}_stacks` (17 slugs; magnitudes scale
  with pick phase; repeated picks stack). Verified: 剑韵修炼 @境2+境5 = +1/+2
  剑意 at battle start.
- Untiered character fates -> their own fields (剑不出鞘, 云海连绵, 雪羽清风,
  五行印记, 灵涌不竭, 修玄不泯, …).
- The 化身 keep-1-命 family is applied by yisim inside its destiny step; the
  engine adopts yisim's post-battle destiny, then consumes the stack
  economy-side with the fate's cost (verified in game0: both saves fired once,
  second loss killed).
- Engine-hook fates (economy triggers): 战斗历练 (win -> +2 rolls), 易数化劫
  (loss -> +1 roll), 历战不屈 (loss -> +1 maxHP), 磨砺不止 (+1 roll per 7 命
  lost), 勤学苦练 (draw 1 per 8 absorbs), 云雾变幻 (env free roll).
- Anything a seat holds that is in NONE of these tables is listed as
  UNIMPLEMENTED in the referee report (`fate_map.unimplemented`).

## 体魄 economy (v2 — REAL rules, user ruling 2026-09-16)

- **生命转化**: every 体魄 point = +1 **max** HP (current HP is not healed).
  This is yisim's native `max_hp = hp + physique`, so the bridge passes base
  `hp` unadjusted.
- **跨回合保留**: physique built in battle persists to later rounds. After
  each battle the engine adopts yisim's battle-end physique per side (parsed
  from the log by turn-block attribution), clamped to the **retention cap**.
- **保留上限**: cap starts at 6, grows **+5 every round** from R2
  (engine.begin_round). Fates can modify it (稳固根基 = 上限−1, via
  fates.apply's tipo_cap delta).
- **临时突破上限**: in-battle physique may exceed the cap freely; yisim's
  `increase_idx_physique` grants +1 max HP per point always, and heals
  +1 current HP per **overflow** point — exactly the ruled behavior. The cap
  is passed as yisim's `max_physique`.
- **体魄 breakthrough**: reaching **9/21/36/55 体魄** allows breakthrough to
  境2/3/4/5 even without the 修为 gate (engine.act_breakthrough, PHYS_REQ;
  fires the same fate-offer + 道韵 flow as a 修为 breakthrough).

Verified in stub game90: 小布's 体魄 persisted 5→11→21→33 across rounds while
non-锻玄宗 seats stayed at 0; caps tracked 6+5/round (25 for 小布 = 26−1 from
稳固根基).

## Remaining known gaps

- yisim is a ~1.5.9 snapshot: base-game cards only, no season mechanics —
  matching the arena's card pools, which are also base-game.
- Speed/first-move: house rule = higher 修为 first, ties coin-flip (yisim has
  no speed model; this matches the main sim's rule).
- 斩断俗尘 (谭舒雁 境5: no more 炼气期 cards in deals/rolls) is not applied to
  the deal filter — listed as unimplemented if picked.

## Token-efficiency layer (2026-09-18)

Every DeepSeek tool round-trip resends the conversation, so repetitive work
moved harness-side:

- `batch_run.js` (in the yisim vendor dir): many battles per warm bun process
  — ~16 ms/battle vs ~1.5 s/subprocess. `yisim_bridge.run_battles()` wraps it.
- Observation now carries a computed **SITREP** (loser-damage range, must-win
  flags, seat vs announced opponent, reroll-cap warning, breakthrough
  availability) and a **CARD REFERENCE** (effect text of every card in
  hand/board/opponent's last board). Action results return a compact status
  line instead of the full observation.
- `sim_matchup(my_cards, opp_pid)`: both seats × (opp as-is, opp+1) × N reps
  in one call. `battle_log(round)`: the recorded log of a fought battle.
- Review: a precomputed MATCHUP MATRIX (all final-board pairs, both seats,
  base and +1/+1) is injected into every reflection prompt; `search_board`
  runs a mini-batch hill-climb over composition + ORDER + levels with
  lock_slots / lock_cards, objective choice, ≤120 evals/call, 1200 evals and
  8 min wall-clock per bot (measured: ~40 evals ≈ 4 s). The trace of accepted
  improvements is returned so bots learn WHY, not just what.
## Two engines, split by what each is good at (2026-09-25)

Measured on this machine, same matchups:

| engine | ms/battle | narration |
|---|---|---|
| yisim (bun batch) | ~29 | human-readable turn-by-turn + STATE lines |
| Oracle, 1 warm worker | ~13 | raw telemetry (`ModifyBuffValue a0=629`) |
| Oracle, 8 parallel workers | **~2.6** (383/sec) | same |

The Oracle (`oracle_bridge.py`) is the game's OWN combat code JIT-compiled
native in CoreCLR — bit-exact, takes our card ids and fate ids directly (they
ARE game ids), and probes the same base-HP-per-realm table we use. But the two
engines pick the same winner in only **83% of real corpus matchups**, so:

- **yisim stays the arbiter and the narrator**: it resolves every real arena
  battle, backs `simulate` / `sim_matchup` / `battle_log` / the matchup matrix,
  and writes the logs bots reason from.
- **the Oracle is the search pre-filter only**: `search_board` hill-climbs on
  it (~11x more candidates per second), keeps the top 6 finalists, and then
  **yisim re-ranks those finalists and its verdict is what the bot is told**.
  A disagreement is reported in the tool output. With the Oracle driving, the
  budget is 400 evals/call and 4000/bot; without it the tool falls back to
  pure yisim at 120/call and 1200/bot, labeled in its output.

Never let an Oracle-only verdict reach a notebook: bots would write "100% win"
lessons that lose in the yisim-resolved fight.

- Draw mechanics (2026-09-27): RULES has a DRAWS & ROLLS section (phase gating by realm, 3+1 deal split, rolls are random from the whole deck, burn 3 sect / 2 sidejob / 0 [置换], phase-5 rarity). pool_cards() shows the LIVE deck with per-roll and per-deal odds after burns; SITREP seat line now states the opponent 修为 is their start-of-round value.
- Memory split (2026-09-25): per-bot LEDGER (append-only per-game archive, append_ledger/ledger tools, no length limits) + PLAYBOOK rebuilt by MERGING with a carry-forward contract (delete requires citing disproof; 3+-game rules promoted to CORE PRINCIPLES). RULES now carries a verified COMBAT MECHANICS glossary (tempo/chase/身法, turn-start timing, ~25 keywords from combat_rules.md); card_stats and STATE lines now surface agility and extra actions.
- Review self-audit tools (2026-09-20): `economy_history` (own per-round
  deals/rolls/absorbs + banked exchanges — feeds the ROLL AUDIT phase),
  `board_db` (persistent boards_db.json of every board ever fielded, queried
  by round for similar-power comparisons and search seeds; auto-updated
  post-game, backfilled from games 1-10), `card_stats` (per-card contribution
  parsed from real battle logs: plays/dmg/resources/costs — feeds the CARD
  AUDIT phase).
- Turn caps: 60 in-game, 300 in review. Play prompt = three passes
  (READ computed blocks → EXECUTE notebook plan → DEVIATE only with cause,
  tagged in end_turn). Review prompt = 7 phases (understand fights via
  battle_log → audit notebook → read matrix → constrained searches →
  mechanics → next-game decisions → rewrite notebook ≤120 lines with
  evidence tags).

NOTE: realm gates corrected in RULES to the env's authoritative table:
修为 9/21/36/55 (境2-5) — same thresholds as the 体魄 gates.

## Pending

- (none — arena runs on DeepSeek, one key per seat in deepseek_keys.json)
