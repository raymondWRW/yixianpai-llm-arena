# -*- coding: utf-8 -*-
"""real9 — season-9 RAW replay rounds for the 牧逸风+炼丹师 sandbox.

Source: sharpobject/yxp_replays shards (server records). Each record's
`roundStats` FOLLOWS ONE PLAYER (homePlayerId) round by round — both sides of
every battle carry full private state:
  · handCards        — what the player HELD into the next round (hold model)
  · usedCards        — the fielded board (slot order, duplicates, levels)
  · exp / level / life — real cultivation, realm, destiny
  · replaceCardChance— 换牌 charges LEFT after the round
  · talentSelectionDatas — every fate offer: {id, selected, pendings[]}

Two harvests per shard:
  · TRAJECTORIES: records whose home player is a HUMAN 牧逸风+炼丹师 — full
    games, ~14 rounds each (the roll/realm schedule + fate-pick source).
  · PARTIAL rows: any round where a 牧逸风+炼丹师 HUMAN appears as either side
    (e.g. the record owner battling the home player) — value/hold rows only.

The median roll/realm CURVES come from the season9_builds site data (mined
over the full weighted dataset), not from shard-local samples.
"""
from __future__ import annotations

import io
import json
import tarfile
from collections import Counter, defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_DATA = _HERE / "data"
# Raw replay shards / site data are NOT bundled with the sim package (only the extracted
# real9_mu.jsonl + real9_meta.json are). Drop them under data/replay_analysis to re-extract.
_ANALYSIS = _HERE / "data" / "replay_analysis"
_SHARD_DIRS = [_ANALYSIS, _DATA / "shards9"]
_SITE_BUILDS = _ANALYSIS / "site" / "data" / "season9_builds.json"
_SITE_FATES = _ANALYSIS / "site" / "data" / "season9_fates.json"

CHAR = 1000003          # 龙瑶 (user 2026-07-22: this season's 牧逸风 meta leans
CAREER = 1              # on engine-unknown cards; elixir 龙瑶 trains cleaner)
MIN_DAOXIN = 4000       # 4k+ 道心 games only (the user's "mindset data" band)
CURVE_TIER = 1          # site curve tier: 0=all(3k+), 1=4k+, 2=6k+
OUT_GAMES = _DATA / "real9_mu.jsonl"
OUT_META = _DATA / "real9_meta.json"


def _iter_records(shard: Path):
    import zstandard
    dctx = zstandard.ZstdDecompressor()
    with open(shard, "rb") as f, dctx.stream_reader(f) as r:
        tf = tarfile.open(fileobj=io.BufferedReader(r), mode="r|")
        for m in tf:
            if not m.isfile():
                continue
            try:
                d = json.loads(tf.extractfile(m).read())
            except Exception:
                continue
            dd = d.get("data") or d
            if isinstance(dd, dict) and "roundStats" in dd:
                yield dd


def _side_row(rs, side, opp, selfp):
    pub, priv = side["publicData"], side["privateData"]
    opub, opriv = opp["publicData"], opp["privateData"]
    uid = pub.get("uid")
    ld = rs.get("lifeDamage") or 0
    return {
        "round": rs.get("round") or 0,
        "board": [int(c) for c in (priv.get("usedCards") or []) if c],
        "hand": [int(c) for c in (priv.get("handCards") or []) if c],
        "exp": pub.get("exp") or 0,
        "level": pub.get("level") or 0,
        "life": pub.get("life") or 0,
        "rolls": priv.get("replaceCardChance") or 0,
        "talents": [int(t) for t in (pub.get("talents") or [])],
        "won": rs.get("winerId") == uid,
        "first": rs.get("firstPlayerId") == uid,
        "ld": ld if selfp == "p1" else -ld,          # + = self dealt destiny
        "opp": {
            "char": opub.get("characterId") or 0,
            "career": opub.get("career") if opub.get("career") is not None else -1,
            "board": [int(c) for c in (opriv.get("usedCards") or []) if c],
            "exp": opub.get("exp") or 0,
            "level": opub.get("level") or 0,
            "life": opub.get("life") or 0,
            "talents": [int(t) for t in (opub.get("talents") or [])],
            "bot": bool(opub.get("isAI")) or str(opub.get("uid", "")).startswith("ai"),
        },
    }


def _fate_picks(priv):
    out = []
    for s in (priv.get("talentSelectionDatas") or []):
        if s.get("selected"):
            out.append({"slot": s.get("id"), "selected": s.get("selected"),
                        "pendings": [o for o in (s.get("pendings") or []) if o]})
    return out


def _is_target_human(pub):
    return (pub.get("characterId") == CHAR and pub.get("career") == CAREER
            and not pub.get("isAI")
            and not str(pub.get("uid", "")).startswith("ai"))


