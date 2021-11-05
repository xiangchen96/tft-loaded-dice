import json
from pathlib import Path

from .exceptions import ChampionNotFoundException

here = Path(__file__).resolve().parent

with open(here / "data.json") as f:
    champions_data = json.load(f)


def champion_odds(champion):
    if champion not in champions_data:
        raise ChampionNotFoundException(f"{champion} not found")

    return {
        c: {int(lvl): odds for lvl, odds in v.items()}
        for c, v in champions_data[champion].items()
    }


def best_champions(champion, level):
    odds = champion_odds(champion)
    odds = [(c, odds[c][level]) for c in odds]
    return sorted(odds, key=lambda x: -x[1])
