#!/usr/bin/env python3
"""C4 clock recipe checker for 谭舒雁 (命理师).
Prints, for each C4 piece, how many copies are in the live pool.
Usage: run_program c4_check.py
(No file access needed; data is pasted by the caller each game — edit POOL below.)
"""
# C4 recipe (the ONLY board that matters, g23-audited)
C4 = ["天星·牵引", "厄劫缠身", "血光之灾", "天星·御心",
      "梅开二度", "杯弓蛇影", "流水无情", "诸事不宜"]
# keep-list = C4 + these value subs
KEEP = C4 + ["落花有意"]

# EDIT ME each game: {card_name: copies_in_live_pool}
POOL = {}

def main():
    if not POOL:
        print("Edit POOL with your live deck ({card: copies}) then rerun.")
        print("Target recipe (field by name):", " | ".join(C4))
        return
    total = sum(POOL.values()) or 1
    print("C4 piece  | copies | rolls-to-first (approx)")
    for c in KEEP:
        n = POOL.get(c, 0)
        p = n / total if total else 0
        expect = (1 / p) if p > 0 else float("inf")
        print(f"  {c:12s} {n:4d}      {expect:6.1f}")
    have = [c for c in C4 if POOL.get(c, 0) > 0]
    print(f"\nHOLDABLE now: {len(have)}/8 -> {have}")
    print("RULE: every R10+ roll must NAMED-target a piece you don't yet hold. STOP when one lands.")

if __name__ == "__main__":
    main()
