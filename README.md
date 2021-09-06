## tft-loaded-dice
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/stradivari96/tft-loaded-dice/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/stradivari96/tft-loaded-dice/branch/main/graph/badge.svg?token=NYKUYQR8ZG)](https://codecov.io/gh/stradivari96/tft-loaded-dice)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Usage
TODO

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