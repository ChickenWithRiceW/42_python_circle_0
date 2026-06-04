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


class Flower(Plant):
    def __init__(self, name: str, height: float, age_v: int,
                 growth_speed: float, color: str) -> None:
        super().__init__(name, height, age_v, growth_speed)
        self.color = color.capitalize()
        self._bloom_status = False

    def bloom(self) -> None:
        if self._bloom_status is False:
            self._bloom_status = True
        else:
            print(f"{self.name} is already blooming!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloom_status is False:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age_v: int,
                 growth_speed: float,  trunk_diameter: float) -> None:
        super().__init__(name, height, age_v, growth_speed)
        self._trunk_diameter = 0.0
        self.set_trunk_diameter(trunk_diameter)

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of {self._height}cm long"
            f" and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def set_trunk_diameter(self, new_trunk_diameter: float) -> None:
        if new_trunk_diameter >= 0:
            self._trunk_diameter = new_trunk_diameter
        else:
            print(f"{self.name}: Error, trunk diameter can't be negative")
            print("Trunk diameter update rejected")

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_v: int,
                 growth_speed: float, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age_v, growth_speed)
        self._nutritional_value = 0
        self.harvest_season = harvest_season.capitalize()
        self.set_nutritional_value(nutritional_value)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow_in_days(self, days: int = 1) -> None:
        super().grow_in_days(days)
        self._nutritional_value += days

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def set_nutritional_value(self, new_nutritional_value: int) -> None:
        if new_nutritional_value >= 0:
            self._nutritional_value = new_nutritional_value
        else:
            print(f"{self.name}: Error, nutritional value can't be negative")
            print("Nutritional value update rejected")

    def get_nutritional_value(self) -> int:
        return self._nutritional_value


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.5, "Red")
    rose.show()
    print(f"[asking the {rose.name} to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.5, 5.0)
    oak.show()
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 3.0, "April", 0)
    tomato.show()
    print(f"[make {tomato.name} grow and age for 20 days]")
    tomato.grow_in_days(20)
    tomato.show()


if __name__ == "__main__":
    main()
