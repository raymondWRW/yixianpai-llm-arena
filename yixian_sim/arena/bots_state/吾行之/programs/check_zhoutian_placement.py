"""
Helper: reminds future-me to test BOTH 周天剑阵 placement extremes before set_board.
This is a reminder script, not a solver. Place 周天剑阵+1 FIRST vs fast burst, LAST vs slow clock.
Run: run_program('check_zhoutian_placement.py')
"""
import os

YISIM = os.environ.get('YISIM_DIR', '')

def main():
    print("=== 周天剑阵 PLACEMENT CHECKLIST (g29 discovery) ===")
    print("周天剑阵 = [持续]N: every ATK card gains an EXTRA +5 ATK hit, N charges.")
    print("Charge placement decides which attacks get buffed -> decides the matchup.")
    print()
    print("MUST sim BOTH before set_board:")
    print("  A) 周天剑阵 at SLOT 1  (buff every attack from turn 1)  <- vs FAST BURST (小布 崩拳)")
    print("  B) 周天剑阵 at SLOT 7  (buff the BIG late 水势-scaled hits) <- vs SLOW CLOCK (谭舒雁 内伤)")
    print()
    print("g29 evidence: vs 谭舒雁 clock, slot3=100f/0s, slot7=100f/100s (pure reorder).")
    print("Reference winning board:")
    print("  ['水灵·泉涌+1','水灵阵','水灵·纳百川','水灵·汹涌+1','水灵·汹涌','水灵·涛+1','周天剑阵+1','五行刺+1']")
    print()
    print("Also: FIELD 7-8 CARDS. A 4-card board loses to everyone.")

if __name__ == '__main__':
    main()
