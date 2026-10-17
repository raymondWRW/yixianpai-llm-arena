# Helper: print the R17 万法 qi-nuke recipe and its key engine pieces.
# Use to plan boards: check your hand/pool for these names.
RECIPE = ["飞灵闪影剑+1", "聚灵心法", "凝意诀", "云剑·游龙+1", "形意剑+1",
          "灵犀剑阵+1", "巨鲲灵剑+1", "万法归灵剑"]
ENGINE = ["万法归灵剑", "巨鲲灵剑", "聚灵心法", "凝意诀", "灵犀剑阵",
          "云剑·游龙", "云剑·闪风", "飞灵闪影剑", "形意剑", "御空剑阵"]
ANTI_PID1 = ["辟邪阵纹", "驱邪丹", "万事如意", "还魂丹", "锻体玄丹"]
def main(args):
    print("R17 RECIPE (100% vs pid2 & pid3 both seats, even +1):")
    for i, c in enumerate(RECIPE):
        print(f"  slot {i}: {c}")
    print("\nENGINE PIECES to HOARD (R3-R9):", ENGINE)
    print("ANTI-pid1 (谭舒雁) levers:", ANTI_PID1)
    print("\npid1 = UNBEATABLE with pure Cloud Sword; do NOT brawl her, farm others.")
if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
