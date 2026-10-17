# Referee report

## Unimplemented fates held this game
- none

## 牧逸风: program audit flags
- egrep.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys
- egrep.py:4 [os\s*\.\s*walk|os\s*\.\s*listdir|scandir] for f in os.listdir(d):
- readsrc.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import sys, glob, os
- show.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys
- src.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, glob, sys
## 谭舒雁: program audit flags
- base12.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- basepool.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- cards.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json, sys
- explore.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, glob, sys
- find5.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- find_cards.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json, sys
- findids.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- findmine.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- fulu.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- fulu2.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- fulu3.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- fulu4.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- hecards.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- hp_cards.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- hunt.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- my_cards.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- myhe1.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json, sys
- p3.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- p30.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- p300.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- read_src.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys
- readsrc.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys
- sidejob.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- sj.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- sj2.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
## 吾行之: program audit flags
- findcards.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json, sys
- grepgs.py:1 [Recycle] # REFEREE-FIXED: original hard-coded a Recycle-Bin path found by crawling C:\.
- grepgs.py:3 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys
- names.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json, sys, io
- peek.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys
- peek_js.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, re, sys
- pool.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys, json, re
- pool.py:4 [os\s*\.\s*walk|os\s*\.\s*listdir|scandir] for fn in os.listdir(d):
- readgs.py:1 [Recycle] # REFEREE-FIXED: original hard-coded a Recycle-Bin path found by crawling C:\.
- readgs.py:3 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys
- readlines.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import sys, os
## 小布: program audit flags
- fatedesc.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- fateterm.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json
- findfates.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, glob
- findfates.py:4 [os\s*\.\s*walk|os\s*\.\s*listdir|scandir] for f in sorted(os.listdir(d)):
- findfates.py:8 [os\s*\.\s*walk|os\s*\.\s*listdir|scandir] for root, dirs, files in os.walk(d):
- read_src.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, sys
- readfates.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os
- readfates2.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os
- search_board.py:2 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json, subprocess, sys, itertools
- search_board.py:15 [os\s*\.\s*walk|os\s*\.\s*listdir|scandir] print(os.listdir(YISIM))
- talentparams.py:1 [^\s*(import|from)\b[^\n]*\b(os|shutil|socket|requests|urllib|http|subprocess|pathlib|ctypes|winreg)\b] import os, json

## Qi-stall counts per battle (turns spent gaining qi)
- R1 pid0 vs pid3: first-seat stalls=0, second=0
- R1 pid1 vs pid2: first-seat stalls=0, second=1
- R2 pid0 vs pid2: first-seat stalls=0, second=2
- R2 pid1 vs pid3: first-seat stalls=2, second=0
- R3 pid3 vs pid2: first-seat stalls=0, second=2
- R3 pid1 vs pid0: first-seat stalls=2, second=0
- R4 pid3 vs pid0: first-seat stalls=0, second=0
- R4 pid2 vs pid1: first-seat stalls=2, second=1
- R5 pid2 vs pid0: first-seat stalls=2, second=0
- R5 pid3 vs pid1: first-seat stalls=0, second=0
- R6 pid3 vs pid2: first-seat stalls=0, second=2
- R6 pid1 vs pid0: first-seat stalls=0, second=0
- R7 pid3 vs pid1: first-seat stalls=0, second=0
- R7 pid2 vs pid0: first-seat stalls=0, second=0
- R8 pid1 vs pid2: first-seat stalls=0, second=0
- R8 pid3 vs pid0: first-seat stalls=0, second=0
- R9 pid1 vs pid3: first-seat stalls=0, second=0
- R9 pid2 vs pid0: first-seat stalls=0, second=0
- R10 pid2 vs pid3: first-seat stalls=0, second=0
- R10 pid1 vs pid0: first-seat stalls=0, second=0
- R11 pid3 vs pid0: first-seat stalls=0, second=0
- R11 pid1 vs pid2: first-seat stalls=0, second=0
- R12 pid1 vs pid3: first-seat stalls=10, second=0  <-- CHECK
- R12 pid2 vs pid0: first-seat stalls=0, second=0
- R13 pid1 vs pid2: first-seat stalls=16, second=0  <-- CHECK
- R13 pid3 vs pid0: first-seat stalls=0, second=1
- R14 pid3 vs pid2: first-seat stalls=0, second=0
- R14 pid1 vs pid0: first-seat stalls=6, second=3  <-- CHECK
- R15 pid1 vs pid3: first-seat stalls=8, second=1  <-- CHECK
- R15 pid3 vs pid0: first-seat stalls=0, second=0
- R16 pid1 vs pid0: first-seat stalls=0, second=2
- R16 pid3 vs pid0: first-seat stalls=0, second=1
- R17 pid1 vs pid3: first-seat stalls=1, second=0
- R17 pid3 vs pid0: first-seat stalls=0, second=3
- R18 pid1 vs pid0: first-seat stalls=0, second=3