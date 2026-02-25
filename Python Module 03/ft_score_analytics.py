import sys


def main():
    print("=== Player Score Analytics ===")
    argv = sys.argv
    argc = len(argv)
    if (argc == 1):
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    if (argc > 1):
        scores = []
        for i in range(1, argc):
            try:
                number = int(argv[i])
                scores.append(number)
            except ValueError as e:
                print(f"Error: {e}")
        if (len(scores) > 0):
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores)/len(scores): .1f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
