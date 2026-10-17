# -*- coding: utf-8 -*-
"""build_site.py — generate the GitHub Pages site (docs/) for the arena.

    python build_site.py

Writes <repo>/docs/index.html (the 30-game analysis report),
docs/replays.html (a viewer for every per-bot replay) and copies the replay
pages into docs/replays/g<N>/p<pid>.html. All numbers come from the game
artifacts via extract.py; the narrative is written here.
"""
from __future__ import annotations

import html
import json
import shutil
from collections import Counter
from pathlib import Path

import extract as X

ROOT = Path(__file__).resolve().parent.parent.parent      # repo root
DOCS = ROOT / "docs"
REPO_URL = "https://github.com/raymondWRW/yixianpai-llm-arena"

BOT_COLOR = {0: "#2f6fd6", 1: "#8a4fd1", 2: "#1f9e73", 3: "#d9622b"}
BOT_EN = {0: "Mu Yifeng", 1: "Tan Shuyan", 2: "Wu Xingzhi", 3: "Xiao Bu"}
SECT = {0: "云灵剑宗 Cloud Spirit Sword", 1: "七星阁 Heptastar",
        2: "五行道盟 Five Elements", 3: "锻玄宗 Body Tempering"}
ARCH_COLOR = {
    "Sustain / reflect": "#7d8c99", "Star (星弈)": "#8a63d2",
    "Five-element seals": "#6b9e3a", "Force fist (崩拳)": "#e07b39",
    "Qi-dump swords": "#3a7bd5", "内伤 clock": "#c2416b",
    "Water drain": "#1aa0a8", "Formation swords": "#a0782c",
    "Cloud swords": "#5b8db8", "Other": "#9aa3ad",
}
CAREER_COLOR = {1: "#d1495b", 2: "#edae49", 3: "#66a182", 4: "#c77dff",
                5: "#2e86ab", 6: "#8ac926", 7: "#6c757d"}

esc = html.escape


# ── charts (inline SVG, theme-aware via CSS variables) ──────────────────────
def chart_titles(games):
    W, H, L, R, T, B = 760, 280, 44, 120, 16, 34
    n = len(games)
    counts = {p: 0 for p in range(4)}
    series = {p: [] for p in range(4)}
    for f in games:
        if f["winner"] is not None:
            counts[f["winner"]] += 1
        for p in range(4):
            series[p].append(counts[p])
    ymax = max(max(s) for s in series.values()) + 1
    x = lambda i: L + i * (W - L - R) / (n - 1)
    y = lambda v: T + (H - T - B) * (1 - v / ymax)
    out = [f'<svg viewBox="0 0 {W} {H}" class="chart" role="img" '
           f'aria-label="Cumulative titles per bot across 30 games">']
    for v in range(0, ymax + 1, 2):
        out.append(f'<line x1="{L}" x2="{W-R}" y1="{y(v):.1f}" y2="{y(v):.1f}" '
                   f'class="grid"/><text x="{L-8}" y="{y(v)+4:.1f}" '
                   f'class="axis" text-anchor="end">{v}</text>')
    for i, f in enumerate(games):
        if f["game"] % 5 == 0 or f["game"] == 1:
            out.append(f'<text x="{x(i):.1f}" y="{H-12}" class="axis" '
                       f'text-anchor="middle">g{f["game"]}</text>')
    for p in range(4):
        pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(series[p]))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{BOT_COLOR[p]}" '
                   f'stroke-width="2.5" stroke-linejoin="round"/>')
        out.append(f'<text x="{W-R+8}" y="{y(series[p][-1])+4:.1f}" '
                   f'fill="{BOT_COLOR[p]}" class="lbl">{X.NAMES[p]} {series[p][-1]}</text>')
    out.append("</svg>")
    return "".join(out)


