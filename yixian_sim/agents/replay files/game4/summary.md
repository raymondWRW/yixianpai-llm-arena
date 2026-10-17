# Game 4 — 林小月 猫画师剑意 (seed 107, `--ghosts`) — **1st place**, 11W-0D-5L (4 byes), 命 43

Played 2026-08-30 by an Opus agent following `agents/strategy_linxiaoyue.md` plus the
game1/game2/game3 reviews (game3's review treated as binding). Same recorded-bot lobby as
game3: pid1 姜袭明[ai7-lv5], pid2 吾行之[ai4], pid3 慕虎[ai2], pid4 龙瑶[ai5],
pid5 陆剑心[ai7], pid6 炎雪[ai3], pid7 炎尘[ai5].
Files: `log.txt` (365-move exact-state log), `replay.html`.

## Result

- **1st of 8 at 43 命**, still alive at the R20 buzzer. 2nd 龙瑶 18, 3rd 慕虎 6.
- Record: **11W · 0D · 5L · 4 byes** (byes R12, R14, R17, R20 — and every one landed in a
  round where the alternative was a −25-ish loss).
- 命 curve: 100 → 96 (R1 L) → 96 through R7 (six straight wins) → 85 (R8 L) → 63 (R10 L,
  慕虎) → **93** (R12 breakthrough fate 休养生息 +30) → 67 (R16 L) → 43 (R18 L) → 43.
- Elimination order: 炎尘 R11 · 陆剑心 R13 · 吾行之 R13 · 姜袭明 R15 · 炎雪 R15.
- Realm path: 境2 R5 (锻体) · 境3 R6 (机缘造化) · 境4 R9 (灵猫乱剑) · 境5 R12 (休养生息).
  Final 修为 85. **境5 is MAX_REALM in the sim** — 修为 past 55 only buys turn order.
- Final board (cyclic, R20): 百鸟灵剑诀+2 → 巨鲲灵剑+1 → 飞灵闪影剑+1 → 巨鲲灵剑 →
  万法归灵剑+1 → 云剑·游龙 → 飞灵闪影剑 → 化灵诀 (sim **+28 vs 龙瑶**, −37 vs 慕虎).

## How the guide's phase plan went

- **Phase 1 (R1–R5) — the guide's target board was assembled EXACTLY, one round early.**
  By R5: 剑劈+2 (lv3) · 剑挡+1 · 灵气灌注+1 · 飞牙剑+1 ×2 · 震雷剑+1, with 猫薄荷 banked
  since R2. The only miss vs the guide was **剑挡 never reaching lv3** (pool ran to 1 copy).
  The build came online at R4: **+7.9 avg, 7/7 wins**, and R4–R7 were four straight wins
  worth +8/+11/+11/+14.
- **Broke phase 1 at R5** (guide window R5–6) with 修为 16 vs a gate of 9.
- **Roll hoard held through phases 2–4 exactly as the game3 review demands.** R6–R11 spent
  only [置换] freebies (练笔). Rerolls climbed 4 → 26 by the 境5 breakthrough at R12.
  R11 was the "it is okay if we lose this round" round: the board had fallen to +3.6 and the
  hoard was NOT broken. That is the single biggest difference from game3.
- **猫薄荷 timing: perfect, four times.** Catnip #1 (R9) landed on 灵猫乱剑 with a
  *guaranteed* hit — at that moment 灵猫乱剑 was the only lv1 猫 card in hand-or-board.
  #2–#4 (R13, R13, R15) were farmed in phase 5 and each was aimed by first absorbing every
  rival lv1 card: → 化灵诀+1, → 飞灵闪影剑+1, → 形意剑+1.
- **Phase 5 (R12–R20): the hoard paid.** 26 charges bought 万法归灵剑 (x2 → merged +1),
  飞灵闪影剑, 云舞诀, 凝意诀, 形意剑, 剑意激荡, 百鸟灵剑诀+1 (x2 → merged **+2**),
  巨鲲灵剑+1 — i.e. the entire late-game deck. The R13 board jumped from **−21.2 → +6.8**
  in one round on the back of 万法归灵剑+1 alone.

## 好奇心 usage (9/9 triggers, all consumed)

1. **R2, trigger #1 → 猫薄荷 on the first try.** Then STOPPED, per the game1 ruling
   (farm only until the first catnip, bank the rest). Triggers 2–9 sat unused for ten rounds.
2. **Triggers 2–9 all spent in phase 5 (R12–R16)** at a standing cost of 0 charges
   (a trigger fires at exactly 1 charge and refunds +1). Yield: **猫薄荷 x3**, 狼皇血晶
   (the 10% 法宝/灵宠 branch — see bugs), 青铜猫, 小鱼干, 云剑·飞砂 x2.
3. Banking the triggers **paid this game**, unlike game3: three phase-5 catnips converted
   directly into three board upgrades (化灵诀+1, 飞灵闪影剑+1, 形意剑+1).

## The game3-review corrections, and how each played out

| Correction | Outcome |
|---|---|
| **R1: roll twice — 好奇心 only fires on the LAST charge; roll junk like 云剑·飞刺** | Done exactly. Rolled 云剑·飞刺 → 轻剑, then 轻剑 → **震雷剑**. R1 board 轻剑·剑挡·震雷剑 simmed **+1.6 / 5-of-7** where game3's R1 was −5.1 / 0-of-7. Still lost R1 (−4), but a 4-命 loss instead of 5. |
| **飞牙剑 goes BETWEEN 剑意 generators and multi-hit cards** | Held through phases 1–3. The R4/R5/R7 boards were literally 剑劈 · 剑挡 · (qi) · 飞牙剑 · 飞牙剑 · 震雷剑/三峰剑 — R7's version scored **+13.0, 7/7**. |
| **Watch the qi budget** | Checked every board by hand (gen >= spend) before simming. One deliberate exception, noted below. |
| **Only 2 copies of 飞牙剑; merge two lv2s into a lv3 when a third appears** | Kept 2 separate lv1s at R3 (the review's move-17 ruling), then at R5 four lv1s arrived at once → merged into exactly **two 飞牙剑+1**. A third lv2 never appeared, so no lv3 merge was needed. |
| **Do not merge 剑挡 to lv3 while the core is missing** | Followed; 剑挡 stayed at +1 all game and the pool dried up. Minor cost. |
| **Phase 4: do NOT roll; save every roll for phase 5** | Followed to the letter. Zero non-[置换] rolls between R6 and R11 inclusive. |
| **境4 天命 = ALWAYS 灵猫乱剑, eat other lv1 猫 first, then 猫薄荷** | Done at R9; log shows the deterministic `fx 猫薄荷[炼化]: 升级1级牌 灵猫乱剑`. |
| **Hold >=3 hand cards once 灵猫乱剑 is fielded** | Followed from R9 on; decisive at R12 (a 6-card board with 3 in hand scored **−6.0** vs a 7-card board with 2 in hand at **−13.0**). |
| **Keep 连环剑阵 / 御空剑阵 for defence** | **Failed.** 连环剑阵 was found twice at R12 and rolled away both times (dead without a partner 剑阵); 御空剑阵 appeared once at R19 and was rolled away by an automated hunt whose keeper list omitted it. |
| **慕虎 is a poor matchup — do not bleed extra 命 into it** | Lost to 慕虎 at R1 (−4), R10 (−22) and R16 (−26). But R19 found a counter (below). |

## The 慕虎 counter that showed up at R19

Every board built on 剑意 payoff lost to the 土灵 wall by 60–130 HP. The board that finally
beat it **+25** contains no sword-intent card at all:

    飞灵闪影剑+1 · 飞灵闪影剑 · 化灵诀+1 · 百鸟灵剑诀+2 · 暗鸦灵剑 · 画饼充饥 · 灵气灌注+1 · 万法归灵剑+1

It is a pure **qi bomb**: five qi sources (化灵诀+1 = 4, 百鸟灵剑诀+2 = 3 plus *灵剑 cost −2*,
画饼充饥 = 2, 灵气灌注+1 = 3, plus 1 qi per injuring hit from the two 飞灵闪影剑) all feeding
**万法归灵剑+1 (5攻, exhaust qi, +6攻 per point)**, with **灵气灌注+1 parked immediately before
it so the single huge hit is [无视防御]**. That adjacency is the whole trick against a defence
wall — one un-blockable 60–90 damage hit instead of a hundred small blocked ones. The same
shape (with 巨鲲灵剑+1 x2 for [再次行动] free actions) scored **+28 vs 龙瑶** at R20.

## Deviations from the guide (with reasons)

1. **境2 天命: 锻体 (+5 max HP) instead of 剑阵传承 (a free 剑阵 card).** Not a choice — my
   `break` preference list (4/53/12/45) contained none of the four offered fates, so the
   default scorer picked. **Process error**: always pass a long preference list. 剑阵传承
   would have given the 御空剑阵/连环剑阵 defence package the guide asks for.
2. **境5 天命: 休养生息 over 灵猫踏云.** Again the default scorer (my list was 16/4/45/116/…,
   none offered). Hugely lucky: **+30 命** exactly when I was bleeding 20/round, and it is
   why I finished at 43 instead of 13.
3. **R14 道韵: 自在随心 over 剑意激荡.** My daoyun preference list *did* contain 剑意激荡
   (1000044) and the offer *did* include it — but the preference silently did not reach the
   chooser (bug 1). A genuine loss.
4. **剑意激荡 was later found by rolling (R14) and then ABSORBED (R15).** Every board
   containing it tested byte-identical to the board without it, because at 9–12-turn battles
   only ~5 of my card plays ever happen and it never sat in slots 1–5. Absorbed for 修为 +
   catnip determinism. Contradicts the guide's "premium card" label; the reason is the turn
   budget, not the card.
5. **灵气灌注 was dropped from the board at R11 and R17–R18** (game3 hit the same wall) but
   returned as the *keystone* of the R19–R20 qi-bomb board. Its [无视防御] line is worth far
   more adjacent to one giant hit than sprinkled among small ones.
6. **From R12 the board stopped being a 剑意 board.** 剑劈+2 / 剑挡+1 / 震雷剑+1 / 三峰剑+1 /
   飞牙剑+1 all fell out in favour of 万法归灵剑+1 · 飞灵闪影剑+1 · 百鸟灵剑诀+2 · 巨鲲灵剑+1.
   Sword intent stops scaling against 境5 ghost decks; the qi-exhaust bomb does not.
   灵猫乱剑+1 stayed fielded through R15 and was benched from R17 (it tested neutral).
7. **修为 was deliberately NOT pushed after R18.** Measured directly: acting FIRST was
   *worse* for me (vs 慕虎 −32 as first mover vs −25 as second; vs 龙瑶 −32 vs −24), because
   these decks out-damage mine and moving second buys extra turns. So I stopped absorbing at
   修为 83–85 to stay below 慕虎 (91) and 龙瑶 (92). **This inverts game3's R17–R20 advice of
   absorbing for initiative** — buy initiative only when you are the faster killer.
8. **R11 board ran a qi deficit on purpose** (凝意诀 gen 1 vs 飞牙剑 x2 spend 2) because
   swapping 灵气灌注+1 → 三峰剑+1 tested +3.6 vs −0.5. A knowing exception to the qi-budget
   rule; multi-hit bodies that cost no qi can be worth a starved slot.

## Endgame play (R18–R20) — the part that won the game

At R18 the standings were 龙瑶 51 · me 43 · 慕虎 31, no board could beat either survivor
(best average −24.5), and four rounds of −25 would have killed me. What won it was reading
`env._pair`: **pairing avoids each player's immediate-previous opponent when the pool allows.**

- After R18 (me vs 龙瑶) the only possible R19 pairings were *me vs 慕虎* (2/3) or
  *龙瑶 vs 慕虎* (1/3) — I could not face 龙瑶. So I built a board optimised **only against
  慕虎** (+25 / −35 split, average −5.0 instead of −25.5) and won R19 +25.
- After R19 (me vs 慕虎) the only R20 pairings were *me vs 龙瑶* (1/3) or *龙瑶 vs 慕虎*
  (2/3, me bye). So I built a board optimised **only against 龙瑶**: +28 / −37.
- Deliberately did **not** try to kill 慕虎 at R19 (+25 left him at 6). A live 慕虎 is a bye
  generator and the only deck in the lobby that beats 龙瑶. It paid exactly: R20 was
  慕虎 vs 龙瑶, 慕虎 won **+33**, 龙瑶 fell 51 → 18, I took the bye at 43 and won.

Generalisable rule: **with 3–4 players left the next pairing is nearly determined by
`last_opp`. Optimise the board against the opponent you can actually be paired with, not
against the average.** A specialised board was worth ~20 命/round here.

## Bugs / suspicious behaviour (reported, not fixed)

1. **`play.py` fate/道韵 preferences silently stop working if any helper script imports
   `play` as a module and re-saves the state.** The env pickles `fate_chooser` /
   `daoyun_chooser` / `sidejob_chooser` by reference. Running `play.py` as a script binds
   them to `__main__.*`; a helper that does `import play` and `PL.save(st)` rewrites them to
   `play.*`. On the next `play.py` run the chooser then reads `play.PREFS` while `load()`
   updates `__main__.PREFS` — two different dicts — so every preference is ignored and the
   log prints "(default scorer)". **This cost 剑意激荡 at the R14 道韵.** Suggested fix: read
   prefs off `st`/`env` rather than a module global. (Workaround used: force
   `__module__ = "__main__"` on the three functions before saving.)
2. **`break` reports a nonsense error at the realm cap.** At 修为 75 / 境5 it printed
   `cannot break: 修为 75 < 75`. `E.MAX_REALM = 5`, so the realm is capped, but the driver
   prints `CULT_REQ[realm+1]` regardless; `show` likewise advertises "next gate 75" forever.
3. **`休养生息` gave +30 命 although its text says [命元]+14.** 63 → 93 at the R12
   breakthrough. Either the fate scales with realm (undocumented) or it is applied twice.
4. **The 好奇心 10% 法宝/灵宠 branch fired once (狼皇血晶, R12)** — so the pool is not
   phase-blind, confirming game3's post-game triage. Note for future agents: automated
   roll-hunt loops must include 法宝/灵宠 names in their keeper list or they will roll the
   rare branch straight back into the pool (that happened here).
5. **The 8th board slot is frequently a no-op — and from R14 on, so are slots 6–8.** Boards
   differing only in slots 6–8 returned byte-identical sims (battles ran 9–12 turns → ~5 of
   my plays). Extends game3's finding #5: at 境5 against these decks **only the first ~5
   slots exist**. Corollary: never spend a card on slot 7–8 that could be absorbed for 修为
   or held for 灵猫乱剑.
6. **`!! hand over 16` fired once (R20)**, dropping 化灵诀+1 / 暗鸦灵剑 / 画饼充饥 /
   灵气灌注+1. The guard works and logged correctly; the hand had grown to 20 from heavy
   phase-5 rolling. Not a bug, but a reminder to absorb down before ending a round.
7. Still open from game2/game3: `merge` exits 1 on a missing second copy (kills `&&` chains),
   and `roll` on a board card warns but continues the rest of the argument list.

## Rules confirmed working in play

- [置换]-before-好奇心 ordering (练笔 rolled at 1 charge refills without burning a trigger).
- 好奇心 triggers are charge-free: fire at exactly 1 charge, refund +1, so all 9 can be
  farmed back-to-back in a single round at zero standing cost.
- 猫薄荷 targets lv1 cards in **hand or board**, 猫-name first — clearing rival lv1s (or
  rival 猫 cards) beforehand makes it deterministic. Verified four times.
- 机缘造化 (fixed) granted 灵宠认主, and rolling that granted a 灵宠 (胖仙狸) in place of the
  normal draw. 以画入道 granted 境5 sect cards; 妙笔生花 granted 百鸟灵剑诀+1 and 云剑·闪风+1;
  触类旁通 granted a sidejob card **and** +1 charge. All [置换] grants replaced the draw with
  no pool burn, as specified.
- `sim` now seats the higher-修为 side first (game3's fix) — which is what made the
  "do not chase initiative" measurement above possible.
- Byes log explicitly (`R{n}: BYE (no opponent this round)`), four times, correctly.
- 灵猫乱剑 hand-count bonus is modelled and matters: caps at +3, and the 3rd hand card is
  worth much less than the 2nd (matching game2's −12/−10/+11/+12 curve).

## Post-game triage of the bugs (2026-08-27)

1. **PREFS lost after helper re-save — FIXED.** Choosers now read preferences off
   `env.prefs` (set on every save/load); the `__main__.*` vs `play.*` pickle
   rebinding can no longer point them at an unloaded module-global dict.
2. **Realm-cap messages — FIXED.** `break` at 境5 now says "already 境5 (MAX
   realm)" and `show` prints "(MAX realm — 修为 past here is inert)" instead of
   silently dropping the gate.
3. **休养生息 +30 — NOT a bug.** Fate magnitudes scale with the breakthrough
   phase (v0=境2 … v3=境5); its 境5 version is 命元+30. Only the offer line
   shows the base (+14) text — display-only.
4. Slots 6–8 dead at 境5 / curiosity 10% branch / hand-16 guard — informational,
   playbook notes stand. CLI exit-code quirks still open (game2 item 4).
