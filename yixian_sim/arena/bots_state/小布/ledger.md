# 小布 — game ledger (append-only archive)

==== LEDGER ENTRY · Game 13 ====
=== GAME (小布 sect4 崩拳, pid3) — RESULT: NOT FIRST, died R20 at 命0 ===
PLACEMENT: 3rd/4 (died last round; 牧逸风 pid0 & 吾行之 pid2 died earlier). Winner 谭舒雁(pid1) ended 命63 — she
was NEVER threatened. Runner-up ceiling.

SIDEJOB: 7 (命理师). FATES (in order): 磨砺不止, 锻体不息, 变换之道, 生机不灭, 休养生息.
(生机不灭 = once/game death-protect, DID fire? I went 4命 R18 -> lost R19 -3 -> 1命 -> R20 -29 -> -28. So NO,
it did not save me — either consumed earlier or the -29 exceeded. NOTE: verify why 生机不灭 didn't hold at 1命.)

FINAL BOARD (R20): 厄劫缠身, 崩天步+1, 起势, 崩拳·惊触+1, 崩拳·连崩+1, 崩拳·寸劲. Hand: 磅礴之势+1 unfielded.
**FATAL: NO 气势 generator on final board** -> 崩拳·寸劲 & 磅礴之势 did ~nothing. Same mistake as notebook R19 rule.

PER-RIVAL:
- pid0 牧逸风 (云剑/巨灵剑): W R7,R16; L R1,R3,R5,R10. Early losses R1/R3/R5 were CLOSE (he ended R3 at 3hp,
  R5 at 1hp) — my early board (起势/罗刹扑/锻拳+1/崩拳·弹/血气方刚/破空爪) was just short on burst.
- pid2 吾行之 (五灵/水灵): W R2,R4,R6,R9,R14; L R12. I beat him consistently early-mid.
- pid1 谭舒雁 (命理师 内伤 clock): L R11,R12,R15,R17,R18,R19,R20; W R13. **THE GAME-DECIDER.**

*** TOP DISCOVERY: 谭舒雁's endgame 内伤 board is UNBEATABLE by ANY 小布 board. ***
EVIDENCE: search_board vs pid1, start=探灵/起势/崩灭心法/势如破竹 x2/崩拳·寸劲/朝气蓬勃+1/磅礴之势, pools {base},{1,5},{7,6},{3,5},
objective both/first => 0% first & 0% second, EVERY search, ~21 evals each (no improvement ever accepted).
Archetypes tested & ALL LOSE: g9 探灵-engine, g12 踏破九霄/冲霄破浪, g7 起势/厄劫缠身, max-burst 双势如破竹, 回春曲+断肠曲 clock.
Her clock (verified R20 log): 内伤 stacks at MY turn start = 3,5,7,8,12,14,16,18 -> alone ~83 dmg over 8 turns, PLUS
card dmg. My max board reached her to ~34-37hp by turn 8 and I died. I need her dead by ~t6 (120-18hp) but can only
deal ~90 by then. Structurally short.

MECHANICS LEARNED (verified in engine):
- 内伤 (internal_injury) is dealt via reduce_idx_hp DIRECTLY -> IGNORES 防. Only 护体(guard_up, negates 1 hit),
  金蝉脱壳(covert_shift, reverses), dream-motionless/leaf-shield reduce it. Sect4 小布 has NONE of these.
  gamestate_full.js:2798 do_internal_injury; :3671 reduce_idx_hp.
- 厄劫缠身 [开局]: downgrades opponent's SAME-SLOT card by 1 level (deals 6 dmg if can't downgrade). Merge key
  cards to +2 so a single downgrade doesn't gut them.
- 断肠曲 (琴师3, [持续]): BOTH sides +1 内伤/turn; 回春曲 (琴师3, [持续]): BOTH sides +4hp&maxhp/turn end. A symmetric
  clock+heal that actually let me reach 148 maxhp — but her 内伤 output (24/turn) dwarfs my 1/turn. Not enough.
- 内伤 damage is UNSTOPPABLE — no "辟邪"/hexproof resistance exists in engine for it (grep found nothing).

ECONOMY: broke 境2@R3, 境3@R6, 境4@R9, 境5@R13 (修为 36@R9, 55@R13). 修为 91@R18, 104 final. Fine.
Roll audit: R9 spent 24 exchanges (over-rolled hunting 崩天步 — got it eventually). R18 spent 25 (over-rolled,
gutted board). R19 spent 10 (gutted 崩灭心法+威震四方 = THE fatal mistake). Banked 21-23 at R16/R17 caps — WASTED grants.

SURPRISE: Winner's board (命理师 内伤) beats EVERY OTHER final board 100% per the matrix — it's a rock-paper-
scissors blind spot in this lobby (nobody else ran 内伤-resist). Next game: if 谭舒雁/命理师-leaning rival is in the
lobby, consider picking a sidejob with 内伤 mitigation or racing harder (win early, deny her lategame).

==== LEDGER ENTRY · Game 14 ====
==== LEDGER ENTRY · Game 14 ====
=== GAME (小布 sect4 崩拳/气势, pid3) — RESULT: NOT FIRST, died R20 at 命0. PLACEMENT 3rd/4 (牧逸风 pid0 & 吾行之 pid2 died earlier; winner 谭舒雁 pid1 ended 命63 — again!) ===
WAIT — matrix says winner was pid1 谭舒雁 (命63). Final: 牧逸风 pid0 LAST BOARD shown alive 命13 in my R20 obs but matrix suggests pid0 also died. In any case I did NOT win; died R20 to 牧逸风 -32命.

SIDEJOB: 7 (命理师). FATES: 磨砺不止, 稳固根基, 灵涌不竭, 生机不灭, 休养生息.
FINAL BOARD (R20, what I actually fielded): 厄劫缠身, 探灵+1, 起势+1, 踏破九霄, 诸事不宜, 势如破竹+1, 饿虎扑食+1, 磅礴之势.
HAND AT END (UNUSED WIN-CON): 天机·逆施 (never fielded!), 天星·御心, 崩拳·封, 势如破竹, 磅礴之势.
修为 97, 境5, maxHP 123. 20 exchanges banked at end (wasted — never spent).

*** TOP DISCOVERY: 内伤 clock + 天机·逆施 def→dmg BEATS 牧逸风; I had BOTH pieces and fielded NEITHER. ***
EVIDENCE (yisim, me-first, vs his EXACT final board):
- My ACTUAL R20 board: sim_matchup 100% first ... but real R20 LOST -32 (his real board stronger than last-shown / RNG). Died t10 to 万法归灵剑 44dmg + 巨鲲chase.
- BEST board (search_board op=first, yisim-verified): **厄劫缠身, 探灵+1, 势如破竹+1, 天机·逆施, 踏破九霄, 磅礴之势, 浩然正气, 诸事不宜** = 100% first (0% second). Full-log WIN t10: 内伤 clock ticks 4→5/turn ignoring his 辟邪/防; 天机·逆施 converts 磅礴之势(20def→+10dmg) + 浩然正气(4def→+2) + 诸事不宜(4def→+2) into damage. Killed him at exactly t10.
- The two DIFFERENCES vs my real board: swap 饿虎扑食+1 -> 天机·逆施; swap 起势+1 -> 浩然正气. 天机·逆施 was IN MY HAND.

MECHANICS VERIFIED (engine):
- **辟邪(hexproof) absorbs debuff application**: gamestate_full.js:4251 `to_sub = min(amt, hexproof)`. So 牧逸风's 辟邪阵纹 lead eats 厄劫缠身's 4 内伤 → only 1 applied (R20 log). R18 vs him I landed 4 内伤 (he had no 辟邪 up t1) and the clock killed him t15.
- **厄劫缠身 [开局] downgrades opponent's SAME-SLOT card 1 level** (R18: downgraded his 聚灵心法; R20: downgraded his 辟邪阵纹 — poor target). Card cycling re-applies base 4 内伤 each loop.
- 天机·逆施 (career7 境5): [灵气]+2 | 加[防]或生命时向对方造成50%伤害, 持续3回合 | [转换]. THIS is the damage engine — my deck gains LOADS of def (磅礴/诸事不宜/浩然正气/荷重), each converted to dmg.

PER-RIVAL (this game):
- pid0 牧逸风 (云剑/qi-ramp 巨灵剑): W R4,R6,R7,R9,R16,R17,R18; L R5,R11,R13,R19,R20. His kill = 万法归灵剑 (耗尽灵气 +6dmg/qi: 44 dmg at qi7) + 巨鹏→巨鲲 chase chain. Beat him when I had 内伤 clock online (R18 win t15) or 诸事不宜 wall; lost when I fielded slow boards or he had 辟邪 up.
- pid2 吾行之 (金灵): W R14; L R10. Dead before endgame.
- pid1 谭舒雁 (命理师 内伤): W R16; L R2,R3,R12,R15. She WON the game (命63) — same as g13. Her 内伤 board is still my structural nemesis.

ECONOMY: broke 境2@R3, 境3@R6, 境4@R9, 境5@R13. ROLL AUDIT: R7 spent 14 rolls -> all junk (天命·飞逝/罗刹扑/风冥爪/探马掌), got nothing durable. R11 13 rolls -> junk. R13 20 rolls -> junk except 势如破竹. R17 12 rolls -> junk (gutted good cards). **THE FATAL PATTERN: I burned 60+ rolls R7-R17 and NEVER found 天机·逆施/浩然正气/血光之灾 as fieldable pieces — but 天机·逆施 LITERALLY arrived in my R19 deal and I never fielded it.** R19 banked 21, R20 banked 20 = ~41 wasted exchanges (grants capped). Should have been rolling HARD R18-R20 hunting 天机·逆施/浩然正气/厄劫缠身-upgrade.

SURPRISE: A single card (天机·逆施) was the difference between my R20 board (loses to his real board) and a 100%-first winner. It was sitting in my hand. Lesson: **review HAND every round for win-con cards, not just board.**

==== LEDGER ENTRY · Game 15 ====
## Game 15 (小布 sect4 崩拳, pid3) — RESULT: 1st PLACE, WINNER, 命69. 
R1-R6 rough (1W/5L, dropped to ~69命) then a dominant 10-round win streak R7-R17 sealed it.

SIDEJOB: 7 (命理师). FATES: 磨砺不止, 锻体不息, 炼体传承, 体修入道, 再生之躯 (境2@R3, 境3@R6, 境4@R9, 境5@R12 — broke every gate ASAP).
FINAL BOARD (R17): 血光之灾, 天星·御心, 修罗吼, 气若悬河, 踏破九霄, 崩拳·降龙+1, 崩拳·封+1, 夜鬼啸  (all lv1 except the two 崩拳).
修为 87, 境5, maxHP 107-135, 体魄 28, 8 slots.

=== WINNING ENGINE (THE discovery of this game) ===
**内伤-clock overlay on a 崩拳/气势/身法 burst skeleton** — and it DOUBLE-DIPS:
- 血光之灾 = [开局]+1内伤, then the base card re-applies 1内伤 each cycle.
- 天星·御心 (right after 血光) RETRIGGERS 血光's [开局] TWICE → 3 injury applications in 2 turns. ([防]+4, 生命+4 too).
- 修罗吼 = 双方各加4内伤 AND "+1 灵气 and +1 生命 for each 2 stacks of [Debuff] YOU have". So the injury I take
  from 血光/修罗吼 becomes qi+hp for ME → **the clock pays for itself.** It gave me +8qi/+8hp in the R17 log.
- 气若悬河 (气势+1, qi+2, next 2 attacks +1气势) → 踏破九霄 (气势+3 身法+6) → chase. Then 崩拳·降龙→崩拳·封 chain
  (降龙 gives next 崩拳 +7def/+7atk) → 夜鬼啸 (14atk IGNORE-DEF) as the finisher.
This board won 11 of my last 11 fights. Damage source split (R12): 内伤 clock ~60% + 崩拳 burst ~30% + 夜鬼啸 ~10%.

=== PER-RIVAL (final) ===
- pid0 牧逸风 (云剑/巨灵剑 qi-ramp): W R7,R11,R13,R15,R17; L R1,R3,R5 (early). His kill card = 万法归灵剑(+6dmg/qi) + 巨鹏→巨鲲 chase.
  My 内伤 clock + 夜鬼啸 ignore-def beats his 防/辟邪 wall. R17 win t8 (-23): injury 8-16/turn did most of it.
- pid2 吾行之 (五灵/水灵): W R2,R9,R14,R16; L R4,R6. Water spirit 波澜/汹涌 ramps; I out-burst early-mid. Easiest rival.
- pid1 谭舒雁 (命理师/内伤 clock): W R8,R10,R12; L R3,R5 (early). SHE WAS DEAD by R17 (命0). R12 win t14 (-19) — my clock
  out-ticked hers because 修罗吼 converts my injury→qi/hp. THIS IS THE MATCHUP THE WHOLE GAME HINGED ON.

=== ROLL/Economy AUDIT ===
Rolls/round: 0,2,0,0,4,6,8,5,6,4,0,8,6,4,4,6,2. Total ~63. Bank ended 8 at R17 (under-spent late — C6/M8 still violated).
KEY MISS: **R16 I was dealt/rolled a 2nd 夜鬼啸 and ROLLED IT INTO 起势→修罗吼→崩拳·缠→卜命 (junk).** I merged 崩拳·封 to +1
  instead. sim-verified: 夜鬼啸 lv1→lv2 flips pid1 from **0%→100%** going first (5 reps), and makes the pid0 board win BOTH seats.
  That single merge (a 2-identical-copies merge, fully reachable — I HELD both copies) was the biggest unforced error.
- R7 spent 8 → junk (天命·飞逝/探马掌/风冥爪/迎风掌). R13 spent 6 → mostly junk. Pattern: mid-round shotgun rolls yield junk.

=== TOP DISCOVERY (with evidence) ===
1. **内伤-clock + 修罗吼 self-conversion = a self-sustaining clock vs 命理师.** New: 修罗吼's "+qi/+hp per 2 debuff" turns
   the injury you'd take anyway into economy. Evidence: R12 14-turn win vs 谭舒雁; R17 8-turn win vs 牧逸风.
2. **同心曲 (琴师3, 境4) is the SPECIFIC counter that beats 谭舒雁 even SECOND seat.**
   sim-verified both-seat winner vs her: [血光之灾, 修罗吼, 天命·飞逝, 气若悬河, 踏破九霄, 崩拳·降龙+2, 同心曲, 夜鬼啸+1]
   = 100% first / 100% second. 同心曲 "apply all MY debuffs to the opponent" dumps my injury onto her.
   BUT the same board drops to 0% vs pid2 → it's a TARGETED tech swap, not a general upgrade.
3. **Seat (修为) is decisive**: my board is 100% first-seat vs pid0/pid2 and 0% second-seat. I won the game by
   out-修为-ing everyone (87 vs 74/75/76 at R17) and acting first in nearly every late fight.

=== SURPRISES ===
- 谭舒雁's 流水无情 (m_ruthless_water_stacks) CONVERTS any non-内伤 debuff I apply into 内伤 ON ME (x stacks).
  So 夜鬼啸's 虚弱 self-debuff is a liability vs her — but its raw 18 ignore-def dmg at +1 finishes the kill first.
- I never fielded 天机·逆施 this game (my g14 win-con) — the 内伤 hybrid simply outperformed it. Good sign: multiple viable archetypes.
- Fates changed NOTHING in any sim (fate 1/3/5 identical 13-turn loss vs her base). Confirms prior notebook.
- I WON with an objectively non-optimal final board (0% vs her base per matrix) purely on seat + everyone else dying.
  The marginal upgrade (夜鬼啸+1) was in my hand.