def chart_strip(games):
    cells = []
    for f in games:
        g = f["game"]
        if f["winner"] is None:
            cells.append(f'<a class="cell void" href="replays.html#g{g}" '
                         f'title="Game {g}: unfinished (stopped by a harness '
                         f'round cap)"><span>g{g}</span><b>—</b></a>')
            continue
        arch = f["archetypes"].get(f["winner"], ("Other", False))[0]
        cells.append(
            f'<a class="cell" href="replays.html#g{g}-p{f["winner"]}" '
            f'style="--c:{ARCH_COLOR.get(arch, "#999")}" title="Game {g}: '
            f'{esc(f["winner_name"])} — {esc(arch)}"><span>g{g}</span>'
            f'<b style="color:{BOT_COLOR[f["winner"]]}">{esc(f["winner_name"][0])}</b></a>')
    used = []
    for f in games:
        if f["winner"] is not None:
            a = f["archetypes"].get(f["winner"], ("Other", False))[0]
            if a not in used:
                used.append(a)
    legend = "".join(f'<span class="key"><i style="background:{ARCH_COLOR[a]}">'
                     f'</i>{esc(a)}</span>' for a in used)
    return (f'<div class="strip">{"".join(cells)}</div>'
            f'<div class="legend">{legend}<span class="key"><i class="voidkey">'
            f'</i>unfinished</span></div>')


def chart_sidejobs(games):
    rows = []
    for p in range(4):
        cells = []
        for f in games:
            c = f["sidejobs"].get(p)
            col = CAREER_COLOR.get(c, "transparent")
            cells.append(f'<i style="background:{col}" title="Game {f["game"]}: '
                         f'{esc(X.NAMES[p])} → {esc(X.CAREERS.get(c, "?"))}"></i>')
        rows.append(f'<div class="hrow"><span style="color:{BOT_COLOR[p]}">'
                    f'{esc(X.NAMES[p])}</span><div class="hcells">{"".join(cells)}'
                    f'</div></div>')
    axis = "".join(f'<em>{f["game"] if f["game"] % 5 == 0 or f["game"] == 1 else ""}</em>'
                   for f in games)
    legend = "".join(f'<span class="key"><i style="background:{CAREER_COLOR[c]}">'
                     f'</i>{esc(n)}</span>' for c, n in X.CAREERS.items())
    return (f'<div class="heat">{"".join(rows)}<div class="hrow"><span></span>'
            f'<div class="hcells axisrow">{axis}</div></div></div>'
            f'<div class="legend">{legend}</div>')


def chart_turns(games):
    W, H, L, R, T, B = 760, 230, 44, 20, 14, 34
    vals = []
    for f in games:
        late = [t for rd, t in f["battles"] if rd >= 13]
        vals.append(sum(late) / len(late) if late else 0)
    ymax = 20
    n = len(games)
    bw = (W - L - R) / n
    y = lambda v: T + (H - T - B) * (1 - v / ymax)
    out = [f'<svg viewBox="0 0 {W} {H}" class="chart" role="img" '
           f'aria-label="Average battle length in rounds 13 and later, per game">']
    for v in range(0, ymax + 1, 5):
        out.append(f'<line x1="{L}" x2="{W-R}" y1="{y(v):.1f}" y2="{y(v):.1f}" '
                   f'class="grid"/><text x="{L-8}" y="{y(v)+4:.1f}" '
                   f'class="axis" text-anchor="end">{v}</text>')
    for i, (f, v) in enumerate(zip(games, vals)):
        x0 = L + i * bw + bw * 0.15
        dot = f["winner"] is not None and f["archetypes"].get(
            f["winner"], ("", False))[1]
        cls = "bar dot" if dot else "bar"
        out.append(f'<rect x="{x0:.1f}" y="{y(v):.1f}" width="{bw*0.7:.1f}" '
                   f'height="{(H-B)-y(v):.1f}" class="{cls}" rx="2">'
                   f'<title>Game {f["game"]}: {v:.1f} turns per late battle</title></rect>')
        if f["game"] % 5 == 0 or f["game"] == 1:
            out.append(f'<text x="{x0 + bw*0.35:.1f}" y="{H-12}" class="axis" '
                       f'text-anchor="middle">g{f["game"]}</text>')
    out.append("</svg>")
    return "".join(out)


# ── stats used in the text ───────────────────────────────────────────────────
def stats(games):
    decided = [f for f in games if f["winner"] is not None]
    titles = Counter(f["winner"] for f in decided)
    dot_wins = [f["game"] for f in decided
                if f["archetypes"].get(f["winner"], ("", False))[1]]
    late12 = [f for f in decided if f["game"] >= 19]
    dot_late = [f["game"] for f in late12 if f["game"] in dot_wins]
    zf = [f for f in games if f["game"] >= 17]
    zhen = sum(sum(1 for c in f["sidejobs"].values() if c == 5) for f in zf)
    return {"decided": len(decided), "titles": titles, "dot_wins": dot_wins,
            "dot_late": dot_late, "late12": len(late12),
            "zhen_late": zhen, "zhen_slots": 4 * len(zf), "zf_games": len(zf)}


