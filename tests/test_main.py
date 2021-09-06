import pytest

from tft_loaded_dice import best_champions, champion_odds
from tft_loaded_dice.exceptions import ChampionNotFoundException


def test_not_found():
    with pytest.raises(ChampionNotFoundException):
        champion_odds("Bob")


@pytest.mark.parametrize(
    "champion,level,best", [("Gwen", 9, "Gwen"), ("Fiddlesticks", 9, "Gwen")]
)
def test_best_champions(champion, level, best):
    assert best_champions(champion, level)[0][0] == best


@pytest.mark.parametrize(
    "champion,odds",
    [
        (
            "Teemo",
            {
                "Ziggs": {3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.01, 8: 0.05, 9: 0.15},
                "Kled": {3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.01, 8: 0.05, 9: 0.15},
                "Syndra": {
                    3: 0.0,
                    4: 0.0,
                    5: 0.0,
                    6: 0.0,
                    7: 0.005,
                    8: 0.025,
                    9: 0.075,
                },
                "Kennen": {
                    3: 0.0,
                    4: 0.0,
                    5: 0.0,
                    6: 0.0,
                    7: 0.005,
                    8: 0.025,
                    9: 0.075,
                },
                "Poppy": {3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.005, 8: 0.025, 9: 0.075},
                "Tristana": {3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.01, 8: 0.05, 9: 0.15},
                "Teemo": {3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.01, 8: 0.05, 9: 0.15},
                "Lulu": {3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.005, 8: 0.025, 9: 0.075},
                "Ivern": {
                    3: 0.0,
                    4: 0.0,
                    5: 0.0,
                    6: 0.0,
                    7: 0.003333333333333333,
                    8: 0.016666666666666666,
                    9: 0.05,
                },
                "Karma": {3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.005, 8: 0.025, 9: 0.075},
            },
        ),
        (
            "Riven",
            {
                "Kalista": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Garen": {
                    3: 0.0,
                    4: 0.075,
                    5: 0.1,
                    6: 0.15,
                    7: 0.175,
                    8: 0.175,
                    9: 0.15,
                },
                "Aatrox": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Gragas": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Nidalee": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Kha'Zix": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Soraka": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Kayle": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Draven": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Irelia": {
                    3: 0.0,
                    4: 0.03,
                    5: 0.04,
                    6: 0.06,
                    7: 0.07,
                    8: 0.07,
                    9: 0.06,
                },
                "Riven": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Yasuo": {
                    3: 0.0,
                    4: 0.05,
                    5: 0.06666666666666667,
                    6: 0.1,
                    7: 0.11666666666666665,
                    8: 0.11666666666666665,
                    9: 0.1,
                },
                "Karma": {
                    3: 0.0,
                    4: 0.075,
                    5: 0.1,
                    6: 0.15,
                    7: 0.175,
                    8: 0.175,
                    9: 0.15,
                },
            },
        ),
    ],
)
def test_get_champion_odds(champion, odds):
    assert champion_odds(champion) == odds
