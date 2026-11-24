#!/usr/bin/env python3
"""Build real-games.js for the "For Real This Time" quiz.

Combines BGG data (tools/details.json, from fetch_details.py) with hand-picked tags below.
Run after updating the top 50:  python3 tools/build_real_games.py
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
details = json.loads((HERE / "details.json").read_text())

# BGG rank snapshot (id -> rank). Update with the top 50.
RANKS = [224517, 342942, 161936, 174430, 397598, 316554, 233078, 115746, 167791, 187645,
         162886, 291457, 220308, 418059, 338960, 12333, 84876, 421006, 182028, 295770,
         193738, 28720, 246900, 173346, 167355, 177736, 169786, 266507, 312484, 124361,
         341169, 373106, 205637, 237182, 164928, 120677, 192135, 266192, 251247, 96848,
         321608, 284378, 521, 365717, 183394, 390092, 324856, 199792, 436217, 366013]

# Near-duplicates left out (the higher-ranked sibling stays in).
SKIP = {316554, 28720, 291457, 295770, 341169, 365717}

SHORT = {
    397598: "Dune: Imperium – Uprising", 233078: "Twilight Imperium", 115746: "War of the Ring",
    418059: "SETI", 338960: "Slay the Spire: The Board Game", 421006: "LOTR: Duel for Middle-earth",
    182028: "Through the Ages", 246900: "Eclipse: Second Dawn", 266507: "Clank! Legacy",
    205637: "Arkham Horror: The Card Game", 96848: "Mage Knight", 321608: "Hegemony",
    183394: "Viticulture", 390092: "Ticket to Ride Legacy", 436217: "LOTR: Fate of the Fellowship",
    324856: "The Crew: Mission Deep Sea", 366013: "Heat: Pedal to the Metal",
}

# Hand tags. Scale 0 to 1.
#   coop: players work together    conflict: players attack each other directly
#   luck: dice/card swinginess      campaign: a story that continues across sessions
#   engine: build something that snowballs     themes: space, fantasy, history, nature, modern
#   blurb: one plain-English line about the game
T = {
 224517: (0, .4, .1, 0, .7, ["history"], "Build canals and railways across industrial England, then watch your network pay off."),
 342942: (0, .2, .3, 0, 1, ["nature"], "Design a modern zoo, care for animals, and fund conservation projects."),
 161936: (1, 0, .5, 1, .1, ["modern"], "Save the world from four diseases in a campaign where every game changes the board forever."),
 174430: (1, 0, .4, 1, .2, ["fantasy"], "A giant dungeon-crawling campaign where your party levels up across dozens of nights."),
 397598: (0, .8, .3, 0, .5, ["space"], "Scheme for control of the desert planet Arrakis with cards, spies, and armies."),
 233078: (0, 1, .4, 0, .5, ["space"], "An all-day galactic epic of trade, politics, betrayal, and starship battles."),
 115746: (0, 1, .6, 0, 0, ["fantasy"], "Refight all of The Lord of the Rings: armies on one side, the Ring-bearers sneaking on the other."),
 167791: (0, .3, .4, 0, 1, ["space"], "Run a corporation turning Mars green, one clever card combo at a time."),
 187645: (0, 1, .5, 0, .1, ["space"], "Play the Empire hunting the hidden Rebel base, or the Rebels trying to survive."),
 162886: (1, 0, .2, 0, .5, ["fantasy", "nature"], "Play island spirits working together to drive off invading colonists."),
 220308: (0, .3, .1, 0, .9, ["space"], "Expand an alien civilization across the galaxy in a deep, puzzly engine builder."),
 418059: (0, .3, .4, 0, .8, ["space"], "Launch probes and telescopes in a race to find signs of alien life."),
 338960: (1, 0, .5, .5, .7, ["fantasy"], "Climb a monster-filled spire together, building your deck as you go."),
 12333: (0, 1, .6, 0, 0, ["history", "modern"], "The whole Cold War as a tense two-player tug-of-war for world influence."),
 84876: (0, .2, .5, 0, .7, ["history"], "Build up your corner of medieval France with dice and lots of clever choices."),
 421006: (0, .8, .2, 0, .4, ["fantasy"], "A quick two-player duel: the Fellowship against Sauron for Middle-earth."),
 182028: (0, .6, .2, 0, .9, ["history"], "Guide a civilization from ancient times to the modern age with cards."),
 193738: (0, .3, .3, 0, .8, ["history"], "Drive cattle across the Old West to Kansas City, fine-tuning your deck along the way."),
 246900: (0, .9, .6, 0, .6, ["space"], "Explore, expand, and battle for the galaxy with customizable starships."),
 173346: (0, .7, .3, 0, .6, ["history"], "Build an ancient civilization in a fast, tense two-player card duel."),
 167355: (.6, .6, .7, 0, 0, ["space"], "Wake up on a ship full of aliens. Survive, and maybe betray your crewmates."),
 177736: (0, .1, .1, 0, .6, ["history"], "Live a Viking life of feasts, farming, raids, and a giant tile puzzle."),
 169786: (0, .6, 0, 0, .8, ["history"], "An alternate-history 1920s Europe with giant mechs and very efficient farming."),
 266507: (0, .4, .6, 1, .6, ["fantasy"], "Sneak into dungeons for loot in a funny, evolving legacy campaign."),
 312484: (0, .2, .4, 0, .7, ["history"], "Explore a jungle island for lost ruins, mixing deck building and worker placement."),
 124361: (0, .3, .1, 0, .6, ["history"], "Build a trading empire across the ancient Mediterranean. Elegant and thinky."),
 373106: (1, 0, .6, .5, 0, ["modern"], "Two pilots try to land a plane together without talking. Short and tense."),
 205637: (1, 0, .6, 1, .4, ["fantasy"], "Investigate eerie mysteries in a story-driven card campaign for one or two."),
 237182: (0, 1, .5, 0, .4, ["fantasy", "nature"], "Cute woodland animals fight a war where every faction plays by different rules."),
 164928: (0, .2, .4, 0, .8, ["history"], "Build a following in medieval France by pulling the right people from your bag."),
 120677: (0, .5, 0, 0, .8, ["fantasy"], "Transform the land for your fantasy race in a no-luck strategy classic."),
 192135: (1, 0, .8, .5, .4, ["fantasy"], "A dice-chucking adventure where your heroes build up wild combos together."),
 266192: (0, .1, .5, 0, 1, ["nature"], "Attract birds to your wildlife preserves in a relaxing, gorgeous engine builder."),
 251247: (0, .6, .1, 0, .7, ["modern"], "Build dams and fight over water flow in a cutthroat engineering game."),
 96848: (.3, .3, .4, .3, .7, ["fantasy"], "An epic solo-friendly adventure: conquer cities and level up a mighty hero."),
 321608: (0, .7, .2, 0, .4, ["modern"], "Lead a social class in a modern society and negotiate your way to the top."),
 284378: (0, .3, .1, 0, .6, ["modern"], "Run an electric car factory under a famously demanding manager."),
 521: (0, .9, .4, 0, 0, ["modern"], "Flick wooden discs across a round board. Simple, physical, and endlessly fun."),
 183394: (0, .2, .5, 0, .7, ["nature", "history"], "Run a Tuscan vineyard: plant, harvest, make wine, and fill orders."),
 390092: (0, .4, .5, 1, .3, ["history"], "Build railroads across the American West in a 12-game legacy campaign."),
 324856: (1, 0, .5, 1, 0, ["modern"], "A cooperative trick-taking card game with dozens of missions to complete together."),
 199792: (0, .2, .4, 0, 1, ["nature", "fantasy"], "Build a cozy woodland city of critters and constructions."),
 436217: (1, 0, .5, 0, .3, ["fantasy"], "Work together to get the Ring to Mount Doom before the darkness spreads."),
 366013: (0, .6, .6, 0, .2, ["modern"], "Race 1960s cars, managing your engine heat so you don't burn out on the turns."),
}


def heavy(w):
    return round(min(1, max(0, (w - 1.2) / 3.25)), 2)


def long(t):
    pts = [(20, 0), (30, .05), (60, .25), (90, .4), (120, .55), (150, .7), (180, .8), (240, .95), (480, 1)]
    for (t1, v1), (t2, v2) in zip(pts, pts[1:]):
        if t <= t1:
            return v1
        if t <= t2:
            return round(v1 + (v2 - v1) * (t - t1) / (t2 - t1), 2)
    return 1


def duo(d):
    best = [int(b) for b in d["best"] if b.isdigit()]
    if d["maxplayers"] == 2:
        return 1
    if best and max(best) <= 2:
        return .75
    if best and min(best) >= 5:
        return 0
    if best and max(best) >= 4:
        return .3
    return .45


def crowd(d):
    m = d["maxplayers"]
    return 1 if m >= 5 else (.4 if m >= 4 else 0)


games = []
for rank, gid in enumerate(RANKS, 1):
    if gid in SKIP:
        continue
    d = details[str(gid)]
    coop, conflict, luck, campaign, engine, themes, blurb = T[gid]
    games.append({
        "id": gid, "rank": rank, "name": SHORT.get(gid, d["name"]),
        "thumb": d["thumbnail"], "image": d["image"],
        "weight": round(d["weight"], 2), "time": int(d["playingtime"]),
        "min": int(d["minplayers"]), "max": int(d["maxplayers"]),
        "blurb": blurb, "themes": themes,
        "dims": {"heavy": heavy(d["weight"]), "long": long(d["playingtime"]), "coop": coop,
                 "conflict": conflict, "luck": luck, "campaign": campaign, "engine": engine,
                 "duo": duo(d), "crowd": crowd(d)},
    })

out = HERE.parent / "real-games.js"
out.write_text("// Generated by tools/build_real_games.py. Do not edit by hand.\n"
               "const REAL_GAMES = " + json.dumps(games, indent=1, ensure_ascii=False) + ";\n")
print(f"Wrote {len(games)} games to {out}")