# ── page assembly ─────────────────────────────────────────────────────────────
CSS = """
:root{--bg:#fbfaf7;--fg:#1d1f23;--muted:#5f6670;--line:#e3e0d8;--card:#ffffff;
--accent:#b8862b;--grid:#ebe8e0;--bar:#9aa3ad;--dot:#c2416b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#15171b;
--fg:#e8e6e1;--muted:#a0a6ae;--line:#2c3037;--card:#1d2026;--accent:#d8a948;
--grid:#262a31;--bar:#5d6670;--dot:#e0567f}}
:root[data-theme="dark"]{--bg:#15171b;--fg:#e8e6e1;--muted:#a0a6ae;--line:#2c3037;
--card:#1d2026;--accent:#d8a948;--grid:#262a31;--bar:#5d6670;--dot:#e0567f}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 -apple-system,
"Segoe UI",Roboto,"Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif}
main{max-width:860px;margin:0 auto;padding:0 16px 80px}
nav.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid
var(--line)}
nav.top div{max-width:860px;margin:0 auto;padding:10px 16px;display:flex;gap:18px;
flex-wrap:wrap;font-size:14px}
nav.top a{color:var(--muted);text-decoration:none}nav.top a:hover{color:var(--fg)}
nav.top a.home{color:var(--fg);font-weight:700;margin-right:auto}
header.hero{padding:56px 0 28px;border-bottom:1px solid var(--line)}
.eyebrow{color:var(--accent);font-size:13px;letter-spacing:.12em;text-transform:uppercase;
font-weight:700}
h1{font-size:clamp(32px,6vw,48px);line-height:1.15;margin:.3em 0 .4em;letter-spacing:-.01em}
.lede{font-size:19px;color:var(--muted);max-width:680px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;
margin:28px 0 0}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.stat b{display:block;font-size:24px}.stat span{color:var(--muted);font-size:13px}
h2{font-size:27px;margin:56px 0 10px;letter-spacing:-.01em}
h3{font-size:19px;margin:30px 0 6px}
h3 small{color:var(--muted);font-weight:400;font-size:14px;margin-left:6px}
p{margin:.6em 0}a{color:var(--accent)}
.fig{background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:16px;margin:18px 0}
.fig figcaption{color:var(--muted);font-size:14px;margin-top:8px}
.chart{width:100%;height:auto;display:block}
.chart .grid{stroke:var(--grid);stroke-width:1}
.chart .axis{fill:var(--muted);font-size:12px}
.chart .lbl{font-size:13px;font-weight:700}
.chart .bar{fill:var(--bar)}.chart .bar.dot{fill:var(--dot)}
.strip{display:grid;grid-template-columns:repeat(15,minmax(0,1fr));gap:4px}
.cell{display:flex;flex-direction:column;align-items:center;justify-content:center;
background:color-mix(in srgb,var(--c) 26%,var(--card));border:2px solid var(--c);
border-radius:6px;padding:3px 0;text-decoration:none;color:var(--fg);min-height:46px}
.cell span{font-size:10px;color:var(--muted)}.cell b{font-size:15px}
.cell.void{--c:var(--line);background:transparent;border-style:dashed}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:10px;font-size:13px;color:var(--muted)}
.key i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:5px;
vertical-align:-1px}.key i.voidkey{border:1.5px dashed var(--muted)}
.heat .hrow{display:grid;grid-template-columns:62px 1fr;align-items:center;gap:8px;margin:3px 0}
.heat .hrow span{font-size:14px;font-weight:600}
.hcells{display:grid;grid-template-columns:repeat(30,minmax(0,1fr));gap:2px}
.hcells>*{min-width:0;overflow:hidden}.heat{overflow-x:auto}
.strip>*{min-width:0}main{overflow-wrap:anywhere}
.hcells i{height:18px;border-radius:2px}
.hcells.axisrow em{font-size:10px;color:var(--muted);font-style:normal;text-align:center}
.era{border-left:3px solid var(--accent);padding-left:16px;margin:26px 0}
table{width:100%;border-collapse:collapse;font-size:15px;margin:14px 0}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--muted);font-weight:600;font-size:13px}
.tablewrap{overflow-x:auto}
.callout{background:var(--card);border:1px solid var(--line);border-left:4px solid
var(--accent);border-radius:8px;padding:14px 18px;margin:18px 0}
.callout .who{font-size:13px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
.bots{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin:16px 0}
.bot{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--bc);
border-radius:10px;padding:10px 12px;font-size:14px}
.bot b{font-size:18px;display:block}
.cta{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;
padding:10px 18px;border-radius:8px;font-weight:600;margin-top:12px}
footer{color:var(--muted);font-size:14px;border-top:1px solid var(--line);margin-top:60px;padding-top:18px}
@media (max-width:600px){.strip{grid-template-columns:repeat(10,minmax(0,1fr))}.hcells.axisrow em{font-size:8px}
.heat .hrow{grid-template-columns:52px 1fr}body{font-size:16px}}
"""


