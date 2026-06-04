import random
import typing

player_event = tuple[str, str]


def consume_event(player_list: list[player_event]) -> typing.Generator[
        player_event, None, None]:
    while player_list:
        event = random.choice(player_list)
        print(f"\nGot event from list: {event}")
        player_list.remove(event)
        yield event


def gen_event() -> typing.Generator[player_event, None, None]:
    players = ["Ivo", "Baran", "Mark", "Félix", "Artem"]
    events = ["died", "exploded", "got stabbed", "started flying", "ate grass"]
    while True:
        yield (random.choice(players), random.choice(events))


def main() -> None:
    generator_event = gen_event()
    for i in range(1000):
        player_name, event = next(generator_event)
        print(f"Event {i}: Player {player_name} {event}")

    event_list = []
    for i in range(10):
        event_list.append(next(generator_event))
    print(f"Build list of 10 events: {event_list}")

    for _ in consume_event(event_list):
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
