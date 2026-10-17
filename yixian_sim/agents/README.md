# agents/ — hand-written agents for yixian_sim

## claude_policy.py — the strategy

Sources: TheGamer / GameRant beginner guides (use exchanges every round to find upgrades,
break through before fishing so higher-tier cards are in the pool, keep 1-2 spare Qi so
the cycle never stalls, retire outdated starter cards, stay flexible) + what the sibling
project mined from 4k+ 道心 replays (real median realm schedule 境3@R5 / 境4@R7 / 境5@R11;
rerolls banked early and dumped R10-14; board caps ≤2 消耗 / ≤2 持续).

Per prep phase:

| step | what | why |
|---|---|---|
| 0 pre-pass | Oracle search on the current hand → the cards it would field are **needed** | everything else is roll/absorb fodder |
| 1 tempo | break through if able; if behind schedule and the cult gap ≤ chaff + spare board cards, absorb them and break **now** | HP jump + the new phase's cards enter the pool before this round's rolls |
| 2 rolls | exchange non-needed, non-pair, lowest-phase cards down to a bank floor (0 R1-3, 3 R4-9, 0 R10+); never burn current-phase cards after R4 | exchanges are the only way to find upgrades; pool burn (−3 copies) is fine on chaff |
| 3 board | `placement.best_board` over card sets vs a field sample, objective WIN ≫ kill-speed ≫ 命, cyclic ordering optimised (qi fuel before consumers) | combat is exact, so search it |
| 4 hold/absorb | keep ≤6 cards that are current-phase-or-higher or complete a merge pair; absorb the rest; if absorbing the keep pile crosses a realm gate, do that instead | cultivation is the tempo currency; hoarding loses to breaking |
| meta | side job by sect (炼丹师; 符咒师 for 七星阁), fates via `fates.choose` | |

## eval_claude.py — benchmark

Shared 8-player tables, seats 0-3 = claude_policy, 4-7 = opponent (`--opp search` = the
project's Oracle-search agent `env.make_field_policy(order=True)`, `--opp greedy`).
Field bank shared across games. Prints per-game ranks and mean placement.

Results (seed 1, k=6, cap=14, 2026-08-15):

| opponent | games | claude mean placement | opp mean placement | claude wins |
|---|---|---|---|---|
| greedy | 1 | 2.50 (ranks 1-4) | 6.50 (ranks 5-8) | 1/1 |
| Oracle search (`make_field_policy(order=True)`) | 5 | **4.05** | 4.95 | 3/5 |

Full log: `eval_vs_search.log`. The edge over the search baseline comes from the economy
layer (breakthrough schedule + roll-chaff-only + hold pairs) — both sides use the same
board search. 5 games is a small sample; run `--games 20` for a firmer number.
