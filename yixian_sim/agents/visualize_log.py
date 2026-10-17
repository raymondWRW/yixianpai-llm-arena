# -*- coding: utf-8 -*-
"""visualize_log.py — render a hand-played game log (agents/mygame/log.txt) as a self-contained
HTML timeline: every roll / merge / absorb / take / board / breakthrough / fate / 道韵 decision in
order, the battle result each round, standings, and a 命 chart for all seats.

    python agents/visualize_log.py [--log agents/mygame/log.txt] [--out agents/mygame/game.html]
"""
from __future__ import annotations
import argparse, html, json, re
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def parse(text: str) -> dict:
    g = {"header": "", "me": "?", "opps": [], "rounds": [], "final": ""}
    cur = {"n": 1, "actions": [], "battles": [], "mine": None, "standings": None, "board": None}
    lines = text.splitlines()
    m = re.match(r"NEW GAME seed=(\d+) me=(\S+) vs \[(.*)\]", lines[0] if lines else "")
    if m:
        g["header"] = lines[0]; g["me"] = m.group(2)
        g["opps"] = [s.strip().strip("'") for s in m.group(3).split(",")]
    else:                       # ghost lobby: pidN 名字[uid rA-B of rec.json], …
        m = re.match(r"NEW GAME seed=(\d+) me=(\S+) vs RECORDED BOTS: (.*)", lines[0] if lines else "")
        if m:
            g["header"] = lines[0]; g["me"] = m.group(2); g["ghosts"] = {}
            for gm in re.finditer(r"pid(\d+) (\S+?)\[(\S+) r(\d+)-(\d+) of ([^\]]+)\]", m.group(3)):
                pid = int(gm.group(1))
                g["ghosts"][pid] = {"name": gm.group(2), "uid": gm.group(3), "rec": gm.group(6)}
            g["opps"] = [g["ghosts"][k]["name"] for k in sorted(g["ghosts"])]
    for ln in lines[1:]:
        s = ln.strip()
        if not s: continue
        if s.startswith("--- R"):
            continue                       # battle block header for the current round
        if s.startswith("pid") and " vs pid" in s:
            cur["battles"].append(s); continue
        m = re.match(r"R(\d+) vs pid(\d+) (\S+) \((.*?)\): (WIN|LOSS|DRAW) margin ([+-]?\d+) → my 命 (\d+)", s)
        if m:
            cur["mine"] = {"opp_pid": int(m.group(2)), "opp": m.group(3), "first": m.group(4),
                           "res": m.group(5), "margin": int(m.group(6)), "destiny": int(m.group(7))}
            continue
        if s.startswith("standings:"):
            cur["standings"] = {int(k.strip()[3:]): int(v) for k, v in
                                (kv.split(":") for kv in s[len("standings:"):].split(","))}
            g["rounds"].append(cur)
            cur = {"n": cur["n"] + 1, "actions": [], "battles": [], "mine": None, "standings": None, "board": None}
            continue
        if s.startswith("GAME OVER"):
            g["final"] = s; continue
        # actions
        a = None
        if s.startswith("deal "):
            a = {"t": "deal", "cards": [c.strip() for c in s[5:].split(",") if c.strip()]}
        elif s.startswith(". "):               # exact-state sync line (play.py sync())
            st_ = {}
            for kv in re.finditer(r"(\w+)=([^ ]*)", s[2:]):
                k, v = kv.group(1), kv.group(2)
                st_[k] = [x for x in v.split("|") if x] if k in ("hand", "board", "talents") \
                    else (int(v) if v.lstrip("-").isdigit() else v)
            a = {"t": "state", **st_}
        elif s.startswith("fx "):
            a = {"t": "fx", "text": s[3:]}
        elif s.startswith("roll "):
            m = re.match(r"roll (.+?) -> (.+)", s); a = {"t": "roll", "from": m.group(1), "to": m.group(2)}
        elif s.startswith("absorb "):
            m = re.match(r"absorb (.+?) -> 修为 (\d+)", s); a = {"t": "absorb", "card": m.group(1), "cult": int(m.group(2))}
        elif s.startswith("merge ->"):
            m = re.match(r"merge -> (.+?) \(\+1 修为 = (\d+)\)", s); a = {"t": "merge", "card": m.group(1), "cult": int(m.group(2))}
        elif s.startswith("take "):
            a = {"t": "take", "card": s[5:]}
        elif s.startswith("board = "):
            cards = [c.strip().strip("'") for c in s[len("board = ["):-1].split(",") if c.strip()]
            a = {"t": "board", "cards": cards}; cur["board"] = cards
        elif s.startswith("BREAKTHROUGH"):
            m = re.match(r"BREAKTHROUGH 境(\d) -> 境(\d); HP (\d+); 天命 \[(.*)\]", s)
            a = {"t": "break", "from": int(m.group(1)), "to": int(m.group(2)), "hp": int(m.group(3)),
                 "talents": [x.strip().strip("'") for x in m.group(4).split(",")]}
        elif s.startswith("天命 offer"):
            a = {"t": "fate_offer", "text": s.split(":", 1)[1].strip()}
        elif s.startswith("道韵 offer"):
            a = {"t": "dao_offer", "text": s.split(":", 1)[1].strip()}
        elif s.startswith("-> picked"):
            a = {"t": "pick", "text": s[len("-> picked "):]}
        elif s.startswith("sim "):
            a = {"t": "sim", "text": s[4:]}
        else:
            a = {"t": "note", "text": s}
        cur["actions"].append(a)
    if cur["actions"] or cur["battles"]:
        g["rounds"].append(cur)
    return g


