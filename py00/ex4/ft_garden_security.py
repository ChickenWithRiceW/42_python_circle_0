class Plant:
    def __init__(self, name: str, height: float, age_v: int,
                 growth_speed: float) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self._growth_speed = 0.0
        self.set_height(height)
        self.set_age(age_v)
        self.set_growth_speed(growth_speed)

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 2)}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self._growth_speed

    def age(self) -> None:
        self._age += 1

    def grow_in_days(self, days: int = 1) -> None:
        for day in range(days):
            self.grow()
            self.age()

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def set_growth_speed(self, new_growth_speed: float) -> None:
        if new_growth_speed >= 0:
            self._growth_speed = new_growth_speed
        else:
            print(f"{self.name}: Error, growth speed can't be negative")
            print("Growth speed update rejected")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)

    def get_growth_speed(self) -> float:
        return (self._growth_speed)


def main() -> None:
    melon: Plant = Plant("Melon", 10.00, 2, 1.00)
    print("Plant created: ", end='')
    melon.show()

    melon.set_height(25.00)
    print(f"Height updated: {melon.get_height()}cm")
    melon.set_age(10)
    print(f"Age updated: {melon.get_age()} days old")

    melon._age = 21
    melon.set_height(-1)
    melon.set_age(-1)

    print("Current state: ", end='')
    melon.show()


if __name__ == "__main__":
    main()
