
import os, sys, json, itertools, subprocess
YISIM = os.environ.get('YISIM_DIR')
# Use yisim directly if there's a CLI; otherwise we cannot. We'll try importing the engine.
print("YISIM_DIR=", YISIM)
print(os.listdir(YISIM)[:20] if YISIM else "none")
