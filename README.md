## tft-loaded-dice
[![Pypi](https://img.shields.io/pypi/v/tft-loaded-dice)](https://pypi.org/project/tft-loaded-dice/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/stradivari96/tft-loaded-dice/blob/master/LICENSE)
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

best_champions("Ezreal", level=7)
# [('Ao Shin', 0.19), ('Ezreal', 0.19), ('Qiyana', 0.19), ('Twitch', 0.095), ('Lee Sin', 0.06333333333333332), ('Ornn', 0.06333333333333332), ('Xayah', 0.06333333333333332), ('Ashe', 0.0475), ('Varus', 0.0475)]

champion_odds("Shaco")
# {'Ashe': {3: 0.08333333333333334, 4: 0.1, 5: 0.11, 6: 0.13333333333333333, 7: 0.1, 8: 0.06666666666666667, 9: 0.05, 10: 0.03333333333333333, 11: 0.006666666666666666}, 'Ryze': {3: 0.08333333333333334, 4: 0.1, 5: 0.11, 6: 0.13333333333333333, 7: 0.1, 8: 0.06666666666666667, 9: 0.05, 10: 0.03333333333333333, 11: 0.006666666666666666}, 'Talon': {3: 0.08333333333333334, 4: 0.1, 5: 0.11, 6: 0.13333333333333333, 7: 0.1, 8: 0.06666666666666667, 9: 0.05, 10: 0.03333333333333333, 11: 0.006666666666666666}, 'Varus': {3: 0.08333333333333334, 4: 0.1, 5: 0.11, 6: 0.13333333333333333, 7: 0.1, 8: 0.06666666666666667, 9: 0.05, 10: 0.03333333333333333, 11: 0.006666666666666666}, 'Sejuani': {3: 0.125, 4: 0.15, 5: 0.165, 6: 0.2, 7: 0.15, 8: 0.1, 9: 0.075, 10: 0.05, 11: 0.01}, 'Xayah': {3: 0.0625, 4: 0.075, 5: 0.0825, 6: 0.1, 7: 0.075, 8: 0.05, 9: 0.0375, 10: 0.025, 11: 0.005}, 'Ezreal': {3: 0.08333333333333334, 4: 0.1, 5: 0.11, 6: 0.13333333333333333, 7: 0.1, 8: 0.06666666666666667, 9: 0.05, 10: 0.03333333333333333, 11: 0.006666666666666666}, 'Bard': {3: 0.125, 4: 0.15, 5: 0.165, 6: 0.2, 7: 0.15, 8: 0.1, 9: 0.075, 10: 0.05, 11: 0.01}, 'Twitch': {3: 0.125, 4: 0.15, 5: 0.165, 6: 0.2, 7: 0.15, 8: 0.1, 9: 0.075, 10: 0.05, 11: 0.01}}
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