ICON = {"roll": "换", "absorb": "炼", "merge": "合", "take": "回", "board": "阵", "break": "突",
        "fate_offer": "命", "dao_offer": "韵", "pick": "选", "sim": "算", "note": "·",
        "deal": "抽", "fx": "效", "state": "·"}


def esc(x): return html.escape(str(x))


def chips(cards, cls="chip"):
    return "".join(f'<span class="{cls}">{i+1}<b>{esc(c)}</b></span>' for i, c in enumerate(cards))


def render(g: dict) -> str:
    rounds = g["rounds"]
    seats = sorted({pid for r in rounds if r["standings"] for pid in r["standings"]})
    names = {0: g["me"]}
    for i, n in enumerate(g["opps"], start=1): names[i] = n
    # ---- 命 chart (SVG) ----
    W, H, PL, PB = 720, 220, 36, 26
    nR = max(1, len(rounds))
    xs = lambda i: PL + i * (W - PL - 10) / max(1, nR - 1)
    ys = lambda v: 8 + (H - PB - 8) * (1 - v / 120)
    paths = []
    for pid in seats:
        pts = []
        for i, r in enumerate(rounds):
            if r["standings"] and pid in r["standings"]:
                pts.append(f"{xs(i):.1f},{ys(r['standings'][pid]):.1f}")
        cls = "me" if pid == 0 else "opp"
        paths.append(f'<polyline class="{cls}" points="{" ".join(pts)}"/>')
        if pts:
            lx, ly = pts[-1].split(",")
            paths.append(f'<text class="lbl {cls}" x="{float(lx)+4:.0f}" y="{float(ly)+4:.0f}">{esc(names.get(pid, pid))}</text>')
    grid = "".join(f'<line class="grid" x1="{PL}" x2="{W-10}" y1="{ys(v):.1f}" y2="{ys(v):.1f}"/>'
                   f'<text class="ax" x="{PL-6}" y="{ys(v)+4:.1f}">{v}</text>' for v in (0, 25, 50, 75, 100))
    xt = "".join(f'<text class="ax" x="{xs(i):.1f}" y="{H-8}">R{r["n"]}</text>' for i, r in enumerate(rounds))
    chart = f'<svg viewBox="0 0 {W} {H}" class="chart" role="img" aria-label="命 by round">{grid}{xt}{"".join(paths)}</svg>'

    # ---- summary ----
    wins = sum(1 for r in rounds if r["mine"] and r["mine"]["res"] == "WIN")
    losses = sum(1 for r in rounds if r["mine"] and r["mine"]["res"] == "LOSS")
    n_act = {k: 0 for k in ICON}
    for r in rounds:
        for a in r["actions"]: n_act[a["t"]] += 1
    last = rounds[-1]["standings"] if rounds and rounds[-1]["standings"] else {}
    alive = sorted(((v, k) for k, v in last.items() if v > 0), reverse=True)
    place = [k for _, k in alive].index(0) + 1 if 0 in [k for _, k in alive] else "—"

    # ---- rounds ----
    out = []
    for r in rounds:
        mine = r["mine"]
        badge = ""
        if mine:
            cls = {"WIN": "win", "LOSS": "loss", "DRAW": "draw"}[mine["res"]]
            badge = f'<div class="badge {cls}">{mine["res"]}<span>{mine["margin"]:+d}</span></div>'
        acts = []
        for a in r["actions"]:
            t = a["t"]; ic = f'<i class="ic {t}">{ICON[t]}</i>'
            if t == "roll":
                body = f'换牌 <b>{esc(a["from"])}</b> <span class="arrow">→</span> <b class="new">{esc(a["to"])}</b>'
            elif t == "absorb":
                body = f'炼化 <b>{esc(a["card"])}</b> <span class="dim">修为 {a["cult"]}</span>'
            elif t == "merge":
                body = f'合成 <b class="new">{esc(a["card"])}</b> <span class="dim">+1 修为 = {a["cult"]}</span>'
            elif t == "take":
                body = f'拿回 <b>{esc(a["card"])}</b>'
            elif t == "board":
                body = f'摆阵 <span class="board">{chips(a["cards"])}</span>'
            elif t == "break":
                body = (f'<b class="gold">突破 境{a["from"]} → 境{a["to"]}</b> <span class="dim">HP {a["hp"]}</span>'
                        f' <span class="dim">天命: {esc(", ".join(a["talents"]))}</span>')
            elif t == "fate_offer":
                body = f'天命 offer <span class="dim">{esc(a["text"])}</span>'
            elif t == "dao_offer":
                body = f'道韵 offer <span class="dim">{esc(a["text"])}</span>'
            elif t == "pick":
                body = f'→ picked <b class="new">{esc(a["text"])}</b>'
            elif t == "deal":
                body = f'发牌 <span class="board">{chips(a["cards"])}</span>'
            elif t == "fx":
                body = f'<b class="gold">{esc(a["text"])}</b>'
            elif t == "state":
                continue                                  # sync line: replay only
            elif t == "sim":
                body = f'算伤害 <span class="dim">{esc(a["text"])}</span>'
            else:
                body = esc(a["text"])
            acts.append(f'<li class="act {t}">{ic}<div>{body}</div></li>')
        battle = ""
        if mine:
            battle = (f'<div class="battle"><span class="dim">battle</span> vs <b>{esc(mine["opp"])}</b> '
                      f'<span class="dim">({esc(mine["first"])})</span> · margin <b>{mine["margin"]:+d}</b> · 命 → <b>{mine["destiny"]}</b></div>')
        st = ""
        if r["standings"]:
            st = '<div class="stand">' + "".join(
                f'<span class="{"me" if k == 0 else ""}{" dead" if v == 0 else ""}">{esc(names.get(k, k))}<b>{v}</b></span>'
                for k, v in sorted(r["standings"].items(), key=lambda kv: -kv[1])) + "</div>"
        board = f'<div class="final"><span class="dim">fielded</span> {chips(r["board"])}</div>' if r["board"] else ""
        out.append(f'''<section class="round">
  <div class="rail"><div class="rn">R{r["n"]}</div>{badge}</div>
  <div class="body"><ol class="acts">{"".join(acts)}</ol>{board}{battle}{st}</div>
</section>''')

    return f'''<title>{esc(g["me"])} 弈仙牌 Playthrough</title>
<style>
:root{{--bg:#f4f6f8;--surface:#ffffff;--ink:#1b2430;--muted:#66788a;--line:#d9e0e7;--accent:#c4432c;--accent-ink:#ffffff;
--win:#2f8f6c;--loss:#c4432c;--gold:#a8791f;--chip:#e9eef3;--rail:#e2e8ee;--new:#1d5c8f}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#12171d;--surface:#1a2129;--ink:#e6ebf0;--muted:#94a3b3;--line:#2b3540;--accent:#e2604a;--accent-ink:#12171d;--win:#4fb08c;--loss:#e2604a;--gold:#d3a044;--chip:#242e39;--rail:#202932;--new:#7fb6e6}}}}
:root[data-theme="dark"]{{--bg:#12171d;--surface:#1a2129;--ink:#e6ebf0;--muted:#94a3b3;--line:#2b3540;--accent:#e2604a;--accent-ink:#12171d;--win:#4fb08c;--loss:#e2604a;--gold:#d3a044;--chip:#242e39;--rail:#202932;--new:#7fb6e6}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 "PingFang SC","Microsoft YaHei","Noto Sans CJK SC",system-ui,sans-serif}}
.wrap{{max-width:980px;margin:0 auto;padding:28px 20px 60px}}
h1{{font:600 30px/1.2 "Songti SC","STSong","SimSun","Noto Serif CJK SC",Georgia,serif;margin:0 0 4px;text-wrap:balance}}
.sub{{color:var(--muted);margin:0 0 18px}}
.summary{{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:0 0 18px}}
.stat{{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:10px 12px}}
.stat small{{display:block;color:var(--muted);letter-spacing:.06em;text-transform:uppercase;font-size:11px}}
.stat b{{font-size:22px;font-variant-numeric:tabular-nums}}
.stat b.win{{color:var(--win)}} .stat b.loss{{color:var(--loss)}}
.chartbox{{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:12px;margin:0 0 26px;overflow-x:auto}}
.chart{{width:100%;height:auto;display:block}}
.chart .grid{{stroke:var(--line);stroke-width:1}} .chart .ax{{fill:var(--muted);font-size:10px;text-anchor:middle}}
.chart polyline{{fill:none;stroke:var(--muted);stroke-width:1.2;opacity:.55}}
.chart polyline.me{{stroke:var(--accent);stroke-width:2.6;opacity:1}}
.chart .lbl{{font-size:10px;fill:var(--muted)}} .chart .lbl.me{{fill:var(--accent);font-weight:700}}
.round{{display:grid;grid-template-columns:76px 1fr;gap:14px;margin:0 0 14px}}
.rail{{background:var(--rail);border-radius:6px;padding:10px 8px;text-align:center;display:flex;flex-direction:column;gap:8px;align-items:center}}
.rn{{font:700 20px/1 "Songti SC","STSong","SimSun","Noto Serif CJK SC",Georgia,serif}}
.badge{{font:700 11px/1.1 ui-monospace,Consolas,monospace;padding:5px 6px;border-radius:4px;color:#fff;min-width:56px}}
.badge span{{display:block;font-size:14px;margin-top:2px}}
.badge.win{{background:var(--win)}} .badge.loss{{background:var(--loss)}} .badge.draw{{background:var(--muted)}}
.body{{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:10px 14px}}
.acts{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:5px}}
.act{{display:grid;grid-template-columns:24px 1fr;gap:10px;align-items:start;font-size:14px}}
.ic{{font-style:normal;display:inline-grid;place-items:center;width:22px;height:22px;border-radius:4px;background:var(--chip);color:var(--muted);font-size:12px;font-weight:700}}
.ic.roll{{background:var(--accent);color:var(--accent-ink)}} .ic.board{{background:var(--ink);color:var(--bg)}}
.ic.break,.ic.pick{{background:var(--gold);color:#fff}} .ic.merge{{background:var(--new);color:#fff}}
.act b{{font-weight:600}} .act .new{{color:var(--new)}} .act .gold{{color:var(--gold)}}
.arrow,.dim{{color:var(--muted)}}
.board,.final{{display:inline-flex;flex-wrap:wrap;gap:4px;align-items:center}}
.final{{margin-top:8px;padding-top:8px;border-top:1px dashed var(--line);font-size:13px}}
.chip{{display:inline-flex;align-items:center;gap:5px;background:var(--chip);border-radius:4px;padding:2px 7px 2px 5px;font-size:12.5px;font-variant-numeric:tabular-nums}}
.chip:first-child{{margin-left:6px}}
.chip::first-letter{{color:var(--muted)}} .chip b{{font-weight:600}}
.battle{{margin-top:8px;font-size:13.5px}}
.stand{{margin-top:6px;display:flex;flex-wrap:wrap;gap:4px 12px;font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}}
.stand b{{margin-left:4px;color:var(--ink)}} .stand .me b{{color:var(--accent)}} .stand .dead{{text-decoration:line-through;opacity:.6}}
.legend{{display:flex;flex-wrap:wrap;gap:8px 14px;color:var(--muted);font-size:12px;margin:0 0 14px}}
.legend .ic{{margin-right:4px;vertical-align:middle}}
.final-line{{margin-top:22px;padding:12px 14px;border-left:4px solid var(--accent);background:var(--surface);border-radius:4px}}
</style>
<div class="wrap">
<h1>{esc(g["me"])} · 弈仙牌 playthrough</h1>
<p class="sub">{esc(g["header"])}</p>
<div class="summary">
  <div class="stat"><small>Final place</small><b>{place}</b></div>
  <div class="stat"><small>Rounds</small><b>{len(rounds)}</b></div>
  <div class="stat"><small>Battles won</small><b class="win">{wins}</b></div>
  <div class="stat"><small>Battles lost</small><b class="loss">{losses}</b></div>
  <div class="stat"><small>换牌 rolls</small><b>{n_act["roll"]}</b></div>
  <div class="stat"><small>炼化 absorbs</small><b>{n_act["absorb"]}</b></div>
  <div class="stat"><small>合成 merges</small><b>{n_act["merge"]}</b></div>
  <div class="stat"><small>突破</small><b>{n_act["break"]}</b></div>
</div>
<div class="chartbox">{chart}</div>
<div class="legend">
  <span><i class="ic roll">换</i>reroll</span><span><i class="ic absorb">炼</i>absorb</span><span><i class="ic merge">合</i>merge</span>
  <span><i class="ic take">回</i>take back</span><span><i class="ic board">阵</i>set board (cyclic order)</span><span><i class="ic break">突</i>breakthrough</span>
  <span><i class="ic fate_offer">命</i>天命 offer</span><span><i class="ic dao_offer">韵</i>道韵 offer</span><span><i class="ic pick">选</i>pick</span><span><i class="ic sim">算</i>damage calc</span>
</div>
{"".join(out)}
<div class="final-line">{esc(g["final"]) or "game in progress"}</div>
</div>'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default=str(_HERE / "mygame" / "log.txt"))
    ap.add_argument("--out", default=str(_HERE / "mygame" / "game.html"))
    a = ap.parse_args()
    g = parse(Path(a.log).read_text(encoding="utf-8"))
    Path(a.out).write_text(render(g), encoding="utf-8")
    print(f"wrote {a.out}: {len(g['rounds'])} rounds, "
          f"{sum(len(r['actions']) for r in g['rounds'])} actions")


if __name__ == "__main__":
    main()
