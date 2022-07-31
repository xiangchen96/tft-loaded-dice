import pytest

from tft_loaded_dice import best_champions, champion_odds
from tft_loaded_dice.exceptions import ChampionNotFoundException


def test_not_found():
    with pytest.raises(ChampionNotFoundException):
        champion_odds("Bob")


@pytest.mark.parametrize(
    "champion,level,best",
    [("Ornn", 8, "Lee Sin"), ("Corki", 7, "Tristana")],
)
def test_best_champions(champion, level, best):
    assert best_champions(champion, level)[0][0] == best
