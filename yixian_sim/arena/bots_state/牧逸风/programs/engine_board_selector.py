"""
牧逸风 (云剑/阵法师5) — ENGINE BOARD SELECTOR.
Given the announced opponent's last board, prints the recommended engine board
from the g27-verified candidate list. Run before set_board, then sim_matchup to confirm.

Usage:
  python engine_board_selector.py <opp_name>
  opp_name in {xiaobu, wuxingzhi, tanshuyan, unknown}

Boards (g27 yisim-verified):
  UNIVERSAL : ['聚灵心法+1','回响阵纹','百鸟灵剑诀+1','引气剑+1','白鹭灵剑','万法归灵剑+1','化灵诀+1','云剑·汇灵']
              100/100 vs 谭舒雁 & 吾行之 (incl +1); 100%first/0%second vs 小布's upgraded master.
  ANTI-BURST: ['聚灵心法+1','回响阵纹','灵气灌注+1','引气剑+1','化灵诀','万法归灵剑+1','百鸟灵剑诀','云剑·汇灵']
              100/100 vs 小布's FULLY-upgraded master (20qi 万法=124dmg). LOSES to 内伤 clock — 小布 only.
  CLOCK     : same as UNIVERSAL (the 白鹭 chip is load-bearing vs 内伤; never swap it out for 谭舒雁).

KEY: vs a FAST BURST needing no chip -> battery(化灵诀) > chip(白鹭). vs 内伤 clock -> KEEP 白鹭 chip.
"""

UNIVERSAL = ['聚灵心法+1','回响阵纹','百鸟灵剑诀+1','引气剑+1','白鹭灵剑','万法归灵剑+1','化灵诀+1','云剑·汇灵']
ANTI_BURST = ['聚灵心法+1','回响阵纹','灵气灌注+1','引气剑+1','化灵诀','万法归灵剑+1','百鸟灵剑诀','云剑·汇灵']

def pick(opp):
    opp = opp.lower()
    if opp in ('xiaobu','pid3','小布','burst','崩拳'):
        return 'ANTI-BURST (hold seat; 化灵诀 slot5 for max qi burst)', ANTI_BURST
    if opp in ('wuxingzhi','pid2','吾行之','tank','水灵','heal'):
        return 'UNIVERSAL (tank: any works 100/100; big 万法 bank one-shots)', UNIVERSAL
    if opp in ('tanshuyan','pid1','谭舒雁','clock','内伤','命理'):
        return 'UNIVERSAL / CLOCK (KEEP 白鹭 chip — never swap to 化灵诀)', UNIVERSAL
    return 'UNKNOWN -> try UNIVERSAL first, sim both', UNIVERSAL

if __name__ == '__main__':
    import sys
    opp = sys.argv[1] if len(sys.argv) > 1 else 'unknown'
    label, board = pick(opp)
    print(f"opp={opp}\nrecommend: {label}\nboard={board}")
