# REFEREE-FIXED: original hard-coded a Recycle-Bin path found by crawling C:\.
# yisim source access is allowed ONLY via the YISIM_DIR env var (set by the harness).
import os, sys
p = os.path.join(os.environ["YISIM_DIR"], "gamestate_full.js")
start = int(sys.argv[1]) if len(sys.argv) > 1 else 1540
end = int(sys.argv[2]) if len(sys.argv) > 2 else 1620
with open(p, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()
for i in range(start - 1, min(end, len(lines))):
    print(i + 1, lines[i].rstrip())
