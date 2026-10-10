#!/usr/bin/env python3
import sys


def main() -> None:
    """Display the program name and every command-line argument."""
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    arguments: list[str] = sys.argv[1:]
    if len(arguments) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(arguments)}")
        position: int = 1
        for argument in arguments:
            print(f"Argument {position}: {argument}")
            position += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
