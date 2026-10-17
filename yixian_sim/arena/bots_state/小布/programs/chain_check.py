"""
Crash-Fist (崩拳) board CHAIN CHECKER for 弈仙牌.

Usage: run_program("chain_check.py", ["崩天步","崩拳·缠+1",...,"崩拳·惊触"])

Encodes the CONFIRMED mechanics learned the hard way:
 - 崩天步 must be slot 1 (makes every card count as 崩拳).
 - setup cards (缠/戳/突/察体) buff the NEXT crash fist -> should precede a payoff.
 - 惊触 (finisher) should be LAST in the cycle so hp_lost is max when its bonus fires.
 - flags FILLER cards that don't advance the chain and aren't DEF/Qi (the v38 bug:
   势大力沉 needs Qi; 劈山掌 costs HP -> warned explicitly).
Prints an ORDER SCORE and concrete fixes. Heuristic only -- ALWAYS confirm with simulate().
"""
import sys

# card -> (role, notes)
ROLE = {
    "崩天步":   ("OPENER", "MUST be slot 1: every card becomes 'crash fist'"),
    "崩拳·缠":  ("SETUP",  "next crash-fist: +Wound (DoT, ignores DEF)"),
    "崩拳·戳":  ("SETUP",  "next crash-fist: +ATK"),
    "崩拳·突":  ("SETUP",  "self+next crash-fist: SMASH DEF (pierce)"),
    "察体":     ("SETUP",  "[opening] next attack smash-def + next ATK card +8"),
    "崩拳·惊触":("FINISH", "scaling bonus hit = 1+hp_lost/5 AFTER next crash fist"),
    "崩拳·降龙":("PAYOFF", "big crash fist"),
    "崩拳·撼":  ("PAYOFF", "Force spender -- needs a Force engine"),
    "势大力沉": ("FILLER?", "needs 1 Qi to be good -- only if you have a Qi engine"),
    "劈山掌":   ("FILLER?", "costs HP (feeds 惊触) but shrinks your HP pool"),
}
DEFKEY = ("护", "御", "盾", "甲", "罡", "灵甲", "周天", "反身")  # rough DEF/shield names


def base(c):
    return c.split("+")[0]


def main(cards):
    if not cards:
        print(__doc__); return
    score = 100
    notes = []
    seen_opener = False
    for i, c in enumerate(cards):
        r, n = ROLE.get(base(c), ("?", "unknown"))
        print(f"  slot {i}: {c:16s} [{r}] {n}")
        if i == 0 and base(c) != "崩天步":
            score -= 15
            notes.append(f"slot0 is '{c}', expected 崩天步 -> chain bonuses may not fire.")
        if base(c) == "崩天步":
            seen_opener = True
            if i != 0:
                score -= 20
                notes.append("崩天步 NOT first -> will not open the chain.")
        if r == "FILLER?" and not any(k in c for k in DEFKEY):
            has_qi = any("气" in x or "灵气" in x for x in cards)
            if base(c) == "势大力沉" and not has_qi:
                score -= 6
                notes.append(f"'{c}' filler with no Qi engine -- cut it.")
            elif base(c) == "劈山掌":
                score -= 4
                notes.append(f"'{c}' costs HP -- only if you WANT tanky 惊触 scaling.")
    if not seen_opener:
        score -= 25
        notes.append("No 崩天步 -> this is NOT a crash-fist chain board; scrap the plan.")
    # 惊触 last check
    fin = [i for i, c in enumerate(cards) if base(c) == "崩拳·惊触"]
    if fin and fin[-1] != len(cards) - 1:
        score -= 10
        notes.append("惊触 not last -> its scaling bonus fires too early (low hp_lost).")
    # any SETUP after a PAYOFF/FINISH in the cycle -> wasted
    seen_pay = False
    for c in cards:
        r = ROLE.get(base(c), ("?", ""))[0]
        if r in ("PAYOFF", "FINISH"):
            seen_pay = True
        elif r == "SETUP" and seen_pay:
            score -= 8
            notes.append(f"SETUP '{c}' after a payoff wraps the cycle oddly; consider reorder.")
    print(f"\nORDER SCORE: {score}/100")
    for n in notes:
        print("  -", n)
    print("\nREMINDERS: (1) act-last kills you -> raise 修为 (merge/absorb).")
    print("           (2) RE-SIM every round vs each opponent's LAST board + an upgrade.")
    print("           (3) high rounds: a loss can be fatal -> only field boards that WIN sim.")


if __name__ == "__main__":
    main(sys.argv[1:])
