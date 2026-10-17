# Game 7 — learning report (2026-09-18, model deepseek-chat, seed 207)

**Result:** 小布 (pid3) DEFENDS its title — 命22 after 18 rounds, winning a
genuine heavyweight duel: from R15 it was heads-up vs 谭舒雁 at 41–41, they
traded kills (谭 took R16, 小布 took R17–18). Eliminations: 吾行之 R12,
牧逸风 R14 (died at 命1 fighting ghost copies of the champion two rounds
running), 谭舒雁 R18. Titles now: 谭舒雁 4, 小布 2, 吾行之 1.

First game with the 1200-eval search budget and per-call search logging.

## The decisive margin

小布's win condition vs 谭舒雁 was its own game-6 discovery executed live:
厄劫缠身's [开局] same-slot downgrade crippled 谭舒雁's 星弈·断+1 in the R17
and R18 fights. Its review then locked that tech into a 100%/100% recipe.

谭舒雁's review claimed the most painful miss of the series ("one merge =
the game": a third 静气心法 sat unmerged in hand at R18). **CORRECTION
(user-prompted re-check, 2026-09-18)**: the claim fails twice. (a) Its
simmed fix (静气心法+2 AND +1 together) was not craftable — merging needs
identical-level pairs, so a lv3 costs four lv1 copies; it held lv2+lv1+lv1.
(b) Re-simmed against 小布's EXACT final board (with 厄劫缠身+1, which
downgrades the same-slot card at battle start), every variant loses 0/7 —
as fielded, legally merged (+1/+1), or even the illegal +2&+1. Its "[SIM
1rep]" tag was the giveaway: one rep, against a stale opponent board. The
review prompt now carries a REACHABILITY RULE (count your copies; sim vs the
exact final board, 3+ reps) to prevent this class of poisoned lesson.

## Search-lock audit (new logging, 23 calls this game)

The logging shows constraint discipline is now real strategy:

- 牧逸风 ran a textbook refinement arc vs the champion: locked its sword
  cores → 0%; dropped all locks → 100% one seat; re-locked around the DEF
  trio the sweep surfaced (诸事不宜/龟甲阵+1/天机·逆施) → 100%/100%. It now
  holds sim-verified counters to every rival — its play-side problem remains
  the weak midgame that killed it by R9.
- 小布 locked its four-card engine and confirmed variants around it; also
  re-verified with pure slot-locks (起势@0, 厄劫缠身@2).
- 谭舒雁 locked its star core and found a 100/100 anti-小布 board once it
  added the career-5 pool.
- 吾行之 logged 10+ searches — every one 0%, including opp_cards-override
  models of upgraded enemies. Two games of exhaustive search now say the
  same thing: its problem is not the board, it's the engine-less archetype
  and the economy curve that builds it. Its notebook finally corrected a
  long-standing false claim (the 加攻-scaler board "beats sustain 100%" —
  retested at 0%).

Budget usage stayed modest (biggest single call: 71 evals; totals well under
1200) — the early-stop is aggressive, which the depth test showed is usually
fine, but with the doubled budget there is headroom to raise search patience
if we want more thorough climbs.

## Harness notes

- Two 境5-cap bugs found BY A BOT and fixed after the game: SITREP offered a
  "境6" breakthrough (the realm table has a key 6 the game never uses), and
  peek_breakthrough threw at max realm instead of saying so. 小布 worked
  around both correctly in-game ("SITREP is LIE; ignore").
- No referee flags: no qi stalls, no program escapes, no unimplemented
  fates, zero turn-cap hits.
- Ghost rule note: 牧逸风's death by ghost battles (R13–14) is the first
  elimination driven purely by odd-player draws against a stronger player's
  copy — worth watching whether bots start planning 命 buffers around it.

## Meta after seven games

小布's force engine has now won twice in a row, and everyone's notebook
contains a sim-verified 100% counter to it (牧逸风's DEF trio, 谭舒雁's
merged-静气 sustain, even 吾行之 knows what beats it — it just can't build
it). Game 8 is a referendum on execution: three bots hold the answer on
paper; the champion's edge is that it executes its own paper.
