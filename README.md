# 弈仙牌 LLM Arena

Four language-model bots taught themselves the 4-player card auto-battler
**弈仙牌 (YiXianPai)** over 30 games of self-play, starting from nothing but the
rules, a combat simulator and an empty notebook.

**→ [Read the analysis report and watch all the replays](https://raymondwrw.github.io/yixianpai-llm-arena/)**

The report covers how each bot's strategy changed over the 30 games, the key
cards and counters they discovered, and how close their play is to real
players.

## How it works

- **Four seats, one per sect:** 牧逸风 (云灵剑宗), 谭舒雁 (七星阁), 吾行之 (五行道盟)
  and 小布 (锻玄宗). Each seat is a DeepSeek (`deepseek-chat`) agent that plays the
  full game through tools: roll, absorb, merge, field a board, break through,
  pick a sidejob and fates.
- **Combat** is resolved by [yisim](https://github.com/sharpobject/yisim), an
  open-source reimplementation of the game's battles. Bots can simulate any
  board before committing to it.
- **During a game** each bot sees only what a player would: its own hand and
  board, opponents' previous-round boards, and its announced opponent.
- **After each game** every bot reviews turn-by-turn battle logs, a per-card
  damage audit and its roll history, searches for boards that beat the ones
  it lost to, then updates its playbook and an append-only ledger. Its
  conversation memory is wiped between games; only those files survive. From
  game 16, reviews could read every rival's files.

## Repository layout

| Path | What it is |
|---|---|
| `docs/` | The GitHub Pages site (report + replay viewer). Rebuild with `python yixian_sim/site/build_site.py`. |
| `yixian_sim/arena/` | The arena: engine, bot tools and prompts (`bots.py`), game runner (`run_arena.py`, `run_series.py`), referee. |
| `yixian_sim/arena/games/gameN/` | Every game's log, battle logs, result and per-bot replays. |
| `yixian_sim/arena/bots_state/<bot>/` | Each bot's playbook (`notebook.md`), ledger (`ledger.md`) and self-written helper programs. |
| `yixian_sim/arena/reports/` | Per-game learning reports (games 1–21). |
| `yixian_sim/selfplay/` | The economy simulation (deals, rolls, fates, realms) the arena runs on. |
| `yixian_sim/agents/` | An earlier project: hand-played games and a strategy playbook for 林小月. |

## Not included

- **API keys** (`arena/deepseek_keys.json`): add your own DeepSeek keys, one per
  seat, as `{"0": "sk-...", "1": "...", "2": "...", "3": "..."}`.
- **yisim**: clone it from upstream; the bridge expects it in a sibling
  `card counter with proxy/vendor/yisim-master` folder (path in
  `arena/yisim_bridge.py`).
- **Extracted game data, live-game tooling and raw captures of live matches**
  are deliberately left out of this public repo.

This is an independent fan project; 弈仙牌 and its card names belong to their
owners.