def page_index(games, s):
    T = s["titles"]
    total = sum(T.values())
    bots = "".join(
        f'<div class="bot" style="--bc:{BOT_COLOR[p]}"><b>{esc(X.NAMES[p])}</b>'
        f'{esc(BOT_EN[p])} · {esc(SECT[p])}<br><strong>{T.get(p,0)}</strong> '
        f'title{"s" if T.get(p,0)!=1 else ""}</div>' for p in range(4))
    dot_n, dot_late = len(s["dot_wins"]), len(s["dot_late"])
    cards = [
        ("聚气咒", "谭舒雁", "2", "Turns qi into defense. Fixed the star board's losses when it had to act second."),
        ("天元心法 in slot 1", "谭舒雁", "2", "Makes every slot a star point, so every attack gets the star-power bonus."),
        ("土灵·扬尘", "吾行之", "3", "Defense that scales with the opponent's max-HP lead — the answer to a physique HP wall."),
        ("破气剑 early in the cycle", "牧逸风", "4", "Strips the opponent's qi on hit; the first counter that beat the star engine."),
        ("梅开二度 → 镇魂封元符", "谭舒雁", "5", "Doubles a 40% max-HP strip plus a qi drain on the next card."),
        ("威震四方", "小布", "6 · 19 · 26", "Raises the force (气势) cap from 6 to 9. Found in game 6, forgotten, rediscovered in game 19, finally fielded in a winning board in game 26."),
        ("厄劫缠身", "小布 · 谭舒雁", "7 · 30", "Its opening downgrades the opponent's card in the same slot. In game 30 the bot showed from the engine source that it belongs in slot 1."),
        ("杯弓蛇影 + 厄劫缠身 (内伤 clock)", "谭舒雁", "10", "Internal injury ticks at the start of the victim's turn, so it kills through defense and healing. Four straight titles."),
        ("辟邪阵纹 in slot 1", "牧逸风", "14", "Blanks internal-injury ticks — the hard counter that ended the 内伤 dynasty."),
        ("踏破九霄 / 冲霄破浪 (身法)", "小布", "15 · 18", "Builds agility to 10, which buys an automatic extra card every turn."),
        ("万花迷魂阵 + 回响阵纹", "吾行之", "19", "A drain retriggered every turn that ignores defense and force, while its attack-down stacks shrink burst damage."),
        ("诸事不宜", "谭舒雁", "20", "−6 attack on the opponent's next two hits; the key anti-burst slot in every one of its later wins."),
        ("不动金刚阵", "吾行之", "18 → 23", "Defense and max HP at turn end for several turns; lets the water board survive burst. Its own notes had wrongly called it illegal."),
        ("万法归灵剑", "牧逸风", "8 · 14 · 21", "Dumps all banked qi into one hit — 15 qi became 95 damage in game 21. Rare: about one copy per game at phase 5."),
    ]
    rows = "".join(f"<tr><td><b>{esc(c)}</b></td><td>{esc(w)}</td><td>{esc(g)}</td>"
                   f"<td>{esc(d)}</td></tr>" for c, w, g, d in cards)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>弈仙牌 LLM Arena</title>
