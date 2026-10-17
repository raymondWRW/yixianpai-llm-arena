
# Brute-force board orderings for 牧逸风 vs 小布 (pid3), acts SECOND.
# Prints candidate orderings; user feeds to simulate. We cannot call yisim here.
import itertools

# Available distinct cards (with copies): board + hand
cards = [
 "百鸟灵剑诀+1","辟邪阵纹","化灵诀","引气剑","巨鲲灵剑+1","水月剑阵","巨鲲灵剑","白鹭灵剑+1",
 "灵气灌注","云剑·点星","白鹭灵剑","聚灵阵","万花迷魂阵","剑意激荡","狂剑·一式","聚灵心法",
 "灵感剑","云剑·无妄","狂剑·二式","云剑·回守","天罡聚力阵"
]
# We just print a few hand-picked orderings to test.
print("Run simulate() on these orderings manually.")
