
"""
Helper: print the two canonical 小布 endgame boards + the pid-specific swap rule.
Used as a quick reference during the round-economy phase in future games.
Run: python endgame_check.py <opp_pid>
"""
import sys

GENERAL = ["气若悬河", "冲霄破浪", "威震四方", "势如破竹", "踏破九霄",
           "朝气蓬勃", "磅礴之势+1", "崩拳·降龙"]
VS_PID1 = ["气若悬河", "冲霄破浪", "威震四方", "天谕·守", "踏破九霄",
           "朝气蓬勃", "磅礴之势+1", "崩拳·降龙"]

def main():
    opp = sys.argv[1] if len(sys.argv) > 1 else "?"
    print("BOARD vs opp:", opp)
    if opp == "1":
        print(" slot4 SWAP 势如破竹 -> 天谕·守 (def-wall vs her 内伤 clock):")
        print(" ", VS_PID1)
    else:
        print(" ", GENERAL)
    print("RULES: 磅礴之势+1 BEFORE 崩拳·降龙; 势如破竹 EARLY; 踏破九霄(+6agi) triggers auto-chase.")
    print("Late game: absorb to WIN SEAT (修为). Name ONE merge target or STOP rolling (C8).")

if __name__ == "__main__":
    main()
