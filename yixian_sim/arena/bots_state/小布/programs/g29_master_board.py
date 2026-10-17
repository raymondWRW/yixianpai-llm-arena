# g29 finding: the 崩拳 master board needs ONE BIG-ATTACKER +1 to win BOTH seats vs 谭舒雁's 内伤 clock.
# As-fielded (no upgrade) = 100% first / 0% second. Upgrade 连崩/撼/突/威震四方 -> 100/100.
# Upgrade 惊触 does NOT work. Sustain (不动金刚阵) does NOT work. Order does NOT work.

MASTER_G29 = ["崩拳·闪击", "威震四方+1", "崩拳·撼+2", "崩拳·连崩+1",
              "崩拳·突", "崩拳·降龙", "崩拳·惊触", "不动金刚阵"]
# minimum viable: any ONE of these in the assembled board wins both seats vs 谭舒雁:
#   崩拳·连崩+1 (best, 16 atk) > 崩拳·撼+2 > 崩拳·突+1 > 威震四方+1
# verified via sim_matchup + 3 search_board runs + manual full-log simulate (g29 review).

# yisim usage:
#   simulate(my_cards=MASTER_G29, opp_pid=1, i_go_first=False)  # -> WIN vs 谭舒雁 final board
#   sim_matchup(MASTER_G29, opp_pid=1)  # -> should read 100% first / 100% second

if __name__ == "__main__":
    print("g29 master 崩拳 board:", *MASTER_G29, sep="\n  ")
    print("Requires ONE big-attacker +1 (连崩+1 preferred).")
