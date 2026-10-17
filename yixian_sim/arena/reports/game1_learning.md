# Game 1 — learning report (2026-09-16, model deepseek-chat, seed 201)

**Result:** 谭舒雁 (pid1) wins after 19 rounds with 命21.
Eliminations: 牧逸风 R16, 吾行之 R18, 小布 R19.
Sidejobs chosen at R2: 牧逸风→炼丹师, 谭舒雁→命理师, 吾行之→命理师, 小布→炼丹师.

## How the game went

- 谭舒雁 found the winning archetype by mid-game: a sustain/reflect turtle
  (静气心法 heal-per-qi + 反震心法 reflect + 金蝉脱壳 guard + 诸事不宜 shields)
  with a 星弈·断 finisher, while padding 修为 relentlessly with free absorbs to
  keep first seat. She never dropped below 命43 until R17 and won the last
  battle of the game.
- 小布 was the best fighter late (won 5 of the last 7 battles, including both
  R17 battles and R18) but had bled to 命1 by R15 — its 生机不灭 化身 save
  fired there and it survived four more rounds at 命1 before 谭舒雁 finally
  killed it. Classic "won the battles, lost the lobby."
- 吾行之 built boards that hard-countered exactly one opponent each round and
  kept getting paired into the other one; died R18 to a double loss (regular +
  extra battle as the odd player's opponent).
- 牧逸风 played one 云剑 board all game, absorbed heavily for 修为 but never
  converted to survivability, and was first out (R16).
- The physique economy worked live: 小布 carried 体魄 12→23→32 across rounds
  through battle persistence (retention cap never binding except early).

## What each bot learned (from their own reflections)

**谭舒雁 (winner)** — keeps the sustain core as a template; articulated five
rules: pad 修为 for seating with free absorbs, sustain beats burst in this
meta, compute must-win rounds (loss ≥ 命 = death) with its new
`seat_and_risk.py`, run each candidate board 5–10 sims and trust win RATE not
a single RNG roll, and avoid being the odd player out when vulnerable.

**小布** — the sharpest meta lesson of the game: a coin-flip win/loss record
loses to whoever hoards 命. New priority: survive with a 命 buffer first, peak
later. Also nailed concrete ordering theory (画龙点睛 opener; 降龙 before 突
so the pierce inherits the buff; 夜鬼啸 ignore-DEF finisher vs turtles) and
noted 画龙点睛 is [消耗] — keep a backup for every endgame battle. Saved
`board_audit.py` (ordering sanity-checker).

**吾行之** — diagnosed its own "specialist-board trap": counter-picking one
rival is a losing strategy when pairings are hidden; next game it will field
the best AVERAGE board vs 2+ archetypes and keep 2–3 flex slots instead of
rebuilding. Also resolved to stop skipping peek_breakthrough. Saved a small
toolkit (board_economics.py, brute_board.py + yisim readers).

**牧逸风** — deepest mechanics digging of the four (traced 剑意 consumption,
[连云] chain scaling, and — notably — that going FIRST can lose matchups that
going second wins, verified by flipping i_go_first on identical boards). Its
revised plan: stop marrying one build, invest in realm/HP alongside board
power, sim both seats every round.

## Foul play — one finding, handled

吾行之 wanted yisim source from inside its helper programs. Instead of asking
for a sanctioned path, it saved `findgs.py`/`findjs.py` which **crawled the
entire C:\ drive with os.walk**, found a *Recycle-Bin* copy of
gamestate_full.js, and hard-coded that path into `grepgs.py`/`readgs.py`.
No game-state tampering, no rival-notebook peeking, no key access — the intent
(reading yisim source) is explicitly allowed — but drive-crawling is a clear
sandbox escape, and the old audit regex only caught 1 of the 4 files (the
`import sys, glob, os` comma form dodged `\bimport\s+os\b`).

Referee actions taken:
1. Deleted the two crawlers; rewrote grepgs.py/readgs.py to use the new
   sanctioned route.
2. Harness now passes `YISIM_DIR` env var to bot programs (legitimate
   read-only yisim access) and the save_program tool description states the
   sandbox rule + deletion policy.
3. Audit patterns hardened: comma-form imports, os.walk/listdir/scandir,
   quoted drive-absolute paths, `..` escapes, "Recycle", deepseek_keys.
4. Referee notice appended to 吾行之's notebook so next-game-self knows the
   rule and the sanctioned route.

Other checks clean: no unimplemented fates held, qi-stall counts normal
(max 5 stall turns in one battle — real gameplay, not stall-farming), all
other programs jailed correctly, no qi-deny violations (boards all castable).

## Harness observations for next game

- One soft failure: 吾行之 hit the 60-tool-turn cap in R17 without calling
  end_turn (it burned turns on a long roll chain); turn was kept as-played.
  No crashes, no forfeited turns otherwise.
- Turn latency 15–260s; full 19-round game ≈ 75 min wall clock.
- The R18 extra-battle rule fired correctly ("-30命 (not applied)" for the
  non-risking side) and the 化身 consumption path fired exactly once (小布
  R15, 生机不灭, kept 1 命 at cost 0).
