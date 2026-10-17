"""
Board audit helper.
Usage: run_program("board_audit.py", ["card1","card2",...])
Given a list of card names (as fielded in cyclic order), prints:
 - count, rough ATK/DEF/Qi/Force tags per card via a small keyword table
 - flags cards that are *consumable* (画龙点睛 [消耗]) or [持续]/setup openers
 - a heuristic "front load" note: setup cards should be early, payoff cards late.
This is a heuristic *planning* aid; ALWAYS confirm with simulate().
"""
import sys

# crude keyword tags for the Crash-Fist / Force archetype and common utility
TAGS = {
    # ATK values by base card (lv1); +1 level roughly +base*0.4 but keep simple
    "崩拳·降龙": ("ATK10", "buff:next-crash-fist +DEF/+ATK", "SETUP"),
    "崩拳·突":   ("ATK10", "碎防 pierce", "PAYOFF"),
    "崩拳·惊触": ("", "crash-fist", "PAYOFF"),
    "崩拳·撼":   ("", "crash-fist", "PAYOFF"),
    "崩灭心法":  ("Force+2", "[持续]: +1 Force per HP-cost card", "SETUP"),
    "画龙点睛":  ("upgrade next 3", "[消耗] consumable", "OPENER"),
    "夜鬼啸":    ("ATK14", "ignore DEF", "PAYOFF"),
    "气若悬河":  ("Qi+2 Force+1", "+1 Force during next 2 atks", "SETUP"),
    "崩拳":      ("crash-fist", "", "PAYOFF"),
}

def tag(card):
    base = card.split("+")[0]
    return TAGS.get(base, ("", "", ""))

def main(cards):
    print(f"Board size: {len(cards)}")
    setup = 0; payoff = 0; consumable = 0
    for i, c in enumerate(cards):
        atk, extra, role = tag(c)
        lvl = "+" + c.split("+")[1] if "+" in c else "lv1"
        if "消耗" in extra:
            consumable += 1
        if role == "SETUP" or role == "OPENER":
            setup += 1
            if payoff > 0:
                print(f"  !! slot {i}: SETUP '{c}' comes AFTER a payoff card -> suboptimal order?")
        if role == "PAYOFF":
            payoff += 1
        print(f"  slot {i}: {c:18s} {lvl:4s} {atk:7s} {extra}  [{role}]")
    print(f"\nsetup={setup} payoff={payoff} consumable={consumable}")
    if setup == 0:
        print("WARN: no setup card -- crash-fist payoffs will be weak.")
    if consumable:
        print(f"WARN: {consumable} consumable card(s) -- they DON'T return after battle; keep backups.")
    print("\nRule of thumb: OPENERS/setup first, PAYOFFS last, cyclic so board loops.")

if __name__ == "__main__":
    main(sys.argv[1:])