==== LEDGER ENTRY · Game 16 ====
g17 R11 (小布, sidejob7, 境4 修为46→47): beat 吾行之/pid2 (五灵/水灵 ramp).
KEY DISCOVERY — 双鬼拍门 is the anti-mitigation/anti-sustain key vs 五灵 water-ramp:
- Opp's deck = 水灵阵+1 qi ramp + 潜遁 (40% dmg mitigation, 2turns) + 水势-scaling 涛/汹涌 + 金灵·穿心 (ignore-def) finisher. My pure 崩拳 burst boards ALL lost 0% (he out-sustains + mitigates through turn 8-9, finishing me with 穿心).
- WINNING BOARD (100% fore, 0% aft — I go first 修为46>42): [双鬼拍门, 气若悬河, 锻骨, 势如破竹, 崩拳·突+1, 崩拳·连崩, 崩拳·封+1, 劈山掌+1]
  - 双鬼拍门 (双方各+1内伤+1外伤, 6atk×2): the 内伤 clock ticks him through ALL 防/mitigation, and 外伤 amplifies. This is what finally converted my near-losses.
  - 锻骨 = the SURVIVAL key: raises my maxHP to 102 (vs his 95) via in-battle 体魄, giving me the 1-2 extra turns needed for the 内伤 clock to finish him. Removed 锻骨 → lost; added it → won. HP buffer > 防 (his 穿心 ignores 防).
  - Without 双鬼拍门 (pure burst): lost by ~5 HP. Without 锻骨 (double鬼+burst): 双鬼 got him to 1 HP but I died.
- Board alone was NOT enough for going-second; the win is seat-dependent. My decisive 修为 lead (46 vs 42) made first-seat reliable.
- Economy: rolled 罗刹扑→万事如意, 察体→磅礴之势, 凶象→夜鬼啸, 天星·御心→卜命, 卜命→双鬼拍门, 夜鬼啸→崩拳·撼, 崩拳·撼→踏破九霄, 察体→踏破九霄; merged 2×踏破九霄 → 修为47. Ended banked 12 (≤21, good).
- 夜鬼啸 (ignore-def, self+3虚弱) AGAIN proved a trap in short fights AND cost 1qi it couldn't pay → "gained qi instead of playing." Avoid unless qi engine is robust.
- LESSON: vs a mitigation/sustain wall, the answer is a DAMAGE-OVER-TIME clock (内伤 via 双鬼拍门/血光之灾) + an HP buffer (锻骨), NOT more burst. Bookmark 双鬼拍门 as a strong pickup for 崩拳 decks.

==== LEDGER ENTRY · Game 16 ====
## Game 16 (小布 sect4 崩拳/气势, pid3) — RESULT: **NOT 1st** (2nd, 命 0). Winner = 牧逸风 (pid0, 万法 qi-nuke), 命40.
Record: L R1,R2,R3,R4 (dropped to ~30命) → W R5-R14 (10 straight) → L R15,R16,R17,R18 (all to pid0/pid1) → W R18(vs pid1) → L R19(vs pid0). 命 hit 0 at R19.

SIDEJOB: 7 (命理师). FATES: 磨砺不止, 锻体不息, 炼体传承, 气势充沛, 稳固根基. Gates broke on TIME not dump (境2 R3, 境3 R6, 境4 R9, 境5 R12). Ended 修为96 境5 maxHP126.

FINAL BOARD (R19, what I fielded — THE MISTAKE): [探灵, 气若悬河, 冲霄破浪, 势如破竹, 威震四方, 踏破九霄, 崩拳·寸劲, 磅礴之势+1]
  → 4/8 slots dealt ZERO damage (探灵/气若悬河/冲霄破浪/威震四方/踏破九霄 = pure setup). Only 势如破竹(10), 崩拳·寸劲(10+), 磅礴之势 dump hit. Damage/turn ~30 vs 110+ HP pools.
  card_stats R19: 探灵 0dmg, 气若悬河 0dmg, 冲霄破浪 0dmg, 威震四方 0dmg, 踏破九霄 0dmg, 崩拳·寸劲 24dmg, 磅礴之势 28dmg.

*** TOP DISCOVERY (sim-verified, 5 reps) — MY CORRECT R19 BOARD ***
  `[气若悬河, 冲霄破浪, 威震四方, 势如破竹, 踏破九霄, 朝气蓬勃, 磅礴之势+1, 崩拳·降龙]`
  = 100% FIRST / 100% SECOND vs 牧逸风's real R19 board (survives his t7 万法 nuke at ~15hp, wins t9-10).
  = 100% both vs 吾行之.
  = 100% first / 0% second vs 谭舒雁; swap slot4 势如破竹→天谕·守 → 100% BOTH vs her base.
  FIX vs my fielded board: (1) 崩拳·寸劲→朝气蓬勃 (6+force atk, and lets 磅礴 dump), (2) ORDER: 势如破竹 EARLY, 磅礴之势+1 BEFORE 崩拳·降龙 (dump force→40def+40dmg, then finisher chases). Original had 寸劲 + 磅礴 last-ish.
  WHY IT WINS: 踏破九霄(+6agi) triggers the ≥10-身法 AUTO-CHASE each turn = free extra card. 威震四方 cap 6→9. 磅礴之势 dumps cap-9 force into 36-40 def (survive 万法) + 27-40 dmg.

*** #1 LESSON — ROLL WITH A NAMED MERGE TARGET, NOT SHOTGUN. ***
  My economy: rolls/round = 0,0,0,0,0,2,0,0,4,4,3,4,4,6,17,0,19,16,3 (~82 total). R15/R17/R18 = 17/19/16 rolls ALL JUNK (hunting nothing specific, found nothing). I lost ~50 exchanges to junk.
  牧逸风 by contrast: R19 rolled 15× hunting the 万法归灵剑 MERGE → lv1→lv2 → 80dmg nuke → killed me 68→-12 in the FINAL round. He KNEW his target (his CP10) and put EVERY roll there.
  FIX: by R13+ pick ONE attainable merge target (崩塌卡 or a lv2 upgrade of a load-bearing card), and ONLY roll toward it. If no target is attainable, STOP and absorb to 修为 instead.

*** SEAT/修为 IS DECISIVE — and 牧逸风 out-修为'd me at the end (97 vs my 96). ***
  I was 96 at R19 start but he absorbed +4 to 97 and took FIRST seat R19. He then built his qi bank unopposed and nuked t7.
  R17/R18 I lost the seat vs pid1 (she went first) → my slow clock lost. My board vs pid1/pid0 is FIRST-SEAT-only in several configs.
  FIX: (already in playbook C5) at R15+ with 命 high, ABSORB everything into 修为 to secure the seat.

*** 牧逸风 COUNTER-NOTE (from his own playbook, open-review): CP10 = 万法 LEVEL-UP is the decisive lever (lv2 80dmg vs lv1 30dmg through def). CP11: vs my pure-气势 board he SWAPS 辟邪 for 云剑·游龙 to pull qi forward a turn. He simmed my board at 0% in his notes (g20) but my reordered board now flips it — HIS notes are now stale, mine are current.

