
# 小布 气势-bomb engine reference boards (verified this game vs all 3 rivals' base boards).
# Usage: print the recommended cyclic board for the announced opponent.

BASE = ["聚灵阵", "起势", "崩灭心法", "势如破竹", "崩拳·寸劲+1", "朝气蓬勃+1", "磅礴之势", "破空爪+1"]
WITH_FORCE_CAP = ["修罗吼", "威震四方+1", "崩灭心法", "势如破竹", "崩拳·寸劲+2", "朝气蓬勃+1", "磅礴之势", "破空爪+1"]

# Verified win% vs final boards (this game, sim_matchup base boards):
#   pid0 云剑: 100/100 ; pid1 星力: 100/100 (after 寸劲+1) ; pid2 5-elem: 100/100
# vs +1-upgraded boards: pid0 mixed, pid1 0%, pid2 100% first. => draw 修罗吼 vs pid1.

def board_for(opp):
    """opp: 'pid0'/'云剑', 'pid1'/'星力', 'pid2'/'5elem'. Returns recommended board."""
    if opp in ("pid1", "星力"):
        # sustain matters; if 修罗吼 in hand use WITH_FORCE_CAP else BASE
        return WITH_FORCE_CAP
    return BASE

if __name__ == "__main__":
    import sys
    opp = sys.argv[1] if len(sys.argv) > 1 else "pid0"
    print(" | ".join(board_for(opp)))
