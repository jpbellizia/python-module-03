#!/usr/bin/env python3
import sys


def parse_scores(arguments: list[str]) -> list[int]:
    """Convert arguments to int scores, reporting and skipping bad ones."""
    scores: list[int] = []
    for argument in arguments:
        try:
            scores.append(int(argument))
        except ValueError:
            print(f"Invalid parameter: '{argument}'")
    return scores


def show_stats(scores: list[int]) -> None:
    """Print basic infos"""
    total: int = sum(scores)
    high: int = max(scores)
    low: int = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {total / len(scores)}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


def main() -> None:
    """Entry point: parse the scores, then display the analytics."""
    print("=== Player Score Analytics ===")
    scores: list[int] = parse_scores(sys.argv[1:])
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    show_stats(scores)


if __name__ == "__main__":
    main()
