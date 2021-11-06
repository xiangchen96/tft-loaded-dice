## tft-loaded-dice
[![Pypi](https://img.shields.io/pypi/v/tft-loaded-dice)](https://pypi.org/project/tft-loaded-dice/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/stradivari96/tft-loaded-dice/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/stradivari96/tft-loaded-dice/branch/main/graph/badge.svg?token=NYKUYQR8ZG)](https://codecov.io/gh/stradivari96/tft-loaded-dice)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<a href="https://gitmoji.dev">
  <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg" alt="Gitmoji">
</a>

![loaded dice](https://static.wikia.nocookie.net/leagueoflegends/images/b/b7/Twisted_Fate_Loaded_Dice.png)
## Usage
Use the resulting [json](https://raw.githubusercontent.com/stradivari96/tft-loaded-dice/main/tft_loaded_dice/data.json)

or
```
pip install tft-loaded-dice
```
```python
from tft_loaded_dice import best_champions, champion_odds

best_champions("Jayce", level=7)
# [('Zilean', 0.01), ('Jayce', 0.01), ('Caitlyn', 0.01), ('Fiora', 0.005), ('Singed', 0.005), ('Ezreal', 0.005), ('Heimerdinger', 0.005), ('Seraphine', 0.005), ('Vi', 0.003333333333333333)]

champion_odds("Shaco")
# {'Ekko': {3: 0.0, 4: 0.075, 5: 0.1, 6: 0.15, 7: 0.175, 8: 0.175, 9: 0.15, 10: 0.1, 11: 0.06}, 'Braum': {3: 0.0, 4: 0.075, 5: 0.1, 6: 0.15, 7: 0.175, 8: 0.175, 9: 0.15, 10: 0.1, 11: 0.06}, 'Talon': {3: 0.0, 4: 0.05, 5: 0.06666666666666667, 6: 0.1, 7: 0.11666666666666665, 8: 0.11666666666666665, 9: 0.1, 10: 0.06666666666666667, 11: 0.04}, 'Shaco': {3: 0.0, 4: 0.075, 5: 0.1, 6: 0.15, 7: 0.175, 8: 0.175, 9: 0.15, 10: 0.1, 11: 0.06}, 'Twisted Fate': {3: 0.0, 4: 0.05, 5: 0.06666666666666667, 6: 0.1, 7: 0.11666666666666665, 8: 0.11666666666666665, 9: 0.1, 10: 0.06666666666666667, 11: 0.04}, 'Twitch': {3: 0.0, 4: 0.0375, 5: 0.05, 6: 0.075, 7: 0.0875, 8: 0.0875, 9: 0.075, 10: 0.05, 11: 0.03}, 'Darius': {3: 0.0, 4: 0.075, 5: 0.1, 6: 0.15, 7: 0.175, 8: 0.175, 9: 0.15, 10: 0.1, 11: 0.06}, 'Akali': {3: 0.0, 4: 0.075, 5: 0.1, 6: 0.15, 7: 0.175, 8: 0.175, 9: 0.15, 10: 0.1, 11: 0.06}, 'Katarina': {3: 0.0, 4: 0.05, 5: 0.06666666666666667, 6: 0.1, 7: 0.11666666666666665, 8: 0.11666666666666665, 9: 0.1, 10: 0.06666666666666667, 11: 0.04}, 'Zyra': {3: 0.0, 4: 0.05, 5: 0.06666666666666667, 6: 0.1, 7: 0.11666666666666665, 8: 0.11666666666666665, 9: 0.1, 10: 0.06666666666666667, 11: 0.04}}
```

## Development

1. Install poetry

https://python-poetry.org/docs/#installation

2. Install dependencies
```
poetry install
poetry run pre-commit install
```

3. Run test
```
poetry run pytest --cov=tft_loaded_dice --cov-fail-under=80 --cov-report xml
```

## References
* https://github.com/alanz132/loadedDiceOdds
* https://giantslayer.tv/blogs/5261054387/correctly-using-loaded-dice/
* https://www.reddit.com/r/CompetitiveTFT/comments/kw4ah7/loaded_die_odds_for_every_champion/
* https://raw.communitydragon.org/latest/cdragon/tft/en_gb.json
