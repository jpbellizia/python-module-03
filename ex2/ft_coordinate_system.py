#!/usr/bin/env python3
"""Exercise 2 - Position Tracker: 3D coordinates stored in tuples."""
import math


def get_player_pos() -> tuple[float, float, float]:
    """Ask for 'x,y,z' until valid, then return it as a tuple of floats."""
    while True:
        text: str = input("Enter new coordinates as floats in format "
                          "'x,y,z': ")
        if text.count(",") != 2:
            print("Invalid syntax")
        else:
            parts: list[str] = text.split(",")
            param: str = ""
            try:
                param = parts[0]
                x: float = float(param)
                param = parts[1]
                y: float = float(param)
                param = parts[2]
                z: float = float(param)
                return (x, y, z)
            except ValueError as error:
                print(f"Error on parameter '{param}': {error}")


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    """Return the Euclidean distance between two 3D points."""
    dx: float = b[0] - a[0]
    dy: float = b[1] - a[1]
    dz: float = b[2] - a[2]
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


def main() -> None:
    """Entry point: read two positions and compute distances."""
    print("=== Game Coordinate System ===")
    try:
        print("\nGet a first set of coordinates")
        first: tuple[float, float, float] = get_player_pos()
        print(f"Got a first tuple: {first}")
        print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
        center: tuple[float, float, float] = (0.0, 0.0, 0.0)
        print(f"Distance to center: {round(distance(center, first), 4)}")

        print("\nGet a second set of coordinates")
        second: tuple[float, float, float] = get_player_pos()
        result: float = round(distance(first, second), 4)
        print(f"Distance between the 2 sets of coordinates: {result}")
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted - exiting.")


if __name__ == "__main__":
    main()
