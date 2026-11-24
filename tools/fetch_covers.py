#!/usr/bin/env python3
"""Fetch box cover image links from the BoardGameGeek XML API.

The API token is read from the macOS Keychain (service "bgg-api-token"),
never from this file. Saves results to tools/covers.json.

Usage:
  python3 tools/fetch_covers.py 224517 342942 ...      # look up game ids
  python3 tools/fetch_covers.py --search "Monopoly Junior"  # find ids by name
"""
import json, subprocess, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

API = "https://boardgamegeek.com/xmlapi2/"
OUT = Path(__file__).with_name("covers.json")


def token():
    return subprocess.run(
        ["security", "find-generic-password", "-s", "bgg-api-token", "-a", "bgg", "-w"],
        check=True, capture_output=True, text=True,
    ).stdout.strip()


def get(path, params):
    url = API + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token()}",
        "User-Agent": "board-game-quiz/1.0",
    })
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                if r.status == 202:  # BGG says "queued, try again"
                    time.sleep(3)
                    continue
                return ET.fromstring(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (202, 429, 500, 503):
                time.sleep(5)
                continue
            raise
    raise RuntimeError("BGG API kept asking us to wait. Try again in a minute.")


def lookup(ids):
    results = {}
    for i in range(0, len(ids), 20):  # API allows 20 ids per request
        root = get("thing", {"id": ",".join(ids[i:i + 20]), "type": "boardgame"})
        for item in root.findall("item"):
            name = item.find("name[@type='primary']")
            results[item.get("id")] = {
                "name": name.get("value") if name is not None else "",
                "thumbnail": (item.findtext("thumbnail") or "").strip(),
                "image": (item.findtext("image") or "").strip(),
            }
        time.sleep(2)  # be polite
    return results


def search(query):
    root = get("search", {"query": query, "type": "boardgame"})
    for item in root.findall("item"):
        name = item.find("name")
        year = item.find("yearpublished")
        print(item.get("id"), name.get("value") if name is not None else "",
              year.get("value") if year is not None else "")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--search"]:
        search(" ".join(args[1:]))
    else:
        data = lookup(args)
        OUT.write_text(json.dumps(data, indent=2))
        print(f"Saved {len(data)} games to {OUT}")
