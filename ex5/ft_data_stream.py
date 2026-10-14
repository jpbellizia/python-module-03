"""Exercise 5 - Stream Wizard: produce and consume events with generators."""
import random
from typing import Generator

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = ["run", "eat", "sleep", "grab", "move", "climb",
                      "swim", "use", "release"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Endlessly yield random (player, action) events."""
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
        events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    """Remove a random event from the list and yield it until it's empty."""
    while len(events) > 0:
        yield events.pop(random.randrange(len(events)))


def main() -> None:
    """Entry point: stream 1000 events, then build and consume a list."""
    print("=== Game Data Stream Processor ===")
    stream: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events.append(next(stream))
    print(f"Built list of {len(events)} events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