<meta name="description" content="Thirty games of self-play: four LLM bots learn the auto-battler 弈仙牌 (YiXianPai) from a rulebook, a combat simulator and their own notes.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🀄</text></svg>">
<style>{CSS}</style></head><body>
<nav class="top"><div><a class="home" href="index.html">弈仙牌 LLM Arena</a>
<a href="#eras">Strategy over time</a><a href="#counters">Key counters</a>
<a href="#real">vs real players</a><a href="replays.html">Replays</a>
<a href="{REPO_URL}">GitHub</a></div></nav>
<main>
<header class="hero">
<div class="eyebrow">An experiment in AI self-play</div>
<h1>Four AI bots teach themselves 弈仙牌</h1>
<p class="lede">Thirty games of a 4-player card auto-battler, played by four language-model
bots that started with nothing but the rules, a combat simulator and an empty notebook.
After every game each bot studied its losses and rewrote its own strategy. This is how
their play changed.</p>
<div class="stats">
<div class="stat"><b>30</b><span>games played</span></div>
<div class="stat"><b>{s['decided']}</b><span>decided (2 unfinished)</span></div>
<div class="stat"><b>{total}</b><span>titles shared by 4 bots</span></div>
<div class="stat"><b>~$0.53</b><span>API cost per game (late games)</span></div>
</div>
<div class="bots">{bots}</div>
<a class="cta" href="replays.html">Watch the replays →</a>
</header>

<h2 id="setup">The setup</h2>
<p>Four seats, one per sect. Each seat is an LLM agent (DeepSeek <code>deepseek-chat</code>)
playing the whole game through tools: rolling and absorbing cards, merging copies, fielding
its board, breaking through realms, choosing a sidejob in round 2 and a fate at every realm gate.
Battles are resolved by <a href="https://github.com/sharpobject/yisim">yisim</a>, an open-source
reimplementation of the game's combat, which the bots can also call to test any board before
committing to it.</p>
<p>During a game each bot sees only what a human player would: its own hand and board, its
opponents' boards from the previous round, and who it fights this round. After the game it gets a
long review with full replays of every battle, a per-card damage audit, its roll history, and a
board-search tool. It then rewrites its playbook and adds an entry to a permanent ledger. Its
memory of the conversation is wiped between games; only those files survive. From game 16 the
reviews were open: every bot could read every rival's playbook and watch every battle.</p>

<h2 id="results">Results at a glance</h2>
<figure class="fig">{chart_titles(games)}
<figcaption>Cumulative titles per bot. 谭舒雁 led early with two dynasties (games 1–5 and
10–13); the field evened out after game 14, and all four bots won at least twice in the last
nine games.</figcaption></figure>
<figure class="fig">{chart_strip(games)}
<figcaption>Every game's winner, coloured by the archetype of its winning board (letter =
winning bot). Click a game to open its replay.</figcaption></figure>

<h2 id="eras">How strategy changed over time</h2>

<div class="era"><h3>Games 1–5 · Sustain, then stars <small>谭舒雁 wins 4 of 5</small></h3>
<p>Early bots fielded whatever they drew and spent heavily on cultivation without a plan.
谭舒雁 won game 1 with a sustain wall (静气心法 healing per qi, 反震心法 reflection, 金蝉脱壳
guard), then in game 2 pivoted mid-game to a <b>star engine</b>: 天元心法 in slot 1 turns every
slot into a star point, and 聚气咒's qi-to-defense floor fixed its losses when acting second.
By game 2, three bots had independently read the destiny-damage formula out of the engine
source and reached the same conclusion: winning the round matters far more than the margin.
吾行之 took game 3 by committing to one engine early and banking 命 while rivals were weak,
closing with 土灵·扬尘 against 小布's growing HP wall.</p></div>

<div class="era"><h3>Games 6–9 · Engines, force and physique <small>小布 rises</small></h3>
<p>小布's game-5 review proved its losses came from card levels and seat order, not its build;
it won games 6 and 7 with a <b>force-stacking 崩拳 engine</b> on top of a physique (体魄) HP wall.
Reviews got deeper: bots began citing engine source lines, and 谭舒雁 discovered that slots 3
and 6 are star points by default. In game 7 小布 found that 厄劫缠身's opening downgrades the
opponent's card in the same slot, and used it to cripple 谭舒雁's finisher. 牧逸风 took its
first title in game 8 with a qi-battery burst (聚灵心法 → 灵犀剑阵 → 白鹭灵剑 →
万法归灵剑), surviving four straight rounds at 命1.</p></div>

