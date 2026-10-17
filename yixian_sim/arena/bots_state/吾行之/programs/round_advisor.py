"""
round_advisor.py — one-stop per-round decision helper for 弈仙牌.

Usage: python round_advisor.py <round> <my_命> <my_修为> <leader_修为> <alive> [typ_loss_delta]
Prints: must-win verdict, seat-order flag (am I behind on 修为?), 命-margin,
and the recommended board ORDER for the 五行 chase engine (copy-paste ready),
plus reminders for absorb/merge/exchange-cap.

Purpose (from v47 post-mortem): I lost the lobby because (1) 修为 deficit -> went
second nearly every battle, and (2) 五行 board didn't scale vs peaked 崩拳/星弈.
This tool each round forces me to (a) check seat deficit, (b) decide must-win,
(c) field the sim-verified chase engine board in the right order.
"""
import sys, math

def loss_damage(round_no, hp_delta):
    if hp_delta <= 20:
        d = round_no + 1 + math.ceil(hp_delta / 5)
    else:
        extra = min(math.ceil((hp_delta - 20) / 10), 2 + round_no // 2)
        d = round_no + 5 + extra
    if round_no <= 9:
        d -= 1
    return max(d, 1)

# sim-verified best-scaling 五行 chase engine (copy into set_board, cyclic order)
CHASE_ENGINE = [
    "金灵·蓄锐+2", "五行流转+2", "金灵·穿心+2", "金灵·飞梭+2",
    "混元无极阵+2", "金灵·巨鼎落+2", "金灵·巨鼎落+2", "五行天髓诀+2",
]
# early / budget version (what you can actually field before peaks)
CHASE_ENGINE_CHEAP = [
    "金灵·针", "察体", "金灵·飞梭", "五行流转", "混元无极阵",
    "金灵·巨鼎落", "金灵·巨鼎落", "火灵·窜",
]
# HP-cap shred variant vs very tanky opponents
SHRED = [
    "金灵·蓄锐+2", "金灵·穿心+2", "混元无极阵+2", "火灵·瞬燃+2",
    "金灵·飞梭+2", "金灵·巨鼎落+2", "火灵·轰爆", "金灵·巨鼎落+2",
]

def main():
    a = sys.argv[1:]
    rnd = int(a[0]); my = int(a[1]); mycul = int(a[2]); leadcul = int(a[3])
    alive = int(a[4]) if len(a) > 4 else 4
    typ = int(a[5]) if len(a) > 5 else 20

    avg = loss_damage(rnd, typ)
    cat = loss_damage(rnd, 80)
    print(f"R{rnd}: loss dmg typical={avg}  blowout={cat}   my命={my}")
    print(f"  survivable: typical={my/avg:.2f}x  blowout={my/cat:.2f}x")

    # must-win verdict
    if my <= 0:
        print("  >>> DEAD")
    elif my < cat:
        print("  >>> MUST-WIN: one blowout loss = dead. Best board, no gambles.")
    elif my < avg * 2:
        print("  >>> DANGER: two losses kill me. Play to win; economy only if free.")
    else:
        print("  >>> OK margin: can afford a loss; still improve board.")

    # seat-order flag
    gap = leadcul - mycul
    if gap > 0:
        print(f"  >>> SEAT DEFICIT: 修为 {mycul} vs leader {leadcul} (-{gap}). "
              f"ABSORB/MERGE spare cards + breakthrough to overtake before battle.")
    else:
        print(f"  >>> SEAT OK/AHEAD: 修为 {mycul} vs leader {leadcul}. Lock it in.")

    # endgame, lowest-命 flag
    if my < 30 and rnd >= 10:
        print("  >>> LOW 命 late-game: I am the farm target. Bank by WINNING now; avoid being paired into a burst build.")

    print("\nRecommended board (peak chase engine):")
    print("  " + ", ".join(CHASE_ENGINE))
    print("Budget/early board:")
    print("  " + ", ".join(CHASE_ENGINE_CHEAP))
    print("Anti-tank HP-shred board:")
    print("  " + ", ".join(SHRED))
    print("\nReminders: 金灵 must be ACTIVE first (蓄锐/针/印). Field BOARD, then absorb "
          "ALL leftovers + merge dups. End round with exchanges <=22 to keep the grant.")

if __name__ == "__main__":
    main()
