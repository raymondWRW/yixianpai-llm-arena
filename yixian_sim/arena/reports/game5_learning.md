# Game 5 — learning report (2026-09-17, model deepseek-chat, seed 205)

**Result:** 谭舒雁 wins its FOURTH title (4 of 5) — but by the skin of its
teeth: 命10 after a winner-take-all R19. Eliminations: 吾行之 R13, 牧逸风 R17,
小布 R19. First fully clean-rules game (correct sidejob pools, ≤2 [消耗]/[持续]
boards, announced matchups, reroll cap, review powers).

## The game

- Sidejob picks finally diversified, and deliberately: 谭舒雁 took 符咒师 —
  the pool it had BY ACCIDENT in game 4's bug and liked; 牧逸风 took 阵法师
  to feed its formation archetype legally; 小布 and 吾行之 took 命理师.
- The endgame was the best theater yet: R18, 小布 (命35) beat 谭舒雁 down to
  命10; R19 was mutual-lethal — and 谭舒雁's assembled star engine
  (天元心法 → 众星拱月+1 → 紫气东来 → 梅开二度 doubling 镇魂封元符's 40%
  max-HP strip + qi drain → 星弈 payoffs) killed the force tank in 8 turns
  for −35.
- 小布 was odd-player-out three rounds straight (R14–16) and WON all three
  ghost battles, so it carried 命35 into the final — the ghost rule read
  correctly every time (its wins over the real 谭舒雁's ghost cost her
  nothing; its own risk never materialized).
- 牧逸风's 云影化身 fired at R16 (kept 1 命) — the first 化身 consumption
  since game 1 — before 小布's −30 finished it at R17.

## What each bot learned

**谭舒雁** — wrote the full star-engine recipe structurally (slot roles, why
梅开二度 must sit immediately before 镇魂封元符, 打→点→断 ordering) and — for
the first time — reasons about the NEW legality rule inside the build:
"[消耗]/[持续] count = 天元+镇魂 = exactly 2 = the max. Do NOT add a 3rd."

**小布** — best analytical entry of the game: it re-simmed its R19 loss in
review with card-level variants and found the matchup flips entirely on
LEVELS and seat ("same multiset, just upgraded, flips LOSE→WIN. Levels > a
fancy new card"). Its conclusion — keep the build, out-level and out-seat
next time — is exactly right per the sims it ran.

**牧逸风** — identified the power-curve problem correctly this time: its
fixed-damage 剑阵 board won R1–R8 then lost 8 of 9 as scaling decks
(star-power, 气势, 五行) passed it, compounded by fielding lv1 cards at R17.
Documented all three rivals' engines card-by-card.

**吾行之** — died first again despite its game-3 title. Root causes it wrote:
a 30+ 修为 seat deficit (58 vs 82/93/94 — went second in nearly every late
battle) and a 五行 ATK board that doesn't scale into the late peaks.

## Rules verification (all five new rules live)

- Sidejob pools correct end-to-end: 谭舒雁 (符咒师) drew 护灵符/火云符/
  镇魂封元符; 小布/吾行之 (命理师) drew 天谕/天运/卜命/吉运初显; 牧逸风
  (阵法师) drew 邪蛊阵/冲击阵纹/龟甲阵/辟邪阵纹.
- Board legality: every fielded board all game held ≤2 [消耗]/[持续] cards;
  牧逸风 ran exactly 2 (邪蛊阵+碎杀阵 early, later 邪蛊阵+万花迷魂阵), and
  谭舒雁's notebook shows bots now BUILD AROUND the cap.
- Reroll floor behavior visible: several bots ran their banks to 0 in the
  endgame (小布 spent 20+ in single rounds) — no one wasted grants above 25.
- Ghost battles: three consecutive rounds of "[extra for pid3]" resolved with
  only the ghost-fighter at risk.

## Referee findings

Clean. No unimplemented fates, no qi-stall flags, one turn-cap hit (吾行之
R9 during a 30-roll fishing spree — its own notebook now calls this out as a
seat-deficit cause). Programs: 牧逸风 added grepall.py — os.walk strictly
inside YISIM_DIR (sanctioned route, same as 小布's findfates.py). No
escapes, no rival-dir access.

## Meta after five games

谭舒雁 4 titles, 吾行之 1. But the gap is closing measurably: game 4 was won
at 命44, game 5 at 命10, and 小布 has now beaten the champion's board in
direct fights twice across g4–g5 endgames. Every bot's notebook now contains
(a) the destiny formula, (b) seat/修为 doctrine, (c) at least one named rival
engine with a counter-plan. The review powers got real use: 小布's
level-variant sims and 谭舒雁's legality-aware recipe both came out of the
post-game conversation.