def shard_paths():
    out = []
    for d in _SHARD_DIRS:
        if d.is_dir():
            out += sorted(d.glob("*.tar.zst"))
    return out


def extract(shards=None, min_daoxin=MIN_DAOXIN):
    trajs, partial = [], []
    for shard in (shards or shard_paths()):
        for dd in _iter_records(shard):
            if (dd.get("beginDaoXinRankScore") or 0) < min_daoxin:
                continue
            rs_list = dd.get("roundStats") or []
            if not rs_list:
                continue
            home = rs_list[0].get("homePlayerId")
            home_rounds, home_priv = [], None
            for rs in rs_list:
                for sp in ("p1", "p2"):
                    side = rs[sp]
                    opp = rs["p2" if sp == "p1" else "p1"]
                    pub = side["publicData"]
                    if pub.get("uid") == home:
                        if _is_target_human(pub):
                            home_rounds.append(_side_row(rs, side, opp, sp))
                            home_priv = side["privateData"]
                    elif _is_target_human(pub):
                        # non-home target human — partial row
                        partial.append(_side_row(rs, side, opp, sp))
            if home_rounds:
                trajs.append({"gameId": dd.get("gameId"),
                              "daoxin": dd.get("beginDaoXinRankScore") or 0,
                              "endTs": dd.get("endTs") or 0,
                              "rounds": home_rounds,
                              "fate_picks": _fate_picks(home_priv or {})})
    return trajs, partial


def load():
    """(trajectories, partial_rows) from the extracted jsonl."""
    trajs, partial = [], []
    with open(OUT_GAMES, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            if d.get("partial"):
                partial.append(d["row"])
            else:
                trajs.append(d)
    return trajs, partial


def meta():
    return json.loads(OUT_META.read_text(encoding="utf-8"))


def _base(c):
    return c - ((c // 10000) % 100) * 10000


def mine_usage(trajs, partial):
    """Per-round REAL card usage: usage[round][base_id] = fraction of real
    boards that round fielding the card (counts multiple copies). This is the
    'what do players actually play each round' table that drives roll/hold/
    prescreen decisions (user: analysis instead of the value model)."""
    boards = defaultdict(int)
    use = defaultdict(Counter)
    rows = [r for g in trajs for r in g["rounds"]] + list(partial)
    for r in rows:
        rn = min(16, int(r["round"]))
        if not r["board"] or rn < 1:
            continue
        boards[rn] += 1
        for c in r["board"]:
            use[rn][_base(c)] += 1
    return {str(rn): {str(b): round(n / boards[rn], 4)
                      for b, n in use[rn].most_common()}
            for rn in sorted(boards)}


def mine_meta(trajs, partial=()):
    """Roll/realm medians from the SITE build data (full-dataset weighted
    medians, tier 0 = all daoxin) + fate pick stats from site + trajectories."""
    out = {"usage": mine_usage(trajs, partial)}
    try:
        b = json.loads(_SITE_BUILDS.read_text(encoding="utf-8"))
        # tier 1 = the 4k+ 道心 cumulative band (user: "4k+ dao mindset data")
        curve = b["builds"][f"{CHAR}_{CAREER}"]["curve"][CURVE_TIER]
        out["rolls_median"] = {str(i + 1): int(e[1]) for i, e in enumerate(curve) if e[0] > 0}
        out["realm_median"] = {str(i + 1): int(e[2]) for i, e in enumerate(curve) if e[0] > 0}
        out["curve_weight"] = {str(i + 1): float(e[0]) for i, e in enumerate(curve) if e[0] > 0}
    except Exception as e:
        out["curve_error"] = str(e)
    fate = defaultdict(Counter)
    fate_off = defaultdict(Counter)
    for g in trajs:
        for p in g["fate_picks"]:
            fate[p["slot"]][p["selected"]] += 1
            for o in p["pendings"]:
                fate_off[p["slot"]][o] += 1
    out["fate_picks"] = {str(s): dict(c.most_common()) for s, c in fate.items()}
    out["fate_offered"] = {str(s): dict(c.most_common()) for s, c in fate_off.items()}
    return out


if __name__ == "__main__":
    trajs, partial = extract()
    _DATA.mkdir(exist_ok=True)
    with open(OUT_GAMES, "w", encoding="utf-8") as f:
        for g in trajs:
            f.write(json.dumps(g, ensure_ascii=False) + "\n")
        for row in partial:
            f.write(json.dumps({"partial": True, "row": row}, ensure_ascii=False) + "\n")
    m = mine_meta(trajs, partial)
    OUT_META.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    nr = sum(len(g["rounds"]) for g in trajs)
    print(f"{len(trajs)} trajectories ({nr} rounds) + {len(partial)} partial rows")
    print("rolls median:", [m.get("rolls_median", {}).get(str(r)) for r in range(1, 17)])
    print("realm median:", [m.get("realm_median", {}).get(str(r)) for r in range(1, 17)])
