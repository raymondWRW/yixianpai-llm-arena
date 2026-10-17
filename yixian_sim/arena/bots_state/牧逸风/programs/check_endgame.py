#!/usr/bin/env python3
"""牧逸风 endgame board checker.
Prints the canonical assessment target board. During a live game, run this in
your head: the goal is ALWAYS to field the 万法 board (辟邪 at slot 8), never the
no-finisher fallback. Post-game, use search_board/sim_matchup for exact numbers.
"""
UNIVERSAL = ["聚灵心法+1","百鸟灵剑诀+1","引气剑+1","巨鲲灵剑+2",
             "云剑·点星","白鹭灵剑+1","万法归灵剑+2","辟邪阵纹+1"]
FALLBACK  = ["聚灵心法","百鸟灵剑诀","引气剑","化灵诀",
             "云剑·极意+1","白鹭灵剑","飞牙剑","地煞剑"]

def main():
    print("TARGET (万法 board, 辟邪 SLOT 8):")
    for i,c in enumerate(UNIVERSAL,1): print(f"  slot{i}: {c}")
    print()
    print("FALLBACK (no 万法 yet) — WARNING: loses t12 vs 小布. Hunt 万法; do NOT field twice.")
    for i,c in enumerate(FALLBACK,1): print(f"  slot{i}: {c}")
    print()
    print("CHECKLIST: (1) 万法 in hand? (2) 境5 broken EARLY (R9-10 target)?")
    print("           (3) 修为 not lowest in lobby? (4) 辟邪 at slot 8? (5) rolling with NAMED target?")

if __name__ == "__main__":
    main()
