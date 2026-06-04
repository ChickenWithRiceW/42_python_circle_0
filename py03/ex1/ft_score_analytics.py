import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    int_scores = []
    # Parse trough input
    for i, score in enumerate(sys.argv[1:], start=1):
        try:
            int_scores.append(int(score))
        except Exception:
            print(f"! Invalid paramter {i}: '{score}'")
            print("-------------------------------")

    if len(int_scores) > 0:
        print("\n/----------------------------------")
        print(f"Scores processed: {int_scores}")
        print(f"Total players   : {len(int_scores)}")
        print(f"Average score   : {sum(int_scores) / len(int_scores):.2f}")
        print(f"High score      : {max(int_scores)}")
        print(f"Low score       : {min(int_scores)}")
        print(f"Score range     : {max(int_scores) - min(int_scores)}")
        print("\\----------------------------------")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")


if __name__ == "__main__":
    main()
