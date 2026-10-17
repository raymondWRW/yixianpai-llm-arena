# Game 18 — learning report (2026-09-27, model deepseek-chat, seed 218)

**Result:** 小布 wins its FOURTH title (g6, g7, g15, g18) — 命20 after 17
rounds, a natural finish. It entered R14 third on 命 (20, behind 谭舒雁 43
and 牧逸风 25) and never lost again: held 命20 untouched from R14 to R17
while 谭舒雁 collapsed from 43 to 0 in two rounds and 牧逸风 fell R17.
Order out: 吾行之, 谭舒雁, 牧逸风. Fates 16/16; zero turn caps, zero crashes.

First game with no round cap (the old R20 cap was a harness invention —
user ruling) and the first with review tool calls logged.

Corrected titles: 谭舒雁 8, 小布 4, 牧逸风 3, 吾行之 1, + 2 unfinished
(games 9 and 17, truncated by the old cap).

## Winning board: its force engine, now tempo-integrated

[气若悬河+1, 冲霄破浪, 踏破九霄+1, 势如破竹+1, 崩拳·降龙+1, 崩拳·寸劲+1,
朝气蓬勃+1, 崩拳·突] — the g15 synthesis refined: 踏破九霄 (身法) is now
UPGRADED and joined by 冲霄破浪, so the agility line reaches the 10-身法
auto-chase more reliably; nearly every slot is levelled. The tempo lesson
from game 13's rules update has gone from "fielded once" (g13) to "in the
winning list" (g15) to "levelled and doubled" (g18).

## Open review: now measured — and used

Review tool calls were logged this game (201 calls across four bots, plus
42 search_board calls). Every bot read rival files; none ignored them:

| Bot | Rival playbooks | Rival ledgers | Rival economy |
|---|---|---|---|
| 小布 (winner) | 牧逸风, 谭舒雁, 吾行之 | — | 谭舒雁, 牧逸风 |
| 牧逸风 | 小布, 谭舒雁 | 小布, 谭舒雁 | 谭舒雁 |
| 吾行之 | 谭舒雁, 牧逸风 | 小布 | 小布 |
| 谭舒雁 | 牧逸风 | 牧逸风 | 小布 |

All four also queried board_db for rival boards (name='any'). The champion
was the most thorough reader — the only bot to open all three rival
playbooks. Rival reads are still a small slice of review effort (roughly
3-7 of ~50 calls per bot; the bulk remains sims, battle logs and search),
which is sensible: the files are a map, the sims are the terrain.

The earlier "no notebook cites a rival" observation (g16-17) is now
explained: bots read rival files but record the conclusions as their own
matchup notes rather than attributing them.

## Referee

Clean. 吾行之 tried to run a program (x.py) it had never saved — harmless
"not found". Program audit flags are all long-standing sanctioned readers
(YISIM_DIR walkers) plus 牧逸风's old cand.py, which imports subprocess but
never calls it.
