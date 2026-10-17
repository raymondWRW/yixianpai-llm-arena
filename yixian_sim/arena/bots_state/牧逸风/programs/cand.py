import subprocess, os, itertools, json
# We'll just enumerate a few candidate boards by hand and rely on simulate tool.
# This program prints candidate boards to try.
hand = ["云剑·汇灵", "聚灵心法", "云剑·月影", "冲击阵纹"]
board = ["邪蛊阵+1", "灵气灌注+1", "化灵诀", "万花迷魂阵", "巨鲸灵剑+1", "巨鲲灵剑+1", "巨虎灵剑+1", "冲击阵纹+1"]
pool = hand + board
print(len(pool), pool)
