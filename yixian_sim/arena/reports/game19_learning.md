# Game 19 — learning report (2026-09-29, model deepseek-chat, seed 219)

**Result:** 吾行之 wins its SECOND title — its first since game 3, sixteen
games ago — with 命31 after 17 rounds. It entered the endgame level with
小布 (both 命31 at R13) and beat 小布 in four of the last five rounds,
including the R17 kill. Order out: 牧逸风, 谭舒雁, 小布.
Titles: 谭舒雁 8, 小布 4, 牧逸风 3, 吾行之 2, + 2 unfinished (g9, g17).
Fates 16/16; one turn-cap hit (牧逸风), no crashes. Finished 05:43 UTC,
inside the off-peak window.

## How 吾行之 won: a drain engine nobody had seen

Final board: [万花迷魂阵, 回响阵纹, 水灵·泉涌+1, 水灵·波澜+1, 水灵·纳百川,
水灵·汹涌+1, 金灵·巨鼎落, 金灵·铁骨]. 万花迷魂阵 applies a [减攻] stack every
turn and drains HP per stack; 回响阵纹 in slot 2 retriggers it, so the drain
fires twice a turn and ignores 防 and 气势. The same [减攻] stacks shrink
小布's force-scaled hits. After sixteen games of "a strong board that loses
to one archetype", this is the first 吾行之 board that beat the champion
archetype directly.

Its review then found what it calls a universal board — the drain engine
plus 不动金刚阵+2 (anti-burst survival) and 辟邪阵纹 (blanks 谭舒雁's 内伤
ticks; 牧逸风's game-14 tech) — simming ~100% against all three rivals,
both seats, base and +1. It checked reachability honestly: 不动金刚阵+2
needs four copies, which it marks as a stretch.

## What the others learned

- **小布 rediscovered a lesson it had lost.** Its 崩拳·寸劲 hit for 37
  instead of the expected 44–58 because 气势 is capped at 6 and its
  generators make 8–9 a turn — everything above the cap is thrown away. It
  cited the engine source line and found the fix: 威震四方 raises the cap to
  9, and the swapped board beats all three rivals. The twist: its **game-6**
  notebook already said "威震四方 = cap raiser — LOCK IT". That rule was lost
  in the pre-ledger era, when notebooks were rewritten from scratch each
  game — the forgetting problem the ledger/playbook split was built to fix.
- **谭舒雁 overturned its own long-held belief.** 厄劫缠身 — the card it has
  hunted for six games — sims only 33%/0% against 吾行之. The real lever is
  白鹤亮翅 as a qi enabler, which brings its 内伤 clock online a turn earlier:
  100%/100% against 吾行之 and 牧逸风. Against 小布 it found no winning
  board in its whole sidejob pool and wrote: don't fight him head-on.
- **牧逸风 found a board it could have fielded.** Without 万法归灵剑, a 巨鲲灵剑
  chase into a qi-scaled 白鹭灵剑 beats 小布's exact final board both seats —
  and it held every piece of that board during the game, never fielded
  together. It also had the lowest 修为 (58) and lost every seat race.

## The draw rules landed

Both bots that chased phase-5 cards now quote the real odds from
pool_cards(): 牧逸风 "6 copies, 2%/roll" (it believed 9% last game) and
谭舒雁 "2.2%/roll, 7.1%/deal". Their plans now include fallback boards
instead of betting a game on one rare card.

## Harness fixes from this wrap-up

1. **Ledger entry boundaries.** The harness marked entries with "## Game N",
   but bots write their own "## Game …" headings inside entries, which faked
   extra boundaries (4–6 per ledger) and broke `ledger(last_n)`. Entries now
   use a harness-only marker ("==== LEDGER ENTRY · Game N ===="); existing
   ledgers migrated (backup: bots_state_pre_ledgerfix/). Bot text untouched.
2. **Wrong winner in two ledgers.** 谭舒雁 and 牧逸风 recorded 小布 as the
   winner — the review prompt only told each bot its own placement, and the
   observation snapshot is from the start of the last round, when 小布 was
   still alive. Review prompts now open with the game number and the full,
   authoritative final standings. The two wrong game-19 entries were left as
   written (bots own their memory); the next review will show the truth, and
   both will read 吾行之's ledger via open review.
3. Mid-game off-peak pausing shipped just before this game (not needed:
   the game ended 17 minutes before peak).
