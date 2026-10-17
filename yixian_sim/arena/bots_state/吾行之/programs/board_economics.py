
# Helper: compute 命-margin risk for endgame decisions.
# Loss damage scales with round number; late-game one loss can be lethal.
# Use this to decide: aggressive (must-win) vs safe (acceptable loss) rounds.
#
# Inputs (edit and run): current 命, round#, typical loss dmg seen so far.
# Output: how many losses of that size I can survive, and flags.

def survive_margin(hp, loss_dmg):
    if loss_dmg <= 0:
        return float("inf")
    return hp / loss_dmg  # number of losses survivable

def assess(round_no, my_hp, opp_hps, my_shouwei_lead, typical_loss):
    # opp_hps: dict pid->命 ; my_shouwei_lead: True if I act first (highest 修为)
    losses_left = survive_margin(my_hp, typical_loss)
    dead_opps = [p for p, h in opp_hps.items() if h <= 0]
    alive = [p for p, h in opp_hps.items() if h > 0]
    print(f"R{round_no}: 命={my_hp}  typical_loss={typical_loss:.0f}  "
          f"losses_survivable={losses_left:.2f}  alive_opps={len(alive)}  "
          f"go_first={my_shouwei_lead}")
    if losses_left < 1:
        print("  >>> CRITICAL: ANY loss is lethal. Field a must-WIN board; "
              "sim vs ALL likely opponents, pick best expected board.")
    elif losses_left < 2:
        print("  >>> DANGER: one loss leaves no margin. Play to win this round.")
    else:
        print("  >>> OK margin. Can afford a loss; still optimize, prefer "
              "general-power board over narrow counter.")

# Endgame with 3 alive: odd-one-out fights an EXTRA battle (only they risk 命).
# This means with odd player count, being the extra fighter is extra risk ->
# keep 命 margin for the possibility of fighting twice.

if __name__ == "__main__":
    # Example replay of last game's fatal endgame:
    assess(17, my_hp=13, opp_hps={1: 21, 3: 1}, my_shouwei_lead=True, typical_loss=24)
    assess(18, my_hp=13, opp_hps={1: 21, 3: 1}, my_shouwei_lead=True, typical_loss=27)
