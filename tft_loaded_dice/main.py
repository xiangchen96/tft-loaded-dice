import json
from collections import Counter, defaultdict
from pathlib import Path

from .consts import LEVEL_ODDS
from .exceptions import ChampionNotFoundException

here = Path(__file__).resolve().parent

with open(here / "champions.json") as f:
    champions_data = json.load(f)

champions_data = {
    c["name"]: {
        "cost": c["cost"],
        "traits": c["traits"],
    }
    for c in champions_data
}

traits_to_units = defaultdict(list)
for c, v in champions_data.items():
    for t in v["traits"]:
        traits_to_units[t].append(c)


def champion_odds(champion):
    if champion not in champions_data:
        raise ChampionNotFoundException(f"{champion} not found")
    result = {}
    potential_units = _potential_units(champion)
    for unit in potential_units:
        unit_odds = {}
        potential_rerolled = Counter(
            champions_data[c]["cost"] for c in _potential_units(unit)
        )
        for level in range(3, 9 + 1):
            num = den = 0
            for cost in range(1, 5 + 1):
                if cost == champions_data[champion]["cost"]:
                    num += LEVEL_ODDS[level][cost] / potential_rerolled[cost]
                if potential_rerolled[cost]:
                    den += LEVEL_ODDS[level][cost]
            unit_odds[level] = num / den if den > 0 else 0
        result[unit] = unit_odds
    return result


def best_champions(champion, level):
    odds = champion_odds(champion)
    odds = [(c, odds[c][level]) for c in odds]
    return sorted(odds, key=lambda x: -x[1])


def _potential_units(champion):
    return {
        c
        for trait in champions_data[champion]["traits"]
        for c in traits_to_units[trait]
    }
