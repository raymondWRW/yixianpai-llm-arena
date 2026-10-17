# Game 1 — 林小月 猫画师剑意 (seed 42) — 1st place, 20-0, 命 102

Archived from `agents/mygame/` on 2026-08-24. Files: `log.txt` (full action log with
exact-state sync lines), `replay.html` (292-move interactive replay), `review.md`
(the user's round-1-4 review — READ IT before playing again).

Final board (cyclic): 剑劈+1 → 剑挡+1 → 凝意诀+1 → 剑意激荡+1 → 青铜猫+1 → 飞牙剑+1 →
飞灵闪影剑+1 → 云剑·猫爪+1. Kill in 14 turns, +33 命/round by the end.

## Bugs this game exposed (both fixed after)

1. **Move 41**: 练笔 rolled on the LAST charge triggered both 练笔[置换] and 好奇心.
   Wrong — the [置换] effect resolves FIRST, the refilled charges mean 好奇心 does not
   trigger. Fixed in `env.reroll`.
2. **+2 max HP per round** was missing entirely: every player gains +2 max HP at each
   round start from R2 (R1=40, R2=42, …). Fixed in `economy.passive_hp` +
   `env.play_round` + `play.py begin_round`.

## The user's play review (full text in review.md) — key rulings

- **Roll the weakest card, not the most convenient**: 轻剑 (+1 qi) fuels 飞牙剑 — it was
  wrong to roll it while 云剑·厚土 sat in hand. Qi sources (轻剑/护身灵气/调色/化灵诀)
  are build infrastructure, never roll fodder while 飞牙剑 lacks fuel.
- **好奇心 discipline**: farm triggers only until the FIRST 猫薄荷, then stop — bank the
  remaining triggers for phase 5. Wasting them on phase-1 junk (moves 8/24/39) threw
  away late-game 法宝/灵宠 value.
- **猫薄荷 is FOR 灵猫乱剑**: hold it (don't absorb) until the 境4 fate grants 灵猫乱剑,
  so the upgrade lands on the key card (move 51 was wrong).
- **Never roll core build cards**: 剑劈/剑挡/飞牙剑, and 骤风剑 (the ×2-attack 剑意
  payoff until 震雷剑 shows up). Move 37 (rolling a 剑劈) was an outright error.
- **Absorb vs roll**: with key cards still missing (灵气灌注/震雷剑), spare cards should
  be ROLLED to hunt them, not absorbed for 修为 (move 47).
- **Breakthrough is a choice, not a reflex**: staying 境1 keeps the pool small and the
  core cards findable — at move 48 the right play was to NOT break yet.
- **Don't merge off-build cards**: merging 云剑·极意 (move 64) wasted two roll targets;
  roll both copies away hunting build cards instead.
