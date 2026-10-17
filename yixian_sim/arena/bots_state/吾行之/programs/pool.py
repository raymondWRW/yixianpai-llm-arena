import os, sys, json, re
d = os.environ['YISIM_DIR']
# find swogi definition file
for fn in os.listdir(d):
    print(fn)
