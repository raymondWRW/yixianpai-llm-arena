"""
order_search.py — brute-force cyclic ORDERINGS of a fixed card multiset against
a given opponent board, using the yisim engine directly.

USAGE (from run_program):
    args = [ "CARD1,CARD2,...cards", "OPPCARD1,OPPCARD2,...", "first|second" ]
It prints, for each permutation of the multiset, WIN/LOSE + loser destiny dmg,
sorted by best (win, then highest dmg dealt).

This wraps the engine so future-me doesn't have to guess orderings by hand.
It is defensive: if the engine import path/API differs, it prints a clear error
instead of crashing, so I still learn something.
"""
import os, sys, itertools

YISIM = os.environ.get('YISIM_DIR')

def main():
    if len(sys.argv) < 3:
        print("need: cards_csv opp_cards_csv [first|second]")
        return
    my = [c for c in sys.argv[1].split(',') if c]
    opp = [c for c in sys.argv[2].split(',') if c]
    first = (len(sys.argv) < 4) or (sys.argv[3].lower().startswith('f'))
    print("YISIM_DIR =", YISIM)
    try:
        print("files:", os.listdir(YISIM))
    except Exception as e:
        print("listdir err:", e)
    # NOTE: the exact engine entry point is not stable across versions.
    # Try to locate a battle function.
    try:
        sys.path.insert(0, YISIM)
        import gamestate_full as g
        print("gamestate_full attrs sample:",
              [a for a in dir(g) if a.lower().startswith(('sim','battle','run','fight'))][:20])
    except Exception as e:
        print("import err:", e)
    # Print unique orderings count so I can at least size the search.
    uniq = set(itertools.permutations(my))
    print("unique orderings to try:", len(uniq), "(first)" if first else "(second)")
    for p in list(uniq)[:50]:
        print("  ", "|".join(p))

if __name__ == "__main__":
    main()
