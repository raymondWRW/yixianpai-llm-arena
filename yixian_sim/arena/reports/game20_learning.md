# Game 20 — learning report (2026-10-03, model deepseek-chat, seed 220)

**Result:** 小布 wins its FIFTH title — 命49 after 18 rounds, without losing
a single point of 命 after R14. 谭舒雁 led the lobby at 命53 going into
R16, then lost three straight head-to-heads to 小布 (53 → 35 → 14 → 0).
Order out: 吾行之, 牧逸风, 谭舒雁. Fates 16/16; one turn-cap hit; no
crashes. Ran entirely off-peak (Saturday).
Titles: 谭舒雁 8, 小布 5, 牧逸风 3, 吾行之 2, + 2 unfinished (g9, g17).

## Why the leader lost: an empty hand

谭舒雁's hand was EMPTY in rounds 16, 17 and 18. It had absorbed and
merged every spare card to win the 修为 seat race, so its final boards had
only 6 of 8 slots filled (empty slots fire a plain normal attack) — and it
no longer held 诸事不宜. Both bots' reviews converged on the same fact from
opposite sides:
- 小布: "I won the lobby BECAUSE 谭舒雁 fielded the wrong board. Her own
  notebook has the counter" — her 8-card recipe with 诸事不宜 (−6 attack on
  my next two hits) beats my final board in both seats, 3 reps each.
- 谭舒雁: "the 内伤 board must be 8 slots and must include 诸事不宜 vs 崩拳
  burst — removing it drops the 小布 matchup from 100% to 20%/0%."

New lesson for the lobby: the 修为 race has a hidden cost. Absorbing every
card wins the seat but can leave you unable to field your recipe. (Checked:
the recipe is legal — zero [消耗]/[持续] cards — so nothing in the rules
blocked it.)

## What each bot took away

- **小布 (winner)** won without 威震四方 — the force-cap fix it found last
  game. It never drew one this game (zero appearances in deals or rolls),
  so the 7-card burst board carried it alone.
- **谭舒雁** fielded last game's lesson (白鹤亮翅 as the qi lever) but lost
  the slots to over-absorbing. Its rewritten rule: keep enough cards in hand
  to field 8 slots including the anti-burst card.
- **牧逸风** quantified the threshold for its no-万法 board: 百鸟灵剑诀+1 or
  白鹭灵剑+2 (or two 巨鲲灵剑+1); 白鹭灵剑+1 alone loses.
- **吾行之** found a board from cards it already held that beats 小布's final
  board 100% going second (0% going first) — seat-dependent, so it now knows
  exactly how much the 修为 race matters in that matchup.

## Harness checks

- **Final standings in the review prompt: working.** All four bots recorded
  小布 as the winner (last game two recorded the wrong winner), and ledger
  entries now carry the real arena game number.
- **Ledger boundaries: working.** Game-20 entries read back cleanly under
  the new harness-only marker.
- **Open review:** every bot read rival files again. All three losers read
  the winner's playbook, ledger and economy; the winner read all three rival
  playbooks — which is how it spotted 谭舒雁's unfielded counter.
- Referee: clean.
