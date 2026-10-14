import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer", "Strategist",
    "Unstoppable", "Speed Runner", "Survivor", "Treasure Hunter",
    "First Steps", "Sharp Mind", "Hidden Path Finder", "Night Owl",
    "Perfectionist", "Lucky Shot", "Team Player", "Lore Master",
    "Dragon Tamer",
]


def gen_player_achievements() -> set[str]:
    """Return a random set of achievements picked from ACHIEVEMENTS.

    Picking about half of the list keeps both the common set and each
    player's exclusive set likely to be non-empty.
    """
    count: int = random.randint(8, 12)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    """Entry point: generate players and analyse their achievements."""
    print("=== Achievement Tracker System ===\n")
    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    players: list[tuple[str, set[str]]] = []
    for name in names:
        achievements: set[str] = gen_player_achievements()
        players.append((name, achievements))
        print(f"Player {name}: {achievements}")

    """ '_' its a convention to describe something that you will not use,
     but exist, and you want to disconsider.
    """
    all_sets: list[set[str]] = []
    for _, achievements in players:
        all_sets.append(achievements)
    """ '*' is the same to write set().union(alicem bobm charlie, dylan)"""
    distinct: set[str] = set().union(*all_sets)
    print(f"\nAll distinct achievements: {distinct}")
    # same as alice.intersection(bob, charlie, dylan)
    common: set[str] = all_sets[0].intersection(*all_sets[1:])
    print(f"\nCommon achievements: {common}\n")
    '''
    loop to find who is not the currently player
    '''
    for name, achievements in players:
        others: list[set[str]] = []
        for other_name, other_set in players:
            if other_name != name:
                others.append(other_set)
        print(f"Only {name} has: {achievements.difference(*others)}")

    print()
    '''
    show all achievements is missing to the player
    '''
    every_achievement: set[str] = set(ACHIEVEMENTS)
    for name, achievements in players:
        missing: set[str] = every_achievement.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
