# -*- coding: utf-8 -*-
"""replay_viewer.py — chess-style replay of a hand-played game (agents/mygame/log.txt).

Reconstructs the full visible state (board slots, hand, rerolls, cult/HP/命, talents) after
every logged action and emits ONE self-contained HTML file laid out like the game screen:

    top-left  cult / max HP / 命          top-right  Round N + Move i/total
    middle    8 board slots (cyclic order, locked slots greyed)
    bottom    hand cards (center) · character + 天命 (left) · 换牌 left (right)

Navigate with ◀ ▶ buttons, ←/→ keys, or the scrubber. The acting cards glow and an action
banner says what happened.

    python agents/replay_viewer.py [--log agents/mygame/log.txt] [--out agents/mygame/replay.html]

Every move is exact: play.py logs the round's DEAL (the opening 5 at R1, the 3-4 drawn each
round after) plus a `. hand=… board=… rr=… cult=…` sync line after each action, so the
viewer replays recorded state rather than inferring it. Logs written before sync lines
existed still replay — the inference path fills the gaps.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

_HERE = Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(_HERE))
from visualize_log import parse  # noqa: E402

REALM_HP = {1: 40, 2: 45, 3: 52, 4: 62, 5: 75}


def base_lv(name: str):
    m = re.match(r"^(.*?)\+(\d)$", name)
    return (m.group(1), int(m.group(2)) + 1) if m else (name, 1)


def reroll_grant(rnd):
    return 3 if rnd <= 9 else (4 if rnd <= 12 else 6)


def build_moves(g: dict) -> list:
    """Linear list of move snapshots. Each: dict(round, type, text, board, hand,
    hlB, hlH, cult, realm, hp, destiny, rerolls, talents, standings).

    play.py writes a `. hand=… board=… rr=…` sync line after every action, so state is
    read straight from the log; the inference below (used for logs predating sync lines)
    only fills the gaps."""
    S = {"round": 0, "cult": 0, "realm": 1, "hp": 40, "destiny": 100, "rerolls": 0,
         "talents": [], "board": [], "hand": [], "standings": None, "slots": 3}
    moves = []

    def materialize(name):
        if name not in S["hand"]:
            S["hand"].append(name)

    def snap(typ, text, hl_b=(), hl_h=(), sub="", hl_names=()):
        moves.append({"round": S["round"], "type": typ, "text": text, "sub": sub,
                      "board": list(S["board"]), "hand": list(S["hand"]),
                      "hlB": list(hl_b), "hlH": list(hl_h), "hlN": list(hl_names),
                      "cult": S["cult"], "realm": S["realm"], "hp": S["hp"],
                      "destiny": S["destiny"], "rerolls": S["rerolls"],
                      "slots": S["slots"], "talents": list(S["talents"]),
                      "standings": S["standings"]})

    def apply_state(a):
        """A `. hand=… board=…` sync line: ground truth. Rewrites the running state AND
        the move it follows, so every snapshot is exactly what the game held."""
        for k, key in (("hand", "hand"), ("board", "board"), ("talents", "talents")):
            if k in a:
                S[key] = list(a[k])
        for k, key in (("rr", "rerolls"), ("cult", "cult"), ("realm", "realm"),
                       ("hp", "hp"), ("destiny", "destiny"), ("slots", "slots")):
            if k in a:
                S[key] = a[k]
        if moves:
            m = moves[-1]
            m.update(board=list(S["board"]), hand=list(S["hand"]), talents=list(S["talents"]),
                     rerolls=S["rerolls"], cult=S["cult"], realm=S["realm"], hp=S["hp"],
                     destiny=S["destiny"], slots=S["slots"])
            # re-anchor highlights that were computed against the pre-sync hand
            if m.get("hlN"):
                m["hlH"] = [i for i, c in enumerate(S["hand"]) if c in m["hlN"]]
            if m["type"] == "board":
                m["hlB"] = list(range(len(S["board"])))

    for r in g["rounds"]:
        S["round"] = r["n"]
        S["rerolls"] += reroll_grant(r["n"])
        S["slots"] = min(8, max(3, r["n"] + 2))
        if r["n"] >= 2:
            S["cult"] += 2                       # passive (absorb lines re-anchor exactly)
        snap("round", f"Round {r['n']} begins",
             sub=f"+{reroll_grant(r['n'])} 换牌" + (" · +2 修为 passive" if r["n"] >= 2 else ""))
        for a in r["actions"]:
            t = a["t"]
            if t == "state":
                apply_state(a); continue
            if t == "deal":
                S["hand"] += a["cards"]
                lbl = "opening hand" if r["n"] == 1 else f"drew {len(a['cards'])}"
                snap("deal", f"发牌 {lbl}", sub=" · ".join(a["cards"]),
                     hl_h=list(range(len(S["hand"]) - len(a["cards"]), len(S["hand"]))),
                     hl_names=a["cards"])
            elif t == "fx":
                snap("fx", a["text"])
            elif t == "roll":
                materialize(a["from"])
                S["hand"].remove(a["from"])
                S["hand"].append(a["to"])
                S["rerolls"] = max(0, S["rerolls"] - 1)
                snap("roll", f"换牌 {a['from']} → {a['to']}", hl_h=[len(S['hand']) - 1],
                     hl_names=[a["to"]])
            elif t == "absorb":
                materialize(a["card"]); S["hand"].remove(a["card"])
                S["cult"] = a["cult"]
                snap("absorb", f"炼化 {a['card']}", sub=f"修为 → {a['cult']}")
            elif t == "merge":
                b, lv = base_lv(a["card"])
                low = b if lv == 2 else f"{b}+{lv-2}"
                for _ in range(2):
                    materialize(low); S["hand"].remove(low)
                S["hand"].append(a["card"]); S["cult"] = a["cult"]
                snap("merge", f"合成 {a['card']}", sub=f"+1 修为 = {a['cult']}",
                     hl_h=[len(S['hand']) - 1], hl_names=[a["card"]])
            elif t == "take":
                if a["card"] in S["board"]:
                    S["board"].remove(a["card"])
                S["hand"].append(a["card"])
                snap("take", f"拿回 {a['card']}", hl_h=[len(S['hand']) - 1], hl_names=[a["card"]])
            elif t == "board":
                old = list(S["board"]); new = list(a["cards"])
                for c in new:                    # consume from hand / old board
                    if c in S["hand"]:
                        S["hand"].remove(c)
                    elif c in old:
                        old.remove(c)
                    # else: dealt-then-played, never seen — fine
                S["hand"].extend(old)            # displaced cards back to hand
                S["board"] = new
                snap("board", "摆阵 set the board", hl_b=list(range(len(new))),
                     sub=" · ".join(new))
            elif t == "break":
                S["realm"] = a["to"]; S["hp"] = a["hp"]; S["talents"] = a["talents"]
                snap("break", f"突破 境{a['from']} → 境{a['to']}", sub=f"HP {a['hp']} · 天命 {', '.join(a['talents'])}")
            elif t == "fate_offer":
                snap("offer", "天命 offer", sub=a["text"])
            elif t == "dao_offer":
                snap("offer", "道韵 offer", sub=a["text"])
            elif t == "pick":
                snap("pick", f"picked {a['text']}")
            elif t == "sim":
                snap("sim", "damage calc", sub=a["text"])
            else:
                snap("note", a["text"])
        if r["standings"]:
            S["standings"] = r["standings"]
        if r["mine"]:
            m = r["mine"]
            S["destiny"] = m["destiny"]
            snap("battle", f"{m['res']} vs {m['opp']} ({m['margin']:+d})",
                 sub=f"{m['first']} · 命 → {m['destiny']}", hl_b=list(range(len(S["board"]))))
            moves[-1].update(oppPid=m.get("opp_pid"), res=m["res"], margin=m["margin"],
                             first=m["first"])          # combat-screen fields
        elif r["battles"]:
            snap("battle", f"Round {r['n']} battles resolved", sub="; ".join(r["battles"]))
    if g["final"]:
        snap("final", g["final"])
    return moves


def _marks(prev: list, cur: list, cap: int | None = None) -> list:
    """[[name, flag], …] for `cur`, flag 1 = APPEARED this action (green border).
    Cards present in `prev` but not `cur` are appended with flag 2 = LEAVING — they stay
    on screen for this one action wearing a red ✕, and are gone on the next move.
    `cap` (the board's 8 slots) drops the leaving markers when they wouldn't fit."""
    from collections import Counter
    pc, cc = Counter(prev), Counter(cur)
    added, removed = cc - pc, pc - cc
    out, left = [], dict(added)
    for n in cur:
        if left.get(n, 0) > 0:
            out.append([n, 1]); left[n] -= 1
        else:
            out.append([n, 0])
    gone = list(removed.elements())
    if gone and (cap is None or len(out) + len(gone) <= cap):
        out += [[n, 2] for n in gone]
    return out


def mark_moves(moves: list) -> None:
    """Attach handShow/boardShow (name + appear/leave flag) by diffing each move
    against the one before it."""
    prev_h, prev_b = [], []
    for m in moves:
        m["handShow"] = _marks(prev_h, m["hand"])
        m["boardShow"] = _marks(prev_b, m["board"], cap=8)
        prev_h, prev_b = m["hand"], m["board"]


# ── asset resolution (yxp_wiki id space == ours) ──────────────────────────────

WIKI = "https://sharpobject.github.io/yxp_wiki/assets"


def prep_assets(g: dict, moves: list) -> dict:
    """Resolve every card/character/talent NAME in the replay to the wiki's asset
    ids (same yisim id space as the sim). Anything unresolvable renders as the
    text fallback tile, so failures are cosmetic only."""
    import sys as _sys
    _sys.path.insert(0, str(_HERE.parent / "selfplay"))
    import cards as C
    import characters as CHR

    card_ids = {}

    def art_id(name):
        if name in card_ids:
            return card_ids[name]
        b, lv = base_lv(name)
        try:
            base = C.name_to_base_id(b)
            cid = (base + 10000 * (lv - 1)) if base else 0
        except Exception:
            cid = 0
        card_ids[name] = cid
        return cid

    for m in moves:
        for n in m["hand"] + m["board"]:
            art_id(n)

    char_by_name = {nm: cid for cid, nm, _ in CHR.roster()}
    me_char = char_by_name.get(g["me"], 1000004)

    # talents → immortal-fate icon ids
    fate_ids = {}
    try:
        fates = json.loads((_HERE.parent / "vendor" / "yisim-master" / "localization"
                            / "1.5.8" / "immortal_fates.json").read_text(encoding="utf-8"))
        by_cn = {f.get("name_cn"): f.get("id") for f in fates}
        for m in moves:
            for t in m["talents"]:
                if t not in fate_ids and by_cn.get(t):
                    fate_ids[t] = by_cn[t]
    except Exception:
        pass

    # ghost lobby: per-round recorded boards/hands for the inspect view
    roster = [{"pid": 0, "name": g["me"], "char": me_char, "uid": ""}]
    ghosts, id_names = {}, {}
    ginfo = g.get("ghosts") or {}
    trajs = []
    try:
        trajs = json.loads((_HERE / "ghosts.json").read_text(encoding="utf-8"))["trajs"]
    except Exception:
        pass
    for pid in sorted(ginfo):
        info = ginfo[pid]
        t = next((t for t in trajs if t["uid"] == info["uid"] and
                  (t["rec"] == info["rec"] or t["rec"].endswith("/" + info["rec"])
                   or info["rec"].endswith("/" + t["rec"]))), None)   # shard-prefix tolerant
        char = t["char"] if t else char_by_name.get(info["name"], 0)
        roster.append({"pid": pid, "name": info["name"], "char": char, "uid": info["uid"]})
        if t:
            rounds = {}
            for rn, rd in t["rounds"].items():
                rounds[int(rn)] = {"board": rd["board"], "hand": rd.get("hand") or [],
                                   "level": rd.get("level", 1), "exp": rd.get("exp", 0)}
                for cid in rd["board"] + (rd.get("hand") or []):
                    if cid not in id_names:
                        try:
                            id_names[cid] = C.id_to_name(cid)
                        except Exception:
                            id_names[cid] = str(cid)
            ghosts[pid] = {"char": char, "rounds": rounds}
    if not ginfo:                       # plain lobby: names only, no boards
        for i, nm in enumerate(g["opps"], start=1):
            roster.append({"pid": i, "name": nm, "char": char_by_name.get(nm, 0), "uid": ""})

    return {"cardIds": card_ids, "idNames": id_names, "fateIds": fate_ids,
            "roster": roster, "ghosts": ghosts, "meChar": me_char}


_PAGE = """<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@ME@ 弈仙牌 Replay</title>
<style>
:root{color-scheme:dark;--ink:#ded5bb;--muted:#8d9a8f;--line:#41473d;--accent:#d7b15d;--gold:#f5d995}
*{box-sizing:border-box} [hidden]{display:none!important}
body{margin:0;background:#080b09;color:var(--ink);
font:14px/1.45 "PingFang SC","Microsoft YaHei","Noto Sans CJK SC",system-ui,sans-serif}
.page{max-width:1240px;margin:0 auto;padding:14px 14px 40px}
.intro{display:flex;align-items:end;justify-content:space-between;gap:16px;margin:2px 0 9px}
.eyebrow{margin:0 0 4px;color:var(--accent);font-size:11px;font-weight:850;letter-spacing:.1em;text-transform:uppercase}
.intro h1{margin:0;font-size:24px;color:#f0e8d0}
.intro .muted{margin:4px 0 0;color:var(--muted);font-size:13px;overflow-wrap:anywhere}
.shell{overflow:hidden;border:1px solid #474b3f;border-radius:12px;background:#0d120f;box-shadow:0 22px 52px rgba(0,0,0,.35)}
.toolbar{display:grid;grid-template-columns:34px 34px minmax(160px,1fr) 132px auto;align-items:center;gap:6px;
padding:6px 9px;border-bottom:1px solid #41473d;background:#151d18}
.toolbar button,.toolbar select{border:1px solid var(--line);border-radius:7px;background:#111713;color:var(--ink);
padding:5px;font:inherit;font-size:16px;line-height:1;cursor:pointer}
.toolbar select{font-size:13px;padding:6px}
.toolbar button:hover,.toolbar select:hover{border-color:var(--accent)}
.toolbar button:disabled{opacity:.35;cursor:default}
.toolbar input{width:100%;accent-color:var(--accent)}
#step-label{min-width:96px;color:var(--muted);font-size:12px;text-align:right}
.stage{position:relative;isolation:isolate;padding:0 0 12px;
background:radial-gradient(ellipse at 55% 3%,rgba(72,103,123,.44),transparent 38%),
linear-gradient(180deg,#07141c 0 15%,#2f3a37 15.2% 58%,#0b2527 58.2% 100%)}
.stage::before{content:"";position:absolute;z-index:-1;inset:0;pointer-events:none;
background:linear-gradient(90deg,rgba(2,8,12,.78),transparent 18%,transparent 82%,rgba(2,8,12,.78)),
repeating-linear-gradient(112deg,transparent 0 70px,rgba(255,255,255,.018) 71px 72px)}
.roster{position:relative;z-index:7;display:grid;grid-template-columns:repeat(8,minmax(58px,1fr));gap:5px;
max-width:900px;margin:0 auto;padding:8px 60px 4px 12px}
.pchip{position:relative;display:grid;justify-items:center;gap:2px;min-width:0;border:0;background:transparent;
color:#e8e0c8;cursor:pointer;font:inherit;padding:0}
.avatar-wrap{position:relative}
.avatar{display:block;width:46px;height:46px;border:2px solid #242d2d;border-radius:50%;background:#17241c;
object-fit:cover;object-position:50% 19%;box-shadow:0 5px 14px rgba(0,0,0,.55)}
.avatar-fb{display:grid;place-items:center;width:46px;height:46px;border:2px solid #242d2d;border-radius:50%;
background:#17241c;color:var(--gold);font:700 16px Georgia,serif;box-shadow:0 5px 14px rgba(0,0,0,.55)}
.pchip:hover .avatar,.pchip.selected .avatar,.pchip:hover .avatar-fb,.pchip.selected .avatar-fb{border-color:#f2ce76;
box-shadow:0 0 0 3px rgba(237,190,92,.22),0 6px 18px rgba(0,0,0,.58)}
.pchip.selected .name{color:#ffdc87}
.pchip.settled{filter:grayscale(.8);opacity:.5}
.life-gem{position:absolute;top:-3px;right:-7px;display:grid;place-items:center;width:22px;height:22px;
transform:rotate(45deg);border:2px solid #070d11;border-radius:4px;background:linear-gradient(135deg,#6b1c18,#6a1a1b);
color:#fff;font-size:8px;font-weight:900;box-shadow:0 2px 5px #000}
.life-gem span{line-height:1;white-space:nowrap;transform:rotate(-45deg)}
.pchip.own .life-gem{background:linear-gradient(135deg,#183c6b,#1b3e6a)}
.pchip .name{max-width:115px;overflow:hidden;color:#e9e1ca;font-size:9px;font-weight:700;line-height:1.15;
text-overflow:ellipsis;text-shadow:0 2px 3px #000;white-space:nowrap}
.round-marker{position:absolute;z-index:6;top:70px;right:15px;padding:5px 10px;border:1px solid rgba(231,214,158,.35);
border-radius:999px;background:rgba(8,17,20,.84);color:var(--gold);font-family:Georgia,serif;font-size:15px;text-shadow:0 2px 2px #000}
.caption{position:relative;z-index:6;max-width:72%;margin:6px 0 0 14px;padding:4px 10px;border:1px solid rgba(226,214,168,.24);
border-radius:999px;background:rgba(6,16,18,.8);color:#dbd2b8;font-size:12px;width:fit-content}
.caption b{color:var(--gold)} .caption.win b{color:#7fd6a4} .caption.loss b{color:#e57e66}
.caption .sub{color:var(--muted);margin-left:7px;font-size:11px}
.stage-grid{position:relative;display:grid;grid-template-columns:212px minmax(0,1fr);gap:10px;padding:6px 12px 0}
.char-panel{position:relative;align-self:end;min-height:318px}
.char-art{position:absolute;bottom:132px;left:-14px;width:196px;height:186px;object-fit:contain;object-position:bottom center;
filter:drop-shadow(0 12px 13px rgba(0,0,0,.72));opacity:.96;pointer-events:none}
.trait-panel{position:absolute;top:0;right:0;left:0;z-index:5;display:grid;gap:4px;padding:5px 6px;
border:1px solid rgba(130,170,167,.28);border-radius:9px;background:rgba(7,22,23,.84);box-shadow:0 8px 22px rgba(0,0,0,.42)}
.trait-heading{display:block;margin-bottom:2px;color:#b9d3cb;font-size:8px;font-weight:850;letter-spacing:.04em;text-transform:uppercase}
.trait-row{display:flex;min-height:30px;gap:3px;flex-wrap:wrap;padding:1px}
.trait-icon{position:relative;flex:0 0 30px;width:30px;height:30px;border:1px solid #8e835e;border-radius:50%;
background:#172019;box-shadow:0 3px 8px rgba(0,0,0,.48)}
.trait-icon img{width:100%;height:100%;object-fit:contain;border-radius:50%}
.trait-icon .tt{display:grid;place-items:center;width:100%;height:100%;color:#d9cfa8;font-size:8px;text-align:center;line-height:1.05}
.trait-empty{align-self:center;color:#7e9790;font-size:10px;font-style:italic}
.char-stats{position:absolute;right:0;bottom:0;left:0;z-index:3;display:grid;gap:2px;padding:6px 8px;
border:1px solid rgba(216,205,161,.34);border-radius:8px;background:rgba(7,17,17,.9);box-shadow:0 8px 18px rgba(0,0,0,.48)}
.char-stats strong{color:#f1d58d;font-size:13px}
.char-stats span{color:#c8c0a7;font-size:10px;line-height:1.3}
.char-stats b{color:#f1d58d;font-weight:700}
.board-col{display:grid;gap:6px;align-content:end;min-width:0;padding-bottom:2px}
.deck-zone{position:relative;display:grid;grid-template-rows:auto 1fr;min-height:0;padding:16px 10px 7px;
border:1px solid rgba(69,88,81,.8);border-radius:5px 5px 14px 14px;
background:radial-gradient(ellipse at 50% 30%,rgba(194,201,182,.12),transparent 62%),
linear-gradient(180deg,rgba(121,131,119,.92),rgba(83,96,88,.94));
box-shadow:inset 0 0 55px rgba(15,25,22,.48),0 6px 18px rgba(0,0,0,.34)}
.deck-zone::before,.deck-zone::after{content:"";position:absolute;top:7px;bottom:7px;width:7px;
border-top:1px solid rgba(219,204,155,.36);border-bottom:1px solid rgba(219,204,155,.36)}
.deck-zone::before{left:5px;border-left:1px solid rgba(219,204,155,.36)}
.deck-zone::after{right:5px;border-right:1px solid rgba(219,204,155,.36)}
.hand-zone{position:relative;display:grid;grid-template-rows:auto 1fr;align-items:end;min-height:118px;padding:2px 62px 0 9px}
.zone-label{margin:0 0 3px;color:#e2d4ad;font:700 10px Georgia,serif;letter-spacing:.07em;text-align:center;
text-shadow:0 2px 3px #000;text-transform:uppercase}
.strip{display:flex;align-items:center;justify-content:center;gap:4px;min-width:0;flex-wrap:wrap}
.game-card{position:relative;width:82px;min-width:48px;max-width:88px;flex:0 1 82px;aspect-ratio:5/8;
transition:transform .12s ease,filter .12s ease}
.hand-zone .game-card{width:70px;flex-basis:70px;max-width:76px}
.game-card:hover{z-index:12;transform:translateY(-7px) scale(1.28);filter:drop-shadow(0 9px 9px rgba(0,0,0,.75))}
.game-card img{position:relative;z-index:2;display:block;width:100%;height:100%;border-radius:6px;
filter:drop-shadow(0 5px 5px rgba(0,0,0,.6));object-fit:contain}
.card-fallback{position:absolute;inset:0;display:grid;place-content:center;gap:5px;padding:8px;border:1px solid #9b8357;
border-radius:6px;background:linear-gradient(155deg,#39433a,#18241f);color:#f1dfb3;text-align:center}
.card-fallback strong{font:700 11px Georgia,serif} .card-fallback small{color:#aeb8aa;font-size:9px}
.slot-num{position:absolute;z-index:4;top:-7px;left:-5px;width:17px;height:17px;border-radius:50%;background:var(--accent);
color:#101512;font:800 10px/17px sans-serif;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.6)}
.lv-pill{position:absolute;z-index:4;right:-3px;bottom:-4px;padding:1px 5px;border:1px solid #dbc885;border-radius:999px;
background:#1b2921;color:#fff1bd;font-size:9px;font-weight:800}
.game-card.appear{filter:drop-shadow(0 0 9px rgba(127,214,164,.9))}
.game-card.appear img,.game-card.appear .card-fallback{outline:2px solid #7fd6a4;outline-offset:1px;border-radius:6px}
.game-card.leaving{opacity:.6}
.game-card.leaving img,.game-card.leaving .card-fallback{outline:2px solid #e57e66;outline-offset:1px;border-radius:6px}
.xmark{position:absolute;z-index:5;inset:0;display:grid;place-items:center;color:#ff8f75;font:800 44px/1 sans-serif;
text-shadow:0 0 10px rgba(0,0,0,.6);pointer-events:none}
.empty-slot{position:relative;width:82px;max-width:88px;flex:0 1 82px;aspect-ratio:5/8;border:1px dashed rgba(224,211,159,.31);
border-radius:7px;background:rgba(7,16,11,.13);box-shadow:inset 0 0 22px rgba(8,14,10,.25)}
.empty-slot.locked{border-color:rgba(140,150,140,.22)}
.empty-slot.locked::after{content:"锁";position:absolute;inset:0;display:grid;place-items:center;
color:rgba(180,190,175,.28);font:400 20px "Songti SC","SimSun",serif}
.exchange-counter{position:absolute;right:8px;bottom:13px;min-width:44px;padding:4px 5px;border:1px solid rgba(231,214,158,.52);
border-radius:5px;background:rgba(8,20,19,.9);color:#f4dfa5;font:850 11px Georgia,serif;text-align:center;box-shadow:0 3px 9px rgba(0,0,0,.5)}
.exchange-counter small{display:block;font-size:8px;color:#bfae7d;font-weight:700}
.private-note{align-self:center;justify-self:center;padding:13px 18px;border:1px dashed rgba(218,205,161,.28);border-radius:9px;
color:#c3bba2;background:rgba(10,18,14,.42);font-style:italic;font-size:12px}
.opp-preview{display:grid;grid-template-columns:170px minmax(0,1fr);gap:8px;min-width:0;padding:8px 10px;
border:1px solid rgba(177,154,105,.55);border-radius:14px 14px 5px 5px;
background:radial-gradient(ellipse at 70% 20%,rgba(164,123,75,.14),transparent 58%),
linear-gradient(180deg,rgba(65,63,54,.97),rgba(42,51,48,.97));
box-shadow:inset 0 0 48px rgba(5,15,14,.52),0 6px 18px rgba(0,0,0,.35)}
.opp-summary{display:grid;grid-template-columns:40px minmax(0,1fr);gap:7px;align-items:center;min-width:0}
.opp-summary img{width:40px;height:40px;border:2px solid #9b8c63;border-radius:50%;object-fit:cover;
object-position:50% 19%;box-shadow:0 4px 10px #000}
.opp-summary div{display:grid;gap:1px;min-width:0}
.opp-summary strong{overflow:hidden;color:#f2dfab;font-size:11px;text-overflow:ellipsis;white-space:nowrap}
.opp-summary span{overflow:hidden;color:#bdc7bd;font-size:9px;text-overflow:ellipsis;white-space:nowrap}
.opp-cards{display:grid;gap:3px;min-width:0}
.opp-row{display:flex;align-items:center;gap:3px;min-width:0;flex-wrap:wrap}
.opp-row .rl{flex:0 0 auto;color:#cbbd93;font:700 8px Georgia,serif;letter-spacing:.06em;text-transform:uppercase;width:34px}
.opp-preview .game-card{width:52px;flex-basis:52px;min-width:36px;max-width:56px}
.opp-preview .game-card:hover{transform:translateY(-4px) scale(1.6)}
.battle-panel{display:grid;gap:6px;margin:6px 12px 0;padding:8px 9px 9px;
border:1px solid rgba(211,198,147,.42);border-radius:9px;
background:linear-gradient(180deg,rgba(38,55,52,.96),rgba(18,32,31,.98));
box-shadow:inset 0 0 65px rgba(0,0,0,.3),0 8px 22px rgba(0,0,0,.55)}
.battle-heading{display:flex;align-items:baseline;justify-content:center;gap:9px;color:#ddcca0;
font:700 12px Georgia,serif;letter-spacing:.04em}
.battle-heading strong{color:#f6dfa0;font-size:17px}
.battle-combatant{position:relative;display:grid;grid-template-columns:196px 122px minmax(0,1fr);align-items:center;
gap:8px;min-width:0;padding:7px 9px;border:1px solid rgba(143,161,148,.36);border-radius:7px;
background:linear-gradient(90deg,rgba(49,65,59,.94),rgba(79,88,76,.8) 60%,rgba(34,50,48,.93))}
.battle-combatant.win{border-color:rgba(232,198,112,.58)}
.battle-combatant.loss{filter:saturate(.82)}
.battle-player{display:grid;grid-template-columns:46px minmax(0,1fr) 44px;align-items:center;gap:7px;min-width:0}
.battle-player>img,.battle-player>.avatar-fb{width:44px;height:44px;border:2px solid #9b8c63;border-radius:50%;
object-fit:cover;object-position:50% 19%;box-shadow:0 4px 10px #000}
.battle-player>div{display:grid;gap:2px;min-width:0}
.battle-player strong{overflow:hidden;color:#f2dfab;font-size:11px;text-overflow:ellipsis;white-space:nowrap}
.battle-player span{overflow:hidden;color:#bdc7bd;font-size:8.5px;text-overflow:ellipsis;white-space:nowrap}
.battle-stamp{color:#e4c76f;font:900 17px Georgia,serif;text-shadow:0 2px 3px #000;transform:rotate(-7deg)}
.battle-combatant.loss .battle-stamp{color:#d78c84}
.battle-combatant.draw .battle-stamp{color:#aeb9b1}
.battle-values{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px}
.battle-values>span:not(.battle-first){display:grid;gap:1px;padding:4px 5px;border:1px solid rgba(213,199,151,.2);
border-radius:5px;background:rgba(8,20,19,.42)}
.battle-values small{color:#aebbb1;font-size:7px;text-transform:uppercase}
.battle-values strong{color:#f3e5bc;font-size:12px}
.bd-delta.neg{color:#ff8b8b} .bd-delta.pos{color:#8bd8a8}
.battle-first{grid-column:1/-1;color:#e4c56c;font-size:8px;font-weight:850;text-align:center}
.battle-deck{display:flex;align-items:center;justify-content:center;gap:3px;min-width:0;flex-wrap:wrap}
.battle-deck .game-card{width:58px;min-width:38px;max-width:64px;flex-basis:58px}
.battle-deck .game-card:hover{transform:translateY(-3px) scale(1.5)}
.battle-note{align-self:center;justify-self:center;color:#c3bba2;font-style:italic;font-size:11px}
@media (max-width:900px){.battle-combatant{grid-template-columns:1fr}.opp-preview{grid-template-columns:1fr}}
.history{padding:11px 13px 13px;border-top:1px solid #3f453b;background:#10150f}
.history-head{display:flex;align-items:end;justify-content:space-between;gap:20px}
.history h2{margin:0;font-size:16px;color:#eee4c8}
.history .meta{color:var(--muted);font-size:12px}
.history ol{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:5px;margin:6px 0 0;padding:0;list-style:none}
.history li{min-height:44px;padding:6px 7px;border:1px solid var(--line);border-radius:6px;background:#1a211d;
color:#ded5bb;font-size:10px;line-height:1.25;cursor:pointer;overflow:hidden}
.history li:hover{border-color:var(--accent)}
.history li.current{border-color:#a68245;background:#24271f}
.history li .rd{color:var(--muted);margin-right:4px}
.history li .sb{display:block;color:var(--muted);margin-top:2px;font-size:9px;max-height:22px;overflow:hidden}
kbd{background:#151d18;border:1px solid var(--line);border-radius:3px;padding:0 5px;font-size:10px}
@media (max-width:900px){.stage-grid{grid-template-columns:1fr}.char-panel{min-height:150px}
.char-art{display:none}.history ol{grid-template-columns:repeat(2,1fr)}.roster{padding:8px 12px 4px}}
</style>
</head>
<body>
<div class="page">
  <div class="intro">
    <div>
      <p class="eyebrow">Match recording</p>
      <h1>@ME@ · 弈仙牌 replay</h1>
      <p class="muted">@HEADER@</p>
    </div>
  </div>
  <section class="shell">
    <div class="toolbar">
      <button id="prev" type="button" aria-label="Previous action">←</button>
      <button id="next" type="button" aria-label="Next action">→</button>
      <input id="timeline" type="range" min="0" max="@MAXI@" value="0" aria-label="timeline">
      <select id="round-select" aria-label="Jump to round"></select>
      <span id="step-label"></span>
    </div>
    <div class="stage">
      <div class="round-marker" id="round-marker"></div>
      <div class="roster" id="roster" aria-label="Players; select one to inspect"></div>
      <div class="caption" id="caption"></div>
      <section class="battle-panel" id="battle-panel" hidden></section>
      <div class="stage-grid" id="stage-grid">
        <aside class="char-panel">
          <img class="char-art" id="char-art" alt="">
          <div class="trait-panel">
            <span class="trait-heading">天命 Fates</span>
            <div class="trait-row" id="traits"></div>
          </div>
          <div class="char-stats" id="char-stats"></div>
        </aside>
        <div class="board-col">
          <div class="opp-preview" id="opp-preview" hidden></div>
          <div class="deck-zone">
            <div class="zone-label" id="deck-label">牌阵 Deck</div>
            <div class="strip" id="deck"></div>
          </div>
          <div class="hand-zone">
            <div class="zone-label" id="hand-label">手牌 Hand</div>
            <div class="strip" id="hand"></div>
            <div class="exchange-counter" id="rr"><small>换牌</small><span id="rr-n">0</span></div>
          </div>
        </div>
      </div>
    </div>
    <section class="history">
      <div class="history-head">
        <div><p class="eyebrow">At this point</p><h2>Recent actions</h2></div>
        <span class="meta">@TOTAL@ moves · <b style="color:#7fd6a4">green</b> = gained · <span style="color:#e57e66">✕</span> = leaving · <kbd>←</kbd><kbd>→</kbd></span>
      </div>
      <ol id="action-list"></ol>
    </section>
  </section>
</div>
<script>
const MOVES = @MOVES@;
const CARD_IDS = @CARD_IDS@;
const ID_NAMES = @ID_NAMES@;
const FATE_IDS = @FATE_IDS@;
const ROSTER = @ROSTER@;
const GHOSTS = @GHOSTS@;
const ROUND_STARTS = @ROUND_STARTS@;
const WIKI = "@WIKI@";
let i = 0, sel = 0;
const $ = id => document.getElementById(id);
const esc = v => String(v ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"})[c]);
function baseLv(n){ const m = n.match(/^(.*?)\\+(\\d)$/); return m ? [m[1], +m[2]+1] : [n, 1]; }
function cardHtml(name, flag, num){
  const [b, lv] = baseLv(name);
  const cid = CARD_IDS[name] || 0;
  const cls = "game-card" + (flag === 1 ? " appear" : flag === 2 ? " leaving" : "");
  return `<div class="${cls}" title="${esc(name)}">
    ${num ? `<span class="slot-num">${num}</span>` : ""}
    <span class="card-fallback"><strong>${esc(b)}</strong><small>Lv.${lv}</small></span>
    ${cid ? `<img loading="lazy" src="${WIKI}/cards/${cid}_zh.webp" alt="" onerror="this.remove()">` : ""}
    ${lv > 1 ? `<span class="lv-pill">Lv${lv}</span>` : ""}
    ${flag === 2 ? `<span class="xmark">✕</span>` : ""}
  </div>`;
}
function cardHtmlById(cid, num){
  const name = ID_NAMES[cid] || ("#" + cid);
  return `<div class="game-card" title="${esc(name)}">
    ${num ? `<span class="slot-num">${num}</span>` : ""}
    <span class="card-fallback"><strong>${esc(name)}</strong></span>
    <img loading="lazy" src="${WIKI}/cards/${cid}_zh.webp" alt="" onerror="this.remove()">
  </div>`;
}
function ghostRound(pid, rnd){
  const gh = GHOSTS[pid]; if(!gh) return null;
  const ks = Object.keys(gh.rounds).map(Number).sort((a,b)=>a-b);
  let best = null;
  for(const k of ks){ if(k <= rnd) best = k; }
  if(best === null) best = ks[0];
  return gh.rounds[best];
}
function renderRoster(m){
  const st = m.standings || {};
  $('roster').innerHTML = ROSTER.map(p => {
    const life = st[p.pid] !== undefined ? st[p.pid] : (p.pid === 0 ? m.destiny : 100);
    const dead = st[p.pid] === 0;
    const av = p.char ? `<img class="avatar" src="${WIKI}/characters/${p.char}-avatar.webp" alt=""
        onerror="this.outerHTML='<span class=avatar-fb>${esc(p.name[0])}</span>'">`
      : `<span class="avatar-fb">${esc(p.name[0])}</span>`;
    return `<button type="button" class="pchip${p.pid===0?" own":""}${p.pid===sel?" selected":""}${dead?" settled":""}"
      data-pid="${p.pid}" title="${esc(p.name)}${p.uid?" ["+esc(p.uid)+"]":""}">
      <span class="avatar-wrap">${av}<span class="life-gem"><span>${life}</span></span></span>
      <span class="name">${esc(p.name)}</span>
    </button>`;
  }).join("");
  document.querySelectorAll('.pchip').forEach(b => b.onclick = () => {
    const p = +b.dataset.pid;
    sel = (p === sel || p === 0) ? 0 : p;      // toggle preview; own avatar clears
    render();
  });
}
function renderMine(m){
  const unlocked = m.slots ?? Math.min(8, Math.max(3, m.round + 2));
  const bs = m.boardShow || m.board.map(c => [c, 0]);
  let deck = "";
  for(let k = 0; k < 8; k++){
    if(k < bs.length) deck += cardHtml(bs[k][0], bs[k][1], k + 1);
    else deck += `<div class="empty-slot${k < unlocked ? "" : " locked"}"></div>`;
  }
  $('deck').innerHTML = deck;
  $('deck-label').textContent = "牌阵 Deck";
  const hs = m.handShow || m.hand.map(c => [c, 0]);
  $('hand').innerHTML = hs.length ? hs.map(e => cardHtml(e[0], e[1])).join("")
    : `<div class="private-note">(hand empty)</div>`;
  $('hand-label').textContent = "手牌 Hand";
  $('rr').hidden = false; $('rr-n').textContent = m.rerolls;
  const meR = ROSTER[0];
  $('char-art').src = `${WIKI}/characters/${meR.char}-portrait.webp`;
  $('char-art').hidden = false;
  $('traits').innerHTML = m.talents.length ? m.talents.map(t => {
    const fid = FATE_IDS[t];
    return `<span class="trait-icon" title="${esc(t)}">${fid
      ? `<img src="${WIKI}/fates/Icon_Talent_${fid}.webp" alt=""
           onerror="if(!this.dataset.f){this.dataset.f=1;this.src='${WIKI}/fates/Icon_FateStrategy_${fid}.webp'}else{this.outerHTML='<span class=tt>${esc(t)}</span>'}">`
      : `<span class="tt">${esc(t)}</span>`}</span>`;
  }).join("") : `<span class="trait-empty">—</span>`;
  $('char-stats').innerHTML = `<strong>${esc(meR.name)} · 画师</strong>
    <span>境 <b>${m.realm}</b> · 修为 <b>${m.cult}</b> · HP <b>${m.hp}</b></span>
    <span>命 <b>${m.destiny}</b> · 换牌 <b>${m.rerolls}</b></span>`;
}
function renderPreview(m){
  const host = $('opp-preview');
  if(!sel){ host.hidden = true; host.innerHTML = ""; return; }
  const p = ROSTER.find(r => r.pid === sel);
  const gr = ghostRound(sel, m.round);
  const st = m.standings || {};
  const av = p.char ? `<img src="${WIKI}/characters/${p.char}-avatar.webp" alt=""
      onerror="this.outerHTML='<span class=avatar-fb>${esc(p.name[0])}</span>'">`
    : `<span class="avatar-fb">${esc(p.name[0])}</span>`;
  host.innerHTML = `<div class="opp-summary">${av}<div>
      <strong>${esc(p.name)}${p.uid ? " · " + esc(p.uid) : ""}</strong>
      <span>境 ${gr ? gr.level : "?"} · 修为 ${gr ? gr.exp : "?"} · 命 ${st[sel] !== undefined ? st[sel] : "?"}</span>
      <span>${gr ? `recorded board · R${m.round}` : "no recorded board"}</span></div></div>
    <div class="opp-cards">
      <div class="opp-row"><span class="rl">牌阵</span>${gr ? gr.board.map((c, k) => cardHtmlById(c, k + 1)).join("") : ""}</div>
      ${gr && gr.hand.length ? `<div class="opp-row"><span class="rl">手牌</span>${gr.hand.map(c => cardHtmlById(c)).join("")}</div>` : ""}
    </div>`;
  host.hidden = false;
}
function lifeBefore(pid){
  for(let k = i - 1; k >= 0; k--){
    const st = MOVES[k].standings;
    if(st && st[pid] !== undefined) return st[pid];
  }
  return 100;
}
function combatantHtml(cls, av, name, subs, stamp, values, deck){
  return `<article class="battle-combatant ${cls}">
    <div class="battle-player">${av}<div><strong>${name}</strong>${subs}</div>
      <b class="battle-stamp">${stamp}</b></div>
    <div class="battle-values">${values}</div>
    <div class="battle-deck">${deck}</div>
  </article>`;
}
function renderBattlePanel(m){
  const host = $('battle-panel');
  const opp = ROSTER.find(r => r.pid === m.oppPid);
  const gr = m.oppPid != null ? ghostRound(m.oppPid, m.round) : null;
  const st = m.standings || {};
  const meFirst = /I act first/.test(m.first || "");
  const myPrev = i > 0 ? MOVES[i - 1].destiny : 100;
  const myDelta = m.destiny - myPrev;
  const oppRes = m.res === "WIN" ? "loss" : m.res === "LOSS" ? "win" : "draw";
  const oppLife = opp && st[opp.pid] !== undefined ? st[opp.pid] : null;
  const oppPrev = opp ? lifeBefore(opp.pid) : null;
  const oppDelta = oppLife !== null && oppPrev !== null ? oppLife - oppPrev : 0;
  const deltaHtml = d => d ? `<span class="bd-delta ${d > 0 ? "pos" : "neg"}">${d > 0 ? "+" : ""}${d}</span>` : "";
  const meR = ROSTER[0];
  const stampTxt = {win: "胜", loss: "败", draw: "平"};
  const myVals = `<span><small>命 Destiny</small><strong>${myPrev} → ${m.destiny}${deltaHtml(myDelta)}</strong></span>
    <span><small>修为 · 境</small><strong>${m.cult} · 境${m.realm}</strong></span>
    ${meFirst ? `<span class="battle-first">◆ 先手 first action</span>` : ""}`;
  const oppVals = opp ? `<span><small>命 Destiny</small><strong>${oppPrev ?? "?"} → ${oppLife ?? "?"}${deltaHtml(oppDelta)}</strong></span>
    <span><small>修为 · 境</small><strong>${gr ? gr.exp : "?"} · 境${gr ? gr.level : "?"}</strong></span>
    ${!meFirst ? `<span class="battle-first">◆ 先手 first action</span>` : ""}` : "";
  const oppAv = opp && opp.char ? `<img src="${WIKI}/characters/${opp.char}-avatar.webp" alt=""
      onerror="this.outerHTML='<span class=avatar-fb>${esc(opp.name[0])}</span>'">`
    : `<span class="avatar-fb">${esc(opp ? opp.name[0] : "?")}</span>`;
  const meAv = `<img src="${WIKI}/characters/${meR.char}-avatar.webp" alt=""
      onerror="this.outerHTML='<span class=avatar-fb>${esc(meR.name[0])}</span>'">`;
  const oppDeck = gr ? gr.board.map((c, k) => cardHtmlById(c, k + 1)).join("")
    : `<span class="battle-note">(board not recorded)</span>`;
  const myDeck = (m.boardShow || m.board.map(c => [c, 0])).map((e, k) => cardHtml(e[0], 0, k + 1)).join("");
  host.innerHTML = `<div class="battle-heading"><span>第 ${m.round} 回合</span><strong>战斗结算 · ${esc(m.text)}</strong></div>`
    + (opp ? combatantHtml(oppRes, oppAv, esc(opp.name), `<span>${opp.uid ? esc(opp.uid) + " · " : ""}recorded ghost</span>`,
        stampTxt[oppRes], oppVals, oppDeck) : "")
    + combatantHtml(m.res.toLowerCase(), meAv, esc(meR.name), `<span>画师 Painter</span>`,
        stampTxt[m.res.toLowerCase()], myVals, myDeck);
  host.hidden = false;
}
function renderHistory(){
  const from = Math.max(0, Math.min(i - 4, MOVES.length - 10));
  let out = "";
  for(let k = from; k < Math.min(from + 10, MOVES.length); k++){
    const m = MOVES[k];
    out += `<li class="${k === i ? "current" : ""}" data-i="${k}">
      <span class="rd">R${m.round} · ${k + 1}</span>${esc(m.text)}
      ${m.sub ? `<span class="sb">${esc(m.sub)}</span>` : ""}</li>`;
  }
  $('action-list').innerHTML = out;
  document.querySelectorAll('#action-list li').forEach(li => li.onclick = () => go(+li.dataset.i));
}
function render(){
  const m = MOVES[i];
  $('round-marker').textContent = `第 ${m.round} 回合`;
  $('step-label').textContent = `Move ${i + 1} / ${MOVES.length}`;
  const cap = $('caption');
  cap.className = "caption" + (m.type === "battle" ? (m.text.startsWith("WIN") ? " win" : m.text.startsWith("LOSS") ? " loss" : "") : "");
  cap.innerHTML = `<b>${esc(m.text)}</b>${m.sub ? `<span class="sub">${esc(m.sub)}</span>` : ""}`;
  renderRoster(m);
  renderMine(m);
  renderPreview(m);
  const inBattle = m.type === "battle" && m.res;
  $('stage-grid').hidden = inBattle;
  if(inBattle) renderBattlePanel(m); else { $('battle-panel').hidden = true; }
  renderHistory();
  $('timeline').value = i;
  $('round-select').value = m.round;
  $('prev').disabled = i === 0; $('next').disabled = i === MOVES.length - 1;
}
function go(n){ i = Math.max(0, Math.min(MOVES.length - 1, n)); render(); }
$('prev').onclick = () => go(i - 1);
$('next').onclick = () => go(i + 1);
$('timeline').oninput = e => go(+e.target.value);
const rs = $('round-select');
Object.keys(ROUND_STARTS).forEach(r => {
  const o = document.createElement('option'); o.value = r; o.textContent = `Round ${r}`; rs.appendChild(o);
});
rs.onchange = () => go(ROUND_STARTS[rs.value] ?? 0);
addEventListener('keydown', e => {
  if(e.key === 'ArrowLeft'){ go(i - 1); e.preventDefault(); }
  if(e.key === 'ArrowRight'){ go(i + 1); e.preventDefault(); }
});
render();
</script>
</body>
</html>"""


def render(g: dict, moves: list) -> str:
    A = prep_assets(g, moves)

    def js(o):
        return json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    round_starts = {}
    for i, m in enumerate(moves):
        round_starts.setdefault(m["round"], i)
    out = _PAGE
    for key, val in (("@ME@", g["me"]), ("@HEADER@", g["header"]),
                     ("@MAXI@", str(len(moves) - 1)), ("@TOTAL@", str(len(moves))),
                     ("@MOVES@", js(moves)), ("@CARD_IDS@", js(A["cardIds"])),
                     ("@ID_NAMES@", js(A["idNames"])), ("@FATE_IDS@", js(A["fateIds"])),
                     ("@ROSTER@", js(A["roster"])), ("@GHOSTS@", js(A["ghosts"])),
                     ("@ROUND_STARTS@", js(round_starts)), ("@WIKI@", WIKI)):
        out = out.replace(key, val)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default=str(_HERE / "mygame" / "log.txt"))
    ap.add_argument("--out", default=str(_HERE / "mygame" / "replay.html"))
    a = ap.parse_args()
    g = parse(Path(a.log).read_text(encoding="utf-8"))
    moves = build_moves(g)
    mark_moves(moves)
    Path(a.out).write_text(render(g, moves), encoding="utf-8")
    print(f"wrote {a.out}: {len(moves)} moves across {len(g['rounds'])} rounds")


if __name__ == "__main__":
    main()
