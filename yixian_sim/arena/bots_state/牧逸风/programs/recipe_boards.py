"""Print the two recipe boards for 牧逸风 (剑阵 + 命理师).
Usage: run_program('recipe_boards.py', ['opp_pid'])  -> prints recommended recipe.
opp_pid 3 (小布/body-temper) -> REFLECT board; else -> QI board.
"""
import sys

QI = ["化灵诀+1", "聚灵心法", "巨鲲灵剑+1", "天机·顺应+1",
      "万法归灵剑", "灵气灌注", "巨鹏灵剑+1", "云剑·点星"]
REFLECT = ["化灵诀+1", "水月剑阵", "巨鲲灵剑+1", "天机·顺应+1",
           "天机·逆施", "诸事不宜", "万法归灵剑", "聚灵心法"]

def main():
    pid = sys.argv[1] if len(sys.argv) > 1 else "?"
    if pid == "3":
        print("REFLECT board (anti body-temper burst):")
        print(" / ".join(REFLECT))
    else:
        print("QI board (baseline / vs star & element decks):")
        print(" / ".join(QI))

if __name__ == "__main__":
    main()
