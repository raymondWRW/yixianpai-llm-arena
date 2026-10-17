# Game 2 — learning report (2026-09-16, model deepseek-chat, seed 202)

**Result:** 谭舒雁 (pid1) wins AGAIN — back-to-back titles — after 18 rounds
with 命26. Eliminations: 吾行之 R14, 小布 R17, 牧逸风 R18.
Sidejobs: 牧逸风→灵植师, 谭舒雁→灵植师, 吾行之→命理师, 小布→炼丹师.

## How the game went

- **First live 体魄 breakthrough**: R9, 小布 broke 境3→境4 at 修为33 / 体魄40
  ("BREAKTHROUGH via 体魄") — the 9/21/36/55 gate rule carrying a bot through a
  realm it couldn't afford with cultivation. It followed its game-1 notebook:
  built 体魄 early (20 by R6, 40 by R9, 52 by R12) and held the 命 lead
  (95 at R9, 72 into R14) exactly as its "buffer first" lesson demanded.
- But 小布's burst deck fell off past R14 — battles stretched to 19–21 turns
  where remaining HP decides, its deck had no sustain, and being the odd player
  out twice (R15, R17 double battles) finished it.
- 谭舒雁 had a rocky middle (dropped to 命26 by R13, including a −26 loss to
  nearly-dead 吾行之) then **pivoted archetypes mid-game**: from the game-1
  turtle to a 星弈 star-point board (天元心法 slot-1 makes every slot [星位],
  星弈·飞 chase payoff, 聚气咒 qi→DEF floor) and won the last 5 rounds
  straight, beating both seats.
- 牧逸风 committed to a mono-云剑 chain deck, hovered at 命1 for the last
  three rounds on extra-battle wins over 小布, and died last (R18, −34).
- 吾行之 out-economied everyone again (highest 修为 for stretches) with a weak
  board again, lost 11 of 14 battles, first out. Its own notebook now says it:
  "Economy without board power = death."

## What each bot learned

**Three bots independently extracted the exact destiny-damage formula** from
gamestate_full.js:1619 (小布, 牧逸风, 吾行之 all quote
`round + 1 + ceil(hp_delta/5)` / the >20 branch) and drew the same conclusion:
margin barely matters, WINNING the round is everything, and late losses cost
~20–26 命. This is emergent convergent study — none of them saw the others'
notebooks.

**谭舒雁 (winner)** — documented the star-point archetype and the key tech
swing: 聚气咒's qi→DEF cap-7 floor is what turned "wins going first, loses
going second" into winning both seats. New rules: always carry a going-second
defensive card; by R13+ brute-force the board to win BOTH seats; cross-validate
vs buffed opponent variants.

**小布** — "BURST-ONLY IS A TRAP": wins in 11 turns mid-game but loses the
19–21-turn late grinds; plans DEF/HP-gain in the deck next time. Spotted that
狂舞曲 buffs BOTH sides' attack (bad in long fights). Noted loss-prevention
fates (龙鳞 cap-20, 猫魂 halving, 慈念曲) as late-game gold. Also learned the
odd-player-out double-battle risk the hard way.

**牧逸风** — "MY BOARD WAS A GRINDER, NOT A KILLER": 10–14-turn narrow wins
lose to late HP walls; next game it wants stack-then-one-big-finisher (巨鲲)
instead of chip. Confirmed seat-flipping a matchup via 修为 padding works
(measured an auto-loss→auto-win flip).

**吾行之** — the bluntest self-diagnosis of the four: it treated the game as a
修为 race, reached max realm with the highest cultivation and a weak board,
and died first two games running. New hierarchy: board power > 体魄/HP >
修为-just-for-seat-and-gates. Whether it executes this next game is the thing
to watch.

## Referee findings

- **Programs**: the YISIM_DIR sanctioned route worked — ~40 new programs this
  game and essentially all source readers use `os.environ['YISIM_DIR']`.
  One violation: 牧逸风's game-1 leftover `readsrc.py` globbed from `/`
  (drive root) — deleted; its own newer YISIM_DIR-based tools supersede it.
  小布's `findfates.py` os.walks only *inside* YISIM_DIR — allowed.
  谭舒雁 built a 28-program toolkit (card DB dumps, seat/lethal calculators,
  board testers) — all jailed correctly.
- **Qi-stall flags** (R12–R15, 谭舒雁 first-seat stalls 6–16 turns): manual
  review shows a genuine deck-building error, not stalling-for-advantage — its
  transitional board carried expensive cards (气吞山河+1, 天元心法) after it
  had absorbed its qi engines, so it sat generating qi. It lost the worst of
  those battles (−26, R13) and fixed the board by R14 (聚气咒/吸灵符 qi
  sources). No action needed; this is the qi-legality check working.
- No unimplemented fates held. No rival-dir or harness access. Extra-battle
  "(not applied)" destiny rule fired correctly at R15/R17.

## Harness observations

- Four turn-cap hits without end_turn (R9 吾行之, R10/R11 谭舒雁, R18
  牧逸风) — all during long roll-chains; turns were kept as played. Might be
  worth raising MAX_TOOL_TURNS or warning the bot at turn 50 in a future
  version, but the cap is doing its job as a cost control.
- Wall clock ≈ 80 min; turn latency 13–205s.
- Both remaining meta-questions from game 1 stayed stable: 谭舒雁's win was
  archetype-driven (not seat luck), and the 体魄 economy is now a live
  strategic lane (小布's physique gate breakthrough).
