# yixian_sim — standalone YiXianPai (弈仙牌) game simulator

A self-contained copy of the full-game simulator extracted from the
`card counter with proxy` project, packaged so future models/agents can be
trained and evaluated against it without the live game, the proxy, or the HUD.

* **Combat is exact** — battles run through the **Oracle**, the game's own combat
  DLL re-hosted headless (99.97% bit-parity vs 12k recorded rounds).
* **Prep economy is reimplemented in Python** from the game's config tables +
  mined real games (realm table, slots, rerolls, draw law, merges, fates, 道韵,
  side jobs, physique) and validated by replaying recorded games.
* **8-player game loop** with random pairing, 命 (destiny) loss, elimination and
  final placement; plus a **placement search** (best legal board + cyclic
  ordering vs a sample of the opponent field) and several baseline policies.

```
yixian_sim/
  smoke_test.py            run this first
  requirements.txt
  selfplay/                the simulator (see selfplay/GAME_MODEL.md for rule provenance)
    env.py                 YiXianEnv: 8-player loop, PlayerState, play_round/play_game, greedy_policy, make_field_policy
    economy.py draws.py    exact/mined transition rules; weighted-bag deal & reroll sampler
    cards.py merge.py      name⇄id, level-up map           characters.py fates.py fate_fx.py body.py qi.py bias.py
    field.py               FieldBank — rolling bank of opponent boards (the reward core)
    placement.py           placement macro-action: best_board / best_ordering through the Oracle
    encode.py              state → features (for nets)
    econ9.py real9.py      strongest baseline agent (real-data schedules + target build), data/real9_*.json
    net.py policy_net.py card_value.py battlenet.py choosers.py planner.py econ.py  (older learned-policy modules; need torch)
    selfplay_game.py duel9.py build_replay.py   narrated playthroughs + HTML replay
    *.json                 card_pool / fate_pools / char_innates / card_bias (committed data)
  proxy/
    oracle_sim.py          Oracle bridge: worker pool, fixtures, matchup / batch_matchup, candidate gen, ordering search
    hk_order.py live_nash.py card_id_map.json card_types.json model/adjacency.npz
  oracle/                  the engine (Oracle.exe, facades, game DLL + configs, oracle_pool.py)
  tools/card_phases.json   vendor/yisim-master/localization/1.5.8/{immortal_fates,combined_cards}.json
```

## Requirements

* Windows, **.NET 8 runtime** (Oracle.exe is framework-dependent; install
  "ASP.NET Core / .NET Desktop Runtime 8" if `smoke_test.py` reports the Oracle
  unavailable).
* Python 3.11+ and `pip install -r requirements.txt` (torch/zstandard optional).

## Quick start

```powershell
python smoke_test.py            # Oracle ping, rules load, one 8-player greedy game (~1 s)
python smoke_test.py --search   # + one game with the Oracle board-search policy (~5 s)
python selfplay/selfplay_game.py --order      # narrated strong-policy game, writes selfplay/data/game.json
python selfplay/duel9.py                     # 2-player mirror with the real-data (econ9) agent
```

## Using it to test a model

```python
import sys; sys.path[:0] = ["yixian_sim/selfplay", "yixian_sim/proxy"]
import env as EV, field as F, characters as CH, economy as E, placement as P, oracle_sim

# A policy is just: policy(env, player) -> None, mutating player.hand/board and calling
# env.reroll / env.absorb / env.try_breakthrough etc. during that player's prep.
def my_policy(env, p):
    ...                                   # your model decides rolls / absorbs / merges / board
    EV.absorb_leftovers(env, p)           # or reuse the helpers in env.py

bank = F.FieldBank()                      # persists across games so opponents sharpen
game = EV.YiXianEnv(n_players=8, characters=CH.sample(8, __import__("random").Random(0)),
                    seed=0, field_bank=bank)
placement = game.play_game(my_policy)     # pid list, 1st → 8th
```

Useful hooks:

* `EV.YiXianEnv(fate_chooser=, sidejob_chooser=, daoyun_chooser=, ghost_bank=)` —
  plug learned pickers; `ghost_bank` (a FieldBank of REAL boards) turns the game
  into 8 independent single-agent runs graded against real opponents.
* `EV.decision_state(env, p)` — canonical state dict; `encode.encode(state)` → features.
* `P.best_board(me_fixture, board, hand, slots, opponents, objective="win_fast", ...)` —
  the Oracle placement search (returns board + counterfactual `scored` list, useful as
  training rows). `P.candidates`, `P.best_ordering` are exposed separately.
* `oracle_sim.matchup(fixA, fixB, rnd)` / `oracle_sim.batch_matchup(pairs, rnd)` —
  raw exact battles: `{"lifeDamage", "hpDelta", "turns", ...}` from A's point of view.
  `p.to_fixture(unlocked_slots)` builds a fixture from a PlayerState.
* Environment: `ORACLE_POOL=n` (workers, default `min(6, cpu//3)`), `ORACLE_RANDOM_PARAMS=1`
  (random battle RNG queue instead of deterministic defaults), `ORACLE_EXE` (override path).
* Baselines to beat: `EV.greedy_policy` (weak), `EV.make_field_policy(k, cap, order=True)`
  (Oracle search — search agents place ~2.6 avg vs greedy ~6.3), `econ9.make_real9_policy(meta)`
  (real-data schedules + 龙瑶 target build; `meta = real9.meta()`).

## Notes / caveats

* Files were copied verbatim except three hard-coded external paths (`econ9.py`,
  `real9.py`, `bias.py`) now point inside this package. `fate_categories.json`,
  `real9_meta.json`, `real9_mu.jsonl` are bundled; raw replay shards are not.
* The Oracle here is a snapshot of the game version extracted on 2026-07-24
  (`oracle/data/extracted/`). The original project auto-re-extracts from the
  user's game install on updates (`proxy/oracle_bootstrap.py`, not included);
  after a game patch, re-copy `oracle/data/extracted/` from that project.
* Open modelling items are listed in `selfplay/GAME_MODEL.md` (passive-cultivation
  source, 天衍 offer rules, the occasional +1 deal). Combat itself is exact.
* `characters.py` excludes 2 of the 24 characters (`EXCLUDED = {3000006, 1000006}`)
  whose innates aren't modelled; `fates.all_fates()` returns 216 (template-tier
  fates skipped).
