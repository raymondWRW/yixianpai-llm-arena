# Xiao Bu 崩拳/气势 — g25-verified board recipes. Run with run_program to print the recipes to field.
# The CORE insight (g25): same 8 cards, ORDER decides vs each opponent.
RECIPES = {
  "vs_谭舒雁_内伤clock (force EARLY, need first seat)": [
     "气若悬河+1","势如破竹","崩拳·突+1","冲霄破浪","踏破九霄",
     "崩拳·寸劲","崩拳·缠","崩拳·惊触"],
  "vs_牧逸风_qi-nuke (burst FAST, force LATE)": [
     "气若悬河+1","崩拳·突+1","冲霄破浪","踏破九霄","崩拳·寸劲",
     "崩拳·惊触","势如破竹","崩拳·缠"],
  "MASTER_if_威震四方+1 (beats all 100/100)": [
     "气若悬河+1","威震四方+1","崩拳·突+1","冲霄破浪","踏破九霄",
     "崩拳·寸劲","崩拳·惊触","崩拳·连崩"],
}
KEEP = ["崩拳·寸劲","崩拳·连崩","崩拳·惊触","崩拳·闪击","威震四方",
        "气若悬河","冲霄破浪","踏破九霄","势如破竹","灵玄迷踪步"]
ORDER_ROLLS_R12 = ["威震四方","崩拳·连崩","崩拳·寸劲","崩拳·闪击",
                   "冲霄破浪","踏破九霄","势如破竹"]
if __name__ == "__main__":
    for k,v in RECIPES.items():
        print(k)
        print("   ", v)
    print("\nKEEP (never roll/absorb):", KEEP)
    print("R12+ named roll order:", ORDER_ROLLS_R12)