*** WHAT SURPRISED ME: my 命 survived to R19 (better than g15's early win) but I NEVER fielded my g15-winning 内伤 hybrid (血光+天星·御心+修罗吼). That board now sims 0% vs his evolved board — so the hybrid is OBSOLETE vs pid0's mature deck. The correct answer vs pid0 is a 气势 DUMP board (磅礴之势) that both survives the nuke with def AND out-damages him after.

ECONOMY NUMBERS: banked-end sequence 3,7,10,14,17,18,21,24,21,21,22,21,21,19,11,20,10,3,7. Rolled ~82 exchanges; ~50 wasted on 3 shotgun rounds (R15/17/18). Don't repeat.

==== LEDGER ENTRY · Game 17 ====
## Game 17 (小布 sect4 崩拳/气势, pid3) — RESULT: NOT 1st (runner-up, 命 0 at R20). Winner = 谭舒雁 (pid1, 命理师/内伤, 命1). Lobby: pid0 牧逸风 云剑 (died), pid2 吾行之 水灵 (died).
Record: W R1,R2,R3 → L R4,R5 → W R6,R7,R8,R9,R10,R11,R12,R13 → L R14 → W R15(×2),R16,R18 → L R17,R19,R20. 命 bled to 0 only at the final R20.

SIDEJOB: 5 (阵法师). FATES: 磨砺不止, 再生之躯, 崩拳传承, 生机不灭, 筋骨健壮. Gates 境2@R3/境3@R6/境4@R9/境5@R13 (time-based, not dumped). Ended 修为104 境5 maxHP~117-164 (in-battle).

FINAL BOARD (R20 fielded — THE MISTAKE): [气若悬河, 冲霄破浪, 威震四方, 踏破九霄, 鹤步, 朝气蓬勃+1, 崩拳·寸劲, 磅礴之势+1]. vs 谭舒雁: wins FIRST seat by ~5 HP (coin flip), LOSES second seat. I went first yet lost the real match (variance + her 杯弓蛇影+1 doubled by 梅开二度 = 23 dmg instant).

*** TOP DISCOVERY (search_board + sim_matchup, 5-7 reps) — 天地浩荡 IS THE MISSING TEMPO CARD. ***
`[气若悬河, 冲霄破浪, 鹤步, 威震四方, 踏破九霄, 天地浩荡, 崩拳·寸劲+1, 磅礴之势+1]`
= 100% FIRST / 100% SECOND vs 谭舒雁 base AND +1 (~9t, I end at 47/164).
= 100%/100% vs 牧逸风 base AND +1.
= 100%/100% vs 吾行之 base AND +1.
A board that beats EVERYONE both seats, fully upgraded, at 47 HP to spare. THIS WON THE LOBBY.
WHY 天地浩荡 (lv1: 10atk, HP+4, 身法+4 AND +2 more per REMAINING 气势): with ~10 force it grants ~24 agi, refueling the ≥10-身法 AUTO-CHASE for 2+ turns → ~2 cards/turn sustained. It is simultaneously (a) damage (10atk, which my R20 board lacked early), (b) HP buffer (+4, beats her 内伤 clock race), (c) TEMPO (feeds the chase engine). 鹤步 (only agi from physique, cap 10) is strictly worse in this slot.

*** #1 ROOT CAUSE — I WAS DEALT 天地浩荡 at R14 AND ROLLED IT AWAY (天地浩荡→冲霄破浪). ***
economy_history R14 confirms it. SAME M22 failure mode as g15/g16: I held the winning piece and didn't recognize it. FIX: add 天地浩荡 to the DO-NOT-ROLL list; when dealt 天地浩荡, treat it as a core card (it slots into the 气势/chase skeleton at the 鹤步/朝气蓬勃 position).

*** #2 ROOT CAUSE — SHOTGUN ROLLS AT R20: 25 rolls ALL JUNK (hunting 崩拳·降龙, found 鹤步×2/修罗吼×3/须弥阵纹...). ***
R14=8 junk, R16=8 junk, R13=8 junk, R11=17 junk, R7=16 junk. I banked to 25 at R19 then wasted the grant. FIX (M18 again): from R13+ name ONE target or stop and absorb to 修为.

PER-RIVAL CAUSES:
- pid1 谭舒雁 (WINNER, 内伤 clock): beat me R17 (-24), R19 (-28), R20 (-20, FINAL). Her clock: 天星·牵引 triggers 血光[开局], 天星·御心 retriggers it ×2, 梅开二度 doubles 杯弓蛇影+1 (3 内伤 + force all enemy 内伤 to tick NOW = 23 dmg swing). Her damage ALL ignores my 防 (内伤) → my 32-def 磅礴 dump was USELESS defensively. The race: she kills t10-11; my R20 board kills t9-11 → coin flip; the 天地浩荡 board kills t9 with 47 HP spare → decisive.
- pid0 牧逸风 云剑/万法: lost R4 early; beat R8,R11,R13 (and would beat him 100% both seats with the 天地浩荡 board).
- pid2 吾行之 水灵 healer: I actually WON most (R5,R9,R15,R16,R18). His OWN notebook says his CORRECT-ORDER board beats me 100%/100% — I was lucky. The 天地浩荡 board beats his real board 100%/100% too.

ECONOMY: rolls/round = 0,0,0,0,0,0,16,0,0,3,17,0,8,8,0,8,0,2,4,25 (~91 total). ~50 wasted on junk (R7/R11/R20). Bank-end: 3,6,9,12,16,19,6,9,12,13,0,4,2,2,8,6,16,20,25,3.
- KEY CONTRAST 谭舒雁: R9 = 17 rolls that landed her ENTIRE engine (牵引+御心+血光+流水) — a TARGETED dump at the right phase (境4 pool unlocked). Then 6-roll targeted rounds. She hit 修为110 (won seats late).
- LESSON: dump big at the ROUND A KEY CARD'S PHASE UNLOCKS (R9@境4 for support engine, R13+@境5 for finishers), with NAMED targets; never shotgun.

SURPRISES:
1. 天地浩荡 (+agi per remaining 气势) — a 10atk/HP+/tempo card I'd never valued. It's a CORE card for the 气势-chase deck.
2. Her 内伤 clock makes ALL my 防 worthless; the answer is HP buffer + tempo, not def.
3. 3rd+ game where I had the winning card in hand/draw and rolled/absorbed it. Recognition of core cards > board theory.
4. Fates again combat-irrelevant (A/B [1] vs [3] identical 28-命 win, 9t).

==== LEDGER ENTRY · Game 18 ====
# Game 18 (小布 sect4 崩拳/气势/体魄, pid3) — RESULT: **1st PLACE (WINNER), 命 20**. 
Lobby: pid0 牧逸风 云剑(命1, survived to R17), pid1 谭舒雁 命理(dead), pid2 吾行之 水灵(dead).
Record: L R1(vs pid1) → W R2,R3 → L R4,R5? → ... → L R8,R9,R10,R11,R12 (命 bled to ~72) → W R13,R14,R15,R16(×2),R17. 
命 never fell below ~20 after mid-game; rode the wins home. Final battle R17 vs pid0 = -27命 kill.

SIDEJOB: 5 (阵法师). FATES: 磨砺不止, 再生之躯, 体修入道, 生机不灭, 气势充沛 (all passed, but combat-irrelevant again — 6th confirmation).
Gates on TIME: 境2@R3, 境3@R5, 境4@R9, 境5@R13. Ended 修为84 境5 maxHP~141 (体魄33→141 HP in battle).

FINAL BOARD (R17 fielded — THE WINNER): ['气若悬河+1','冲霄破浪','踏破九霄+1','势如破竹+1','崩拳·降龙+1','崩拳·寸劲+1','朝气蓬勃+1','崩拳·突']
  NO 天地浩荡 (never drawn this game), NO 威震四方/鹤步. The BURST 崩拳 skeleton alone won the lobby.

*** TOP DISCOVERY (sim-verified ~5-10 reps) — THE BURST BOARD IS A LOBBY-WINNER WITHOUT 天地浩荡. ***
  My fielded board: 100%/100% vs 牧逸风 base AND +1 (5t); 100%/100% vs 吾行之 base AND +1; 
  100%/100% vs 谭舒雁 base; ~coin-flip (0-100% across reps) vs her FULLY +1 SECOND seat.
  → the g17 notebook's "天地浩荡 board = 100% vs EVERYONE" is STALE (M14 again): re-sim TODAY, both boards
    are equal vs 谭舒雁 base, and my burst board is FASTER vs 牧逸风 (5-6t vs 9t).
  → 崩拳·寸劲+1 (2×force) + 崩拳·降龙+1 (pre-buff) + 磅礴/朝气 dumps = lethal t5-6. Order: 气若悬河(+qi,+force)
    → 冲霄破浪(force=qi, +5agi) → 踏破九霄(+4force,+6agi → 11 agi = AUTO-CHASE) → [chase 势如破竹: 3 qi→3 force, +9atk]
    → 崩拳·降龙+1 (pre-buff next 崩拳 +7atk/+7def) → 崩拳·寸劲+1 (14 + 2×8force = ~44-58 dmg) → 朝气蓬勃(+force dump) → 崩拳·突.

*** REACHABILITY-VERIFIED near-fix ***
  崩拳·降龙+2 (lv3 = FOUR lv1 copies) would flip 谭舒雁 full-+1 SECOND seat from 0%→100% (search_board, 3 reps).
  NOT REACHABLE: I drew only 2 降龙 lv1 copies total (merged to +1). Filed as "next time: if you see 3+ 降龙, hunt the 4th".

*** #1 ECONOMY WIN — MY ABSORB-EVERYTHING + 2 TARGETED MEGA-DUMPS IS NOW THE LOBBY BENCHMARK. ***
  rolls/round = 0,0,0,0,15,0,4,4,0,0,18,6,0,0,1,0,10 (~58 total). TARGETED dumps: R5=15 (landed 势如破竹 only — junk),
  R11=18 (landed 气若悬河+崩拳·降龙 — keepers), R17=10 (landed 磅礴之势+崩拳·寸劲+1 merge).
  Ended 修为84 = WON every seat race vs 牧逸风(67)/谭舒雁(77)/吾行之(70). 
  BOTH rivals' notebooks now cite ME: 吾行之 CP1b "小布 hits 84 by absorbing EVERYTHING", 牧逸风 CP3 "seat decides".
  牧逸风 HUNTED 万法 (17+15+8+8+8+6+4 shotgun rolls, never drew it) → 修为 67, lost the seat, lost R17.

*** ECONOMY MISTAKES THIS GAME ***
  R5: 15 rolls, landed ONLY 势如破竹 (rest junk) = a mild shotgun. R16 banked to 25 → R17 grant WASTED (+6 lost).
  FIX: schedule to land ≤21 before R16; and give R5 a NAMED target (崩拳·寸劲 or 势如破竹), not "hunt for anything".

*** PER-RIVAL CAUSES ***
  pid0 牧逸风 (云剑/万法): I beat him R16,R17 (kills). He never drew 万法 lv2 (4th straight game) → his CP15
    ("finisher must exceed 小布's 138 HP") was never met. My 崩拳·寸劲+1 (47-58 dmg) outraced his 巨鲲/白鹭 chip.
  pid1 谭舒雁 (命理/内伤 clock): beat me mid (R8/R11/R12 — my engine wasn't online yet) but I beat her R13,R15,R16.
    Her 厄劫缠身 (her CP2 win-con) never drawn (6th straight). Her 内伤 clock (~11 stacks by t6) is real but my
    141-HP / t5-6 kill outraced it once the chase engine was up.
  pid2 吾行之 (水灵 healer): 100%/100% both seats; his own notebook's "winning board" claim (不动金刚阵 vs my burst)
    is STALE vs my fielded board — I went 100% vs his real R17 board.

*** SURPRISES ***
  1. 天地浩荡 — a card I've written into 2 notebooks as CORE — was NEVER DRAWN and I still won the lobby. Its
     value is real but the burst 崩拳 skeleton is self-sufficient.
  2. 抱气法 = +2 体魄 (+HP). I ABSORBED 抱气法 at R2 and R13. Given 体魄→HP scaling is my KEY survival axis,
     fielding 抱气法 EARLY to ramp 体魄 may beat absorbing it. HYPOTHESIS to test next game (not yet verified).
  3. Both rivals' notebooks already model MY engine in detail (吾行之 CP1f: 不动金刚阵 = anti-burst; 谭舒雁: clock+burst
     races my t5). They are reading my notes. My board must keep evolving.

SIDEJOB READ: 5 (阵法师) is fine; nothing beat it. 不动金刚阵 (the anti-burst card my rivals use against ME) exists
  in career-5 pool — consider teching it if a burst rival appears.

==== LEDGER ENTRY · Game 19 ====
## Game 19 (g19) — 小布 (sect4 崩拳/气势/体魄, pid3).
# RESULT: NOT 1st (命 0, OUT). Winner = 吾行之 (pid2, 五行/水灵+阵法师 drain board), 命31.
# Lobby: pid0 牧逸风 云剑 (DEAD 命0), pid1 谭舒雁 命理/内伤 (DEAD 命0), pid2 吾行之 水灵 (WINNER).
# Record: L R1(pid2) W R2(pid1) W R3(pid2) L R4(pid0) L R5(pid1) W R6(pid0) L R7(pid1) W R8(pid2)
#         L R9(pid1) W R10(pid0) W R11(pid1) W R12(pid0) L R13(pid2) L R14(pid2) L R15(pid2) W R16(pid2) L R17(pid2).
#   The whole late game was 吾行之 beating me 4 of 5 (R13,R14,R15,R17). He was the wall, not 谭舒雁 this time.
# SIDEJOB: 5 (阵法师). FATES: 磨砺不止, 再生之躯, 崩拳传承, 生机不灭, 云巅雷劫 (combat-irrelevant, 7th confirmation).
# Gates on TIME: 境2@R3, 境3@R5, 境4@R9, 境5@R12. Ended 修为90 境5 maxHP~111-128 (体魄16).

## FINAL BOARD (R17 fielded — THE MISTAKE):
# ['崩灭心法','冲霄破浪','踏破九霄+2','势如破竹+1','崩拳·降龙+1','崩拳·寸劲+1','崩拳·连崩+1','崩拳·突']
#   → vs 吾行之 FINAL board: 100% base, but 0% BOTH seats vs his +1 board. (He upgraded; I beat only his base.)

### ★★★ TOP DISCOVERY (g19) — MY FORCE WAS CAPPED AT 6; 威震四方 IS THE FIX. ★★★
#   崩拳·寸劲+1 did only 37 dmg (not 44-58) and 连崩+1 only 26. ROOT CAUSE: 气势 default cap = 6. My generators
#   (踏破9+2=+5, 冲霄+qi→force, 势如破竹+3, 崩灭) produce 8-9 force/turn → EVERY point above 6 is WASTED.
#   FIX = 威震四方l1 ([防]+8, 气势上限+3, 气势+3): raises cap 6→9 AND adds force AND def.
#   VERIFIED (search_board + sim_matchup, 5-10 reps, both seats, base AND +1):
#     ['威震四方','冲霄破浪','踏破九霄+2','势如破竹+1','崩拳·降龙+1','崩拳·寸劲+1','崩拳·连崩+1','崩拳·突']
#       vs 吾行之: 100%/100% base; 100% first / ~50-100% second vs his +1 board. (寸劲 now lands 50 dmg, 连崩 35.)
#       vs 牧逸风: 100%/100% base AND +1.   vs 谭舒雁: 100%/100% base; 100%/60% vs +1.
#   → A board that beats EVERYONE both seats where my R17 board was 0% vs 吾行之 +1. SWAP: 崩灭心法 → 威震四方.
#   REACHABILITY: 威震四方 = 6 copies in pool (2.8%/roll) — I NEVER drew it in ~65 rolls (bad luck / no named target).
#   ENGINE SOURCE (gamestate_full.js:4565-4573): 气势 spent 1/attack, capped at max_force; 寸劲 doubles the force
#     term (force*=2). Force above cap is DISCARDED. So force-cap is a direct damage multiplier. HP_COST: dmg -= decrease_atk.

### ★★★ THE #1 ROOT CAUSE — I NEVER UNDERSTOOD THE FORCE CAP. 7 GAMES OF 气势 WITHOUT 威震四方. ★★★
#   Every g15-g19 气势 board overflowed its cap. 威震四方 was in my pool every game (6 copies) and I never filed it.
#   This single card is worth ~13 dmg on the 寸劲 finisher (37→50) and swings the 吾行之 matchup.

### ★★★ #2 ROOT CAUSE — 吾行之'S 万花迷魂阵 + 回响阵纹 DRAIN BEAT ME 4 TIMES. ★★★
#   His engine: 万花迷魂阵 [持续]: turn-end +1 减攻 to me, then drains 1HP per 减攻 stack (BYPASSES 防), heals him same;
#   回响阵纹 (slot2) RETRIGGERS slot-1 万花 (upgraded +1 lv) → 2 drain events/turn. 不动金刚阵 = +7防+7maxHP/heal/turn
#   over 3 turns (anti-burst tank). By t9 he had ~7 减攻 stacks = 7+ drain/turn PLUS -7 flat on all my attacks.
#   [减攻] is the direct counter to 气势/force scaling (subtracts FLAT dmg per attack — gamestate_full.js:4572).
#   ANSWER (verified): 威震四方 board races him to a t6 kill (he needs t9-10 for the drain snowball). Kill BEFORE it ramps.
#   ⚠辟邪阵纹/浩然正气 CAN blank 减攻 application (gamestate_full.js:4251-4257: debuff amt reduced by hexproof) BUT
#     万花 strips 2 hexproof/turn → only DELAYS. Tried 辟邪-instead-of-气若悬河: 0% (slower). RACING > blanking here.

### ★3RD ROOT CAUSE — ECONOMY REPEATED BOTH g18 FLAGS. ★
#   rolls/round: R1-4=0, R5=11, R6-8=0/0/2, R9=6, R10=8, R11=0, R12=8, R13=0, R14=0, R15=5, R16=0, R17=25 (~65 total).
#   R17 = 25-roll SHOTGUN (hunting 踏破/降龙 merges, landed some but wasted ~15). R5=11 (landed only 朝气蓬勃).
#   BANKED TO 26 AT R14 → the R15 +4 grant was WASTED (M24, 3rd straight game!). Ended 修为90 — actually BEAT all
#   rivals (吾行之 76, 谭舒雁 82, 牧逸风 58) → I won every seat race and STILL lost (board-quality loss, not seat).
#   FIX: (a) NAME a roll target EVERY dump (威震四方 the moment 境5 unlocks!); (b) land ≤21 before R14 grant.

### PER-RIVAL CAUSE:
# - pid2 吾行之 (WINNER, 万花/drain tank): beat me R13,R14,R15,R17 with the drain+减攻 snowball. His own notebook
#   (STRATEGY v514) is a 100%-win universal board vs all three of us. He IDENTIFIED me as "THE WALL 4 games" and
#   BUILT the counter (万花/回响 drain + 不动金刚阵). He won the matchup-war. My only answer = out-race at t6 (威震四方 board).
# - pid1 谭舒雁 (命理/内伤): beat me R1,R5,R7,R9 mid-game; I beat her R2,R11. 威震四方 board = 100% vs her both seats except +1 second (60%).
# - pid0 牧逸风 (云剑/万法): beat me R4 only early; I beat him R6,R10,R12. 威震四方 board = 100%/100% vs base AND +1.

### SURPRISES:
# 1. 气势 has a HARD CAP (6) that I'd been silently overflowing for 7 games. 威震四方 is the key I never filed.
# 2. 吾行之 built a purpose-made counter to my burst and it WORKED — rivals adapt faster than I re-verify.
# 3. [减攻] subtracts FLAT dmg from EVERY attack (4572) — devastating vs force-scaling; 辟邪 delays but 万花 re-applies.
# 4. 修为 90 (best in lobby) still lost — board quality > seat economy once everyone is at 境5.

==== LEDGER ENTRY · Game 20 ====
## Game 20 (小布 sect4 崩拳/气势/体魄, pid3) — RESULT: **1st PLACE / WINNER, 命 49**.
Lobby: pid0 牧逸风 云剑 (DEAD 命0), pid1 谭舒雁 命理/内伤 (DEAD 命0), pid2 吾行之 水灵 (DEAD 命0).
Record: W R1(pid2) L R2(pid0) L R3(pid1) W R4(pid0) W R5(pid1) W R6(pid2) W R7(pid1) W R8(pid2) W R9(pid0)
        L R10(pid2) L R11(pid0) L R12(pid1) W R13(pid2) W R14(pid0) W R15(pid2) W R16(pid1) W R16(pid0)
        W R17(pid1) W R18(pid1, FINAL vs 谭舒雁). 命 never below ~49 in the last third.

SIDEJOB: 5 (阵法师). FATES: 磨砺不止, 体修入道, 再生之躯, 生机不灭, 储纳灵气 — 8th confirmation combat-irrelevant
  (simulate A/B [0] vs [4] identical 6t win). Gates: 境2@R3, 境3@R6, 境4@R9, 境5@R13. Ended 修为92 境5 体魄32.

FINAL BOARD (R18 fielded, 7 slots): ['崩拳·缠+1','踏破九霄','冲霄破浪','崩拳·寸劲','势如破竹+1','崩拳·连崩','崩拳·戳+1']
  Beat 谭舒雁's fielded R18 board 100%/100% (~6t). R18 real battle was razor-thin: won at 3 HP vs her -2 (7t).

*** TOP DISCOVERY — I WON THE LOBBY *BECAUSE 谭舒雁 FIELDED THE WRONG BOARD*. HER OWN NOTEBOOK HAS THE COUNTER. ***
  Her notebook C6 recipe ['天星·牵引','血光之灾','天星·御心','诸事不宜','落花有意','梅开二度','杯弓蛇影+2','流水无情']
  BEATS my exact final board 0%/0% (I LOSE both seats, confirm 3 reps each). The load-bearing card is 诸事不宜
  (−6 atk to my next 2 hits, source gamestate_full.js:2939/4471). Remove it → she loses.
  ★ Her economy_history shows she was DEALT 诸事不宜 at R9, then ROLLED IT AWAY at R10 (诸事不宜→枯木逢春). ★
  Then at R18 she panic-rolled 25×, merged her two 杯弓+1 into +2, took back her own 血光/落花 → 6-card board.
  Her notebook C8 explicitly warns against this. She made the SAME mistake I made in g17 (rolled away 天地浩荡, M22).
  → THE LOBBY WAS DECIDED BY WHO *DIDN'T* SELF-SABOTAGE. I fielded my best available skeleton and froze it.

*** #1 VERIFIED FIX — THE 威震四方 BOARD IS A UNIVERSAL WINNER (beats all 3 rivals, both seats, base AND +1). ***
  ['威震四方','冲霄破浪','踏破九霄','势如破竹+1','崩拳·降龙+1','崩拳·寸劲+1','崩拳·连崩+1','崩拳·突']
  sim_matchup (5 reps): vs pid1 100%/100% base AND +1 (note: sim_matchup uses her FIELDED board).
  vs 谭舒雁 OPTIMAL C6 board (explicit opp_cards): 100% first / 100% second, ~7t, ends 61/142 HP. 4/4 reps WON.
  vs pid2 吾行之 tank: 100%/100% base; 100%/100% +1 (~7-11t). vs pid0: 100%/100% base+1 (~6t).
  WHY: 威震四方 raises 气势 cap 6→9 (verified: max_force=6 default, gamestate_full.js:311; +3 card_actions.js:5659).
  With cap 9, 寸劲/连崩/势如破竹 land 35-50 dmg instead of 21-34 → kills the clock/counter BEFORE it ramps.
  → MY FIELDED BOARD WAS 0%/0% VS HER OPTIMAL BOARD; THE 威震四方 BOARD IS 100%/100%. I HAD 威震四方 IN MY POOL
    (6 copies, 1.8%/roll) AND NEVER DREW IT. THIS IS THE SAME g19 LESSON, UNAPPIED: NAME 威震四方 FROM R13 (境5).

*** #2 ECONOMY AUDIT (rolls/round): 0,0,0,0,1,5,0,1,13,8,0,0,0,2,3,0,0,0 (~33 rolls, VERY low). ***
  - UNDER-rolled 威震四方 (named target should be #1 from R13 — 6 copies, never once rolled for it).
  - grant WASTED 3× at the 25 cap: R13 ended 24 (R14 +4 → 25), R16 ended 25 (R17 +6 wasted), R17 ended 25 (R18 +6 wasted).
    Pattern: I banked hard early then stopped rolling → grants hit the cap. FIX: land ≤19 before a grant round;
    spend the surplus hunting 威震四方/降龙 merge.
  - R9 = 13 rolls (境4 dump, landed 崩拳·连崩/戳 several — OK targeted-ish). Better than g19's R9=13 pre-境5 shotgun.
  - Ended 修为92 = highest in lobby (牧逸风 75, 谭舒雁 91, 吾行之 68) → WON every seat race. Absorb-everything works.

*** PER-RIVAL CAUSES ***
- pid1 谭舒雁 (6th-seat clock, the FINAL opponent): I beat her fielded board 100%/100% and her R17 8-card clock board
  100%/100%. Her C6 recipe (with 诸事不宜) is a HARD COUNTER I could not beat with ANY card in my pool (search_board
  400 evals converged at 0% — a genuine wall). She just didn't field it. Beat her R7/R13/R16/R17/R18; lost R3/R12.
- pid2 吾行之 (drain tank): my fielded board lost R10 (his Earth-Spirit def 12 + hexproof stacking + 减攻), beat R13/R15/R16.
  The 威震四方 board BEATS his final tank 100%/100% base AND +1 (35-dmg 连崩). His notebook's anti-chase 八门金锁阵
  is seat-locked to SECOND (must go second vs me) — I out-修为'd them (92>68) so he never took that seat vs me.
- pid0 牧逸风 (云剑/qi dud): beat R4/R9/R14/R16; lost R2 (early) / R11 (his ignore_def + hexproof). Never drew 万法 lv2
  (his converter) — his CP5 "engine without converter" curse, 7th straight game. 威震四方 board beats him 100%/100%.

*** SURPRISES ***
1. The lobby was won by my opponent's self-sabotage, NOT by my board being best. My board was the 2nd-best vs her.
2. I again failed to DRAW 威震四方 despite 6 copies in pool and it being THE fix (4th game in a row hunting a cap-raiser).
3. 谭舒雁 was dealt 诸事不宜 R9 and rolled it away — the exact card that beats me. Mutual M22 failure mode.
4. R18 final was decided by 3 HP (me) vs -2 (her) — a coin flip on my suboptimal board.

ECONOMY: ~33 rolls total (vs 谭舒雁 ~75, 牧逸风 ~79). I under-rolled. Bank-end 3,6,10,13,15,13,16,18,8,5,11,18,24,23,22,25,25,25.

==== LEDGER ENTRY · Game 21 ====
## Game 21 (ARENA g21) — 小布 (sect4 崩拳/气势/体魄, pid3). RESULT: NOT 1st, final 命 0 (eliminated R16). WINNER = 牧逸风 (pid0, 命48) — HE ASSEMBLED THE 万法 BOARD. pid1 谭舒雁 & pid2 吾行之 also dead.
Lobby: pid0 牧逸风 云剑/阵法师5, pid1 谭舒雁 命理师7, pid2 吾行之 水灵/阵法师5.
Record: W R1(pid2) L R2(pid1) L R3(pid0) W R4(pid2) L R5(pid0) W R6(pid1) W R7(pid2) W R8(pid0) L R9(pid2) L R10(pid1) W R11(pid0) L R12(pid2) L R13(pid0) L R14(pid1) L R15(pid0) L R16(pid0) L R16(pid1,DEAD). 6-10. Died to 牧逸风 2× + 谭舒雁 in the endgame.
SIDEJOB: 5 (阵法师). FATES: 磨砺不止, 锻体不息, 稳固根基, 生机不灭, 崩拳传承 (combat-irrelevant again, 9th confirmation). Gates 境2@R3 境3@R6 境4@R9 境5@R13. Ended 修为82 境5 体魄7 maxHP117.

## FINAL BOARD (R15/R16 fielded — THE MISTAKE BOARD): ['崩灭心法','岿然不动','崩拳·寸劲','崩拳·连崩','崩拳·戳+1','崩拳·突+1']
  → A 气势 board with NO 气势 ENGINE. card_stats R14/R16: 寸劲 20 dmg, 连崩 22, 戳 5 (hp_cost ate it), 势大力沉 4. TOTAL ~78 dmg over 8t.
  Force stayed at 4-5 the whole fight (only 崩灭心法+2 + 1/attack). 寸劲 (2×force) → 20, NOT the 40-50 it should be. LOST 0%/0% to 牧逸风's 万法 board AND 0%/0% to 谭舒雁.

### ★★★ #1 ROOT CAUSE — I FIELDED A 气势 BOARD WITH NO 气势 CARD. AGAIN (g19 was the same lesson; g20 I fixed it; g21 I RELAPSED). ★★★
  The proven winner skeleton (g18/g20, and re-verified THIS review) is:
  ['崩拳·降龙/缠 (opener, pre-buff)','威震四方','冲霄破浪','踏破九霄','势如破竹','崩拳·寸劲','崩拳·连崩','崩拳·戳/突'].
  It generates 8-9 force and with 威震四方 (cap 6→9) each finisher lands 24-26. My R16 board landed HALF that.
  I had 踏破九霄 dealt at R8 and ROLLED IT AWAY (踏破九霄→荷重前行). I had 崩拳·降龙 THREE TIMES at R14 and rolled all 3 away
  (崩骨→降龙, 周天→降龙, 降龙→天地浩荡). I rolled away 天地浩荡 ×2, 气若悬河, 玄心斩魄. M22 (rolled away engine pieces) at MASSIVE scale.

### ★★★ #2 ROOT CAUSE — 威震四方 NEVER DRAWN, NEVER NAMED. The card that decides g19 (found) and g21 (found again). ★★★
  Re-verified THIS review with search_board (pool 5, 40-50 evals): the ONLY 100%/100% boards vs 牧逸风's 万法 board ALL contain
  [威震四方 + (崩拳·降龙 OR 崩拳·撼) + 冲霄破浪 + 踏破九霄]. WITHOUT 威震四方, exhaustive search of my real pool found 0%/0% — the
  force cap of 6 hard-blocks the burst. 威震四方 = 6 copies live, ~2.7%/roll, 3.8%/deal. I NEVER rolled for it by name (rolling
  into 境5 was done shotgun). SAME failure as g19/g20: I NAME the target and never draw it. FIX: from 境5 unlock, EVERY dump
  = "威震四方" first, then 崩拳·降龙/踏破九霄/冲霄破浪.

### ★ TOP DISCOVERY (yisim-verified, 3-5 reps, both seats) — THE DECISIVE g21 BOARD. ★
`['崩拳·降龙+1','威震四方','冲霄破浪','踏破九霄+1','崩拳·寸劲','崩拳·连崩','崩拳·戳+1','崩拳·突+1']`
  = 100% FIRST / 100% SECOND vs 牧逸风's EXACT final board (t7, kills the turn BEFORE his 万法 fires).
  = 100%/100% vs 谭舒雁's EXACT final board. = 100%/100% vs 吾行之 base AND +1.
  Mechanical proof (full_log): 威震四方 sets max_force 9 → 冲霄破浪(+force=qi)+踏破九霄(+3force,+6agi→chase)+降龙 pre-buff(+5atk)
  → 寸劲=26, 连崩=26, 戳=24, 突=25. Kill lands t7 (opp at -2). My fielded board killed at t9-10 doing 20/card and lost.
  Even g20's WINNING board (崩拳·缠+1,踏破九霄,冲霄破浪,寸劲,势如破竹+1,连崩,撼,戳+1) = 0%/0% vs 牧逸风's 万法 board — the
  万法 board is the lobby CEILING and ONLY 威震四方+降龙 clears it.

### ★ 牧逸风 WON BECAUSE HE DREW 万法归灵剑 (R13 twice → merged +1 by R17). ★
  His final board ['辟邪阵纹','百鸟灵剑诀+1','引气剑+2','化灵诀','云剑·点星','云剑·点星','白鹭灵剑+1','万法归灵剑+1'].
  R16 vs me: 万法 fired 95 dmg in ONE turn (5+6×15qi) at t6b; 白鹭 50 at t5b. ~145 dmg over 2 turns. He banks qi all game then one-shots.
  His notebook CP5 says it 6 games running: the 万法/qi battery IS the win-con. He finally drew it. THIS is the meta board.

### ★ 谭舒雁 SELF-SABOTAGED HER OWN FIX BOARD (identical to my g20 discovery of her). ★
  Her notebook's fix board = [天星·牵引,血光之灾,天星·御心,诸事不宜,落花有意,梅开二度,杯弓蛇影+2,流水无情] (诸事不宜 = -6atk load-bearing).
  She FIELDED it R15/R16 (with 诸事不宜) but at R18 rolled 诸事不宜→杯弓蛇影 and fielded the 6-effect board WITHOUT it.
  → she lost R16 to 牧逸风 and barely limped. THE LOBBY KEEPS BEING DECIDED BY WHO DOESN'T SELF-SABOTAGE (C13, 3rd game).

### ECONOMY AUDIT (rolls/round): 0,0,4,0,0,0,0,0,3,0,8,0,10,25,0,15 (~65 total).
  - R14 = 25 shotgun rolls (rolled through 崩拳·降龙 ×3, 天地浩荡 ×2 — keepers I tossed). R16 = 15 shotgun (found nothing; took 突+1 to hand but never re-fielded it!).
  - grant WASTED: R10 ended 28 (R11 grant lost), R12 ended 26 (R13 grant lost). M24 AGAIN (4th game).
  - Belly: R1-R8 almost 0 rolls (good, absorbed all), but R9+ all shotgun with NO NAME. Ended 修为82 (mid). 牧逸风 90, 谭舒雁 95, 吾行之 67 — I lost the seat to 牧/谭.
  - BANKED EXCHANGES at R14 (landed 3) → then R15 granted +6 to 9 → R16 rolled. Fine in volume, wrong in NAMING.

### PER-RIVAL CAUSES:
 - pid0 牧逸风 (云剑/qi battery, WINNER): beat me R3,R5,R13,R15,R16 with the 万法 board once it came online. His 万法 = 95 one-shot.
   The 威震四方+降龙 board beats him 100%/100% (t7 kill). ONLY that board.
 - pid1 谭舒雁 (命理/内伤 clock): beat me R2,R10,R14,R16. With MY correct board I'd win 100%/100% (her R18 board lacked 诸事不宜).
   内伤 clock ~12-14 stacks; my 117 HP burst board outraces it IF I have a force engine. I did NOT → clock won.
 - pid2 吾行之 (水灵 tank): beat me R9,R12 (his 不动金刚阵+水灵 drain); I beat him R1,R4,R7. He died R14 to 牧逸风's 万法.

### SURPRISES:
 1. 牧逸风 finally drew 万法 (the card his own notebook named as the win-con for 6 games). It one-shot me for 95. CONFIRMS his CP5.
 2. My g20-WINNING board loses 0% to the 万法 board — the meta has moved; the 崩拳 skeleton alone is no longer universal.
 3. I relapsed to the g19 mistake (气势 board with no force card). The single fix is 威震四方 + keep 降龙/踏破/冲霄.

### SIDEJOB READ: 5 (阵法师) still correct (威震四方 is sect4, but 阵法师 gives 辟邪/不动金刚/回响 which are useful tech). Nothing beats it.

==== LEDGER ENTRY · Game 21 ====
## Game 21 ADDENDUM — FATE A/B TEST + reachability note.
- 崩拳传承 A/B (simulate my_extra_fates=[4] vs none): IDENTICAL 7t wins. 9th confirmation combat-fates are irrelevant for sect4 kit.
- REACHABILITY of the g21 decisive board: 崩拳·降龙 — I HAD copies (rolled through 3 at R14!). 威震四方 — NEVER drawn (0 hits in ~65 rolls; 2.7%/roll, 6 live copies).
  So the board was 50% reachable: I could have fielded [崩拳·降龙, 冲霄破浪, 踏破九霄(rolled away R8!), 崩拳·寸劲, 崩拳·连崩, 崩拳·戳+1, 崩拳·突+1] WITHOUT 威震四方 = still 0% vs 万法.
  → The TRUE g21 lesson: I needed 威震四方 and never named it. Had I drawn it + kept 降龙/踏破, I'd beat 牧逸风's 万法 board 100%.
- The lobby was decided at R13 by 牧逸风 drawing 万法 twice. RNG of the converter draw decided the winner. But my OWN error (no named 威震四方 rolls, rolling way 降龙/踏破) removed my counter-play.

==== LEDGER ENTRY · Game 22 ====
==== LEDGER ENTRY · Game 22 (ARENA g22) ====
## Game 22 — 小布 (sect4 崩拳/气势/体魄, pid3). RESULT: **1st PLACE / WINNER, 命 100**. A PERFECT (100 命) run.
Lobby: pid0 牧逸风 云剑/阵法师5 (DEAD 命0), pid1 谭舒雁 命理师7 (DEAD 命0), pid2 吾行之 水灵/阵法师5 (DEAD 命0).
Record: WON ALL 15 ROUNDS (R1-R15). 命 never dropped (a clean sweep — 命 cost never touched since I won every fight).
FATES: 磨砺不止, 气势充沛, 锻体, 崩拳传承, 顿悟 (境2/3/4/5 gates). ~10th confirmation: sect/传承 fates are combat-IRRELEVANT (A/B tested repeatedly).
SIDEJOB: 5 (阵法师). Gates: 境2@R3, 境3@R6, 境4@R9, 境5@R12. Ended 修为79 境5 体魄25 maxHP110-135.

## FINAL BOARD (R15, THE WINNER — 8 slots):
`['崩拳·降龙+1','玄心斩魄','气若悬河+1','踏破九霄','起势','崩拳·连崩+1','朝气蓬勃+1','势大力沉+1']`
  vs 谭舒雁 R15 board: 100% both seats BASE (~10t, wins at 14 HP vs her -3). vs her +1: 0% (structural — her clock at +1 outpaces burst).
  vs 牧逸风 R15 board (his last-known, NO 万法): LOST 0%/0% in review re-sim. vs 吾行之 R15 board: 100% first / 0% second.
  ⚠ I WON THE LOBBY BUT MY FIELDED BOARD IS NOT UNIVERSAL — it loses to 牧逸风's board. I got matched with 谭舒雁 R15 and killed her.

## ★ TOP DISCOVERY — 玄心斩魄 IS A REAL ANTI-CLOCK TECH (new this game). ★
  My R15 board ran 玄心斩魄 slot 2. 玄心斩魄 = "apply 2 stacks of EACH debuff you have to foe; 8 atk (your debuffs count as [Force] in this attack)".
  vs 谭舒雁 her 厄劫缠身 gives ME 内伤 each turn → by t3 I have 6 内伤 stacks → 玄心斩魄 SLAMS 2×6=12 内伤 BACK onto her
  AND treats my 6 内伤 as 6 [Force] on its own hit. Removed 玄心斩魄 (tested w/ 磅礴之势 instead) → drops to 100% first / 0% second vs her base.
  → 玄心斩魄 converts the 内伤 clock INTO burst + reflects it. KEEP IT vs any 内伤/debuff opponent.

## ★ #1 MECHANIC RE-CONFIRMED (g19-g22, 4th game) — 气势 CAP = 6; 威震四方 (+3 cap) IS THE DAMAGE KEY. ★
  gamestate_full.js:311 max_force=6; card_actions.js:5659 威震四方 adds +3 max_force. Force above cap is DISCARDED (4035-4040).
  THE CANONICAL WINNER BOARD (search_board, 3 separate searches agreed, both seats, base AND +1):
  `['崩拳·降龙+1','崩拳·连崩','威震四方','冲霄破浪+1','踏破九霄','崩拳·寸劲','崩拳·戳','崩拳·突']`
    - vs 牧逸风 (万法/last board): 100% first / 100% second BASE; 100% first / 0% second +1. (kills t7, one turn before his 万法 fires)
    - vs 谭舒雁: 100%/100% base; 0% vs her +1.
    - vs 吾行之: 100% first / 0% second base AND +1.
  KEY ORDER FIX found this review: 崩拳·连崩 goes in SLOT 2 (BEFORE 威震四方), then 威震四方 slot 3. That single swap took the board from 0%/0% → 100%/100% vs 谭舒雁. 连崩 slot2 = "carry the crash-fist effect into the next crash fist" pre-buffs 威震四方's line.
  REACHABILITY: 威震四方 = 6 copies @2.0%/roll. I DREW IT ZERO TIMES IN ~23 ROLLS AGAIN (5th straight game). This is the SAME recurring failure.

## ★ ECONOMY — I WON WITHOUT EVER DRAWING 威震四方 OR 万法-ANSWERS; the lobby was self-destructing around me.
  rolls/round: 0,0,2,0,0,1,0,0,8,0,0,0,4,5,3 (~23 total — very LOW, my absorb-everything discipline held).
  - NO 25-cap waste this game (banked 22/20/22 at R13/R14/R15 — under cap). ★ FIXED g20/g21's M24 for the first time.
  - But only ~23 rolls, NO NAMED TARGET → 威震四方 (~30% chance at ~23 rolls) never came. Still the #1 economy leak.

## ★ WHY THE LOBBY ACTUALLY BROKE — RIVALS SELF-SABOTAGED (C13, 4th game running, per their own frozen files):
  - 牧逸风: broke 境5 only at R12; his economy (15 rolls R8 AT 境3-4 = pre-境5 shotgun = 0 value) kept him behind; he NEVER drew 万法归灵剑
    this game (his CP4 win-con, 6+ games hunting it). His R14 board = 白鹭/灵感/点星 CHIP, no converter → couldn't kill me. He died R13 + later to others.
  - 谭舒雁: her OWN notebook C6 says the winning anti-崩拳 board needs 诸事不宜 (-6 atk ×2). Her R15 FIELD board had NO 诸事不宜 (she fielded 厄劫缠身, 探灵, 杯弓蛇影, 卜命, 天运·趋吉, 吉运初显, 金蝉脱壳, 枯木逢春) → my force burst out-raced her clock.
  - 吾行之: 修为 64 (LOWEST) → lost every seat → lost.

## PER-RIVAL CAUSES (all W for me):
  - pid0 牧逸风 (云剑/万法 ceiling): I beat him R3,R5,R7,R9,R13 — my force engine out-raced his qi-chip every time; he never assembled 万法.
    ⚠ In review my FIELDED board loses 0% to his LAST board — I only "beat" the BOSS version of him. He was eliminated by others before facing my board upgraded.
  - pid1 谭舒雁 (内伤 clock): W R2,R8,R10,R12,R15. 玄心斩魄 reflected her 内伤. Her fielded board lacked 诸事不宜.
  - pid2 吾行之 (水灵 tank): W R1,R4,R6,R11,R14. Force burst 100% first.

## SURPRISES:
  1. A 命100 PERFECT run with a board that loses 0% to 牧逸风's listed board — the LOBBY, not my board, decided the win. Opponents' RNG + self-sabotage gifted it.
  2. 玄心斩魄 (which I'd treated as a junk 境5 card) is the anti-injury-clock tech — highest-value NEW find of the game.
  3. Rolling 连崩 to slot 2 (before 威震四方) flipped a matchup 0%→100% — ORDER, not composition.
  4. 5th straight game drawing 威震四方 zero times. It is in 6 copies. NAME IT and roll 10+ for it from 境5.

## NEXT GAME RULES (sharpened):
  - R2 sidejob 5. R1-R9 absorb-everything. Break 境5 R11-12. R12+: EVERY dump NAMED 威震四方 FIRST, then 崩拳·连崩/寸劲/降龙/冲霄破浪/踏破九霄.
  - Field: [降龙, 连崩, 威震四方, 冲霄破浪, 踏破九霄, 寸劲, 戳/势大力沉, 突] with 玄心斩魄 slotted vs debuff/clock foes.
  - Land ≤21 before grant rounds (achieved g22 — keep it).
  - MERGE PRIORITY: 威震四方(no, it's not mergeable usefully) > 崩拳·寸劲 (+2 levels) > 崩拳·降龙 > 冲霄破浪 > 踏破九霄.

==== LEDGER ENTRY · Game 23 ====
==== LEDGER ENTRY · Game 23 (ARENA g23) ====
## Game 23 — 小布 (sect4 崩拳/气势/体魄 burst), pid3. RESULT: 3rd (of 4) — final 命 0. WINNER = 吾行之 (pid2, 命1).
Lobby: pid0 牧逸风 云剑/阵法师5 (DEAD), pid1 谭舒雁 命理师7 (DEAD), pid2 吾行之 水灵tank/阵法师5 (WINNER), pid3 me (DEAD).
Record: W R1(0) W R2(2) L R3(0) W R4(1) W R5(0) L R6(2) L R7(1) L R8(0) W R9(1) W R10(0) W R11(2) W R12(1) L R13(2) W R14(0) L R15(2) W R16(0) W R17(2) L R18(2). 11W-7L. DIED R18 to the tank.
FATES: 磨砺不止/变换之道/感悟丛生/顿悟/崩拳传承. Ended 修为100 境5 (absorb discipline good; seat LEAD 20 by R18).
SIDEJOB: 5 (阵法师). Gates: 境2@R3, 境3@R5, 境4@R8, 境5@R11.

## FINAL BOARD (R18, THE LOSING BOARD — 8 slots):
`['气若悬河','崩天步','威震四方','冲霄破浪','崩拳·寸劲+1','踏破九霄+1','崩拳·寸劲','磅礴之势']`
  card_stats R18: 气若悬河 +6qi/+3fr; 崩天步 +1qi/+4身法; 威震四方 +24def/+9fr; 冲霄破浪 +10fr/+10身法; 寸劲+1 63dmg; 踏破九霄+1 +8fr/+12身法; 寸劲 55dmg; 磅礴之势 57dmg/+76def.
  → total ~175 dmg over 14t. Tank reached 235 maxHP and healed +17/+25/+28 per 纳百川. LOST by 3 HP at t14 (五行刺+2 finished me).

## ★★★★★ TOP DISCOVERY — THE 身法/CHASE THRESHOLD IS THE DECIDER vs THE 水灵 TANK. ★★★★★
  崩拳 burst loses to 吾行之's tank because it can't out-damage the 纳百川 heal (+水势-scaling). The FIX is SPEED:
  stack ≥10 [身法] BEFORE your 寸劲 so 冲霄破浪 (or any card) AUTO-CHASES (gamestate_full.js:2545
  `if (me.agility >= 10 && me.chases < me.max_chases)`), giving TWO 寸劲 hits per cycle → kill by ~t10 BEFORE the ramp.
  VERIFIED (sim_matchup 12 reps vs his EXACT R18 board):
    R18 board (身法 from 冲霄+踏破 only): 100% first / 0% second, ~15t.
    R18 board but slot8 磅礴之势 → 崩拳·闪击 (+7身法): 100% FIRST / 100% SECOND, ~10t. **FLIPPED the second seat.**
    Same swap with 崩拳·惊触 (slot7, 踏破 slot8, 6 copies/2.5%roll): 100%/100% ~10t.
    Same with 天地浩荡 (身法 4+2×force): 100%/100%.
    CONTROL: pure-damage 崩拳·降龙 in that slot instead → 0% first / 0% second. **The 身法 is load-bearing, not the dmg.**
  崩拳·闪击 = 1 copy/0.4%roll (rare); 崩拳·惊触 = 6 copies/2.5%roll (REACHABLE) → use 惊触 as the default 身法 source.
  ⚠ 鹤步 (0% — caps at 10 身法 but needs 体魄 I have 0 of) does NOT work. 身法 SOURCE IDENTITY MATTERS.

## ★ THE FULLY-UPGRADED TANK IS A HARD COUNTER (honest structural finding).
  Every board I searched (with 阵法师 pool too) is 0%/0% vs a +1-everything tank. The tank's own notebook (吾行之 g23)
  confirms it: his base board = 0%/0% vs me; and he'd need the tank to start scaled. NOT winnable by 崩拳 burst kit.
  My REALISTIC target is his ACTUAL board (partially upgraded). 身法-chase boards win that 100%/100%.
  → Reachability lesson: I did NOT need to beat his phantom +1 board; the matrix used 3 sims and the tank ramps are
    high-variance, so MY 11W-7L was already near-optimal composition-wise. The R18 loss was the SECOND seat
    + the missing 身法 source, not a catastrophic build error.

## PER-RIVAL (final):
  - pid2 吾行之 (WINNER, 水灵tank): I was 4W-5L vs him (W R2,R11,R17; L R6,R13,R15,R18 — plus R16 vs 牧逸风). The tank
    out-scales; I win the EARLY/MID boards (his 五行-chip phase, R11/R17) and lose once 纳百川×2+不动金刚阵+回响 are up
    (R15/R18). Killed me R18 by 3 HP at t14 after healing past my burst.
  - pid0 牧逸风 (云剑/万法): I was ~5W-2L. His 万法 board is the ceiling but he only assembled 万法 at R13 (7 rolls NAMED)
    and it was still weak; his chip boards lose to my force burst. His notebook: 破气剑×2 = the anti-tank qi-denial tool.
  - pid1 谭舒雁 (命理师/内伤): I won most (W R4,R9,R12). Her 诸事不宜 (-6 atk ×2) is the anti-burst tool but she
    under-fielded it. Not my problem this game.

## ★ ECONOMY — named-target leak STILL #1 (5th game running), but seat discipline held.
  my rolls/round ≈ R5:2 R7:2 R8:22(!) R11:4 R14:3 R15:9 R16:11 R18:0 (~53 total). NO NAMED TARGET ever.
  R8=22-roll shotgun AT 境4 (pre-境5 → 境5 cards LOCKED → near-100% waste) = worst leak.
  R16=11-roll shotgun (post-境5, hunting nothing named). R15=9 (found 崩拳·寸劲 — useful but luck).
  I DID draw 威震四方 at R11 (rolled 势如破竹→威震四方) — broke the 5-game drought! It carried R15-R18.
  Ended 修为100, LEADING the seat vs everyone (吾行之 80, 牧逸风 79, 谭淑雁 64) — absorb-all discipline WORKED.
  NEXT-GAME ROLL TARGETS: R1-R9 absorb all, 0-2 rolls, land ≤24 before grants. Break 境5 R10-11.
    R11+ EVERY dump NAMED: 崩拳·惊触 (身法!) FIRST, then 威震四方, 崩拳·寸劲, 崩拳·连崩. STOP at ≤8 rolls.
    NEVER shotgun at 境4 (R8's 22 rolls = the single biggest waste of g23).

## SURPRISES:
  1. The fix for a losing matchup was ONE slot — 磅礴之势 → an 身法 source — and it flipped 0%→100% second seat.
     "Def dump" cards (磅礴之势) are TRAPS vs tanks: the tank doesn't care about my DEF, it just heals more.
  2. 身法 SOURCE IDENTITY matters: 崩拳·闪击/惊触 (flat, unconditional) work; 鹤步 (scales off 体魄 I don't have) doesn't.
  3. My notebook's g26 rule "100% first / 0% second, SEAT is everything" was WRONG for g23 — the matrix shows the tank
     beats me BOTH seats on base boards; only the 身法-fixed board wins both. SEAT was NOT the g23 issue; COMPOSITION was.
  4. I reached 修为100 (highest) and STILL lost — seat advantage doesn't help if the board can't kill.

==== LEDGER ENTRY · Game 24 ====
## ARENA Game 24 — 小布 (sect4 崩拳/气势/身法 burst), pid3. RESULT: 4th (of 4) — final 命 0. WINNER = 吾行之 (pid2, 命18).
Lobby: pid0 牧逸风 云剑/阵法师5 (DEAD), pid1 谭舒雁 命理师7 (DEAD), pid2 吾行之 水灵tank/阵法师5 (WINNER), pid3 me (DEAD).
Record: W R1(pid2) W R2(pid1) L R3(pid0) W R4(pid2) W R5(pid0) L R6(pid1) W R7(pid0) L R8(pid1) L R9(pid2) W R10(pid1) L R11(pid0) W R12(pid1) L R13(pid0) W R14(pid2) W R15(pid0) L R16(pid2) W R16(pid0) W R17(pid2) L R18(pid0). 11W-8L, but died R18 to 牧逸风 by 1 HP (he ended at 2). 
FATES: 磨砺不止/体修入道/筋骨健壮/崩拳传承/锻体. Ended 修为93 境5 maxHP121 体魄5 (HIGHEST 修为 in lobby — seat lead held, but board lost anyway).
SIDEJOB: 5 (阵法师). Gates broke 境2@R3, 境3@R6, 境4@R9, 境5@R12.

## FINAL BOARD I LOST WITH (R18):
`['气若悬河+1','冲霄破浪','威震四方','踏破九霄','崩拳·惊触','崩拳·寸劲','崩拳·连崩','崩拳·弹+1']`
  → going FIRST vs 牧逸风: I died t10 at -1 vs his 2 HP (he 邪蛊阵-内伤'd me + 万法归灵剑+1 hit 44). I lost by ~3 HP.
  card_stats R18: 气若悬河+6qi/+2fr; 冲霄破浪+10fr/+10身法; 威震四方+24def/+9fr; 踏破九霄+8fr/+12身法; 惊触 18dmg; 寸劲 35dmg; 连崩 28dmg; 弹+2 26dmg. ~107 dmg total, buried under his HP+内伤 chip.

## ★★★★★★ TOP DISCOVERY (THE FIX): THE 身法/CHASE ENGINE + 崩拳·惊触 = BEATS THE 215HP 水灵 TANK BOTH SEATS. ★★★★★★
  My OLD board had 身法 ONLY from 冲霄破浪(+5)+踏破九霄(+6)=11, dumped once then lost. The tank out-sustained me.
  THE FIX = add 崩拳·闪击 (+7 身法, PERSISTS to next 崩拳 — gamestate_full.js:2099/2111) so 身法 stays ≥10 EVERY turn
    → AUTO-CHASE fires every turn (gamestate_full.js:2545 `if (me.agility >= 10 && me.chases < me.max_chases)`) → 2 crash fists/turn.
  ORDER THAT WINS (yisim, both seats): `['气若悬河+1','威震四方','冲霄破浪','踏破九霄','崩拳·闪击','崩拳·惊触','崩拳·寸劲','崩拳·连崩']`
    vs 吾行之's REAL win board ['不动金刚阵','回响阵纹','水灵阵','水灵·纳百川','水灵·纳百川','水灵·波澜+1','水灵·波澜','五行刺+2'] (215 maxHP):
      **100% first / 100% second** (~11t). I end ~10-13HP. Kills BEFORE his 水势 ramp finishes.
    vs 牧逸风 EXACT final board: same shape, swap slot4 踏破九霄→灵玄迷踪步: `[...,'灵玄迷踪步','崩拳·闪击','崩拳·惊触','崩拳·寸劲','崩拳·连崩']` **100%/100% (~t6 kill!)**.
    vs 谭舒雁: both variants 100%/100% base; 灵玄 variant also 100%/100% vs her +1.
  WHY 惊触 at slot5: its bonus ("+1 ATK after next crash fist, +1 per 5 HP lost") fired for 21-25 EXTRA dmg on the 寸劲, then 连崩/chase
    delivered 33. The bonus GROWS as I lose HP (perfect with a hp-cost crash-fist deck). It's the single highest-leverage slot.
  ⚠ Both boards are 0% vs a FULLY +1-EVERYTHING upgrade — but that "+1 proxy" is over-pessimistic (rivals' own notes agree).

## ★ PER-RIVAL DECISION RULE (announced matchup):
  - vs 吾行之 (水灵 tank): field Board A (踏破九霄 slot4). 100%/100% both seats.
  - vs 牧逸风 (云剑/万法): field Board B (灵玄迷踪步 slot4). 100%/100%, kills t6.
  - vs 谭舒雁 (命理/内伤): Board B is 100%/100% incl +1. Use it.
  (Boards are identical except slot 4; the matchup is announced at round start, so pick per opp.)

## ECONOMY AUDIT (rolls/round): R1-7=0/0/0/0/0/0/1, R8=1, R9=2, R10=0, R11=2, R12=2, R13=0, R14=16(!), R15=0, R16=0, R17=6, R18=0 (~30 rolls).
  - R14=16 rolls right after 境5@R12 landed 崩拳·降龙/寸劲/冲霄/连崩 in one shotgun — landed the engine but was unfocused.
  - ★ I NEVER drew 崩拳·闪击 OR 崩拳·惊触 this game (the two cards the winning board needs!). They're 6 & 5 copies. My R17 6-roll hunt found 惊触 (1×). 闪击 never came.
  - Leak: I rolled 30 total but named NOTHING; the winning engine cards were search/discovery only. NEXT GAME: NAME 崩拳·闪击 + 崩拳·惊触 from 境5, 8-10 rolls each round if unseen.
  - 修为 93 (highest) but lost — seat lead ≠ win (C9 reconfirmed, 2nd game running).

## SURPRISES:
  1. The R18 loss was 1-3 HP — a SINGLE slot (adding 崩拳·闪击 for sustained 身法) flips the whole matchup to 100%/100%. My composition was one card from perfect.
  2. 崩拳·惊触's bonus scales with HP LOST — synergy with the hp-cost crash-fist deck; it's a finisher multiplier, not chip. Bigger than 寸劲.
  3. 灵玄迷踪步 ([持续]: +1qi+1身法/turn first-HP-loss) beats 踏破九霄 vs 云剑 (sustained vs burst) but loses narrowly vs the tank (burst matters more). Slot-4 identity is matchup-specific.
  4. 牧逸风's frozen notebook says "vs 小布 崩拳 burst: UNWINNABLE, he ends ~12" — my R24 revision turns that into my 100% win at t6. His counter-file is now stale.

## NEXT-GAME RULES (sharpened):
  - R2 sidejob 5. R1-9 absorb-all, ≤2 rolls, land ≤24 pre-grant. Break 境5 by R11-12.
  - R12+: EVERY roll NAMED: 崩拳·闪击 > 崩拳·惊触 > 崩拳·寸劲 > 崩拳·连崩 > 威震四方 > 冲霄破浪/踏破九霄.
  - Assembled board (per announced opp slot4): [气若悬河,威震四方,冲霄破浪,踏破九霄|灵玄迷踪步,崩拳·闪击,崩拳·惊触,崩拳·寸劲,崩拳·连崩].
  - ALWAYS sim_matchup both seats + EXACT board before set_board.

==== LEDGER ENTRY · Game 25 ====
==== LEDGER ENTRY · Game 25 (ARENA g25) ====
## Game 25 — 小布 (sect4 崩拳/气势/身法 burst), pid3. RESULT: 4th (of 4) — final 命 0. WINNER = 谭舒雁 (pid1, 命40).
Lobby: pid0 牧逸风 云剑/阵法师5 (DEAD), pid1 谭舒雁 命理师7 (WINNER), pid2 吾行之 水灵tank/阵法师5 (DEAD), pid3 me (DEAD).
Record: L R1(0) W R2(1) W R3(2) W R4(0) W R5(1) W R6(0) L R7(2) L R8(1) L R9(2) W R10(1) L R11(2) W R12(1) W R13(2) L R14(0) L R15(1) L R16(1). 8W-8L. Died R16 to 谭舒雁 (-19) after -21 at R15 — the two-clock-straight collapse.
FATES (境2→境5): 磨砺不止/再生之躯/顿悟/副职兼修/筋骨健壮. Ended 修为83 境5 maxHP105 体魄33. Seat LEAD vs 谭舒雁 (83 vs 82) — I went FIRST in R15/R16 and STILL lost.
SIDEJOB: 5 (阵法师). Gates broke 境2@R3, 境3@R6, 境4@R9, 境5@R11 (GOOD pacing).

## ★★★★★ ROOT CAUSE: BOARD ORDER + BENCHING MY FORCE-SCALING ATTACKER. NOT composition. ★★★★★
My R16 board was `['气若悬河+1','冲霄破浪','灵玄迷踪步','踏破九霄','势如破竹','崩拳·突+1','崩拳·缠','崩拳·惊触']` = 0% both seats vs her.
card_stats R16: 崩拳·突+1 0dmg(?!shown as Blitz), 崩拳·缠 6dmg, 崩拳·惊触 7dmg. Force-source 势如破竹 sat at SLOT 5 (AFTER the 身法 cards) so force was not stacked before the attackers.
**THE WINNING BOARD WITH CARDS I HELD (yisim-verified 100% going first / 0% second vs her EXACT final board):**
   `['气若悬河+1','势如破竹','崩拳·突+1','冲霄破浪','踏破九霄','崩拳·寸劲','崩拳·缠','崩拳·惊触']` (~10t, I end ~4hp)
   vs her +1 board: 0% (proxy is over-pessimistic; her own notebook agrees).
THE THREE ERRORS vs 谭舒雁:
 (1) ★ ABSORBED 崩拳·寸劲 at R16 for +1 修为 (修为82→83) then fielded 惊触 with NO force-scaling attacker. 寸劲 = "10atk, receives DOUBLE [Force] bonus" — the single best 气势-scaling card I own.
 (2) Fielded 灵玄迷踪步 (defensive mobility, 0 dmg scaling) in slot 3 instead.
 (3) Put the force-generator 势如破竹 at slot 5 (late) — force must be banked BEFORE the attackers.
CONTROL (5 reps each, vs her final board): force-source at slot2 → 100% first; force-source at slot5 or 灵玄 in slot3 → 0% both. **THE ORDER IS THE WHOLE GAME** (牧逸风's CP1 reconfirmed).

## ★★★★★ 崩拳·惊触 / 崩拳·连崩 MECHANIC (read from gamestate_full.js:2097-2151, 2449-2452) ★★★★★
 - 惊触 sets `this_card_crash_fist_shocked_stacks`. Fires in the "extra attack zone" AFTER the next CRASH FIST played:
   `atk_amt = 1 + floor(0.2 * hp_lost)` — scales with damage taken (60hp lost → 13 base, ×force → 42 in real log). Then clears the flag.
 - ★ 连崩 (`is_crash_fist_continue`) does NOT clear the per-card flags (line 2103 `if(!is_crash_fist_continue) clear`), so 惊触→连崩 makes the flag survive + 连崩 passes crash-fist effects forward → COMPOUND double-trigger. 连崩 is the multi-copy (8) key to the finisher.
 - 缠 does the same "apply on next 崩拳" but does NOT pass the flag forward → weaker. Prefer 连崩 at the LAST slot.
 - 惊触 MUST be the card IMMEDIATELY BEFORE the triggering crash fist (put it slot7, 连崩/缠 slot8) so the wrap fires.

## ★★★★★ vs 谭舒雁 命理/内伤 CLOCK — HARD COUNTER to burst, BUT beatable going FIRST with the right order ★★★★★
 Her R16 board: [天星·牵引, 厄劫缠身, 杯弓蛇影+1, 诸事不宜+1, 流水无情, 命运轮回+1, 气吞山河+1, 天星·御心].
 The clock: 厄劫缠身 opening +4 内伤, 杯弓蛇影 +2 内伤 +6 dmg, ramps to ~9-13 内伤/turn by t6-10. Ticks at MY turn-start, IGNORES 防, PERMANENT. I out-DPS her but bleed out; my own hp-cost 崩拳 (寸劲/降龙 cost hp) feed the loss.
 WIN = burst ~150 dmg before her t10. Force-source EARLY (slot2) so 寸劲/惊触 land at force cap. Won't kill through her 命运轮回+Great Spirit heal unless I front-load force. NEVER field 降龙 (hp-cost + def, no scaling) vs her; NEVER field 无敌迷踪 as filler.
 ★ vs 谭舒雁 I am 0% going SECOND (she ticks me dead at t10-11). SEAT LEAD (修为 7+) is mandatory — I HAD it (83>82) and still mis-ordered the board.

## ★★★★★ MATCHUPS (final, yisim both seats) ★★★★★
 - pid0 牧逸风 (qi-nuke 万法): burst-RACE board `['气若悬河+1','崩拳·突+1','冲霄破浪','踏破九霄','崩拳·寸劲','崩拳·惊触','势如破竹','崩拳·缠']` = **100%/100%** (force-source LATE — race him fast). With 威震四方+1: 100%/100%.
 - pid1 谭舒雁 (内伤 clock): force-EARLY board (above) = **100% first / 0% second**. With 威震四方+1: 100%/100%.
 - pid2 吾行之 (heal-tank): either board = **100%/100%** (incl his +1). EASY. Burst out-runs 纳百川.
 - ★★ ORDER IS MATCHUP-SPECIFIC: vs the CLOCK (long fight) stack force EARLY; vs the NUKER (fast fight) burst FIRST, force-source LATE. Same 8 cards, two orderings.

## ★★★★★ THE MASTER BOARD (search_board, 威震四方+1 variant) — beat EVERYONE 100%/100% ★★★★★
   `['气若悬河+1','威震四方+1','崩拳·突+1','冲霄破浪','踏破九霄','崩拳·寸劲','崩拳·惊触','崩拳·连崩']`
  100%/100% vs 谭舒雁 AND 牧逸风 AND 吾行之 (both seats). 威震四方 raises force CAP +4 (6→10) → force not clipped → 寸劲/惊触 hit ~40% harder.
  ⚠ REACHABILITY: I drew ZERO 威震四方 this game (6 copies, 2.4%/roll over ~57 rolls — a 57% miss). And +1 needs TWO copies. So this is the LUXURY target; the 势如破竹 order-fix (100% first) was the REALISTIC win.

## ECONOMY AUDIT (my rolls/round): 0,0,0,0,0,0,0,4,0,5,1,23,0,12,11,0 ≈ 56 rolls.
 - R8=4 (境4 shotgun), R10=5, R12=23 (! shotgun at 境5), R14=12, R15=11 — ALL NAMELESS.
 - I drew 崩拳·寸劲 at R11 (dealt) and R16 (dealt) — I rolled it away R11 and ABSORBED it R16. My best card, twice thrown away.
 - NEVER drew: 威震四方, 崩拳·连崩, 崩拳·闪击. The three key finisher/force-cap cards (6/8/6 copies).
 - Broke 境5 R11 (good) and ended 修为83 (SEAT LEAD) — pacing/economy discipline FINE. The fail was ASSEMBLY+ORDER.
 - Winner 谭舒雁: rolls ≈ [0,0,0,0,0,13,5,3,3,4,4,3,7,2,4,0] — ALSO a lot of shotgunning, but she assembled her clock by R13-16 via merges (命运轮回+1 etc. from dealt duplicates).

## SURPRISES
 1. I had the SEAT (修为 83 vs 82) — the exact margin that decides this matchup — and WASTED it on a mis-ordered board. A single reorder (崩拳·突+1 to slot3, 寸劲 in, force-source to slot2) flips 0%→100%.
 2. 崩拳·惊触's real output in R16 was 7 dmg — my notebook's g24 claim ("+34 finisher") was WRONG for that order, because 惊触 was after 缠 (which doesn't pass the flag) and no strong 崩拳 preceded it.
 3. 谭舒雁's clock (内伤) is the lobby's hard counter — she beat EVERYONE 100% base. My burst is the only thing fast enough to beat it, and only going first.
 4. 威震四方 (force cap +3/+4) is the highest-leverage card for 崩拳/气势 — lets 寸劲/惊触 exceed the default 6-force clip. Worth hunting at 境5 above all else.

## NEXT-GAME RULES (sharpened):
 - R2 sidejob 5. R1-9 absorb-all, ≤1 roll, land ≤24 pre-grant. Break 境5 by R11.
 - ★ NAME every 境5 roll: 威震四方 > 崩拳·连崩 > 崩拳·寸劲 > 崩拳·闪击 > 冲霄破浪/踏破九霄/势如破竹. STOP at ≤8-10.
 - ★ NEVER roll away or absorb 崩拳·寸劲 / 崩拳·连崩 / 威震四方 (my scaling trio).
 - ★ ORDER RULE: force-generator (威震四方/势如破竹/冲霄破浪) BEFORE the 寸劲/惊触 attackers. vs a clock: force EARLY. vs a nuker: burst FIRST, force late.
 - ★ 惊触 goes slot7, 连崩 slot8 (finisher pair, last).
 - ALWAYS sim_matchup BOTH seats vs the announced opp's EXACT last board before set_board.

==== LEDGER ENTRY · Game 26 ====
==== LEDGER ENTRY · Game 26 (ARENA g26) ====
## ARENA Game 26 — 小布 (sect4 崩拳/气势/身法 burst), pid3. RESULT: **1st PLACE / WINNER, final 命 17.** ★★★ FIRST WIN IN 7+ GAMES.
Lobby: pid0 牧逸风 云剑/阵法师5 (DEAD 命0); pid1 谭舒雁 命理师7 (DEAD 命0); pid2 吾行之 水灵tank/阵法师5 (DEAD 命0); pid3 me (WINNER 命17).
Record: W R1(0) L R2(2) W R3(0) W R4(2) W R5(1) L R6(0) L R7(1) W R8(0) W R9(1) W R10(2) W R11(1) W R12(0) W R13(1) L R14(0) L R15(2) W R16(2) L R17(0) W R18(0) W R19(2). 14W-5L. Won the R19 title fight vs 吾行之 (-31命 to him, 10t).

## FINAL BOARD (R19, fielded & WON the title round):
['崩拳·闪击','气若悬河+1','威震四方+1','冲霄破浪+1','踏破九霄','崩拳·寸劲','崩拳·惊触','崩拳·连崩+1']
  ★ THIS IS THE MASTER BOARD my g24/g25 playbook predicted, FULLY ASSEMBLED for the first time (威震四方+1 AND 闪击 AND 连崩+1 all together).
  sim_matchup (post-game, 3-5 reps): 100%/100% vs pid0 base AND +1; 100%/100% vs pid1 base AND +1; 100%/100% vs pid2 base.
  ONLY weakness: pid2's +1 board going SECOND (0%) — but nobody fielded a fully +1 board, so IRRELEVANT.

## FATES: 磨砺不止/再生之躯/顿悟/生机不灭/筋骨健壮 (all economy/体魄 — 5th straight confirmation combat fates are combat-irrelevant).
Ended 修为100 (HIGHEST in lobby — held seat lead), 境5 maxHP111 体魄31. Gates: 境2@R3, 境3@R6, 境4@R8, 境5@R12.

## ★★★★★ WHY THIS GAME WON (the thing that finally worked) ★★★★★
EVERYTHING my g24/g25 playbook prescribed, executed:
 (1) ASSEMBLED the master board (闪击+威震四方+1+连崩+1 together) — never achieved before. 身法≥10 sustained EVERY turn → AUTO-CHASE (2 崩拳/turn).
 (2) 威震四方+1 raised force CAP 6→10 → 寸劲/惊触 hit ~40% harder (verified: 惊触 fired 14-18 extra, 连崩 hit 38-41).
 (3) Avoided the g25 blunder: NEVER absorbed a KEEP-LIST attacker. Ended 修为100 by absorbing only TRUE junk.
 (4) R19 title fight: my board killed 吾行之's tank t10 (惊触+连崩 wrap = 38+41 double finisher).

## ★ ECONOMY AUDIT (mine): rolls/round = 0,0,0,0,3,0,0,0,0,5,4,8,9,2,0,0,0,0,0 ≈ 31 total.
 - R10 (5), R11 (4), R12 (8), R13 (9) = the post-境5 named dumps that LANDED 闪击/气若悬河/威震四方/寸劲/连崩 — the engine.
   R13's 9-roll run (崩拳·封→荷重前行→八门金锁阵→锻髓→冲霄破浪→回响阵纹→冥影身法→威震四方) hit 威震四方 = the KEY card.
 - R14 (2), R15-R19 (0) = banked + mass-merged (威震四方+1@R16, 连崩+1@R19). GOOD: this is the R16 mass-merge lesson from 谭舒雁 applied.
 - Banked 31 by game end (well over the 25 cap) — but that's FINE at R17+ (no more need to bank; wasted grants are moot).
 - ★ COMPARISON: I rolled ~31 total but with PURPOSE (per-round named hunts). 谭舒雁 shotgunned 25 at R11 + 5/7/6 after (?W). 牧逸风 12 at R9 + 26 at R13 (nameless). My economy was the CLEANEST ever — and it WON.

## ★ PER-RIVAL CAUSES (final boards):
- pid0 牧逸风 (云剑/万法 qi-nuke, 万法+1 = 60-67 one-shot): 4W-3L (L R6,R14,R17). BEAT him whenever my board was assembled (100%/100% both seats). His 万法 one-shot (67 dmg at t7 vs my 144 maxHP) is survivable because 体魄+maxHP stack. Lost R6/R14/R17 only with PARTIAL boards (missing 威震四方 / 惊触).
- pid1 谭舒雁 (内伤 clock, 命理师7): 4W-2L (L R7,R15). Her clock ticks ~9-11/turn; my burst kills t6-8 → I out-race her. 100%/100% incl +1. Lost R7/R15 with transitional boards.
- pid2 吾行之 (水灵 heal-tank): 5W-2L (L R2,R15). Burst out-runs 纳百川 ramp. R2 loss = unassembled R1-R2 pile (his early 五行刺/火灵 Rush killed me). 100%/100%.
- ★★ DECISIVE INSIGHT: I lost ONLY when my board was a PARTIAL/transitional pile (R2,R6,R7,R14,R15 — all pre-R16). From R16 onward (full master board) I went 3-1, the only loss being R17 (a 1-HP-style race vs 牧逸风 with 惊触 still lv1). The BOARD, not the seat, decides — and once assembled the board beats EVERYONE.

## ★★★★★ TOP DISCOVERY [g26]: THE MASTER 崩拳 BOARD IS REACHABLE AND WINS THE LOBBY. ★★★★★
  ['崩拳·闪击','气若悬河+1','威震四方+1','冲霄破浪+1','踏破九霄','崩拳·寸劲','崩拳·惊触','崩拳·连崩+1']
  = 100%/100% vs ALL THREE rivals' final boards AND their +1 (post-game sim, 3-5 reps). It beats the g25-losing board (谭舒雁) 100/100 BOTH seats.
  The three previously-missing pieces (闪击/威震四方+1/连崩+1) were ALL reachable in a single game: 闪击+连崩+1 dealt/merged, 威震四方 drawn R13 + merged R16.
  ORDER: 闪击(slot1, opens 身法) → 气若悬河+1/威震四方+1/冲霄破浪+1/踏破九霄 (force+身法 battery) → 寸劲 (double-force attacker) → 惊触 (finisher flag) → 连崩+1 (16atk finisher).
  ★ 惊触 at slot7 (AFTER the force battery, BEFORE 连崩) is correct: it sets the flag, the NEXT 崩拳 (连崩 wrap or the chase 崩拳) triggers the +bonus.

## ★ ORDER A/B (post-game, decisive): 
  Order A (惊触 slot7, 连崩 slot8) = 100/100 vs pid0, 100/100 vs pid1, 100/0 vs pid2+1(second). ← MY BOARD, BEST.
  Order B (连崩 slot7, 惊触 slot8) = 100/0 vs pid0(second), 100/100 vs pid1, 100/0 vs pid2+1(second). ← WORSE (broke pid0).
  → KEEP 惊触 slot7, 连崩 slot8. The slot8 连崩's ATK (16) matters vs 牧逸风's fast t7 nuke; reordering to put 惊触 last delays my finisher by one slot and loses the pid0 race.

## SURPRISES:
 1. I WON — after g22-g25 all placing 4th. The difference was purely ASSEMBLY: this game I actually drew and merged 闪击/威震四方/连崩+1 together for the first time.
 2. 体魄 (31) + 境5 maxHP (111) + in-battle 纳百川-style HP growth let me eat 牧逸风's 67-dmg 万法 nuke and keep going (finished R19 at ~48/144).
 3. 崩拳·连崩+1 (16atk lv2) is a MONSTER finisher when the 惊触 flag is live: R19 惊触→连崩 wrap = 38 + 41 (double hit).
 4. The 身法 AUTO-CHASE (闪击 keeps 身法≥10) is what converts 8 cards into ~14-16 card-plays over a 10-turn fight = the whole engine.

## NEXT-GAME RULES (sharpened):
 - R2 sidejob 5. R1-9 absorb-all junk (NEVER a KEEP-LIST card), ≤1-2 rolls, land ≤24 pre-grant. Break 境5 by R11-12.
 - ★ R10-R13: the post-境5 NAMED dump (5-9 rolls/round). PRIORITY: 崩拳·闪击 > 威震四方 > 崩拳·连崩 > 崩拳·寸劲 > 崩拳·惊触 > 冲霄破浪/踏破九霄/气若悬河.
 - ★ R14+: STOP rolling. Bank + mass-MERGE doubles (威震四方+1, 连崩+1) — free power, no deck-burn.
 - ★ TARGET BOARD (slot-by-slot): [崩拳·闪击, 气若悬河+1, 威震四方+1, 冲霄破浪+1, 踏破九霄, 崩拳·寸劲, 崩拳·惊触, 崩拳·连崩+1].
 - ★ LOCK 惊触 slot7 / 连崩 slot8 (Order A). sim_matchup both seats + exact board before every set_board.

==== LEDGER ENTRY · Game 27 ====
## ARENA Game 27 — 小布 (sect4 崩拳/气势/身法 burst + 阵法师5), pid3. RESULT: NOT 1st, final 命 0.
WINNER = 牧逸风 (pid0, 命59, 云剑/万法 qi-nuke). 谭舒雁(pid1) & 吾行之(pid2) also dead 命0.
W/L (18 battles): L R1(pid1) W R2(pid0) W R3(pid1) L R4(pid0) W R5(pid1) L R6(pid2) L R7(pid0) L R8(pid2) L R9(pid0) W R10(pid2) W R11(pid1) W R12(pid2) L R13(pid0) W R14(pid2) L R15(pid0) W R16(pid2) L R17(pid0) L R18(pid0). 8W-10L. I went 0-6 vs 牧逸风 in the last 6 meetings.
FATES: 磨砺不止, 锻体不息, 历战不屈, 生机不灭, 再生之躯 (economy default — fine).
Final 修为90 境5 maxHP125 体魄24. FINAL BOARD: ['崩拳·闪击+1','气若悬河+1','威震四方+1','锻骨','踏破九霄','崩拳·寸劲+1','崩拳·连崩','崩拳·寸劲'].
Gates: 境2@R3 境3@R6 境4@R9 境5@R12.

### ★★★★★ #1 ROOT CAUSE — I DREW 不动金刚阵 AT R18 AND ABSORBED IT FOR +1 修为. ★★★★★
Evidence: economy_history R18: "rolled 荷重前行 -> 不动金刚阵" then "absorbed 不动金刚阵: 修为 88->89".
不动金刚阵 [持续]2: at turn end +7 def, and +7 HP/maxHP if you did NOT chase this turn.
yisim PROOF (5 reps each): my ACTUAL R18 board = 100/100 vs 牧逸风 BASE but **0% when he goes FIRST vs his +1 board** (kills t6, dies to his t6 万法).
THE FIX (swap 踏破九霄 -> 不动金刚阵, keep everything else): **100% first / 100% second vs 牧逸风's EXACT final board AND his +1 board, kill t5** (one turn before 万法 fires).
★ AND IT IS UNIVERSAL: this same board = 100/100 (base AND +1) vs 谭舒雁 AND 吾行之 too. ONE board wins the whole table.

### ★ WHY I LOST THE 牧逸风 WAR (FULL MECHANISM):
牧逸风 = 聚灵心法+1 (slot1) + 回响阵纹 (slot2) DOUBLE-QI ENGINE → qi ramps ~+4/turn → 万法归灵剑 (slot6) fires t6 with 17-21 qi = 90-110 dmg ONE-SHOT.
R17 log: t6 his 万法 = 110 dmg killed me at 99 HP. R18: t6 = 90 dmg killed me at 88 HP.
I lost ONLY the "he goes first AND board even slightly slow" races. My board simply needed ONE more turn of survival. 不动金刚阵 (+7 def/turn +7 hp if no-chase) provided exactly that and pushed my kill to t5.

### ★ #2 — 崩拳·惊触 NEVER APPEARED (6 copies, 3.6%/roll, never dealt). My board lacked the 惊触/连崩 compound finisher; I substituted a 2nd 寸劲. Acceptable but weaker. The g26 MASTER board needs 惊触 — when it's not dealt, the next best is 不动金刚阵 (sustain), NOT a raw attacker.

### ★ #3 — ECONOMY LEAKS (my rolls/round): R1-6=0, R7=15(SHOTGUN at 境3 gate), R8=0, R9=11(shotgun at 境4 gate), R10=10, R11=0, R12=9, R13=6, R14=0, R15=14(shotgun), R16=0, R17=7, R18=10. Total ≈82.
- R7(15) + R9(11) pre-境5 shotguns = near-zero value (7th+ confirmation of M29). 
- The R15/R17/R18 rolls landed the RIGHT pieces (闪击, 连崩, 威震四方+1, 冲霄破浪, 不动金刚阵) but I kept re-rolling/burning them (R18: rolled 踏破九霄->荷重前行, 冲霄破浪->踏破九霄, then 势大力沉->引雷阵; net churn).
- WINNER 牧逸风 also shotgunned (R12=26) but he had a NAMED target (聚灵心法+回响+万法) and LANDED the engine.
- NEXT-GAME: R7/R9-style pre-境5 shotguns = forbidden. Post-境5 rolls must be NAMED.

### TOP DISCOVERY [g27]: 不动金刚阵 IS THE UNIVERSAL 8TH SLOT FOR THE 崩拳 BOARD — it converts the fragile t6 race into a t5 win vs the 万法 nuke AND wins 100/100 vs the whole lobby (base AND +1). I HAD IT IN HAND AND ABSORBED IT. New KEEP-LIST card.
*** SURPRISE: 牧逸风's 聚灵心法+回响阵纹 double-qi engine (which I invented-in-g26-as-小布... no, that was me 小布 in g26) is EXACTLY the engine 牧逸风 used to kill me. The double-qi 万法 nuke is the lobby's real boss; my 崩拳 MUST kill by t5 or lose.
*** REACHABILITY: 不动金刚阵 = sidejob-5, 3 copies, 12.5%/sidejob-deal — I drew it TWICE (R14 absorbed it too! "absorbed 不动金刚阵: 修为 63->64"). Twice drew it, twice absorbed. Double failure.
*** Winner's seat: 牧逸风 ended 修为83 vs my 90 — I had the seat going into R18 (obs said lead by 7) yet the R18 log shows HIM first. He must have absorbed more that turn OR the seat flipped on the round he broke. Either way: don't rely on a thin seat lead.

==== LEDGER ENTRY · Game 28 ====
## ARENA Game 28 — 小布 (sect4 崩拳/气势/身法 burst + 阵法师5), pid3. RESULT: **NOT 1st — final 命 0.** WINNER = 牧逸风 (pid0, 命1). 谭舒雁(pid1)/吾行之(pid2) also dead 命0.
NOTE: my notebook header was STALE (said "g28 WIN") — this ARENA g28 is a LOSS. Trust the standings prompt, not the header.

W/L (20 battles): L R1(pid2) W R2(pid1) W R3(pid0) L R4(pid2) L R5(pid1) W R6(pid0) L R7(pid2) W R8(pid0) L R9(pid2) L R10(pid0) W R11(pid1) L R12(pid0) W R13(pid1) W R14(pid2) W R15(pid0) W R16(pid0) L R17(pid0) W R17(pid2) L R18(pid0) L R19(pid0). 9W-9Lish. vs pid0 牧逸风: 5W-6L. Died R19 going SECOND to 牧逸风.

FATES: 磨砺不止, 储纳灵气, 再生之躯, 生机不灭, 历战不屈 (economy/体魄 — 6th straight confirmation combat fates are irrelevant).
Ended 境5 修为97 maxHP128 体魄47. Gates: 境2@R3 境3@R6 境4@R9 境5@R12.

FINISHED board (R19, LOST): ['崩拳·闪击+1','气若悬河+1','冲霄破浪','威震四方+1','踏破九霄','崩拳·戳','崩拳·弹','崩拳·惊触+1'] — only 3 real attackers + 闪击; ~62 dmg by t6b; got 牧逸风 to 47 then died to his t7a 万法 (95 dmg).

## ★★★★★ #1 ROOT CAUSE — I ROLLED AWAY 崩拳·连崩 TWICE AT R11. ★★★★★
economy_history R11: "rolled 崩拳·截脉 -> 崩拳·连崩" ... then "rolled 崩拳·连崩 -> 浩然正气"; again "势大力沉 -> 崩拳·连崩" then "崩拳·连崩 -> 浩然正气". I HELD the winning finisher-chip TWICE and burned both. 崩拳·连崩 (11atk, retain 崩拳 effect) is a TOP-3 KEEP card — it is the 4th attacker that turns my t6b 47-left into a t6b KILL.
## THE FIX (yisim-verified, 7 reps): swap 冲霄破浪 → 崩拳·连崩; upgrade 崩拳·弹 → +1. Board:
#   ['崩拳·闪击+1','气若悬河+1','崩拳·连崩','威震四方+1','踏破九霄','崩拳·戳','崩拳·弹+1','崩拳·惊触+1']
#   → 100% BOTH seats vs 牧逸风 as-is (kill t6a first / t6b second, BEFORE his t7a 万法).
#   → 100%/100% vs 吾行之 as-is AND +1. → 100%/100% vs 谭舒雁 as-is AND +1. ONE UNIVERSAL BOARD wins the whole lobby BOTH seats.
#   Reachability: I held 连崩 twice (rolled away) + 弹 (absorbed R11). FULLY reachable; this was a DISCIPLINE failure, not a draw failure.

## ★★★★★ #2 — THE SEAT COST ME THE GAME (again). ★★★★★
R18: obs said I LED by 6 修为 (97 vs 91) yet the log shows 牧逸风 FIRST. He absorbed to ~96 in-round. I lost R18 (-5 → 命1) going second. R19: lost again going second → dead (-31). BOTH decisive fights I went second.
→ LESSON (matches all 3 rivals' ledgers): 修为 lead is NOT safe because the opponent absorbs in the same round. THE ANSWER IS A BOARD THAT WINS BOTH SEATS, not a fragile seat lock.
## MUCH more robust than g27's 不动金刚阵 fix: adding 连崩 (chip attacker) instead of 冲霄 (a pure battery). 冲霄 contributes 0 dmg; 连崩 contributes ~13-20 + feeds the chase chain.

## ★ PER-RIVAL CAUSES:
- pid0 牧逸风 (云剑 double-qi 聚灵心法+回响 + 万法 slot8, 95-110 dmg one-shot at t6-7): 5W-6L. I beat him whenever I went FIRST or had an assembled burst. His 万法 fires LAST slot → I have until t6b-t7a to kill. R17 (my best): I got him to 15 HP at t6a but lacked 连崩 → no kill. R18/R19: went second → died to t7a 万法.
- pid2 吾行之 (水灵 sustain, 5 force_of_water ramps + direct dmg): 1W-4L early (R1/R4/R7/R9 — all with unassembled boards), then W R14/R17 once burst assembled. His 力 ramp starts slow; my assembled burst kills t6 (100/100 both seats). Early losses = partial boards, NOT a matchup problem.
- pid1 谭舒雁 (命理师 内伤/attack clock, slow 1-16 dmg/turn): 3W-0L. My burst kills t6 before her clock matters (100/100 both seats both levels).

## ★ ECONOMY (my rolls/round): R9=8, R11=21, R12=8, R13=8, R15=10, R18=24 = ~79 total.
- R11=21 + R18=24 = the two shotguns. R11 was pre-finisher (境3) — burned 21 with mostly junk (landed 寸劲/连崩 but ROLLED BOTH AWAY). R18 was post-境5 but I was hunting 寸劲 (didn't find) and burned my 连崩-eligible hand.
- R9=8 (pre-境4/5) = another pre-gate waste (8th straight confirmation M29).
- WINNER 牧逸风: 0 rolls R1-R8, ONE 13-roll dump R9, ONE 23-roll dump R13, ONE 23-roll dump R17 (found 回响+万法!). Total ~59, ALL post-breakthrough and NAMED. His R17=23 landed 回响阵纹 AND 万法归灵剑 in one session = the engine.
- NEXT-GAME ROLL TARGET: R1-R9 ≤2 rolls (absorb junk for 修为). At 境5 (R12+): NAME-HUNT {崩拳·闪击, 威震四方, 崩拳·连崩, 崩拳·寸劲, 崩拳·惊触, 崩拳·戳, 崩拳·弹} in a tight ≤6/round budget. STOP the instant a KEEP-LIST piece lands. NEVER roll a KEEP-LIST card.

## ★★★★★ TOP DISCOVERY [g28]: 崩拳·连崩 IS THE 4TH ATTACKER THAT FLIPS THE SEAT RACE. ★★★★★
The master board needs FOUR 崩拳 attackers (连崩/戳/弹/惊触) minimum; 冲霄破浪 is a pure battery (0 dmg) and should LOSE its slot to 连崩. With 4 attackers + 闪击 chase, the board kills t6 both seats vs the entire lobby, and 连崩's "retain 崩拳 effect" chains the 惊触 追加. Verified: 连崩-only (弹 lv1) → 100% second/0% first; 弹+1-only → 100% first/0% second; BOTH → 100%/100%. The seat-flip is KNIFE-EDGE — you need BOTH the extra attacker AND the upgrade.

## SURPRISES:
1. Going second in R18 AND R19 killed me — the g27 "absorb everything for the seat" lesson backfired: I had the修为 lead nominally but the opponent absorbed in-round to flip it. SEAT-LOCKING IS UNRELIABLE. Build a both-seat board instead.
2. 牧逸风's 万法 is his LAST slot (slot8) → he needs t7 to fire. If I kill by t6b he never gets it. My loss was ALWAYS "one cycle short" — a single extra attacker fixes it.
3. 吾行之's 力 (force_of_water) deals direct dmg per 水灵 card, ramping. His early R1-R9 wins vs me were board-state (unassembled), confirmable.
4. My notebook header was STALE/WRONG (said g28 WIN). Always reconcile the header against the authoritative standings.

==== LEDGER ENTRY · Game 29 ====
## ARENA Game 29 — 小布 (sect4 崩拳/气势/身法 burst + 阵法师5), pid3. RESULT: NOT 1st — final 命 0.
WINNER = 谭舒雁 (pid1, 命理师7, final 命 87). 牧逸风(pid0)/吾行之(pid2)/me all dead 命0.
W/L (16 battles): W R1(2) W R2(0) L R3(1) L R4(2) W R5(0) L R6(2) L R7(0) L R8(1) L R9(0) W R10(2) L R11(1) W R12(2) L R13(0) L R14(1) W R15(0) L R16(1). 6W-10L.
★ I went 0-4 vs 谭舒雁 THIS GAME (L R3,R8,R11,R14,R16) — she is my actual nemesis, not 牧逸风.
FATES: 磨砺不止, 锻体不息, 变换之道, 生机不灭, 锻体 (7th straight confirmation: economy/体魄 fates are fine; combat fates irrelevant).
Ended 境5 修为79 maxHP121 体魄7. Gates: 境2@R3 境3@R6 境4@R9 境5@R13.
FINAL BOARD (R16, LOST): ['辟邪阵纹','崩拳·闪击','威震四方','崩拳·撼+1','崩拳·连崩','崩拳·突','崩拳·降龙','崩拳·惊触']

### ★★★★★ #1 ROOT CAUSE — I WAS ONE UPGRADE SHORT vs 谭舒雁, AND LOST THE SEAT. ★★★★★
sim_matchup vs 谭舒雁's EXACT final board ['天星·牵引','血光之灾','杯弓蛇影','杯弓蛇影','诸事不宜','诸事不宜','星弈·断','反震心法+1']:
  my AS-FIELDED board: 100% going FIRST / **0% going SECOND** (12t).
  matrix confirms: 谭舒雁 vs 小布 [base/base] = she wins 100% first / 0% second; [+1/+1] = she wins 0% both.
★★★ THE FIX (3 independent search_board runs + manual sim, all agree): **ONE +1 LEVEL ON ANY BIG ATTACKER FLIPS IT TO 100%/100%.**
  - 崩拳·连崩 -> 连崩+1 (11->16 ATK): full-log verified WIN going SECOND (kills t11, hits 27; she dies -5, I live at 4).
  - 崩拳·撼+1 -> 撼+2 (11->12 ATK + force feed): WIN both seats (search trace).
  - 威震四方+1 or 崩拳·突+1: also flips (search trace).
  - ★ 崩拳·惊触+1 does NOT fix it (she survives at 3, kills me t12) — upgrading the FLAG card doesn't add the finisher ATK. UPGRADE THE BIG HITTER (连崩/撼/突), not 惊触.

### ★ WHY (full mechanism, yisim log): 谭舒雁's board = HP-STACK + [内伤] CLOCK + MITIGATION.
  反震心法/Repel Citta-Dharma: +4/+6 maxHP AND heals (+dmg-reflect). She grows 99->103->111->117.
  杯弓蛇影/血光之灾/落花/流水无情: stack [内伤] → I lose 4-11 HP at MY turn start (permanent, through 防).
  诸事不宜: her 防+4 AND reduces my next 2 attacks by 6 → blunts my small hits.
  Her clock finishes ~t11-12. Going SECOND she gets the extra clock tick and wins the race. Going FIRST I kill her before the accumulation.
  → THIS IS A TURN-11 ATTRITION RACE. My kill lands at t11 with as-fielded board; ONE more ATK flips my t11 from "3 HP short" to a kill.

### ★ #2 — SHE OUT-ABSORBED ME 88 vs 79 AND STOLE THE SEAT. I was 9 修为 behind → she went FIRST in every late round.
Her 勤学苦练 fate = DRAW A CARD ON EVERY ABSORB → absorbing is free card-gen for her, so she shotgun-rolled 21 (R9) then absorbed 20+ cards R15-18, ending 修为92. My pure-economy fates gave no such synergy.
→ LESSON: 修为 = seat. When your win-condition vs the announced opp is seat-dependent (0%/100%), you MUST out-absorb them. And 勤学苦练-style draw-on-absorb is a SUPERIOR economy fate for a clock/absorb deck.

### ★ #3 — ECONOMY LEAKS (my rolls/round): 0,0,0,0,0,0,4,2,0,3,0,0,19,0,9,5,0(,0) ≈ 42.
  - R13=19 (post-境5) churned badly: rolled AWAY 崩拳·寸劲 AND 崩拳·连崩 (landed 连崩, re-rolled it to 百杀破境掌 — but 连崩 stayed on board). Did land 寸劲/连崩 then discarded 寸劲.
  - R16 **ABSORBED 不动金刚阵+1 AND 崩拳·戳+1 — BOTH KEEP-LIST +1 CARDS** (修为 77->78, 78->79). This is the g27/g28 mistake for the THIRD straight game. If 戳+1 had been fielded (or 不动金刚阵+1) over 辟邪阵纹... actually sim says sustain-swap doesn't fix the seat. But absorbing keep-list +1s is STILL wrong: those were potential upgrades.
  - 辟邪阵纹 (slot1) = 0-attack 白板 slot — only gives 3 辟邪 + 10 def IF a 持续 was played, which it wasn't. A WASTED SLOT. But sim: swapping it for 不动金刚阵+1 keeps 0% second — only UPGRADES fix the seat.
  WINNER 谭舒雁 rolls/round: 0,0,0,0,0,0,0,0,21,0,0,15,0,11,8,6,6,5 = ~72 (all post-R9, NAMED). 牧逸风 ≈ 65.
  → NEXT-GAME: R1-R9 ≤1-2 rolls (absorb junk). 境5 dumps NAMED + STOP ON HIT. NEVER absorb/roll a KEEP-LIST card OR its +1.

### ★ TOP DISCOVERY [g29]: vs 谭舒雁's 内伤-clock, the answer is ONE MORE BIG-ATTACKER UPGRADE, not sustain and not order.
  ['...','崩拳·连崩+1','...'] (16 ATK finisher) or 撼+2 = 100%/100% vs her exact final board. Upgrading the flag (惊触) does NOT work. Sustain (不动金刚阵) does NOT work. It's a pure t11 ATK-threshold race.
  The whole game was ONE MERGE short (I held 崩拳·连崩 lv1 and had 7 copies in pool; I held 崩拳·撼 lv1 and had 5 copies).
  Reachability: I MERGED 崩拳·撼+1 at R6 (had 2 copies). A 3rd copy = +2. I held 崩拳·连崩 (lv1) at R13. 惊触 (lv1) from R15. ALL were merge-eligible in the endgame; I absorbed 戳+1/不动金刚阵+1 instead.

### ★ SURPRISES:
 1. 谭舒雁 WON the lobby — she was my "EASIEST" matchup in g26 notes and "HARD now" in the g30 note. Her [内伤] clock + HP-stack is a genuine seat-race boss for my burst.
 2. The fix is a SINGLE +1 DOWN TO THE EXACT CARD (连崩/撼/突 work; 惊触 does NOT). Order doesn't save it; sustain doesn't save it; upgrades do.
 3. 牧逸风 fielded a NON-万法 board this game ['邪蛊阵','回响阵纹+1','云舞诀','辟邪阵纹+1','巨鲲灵剑','形意剑','云剑·游龙+1','飞灵闪影剑'] — his 万法 never assembled; my board beat him (W R15 confirms). The lobby's boss shifted to 谭舒雁.
 4. I WON R15 vs 牧逸风 100% but STILL died overall to the seat war vs 谭舒雁.

==== LEDGER ENTRY · Game 30 ====
## ARENA Game 30 — 小布 (sect4 崩拳/气势/身法 burst + 阵法师5), pid3. RESULT: NOT 1st — final 命 0.
WINNER = 谭舒雁 (pid1, 命10). 牧逸风(pid0)/吾行之(pid2)/me all dead 命0.
W/L (19 battles): L R1(pid2) L R2(pid1) L R3(pid0) W R4(pid1) L R5(pid0) W R6(pid2) L R7(pid0) L R8(pid1) L R9(pid2) W R10(pid1) L R11(pid2) L R12(pid1) W R13(pid0) L R14(pid2) L R15(pid0) W R16(pid2) W R17(pid1) W R18(pid1) L R19(pid1). 7W-12L. vs pid0 牧逸风 1W-4L; vs pid2 吾行之 2W-3L; vs pid1 谭舒雁 3W-4L.
FATES: 磨砺不止, 锻体不息, 变换之道, 生机不灭, 休养生息 (economy default — 8th straight confirmation combat/传承 fates irrelevant).
Ended 境5 修为97 maxHP115 体魄9. Gates: 境2@R4 境3@R6 境4@R9 境5@R13.

### ★★★★★ #1 ROOT CAUSE — I WAS ONE *ORDER* AND ONE *SEAT* SHORT. FIX FOUND. ★★★★★
My R19 board: ['崩拳·闪击','威震四方+1','崩灭心法','崩拳·寸劲','崩拳·连崩+1','崩拳·惊触','崩拳·降龙','崩拳·突+1'] (I HAD 连崩+1 — merged it R18).
yisim sim_matchup (12 reps) vs 谭舒雁's EXACT final board ['诸事不宜','厄劫缠身','杯弓蛇影','杯弓蛇影','天星·牵引','星弈·断+1','流水无情','吉运初显']:
  - as-fielded order: 100% going FIRST / **0% going SECOND** (seat-locked, 8-9t). R19 I went SECOND → lost -23命 → dead.
★★★ THE FIX (search_board, pool 5 & 6&7, all agree): **MOVE 崩拳·寸劲 slot4 → SLOT 1.**
  ['崩拳·寸劲','崩拳·闪击','威震四方+1','崩灭心法','崩拳·连崩+1','崩拳·惊触','崩拳·降龙','崩拳·突+1']
  → **100% FIRST / 100% SECOND** vs her exact board (12-rep verified). AND 100/100 vs 牧逸风 AND 吾行之 (base AND +1).
  → A single reorder (costs NOTHING — no merge needed!). This board is UNIVERSAL both seats, the whole lobby.
★ WHY 寸劲@slot1: the board is CYCLIC — 寸劲 (double-[气势] scaling, 10atk + 2×force) firing FIRST on each cycle
  draws on the force banked by the PRIOR cycle's 崩灭心法/威震四方/降龙, landing its huge hit at the TOP of the turn;
  闪击 then sits @slot2 and its [身法]+7 immediately enables the chase into slot3. Putting 寸劲 at slot4 delayed
  the scaled hit into the wrong half of the cycle. SINGLE-CARD ORDER, both-seat swing. (search trace: "move 寸劲 slot4->slot1: 100%/100%".)

### ★★★ #2 — SHE WON THE SEAT WAR DECISIVELY (105 修为 vs my 97). ★★★
Her economy: 勤学苦练 fate = DRAW A CARD ON EVERY ABSORB → absorbing is free card-gen; she ABSORBED EVERY
single junk card every round (R13-19 ~4-5 absorbs/round) and reached 修为105. I reached 97. She went FIRST in
every late round. My pure-economy fates gave no absorb synergy.
→ LESSON (reinforced): the whole g30 lobby is a SEAT WAR. When my board is 100/0 seat-locked, I MUST win 修为.
  Best fix is the BOTH-SEAT board (寸劲@slot1 above) so seat doesn't decide. Second best: OUT-ABSORB her.

### ★ #3 — ECONOMY LEAKS (my rolls/round): R1=1, R7=4, R9=3, R10=2, R12=1, R13=18, R16=10, R17=4, R18=8 ≈ 51.
  - R13=18 at the 境5 gate: rolled AWAY 崩拳·突 and 崩拳·连崩 (re-rolled 连崩 → 百杀破境掌 — a classic keep-list burn).
  - R16=10: landed 崩拳·连崩 (the answer!) then churned 6 more rolls.
  - R18=8: **merged 连崩+1 correctly** (the win-con piece) — good, but then absorbed 崩拳·撑? and ran out of rounds to fix ORDER.
  - UNDER-rolls: I never had a NAMED plan until R13. R1-R12 wasted almost nothing but also BUILT nothing.
  WINNER 谭舒雁 rolls: 0×8, R9=6, R12=17, R14+=0 — SHE ROLLED ~23 TOTAL and absorbed everything else. She
  let the CLOCK KIT come to her via draws, and spent exchanges ONLY on 修为 (which she converted to seat).
  → NEXT-GAME: R1-R12 ≤2 rolls (absorb ALL junk for 修为=seat). Post-境5 ONE NAMED dump for {闪击,连崩,威震四方,寸劲,惊触,突}.
    STOP ON HIT. And CRITICALLY: spend the LAST 2-3 rounds ABSORBING to win 修为, not rolling.

### ★ TOP DISCOVERY [g30]: THE 寸劲-SLOT-1 REORDER FLIPS THE SEAT — FOR FREE.
  My g29 fix (连崩+1) was necessary but NOT sufficient going second vs 谭舒雁. The MISSING piece is putting
  崩拳·寸劲 at slot 1: a zero-cost reorder that turns a seat-locked 100/0 board into 100/100. Reachability: I
  HELD every card; I fielded the WRONG ORDER. This is the g14-g29 [C5] "ORDER IS THE WHOLE GAME" principle
  biting me a FOURTH time. Before every set_board: sim_matchup BOTH SEATS with the CURRENT order — if seat-locked,
  TRY REORDERS (esp. sliding the double-force 寸劲 to slot1 and 闪击 to slot2) BEFORE concluding I need upgrades.

### PER-RIVAL:
- pid1 谭舒雁 (命理师 内伤-clock + HP-stack): 3W-4L. Her clock ~t11-12; both-seat board kills ~t7. The FIX board = 100/100.
- pid0 牧逸风 (云剑/阵法师, g30 fielded a NON-万法 8-card ['聚灵心法+1','百鸟','云剑·无妄','云舞诀','凝意诀','灵犀剑阵','化灵诀','万法归灵剑+1']): 1W-4L. His engine this game was SLOW (万法 last slot, ~t7-8). 100/100 with fix board.
- pid2 吾行之 (水灵 heal-tank 8-card): 2W-3L. Long fight = his win; kill t6-7. 100/100 with fix board.

### SURPRISES:
1. I merged 连崩+1 (the right move!) and STILL lost — because I didn't fix ORDER and didn't win the seat.
2. The fix is a FREE reorder — no merge, no roll. g29 spent 3 search runs concluding "upgrades fix it"; g30 proves
   ORDER ALSO fixes it and ORDER is cheaper. Test order FIRST, upgrades SECOND.
3. 谭舒雁's winner playbook (read in review) independently named the R19 order switch — she uses seat-conditional
   orders (牵引@3 second / 牵引@5 first). SHE also plays the order game. The whole lobby plays the seat war.
4. 修为 97 vs her 98 (SITREP: "TRAIL by 1"). ONE absorb would have tied/flipped the seat. I had 23 exchanges banked
   at the 25-cap and dealt junk I could have absorbed. DO NOT sit at the exchange cap with an un-won seat.
