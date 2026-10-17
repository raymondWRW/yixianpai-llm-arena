# 牧逸风 — game ledger (append-only archive)

==== LEDGER ENTRY · Game 13 ====
GAME (牧逸风, sidejob=阵法师5, 境5, 修为87) — RESULT: 2nd of 3 survivors, 命 hit 0 (-23) at R17. Final alive: pid1 谭舒雁 命63, pid3 小布 命1.

Battles: R1 W/R2 L/R3 W/R4 W/R5 W/R6 W/R7 L/R8 W/R9 L/R10 W/R11 W/R12 L/R13 W/R14 L/R15 L/R16 L/R17 L. Lost the endgame streak R14→R17 entirely.

*** TOP DISCOVERY: 万法归灵剑 NUKE is the answer vs pid1 (谭舒雁). ***
Winning board (100% BOTH seats vs pid1's ACTUAL R16/R17 board, 5 reps, yisim):
  ["聚灵心法+1", "辟邪阵纹+1", "天罡聚力阵", "飞灵闪影剑+1", "白鹭灵剑", "化灵诀", "巨鲲灵剑", "万法归灵剑+1"]
WIN % vs ALL rivals (5 reps each): pid1 100/100, pid2 100/100, pid3 100/100 — and 100/100 even vs their +1 boards (except pid1+1 = 100 first / 0 second).
WHY: 聚灵心法 replenishes qi each turn; 辟邪阵纹 gives hexproof (absorbs her 内伤 instances) + 10 def; 飞灵闪影剑 generates qi; 白鹭灵剑 and 万法归灵剑 both scale off REMAINING qi. By t7 I bank ~10-12 qi and 万法 hits for ~61 dmg -> one-shots her 119hp from ~mid.
This is EXACTLY the 万法 recipe my old notebook had — I FAILED TO DRAW 万法 all game. It's 境5 in my pool (×6). Hunt it HARD once 境5 reached (R12+).

*** SEAT WAS THE DECIDING FACTOR vs pid1. ***
My OLD R16 board ["聚灵心法+1","天罡聚力阵","飞灵闪影剑+1","巨鹏灵剑+1","白鹭灵剑","巨鲸灵剑+1","巨鲲灵剑","形意剑+1"] = 100% FIRST / 0% SECOND vs her actual board. pid1 had 修为104 > my 87 => she ALWAYS went first => I ALWAYS lost. The 万法 board fixes this by winning going second too.

*** BUG/REGRESSION I SUSTAINED: 巨鲸灵剑 auto-DOWNGRADED lv2->lv1 in R16 AND R17 *** (log: "downgrades Giant Whale Spirit Sword (level 2) to (level 1)"). Cause: I fielded 巨鲸灵剑+1 in R16 but the R17 take-back/merge dance left only a lv1 copy on board. In R17 my board ended up mostly lv1 (card_stats: 巨鲸 16 not 20). FIX: after any take/merge, re-verify board levels; never let a +1 downgrade to lv1.

*** R15 LOSS to pid3 (小布) — CAUSE: bad board, not matchup ***
I fielded a costly mishmash ["聚灵心法","凝意诀","飞灵闪影剑","巨鲲灵剑","云剑·游龙","巨鹏灵剑","地煞剑","形意剑+1"] with many lv1 cards; 小布 ramped 气势 (force cap 12!) and Mighty Force hit me for 28+19. Died t10 at hp -2. My strong R16 board beats his final board 100%/100%. Lesson: DON'T field undereleveled/lv1 mixes late; field the proven 8-card board even if not all upgraded.

*** 小布 (pid3) mechanic: 崩天步 gives agility, 气势(force) cap raised to 12 by 起势/磅礴之势, Mighty Force spends qi for big single hits, Overwhelming Force converts force->def+atk. His clock is burst. Out-damage him fast (万法 does).

*** ECONOMY AUDIT: ***
Over-rolled: R3 (10 rolls + 5 absorbs), R13 (16 rolls!! 0 bank kept), R15 (13 rolls). Massive late-game rolls with no bank.
Under-rolled: R1-R2 (0), but fine.
NEVER DREW 万法归灵剑 despite R13's 16-roll spin + R15's 13 rolls at 境5. Pool dilution: 境5 has 万花/凌波/游龙/剑意激荡/回响/御空/连环/须弥/飞灵 (9 cards ×6 = 54 copies) plus 境1-4 commons. 万法 is 6/54 of 境5 ~ 11% per 境5 draw. Need to roll at 境5 specifically and bank ~15 exchanges for it.
Bank pattern: I kept bank<=9 the whole game; never hit the 25 cap. Grants +6 R13+ wasted each round because I spent them immediately on junk rolls.

FATES picked (defaults): 云雾变幻, 云剑传承, 云海连绵, 云影化身, 储纳灵气. Never A/B tested.
体魄=0 all game (never invested).

Surprise: 化灵诀 (境2, +3qi) outperformed 巨鲸灵剑+1 (20 flat dmg) as slot 6 in the 万法 board — qi feeding the nuke > flat damage.

==== LEDGER ENTRY · Game 14 ====
## Game 14 — 牧逸风 (云剑 sect, sidejob=阵法师5) — RESULT: 1st place WINNER, final 命13 (of 4; pid1 谭舒雁 & pid2 吾行之 dead, pid3 小布 命1 chasing). R20 win ended it.

BATTLES: R1 L(pid3,-2,R1 cheap) R2 W(pid2) R3 L(pid1,-4) R4 W R5 W R6 L(pid2,-10) R7 L(pid3,-10) R8 W R9 L(pid3,-12) R10 W R11 W R12 W R13 W R14 W R15 W R16 W R17 L(pid3,-23) R18 L(pid3,-22) R19 W R20 W(pid3,-32, clinch).
Early losses (R1,R3,R6,R7,R9) were all WEAK undereleveled boards during economy phase — cheap, expected. Then a W run R10-R16, then the dangerous R17/R18 双 loss to pid3 (小布) nearly killed me (命35->13).

*** THE DECISIVE DISCOVERY: the 万法归灵剑 QI-NUKE, but ONLY with a qi-feeding support suite. ***
WINNING BOARD (R20, 100% both seats vs all 3 rivals incl. their +1 boards, yisim 3+ reps):
  ["辟邪阵纹+1", "聚灵心法+1", "百鸟灵剑诀", "引气剑+1", "巨鲲灵剑+2", "白鹭灵剑", "御空剑阵", "万法归灵剑+2"]
Dealt 84 dmg in R20 (two 万法 lv3 firings x ~40-44). Kill engine: slot5 巨鲲 lv3 [再次行动] chases -> slot6 白鹭 (qi-scaled atk); slot7 御空 [再次行动] chases -> slot8 万法 (exhausts qi at 7dmg/pt). Two chases per cycle => 万法 fires EVERY cycle (~40 x2 over 10 turns).
WHY THE SUPPORT SUITE MATTERS (THE key mechanic of this game):
  - 百鸟灵剑诀 [持续]: -1 qi cost to "灵剑" cards +1qi on play; 聚灵心法+1: +1 qi/turn aura; 引气剑+1: +3qi on play.
  - R17/R18 I fielded 万法+1 but with a qi-STARVED board (DOUBLE 巨鲲 draining qi, no 百鸟/引气 feed). card_stats R17: 万法 lv2 fired for 11. card_stats R18: 万法 lv2 for 24. It did NOTHING.
  - VERIFIED: R17 actual board ["聚灵心法+1","辟邪阵纹+1","引气剑+1","巨鹏灵剑+1","巨鲲灵剑+1","巨虎灵剑+2","巨鲲灵剑","万法归灵剑+1"] LOSES going first vs pid3's R17 board (13t, hp -1). R20-style board WINS even going SECOND (10t). => 万法 WITHOUT qi-feeding support is a TRAP.

*** ECONOMY: I never drew 万法 until R16 (economy hist), then leveled it +1 (R16) and +2 (R20). ***
Over-rolled: R7 (11!), R11 (9), R18 (12), R20 (14). R13/R15 (7 each) whiffed. I kept bank<=9 all game; never used the +6 R13+ grants well.
Under-rolled effectively: I should have banked to ~20 for the 境5 万法 hunt once 境5 (R12) reached. Got 万法 only at R16 and only via lucky rolls.

*** KEY MECHANICS VERIFIED THIS GAME (yisim/card_text/logs): ***
- 百鸟灵剑诀 lv2 = +3qi AND -1 灵剑 cost (strict upgrade, search preferred it). Priority merge.
- 御空剑阵: [防]>0 => costs NO qi, gives def, [再次行动]. PERFECT free chase feeding 万法. lv2=+14def.
- 引气剑 lv2: +3qi, and if qi>3 deals 3x2 extra. Both a qi source AND a small hit.
- 巨鲲灵剑 lv3: 16atk +16def +chase. lv2=13. Needs its qi; the -1 cost from 百鸟 helps it fire.
- 万法归灵剑: 5 + k*(ALL qi exhausted); lv1/2/3 k=5/6/7. MUST be last in cycle after qi generators.
- 辟邪阵纹: hexproof absorbs pid3/pid1 debuff instances (厄劫 downgrade + 内伤 seeding) AND gives def. Tech vs pid3 & pid1.
- 崩拳(小布): hp-cost cards (饿虎扑食 12hp+4体魄, 崩拳·突), 气势 cap raised to 12, 磅礴之势 converts force->def. His clock is burst 23-33 hits. Out-tempo him.

*** FATES: still default picks (云雾变幻/剑池问心/云海连绵/云影化身/剑韵修炼). A/B sim with my_extra_fates showed NO flip in the decisive matchups. 储纳灵气 (qi) noted as synergy-relevant but untested cleanly. LOW priority.

SURPRISE: The board that dominated was NOT my long-standing 云剑/巨鲸 recipe (g11-g13 always fielded 云舞诀/云剑·X/巨鲸) — those always lost late vs 谭舒雁. It was a 灵剑-qi-nuke. Trust the 万法 line over the 云剑 line from now on.

==== LEDGER ENTRY · Game 15 ====
## Game 15 — 牧逸风 (云剑 sect, sidejob=阵法师5) — RESULT: 3rd place, 命0 at R17 (only pid3 小布 survived). 修为83, 境5.

**BATTLES:** R1 W(pid3) R2 W(pid1) R3 L(pid2) R4 L(pid1) R5 W(pid2) R6 W(pid1) R7 L(pid3) R8 W(pid2) R9 W(pid1) R10 W(pid2) R11 L(pid3) R12 W(pid2) R13 L(pid3) R14 L(pid1) R15 L(pid3) R16 W(pid2) R17 L(pid3). Beat pid2 100% (水灵), beat pid1 early then lost late, **lost to pid3 小布 the last 3 meetings (R13,R15,R17) — that's what killed me.**

**ROOT CAUSE = FAILED TO ASSEMBLE THE 万法 万法归灵剑 QI-NUKE (my own g14 WINNING recipe).** My R17 final board was the OLD 云剑/巨鲸 placeholder: ['化灵诀','凝意诀','云舞诀','引气剑+1','灵感剑','飞牙剑+1','巨鲲灵剑+1','白鹭灵剑+1'] — NO 万法, NO 辟邪阵纹, NO 聚灵心法. My notebook explicitly warns this always loses late. VERIFIED FIX: the g14 万法 board wins 100%/100% (both seats) vs ALL THREE rivals incl. their +1 boards (sim_matchup, 5-6 reps). R17 loss replay: 万法 board beats pid3's exact final board in 6 turns going first (万法 fired 68 dmg); search improved it to also win vs pid1+1 going second: ["辟邪阵纹+1","聚灵心法+1","百鸟灵剑诀","引气剑+2","云剑·点星","巨鲲灵剑+2","白鹭灵剑","万法归灵剑+2"] (100%/100% all 3 rivals, base AND +1).

**CATASTROPHIC ECONOMY ERROR (the real game-loser):** R11 I was dealt BOTH 百鸟灵剑诀 AND found 聚灵心法 — I rolled AWAY 百鸟 AND rolled/absorbed 聚灵心法 (for 修为). R12 I rolled 百鸟 away AGAIN and absorbed 聚灵心法 AGAIN. These are the two CORE 万法-suite cards. My notebook M8 says EXACTLY "when a 万法-suite card appears, HOLD it" — I violated it 4 times. Also: R9 9 rolls, R10 9 rolls, R12 15 rolls, R16 13 rolls ALL with bank going to 0-1, wasting the +6 R13+ grants.

**ROLL MATH:** R1-R8 averaged ~1 roll/round (under-rolled early). R9-R16 averaged ~10 rolls/round (over-rolled, hit nothing engine-relevant). NEVER drew 万法 in this game despite TWO huge roll rounds at 境5 (R12: 15 rolls, R16: 13 rolls). 万法 is 6/54 of the 境5 pool ≈ 11%/draw.

**pid3 小布 (命理师7) MECHANIC (traced in R13/R15/R17 logs):** 血光之灾 [开局] seeds 1 内伤 + 天星·御心 retriggers that [开局] TWICE => double-seeds 内伤 on me; 修罗吼 adds 4 more to BOTH; his 天星·御心 also heals him +4-6/turn. Net: I bleed 8-11 hp at MY turn start every turn (visible as "reduced 牧逸风 hp by 8" recurring), ignoring all my 防. Plus 崩拳·降龙/封 force burst (24 hits). **The answer is 辟邪阵纹 (4 hexproof stacks absorbed the seeds — verified in full_log) + killing him FAST with 万法 before the 内伤 clock matters.** Out-tempo, don't out-sustain.

**KEY MECHANICS CONFIRMED (card_text + logs):**
- 万法归灵剑: 5 + k×(qi exhausted); lv1/2/3 k=5/6/7. MUST be last in cycle after qi gens. lv3 with 13 qi = 86 dmg (full_log verified).
- 百鸟灵剑诀: lv1 +1qi; **lv2 +3qi (HUGE) + -1 灵剑 cost**; lv3 -2 cost. Priority merge.
- 云剑·点星: [灵气]+2/3/4 AND 0atk +1/atk per remaining qi. Double-duty qi gen — search preferred it over 御空剑阵 vs pid1+1.
- 御空剑阵: [防]>0 => free, +8/14/20 def, [再次行动]. Free chase feeding 万法.
- 辟邪阵纹: 3/4/5 hexproof; +10/14/18 def if a 持续 was played. Tech vs pid1(厄劫 downgrade) AND pid3(内伤 seed).
- 聚灵心法: lv1 +1qi/2turns; **lv2 +1qi EVERY turn (essential)**.

**FATES:** still defaults (云雾变幻, 剑韵修炼, 云海连绵, 储纳灵气, 剑阵守护). 剑阵守护 (playing slot1 grants +9 def) A/B-tested via my_extra_fates=[1001] in full_log — no observable flip (I won 7t either way). Low priority.

**SURPRISE:** The failing board was literally my own old recipe, and the winning board was literally my own old recipe — I had the answer in my notebook the whole time and just failed to DRAW AND HOLD the cards.

==== LEDGER ENTRY · Game 16 ====
## Game 20 — 牧逸风 (云剑 sect, sidejob=阵法师5). RESULT: **1st place WINNER, final 命40** (of 4; pid2 吾行之 dead R13, pid1 谭舒雁 died ~R19, pid3 小布 died R19).

BATTLES: W W W W W L W W L L L L W L W W W W W W (R1-R19, 20 fights incl. double-battles). Losses R6(pid2)/R9(pid1)/R10(pid2)/R11(pid1)/R12(pid3)/R14(pid3) all came during my ECONOMY PHASE before 万法 was online — cheap and expected. From R15 on I assembled the 万法 killer and won 6 of my last 7.

FATES: 云雾变幻, 机缘造化, 储纳灵气, 云影化身, 休养生息 (境2@R4, 境3@R7, 境4@R9, 境5@R12). A/B sim with 储纳灵气[id62] = no observable flip. Still low priority.

FINAL BOARD (R19, the WINNER): ["辟邪阵纹+1","聚灵心法+1","百鸟灵剑诀+1","引气剑+1","巨鲲灵剑+2","云剑·点星","白鹭灵剑","万法归灵剑+1"] — 修为97, 境5, maxHP111.

*** THE DECISIVE DISCOVERY: 万法归灵剑 (Dharma Spirit Sword) LEVEL is the entire game — RE-CONFIRMED. ***
R17: 万法 lv1 fired for **30 dmg** (his 40 def ate it); slogged 11 turns, won only thanks to 白鹭 chipping.
R18: 万法 lv1 = 70 dmg.
R19: I ROLLED 15× and MERGED 万法 lv1→lv2 = **80 dmg on t7, killing 小布 68→-12 outright.**
card_stats R19: 万法 lv2 = 80 of my ~130 total dmg. Search verdict: lv2 万法 KILLS t6-7; lv1 needs 11 turns. THE MERGE WAS THE GAME.

*** CARD AUDIT (card_stats): 万法 is the only slot that matters; everything else exists to feed it qi. ***
R19: 万法 lv2=80dmg; 白鹭=21; 巨鲲 lv3=13dmg+16def(chase); 引气剑/点星=qi+small hits; 辟邪=0 dmg (pure defense/tech — CUTTABLE vs non-debuff foes).
R14 (LOST, the dud): NO 万法 → top dmg was 巨鲲 32 over 2 fires + 灵感剑 21. Could NOT kill 小布's 116 HP before his t7 磅礴 burst. CONFIRMS: 万法 is load-bearing; without it the board is a slow loser.

*** NEW (g20) UPGRADE — 云剑·游龙 > 辟邪阵纹 in slot2 (vs non-debuff rivals). ***
sim_matchup 8 reps, 小布's +1 board: 游龙 board = 100% first / **100% second** (kill t6); 辟邪 board = 100% first / 0% second.
WHY: 游龙 lv1 = 2atk×2, [连云]+3def, **[击伤]→[再次行动]** — its hit triggers a chase, pulling 百鸟(+3qi) forward a full turn → 万法 arrives t6 not t7. 辟邪 gives 0 dmg and 小布's final board (气势/burst, no 内伤) leaves it idle.
CAVEAT: 云剑·闪风 slot6 also tested — kills t5 in one lucky full_log but **0% second at 5 reps** = RNG trap. Use 游龙+白鹭, NOT 闪风. Re-test today; trust 5+ reps.
Keep 辟邪 in pocket WHEN a rival runs a debuff package (谭舒雁's 厄劫/内伤, an 内伤-clock 小布 variant).

ECONOMY: rolls/round = 0,0,0,2,2,0,3,5,11,9,10,0,11,7,3,0,12,0,15. Bank stayed ≤17 early, ≤11 mid, ≤3 late. Over-rolled R9(11)/R11(10)/R13(11)/R17(12)/R19(15) — but R19's 15 rolls FOUND the 万法 merge, so late heavy rolling was CORRECT here.
KEY TIMING: 万法 first appeared R15 (境5 pool, ~11%/draw). I had it lv1 R15-R18 then merged R19. 聚灵心法+1 merged R15, 引气剑+1 R17, 巨鲲+2 R14, 百鸟+1 R9(!) — engine assembled over R9-R17.
Under-rolled: R12/R16 spent 0 rolls (banked) while I lacked 万法 — could have hunted it a round or two earlier.

*** RIVAL INTELLIGENCE (post-game open review) ***
小布 (pid3, 崩拳/气势) playbook: HE SIM-ED ~35 BOARDS vs my qi-ramp — ALL 0%. He correctly diagnosed my kit as a hard counter and that 辟邪 blanks his 内伤 clock. His answer is "kill before t7" — which my seat (修为97>89) denied him. **Seat is decisive for BOTH of us** (his C5/M14).
谭舒雁 (pid1, 命理师): died with a clock-less dud board (no 厄劫缠身) — draw failure, not board order.
吾行之 (pid2, 水灵): died R13, my easiest matchup (100% both seats, no 万法 merge even needed).

SURPRISES: (1) My board is SEAT-DEPENDENT vs 小布's upgraded board — 修为 lead was the hidden win-con, and I secured it (97 vs 89) by absorbing leftovers into 修为 every round. (2) Fates still flip nothing. (3) 云剑·游龙 (a lv1 throwaway 云剑) is a real upgrade over 辟邪 in the 万法 shell.

==== LEDGER ENTRY · Game 17 ====
## Game 21 — 牧逸风 (云剑 sect, sidejob=阵法师5) — RESULT: NOT 1st, final 命 0 (last). Winner = 小布 (pid3, 命21); 谭舒雁 (pid1, 命1) also alive; 吾行之 (pid2) dead R13.

BATTLES: R1 L(pid3,-4) R2 W(pid1) R3 W(pid2) R4 W(pid3) R5 W(pid1) R6 L(pid2,-10) R7 L(pid1,-10) R8 L(pid3,-9) R9 L(pid1,-14) R10 L(pid2,-13) R11 L(pid3,-16) R12 L(pid2,-19) R13 L(pid3,-19, DEAD). I won R2-R5 then lost 8 of my last 9.

**ROOT CAUSE = I NEVER ASSEMBLED THE 万法归灵剑 QI-NUKE, MY OWN g20-WINNING RECIPE — FOR THE THIRD GAME RUNNING (g15, now g21).**
My final R13 board was the old 灵剑-qi-suite WITH NO FINISHER: ['聚灵心法','引气剑','化灵诀','百鸟灵剑诀+1','白鹭灵剑','云剑·极意+1','灵犀剑阵','地煞剑']. card_stats R13: 白鹭 did 59 dmg over 12 turns (only dmg source), every other slot = qi/def. vs 小布's 130-HP pool that loses t12. Same failure signature as g15.

*** THE RECIPE WAS CORRECT AND SEAT-INDEPENDENT — PROVEN POST-GAME ***
Best board found (search_board + sim_matchup, vs pid1 AND pid3, base AND +1, both seats = 100%):
  ["聚灵心法+1","百鸟灵剑诀+1","引气剑+1","巨鲲灵剑+2","云剑·点星","白鹭灵剑+1","万法归灵剑+2","辟邪阵纹+1"]
  Wins 100% BOTH seats vs 小布's real R20 board (6t first, 9t second; 万法 lv3 fired for 71-87 dmg).
  Wins 100% BOTH seats vs 谭舒雁's R20 board AND 吾行之's R20 board. The single universal endgame board.

*** NEW DISCOVERY [g21]: 辟邪阵纹 BELONGS AT SLOT 8 (LAST), NOT SLOT 1. ***
search_board trace: moving 辟邪 from slot1->slot8 flipped vs 小布's +1 board from 100%/0% to 100%/100% (both seats). WHY: placed LAST, its 3 hexproof + 14 def (持续-played bonus) land right before the cycle wraps into the enemy's 磅礴之势/崩拳 burst turn, blanking the debuff + shielding the 万法 turn. Placed FIRST it was spent wastesfully early. This made the board SEAT-INDEPENDENT — a big deal since seat is coin-flippy.

*** SEAT WAS THE OTHER HALF OF THE LOSS. My 修为 was the LOWEST in the lobby: me 57, 吾行之 87, 小布 96/103, 谭舒雁 101/110. I LOST EVERY SEAT. ***
Sim proof: identical g20-board going FIRST vs 小布 = WIN t7; going SECOND = LOSE t10 (his 体魄-ramped 156 HP + 42-dmg 磅礴 burst out-sustains my 105 HP). 小布 also ramped physique 43-45 => 156 maxHP vs my 105 (I stayed 体魄 0 ALL GAME — never built physique). **修为/体魄 scaling is as important as the board.**

*** ECONOMY DISASTER — the actual game-loser. Rolls: R1-7=0, R8=3, R9=12, R10=10, R11=2, R12=0, R13=23. ~50 total. ***
- R9 (12 rolls) and R13 (23 rolls!) = SHOTGUN, no named target, found NOTHING (M18 repeated from g16). R13 rolled through 百鸟灵剑诀 x2, 巨鲲灵剑 x2, 云剑·极意, 云剑·游龙, 巨鹏灵剑, 形意剑 — every 万法-suite adjacent card — and kept none, ended with no finisher.
- CRITICAL TIMING ERROR: I broke 境5 at **R12** (修为55) — leaving only R12-R13 to draw 万法 from the 境5 pool (~11%/draw). 谭舒雁 and 小布 were already 境5 by R12 and 吾行之 earlier. I needed 境5 by R9-10 (absorb harder R1-R9) to have 4-5 rounds of 万法 hunting. **Break the realm gate ONE round earlier than feels safe; the extra hunting round is worth more than the cards you absorb.**
- Bank discipline fine (never >23), but I over-rolled with no target instead of banking for a focused R13 万法 hunt.

*** g20'S LESSON RE-CONFIRMED: the 万法 MERGE (lv2/lv3) is the game; lv1 firing = ~30, lv2 = ~80, lv3 = ~87-98 through def. Never got a single 万法 copy this game.***

SURPRISE: 小布 WON this lobby despite the pre-computed matrix showing him losing 100% to 吾行之 and 谭舒雁 going first — he out-lived everyone via physique HP + winning seats. A "losing" board that summons 150+ HP and always acts first can win a lobby. SEAT + HP SCALING > raw board quality.

ECONOMY NUMBERS: banked-end 3,9,14,18,21,22,16(OFF-bank),9,12,16,0 — wait, actual: R1 3,R2 6,R3 9,R4 12,R5 15,R6 18,R7 21,R8 22,R9 14,R10 9,R11 12,R12 16,R13 0. Absorb total ended 修为57 (lowest).

==== LEDGER ENTRY · Game 18 ====
## Game 22 — 牧逸风 (云剑 sect1 + 阵法师5) — RESULT: NOT 1st, final 命 0 (placed 3rd of 4; effectively last-survivor-before-final). Winner = 小布 (pid3, 命20). Others: 谭舒雁 pid1 dead, 吾行之 pid2 dead.
Final 命=0 修为81 境5, board ['百鸟灵剑诀+1','引气剑','巨鲲灵剑+1','灵气灌注','白鹭灵剑+1','巨鲲灵剑','疗愈阵纹','辟邪阵纹'].

BATTLES: R1 W(pid2) R2 L(pid3) R3 W(pid2) R4 W(pid3) R5 W(pid1) R6 W(pid2) R7 L(pid3,-11) R8 L(pid2,-13) R9 L(pid1,-15) R10 W(pid3) R11 W(pid2) R12 W(pid3) R13 W(pid2) R14 L(pid3,-23) R15 W(pid2) R16 L(pid3,-24) R17 L(pid3,-27,DEAD). Record 10-7. Won early, then 小布's scaling 崩拳/体魄 board beat me 4 times late.

*** ROOT CAUSE = SAME AS g15/g21: I NEVER ASSEMBLED THE 万法归灵剑 BOARD. I DREW ZERO 万法 IN 17 ROUNDS. ***
Evidence: economy_history — 万法 (境5, 6/66 pool cards ≈9%/draw) was NEVER in any deal or roll result R12-R17 (24 deals + ~85 rolls). Bad luck compounded by NO NAMED ROLL TARGET (M18).

*** POST-GAME PROOF the 万法 board was the ONLY reachable win: ***
`[聚灵心法+1, 百鸟灵剑诀+1, 引气剑+1, 巨鲲灵剑+2, 云剑·点星, 万法归灵剑+2, 白鹭灵剑+1, 辟邪阵纹+1]`
= 100%/100% BOTH seats vs 小布's R17 board (5t, I end at 5 HP, 万法 fires 75-82 dmg). Re-verified with search_board (locked 万法+聚灵+百鸟+巨鲲 → converged at 21 evals, no better). Also 100%/100% vs 吾行之, 100%/100% vs 谭舒雁 base (only weak: 0% SECOND vs 谭舒雁 FULLY +1 — her 内伤 clock).
- 万法 lv1 = 53 dmg → LOSES (leaves 小布 14 HP). 万法 lv2 = 75-82 → WINS. **LEVEL IS THE WIN THRESHOLD.**
- A single lv1 万法 + 云泉道茶 (upgrade) ALSO wins — my R12 fate 云泉道茶 was the right pick, I just never drew 万法 to use it.
- ~1000 search_board evals across pools {1,2,3,4,5,6,7}: NO non-万法 board beats 小布's R17 board. 0%/0% everywhere. The 阵法师/云剑 qi-fallback (my R17 fielded board) LOSES 0/0.

*** PHASE-1 TRACE of the decisive R17 loss (6 turns, 小布 went FIRST): ***
小布 curve: Majestic Qi(+3qi,+1force,+3 stacks) → Surging Waves(+4force,+5agi) → Sailing through Sky(+4force,+6agi → auto-chase 10 agi → SPENDS it) → chase Mighty Force (3× force → 38-48 dmg through my 0 def) → [t4] 崩拳·降龙+1 (22 dmg, gains "next 崩拳 +7def/+7atk") → [t5] 崩拳·寸劲 (2× force → 42-58 dmg) → [t6] Vigorous Force (kills). His burst is ~40-58 per hit from t3-5. MY board: 70 dmg total but he had 138 HP. I lose t6 at ~5-19 HP.
KEY: his 崩拳·降龙+1 sets up 寸劲; the 势如破竹+1 qi→force conversion + 身法 chase = 2 cards/turn. My 巨鲲 chase + 白鹭 was just too slow/small vs 138 HP.

*** SEAT MYSTERY: 小布 went FIRST in R16 & R17 logs despite my SITREP showing higher 修为 (81 vs 79). Possible: displayed 修为 is POST-battle snapshot, or tie-break coin-flip. NOTE for future: don't trust the sitrep seat line late; the log is ground truth. ***

*** ECONOMY AUDIT (rolls/round): 0,0,0,0,0,3,6,0,0,17,2,15,8,8,6,8,4 (~85 total). ***
- OPENING R1-R5 = 0 rolls, clean (good — the ONE thing I did right; matches g17 谭舒雁).
- R6/R7 = 3+6 junk rolls at 境3 (rolled 引雷阵/云剑·厚土/凝意诀 etc., all absorbed).
- R10 (17!) and R12 (15!) = SHOTGUN, no named target. R10 landed 白鹭+百鸟+引气 (some value); R12 landed NOTHING toward 万法.
- R13/R14 = 16 more junk-ish rolls (R14 got 灵气灌注 — the ONE good late hit).
- **UNDER-ROLLED for the ONE card that matters.** From R12 (境5) I had 6 rounds; I should have spent EVERY exchange hunting 万法 by name. Instead I dribbled.
- BANK: hit 25 at R9-end (wasted a grant). Better to spend before cap.

*** FATE NOTE: took 云泉道茶 (R12 境5) — the RIGHT pick (upgrades a lv1 万法→lv2 = the win threshold). A/B sim: fate[17]=云泉道茶 on a lv1-万法 board flipped... actually tested: lv1万法 needs +1 qi source, not the fate. Fates remain combat-adjacent but the 云泉道茶 万法-upgrade is genuinely load-bearing IF I have a lv1 万法.

*** SURPRISE: 小布 won the lobby with the board the pre-computed matrix called "loses 0% to 谭舒雁/吾行之" — because he out-scales via 体魄 HP (138) AND wins seats. A 150-HP board that acts first beats "better" boards. Same lesson as g21 (小布 won that one too). ***

==== LEDGER ENTRY · Game 19 ====
## Game 23 — 牧逸风 (云剑 sect1 + 阵法师5) — RESULT: NOT 1st, final 命 0 (last of 4). Winner = 小布 (pid3, 命1 — exactly 1!). Others: 谭舒雁 pid1 (命0), 吾行之 pid2 (命31, ALIVE).
Final: 修为58 境5 体魄0 maxHP99. Final board ['周天剑阵+1','凝意诀','百鸟灵剑诀','云剑·点星+1','剑劈+1','飞牙剑'] + hand ['云剑·游龙','不动金刚阵+1','巨鲸灵剑+1','回响阵纹'].

BATTLES: R1 W(pid1) R2 L(pid2) R3 L(pid1) R4 W(pid3) R5 L(pid2) R6 L(pid3) R7 L(pid2) R8 L(pid1) R9 W(pid2) R10 L(pid3) R11 W(pid2) R12 L(pid3) R13 L(pid1,DEAD). Record 4-9. Lost to 小布 EVERY late round.

*** ROOT CAUSE = SAME AS g15/g21/g22: NEVER ASSEMBLED A WIN-CON. Zero 万法归灵剑 drawn (境5 only from R12; 6 copies, 2%/roll). AND — the NEW finding — I ALSO failed to field the REACHABLE no-万法 chase engine.***

*** ★★★ TOP DISCOVERY [g23] — THE REACHABLE NO-万法 WIN BOARD (search_board + sim, 8 reps). ★★★ ***
`[百鸟灵剑诀+1, 引气剑, 巨鲲灵剑+1, 白鹭灵剑+1, 巨鲲灵剑, 聚灵心法, 辟邪阵纹, 灵气灌注]`
= **100% FIRST / 100% SECOND vs 小布's EXACT R17 board** (t8, ends 1-4 HP — tight but real).
= 100% first / 0% second vs 谭舒雁 base (80% first in multi-rep); 100% first / 0% second vs 吾行之 base.
= 0%/0% vs the +1-UPGRADED versions (only 万法 lv2 beats those both seats).
WHY IT WORKS: 巨鲲灵剑 (+10atk,+10def,+CHASE) → chases 白鹭灵剑 (5 + 2×banked-qi → 29-32 dmg with 11 qi). The 聚灵心法+百鸟+引气 qi battery banks qi so 白鹭 scales. THIS IS REACHABLE (I had 巨鲲灵剑+1 merged! I had 百鸟+1, 引气, 聚灵, 辟邪, 灵气灌注 all drawn). I fielded chip 灵剑 instead → 0%/0%.
万法 board (still the ceiling): ['聚灵心法+1','百鸟灵剑诀+1','引气剑+1','巨鲲灵剑+2','云剑·点星','万法归灵剑+2','白鹭灵剑+1','辟邪阵纹+1'] = 100%/100% both seats, 5t, massive margin. CONFIRMED again.

*** #2 ROOT CAUSE — SEAT/修为. Me 58 = LOWEST (小布 83, 谭舒雁 82, 吾行之 76). LOST EVERY SEAT. ***
My R13 log: 谭舒雁 went first EVERY time she faced me and her 内伤 clock + burst won. 小布 went first and burst me down.

*** #3 ROOT CAUSE — ECONOMY SHOTGUN + LATE 境5. ***
rolls/round: R1-5=0, R6=8(junk), R7=0, R8=3, R9=4, R10=2, R11=3, R12=3, R13=24(FULL SHOTGUN, 0 keepers, landed 化灵诀/云剑·极意/回响阵纹 — all junk). Broke 境5 at R12 (修为55) → only 2 rounds of 境5 draws. 修为 ended 58 (lowest). Off-bank: hit 24 twice (R10, R12) wasting grants.

*** PHASE-1 TRACE of R13 loss (谭舒雁 first, 9t): *** Her curve: 杯弓蛇影(3 内伤) → 天星·牵引(+qi,+1 内伤) → 星弈·断(16 dmg, 星位 skip) → 星位·立 → 天星·御心(+def/+maxHP,+2 内伤) → ... 内伤 ticks me 5-7/turn ignoring 防; I dealt only 16+12+7 = ~35 total. Her clock+burst outraced my chip. EXACTLY 谭舒雁's ledger diagnosis of her own board.

*** PHASE-1b CARD AUDIT: my R6/R10/R13 boards = 6-8 chip slots dealing 0-20 each, NO finisher. card_stats R13: 白鹭 would have been 59 but I never fielded it that round; my slots dealt 5-16. Every 'qifeeder' slot is only worth it if a CONVERTER (巨鲲/白鹭/万法) consumes the qi. ***

*** SURPRISE: 小布 won with 命 1 — he nearly died too. The lobby was decided by seat + surviving the last race, not by board quality. Same as g21/g22: 小布's HP-scaling + seat wins lobbies. 吾行之 survived (命31) with a tanky 水灵 board too.***

REACHABILITY CONFIRMED: I HELD the cards for the no-万法 win board (巨鲲灵剑+1 merged, 百鸟+1, 引气剑, 聚灵心法, 辟邪阵纹, 灵气灌注) and fielded NONE of them together. This is M22 again at the BOARD level: I had the winning cards and didn't field them.

FATES: took 云雾变幻/感悟丛生/变换之道/储纳灵气/云泉道茶 (all economy/qi). 云泉道茶 = right pick IF 万法 lv1 drawn (upgrades to lv2 = win threshold). Never having 万法 made it dead.

==== LEDGER ENTRY · Game 20 ====
## Game 24 (ARENA g20) — 牧逸风 (云剑 sect, sidejob=阵法师5) — RESULT: NOT 1st, final 命 0. Winner = 小布 (pid3, 命49). 谭舒雁(pid1) & 吾行之(pid2) also dead.
Record: R1 L(pid1) R2 W(pid3) R3 W(pid2) R4 L(pid3) R5 L(pid2) R6 W(pid1) R7 L(pid2) R8 L(pid1) R9 L(pid3) R10 W(pid1) R11 W(pid3) R12 L(pid2) R13 L(pid1) R14 L(pid3) R15 L(pid1) R16 L(pid3,DEAD). 6-10.
Final 修为75 境5 体魄0 maxHP105; board ['百鸟灵剑诀','聚灵阵+1','巨鲲灵剑+1','云剑·点星+1','灵感剑+1','引气剑','云剑·汇灵+1','云剑·点星'] — a QI BATTERY WITH NO CONVERTER. 0%/0% vs 小布.

*** ROOT CAUSE (SAME AS g15/g21/g22/g23 — 5th straight): NEVER DREW/FIELDED A CONVERTER (万法/白鹭-lv2+). ***
My final board dealt ~70 dmg over 7-8 turns; 小布's 崩拳 burst (11/10/13/14 + 冲霄→寸劲 24-34 + 势如破竹) does ~115 over t1-t8 and he has 130-140 HP.

*** DECISIVE POST-GAME PROOF (yisim, 3-4 reps each): ***
WINNER BOARD = `[辟邪阵纹+1, 聚灵心法+1, 百鸟灵剑诀+1, 引气剑+1, 巨鲲灵剑+2, 白鹭灵剑, 万法归灵剑+1, 云剑·点星]`
  - vs 小布's EXACT final board: **100% FIRST / 100% SECOND, t6** (万法 fires 59 dmg: 5 + 6×9qi).
  - vs 谭舒雁's C7 内伤 recipe: **100%/100%, t7** (万法 77 dmg). Her notebook claims she beats me 100% — SHE IS WRONG vs the 万法 board (she simmed my OLD chip board).
  - vs 吾行之: 100%/100% base AND +1.
  - 万法 lv1 also wins but needs qi≥9 and (vs 小布 base) FIRST seat only; lv2 wins both seats. lv2=win threshold.
**THE ONLY BOARD THAT BEATS THE FIELD IS THE 万法 BOARD. CONFIRMED 5 GAMES RUNNING.**

*** REACHABILITY ANALYSIS OF THE NO-万法 ROUTE (NEW, quantified): ***
RECIPE A `[百鸟, 引气, 巨鲲+1, 白鹭+1, 巨鲲, 聚灵心法, 辟邪阵纹, 灵气灌注]` win-threshold vs 小布 base:
  - 百鸟 BASE + 白鹭+1 + 巨鲲+1  = **LOSE** (26 dmg short, t8).
  - 百鸟+l? Actually: **百鸟+1 (OR 白鹭+2) + 白鹭+1 + 巨鲲+1 = WIN 100%/100%** (t9, ends 2-4 HP — razor thin).
  - 白鹭+2 + 百鸟 base = LOSE. So the threshold is 百鸟+1 OR 白鹭+2 (a "power level" on the engine).
  - 2×巨鲲+1 (4 巨鲲 copies) + 百鸟 base + 白鹭+1 = WIN too.
  I HELD: 百鸟 BASE (x1), 白鹭+1 (x2 merged from 2), 巨鲲+1 (x2 merged). To win I needed exactly ONE more copy of ANY of: 万法(any), 白鹭(→+2), 百鸟(→+1). None drawn.
  → **The "RECIPE A = 100%/100%" claim in my g23 notebook is STALE/conditional: it needs 百鸟+1 or 白鹭+2, which I did NOT have in g24. Re-sim from ACTUAL held cards, not an idealized pool.**

*** PHASE-1 TRACE: WHY I LOST EVERY LATE FIGHT. ***
- vs 小布 (R14/R16): his curve t1 崩拳·缠+1 (11) → t2 撼 (10-11) → t3 连崩 (13-15) → t4 戳 (14-16) → t5 冲霄破浪 (+4force,+5agi) → t6 寸劲 (force×2 → 21-34) → t7 势如破竹 → t8 wrap. He ALSO gains 体魄+1 + heals 2 EVERY 崩拳·缠. My board: 灵感回 8-18, 巨鲲 13, 汇灵/点星 5-12. ~70 total → loses at t7-8 at 5-15 HP.
- vs 谭舒雁 (R13/R15): 杯弓蛇影(+3内伤+tick) → 血光之灾x2 (开局+2) → 流水无情(6dmg,+2内伤) → 天星·牵引(+qi,+1内伤). 内伤 IGNORES 防, permanent, 5→14 stacks across t1-t9. By t8-9 clock out-damages my chip. Her final board also had 白蛇吐信/揽雀尾 in hand.

*** ECONOMY AUDIT (this game) — THE OTHER HALF. ***
rolls/round: R1-6=0, R7=3, R8=4, **R9=23(!)**, R10=0, R11=8, R12=6, R13=6, R14=8, R15=7, R16=7 (~79 total).
- **R9: 23 rolls AT 境4 — 万法 (境5) was NOT EVEN UNLOCKED. 100% wasted shotgun (M18).** This is the single biggest economy blunder.
- Broke 境5 at R12 (修为55, LATEST possible) → only 5 late rounds of 境5 draws. Rivals were 境5 by R12-13 too but built 修为 faster.
- 修为 ended **75 — LOWEST-or-2nd-lowest** (小布 92, 谭舒雁 91, 吾行之 68). I LOST most seat races. My R16 log: 小布 went FIRST (he had 86+).
- BANK: hit 0 repeatedly, never wasted a grant — the ONE clean thing. But I ROLLED AWAY the wrong cards: R16 I ABSORBED 聚灵心法+1 and 灵气灌注+1 (ENGINE PIECES!) then fielded the chip board. M22 at the board level AGAIN.
- 小布 BENCHMARK ECONOMY: **~33 rolls TOTAL** (0,0,0,0,1,5,0,1,13,8,0,0,0,2,3,0,0,0) — absorbs EVERYTHING, ends 修为92. TARGETED dumps only at phase unlock (R6=5→landed 势如破竹/崩拳·撼; R9=13→landed 踏破九霄/崩拳·连崩/崩拳·突; R10=8→势如破竹+1 merge).

*** SURPRISE: 谭舒雁's notebook explicitly says she beats me 100%/100% — but that was simulated vs my CHIP board. The 万法 board beats her 100%/100% both seats. Rivals' notes about ME are stale; and MY notes about "RECIPE A wins" were stale (needed 百鸟+1). RE-SIM FROM HELD CARDS EVERY GAME.**

*** TOP DISCOVERY [g24]: THE WIN THRESHOLD FOR THE NO-万法 BOARD IS 百鸟+1 OR 白鹭+2 (or 2×巨鲲+1). 白鹭+1 ALONE IS A LOSS. Quantified above with exact sims. ***

==== LEDGER ENTRY · Game 21 ====
## ARENA Game 21 — 牧逸风 (云剑 sect1 + 阵法师5) — RESULT: **1st PLACE / WINNER**, final 命 48. Losers: 谭舒雁(pid1) 命0, 吾行之(pid2) 命0, 小布(pid3) 命0.
Full record: R1 W(pid1) R2 W(pid2) R3 W(pid3) R4 W(pid1) R5 W(pid3) R6 W(pid2) R7 W(pid1) R8 L(pid3,-13) R9 W(pid1) R10 W(pid2) R11 L(pid3,-18) R12 L(pid1,-21) R13 W(pid3) R14 W(pid2) R15 W(pid3)+L(pid1) R16 W(pid3) R17 W(pid1) R18 W(pid1) R19 W(pid1). Record 16-3.
Final 修为93 境5 maxHP111 体魄0. Final board = ['辟邪阵纹','百鸟灵剑诀+1','引气剑+2','化灵诀','云剑·点星','云剑·点星','白鹭灵剑+1','万法归灵剑+1'].

*** ★ THE WIN CONDITION FINALLY EXECUTED: THE 万法归灵剑 QI-BATTERY. ***
This is the FIRST game I ever assembled it, and it won the lobby. R13 I rolled 万法归灵剑 TWICE (in ~7 rolls from 境5 pool), merged to +1 at R15/R19. Once fielded, I won R13,R14,R16,R17,R18,R19.
R19 winning line (vs 谭舒雁, 8t, she was FIRST seat): bank qi to 15 by t7, 白鹭灵剑+1 fires 50 (5+3×15), then 万法归灵剑+1 dumps ALL 15 qi = 95 dmg (5+6×15). One card = over half her HP.
万法 fires 71-95 across rounds — by far my top damage slot every late round.

*** ★★★ TOP DISCOVERY [g21] — 辟邪阵纹 IS THE HARD COUNTER TO 谭舒雁's 内伤 CLOCK, BUT ONLY IN SLOT 1. ***
My notebook previously said "辟邪 does NOT stop attacks → useless vs the dump" (true) but I UNDER-RATED it: hexproof ALSO eats 内伤 STACK APPLICATIONS.
Evidence: R19 log, 辟邪 in SLOT 1 → turn 1b/2b/3b "lost 1 hexproof" each time 谭舒雁 played an 内伤 card, and my 内伤 stayed at 1-4 the whole early game (vs 7-10 when 辟邪 absent). She never ramped.
Sim proof (my held cards vs her final board):
  · ['辟邪阵纹','百鸟+1','引气+2','化灵诀','点星','点星','白鹭+1','万法+1'] = **100% FIRST / 100% SECOND** (search_board could NOT improve it — 21 evals, no better).
  · SAME cards but WITH 辟邪 moved to SLOT 8 = **0%/0%** — her [开局] 血光之灾 内伤 lands t1 BEFORE late-辟邪 is up.
  · SAME 8 cards but 辟邪 REPLACED by a 3rd 云剑·点星 = **0% FIRST / 100% SECOND** — loses going first (out-clocked t9).
  → RULE: vs 谭舒雁, 辟邪阵纹 MUST BE SLOT 1. It is load-bearing, not a dead slot.

*** ★ 2ND DISCOVERY [g21] — vs 小布 (崩拳 burst) 辟邪阵纹 IS a dead slot; a 3rd 云剑·点星 is better. ***
小布 applies NO debuff stacks to me (his burst is raw 击伤; [外伤] wound is self-applied). So 辟邪's hexproof does nothing.
Sims vs his final board (6 cards: 崩灭心法/岿然不动/寸劲/连崩/戳+1/突+1):
  · my R19 辟邪 board: base 100%/100%, **+1 board 0%/0%**.
  · ['云剑·点星','百鸟+1','引气+2','化灵诀','点星','万法+1','白鹭+1','点星'] (辟邪→3rd 点星): base **100%/100%, +1 100% FIRST / 0% SECOND** (t6; banks 15 qi, 万法 95 kills before his 寸劲).
  → RULE: matchup-specific final board. vs 谭舒雁/内伤 → 辟邪 SLOT 1. vs 小布/burst → drop 辟邪, field an extra qi feeder (3rd 点星).

*** ★ THE WIN-VS-小布-+1 THRESHOLD = a 点星+1 (or any power-level on the qi engine). ***
['引气+2','点星','点星','点星+1','万法+1','百鸟+1','白鹭+1','辟邪'] = +1 board 100%/100% (5t). Without the 点星+1 it's 0%/0% vs +1. He was DEAD by R19 (命0) so it never mattered, but it's the gap.

*** SEAT/修为: I ended 修为93 (2nd of 4: 小布 had been 92→higher, 谭舒雁 94). I WON the R19 seat race by gaining >1 修为 that turn (SITREP said I trailed by 1). Seat mattered in the R19 win: I actually went SECOND vs 谭舒雁 (log: she is "1a") and still won via 辟邪 supressing her clock. A well-built 万法 board wins BOTH seats vs her, unlike the no-万法 boards. ***

*** ECONOMY AUDIT (rolls/round): R8=15, R10=13, R11=6, R12=6, R13=7, R15=10, R19=6 (~63 total). Broke 境5 at R11 (修为55). ***
- **R8 (15 rolls) + R10 (13 rolls) = 28 rolls at 境4 — 万法 is 境5, NOT UNLOCKED. ~Half my total rolls spent with the win-con unreachable (M29 AGAIN).** R8 did land 聚灵心法/灵气灌注/不动金刚阵 (real pieces) but I later ABSORBED 聚灵心法+1 & 灵气灌注 (M22 again) — engine pieces rolled AND thrown away.
- R11 broke 境5; R13 (7 rolls) landed 万法 ×2 + 引气. R15 (10 rolls) landed 百鸟 + merged 引气+2. Good NAMED hunting once unlocked.
- Bank: hit 21 at R18→R19 waste (grant would have topped to 25 but I was above... actually banked 21, grant fills to 25 — fine). R12/R13 banked 0. No big cap waste.
- LESSON: the fix is break 境5 EARLIER (R10) so the R11+ rolls are all in-pool for 万法. I wasted 28 rolls pre-unlock.

*** SURPRISE: I won with 命 48 while 小布 (who'd beaten me R8/R11) died at 命0. Race outcomes > single-matchup quality. Also 谭舒雁 reached R19 with 命1 and was killed by my 万法 dump — she'd written in her notebook that "the 万法 battery is a ~0% wall" for her clock: she was RIGHT and I proved it. ***

*** FATES: 云雾变幻/储纳灵气/顿悟/云影化身/云泉道茶. 云泉道茶 (万法 lv1→lv2) never needed — I drew 2 万法 naturally. Fate 17 A/B-tested on the win board: no change in outcome (already winning). Fates are secondary once the board is right. ***

*** REACHABILITY CHECK: everything on my final board I actually HELD (3× 云剑·点星 = 2 board + 1 hand). The 辟邪→3rd-点星 swap was reachable. The 点星+1 (need 4 copies) was NOT. ***

==== LEDGER ENTRY · Game 22 ====
## ARENA Game 22 — 牧逸风 (云剑 sect1 + 阵法师5) — RESULT: NOT 1st, final 命 0. WINNER = 小布 (pid3, 命100). 谭舒雁(pid1) & 吾行之(pid2) also dead at 命0.
Record: R1 W(pid1) R2 W(pid2) R3 L(pid3) R4 W(pid1) R5 L(pid3) R6 L(pid1) R7 L(pid3) R8 L(pid2) R9 L(pid3) R10 W(pid2) R11 W(pid1) R12 W(pid2) R13 L(pid3) R14 L(pid1,DEAD). 6-8.
Final 修为68 境5 体魄0 maxHP101. Final board ['百鸟灵剑诀','聚灵阵','引气剑+1','化灵诀','云剑·点星','灵感剑+1','白鹭灵剑+1','白鹭灵剑'] — QI BATTERY, NO 万法 CONVERTER. 0%/0% vs 小布.

### ★ #1 ROOT CAUSE — NEVER DREW 万法归灵剑 (6th straight game without the win-con). SPENT ALL game at 境4, broke 境5 only at R12 (修为55) → only ~3 rounds of 境5 draws, and 万法 is 境5-locked. My R8=15rolls + R9=13rolls were AT 境4 where 万法 is UNREACHABLE. Wasted economy AGAIN (M29).
### ★ #2 ROOT CAUSE — the 万法-board I fielded (R13/R14) STILL LOST even though I lacked 万法. But even WITH a 万法 board, order/defense decides it (see discovery below).

### ★★★ TOP DISCOVERY [g22] — THE BOARD THAT BEATS 小布's FINAL +1 BOARD 100%/100% (yisim, both seats). ★★★
`[百鸟灵剑诀, 引气剑+1, 不动金刚阵, 云剑·点星, 万法归灵剑+1, 白鹭灵剑+1, 辟邪阵纹, 云剑·点星]`
= **100% FIRST / 100% SECOND vs pid3's EXACT final board** (t11 — long DEF-conversion race, I end at 8-10 HP, razor thin but real).
Also beats 谭舒雁's final board 100%/100% (辟邪 SLOT 1 version, t12).
WHY IT WORKS (full_log): the g21-style pure-qi board (引气剑+1,引气剑,化灵诀,点星,点星,汇灵,白鹭,万法) gets 100% FIRST but 0% SECOND vs 小布's NEW +1 board — because 小布's 崩拳·连崩 does 36/27/14/19 = ~96 burst by t8 and out-races it. The FIX = **不动金刚阵 [持续]2次: +7 def/turn AND +7 maxHP when not chasing** → converts the race so 万法's t5-11 firing survives. This is the survival card my g23/g25 notes kept flagging. 辟邪阵纹 must sit LATE (slot 7) not slot 1 vs 小布 (he debuffs nothing worth hexproof-ing and slot1 wastes tempo).

### ★ CONFIRMED MECHANICS this game:
- 引气剑+1 (Spiritage Sword lv2) = +3 qi AND 3atk×2 when qi>3 → the qi engine's early fuel.
- 万法归灵剑 lv2 = 5 + 6×qi exhausted (fired 53-59 as my only real damage).
- 化灵诀 = PURE +3 qi, ZERO attack — a dud slot in a race; 不动金刚阵 (def/HP) is strictly better as the 8th card.

### MATCHUP MATRIX READ (precomputed): vs 小布 base/+1 = I LOSE all seats with any no-万法 board. vs 谭舒雁 base = 50% (seat-dependent), +1 = 0%. vs 吾行之 base = 50%, +1 = 0%. → I was BEHIND the whole lobby at endgame; needed 万法 AND its def support.

### ECONOMY: rolls/round R1-4=0, R5=2, R6-7=0, R8=15, R9=13, R10=0, R11=1, R12=13, R13=7, R14=8 (~59 total). R8+R9 = 28 rolls AT 境4 (万法 unreachable — M29 for the 4th game). Broke 境5 R12 (latest possible). Hit bank 0 repeatedly (R9-R14) but no cap waste. 修为 68 = LOWEST of field.
### 小布 (WINNER) BENCHMARK: ~18 rolls TOTAL (0,0,2,0,0,1,0,0,8,0,0,0,4,5,3) — absorbs EVERYTHING, ends 修为79+. His R9=8 rolls landed 崩拳·连崩/磅礴之势; R13-14 named merges of 降龙+1/连崩+1. He WON by: (a) clean absorb economy → highest 修为 → first seat, (b) assembling the 崩拳 force engine (降龙+1,气若悬河+1,踏破九霄,起势,连崩+1,势大力沉+1,磅礴之势,周天剑阵), (c) 体魄 stacks (25 → 133 HP).

### SURPRISE: 小布's playbook calls MY 万法 board "the boss/ceiling" and says he can't beat it without 威震四方. But HIS final board (气若悬河+1 + 势大力沉+1 + 周天剑阵 + 25 体魄) is now strong enough that even 小布's own claimed-losing-to-万法 board BEAT my actual fielded board every time. The counter-fix I found (不动金刚阵) is what would flip it — 100%/100%.

### FATES: 云雾变幻/云之道/剑韵修炼/云剑传承/云泉道茶 (all economy/qi). 云泉道茶 = right pick IF 万法 lv1 drawn; never had a lv1 万法 so it was dead (M34 again).

==== LEDGER ENTRY · Game 23 ====
==== LEDGER ENTRY · Game 23 ====
## ARENA Game 23 — 牧逸风 (pid0) (云剑 sect1 + 阵法师5) — RESULT: NOT 1st, final 命 0. WINNER = 吾行之 (pid2, 命1). 谭舒雁(pid1) & 小布(pid3) also dead 命0.
Record: R1 L(pid3) R2 W(pid1) R3 W(pid3) R4 W(pid2) R5 L(pid3) R6 W(pid1) R7 W(pid2) R8 W(pid3) R9 W(pid2) R10 L(pid3) R11 W(pid1) R12 W(pid2) R13 W(pid1) R14 L(pid2) L(pid3) R15 L(pid2) R16 L(pid2) L(pid3,DEAD). 10-8-1.
Final 修为79 境5 maxHP105 体魄0. Final board ['引气剑+1','云剑·点星+1','聚灵阵','破气剑','破气剑','不动金刚阵+1','巨鲲灵剑','万法归灵剑'] — 万法 lv1 (5+5×qi) with 巨鲲 STILL STEALING QI (spent 9 qi, dealt 30). 0%/0% vs 吾行之.

*** #1 ROOT CAUSE (the decisive one): vs 吾行之's 水灵 maxHP-grind TANK I fielded a CHIP board. ***
His engine (from his notebook): 不动金刚阵(slot1) + 回响阵纹(slot2) retriggers slot1 = +7def/+7maxHP EVERY cycle; 水灵阵 = +qi; 2× 水灵·纳百川 = +22 maxHP+heal EACH; 水灵·波澜 = dmg grown by force_of_water. He scaled to **207-213 maxHP and healed ~20/turn.** My board dealt ~140 over 19 turns (card_stats R16: 引气 0dmg, 点星 12, 巨鲲 30, 万法 only 50) → he out-healed me. SAME WALL as g27. I lost 0%/0% both seats.

*** ★★★ THE FIX — VERIFIED 100%/100% SOLUTION (this is the whole point of the game) ★★★
# RECIPE "QIBIRD": ['百鸟灵剑诀+1', '引气剑+1', '云剑·点星+1', '云剑·点星', '化灵诀', '回响阵纹', '白鹭灵剑+1', '万法归灵剑+1']
#   (slot1 百鸟+1 MUST be first; 回响 anywhere after → retriggers slot1.)
# sim_matchup (yisim, 3-4 reps EACH):
#   vs 吾行之 EXACT final board (the WINNER, 213HP tank): **100% FIRST / 100% SECOND, ~t8.**
#   vs 小布 EXACT final board (崩拳 burst):          **100% FIRST / 100% SECOND, ~t8.**
#   vs 谭舒雁 EXACT final board (内伤 clock):        **100% FIRST / 100% SECOND, ~t8** AND even vs her +1 board 100%/100%.
#   vs my OWN old final board (万法 lv1):            WINS, 78dmg 万法 t8.
# search_board over {百鸟+1,万法+1,回响} locks + pools [1,2,5] and [5,4]: **no improvement found — the recipe is optimal.**
# HOW IT WINS (full_log t8): 回响阵纹 retriggers slot1 百鸟灵剑诀+1 → +3 qi +3 qi = 6 qi from the pair alone (+ turns
#   the 灵剑 Qi-discount aura on). 引气剑+1/点星/化灵诀 bank qi to ~15-17. 白鹭+1 fires a mid chip. Then 万法归灵剑+1
#   (5 + 6×qi) DUMPS ALL 15-17 qi = **78-107 DAMAGE IN ONE TURN** = an instant kill before the tank scales or heals.

*** ★★★ MECHANIC DISCOVERED & SOURCE-VERIFIED: 回响阵纹 = RETRIGGER SLOT 1 if it is [持续]. ORDER IS LOAD-BEARING. ***
#   card_text: 回响阵纹 "若第一格为持续牌，重复其效果". 百鸟灵剑诀 = [持续] (+3qi lv2).
#   PROOF (A/B sim, both seats): ['百鸟+1'(slot1) ... '回响'(slot6)] = 100%/100% WIN. Move 百鸟+1 to slot2 & put
#   回响 slot1 = **0%/0% LOSS** (回响 sees only itself in slot1, does nothing; 万法 banks just 14 qi = 89 dmg, not lethal).
#   → RULE: a QI-GENERATOR [持续] in slot 1 + 回响 later = DOUBLE qi income. THIS is the cloud-sword qi engine,
#   far better than 巨鲲 or 聚灵阵. g21 used it for 万花 drain; g23 shows it doubles 百鸟's qi.

*** ★ 百鸟+1 (level 2) IS THE WIN THRESHOLD. ***
# ['百鸟'(base) slot1 + everything else identical] vs 吾行之 = **0% FIRST / 0% SECOND**. 百鸟 LOCKED to base → LOSE.
# So the qi engine needs 百鸟 at +1 (4 copies) — OR — a higher 万法. 万法 base works only FIRST seat (100%/0%);
# 万法+1 wins BOTH seats. Two independent "power levels" on the engine.
# 巨鲲灵剑 is a TRAP here: it costs 3 qi and CHASES into 万法 (good for chasing 万法) but STARVES it of qi — vs the
#   tank the correct move is to DROP 巨鲲 entirely and bank max qi into 万法.

*** ECONOMY AUDIT (mine): rolls/round ≈ R1-6=0, R7=4, R9=4, R11=26(!), R12=5, R13=7, R14=7, R15=2, R16=13 (~68).
# - R11: 26-roll shotgun right after breaking 境5 (境4->5 @R11) → landed 白鹭+1 and 不动金刚阵 but ALSO churned past
#   万法 (I actually HIT 万法 via roll at R13). The 26 was wasteful (over-rolled, M29-lite: no NAMED target).
# - R16: 13 rolls hunting 白鹭/巨鲲 — landed 破气剑×2 + 巨鲲 but NOT the 百鸟+1/万法+1 I needed.
# - I broke 境5 at R11 (修为55) — GOOD timing (earliest of the lobby except 小布 R11 too). 修为 ended 79 (吾行之 86, 小布 100, 谭舒雁 ~64).
# - BANK: R7 22, R9 22, R10 25(!cap), R15 5 — the R8→R9→R10 stretch sat at 22-25 and WASTED grants (grant fills to 25 only).
# WINNER 吾行之 economy: broke 境5 R13 (LATE) but then dumped **25 rolls @R13 + 8 @R15** ALL NAMED for the 水灵 kit.
#   小布: absorbed EVERYTHING, ~53 rolls total, ended 修为 100. Both winners = clean absorb + ONE/few targeted post-境5 dumps.

*** PER-RIVAL (final): 吾行之 WINNER (pid2) — 2W-4L (R4,R7,R9 W; R14,R15,R16 L). Beat by his 213HP 水灵 tank.
#   谭舒雁 (pid1) — 3W-0L. My 内伤 is not her problem. 小布 (pid3) — 4W-4L (R3,R8 W late; R1,R5,R10,R14,R16 L).
#   Beat by his 崩拳 burst early-mid; his board was the FASTEST (out-raced my chip t8-t10).

*** TOP DISCOVERY [g23]: RECIPE "QIBIRD" = 百鸟+1 slot1 + 回响阵纹 (retrigger) + 万法归灵剑+1 = 100%/100% vs ALL THREE rivals' final boards, ~t8 one-shot. REACHABILITY: 百鸟+1(4 copies)+回响+万法+1(4 copies) — the tight part is TWO +1s; 万法 base + 百鸟+1 = 100% first-seat, and 万法+1 alone would likely suffice with 百鸟 base (untested — test next game). ***

*** SURPRISE: The WINNER only reached 境5 at R13 (last of 4) yet WON — 修为/seat is NOT the game; the BOARD is. His tank out-scaled everyone. My g21-22 notes said "seat decides" but here a well-built board won both seats. And the g22 matrix that claimed "吾行之 beats everyone 100%" was itself beatable by MY recipe. ***

==== LEDGER ENTRY · Game 24 ====
## ARENA Game 24 (g29) — 牧逸风 (pid0) (云剑 sect1 + 阵法师5) — RESULT: NOT 1st, final 命 0. WINNER = 吾行之 (pid2, 命18). 谭舒雁(pid1) & 小布(pid3) also dead 命0.
Record (per battle log): R1 W(pid1) R2 W(pid2) R3 W(pid3) R4 L(pid1) R5 L(pid3) R6 L(pid2) R7 L(pid3) R8 W(pid2) R9 W(pid1) R10 L(pid2) R11 W(pid3) R12 W(pid2) R13 W(pid3) R14 W(pid1) R15 L(pid3)+L(pid2) R16 L(pid3) R17 L(pid2) R18 W(pid3)+L(pid2) R19 L(pid2,DIED -30). 10W-9L.
Final 修为96 境5 maxHP111 体魄0. Final board ['邪蛊阵+1','云舞诀+1','灵气灌注','百鸟灵剑诀+1','巨鹏灵剑','巨鲸灵剑','万法归灵剑+1','巨虎灵剑+1'] — won R18 vs 小布 going second; lost R19 0%/0% vs 吾行之.
FATES: 云雾变幻, 灵剑传承, 云剑传承, 云影化身, 剑阵传承. 云影化身 (one-time lethal-save) was CONSUMED at R19.

### ★★★★★ #1 DISCOVERY — THE WALL CRACKED: 回响阵纹 TRIGGERING 聚灵心法 (qi-gen) IN SLOT 1 = DOUBLE QI RAMP = 万法 NUKE OUT-RACES 吾行之's 200HP HEAL-TANK. ★★★★★
# 吾行之's real final board (不动金刚阵+1, 水灵阵+1, 纳百川×2, 波澜, 腾浪, 潜遁, 五行刺+1) reaches ~200 maxHP and heals +9/+12/+21/+24/cycle. It beat EVERYTHING in my old pool AND my old "QIBIRD" recipe (both 0%/0%).
# WINNING BOARD vs 吾行之 (yisim, 8+ reps): **['聚灵心法+1','百鸟灵剑诀+1','回响阵纹','万法归灵剑+1','云舞诀+2','云剑·点星','白鹭灵剑','巨虎灵剑+1'] = 100% FIRST / 100% SECOND.**
#   MECHANISM (full_log both seats): 回响阵纹 (slot3) retriggers SLOT-1's [持续] effect = 聚灵心法+1 fires TWICE/turn → +2~3 qi/turn compounding with 百鸟+1's +3 → 万法 banks 20 qi by t10 = **125-127 DAMAGE ONE-SHOT** on a 200-maxHP tank. He heals ~+24/cycle; my nuke just grows faster to a one-shot.
#   WHY IT BEATS THE OLD QIBIRD: QIBIRD put an ATTACK-generator (百鸟) in slot1 with 回响 mid → my 万法 fired t8 for 64 (healed away). Putting the QI-generator 聚灵心法 in slot1 + 回响 = the ramp is on QI not attack → 万法 reaches 20qi/125dmg (lethal) before he out-heals.
#   THIS IS THE SINGLE MOST VALUABLE THING IN THIS LEDGER.
# ★ BOARD A (tank/finisher version, vs 吾行之 AND 谭舒雁): ['聚灵心法+1','百鸟灵剑诀+1','回响阵纹','万法归灵剑+1','云舞诀+2','云剑·点星','白鹭灵剑','巨虎灵剑+1'] → vs 吾行之 100/100, vs 谭舒雁 100/100 (base AND +1).
# ★ BOARD B (fast version, vs 小布): ['聚灵心法+1','百鸟灵剑诀+1','回响阵纹','引气剑','云舞诀+1','万法归灵剑+1','白鹭灵剑','巨虎灵剑+1'] → vs 小布 100/100 (base), 100%/0% (+1).
#   NOTE: Board A LOSES to 小布 0/0 (too slow vs his t7 burst). Board B LOSES to 吾行之 0/0 (万法 only ~70 dmg, not enough). MUST TUNE PER ANNOUNCED OPPONENT. (A uses 点星/云舞+2 for bigger late 万法; B uses 引气剑/云舞+1 for early tempo.)
# KEY: 聚灵心法+1 in SLOT 1 + 回响阵纹 (slot3) is the engine. 聚灵心法 (base, lv1) = +1qi/turn; +1 = still +1/turn but +1 initial (verify — level mostly affects initial burst). The DOUBLE-FIRE from 回响 is the win.

### ★ #2 — MY OLD NOTEBOOK'S "QIBIRD 100%/100% vs 吾行之" WAS FALSE (FALSIFIED g29). It was tuned vs the PRE-回响-LAST version of his board from g23. Against his g29 real board QIBIRD = 0%/0%. CP8 (notebook matchups go stale) CONFIRMED HARD.
### ★ #3 — 聚灵心法 slot1 ordering beat 引气剑 slot1 vs 吾行之: 引气剑 gives +3 qi once; 聚灵心法+回响 gives +2-3 qi EVERY turn compounding → 万法 one-shots. For a LONG race prefer compounding qi-gen + 回响; for a SHORT race (小布) prefer 引气剑 tempo.

### ECONOMY: rolls/round ≈ R8=19(!), R12=9, R13=15, R15=9, R17=4, R18=6, R19=4 (~66). R8=19-roll SHOTGUN at 境3→境4 (pre-境5, all junk) = worst leak (M29 AGAIN). Broke 境4 @R8, 境5 @R12 (修为55). 修为 ended 96 (2nd of field, 吾行之 91, 小布 93, 谭舒雁 69). R19 spent bank to absorb to 96 for seat — LOST seat race anyway (吾行之 out-gained). Bank hit cap-ish (22 left).
# 吾行之 (WINNER) economy: broke 境5 R13 (LATE) via 25-roll named dump; ended 修为91. WON with the LATEST 境5 break — his tank board, not his economy.
### PER-RIVAL: vs 吾行之 2W-7L (beat by his 200HP 水灵 heal-tank; now SOLVED with Board A). vs 小布 7W-3L (my 万法/内伤 boards mostly out-raced his burst; R15-16 losses when I fielded slow 内伤 boards). vs 谭舒雁 3W-1L (my boards out-race her 内伤 clock; Board A 100/100).
### SURPRISE: 吾行之's tank is beatable with a QI-COMPOUNDING 万法 one-shot. I had ALL these cards (聚灵心法, 回响阵纹, 点星, 云舞) in my pool/hand most of the game and fielded 邪蛊陣+raw-swords instead. CP "name the engine when you have it" — I had the answer, never assembled it.
### REACHABILITY of Board A: 聚灵心法 (dealt R19), 百鸟+1 (had it), 回响阵纹 (I ROLLED one R19 - "rolled 水月剑阵 -> ..."), 万法+1 (had it), 云舞+2 (had +1, needed merge), 点星 (had it), 白鹭 (rolled R19), 巨虎+1 (had it). ~7/8 pieces IN HAND/RESERVE at R19. Only 回响 was a roll away.

==== LEDGER ENTRY · Game 25 ====
==== LEDGER ENTRY · Arena Game 25 ====
## ARENA Game 25 — 牧逸风 (pid0) (云剑 sect1 + 阵法师5) — RESULT: NOT 1st, final 命 0. WINNER = 谭舒雁 (pid1, 命40). 吾行之(pid2) & 小布(pid3) also dead 命0.
W/L: R1 W(pid3) R2 W(pid2) R3 L(pid1) R4 L(pid3) R5 W(pid2) R6 L(pid3) R7 W(pid1) R8 L(pid2) R9 L(pid1) R10 W(pid2) R11 L(pid1) R12 W(pid2) R13 L(pid1) R14 W(pid3) R15 L(pid1) R16 W(pid1) R17 L(pid1,DIED -22). 8W-9L.
Final 修为81 境5 maxHP107 体魄0. Seat vs 谭舒雁: I went SECOND (81 vs 82 修为) — decisive.
FATES: 云雾变幻, 顿悟, 剑阵守护, 云影化身, 云之道 (all economy-ish; 云影化身 = lethal-save).
Final board: ['聚灵心法', '百鸟灵剑诀', '引气剑', '化灵诀', '回响阵纹', '灵气灌注', '白鹭灵剑', '万法归灵剑+1'].

*** ★★★★★ #1 ROOT CAUSE — I LOST R17 TO A SINGLE SLOT-ORDER MISTAKE, NOT A BOARD-COMPOSITION ERROR. ★★★★★ ***
My R17 board HAD the whole engine (聚灵心法 slot1 + 百鸟 + 回响 + 万法+1) but 灵气灌注 sat at SLOT 7.
R17 real log: 万法 fired t8 with only **15 qi = 88 dmg** → 谭舒雁 survived at 8 HP (she'd healed 12+7 via 命运轮回+1/吉运初显), then her 11-stack 内伤 killed me t9. RAZOR-THIN.
*** THE FIX (yisim-verified): SAME 8 CARDS, move 灵气灌注 from slot 7 → slot 4:
    ['聚灵心法','百鸟灵剑诀','回响阵纹','灵气灌注','引气剑','化灵诀','白鹭灵剑','万法归灵剑+1']
    → vs 谭舒雁's EXACT final board: **100% first / 100% second (5-6 reps, ~8t)** — 万法 banks 16 qi = 95 dmg, kills her t8.
    → vs 吾行之 AND 小布 final boards: 100%/100% incl. their +1 upgrades (sim_matchup 3 reps).
    search_board (locks 聚灵/百鸟/回响/万法, pools [1,2,5,7]) accepted NOTHING better — the reorder IS optimal.
  WHY: 灵气灌注 (+2 qi, earlier in cycle) banks the qi BEFORE 万法 fires; at slot 7 it arrives too late to matter. Slot order of qi-generators vs the 万法 dump is LOAD-BEARING (extends g24's "回响 retriggers slot1" finding).
  ALSO: it was NOT a seat problem — my ORIGINAL board LOSES EVEN GOING FIRST vs her final board (verified). The reorder wins BOTH seats.

*** #2 — I ROLLED AWAY THE MERGE THAT WOULD HAVE WON: R16 I was dealt 聚灵心法 and rolled it ('rolled 聚灵心法 -> 地煞剑'). I ALREADY had 聚灵心法 from R12. Two copies = 聚灵心法+1, whose per-turn qi DOUBLES (lv1 = +1qi/2turns, lv2 = +1qi/EVERY turn; card_text). Sim: ['聚灵心法+1', ...reorder board] WINS R17 going second (万法 = 95 dmg). So I had TWO independent fixes and used neither. M51 (had the answer, didn't assemble) recurs at the LEVEL/ORDER layer, not the card-choice layer.

*** ★ #3 — MATCHUP WEAKNESS FOUND: the 2× 杯弓蛇影 clock is a HARD COUNTER to my combo. ***
谭舒雁's OWN notebook says her best build is ['杯弓+2','天星·牵引+1','厄劫缠身','血光之灾','诸事不宜','梅开二度','杯弓蛇影','流水无情']. My reorder board LOSES to THAT 0%/0% both seats (she hits 15 内伤 by t7; I die t7 before my t8 万法). search_board (350 evals, pools [1,2,5,7]) found NOTHING in my pool that beats it. I beat her ACTUAL final board (吉运初显 version) only because she fielded the slower variant. LUCKY. **vs a fast 内伤 clock: my 8-slot combo is ~1 turn too slow → need +HP cards (体魄/maxHP) to survive the extra tick, or a slot-6 万法.**
  Her notebook (frozen) on ME: "pid0 牧逸风 (云剑) +1-upgraded beats me 0% (burst)" — she feared my UPGRADED board; the game was decided by her having 3-4 merges (杯弓+1/诸事不宜+1/命运轮回+1) and the seat while I had ONE (万法+1).

*** ECONOMY AUDIT (mine): rolls/round ≈ R7=2, R10=26(!), R12=9, R15=13, R16=13 (~63). ***
- R10 = 26-roll SHOTGUN at 境4 (pre-境5) → landed only junk (board ['引气剑','巨鹏灵剑','白鹭灵剑','巨鲲灵剑','引雷阵']). M29 AGAIN, worst leak. 26 exchanges for ~0 board value.
- I broke 境5 at R12. 吾行之 AND 小布 both broke 境5 at R11 (ONE round earlier) via a SINGLE named dump. My pacing LAGGED one round.
- R15=13 (landed 万法, merged 万法+1), R16=13 (landed 回响, merged 百鸟+1 — GOOD, but ALSO rolled away the 聚灵心法 merge).
- Pattern (now 7 games): rivals absorb hard + fire ONE post-gate named dump + STOP. I split into R10 pre-gate shotgun + R15/16 post-gate. Consolidate: NO pre-gate shotgun; save exchanges for ONE post-境5 named dump.

*** PER-RIVAL ***
- 谭舒雁 (pid1, WINNER, 内伤 clock): 3W-5L (W R7,R16; L R3,R9,R11,R13,R15,R17). Beat me whenever her clock assembled; I won the two times I out-raced. The reorder fix flips R17. Her 2× 杯弓 is the real wall.
- 小布 (pid3, 崩拳 burst): 2W-2L. Won my two 万法 boards; lost R4/R6 early with piles.
- 吾行之 (pid2, 水灵 tank): 4W-1L (L R8). My reorder board = 100/100 vs him — he was my EASIEST matchup this game (unlike g23/g24 where his tank was the boss). The 万法 one-shot is the tank answer.

*** TOP DISCOVERY [g25]: SLOT-ORDER within the engine board decides the game. SAME CARDS, 灵气灌注 slot7→slot4 = 0% → 100%. Always 2-3 A/B sim_matchup the qi-generator positions before set_board; do not just sim "does my board win". ***
*** REACHABILITY: reorder = 0 new cards (pure). 聚灵心法+1 = 1 merge (2 copies, both dealt R12/R16 I owned). Both fixes were FREE. ***
*** SURPRISE: I broke 境5 R12 (1 round behind the winners R11), went SECOND by 1 修为, and lost by exactly one 内伤 tick — the game was that close and the fix was one card slot.

==== LEDGER ENTRY · Game 26 ====
==== LEDGER ENTRY · Arena Game 26 (ARENA g26) ====
## ARENA Game 26 — 牧逸风 (pid0) (云剑 sect1 + 阵法师5) — RESULT: NOT 1st, final 命 0. WINNER = 小布 (pid3, 命17). 吾行之(pid2) & 谭舒雁(pid1) also dead 命0.
W/L: R1 L(pid3) R2 L(pid1) R3 L(pid3) R4 L(pid1) R5 L(pid2) R6 W(pid3) R7 W(pid2) R8 L(pid3) R9 L(pid2) R10 W(pid1) R11 L(pid2) R12 L(pid3) R13 W(pid2) R14 W(pid3) R15 W(pid1) R16 L(pid2) R17 W(pid2)+W(pid3) R18 L(pid2)+L(pid3) DIED. ~8W-12L. Opened 0-5 (dumped -22命 by R5) — the early-game hole was never fully climbed.
Final 修为93 境5 maxHP116 体魄0. Seat: 修为 93 = 2nd (tied 小布 93, ahead 吾行之 80). I HAD the seat vs 吾行之.
FATES: 云雾变幻, 云之道, 锻体, 云影化身, 狂之执念 (default-ish; 云影化身 = lethal-save).
FINAL BOARD (last ~6 rounds): ['百鸟灵剑诀','引气剑+1','引气剑','化灵诀','灵气灌注+1','白鹭灵剑+1','万法归灵剑+1','云剑·汇灵'].

*** ★★★★★ #1 ROOT CAUSE — I FIELDED THE PLAIN QI-BATTERY INSTEAD OF THE 聚灵心法+回响 DOUBLE-QI ENGINE. THE ENGINE BOARD SWEEPS THE WHOLE LOBBY. ★★★★★ ***
My final board (above) beat 谭舒雁 100/100 (matrix confirms) but LOST to 小布 0%/0% and 吾行之 0%/0% — my elimination.
THE FIX (yisim-verified, POST-GAME search_board):
   ['聚灵心法','回响阵纹','灵气灌注+1','引气剑+1','白鹭灵剑+1','万法归灵剑+1','百鸟灵剑诀','云剑·汇灵']
   → vs 小布(pid3) FINAL board: **100% first / 100% second** (5-6 reps), also 100% first vs his +1 board. (Was 0/0 with my battery.)
   → vs 谭舒雁(pid1) FINAL board: **100% first / 100% second**.
   → vs 吾行之(pid2) FINAL board: **100% going first** (I had the seat, 修为 93>80). 0% going second (seat race).
   → THIS SINGLE BOARD WINS MY ENTIRE R18 (both pid2 and pid3).
MECHANISM (full_log): 聚灵心法 in SLOT1 ([持续] +1qi every 2 turns) + 回响阵纹 ADJACENT (slot2) retriggers slot1's [持续] effect → +2 qi-stacks/turn → the qi bank compounds fast. 万法 at SLOT6 fires ~t6 with ~12 qi = 76 dmg (one-shots 小布's 139HP before his t6 崩拳·惊触 finish), OR 万法 stuffed earlier banks more for 吾行之's 151HP tank. The DOUBLE-QI ramp is what makes 万法 reach lethal on time. (This is the SAME engine as g24's #1 discovery — I re-derived it from scratch this game because I never wrote it into the notebook as a RECIPE.)

*** ★ #2 — 万法's SLOT POSITION IS MATCHUP-DEPENDENT (extends g25's "slot-order is the whole game"). ***
- vs FAST BURST (小布): 万法 must fire by t6 → put it SLOT6 with minimal bank; win 100/100.
- vs HEAL-TANK (吾行之): 万法 must bank big → put it SLOT3-ish (search found slot3 = 100%/100% vs him); a slot6 board is only 100%first/0%second vs him.
- The two optimal orders share the SAME 6 engine cards; only 万法's slot + the trailing 白鹭/百鸟/汇灵 order changes. Decide per ANNOUNCED opponent.

*** ★ #3 — I ROLLED AWAY 回响阵纹 TWICE (R13: '回响阵纹 -> 龟甲阵' and '回响阵纹 -> 天罡聚力阵'). ***
回响阵纹 = 6 copies, sidejob-5 card, 10.3%/sidejob-deal. It is THE linchpin of the engine. I held it in hand at R13 and burned it both times chasing. MISTAKE: I never had a NAMED roll target of 回响阵纹/聚灵心法 because my notebook carried the g24 finding as prose, not as a RECIPE/KEEP-LIST. Fix: 回响阵纹 + 聚灵心法 are now TOP KEEP-LIST cards.

*** #4 — ECONOMY LEAKS (rolls/round): R9=12(!), R11=7, R13=26(!), R14=4, R15=2. ***
- R9 = 12-roll SHOTGUN at the 境3→境4 gate (pre-境5) → landed only junk (bought nothing). M29 7th confirmation.
- R13 = 26-roll shotgun right after 境5 → this one DID land 万法 + (a 回响 it then rolled away) + 云舞, but it also burned the 回响 copies. A NAMED dump (targeting 回响+聚灵) would have assembled the engine.
- Pattern (now 8 games): rivals absorb hard R1-R10, break 境5 R11, ONE named dump, STOP. I kept splitting my rolls and shotgun-rolled at gates.

*** PER-RIVAL (final boards, matrix): ***
- vs 小布(pid3, WINNER, 崩拳 burst): my battery 0/0. Engine board 100/100. He wins by t6-8 chase burst (崩拳·闪击 opener → 7 agi → auto-chase). Answer = win the t6 race with a fast 万法, OR go 内伤-clock+survival (per 谭舒雁).
- vs 吾行之(pid2, 水灵 heal-tank): my battery 0/0; engine board 100% first (I had seat). Answer = big 万法 one-shot, seat-locked.
- vs 谭舒雁(pid1, 内伤 clock): my battery 100/100. Easiest matchup this game (opposite of g25 where she was the wall).

*** TOP DISCOVERY [g26]: THE 聚灵心法(SLOT1)+回响阵纹(ADJACENT) DOUBLE-QI ENGINE, WITH 万法 AT SLOT6, WINS THE ENTIRE FINAL ROUND (小布 AND 吾行之 AND 谭舒雁) — my plain battery lost to 2 of 3. I had 回响 in hand and rolled it away. The engine is a RECIPE, not a prose note. ***
*** SURPRISE: 小布's 崩拳 burst (the lobby's fastest kill) is BEATABLE if my 万法 fires by t6 — the double-qi ramp gets there. The deciding variable is 万法's slot, not "do I have enough HP".
*** REACHABILITY: 回响阵纹 (6 copies, 10.3%/sidejob-deal — I DREW it), 聚灵心法 (8 copies, 4%/sect-deal — common). Both highly reachable; the fix is assembly + keeping 回响.
*** SURPRISE 2: 谭舒雁 (g25's champion, clock+sustain) was my EASIEST matchup this game — the lobby's RPS shifted; 小布's burst was the new boss. Trust the ANNOUNCED matchup, not last game's labels (CP8 again).

==== LEDGER ENTRY · Game 27 ====
==== LEDGER ENTRY · Arena Game 27 (ARENA g27) ====
## ARENA Game 27 — 牧逸风 (pid0) (云剑 sect1 + 阵法师5) — RESULT: ★★★ 1st PLACE / WINNER ★★★, final 命 59.
Lobby: pid1 谭舒雁 (命理师7) dead, pid2 吾行之 (水灵tank/阵法师5) dead, pid3 小布 (崩拳burst/阵法师5) dead.
W/L: R1 L(pid2) R2 L(pid3) R3 W(pid2) R4 W(pid3) R5 W(pid2) R6 W(pid1) R7 W(pid3) R8 W(pid1) R9 W(pid3) R10 L(pid1) R11 W(pid2) R12 L(pid1) R13 W(pid3) R14 W(pid1) R15 W(pid3) R16 W(pid2) R17 W(pid3) R18 W(pid3,TITLE FIGHT). 15W-3L. Recovered from an 0-2 open.
Final 修为95 境5 maxHP114 体魄0. Seat: 修为 95 = HIGHEST (ahead 小布 85, 我 went FIRST in R18). Gates: 境2@R3, 境3@R6, 境4@R9, 境5@R12.
FATES: 云雾变幻, 锻体, 云海连绵, 云影化身, 云剑传承 (default-ish; A/B showed combat-neutral — identical output with/without).
FINAL BOARD: ['聚灵心法+1','回响阵纹','百鸟灵剑诀+1','引气剑+1','白鹭灵剑','万法归灵剑','化灵诀+1','云剑·汇灵'].

*** ★★★★★ #1 — THE ENGINE RECIPE FINALLY WORKED AND WON THE GAME. ★★★★★ ***
I assembled 聚灵心法(SLOT1)+回响阵纹(SLOT2) for the first time in a real game (g25/g26 I carried it as prose and never fielded it).
R18 real log: 聚灵心法+1 [持续] +1qi EVERY turn, 回响阵纹 retriggers it, 百鸟/引气/化灵 batteries → qi bank ramps ~+7-8/turn. 万法 lv1 fired t6 with **17 qi = 90 dmg** → one-shot 小布's 144-HP board (he was at -2). This is the g26 ledger's predicted recipe, EXECUTED.

*** ★★★★★ #2 — FINAL MATCHUP IS A SEAT RACE, AND I WON IT. ★★★★★ ***
vs 小布(pid3) FINAL board: my board wins 100%/100%. vs his MAXIMALLY-UPGRADED board (连崩+1 master) it is 100%-FIRST/0%-SECOND — a pure seat race. I held first seat (修为 95 > his 85), so I won. Verified: sim vs his master board going first = WIN (万法 89-90dmg t6), going second = LOSE (his extra 连崩+1 hit lands first).

*** ★ THE FIX FOUND (search_board + yisim): swap 白鹭灵剑(chip, slot5) → 化灵诀(+3qi battery, slot5). ***
  Board: ['聚灵心法+1','回响阵纹','灵气灌注+1','引气剑+1','化灵诀','万法归灵剑+1','百鸟灵剑诀','云剑·汇灵']
  → vs 小布's master board +1: 100% FIRST / 100% SECOND (qi bank 20 = 124 dmg one-shot, survives his t6b finisher at 4-6 HP).
  → ALSO 100/100 vs 吾行之 tank (both seats, both levels).
  → BUT 0/0 vs 谭舒雁 (内伤 clock)! Without the 白鹭 chip, 万法 leaves her at 7 HP and her clock kills me.
  ★ LESSON: NO SINGLE BOARD beats all three; the tradeoff is CHIP (beats clock) vs EXTRA-QI-BURST (beats seat-race). MATCHUP-DEPENDENT (extends CP15).
  THE BEST UNIVERSAL BOARD (search_board-verified, 100/100 vs 谭 AND 吾行之 incl +1, 100%first/0%second vs 小布+1):
   ['聚灵心法+1','回响阵纹','百鸟灵剑诀+1','引气剑+1','白鹭灵剑','万法归灵剑+1','化灵诀+1','云剑·汇灵'] (my actual board but 万法 UPGRADED to +1).

*** ★★★ ECONOMY AUDIT: NO MAJOR LEAK THIS GAME. rolls/round = R7=4, R8=2, R12=26, R13=6, R14=5, R16=10 (~53). ***
- R12=26 shotgun — but this one ASSEMBLED the engine (聚灵+1, 回响 via R16, 引气+1, 百鸟+1, 化灵+1). NOT a waste (unlike g26's R13=26).
- R16=10 landed 回响阵纹 = THE linchpin. R13=6, R14=5 minor.
- I broke 境5 at R12 (one round behind 小布's R12 tie; he also broke R12). Fine.
- 小布 (winner's economy in g26) = ~31 rolls TOTAL vs my ~53. He's leaner; I had a productive 26-roll dump. NET: acceptable.

*** ★ REACHABILITY OF THE FIX: I ONLY EVER DREW 万法归灵剑 ONCE (R15 sect deal) — never 2 copies, so 万法+1 (the fix's key) was UNREACHABLE. My game was already draw-optimal. The 白鹭→化灵诀 swap WOULD have been free (I had both) and fixes the seat-race — THAT is the actionable lesson. ***

*** PER-RIVAL ***
- 小布(pid3, 崩拳 burst): 4W-1L (L R2 early pile). Won every mid-late fight with the engine board. His master board beats me going 2nd; I held seat. ANSWER: win the t6 race (万法 qi bank) OR hold seat.
- 谭舒雁(pid1, 内伤 clock): 2W-2L (L R10,R12). Her clock ticks 7→9→13→14; my board beats her ACTUAL final board 100/100 (chip + 万法 kills t6-11). The 化灵诀 board LOSES to her — keep the 白鹭 chip.
- 吾行之(pid2, 水灵 tank): 4W-1L (L R1). EASIEST matchup. 万法 one-shots his ~140 maxHP. 100/100 both boards.

*** TOP DISCOVERY [g27]: THE ENGINE RECIPE WINS THE LOBBY WHEN ASSEMBLED — finally fielded 聚灵心法+回响阵纹 and went 15W-3L to WINNER (命59). The single remaining gap is a SEAT RACE vs a fully-upgraded 小布, fixable by swapping the 白鹭 chip slot for a 化灵诀 qi battery (100%-first→100%-both), at the cost of losing to the 内伤 clock. ***
*** SURPRISE: I won the whole lobby after opening 0-2. The 命 economy (lose cheap early, win the fat late rounds — R16 -31, R18 -28) let me climb from a hole. Late rounds carry 20-31命/swing; early rounds 2-5. PLAY THE LONG GAME.
*** SURPRISE 2: 吾行之's playbook claims his canonical tank beats my 万法 100/100 — but he fielded a WEAKER water board (纳百川×3/波澜×2/泉涌×2, no 不动金刚阵, no 潜遁). His THEORETICAL board may beat me; his ACTUAL one didn't. Trust the sim of the ACTUAL last board (CP8).

==== LEDGER ENTRY · Game 28 ====
## ARENA Game 28 — 牧逸风 (pid0) (云剑 sect1 + 阵法师5) — RESULT: ★★★ 1st PLACE / WINNER ★★★, final 命 1.
Lobby: pid1 谭舒雁 (命理师7) dead 命0, pid2 吾行之 (水灵 tank) dead 命0, pid3 小布 (崩拳 burst) dead 命0 (lost the R19 title fight to me, -31命).
W/L (19 battles): R1 L(pid1) R2 L(pid2) R3 L(pid3) R4 L(pid1) R5 L(pid2) R6 L(pid3) R7 W(pid1) R8 L(pid3) R9 W(pid1) R10 W(pid3) R11 L(pid2) R12 W(pid3) R13 W(pid2) R14 W(pid1) R15 L(pid3)+L(pid2) R16 L(pid3)+W(pid2) R17 W(pid3) R18 W(pid3) R19 W(pid3,TITLE). 10W-9L — I opened 0-6 then won the late fat rounds. 修为97 (HIGHEST), 境5, maxHP111, 体魄0. Gates: 境2@R3, 境3@R6, 境4@R9, 境5@R13.
FATES: 云雾变幻, 储纳灵气, 云海连绵, 云影化身, 云泉道茶 (default-ish; 云泉道茶 = -1修为/2 upgrade cards).

*** ★★★★★ ROOT CAUSE OF THE WIN: THE 聚灵心法(SLOT1)+回响阵纹 DOUBLE-QI ENGINE → 万法归灵剑 ONE-SHOT. FINALLY EXECUTED. ★★★★★ ***
My final board: ['聚灵心法+1','回响阵纹','百鸟灵剑诀','化灵诀','云舞诀','巨鲲灵剑+1','白鹭灵剑+1','万法归灵剑'].
R19 real log (TITLE fight vs 小布): 聚灵心法+1 [持续] +1qi/EVERY turn (lv2), 回响阵纹 retriggers it → +2qi/turn compounding with 百鸟+化灵+云舞 → qi bank 18 by t7 → 万法归灵剑 fired t7a for **95 dmg**, one-shot 小布's 174 HP board (he was at -41). R17 (97 dmg) and R18 (95 dmg) same line. THIS is the recipe my g26/g27 ledgers predicted — and it won the title.
MECHANIC CONFIRMED (card_text): 聚灵心法 lv1 = +1qi every 2 TURNS; lv2 (+1) = +1qi EVERY turn. 回响阵纹 retriggers slot-1's [持续] effect. So 聚灵心法+1 (slot1) + 回响 = +2qi/turn. 白鹭灵剑 = +3dmg per remaining qi → placed before 万法 it hits for 38-53. 百鸟 lv1 = +1qi, lv2 = +3qi, + [持续] 灵剑 qi-cost -1.

*** ★★★★★ #1 IMPROVEMENT FOUND (search_board + yisim, 4+ reps, BOTH seats): REORDER + UPGRADE = UNIVERSAL BOARD. ★★★★★ ***
THE BOARD: ['聚灵心法+1','回响阵纹','化灵诀','云舞诀+1','巨鲲灵剑+1','白鹭灵剑+1','万法归灵剑','百鸟灵剑诀']
→ 100%/100% vs 谭舒雁 FINAL board AND her +1 board.
→ 100%/100% vs 吾行之 FINAL board AND his +1 board.
→ 100%/100% vs 小布 FINAL board AND **his absolute MASTER board (惊触+2, 弹+1, 戳+1)** — BOTH seats (t6, 74-75 dmg kill).
This board is STRICTLY BETTER than my actual final board (mine was 0% going second vs 小布+1). TWO changes:
  (1) REORDER: move 百鸟灵剑诀 to SLOT 8 (last) and 万法归灵剑 to SLOT 7. 百鸟's [持续] aura only needs to be on the board, not early — the qi comes from 聚灵心法+回响. Putting 万法 one slot earlier makes it fire t6 instead of t7.
  (2) UPGRADE 云舞诀 to +1 (+2qi → 万法 fires with 14 vs 13 qi = 74 vs 70 dmg = the killing margin).
★ NOTE THE SEAT NUANCE: my ORIGINAL order (万法 slot8) banks DEEPER (18 qi = 95 dmg) and wins the FIRST seat vs even 小布's master board; the REORDER (万法 slot7) fires EARLIER and wins when going SECOND. A/B: original order + 云舞lv1 = 100first/0second vs 小布+1; reorder+云舞lv1 = 0first/100second; reorder+云舞+1 = 100/100 vs everything. THE ROBUST BOARD NEEDS BOTH the reorder AND 云舞+1. (Extends CP1: order is matchup AND seat dependent.)

*** ★★★ ECONOMY AUDIT: CLEANEST YET — the R13/R17 NAMED dumps did the work. ***
rolls/round: R1-R8=0 (banked 3→24, no cap waste), R9=13, R10=0, R11=10, R12=0, R13=23, R14-16=0, R17=23, R18-19=0 (~69 total).
- R9=13 + R11=10 were at 境4 (万法/回响 LOCKED at 境5) → pre-境5 leak (M29 8th confirmation). R13/R17 (both post-境5) were PRODUCTIVE: R13 landed 百鸟+1/闪风+1; **R17's 23-roll run landed 万法 (24th roll) AND 回响 — the two cards that won the game.**
- Broke 境5 at R13 (修为55). Kept 修为 97 = first seat all endgame → won every must-win seat race.
- LESSON: hoard rolls R1-R12, break 境5, then ONE 20+ NAMED dump. My R13+R17 were exactly that. The only leak was R11=10 (pre-境5, but it landed 百鸟 = a keep, so near-neutral).

*** PER-RIVAL (final boards, matrix + my sims): ***
- 小布(pid3, 崩拳 burst): 4W-3L endgame (L R15/R16 pre-engine R16b; W R17/R18/R19 once engine online). His burst kills t7-9 (闪击→身法≥10 auto-chase→威震四方+1 cap10→惊触追加). I beat him by winning the SEAT RACE (修为97>90) and firing 万法 t6-7 before his finisher. ANSWER: engine + seat.
- 吾行之(pid2, 水灵 tank): he was DEAD by R19 but my board 100/100 vs his final. 万法 one-shots his ~140 HP.
- 谭舒雁(pid1, 命理师 clock): 100/100 both boards. Easiest.

*** TOP DISCOVERY [g28]: THE UNIVERSAL ENGINE BOARD `['聚灵心法+1','回响阵纹','化灵诀','云舞诀+1','巨鲲灵剑+1','白鹭灵剑+1','万法归灵剑','百鸟灵剑诀']` WINS 100/100 vs EVERY rival's final board AND +1 upgrade incl. 小布's master +2 BOARD — TWO free changes (reorder 百鸟→slot8/万法→slot7, upgrade 云舞诀). My game-winning board was already the engine; this is the polish. ***
*** SURPRISE: I won the WHOLE LOBBY after opening 0-6. The 命 economy (lose cheap early -2/-3/-4, win the fat late rounds -25/-31) let me climb from a deep hole. PLAY THE LONG GAME (g27 surprise confirmed again). ***
*** SURPRISE 2: 小布's own playbook (frozen) says his g28 (=his win) came from out-bursting me t7a with 戳/弹→惊触 ordering, and his g27 lesson was "不动金刚阵 as universal 8th slot vs 万法". But in MY g28 he fielded NO 不动金刚阵 and I out-ran him. His theoretical master board beats my ACTUAL board going second — but my IMPROVED board beats even that. Trust the seat + the reorder.
*** REACHABILITY: 聚灵心法 (8 copies, 4%/sect-deal), 回响阵纹 (sidejob5, 10%/deal), 万法 (6 copies 境5). I drew all three by R17. 云舞诀 upgrade = 2 copies (drew 云舞 multiple times). All reachable.

==== LEDGER ENTRY · Game 29 ====
## ARENA Game 29 — 牧逸风 (pid0) (云剑 sect + 阵法师5). RESULT: NOT 1st — final 命 0 (2nd of the standings; winner 谭舒雁 pid1 命87). Rivals: 谭舒雁(命理师7) WINNER 87, me/吾行之(水灵 tank)/小布(崩拳 burst) all 命0.
W/L (15 battles): W R1(pid1) L R2(pid3) W R3(pid2) L R4(pid1) L R5(pid3) L R6(pid1) W R7(pid3) W R8(pid2) W R9(pid3) L R10(pid1) L R11(pid2) L R12(pid1) W R13(pid3) L R14(pid2) L R15(pid3). 6W-9L. Started 1-0 then 1-5; rallied 3 wins R7-R9 then collapsed 1-5 late. Gates: 境2@R3, 境3@R6, 境4@R9, 境5@R11 (via absorb, 修为55). Ended 境5 修为74 maxHP103. FATES: 云雾变幻, 云剑传承, 云海连绵, 云影化身, 剑韵修炼 (economy/misc — A/B re-verified neutral).

FINAL BOARD (the pile that lost): ['邪蛊阵','回响阵纹+1','云舞诀','辟邪阵纹+1','巨鲲灵剑','形意剑','云剑·游龙+1','飞灵闪影剑']
card_stats(R15): total ~32 dmg over 11 turns; 邪蛊阵/回响阵纹 did 0 dmg; NO 万法, NO 聚灵心法. THIS WAS NOT THE ENGINE. It was a chip/内伤 board with only one real payoff (巨鲲 10 dmg, 形意 8).

*** ★★★★★ ROOT CAUSE #1 (>90% of the loss): I NEVER ASSEMBLED THE 万法 ENGINE. ★★★★★ ***
g27 (WINNER 命59) and g28 (WINNER 命1) were BOTH won by the board ['聚灵心法+1','回响阵纹',...,'万法归灵剑','百鸟灵剑诀']. This game I fielded a chip pile instead. sim_matchup PROVES it: my actual final board is **0%/0% vs 谭舒雁's final board**; the g28/g27 engine board is **100%/100%**. Same lobby, same rosters — the ONLY difference is assembly. This is the 1st game where the failure was purely "did not field my own proven win-con."

*** ★★★★★ ROOT CAUSE #2: DISCIPLINE — I ROLLED AWAY 聚灵心法 AT R13. ★★★★★ ***
economy_history R13: "rolled 巨鲸灵剑 -> 聚灵心法 ... rolled 聚灵心法 -> 骤风剑" — I DREW 聚灵心法 (the #1 engine card, slot-1 of the whole board) and immediately rolled it into junk. Also R13 drew 云剑·游龙/云剑·汇灵 and I kept the CHIP cards over the battery. Same class of error as 小布's g28 (rolled 连崩 twice) and 谭舒雁's g28 (rolled 诸事不宜) — ALL FOUR bots lost games to rolling KEEP-LIST pieces. M-X1 recurrence #N.

*** ★★★★★ ROOT CAUSE #3: PRE-境5 SHOTGUNS COST ME THE SEAT. ★★★★★ ***
rolls/round: R1-R9 = 0,0,0,0,0,3,0,0,5 (8 total); R10=12, R11=19, R12=5, R13=7, R14=7, R15=0. 
- **R10=12 AND R11=19 were at 境4 (万法/回响 LOCKED at 境5)** — pure waste, ~31 rolls. Half of those should have been ABSORB for 修为/seat.
- Ended 修为 74 vs winner 谭舒雁 88. I LOST the seat. My engine is 100%-FIRST / ~50%-second vs her board (the 万法 fires t6 first-seat vs t11 going second = she clock-kills first). So losing the seat = losing R10/R12 directly.
- The winner 谭舒雁 rolled 0 at R1-R8, ONE 21-roll dump R9 (境4, landed 诸事不宜), then R12=15 post-境5, R14-18 = 5-11/round named dumps. Leaner AND more productive. Her 勤学苦练 fate drew cards on every absorb (visible: "勤学苦练 drew 星弈·点") = a real economy engine I undervalued.

*** ★★★★★ TOP DISCOVERY [g29]: THE ENGINE BOARD NEEDS 百鸟灵剑诀 AT SLOT 2, NOT SLOT 8 — AND THAT MAKES IT WIN BOTH SEATS. ★★★★★ ***
NEW UNIVERSAL BOARD (search_board + yisim, 4+ reps, verified THIS review):
  **['聚灵心法+1','百鸟灵剑诀','回响阵纹','化灵诀','云舞诀+1','巨鲲灵剑+1','白鹭灵剑+1','万法归灵剑']**
  - vs 谭舒雁 FINAL board: 100% first / 100% second.
  - vs 谭舒雁's MAXIMALLY-UPGRADED board: 100% first / 100% second (万法 fires t7 with **17 qi = 84 dmg** one-shot both seats).
  - vs 小布 FINAL board: 100%/100% (85-90 dmg t7). vs 小布 +1: 100% first (the old order was 0% both vs 小布+1!).
  - vs 吾行之 FINAL AND +1: 100%/100%.
  WHY: moving 百鸟 (+1qi + [持续] 灵剑-cost-1 aura) to SLOT 2 banks qi MUCH deeper (百鸟 comes online turn 2). The OLD g28 order (百鸟 slot8) fires 万法 at t6 with only 13 qi = 60 dmg going first, and STRANDS it going second (she clock-kills t11). The trace: "move 百鸟灵剑诀 slot8->slot2: win 100% first / 100% second."
  ★ This supersedes the g28 universal order. Same cards, one slot move, flips the both-seat result.

*** ★ CONFIRMED: 万法 WITHOUT the converter = DUD. ***
search_board (pool 5) of a qi-battery board `['聚灵心法','回响阵纹','云剑·汇灵','化灵诀','云舞诀','巨鲲灵剑','白鹭灵剑','百鸟灵剑诀']` = **0%/0% vs 谭舒雁**. A pure-attack board (巨鲲/形意/游龙/飞灵) = also **0%/0%**. Only the 万法 one-shot beats her clock+反震. CP4 re-confirmed.

*** ★ MECHANICS verified: 厄劫缠身 [开局] downgrades opp's SAME-SLOT card (card_text). 命运轮回 HP+8 + skip slots 4/5 + trigger their [开局]. 反震心法 reflects 2-4 per HIT — a TRAP vs my multi-hit chips (游龙/飞灵 each trigger it). 聚灵心法+1 (lv2) = +1 qi EVERY turn, and it ACCUMULATES stacks (log: +2 stacks/turn via 回响 retrigger). ***

*** PER-RIVAL (final boards, sim-verified): ***
- 谭舒雁 (命理师 内伤 clock + 反震心法+1, WINNER 命87): I went 2W-4L vs her (W R1/R9?no; actual L R4,R6,R10,R12). Her board = 杯弓蛇影×2 + 血光之灾 + 诸事不宜×2 + 反震. **My pile loses 0/0; the new engine board wins 100/100.** Her clock ticks 7→10→11/turn; 反震 punishes my multi-hit. The answer is the single t6-7 万法 one-shot (kills before the clock matters).
- 吾行之 (水灵 tank): 2W-1L (W R3,R8; L R11). Easiest — 万法 one-shots his ~130 HP. 100/100.
- 小布 (崩拳 burst): 2W-2L (W R7,R13; L R2,R5,R15). Burst kills t7. New board 100%/100% vs his g29 final.

*** SURPRISES: ***
1. The winner (谭舒雁) won the WHOLE lobby at 命87 with a board that is just my g28 "FALLBACK" (no double-厄劫) — she never drew 2× 厄劫. Her win was ASSEMBLY DISCIPLINE + economy fate (勤学苦练), not a superior recipe.
2. I verified the new order flips BOTH seats vs 小布+1 (the g28 board was 0/0 there). One slot move = the difference.
3. ALL FOUR bots' g27-g29 ledgers cite the SAME #1 root cause: "rolled away a KEEP-LIST piece" and "fielded a pile instead of my win-con." The meta is an ASSEMBLY-DISCIPLINE race, not a draw race.

*** NEXT-GAME RULES (sharpened): ***
1. R2 sidejob = 5 (阵法师 — 回响阵纹 is the engine linchpin; not replaceable). 
2. NEVER roll before 境5 beyond ≤2/round. R10-11 rolls at 境4 are WASTE (this game: 31 rolls). ABSORB everything for 修为/seat.
3. KEEP-LIST (NEVER roll): 聚灵心法, 回响阵纹, 万法归灵剑, 百鸟灵剑诀, 白鹭灵剑, 化灵诀, 云舞诀, 巨鲲灵剑, 引气剑, 灵气灌注, 云剑·汇灵. 2nd copy = MERGE.
4. TARGET BOARD: ['聚灵心法+1','百鸟灵剑诀','回响阵纹','化灵诀','云舞诀+1','巨鲲灵剑+1','白鹭灵剑+1','万法归灵剑'] — 100/100 both seats vs all three.
5. If 万法 is absent by R13, EMBRACE a fallback (battery + 白鹭 chip) but keep hunting 万法; a battery-only board is a 0/0 DUD.
6. FATES: prefer ECONOMY (勤学苦练 = draw on absorb, the winner's pick). Combat 傳承 are neutral (A/B identical).
7. SEAT = 修為; the new board is both-seat so seat is a bonus not a requirement.

==== LEDGER ENTRY · Game 30 ====
## ARENA Game 30 — 牧逸风 (pid0) (云剑 sect1 + 阵法师5). RESULT: NOT 1st — final 命0 (eliminated). WINNER = 谭舒雁 (pid1, 命10). Others: 吾行之(pid2)/小布(pid3)/me all 命0.
W/L (17 battles): L R1(1,-2) L R2(2,-3) W R3(3,-6) W R4(2,-5) W R5(3,-6) W R6(1,-8) W R7(3,-11) L R8(2,-10) L R9(1,-11) W R10(2,-17) L R11(1,-15) L R12(2,-18) L R13(3,-18) L R14(1,-17) W R15(3,-20) L R16(1,-5) L R17(1,-21). Record 6W-11L. Opened 1-1, rallied to 5-2, then collapsed 1-9 late (lost the fat late rounds that carry 命).
Gates: 境2@R3, 境3@R6, 境4@R9, 境5@R12. Ended 境5 修为86 maxHP107 体魄0. FATES: 云雾变幻, 储纳灵气, 云海连绵, 云影化身, 变换之道 (economy/misc — A/B re-neutral, 20th confirmation).
FINAL BOARD: ['聚灵心法+1','百鸟灵剑诀+1','云剑·无妄','云舞诀','凝意诀','灵犀剑阵','化灵诀','万法归灵剑+1'].

*** ROOT CAUSE #1 (the game): I LOST THE SEAT WAR (修为 86 vs 谭舒雁 98), AND the whole lobby is a SEAT-ONLY race. ***
sim proof (post-game, my live stats): my ACTUAL R17 board vs pid1 (谭舒雁) = **100% first / 100% second** vs her R17 board, and **100% first/100% second** vs her FINAL board too (with 回响 it one-shots). sim vs pid2 吾行之 = 100/100. sim vs pid3 小布 = **0% BOTH seats** (his burst kills t6, my 万法 fires t7). So the ONLY unwinnable matchup was 小布 — yet I lost R16 and R17 to 谭舒雁, the matchup I SIM-BEAT 100%. The discrepancy = my real in-round boards were weaker (I had NOT assembled 回响阵纹) AND the matrix-authoritative "0% vs 谭舒雁" is computed on a DIFFERENT (stale) 牧逸风 board — TRUST MY OWN sim of the actual board.

*** ROOT CAUSE #2: I NEVER FIELDED 回响阵纹 — it was in my POOL (6 copies, sidejob 5) ALL GAME. ***
The g27/g28 WIN-CON was ['聚灵心法+1','回响阵纹',...]. Without 回响, 聚灵心法+1 gives +1 qi/turn; WITH it, +2/turn (回响 retriggers slot-1 持续). Proof: same board 万法 fired at t8 with **21 qi=131 dmg**; with 回响 it fired t7 with **25 qi=149 dmg** → strictly wins the 谭舒雁 clock race with margin. Assembly-discipline failure (4th straight game: g27/g28 "carried as prose", g29 rolled 聚灵心法 away, g30 never drew 回响).

*** ROOT CAUSE #3: THE R12 = 37-ROLL SHOTGUN AT THE 境5 GATE. ***
economy_history R12: 37 rolls, banked 25→1. It did land 聚灵心法/百鸟+1/云舞诀/万法 — lucky — but burned ~37 exchanges that should've been ABSORB-for-修为. Ended 修为86 vs her 98 → lost EVERY seat. THIS IS THE M29 LEAK, 4TH SEAT-LOSS IN A ROW. A clean R12 (absorb + ≤8 rolls) would have given ~+20 修为 = the seat = the game.

*** ★★★★★ TOP DISCOVERY [g30]: 须弥阵纹 IMMEDIATELY BEFORE 万法 = the anti-BURST fix (fires 万法 ONE TURN EARLIER). ★★★★★ ***
- vs 小布 (his burst kills t6b, my 万法 was scheduled t7): putting 须弥阵纹 at SLOT 6 (just before 云剑·无妄→万法) makes its [再次行动] chase 万法 forward → **万法 fires t6a for 117 dmg, kills him (he was at 82)** = 100%-first WIN (was 0%).
- ORDER IS LOAD-BEARING: 须弥 at slot 7 (one too early) → chase carries 云剑·无妄 instead → LOSE t6b. It MUST be the slot directly before 万法.
- NEW BOARD B (vs BURST, all lv1 reachable): ['聚灵心法+1','回响阵纹','云舞诀','凝意诀','化灵诀','须弥阵纹','云剑·无妄','万法归灵剑+1'] = 100%-first vs 小布 (still 0% second — seat-decisive).

*** ★★★★★ TWO-BOARD PLAN (the surviving-g29 tradeoff, now explicit): ★★★★★ ***
- BOARD A (vs SUSTAIN/clock: 谭舒雁, 吾行之): ['聚灵心法+1','回响阵纹','云舞诀','凝意诀','灵犀剑阵','化灵诀','云剑·无妄','万法归灵剑+1'] = 100/100 BOTH seats vs both. (须弥 here = 0/0.)
- BOARD B (vs BURST: 小布): 须弥 at slot 6 (before 万法) = 100%-first. (回响-only here = 0/0.)
- SWITCH BY ANNOUNCED OPPONENT. NEVER field the anti-clock board vs a burst, or vice-versa.
- FULL-POWER universal (search-verified 100/100 vs ALL 3 base boards): ['聚灵心法+1','回响阵纹+1','云舞诀','凝意诀','须弥阵纹+1','化灵诀','云剑·无妄','万法归灵剑+1'] — needs 回响+1 & 须弥+1 (2 copies each); only weakness = 谭舒雁 +1 (0%).

*** ECONOMY AUDIT: rolls/round = R3=2,R8=6,R12=*37*,R13=8,R14=7,R15=6 (≈66 total). ***
- R12=37 at 境4→境5 gate = the SHOTGUN leak (should be ≤8 post-境5 rolls + absorb-all).
- R13-R15 (8/7/6) post-境5 = productive (landed 万法+1, 聚灵心法+1). Fine.
- ★ Vow: R1-R11 = 0-2 rolls/round, absorb EVERYTHING. Break 境5 by R11-12. THEN ≤6 NAMED rolls/round until 回响+须弥+万法 assembled.

*** PER-RIVAL ***
- pid1 谭舒雁 (命理师7, 内伤 clock + HP-stack, WON lobby): 2W-2L THIS game (W R6, L R9/R16/R17). My BOARD A sim-beats her 100/100 both seats / both levels of the board I actually failed to field. Her 修为 98 > my 86 → she had the seat. ANSWER: win 修为 OR field Board A (which doesn't need the seat).
- pid2 吾行之 (水灵 tank, 阵法师5): 2W-0L. Easiest — my engine 100/100 both seats both levels.
- pid3 小布 (崩拳 burst, 阵法师5): 1W-3L (only W R15). His t6 burst beats my t7 万法. BOARD B (须弥@6) fixes going first; seat-decisive.

*** SURPRISES ***
1. My actual board SIM-BEATS the lobby winner 100/100 — the loss was purely (a) never fielding 回响, (b) losing the seat by over-rolling R12.
2. 须弥阵纹's [再次行动] is a TEMPO (not sustain) answer to burst — new category. Placement = the slot before the finisher.
3. 4th straight game where I lost to NOT ASSEMBLING a card that sat in my pool all game (回响阵纹).

*** NEXT-GAME RULES ***
1. R2 sidejob=5. R1-R11 absorb-all, 0-2 rolls (KILL the R12 shotgun). Break 境5 R11-12.
2. Post-境5 NAMED dump ≤6 rolls/round hunting {回响阵纹 > 聚灵心法 > 万法归灵剑 > 须弥阵纹 > 百鸟/化灵/云舞}. STOP on hit. Bank ≤24.
3. ★ NEVER end a round post-境5 without 回响阵纹 on board if it's in pool. It DOUBLES the qi engine.
4. TWO-BOARD PLAN above; switch by announced opp; 须弥 goes IMMEDIATELY before 万法 (slot6), never earlier.
5. Merge every 聚灵心法→+1 and 万法→+1 (free seat/level). 回响+1 & 须弥+1 = the universal board.
6. 修为 = seat = the lobby. Absorb EVERY spare. Match 谭舒雁's 勤学苦练 economy (she hit 98) by out-absorbing.
