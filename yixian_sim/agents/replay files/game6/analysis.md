# Game 6 — mechanism analysis (Claude, 2026-09-05)

Method per the user's directive: instead of reading Oracle verdicts, each key
battle was traced against `agents/combat_rules.md` (yisim-derived), hypotheses
formed from the trace, then tested with single targeted Oracle counterfactuals
(one change at a time). Fixture fidelity check: rebuilding the R14 battle from
the log + ghost data reproduced the recorded result exactly (−20, 12 turns).

## 1. The R14 loss to 慕虎 was self-inflicted — two separate one-change fixes flip it

Actual R14 board (8 slots): 云剑·游龙 · 剑劈+2 · 凝意诀 · 剑挡+2 · 剑意激荡(lv1) ·
灵猫乱剑+1 · **剑劈(lv1) · 流云乱剑+1** ← dead tail. Result −20 in 12 turns.

| change (everything else identical) | result | kill turn |
|---|---|---|
| actual | **−20** | 12 (he kills me) |
| drop the two dead slots (6-card board) | **+28** | 10 (I kill him) |
| 剑意激荡 lv1 → lv3 | **+28** | 9 |
| both | +28 | 10 |

Diagnosis: with 8 slots the cycle is 8 long, so the SECOND pass through
激荡→灵猫乱剑 (the pass with the big multiplied bank) arrives ~2 turns later —
after 慕虎's 山崩 nuke instead of before it. The dead tail wasn't neutral
filler; it was the two turns that let his bomb go off first. The agent's own
summary claimed "compression needs 剑意激荡" from its R10 (境4) measurement and
over-generalized it: at R14 it HAD 激荡 fielded, and compression alone was
worth **±48 命**. Rule sharpened: *once 剑意激荡 is on the board, every slot
that isn't part of the chain is a turn donated to the opponent's setup.*

## 2. Anatomy of the 慕虎 wall (why it beats intent decks, from the card texts)

His R14–R16 list: 锟铻金环 · 土灵阵+2 · 金灵·飞梭(×2) · 土灵·断崖+2 · 运笔如飞 ·
土灵·绝壁+2 · 土灵·山崩 (·土灵·流沙).

- **锟铻金环**: permanently [激活土灵]+[激活金灵] (all his element riders always
  on — the 连-chain rule never gates him) AND +2 on **every** 防 gain. The wall
  is ~25% thicker than card text.
- **土灵阵+2** [持续]: +4(+2) 防 on every 土灵 card — every wall card pays twice.
- **土灵·断崖+2**: 防+20, and the NEXT time his 防 decreases, the decrease is
  dealt to me as damage. Verified in the engine: the decay path routes through
  `reduce_idx_def`, which fires the reflect — so it triggers on *any* 防 loss,
  his own start-of-turn halving included. Consequence: whether my burst or his
  own decay consumes the armed reflect is pure TURN ALIGNMENT — this is a big
  part of why the seat swings this matchup so hard.
- **土灵·绝壁+2**: +1 防 per 4 防 *cumulatively lost* — he profits from his own
  decay and from every point I chew. Long fights literally feed him.
- **土灵·山崩**: halves his own 防, +3 ATK per point lost — the wall is a
  battery for a one-turn ~40–60 damage bomb, arriving roughly turns 9–12.

So 慕虎 is not a siege target, he is a RACE: land the multiplied 灵猫乱剑 burst
before 山崩, and don't chew big 防 while 断崖's reflect is armed.

**The seat flip, quantified** (R16 boards, everything identical): me second
**+28 (kill turn 14)**, me first **−28 (dead turn 9)**. A ±56 命 coin decided
by whose burst/bomb/reflect windows align. My hand-trace gets the first ~8
turns confidently but cannot pin the exact turn-9 death chain without a
turn-by-turn battle log from the Oracle — that is the missing tool (see §5).

## 3. The 陆剑心 losses (R13 −26, R15 −18): the popular theory is wrong

