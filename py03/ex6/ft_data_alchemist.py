import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    player_names = ["Félix", "artem", "Achilles", "Mark", "ivo",
                    "daniil", "Paul", "Martin", "elly"]
    print(f"Initial list of players: {player_names}")

    player_names_u = [p.capitalize() for p in player_names]
    print(f"New list with all names capitalize: {player_names_u}")

    player_names_only_u = [p for p in player_names if p[0].isupper()]
    print(f"New list of capitalized names only: {player_names_only_u}\n")

    score_dict = {p: random.randint(0, 1000) for p in player_names}
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    int_average = round(average)
    high_score_dict = {p: score_dict[p] for p in score_dict
                       if score_dict[p] > int_average}
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    main()
