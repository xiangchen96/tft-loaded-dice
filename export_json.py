import json

from tft_loaded_dice import champion_odds, champions_data


def main():
    result = {}
    for champion in champions_data:
        odds = champion_odds(champion)
        if odds:
            result[champion] = odds
    return result


if __name__ == "__main__":
    output = main()
    with open("output.json", "w") as f:
        json.dump(output, f, ensure_ascii=False)
