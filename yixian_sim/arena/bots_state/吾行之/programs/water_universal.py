
# 吾行之 universal water+阵 board (g20). Print the target board and its fallback tiers.
TARGET = ['万花迷魂阵+1','回响阵纹','水灵·泉涌+1','不动金刚阵+2','水灵·波澜+1','水灵·纳百川','水灵·汹涌+1','辟邪阵纹']
FALLBACK_LOW = ['万花迷魂阵+1','回响阵纹','水灵·泉涌+1','不动金刚阵','水灵·波澜+1','水灵·纳百川','水灵·汹涌+1','辟邪阵纹']
FALLBACK_NOHEX = ['万花迷魂阵+1','回响阵纹','水灵·泉涌+1','不动金刚阵+2','水灵·波澜+1','水灵·纳百川','水灵·汹涌+1','水灵·腾浪']
OUTPUT = ['引气剑']  # placeholder, unused
print("TARGET (beats all 3 rivals base+1 both seats):")
print(TARGET)
print("fallback if 不动 not upgraded:", FALLBACK_LOW)
print("fallback if no 辟邪 (weaker vs 谭舒雁 2nd seat):", FALLBACK_NOHEX)
print("roll target priority: 万花迷魂阵 > 不动金刚阵 > 回响阵纹 > 辟邪阵纹 > 水灵·泉涌 > 波澜/汹涌")
print("DO NOT ABSORB:", TARGET)
