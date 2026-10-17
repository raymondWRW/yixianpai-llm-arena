
import itertools, sys, os
# We can't call yisim directly here easily; instead print candidate boards for external simulate.
# Candidate card pool (cards available: current board + hand)
board = ['邪蛊阵','化灵诀+1','辟邪阵纹','碎杀阵+1','巨鲸灵剑','破气剑+1','周天剑阵+1','龟甲阵+1']
hand = ['反身剑','云剑·柔心','云剑·无妄','不动金刚阵']
print("BOARD", board)
print("HAND", hand)
