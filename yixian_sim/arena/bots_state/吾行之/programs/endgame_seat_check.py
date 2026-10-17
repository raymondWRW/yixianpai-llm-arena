# Discipline helper: before committing an ENDGAME board, you MUST verify it wins BOTH seats.
# In review: run sim_matchup(my_cards, opp_pid, repeats>=5) and READ the two numbers.
# If either seat is 0%, the board is a coin-flip and the game is decided by 修为 — find a board
# that wins both (a single merge/upgrade often flips it; e.g. 水灵·泉涌 -> 水灵·泉涌+1 flipped
# 谭舒雁 second-seat 0%->100%). Usage: python endgame_seat_check.py  # prints the rule.
if __name__ == "__main__":
    print("ENDGAME RULE: never commit a board with a 0% seat vs your announced opponent.")
    print("sim_matchup(...) both-seat numbers are the verdict. Both seats >=90% => commit.")
