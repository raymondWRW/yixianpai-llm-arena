# Game 13 — learning report (2026-09-25, model deepseek-chat, seed 213)

**Result:** 谭舒雁 wins its EIGHTH title — the most dominant since g4: 命63
over the full 20 rounds. Eliminations: 吾行之, 牧逸风, 小布. Titles:
谭舒雁 8, 小布 3, 吾行之 1, 牧逸风 1. Fates 16/16 ranked.

First game on the mechanics-literate stack: COMBAT MECHANICS glossary in
RULES, Oracle-explores/yisim-decides search (4000-eval budgets), and the
ledger + merge-contract playbook memory.

## What the new stack changed, measurably

- **Tempo entered the meta.** 身法/chase cards appeared on fielded boards 12
  times (previously ~0 outside 小布's 崩天步 staple) — 11 of them 小布,
  which built 冥影身法/灵玄迷踪步 agility lines alongside its force ramp.
  Its playbook now discusses the 10-身法-auto-chase rule explicitly. The
  audit tools can finally see it too (agi in STATE lines, extra_actions in
  card_stats).
- **Memory is compounding instead of resetting.** All four ledgers carry
  their first permanent entries (16-45 lines each), and the merged playbooks
  grew to 75-94 lines with game-tagged rules carried forward — no bot
  started from scratch this review.
- **The champion didn't need tempo — it sharpened its clock.** Winning
  board: 厄劫缠身×2 + 血光之灾×2 + 杯弓蛇影 with 梅开二度 doubling and
  天星·牵引/命运轮回 support. Third straight title on the 内伤 archetype,
  each iteration cleaner than the last. 命63 says the gap this game was
  execution, not knowledge.

## Referee

Clean: no program violations, no qi-stall flags, no cap hits; search calls
all lock-disciplined and inside the 4000-eval budgets (Oracle pre-filter +
yisim verdicts throughout — no finalist disagreements escalated to
notebooks unverified).

## Standings after thirteen

谭舒雁 8 / 小布 3 / 吾行之 1 / 牧逸风 1. The dynasty problem is now the
experiment's most interesting question: every rival has the knowledge, the
tools, permanent memory, and (as of this game) tempo literacy — and the
champion still converts faster. Whatever breaks the 内伤 clock will
probably come out of someone's ledger accumulating evidence across games
rather than a single review's insight.
