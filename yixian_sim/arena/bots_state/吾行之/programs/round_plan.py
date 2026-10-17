"""
round_plan.py — the analysis helper I wish I'd had each round.

Answers: "Am I safe to play economy this round, or must I field a must-WIN board?"

Usage:
  python round_plan.py <round> <my_命> <leader_命中> <n_alive> [typical_loss_est]

It prints:
  - loss damage for an average and a catastrophic (hp_delta>20) loss this round
  - how many such losses I can absorb
  - a MUST-WIN / can-afford-loss verdict
  - a warning if I'm the LOWEST 命 in the lobby (endgame = target on my back)

Destiny formula verified against gamestate_full.js:1619.
"""
import sys, math

def loss_damage(round_no, hp_delta):
    if hp_delta <= 20:
        d = round_no + 1 + math.ceil(hp_delta / 5)
    else:
        extra = math.ceil((hp_delta - 20) / 10)
        extra = min(extra, 2 + round_no // 2)
        d = round_no + 5 + extra
    if round_no <= 9:
        d -= 1
    return max(d, 1)

def main():
    a = sys.argv[1:]
    rnd = int(a[0]); my = int(a[1]); leader = int(a[2])
    alive = int(a[3]) if len(a) > 3 else 4
    typical = int(a[4]) if len(a) > 4 else 20  # hp_delta for "typical" loss

    avg = loss_damage(rnd, typical)
    cat = loss_damage(rnd, 80)  # big blowout
    print(f"R{rnd}: loss dmg typical={avg}  blowout={cat}")
    print(f"  my 命={my}. losses survivable: typical={my/avg:.2f}  blowout={my/cat:.2f}")
    gap = leader - my
    print(f"  命 gap to leader = {gap}  (leader {leader})")
    if my <= 0:
        print("  >>> DEAD")
    elif my < cat:
        print("  >>> MUST-WIN: a single blowout loss is lethal. Best board, no gambles.")
    elif my < avg * 2:
        print("  >>> DANGER: two losses kill me. Play to win; economy only if free.")
    else:
        print("  >>> OK margin: can afford a loss; still improve the board.")
    if my == min(my, leader) and alive > 1:
        # heuristic: if I'm not clearly ahead, I'm a target
        if my < leader:
            print("  >>> I am BELOW the leader — need to close the gap NOW by winning.")

    # expected 命 remaining if I lose every remaining round (worst case)
    print("\nWorst-case survival (lose EVERY future round), from today:")
    hp = my; r = rnd; killed_round = None
    while r < 30 and hp > 0 and alive >= 2:
        d = loss_damage(r, 40)
        hp -= d
        if hp <= 0 and killed_round is None:
            killed_round = r
        r += 1
    print(f"  dies around R{killed_round}" if killed_round else "  survives to the cap")

if __name__ == "__main__":
    main()
