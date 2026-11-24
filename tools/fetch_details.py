#!/usr/bin/env python3
"""Fetch game details (complexity, time, players, mechanics, covers) from BGG.

Uses the token in the macOS Keychain via fetch_covers.get(). Writes tools/details.json.
Usage: python3 tools/fetch_details.py 224517 342942 ...
"""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fetch_covers import get

OUT = Path(__file__).with_name("details.json")


def num(item, tag):
    el = item.find(tag)
    try:
        return float(el.get("value")) if el is not None else None
    except (TypeError, ValueError):
        return None


def best_players(item):
    """Player counts the community voted 'Best' (more Best votes than Not Recommended)."""
    best = []
    poll = item.find("poll[@name='suggested_numplayers']")
    if poll is None:
        return best
    for res in poll.findall("results"):
        votes = {r.get("value"): int(r.get("numvotes")) for r in res.findall("result")}
        if votes.get("Best", 0) > max(votes.get("Recommended", 0), votes.get("Not Recommended", 0)):
            best.append(res.get("numplayers"))
    return best


def main(ids):
    out = {}
    for i in range(0, len(ids), 20):
        root = get("thing", {"id": ",".join(ids[i:i + 20]), "type": "boardgame", "stats": 1})
        for item in root.findall("item"):
            name = item.find("name[@type='primary']")
            links = lambda t: [l.get("value") for l in item.findall(f"link[@type='{t}']")]
            out[item.get("id")] = {
                "name": name.get("value"),
                "year": num(item, "yearpublished"),
                "minplayers": num(item, "minplayers"),
                "maxplayers": num(item, "maxplayers"),
                "playingtime": num(item, "playingtime"),
                "weight": num(item, "statistics/ratings/averageweight"),
                "rating": num(item, "statistics/ratings/average"),
                "best": best_players(item),
                "categories": links("boardgamecategory"),
                "mechanics": links("boardgamemechanic"),
                "thumbnail": (item.findtext("thumbnail") or "").strip(),
                "image": (item.findtext("image") or "").strip(),
            }
        time.sleep(2)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Saved {len(out)} games to {OUT}")


if __name__ == "__main__":
    main(sys.argv[1:])