<div class="era"><h3>Games 10–13 · The 内伤 clock <small>谭舒雁 wins four straight</small></h3>
<p>谭舒雁's game-9 review produced the key insight of the series: pure sustain and pure stars
both lose to 小布's burst, but <b>internal injury (内伤)</b> ticks at the start of the victim's
turn — a clock that kills straight through defense and healing. In game 10 it fielded exactly
that board (厄劫缠身 ×2, 杯弓蛇影 ×2): a counter designed in one review and executed the next
game. It won four in a row, the last by a record 命63.</p></div>

<div class="era"><h3>Games 14–21 · Counters and synthesis <small>the dynasty falls</small></h3>
<p>牧逸风 broke the dynasty in game 14 with a <b>levelled qi burst</b> (巨鲲灵剑+2,
万法归灵剑+2) that killed before the 内伤 clock could finish, with 辟邪阵纹 in slot 1 to blank
the injury ticks. In game 15 小布 won with a <b>synthesis</b>: an 内伤 splash (血光之灾) taken
from its rival's toolkit, its own force core, and 踏破九霄 for tempo — once the bots had been
taught that 10 agility (身法) buys an extra card each turn. 吾行之 invented a <b>drain
engine</b> in game 19 (万花迷魂阵 retriggered by 回响阵纹) that ignores defense and force.
The same game, 小布 rediscovered that force caps at 6 and 威震四方 raises it — a lesson its
game-6 notebook already contained but had lost when notebooks were still rewritten from
scratch, which is why permanent ledgers were added. In game 20 the leader lost with an
empty hand: 谭舒雁 had absorbed every card to win the cultivation race and could no longer
field its own recipe.</p></div>

<div class="era"><h3>Games 22–30 · Balance <small>every bot wins at least twice</small></h3>
<p>The last nine games were the most even of the series, and nearly every win executed a lesson
written in an earlier review. 小布 played a perfect game 22 (no 命 lost) and finally fielded
威震四方 in game 26. 吾行之 won games 23–24 back to back on water boards anchored by
不动金刚阵 — a card its own playbook had wrongly listed as illegal until game 18 — and its
reviews turned on slot order: swapping 潜遁 before 腾浪 was worth 50% against 小布.
牧逸风 won games 27–28 with 聚灵心法 + 回响阵纹 feeding a 万法归灵剑 one-shot; 回响阵纹
first appeared in 吾行之's drain board, so it was very likely picked up by reading rival files.
谭舒雁 won three of the last six with 诸事不宜 in every winning board, and in game 30 showed
from the engine source that 厄劫缠身 belongs in slot 1.</p></div>

<h2 id="counters">Key cards and counters the bots found</h2>
<p>Each of these was found by a bot in its own post-game review, usually by replaying the battle
it lost and searching for a board that would have won it.</p>
<div class="tablewrap"><table><thead><tr><th>Card / combo</th><th>Found by</th>
<th>Game</th><th>Why it mattered</th></tr></thead><tbody>{rows}</tbody></table></div>

<h2 id="learning">What made the learning work</h2>
<p><b>Memory that survives.</b> Bots originally rewrote one notebook from scratch after every
game, and lessons kept vanishing (威震四方 is the clearest case). From game 13 each bot kept a
playbook rebuilt by merging plus an append-only ledger with one entry per game. Rules that
held for three games were promoted to a "core principles" section, tagged with the games that
proved them.</p>
<p><b>Seeing the fight.</b> Reviews gained turn-by-turn battle logs with real player names and
HP/defense/resources after every turn, a per-card contribution audit, the bot's own roll
history, a database of every board ever fielded, and a board search that explores with the
game's own combat code and lets yisim pick the winner.</p>
<p><b>Guardrails against false lessons.</b> Bots sometimes wrote down wrong conclusions — one
claimed a merge would have won a game when it didn't own enough copies to make it. Reviews now
require checking that a fix was actually reachable, and every claim carries its evidence or
is marked as a guess.</p>
<p><b>Fate choices.</b> Until game 8 the fate-offer preview silently failed, so most picks fell to
a generic default. Once fixed, bots ranked every fate deliberately — {sum(f['fates_picked'] for f in games if f['game']>=9)}
of {sum(f['fates_picked']+f['fates_default'] for f in games if f['game']>=9)} picks from game 9 on.</p>

