import json
from collections import Counter, defaultdict
from pathlib import Path

LEVEL_ODDS = {
    1: {1: 100, 2: 0, 3: 0, 4: 0, 5: 0},
    2: {1: 100, 2: 0, 3: 0, 4: 0, 5: 0},
    3: {1: 75, 2: 25, 3: 0, 4: 0, 5: 0},
    4: {1: 55, 2: 30, 3: 15, 4: 0, 5: 0},
    5: {1: 45, 2: 33, 3: 20, 4: 2, 5: 0},
    6: {1: 25, 2: 40, 3: 30, 4: 5, 5: 0},
    7: {1: 19, 2: 30, 3: 35, 4: 15, 5: 1},
    8: {1: 15, 2: 20, 3: 35, 4: 25, 5: 5},
    9: {1: 10, 2: 15, 3: 30, 4: 30, 5: 15},
    10: {1: 5, 2: 10, 3: 20, 4: 40, 5: 25},
    11: {1: 1, 2: 2, 3: 12, 4: 50, 5: 35},
}


def get_output():
    champions_data = get_champions_data()
    traits_to_units = defaultdict(list)
    for c, v in champions_data.items():
        for t in v["traits"]:
            traits_to_units[t].append(c)

    result = {}
    for champion in champions_data:
        odds = champion_odds(champion, champions_data, traits_to_units)
        if odds:
            result[champion] = odds
    return result


def get_champions_data():
    here = Path(__file__).resolve().parent
    with open(here / "en_gb.json") as f:
        data = json.load(f)
    champions_data = {
        c["name"]: {
            "cost": c["cost"],
            "traits": [t.strip() for t in c["traits"]],
            "icon": format_icon(c["icon"]),
        }
        for c in data["sets"]["6"]["champions"]
        if c["traits"]
    }
    return champions_data


def format_icon(icon):
    icon = icon.lower().replace(".dds", ".png")
    split = icon.split(".")
    split[0] += "_mobile"
    return f"https://raw.communitydragon.org/latest/game/{'.'.join(split)}"


def champion_odds(champion, champions_data, traits_to_units):
    result = {}
    potential_units = get_potential_units(champion, champions_data, traits_to_units)
    for unit in potential_units:
        unit_odds = {}
        potential_rerolled = Counter(
            champions_data[c]["cost"]
            for c in get_potential_units(unit, champions_data, traits_to_units)
        )
        for level in range(3, 11 + 1):
            num = den = 0
            for cost in range(1, 5 + 1):
                if cost == champions_data[champion]["cost"]:
                    num += LEVEL_ODDS[level][cost] / potential_rerolled[cost]
                if potential_rerolled[cost]:
                    den += LEVEL_ODDS[level][cost]
            unit_odds[level] = num / den if den > 0 else 0
        result[unit] = unit_odds
    return result


def get_potential_units(champion, champions_data, traits_to_units):
    return {
        c
        for trait in champions_data[champion]["traits"]
        for c in traits_to_units[trait]
    }


if __name__ == "__main__":
    output = get_output()
    with open("tft_loaded_dice/data.json", "w") as f:
        json.dump(output, f, ensure_ascii=False)
