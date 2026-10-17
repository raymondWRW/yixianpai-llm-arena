# Game 8 — learning report (2026-09-18, model deepseek-chat, seed 208)

**Result:** 牧逸风 (pid0) wins its FIRST title — surviving at 命1 from R15 and
closing with kills in R16 (吾行之 −20), R17 (小布 −21) and R18 (吾行之 −28,
while 谭舒雁 died to a ghost of 吾行之 in the same round). Every seat has now
won at least once: 谭舒雁 4, 小布 2, 吾行之 1, 牧逸风 1.

First game with humanized battle logs + per-turn STATE lines, hand history,
and the REACHABILITY RULE in review.

## The win

The 0-for-7 bot finally converted its notebook into play. Its engine —
assembled mid-game after picking 符咒师 at R2 — is a qi-battery burst:
聚灵心法 (+1 qi/turn) → double 凝意诀 (qi + 剑意) → 灵犀剑阵 (剑意→qi burst)
→ 飞灵闪影剑+1 → 白鹭灵剑 (qi-scaled ~37) → 御空剑阵+1 chase → 万法归灵剑
LAST as the dump. Kills in 7–9 turns, four rounds straight, while one loss
from elimination every round. Its review traced the whole chain from the
humanized R18 battle log line by line, then locked the six core cards and
confirmed 100/100 vs every rival's final board.

Notably it already self-criticizes the winning game: "sidejob=2 符咒师
SUBOPTIMAL" — the engine used sect cards + 镇魂封元符 only; it wants a
different R2 pick despite the title.

## Review-loop health

- **The poisoned lesson is gone.** 谭舒雁's false "one merge = the game"
  entry (disproven last cycle) does not appear in its rewritten notebook —
  the reachability audit did its job. Its new notebook is a single-recipe
  doctrine (紫气东来 slot-1 star board) with 100/100 claims vs all three
  rivals at 8 reps + full-log verification. Better methodology; game 9 tests
  whether the recipe survives contact.
- 吾行之 found a one-move diagnosis with the new tools: its R18 board died
  to ORDER — 火灵阵+1 buried at slot 3; moving it to slot 1 flips the pid0
  matchup 0%→100% (5 reps both seats). "Root cause = board order, not
  cards."
- 小布 kept its ramp doctrine but rebalanced the recipe front-loaded after
  losing the seat race late.
- Search-lock audit: 牧逸风's calls now lock 5-6 named engine cards and
  probe one variable at a time — the constraint discipline the game-7
  refinement arc taught it. 23 review search calls total, all within
  budget.

## Harness verification

- Humanized logs flowed end-to-end: bots quote lines like "聚灵心法 →
  灵犀剑阵 6→6qi" with correct attribution; no bot confusion about who
  played what (a recurring silent error source in earlier games' reviews).
- STATE lines are being read: 牧逸风's engine trace cites per-turn qi
  totals; 吾行之's order diagnosis leans on them.
- Hand history: present in battle_log headers; no bot repeated the
  "unmerged copy" class of error.
- Referee: clean — no flags of any kind. Zero turn-cap hits.

## Meta after eight games

All four seats have now won. The archetype wheel — sustain-star (谭舒雁),
force-ramp (小布), qi-dump (牧逸风), fire-order (吾行之) — is fully armed,
and every notebook holds sim-verified counters to at least two rivals. The
differentiator has shifted from knowledge to two things: economy execution
(getting YOUR engine to its levels before R12) and seat control. Game 9 is
as open as the arena has ever been.