<h2 id="real">How close is this to real players?</h2>
<div class="callout"><div class="who">Author's assessment</div>
<p>The bots found a lot of good counters, but there are a few things to point out.</p>
<p>Their boards are still evolving, and are not yet as strong as real players' boards. Because of
that, the bots evolved a completely different strategy from normal player boards. The weaker
overall power level means each combat takes much longer than in a real game, which favours
strategies that deal damage over time, such as internal-injury (内伤) and water-spirit (水灵) decks.</p>
<p>This is probably also why several bots chose formation master (阵法师) as their sidejob, even
though in real games it is often considered a weaker sidejob. The lower overall power level lets
the bots take advantage of every benefit of formation master's continuous (持续) cards.</p></div>
<p>The arena data is consistent with this:</p>
<ul>
<li>Damage-over-time boards (内伤 clock or water drain) won <b>{dot_n} of the {s['decided']}</b>
decided games, including {dot_late} of the last {s['late12']}.</li>
<li>From game 17 on, three of the four bots picked 阵法师 in every game:
{s['zhen_late']} of {s['zhen_slots']} sidejob choices across those {s['zf_games']} games.</li>
<li>Late-game battles regularly ran 8–17 turns (chart below). Bars in red are games won by a
damage-over-time board.</li></ul>
<figure class="fig">{chart_turns(games)}
<figcaption>Average battle length in rounds 13 and later, per game (turns). Red = the game was won
by a damage-over-time board.</figcaption></figure>
<figure class="fig">{chart_sidejobs(games)}
<figcaption>Sidejob chosen by each bot in each game. The drift to 阵法师 (blue) from game 16 on is
the formation-master effect described above.</figcaption></figure>

<h2 id="caveats">Caveats</h2>
<ul>
<li>Combat runs on yisim, a community reimplementation from a version-1.5.9 snapshot (base
game only). In a 36-matchup check against the game's own combat code, the two agreed on the
winner 83% of the time.</li>
<li>The economy (deals, rolls, fates, sidejobs) is a simulation built from rulings, not the live
game. Several harness bugs were found and fixed during the run: sidejob pools were random
before game 5; the limit of two 消耗/持续 cards was unenforced before game 5; fate previews
failed before game 9; games 9 and 17 were stopped by a round cap that does not exist in the real
game and are recorded as unfinished; game 16 was lost to a PC sleep and replayed with a new
seed; and in games 16–20 the last bot to review saw rivals' freshly updated notes.</li>
<li>All four bots run the same model; differences come from their sects, their notes and luck.</li>
</ul>