Theory from the game record: "absorbing 云剑·猫爪 at R9 left no pierce attacker,
which is why the walls beat me." Counterfactual: replace 凝意诀 with
灵气灌注+1 (restoring an [无视防御] feed) in the actual R15 board → result
**unchanged** (−28 both ways, his HP margin barely moves).

The trace explains why: 陆剑心's deck isn't a wall I fail to crack — it's a
faster engine. 聚灵心法+2 prints qi every turn; **水月剑阵+1 stops his 防 from
decaying for 4 of his turns**, which turns 镜花剑阵+2 ("attack = your current
防") into a repeating ~25–35 damage hit off UNDECAYED 防; 白鹭灵剑/云剑·点星
convert leftover qi into attack. Pierce on my side doesn't slow any of that
down. What actually beat him at R16 was 剑意激荡+2 making MY clock faster
(+31 vs his R15 list), not any defensive tweak. Lesson: against 水月+镜花
engines, fix your kill turn, not your penetration.

## 4. Fog losses were mostly tempo losses in disguise

R3/R9/R13/R15 all pattern the same way: the ghost's board added exactly one
scaling piece (剑劈 lv-up, 水灵·春雨, 聚灵心法+2, 聚灵丹+1) that moved THEIR
kill turn one turn earlier, while the sim scored last round's slower version.
A robust-board policy helps, but the tracing view is sharper: when your own
kill turn is 9–10, a one-card upgrade on their side matters only if it moves
their clock to ≤ your clock − (seat). R16–R19's minimax boards won precisely
because their kill turn (9–10) was faster than anything the survivors' NEXT
board could plausibly reach — robust in the clock sense, not the margin sense.

## 5. Tooling gap this analysis hit

Hand-tracing resolved every mechanism except exact multi-chase death chains
(the turn-9 first-seat death vs 慕虎). The Oracle returns only
(lifeDamage, hpDelta, turns). A per-turn battle log (card played, damage, 防,
HP per turn) from the fixture runner would make every future trace checkable.
The engine already logs internally under ORACLE_DEBUG_XS-style flags — worth
exposing a `--battle-log` in a future session (user approval needed).

## 6. Rules for the playbook (proposed, pending user review)

1. Once 剑意激荡 is fielded (境5), cut every non-chain slot immediately — a
   dead tail slot ≈ ±20–50 命 vs bomb decks (measured, §1).
2. 慕虎-type walls: race the 山崩 bomb. Prefer whichever seat lands your burst
   turn strictly before his turn-9–12 nuke; his 断崖 reflect means never chew
   30+ 防 in one card while it is freshly armed if you can pop it with a small
   hit (普通攻击/游龙) first.
3. 水月+镜花 engines (陆剑心): pierce doesn't help; only a faster kill turn or
   the seat does. If your clock can't beat theirs, minimize the loss (even 命,
   慈念曲-class tools) instead of tuning the board ±2.
4. The sim reproduces recorded battles exactly from ghost fixtures — when a
   result surprises you, rebuild it and run one-change counterfactuals before
   drawing a lesson (this is how §1's real cause was found; the first theory
   was wrong).

## CORRECTION (2026-09-15, after game7)

§1's counterfactuals B–D were built with UNPADDED fixtures (6 usedCards ⇒ the
engine cycled at 6). The driver — and, per the stall rulings, the real game —
pads unfielded slots with 普通攻击, which are real attacks that SPEND the 剑意
bank. With padding, "dropping the dead tail" means swapping two junk cards for
two bank-burning normal attacks, and game7 measured the 8-card board BETTER by
~16 命 at its R12. §1's diagnosis (the R14 tail delayed the second burst) may
still hold directionally, but the ±48 magnitudes are unreliable; the 激荡
lv1→lv3 counterfactual (same slot count, +48) is the trustworthy one. True
compression = [消耗] + [再次行动] only. The playbook has been corrected.
