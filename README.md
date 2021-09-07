## tft-loaded-dice
[![Pypi](https://img.shields.io/pypi/v/tft-loaded-dice)](https://pypi.org/project/tft-loaded-dice/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/stradivari96/tft-loaded-dice/blob/master/LICENSE)

[![codecov](https://codecov.io/gh/stradivari96/tft-loaded-dice/branch/main/graph/badge.svg?token=NYKUYQR8ZG)](https://codecov.io/gh/stradivari96/tft-loaded-dice)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![loaded dice](https://static.wikia.nocookie.net/leagueoflegends/images/b/b7/Twisted_Fate_Loaded_Dice.png)
## Usage
```
pip install tft-loaded-dice
```
```python
from tft_loaded_dice import best_champions, champion_odds

best_champions("Gwen", level=7)
# [('Gwen', 0.0196078431372549), ('Lux', 0.005), ('Lulu', 0.005), ('Fiddlesticks', 0.005)]

champion_odds("Nocturne")
# {'Nocturne': {3: 0.0, 4: 0.15, 5: 0.2, 6: 0.3, 7: 0.35, 8: 0.35, 9: 0.3}, 'Fiddlesticks': {3: 0.0, 4: 0.0375, 5: 0.05, 6: 0.075, 7: 0.0875, 8: 0.0875, 9: 0.075}, 'Volibear': {3: 0.0, 4: 0.075, 5: 0.1, 6: 0.15, 7: 0.175, 8: 0.175, 9: 0.15}, 'Pyke': {3: 0.0, 4: 0.075, 5: 0.1, 6: 0.15, 7: 0.175, 8: 0.175, 9: 0.15}, 'Viego': {3: 0.0, 4: 0.0375, 5: 0.05, 6: 0.075, 7: 0.0875, 8: 0.0875, 9: 0.075}, 'Diana': {3: 0.0, 4: 0.05, 5: 0.06666666666666667, 6: 0.1, 7: 0.11666666666666665, 8: 0.11666666666666665, 9: 0.1}, "Kha'Zix": {3: 0.0, 4: 0.05, 5: 0.06666666666666667, 6: 0.1, 7: 0.11666666666666665, 8: 0.11666666666666665, 9: 0.1}, 'Ivern': {3: 0.0, 4: 0.075, 5: 0.1, 6: 0.15, 7: 0.175, 8: 0.175, 9: 0.15}}

```

## References
* https://github.com/alanz132/loadedDiceOdds
* https://giantslayer.tv/blogs/5261054387/correctly-using-loaded-dice/
* https://www.reddit.com/r/CompetitiveTFT/comments/kw4ah7/loaded_die_odds_for_every_champion/

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

* Gitmoji: https://gitmoji.dev/
* Black: https://black.readthedocs.io/en/stable/
* Isort: https://pycqa.github.io/isort/
* Poetry: https://python-poetry.org/