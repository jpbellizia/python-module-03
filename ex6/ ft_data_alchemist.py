"""Exercise 6 - Data Alchemist: list and dictionary comprehensions."""
import random


def main() -> None:
    """Entry point: transform and filter player data with comprehensions."""
    print("=== Game Data Alchemist ===\n")
    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                          "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")

    capitalized: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    only_caps: list[str] = [name for name in players if name[:1].isupper()]
    print(f"New list of capitalized names only: {only_caps}\n")

    scores: dict[str, int] = {name: random.randint(0, 1000)
                              for name in capitalized}
    print(f"Score dict: {scores}")
    if len(scores) == 0:
        print("No scores to analyse.")
        return

    average: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")

    high: dict[str, int] = {name: score for name, score in scores.items()
                            if score > average}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
