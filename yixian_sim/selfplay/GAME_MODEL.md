# YiXianPai offline model — for AlphaZero-style self-play

Goal: a faithful, fast, offline simulator of the whole game so a policy can be
trained by self-play without touching the live client. The battle step is exact
(the Oracle = the game's own combat code); the **prep economy is
server-authoritative in the real game**, so it is *reimplemented* here and
validated by replaying recorded games through it.

## The decision problem

Battle auto-resolves — the agent only acts in the **prep phase**. Each round the
agent decides: draft (which offered cards to take), reroll (`ReplaceCardReq`),
absorb (`RefineCardReq` → +cultivation), merge, board arrangement (the 8-slot
cycle), breakthrough timing, and 天衍/道韵 picks. Then the Oracle resolves the
1v1 battle against the paired opponent. It is 8-player, imperfect-information
(opponents' hands/decks hidden), and stochastic (draws).

Design decisions (see the "AlphaZero adaptation" section):
- **Placement is a macro-action** delegated to the existing `oracle_sim`
  HK-ordering + Oracle search — NOT learned. MCTS operates over economy actions
  only, or the branching factor explodes.
- **Opponents come from the self-play population**, not the `next-board-model`.
- **Draws = MCTS chance nodes** (stochastic-AlphaZero / expectimax variant).

## Confirmed transition rules

### Realm / breakthrough — EXACT (configs/LevelConfig.dat, cross-checked vs live HP)
| realm | cultivation required | base HP |
|------|----------------------|---------|
| 1 | 0  | 40 |
| 2 | 9  | 45 |
| 3 | 21 | 52 |
| 4 | 36 | 62 |
| 5 | 55 | 75 |
| 6 | 75 | 100 |

Breakthrough is player-timed: you *may* break once cultivation ≥ the next
realm's requirement (game normally realm-caps at 5; realm 6 exists in config).
Max HP = base HP + extraMaxHp (HP fates add +2/+3 at battle time).

### Board slots — mined (clean), n=103 games
`unlocked = min(8, round + 2)` for rounds 1..6, then 8 thereafter.
(R1→3, R2→4, R3→5, R4→6, R5→7, R6+→8.)

### Cultivation (修为)
- +1 per card absorbed (炼化, `RefineCardResp`) — confirmed in shadow logs.
- Passive gain ~2-4/round on top (round-band; exact source TBD — likely a
  per-round base + card-passive effects). Displayed cult (top-level field 5)
  includes the current round's passive; the 200.3 stat lags it by that passive.

### Merge — configs/CardCombineConfig.dat (86 rows)
3 copies of the same card at level L → 1 at level L+1 (one level per round).
The config maps base id → upgraded id (field 101 = source, field 2 = result).
`shadow_state`/`lingyu_merge` already implement the mechanic.

### Deck pool composition + draws — official FAQ (2026-07-08) + `proxy_view.Counter`
Copies per card (FAQ-confirmed): **8** default (Meditation→Immortality phases),
**6** for Incarnation-phase (= our "phase 5") cards, **3** for the Elixirist
side-job's three elixirs (Talent / Great Bodybuilding / Enlightenment). Sidejob
(副职) and derivation (天衍) cards start at 0, added when the career/derivation
is picked (phase-filtered).

**Draw law (FAQ):**
- **Uniform** — "the probability of obtaining each card is consistent." No
  current-phase priority in general → the deal is a weighted bag sample over
  remaining copies (each copy = weight 1), among cards whose phase is
  *available* (phase unlocks with realm — confirm the exact gating).
- **First-exchange boost (exact)** — on the FIRST exchange of the Foundation /
  Virtuoso / Immortality rounds, **current-phase card copies count DOUBLE** in
  the weighted draw (weight 2 instead of 1), so a current-phase card is twice as
  likely to be drawn as an equal-copy card of another phase. Only that first
  exchange; subsequent draws that round are back to weight 1.
- **Empty pool → "Deviation Syndrome" (走火入魔)** — the fallback card dealt when
  no pool card meets the draw's conditions.
- **Absorb (炼化) does NOT affect the pool.** Only drawing (−1 of the drawn card)
  and exchanging change it.
- **Exchange burn**: removes 2 copies of the discarded card; under this season's
  extra-seasonal-card mechanism SECT cards lose **3**, sub-profession cards lose
  **2**. (Cards WITH an Exchange effect are not removed.) `proxy_view.Counter`
  updated to match (was a flat 3 → sidejob now 2).

**Phase-availability gate (confirmed):** only cards of the **current phase or
lower** are drawable (phase unlocks as you advance). Card phase per id is in
`tools/card_phases.json` (from CardConfig.xlsx: id → {name, phase, sect}).

**Drawable-pool membership (confirmed):** the standard pool is the normal card
set (base sect cards of the player's sect + picked sidejob cards, phase-gated).
It EXCLUDES: derivation / event cards (e.g. 云剑•晚霞 and other 云剑•X / 幻•X —
these enter the deck ONLY via their 天衍 / special-event pick, never the normal
draw), special non-drawable cards, and dream (梦…) / personal-fate (id<1e6)
cards. Membership is NOT pure id math — 云剑•X cards sit in the sect id-range yet
aren't drawable — so `draws.py` builds the bag from the SAME source the counter
uses (`card_phases.json` + `Counter`'s sidejob/derivation/`_is_deck_card` logic),
not from id patterns.

**Deal count per round (mined, n=105 games)** — cards freely dealt at prep open:
**5** opening (round 1), **3** rounds 2-11, **4** rounds 12+. ~75-90% fit this
cleanly; ~20% show +1, likely a breakthrough/grant-round extra draw (pin during
fidelity). `economy.deal_count(round)`. The draw model is now spec-complete
enough to build `draws.py` and validate.

## Resolved from mining (recentBattleDatas, 181 games)
- **Destiny (命) loss** — the round LOSER drops by |net| (= |Oracle lifeDamage
  margin|); the winner's 命 holds. Fits ~56% exactly / ~87% within {net,
  min(0,net)}; the ~13% residual is secondary 命 sources (fate/card/breakthrough
  effects) — accepted approximation (reward is ordinal placement; combat is
  exact). `env.apply_battle`.
- **Pairing** — random among the living, avoiding the immediate-previous
  opponent where possible (consecutive same-opponent only ~7% in real games);
  repeats grow naturally as the field shrinks to survivors. `env._pair`.

## Open items (remaining)
- **Passive cultivation source** — per-round base vs card-passive effects.
- **天衍/道韵 offer rules** — when offered, how many choices, the pick pool.
- **The +1 deal on some rounds** — likely breakthrough/grant extra draw (confirm).
- **Real Oracle battle wiring** — needs board name↔id + the placement
  macro-action (delegated to oracle_sim search) so boards are real card-id lists.

Combat BUFF/DEBUFF math (FAQ, for reference — the Oracle already implements it,
so the sim does not reimplement): apply additions/subtractions first (floored to
1), then multiply by summed percentages; final result ≥ 1.

## Architecture

```
selfplay/
  economy.py     — confirmed transition rules: realm table, slot schedule, merge
                   map, pool composition, cultivation. (DONE)
  draws.py       — the stochastic deal/reroll sampler (DONE, FAQ-exact).
  cards.py       — name⇄id seam (draws speak NAMES, the Oracle speaks IDS). (DONE)
  env.py         — 8-player game loop on EXACT Oracle combat; FieldBank wired,
                   bootstrap economy (absorb→cultivation→breakthrough). (DONE)
  field.py       — FieldBank (rolling opponent-board bank) + board-vs-field
                   expected-outcome reward. (DONE)
  placement.py   — placement macro-action: best legal board vs a field sample,
                   reusing oracle_sim candidate-gen + legality caps. (DONE)
  fidelity.py    — replay recorded games through the sim; economy diffs. (DONE)
  net.py, mcts.py, train.py, league.py — the AlphaZero stack (NEXT).
```

### Combat throughput (measured) — why the hybrid plan
`oracle_sim.matchup` ≈ **98 ms/battle** single-worker (10/s); `batch_matchup`
parallelises across the 5-worker pool for **~200/s** (4.4×). Exact but far too slow
for full-scale AlphaZero (MCTS × millions of games). So: **prototype the RL loop on
the real Oracle now** (proves the loop end-to-end on exact combat), then **learn a
fast battle-net** `B(boardA,statsA,boardB,statsB)→lifeDamage` from Oracle-generated
data to scale. The game splits perfectly: prep dynamics are cheap+exact in Python;
combat is the ONE expensive thing, so it's the only thing worth learning/caching.

### Reward core (board-vs-field) — validated
You never fight a KNOWN opponent (random pairing), so a board's worth is its
EXPECTED destiny outcome vs the FIELD. `FieldBank` holds recently-played boards
(self-play fills it → it sharpens with the policy); `placement.best_board` scores
every legal candidate against ONE shared field sample (paired comparison, single
batched pool call) and plays the best. Head-to-head on real Oracle (4 search vs 4
greedy): **search mean placement ~2.6 vs greedy ~6.3, search wins every game.**
First real strategic behavior — the placement expert the learned policy sits atop.

Validation methodology mirrors how the Oracle was driven to bit-exactness:
replay real recorded games (deck_tracker + recentBattleDatas) step-by-step
through the sim and diff every economy quantity. The sim ships only when it
reproduces recorded games within tolerance.

## AlphaZero adaptation (later milestones, recorded here so the env is shaped right)
- **8-player → league.** Reward = final placement (1st–8th); train a population,
  rank by placement, avoid meta collapse (à la TFT bots / AlphaStar league).
- **Hidden info → belief/sampled opponents** drawn from the population inside the
  tree; no separate opponent predictor needed (self-play generates the field).
- **Stochastic draws → chance nodes** in MCTS.
- **Hierarchical actions**: MCTS over economy decisions; placement solved by the
  existing `oracle_sim` search as a macro-action (reuses the crown jewel, keeps
  the tree tractable).