<footer>Built from the arena's game logs. Code, playbooks, ledgers and per-game reports:
<a href="{REPO_URL}">{REPO_URL.replace("https://", "")}</a>. Card names are from 弈仙牌
(YiXianPai); this is an independent fan project.</footer>
</main></body></html>"""


def page_replays(games):
    items = []
    for f in games:
        g = f["game"]
        tag = (f'<span class="w" style="color:{BOT_COLOR[f["winner"]]}">'
               f'{esc(f["winner_name"])}</span>' if f["winner"] is not None
               else '<span class="w void">unfinished</span>')
        items.append(f'<button data-g="{g}">Game {g}{tag}</button>')
    meta = {f["game"]: {"winner": f["winner"], "rounds": f["rounds"],
                        "arch": (f["archetypes"].get(f["winner"], ("", False))[0]
                                 if f["winner"] is not None else "")}
            for f in games}
    names = json.dumps({p: X.NAMES[p] for p in range(4)}, ensure_ascii=False)
    colors = json.dumps(BOT_COLOR)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Replays · 弈仙牌 LLM Arena</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🀄</text></svg>">
<style>{CSS}
body{{height:100vh;display:flex;flex-direction:column;overflow:hidden}}
.wrap{{flex:1;display:grid;grid-template-columns:200px 1fr;min-height:0}}
aside{{border-right:1px solid var(--line);overflow-y:auto;padding:8px}}
aside button{{display:flex;justify-content:space-between;width:100%;background:none;border:0;
color:var(--fg);padding:7px 10px;border-radius:6px;cursor:pointer;font:inherit;font-size:14px}}
aside button:hover{{background:var(--card)}}aside button.on{{background:var(--card);
outline:1px solid var(--line);font-weight:700}}
.w{{font-size:13px}}.w.void{{color:var(--muted)}}
section.view{{display:flex;flex-direction:column;min-height:0}}
.bar2{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px 14px;
border-bottom:1px solid var(--line)}}
.bar2 .info{{color:var(--muted);font-size:14px;margin-right:auto}}
.tab{{background:var(--card);border:1px solid var(--line);color:var(--fg);padding:6px 12px;
border-radius:6px;cursor:pointer;font:inherit;font-size:14px}}
.tab.on{{border-color:var(--tc);box-shadow:inset 0 -3px 0 var(--tc);font-weight:700}}
iframe{{flex:1;width:100%;border:0;background:#14161d}}
@media (max-width:700px){{.wrap{{grid-template-columns:1fr;grid-template-rows:auto 1fr}}
aside{{display:flex;overflow-x:auto;border-right:0;border-bottom:1px solid var(--line)}}
aside button{{width:auto;flex:0 0 auto;gap:6px}}}}
</style></head><body>
<nav class="top"><div><a class="home" href="index.html">弈仙牌 LLM Arena</a>
<a href="index.html#eras">Strategy over time</a><a href="index.html#counters">Key counters</a>
<a href="replays.html">Replays</a><a href="{REPO_URL}">GitHub</a></div></nav>
<div class="wrap"><aside id="list">{"".join(items)}</aside>
<section class="view"><div class="bar2"><span class="info" id="info"></span>
<span id="tabs"></span></div><iframe id="frame" title="Replay"></iframe></section></div>
<script>
const META={json.dumps(meta, ensure_ascii=False)}, NAMES={names}, COLORS={colors};
let G=30, P=null;
function show(g,p){{
  G=g; const m=META[g]; P=(p!==null&&p!==undefined)?p:(m.winner!==null?m.winner:0);
  document.querySelectorAll('#list button').forEach(b=>b.classList.toggle('on',+b.dataset.g===g));
  document.getElementById('info').textContent='Game '+g+' · '+m.rounds+' rounds'+
    (m.winner!==null?' · winner '+NAMES[m.winner]+(m.arch?' ('+m.arch+')':''):' · unfinished');
  document.getElementById('tabs').innerHTML=[0,1,2,3].map(i=>
    `<button class="tab${{i===P?' on':''}}" style="--tc:${{COLORS[i]}}" onclick="show(${{g}},${{i}})">${{NAMES[i]}}</button>`).join(' ');
  document.getElementById('frame').src='replays/g'+g+'/p'+P+'.html';
  history.replaceState(null,'','#g'+g+'-p'+P);
}}
document.querySelectorAll('#list button').forEach(b=>b.onclick=()=>show(+b.dataset.g,null));
const h=location.hash.match(/g(\\d+)(?:-p(\\d))?/);
show(h?+h[1]:30, h&&h[2]!==undefined?+h[2]:null);
</script></body></html>"""


def main():
    games = X.all_games()
    s = stats(games)
    DOCS.mkdir(exist_ok=True)
    for child in DOCS.iterdir():          # empty it; the folder itself may be
        if child.is_dir():                # held open by a shell or OneDrive
            shutil.rmtree(child)
        else:
            child.unlink()
    (DOCS / "replays").mkdir()
    missing = []
    for f in games:
        g = f["game"]
        out = DOCS / "replays" / f"g{g}"
        out.mkdir()
        for p, name in X.NAMES.items():
            src = X.GAMES / f"game{g}" / "replays" / f"replay_{name}.html"
            if src.exists():
                shutil.copy2(src, out / f"p{p}.html")
            else:
                missing.append(f"g{g}/{name}")
    (DOCS / "index.html").write_text(page_index(games, s), encoding="utf-8")
    (DOCS / "replays.html").write_text(page_replays(games), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    print(f"site built in {DOCS}: {len(games)} games, "
          f"titles {dict(s['titles'])}, DoT wins {s['dot_wins']}, "
          f"阵法师 {s['zhen_late']}/{s['zhen_slots']}; missing replays: {missing or 'none'}")


if __name__ == "__main__":
    main()
