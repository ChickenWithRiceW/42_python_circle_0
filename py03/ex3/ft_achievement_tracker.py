import random

WHITE = "\033[97m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"


def gen_player_achievements() -> set[str]:
    common_set = {"Wrong way", "Talk to a NPC", "Read a magic script",
                  "Walked 100 miles", "Found Frank", "Normal ending"}
    normal_set = {"Killed 9 orgs", "Weird boss ending", "Saw secret Frank"}
    rare_set = {"100% Game Completion", "No death", "Unlocked black magic"}

    sets = [common_set, normal_set, rare_set]
    colors = [WHITE, YELLOW, RED]
    user_set = set()

    for _ in sets * random.randint(1, 4):
        index = random.choices([0, 1, 2], weights=[60, 35, 5], k=1)[0]
        picked = random.choice(list(sets[index]))
        user_set.add(f"{colors[index]}{picked}{RESET}")
    return user_set


class Player:
    all_players: list["Player"] = []

    def __init__(self, name: str):
        self.name = name
        self.set = gen_player_achievements()
        self.all_players.append(self)

    def super_show(self) -> None:
        print(f"Player {self.name}:")

        print("Has:")
        self.show_own_achievements()

        print("Uniq:")
        self.show_own_uniq_achievements()
        print("Missing:")
        self.show_missing_achievements()
        print("")

    def show_own_achievements(self) -> None:
        for achievement in self.set:
            print(f"|  {achievement:<30}{'|'}")
        print("-------------------------")

    def show_missing_achievements(self) -> None:
        copy_list = Player.all_players.copy()
        copy_list.remove(self)
        all_others = set.union(*[p.set for p in copy_list])

        difference = all_others.difference(self.set)
        for achievement in difference:
            print(f"|  {achievement:<30}{'|'}")
        print("⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")

    def show_own_uniq_achievements(self) -> None:
        copy_list = Player.all_players.copy()
        copy_list.remove(self)
        uniq_to_self = self.set.difference(*[p.set for p in copy_list])
        if len(uniq_to_self) != 0:
            for achievement in uniq_to_self:
                print(f"|  {achievement:<30}{'|'}")
        else:
            print("|  Nothing uniq :(")
        print("-------------------------")

    @classmethod
    def show_all_achievments(cls) -> None:
        print("\nAll distinct achievements:")
        set_of_uniq = set.union(*[p.set for p in cls.all_players])
        for achievement in set_of_uniq:
            print(f"|  {achievement:<30}{'|'}")

    @classmethod
    def show_shared_achievements(cls) -> None:
        print("\nCommon achievement:")
        set_of_shared = set.intersection(*[p.set for p in cls.all_players])
        if len(set_of_shared) != 0:
            for achievement in set_of_shared:
                print(f"|  {achievement:<30}{'|'}")
        else:
            print("|  Nothing in common :(")
        print("⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")


def main() -> None:
    print("=== Achievement Tracker System ===")
    paul = Player("Paul")
    mark = Player("Mark")
    elin = Player("Elin")
    fabienne = Player("Fabienne")

    print("=========PLAYER=========")
    paul.super_show()
    mark.super_show()
    elin.super_show()
    fabienne.super_show()

    print("======PLAYER STATS======")
    Player.show_all_achievments()
    Player.show_shared_achievements()


if __name__ == "__main__":
    main()
