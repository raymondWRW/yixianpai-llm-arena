# Game 6 — learning report (2026-09-18, model deepseek-chat, seed 206)

**Result:** 小布 (pid3) wins its FIRST title — 命29 after 16 rounds, and the
most dominant run in arena history: 命100 untouched through R10, then a
double elimination at R16 (牧逸风 −22, and 谭舒雁 −24 as the losing
ghost-fighter — both hit 0 in the same round). Eliminations: 吾行之 R14,
牧逸风 & 谭舒雁 R16. The four-time champion is dethroned.

First game on the token-efficiency loop (SITREP/CARD REFERENCE observations,
sim_matchup, 3-pass play prompt; battle_log + injected matchup matrix +
budgeted search_board in a 7-phase review).

## How the game was won

小布 executed its game-5 post-mortem to the letter: keep the force-stack
build, fix LEVELS and SEAT. It merged its core early (气若悬河+1, 势如破竹+1,
朝气蓬勃+1), padded 修为 relentlessly (79 by R16 — seat priority in the
fights that mattered), and rode 体魄 up to a 44/65 tank frame. Its engine
(威震四方 raising the Force cap → 崩拳·寸劲 double-Force ~39 → 磅礴之势
dump) killed everything in 7–11 turns. It won 13 of 16 rounds.

The old champion 谭舒雁 never stabilized: its star board sat at base levels
too long, and its two late extra battles as ghost-fighter (R15, R16) were
both losses — the second one fatal.

## The new review loop, observed

- **Speed/efficiency**: turns ran 12–163s (median far below the old loop);
  ZERO turn-cap hits all game (previous games: 1–4 per game); no bot wasted
  discovery calls on card text or lethality math.
- **小布 (winner)**: notebook v63 traces its engine card-by-card from a
  battle_log R16 read, quotes the injected matrix per rival, records a
  search_board head-to-head (势如破竹 beats 崩灭心法 in-slot, 8t vs 12t
  kills), and marks its three load-bearing cards LOCK IT. 60 lines.
- **谭舒雁**: went to the engine source with line citations — [SRC
  gamestate_full.js:4440] star_power mechanics, and the discovery that
  0-based slots 2 and 5 are star points BY DEFAULT ("free real estate" its
  decks never exploited). Adopted the [SRC]/[SIM]/[LOG]/[GUESS] tag scheme
  verbatim.
- **牧逸风**: produced a per-rival recipe book — a QI board (聚灵心法 →
  巨鲲灵剑 react → 万法归灵剑 49-58 dump) that sims 100% vs 谭舒雁/吾行之,
  and a separate REFLECT board that sims 100% vs 小布's exact final board.
  If it executes the per-opponent switch next game, it is the credible
  challenger.
- **吾行之**: the most valuable negative result — 4 search_board calls
  drawing from SIX careers' pools all returned 0% vs pid0/pid3. Its
  conclusion is structurally correct: the archetype has no engine, and the
  loss happened in the economy rounds, not R14. It now plans an engine
  build (混元无极阵 chase line) instead of chip.
- Notebook hygiene: 56–102 lines each (was 60–120+ of drifting prose), all
  four carry evidence tags.

## Rules & harness verification

- Matchup matrix computed post-game in ~1.4s and injected into all four
  review prompts (bots quote it directly).
- search_board budgets held (no bot exhausted 600 evals; 吾行之's 4 calls
  were the heaviest user). No search escaped its locks or produced an
  illegal board — every returned board obeys the ≤2 [消耗]/[持续] rule.
- Corrected 修为 gates (9/21/36/55) visible: all four broke 境2 at 修为 9-11
  on R3, a round earlier than the old-belief games.
- Ghost battles (R15/R16) resolved correctly; 谭舒雁's R16 ghost loss WAS
  applied (it was the odd player) — that's what eliminated it.

## Referee findings

Clean: no unimplemented fates, no qi-stall flags, no program violations, no
turn caps. 吾行之's R13 25-roll fishing spree burned its bank 25→0 the round
before it died — its own notebook now names this the terminal mistake.

## Meta after six games

Titles: 谭舒雁 4, 吾行之 1, 小布 1. Three distinct proven engines now
coexist (force-stack, star-power, qi-dump), each with at least one
documented 100% counter in someone's notebook. Game 7's shape: 牧逸风 holds
counters to everyone but must switch boards per announced opponent; 小布's
crown depends on keeping the seat; 谭舒雁 knows about the free star slots.
The lobby has never been this well-armed.
