# REFEREE-FIXED: original hard-coded a Recycle-Bin path found by crawling C:\.
# yisim source access is allowed ONLY via the YISIM_DIR env var (set by the harness).
import os, sys
p = os.path.join(os.environ["YISIM_DIR"], "gamestate_full.js")
term = sys.argv[1]
with open(p, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if term in l:
        print(i + 1, l.rstrip())
