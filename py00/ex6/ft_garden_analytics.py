class Plant:
    def __init__(self, name: str, height: float, age_v: int,
                 growth_speed: float) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self._growth_speed = 0.0
        self.stats = self.Statistics(name)
        self.set_height(height)
        self.set_age(age_v)
        self.set_growth_speed(growth_speed)

    @classmethod
    def create_unknown(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 2)}cm, {self._age} days old")
        self.stats._show_count += 1

    def grow(self) -> None:
        self._height += self._growth_speed
        self.stats._grow_count += 1

    def age(self) -> None:
        self._age += 1
        self.stats._age_count += 1

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

    @staticmethod
    def useless_fun(age: int) -> None:
        print(f"Is {age} days more than a year? -> ", end='')
        if age > 365:
            print("True")
        else:
            print("False")

    class Statistics:
        def __init__(self, name: str) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._name = name

        def show(self) -> None:
            print(f"[statistics for {self._name}]")
            print(
             f"Stats: {self._grow_count} grow, "
             f"{self._age_count} age, {self._show_count} show"
             )


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


class Seed(Flower):
    def __init__(self, name: str, height: float, age_v: int,
                 growth_speed: float, color: str, seed_count: int):
        super().__init__(name, height, age_v, growth_speed, color)
        self._seed_count = 0
        self.set_seed_count(seed_count)

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

    def set_seed_count(self, new_seed_count: int) -> None:
        if new_seed_count >= 0:
            self._seed_count = new_seed_count
        else:
            print(f"{self.name}: Error, seed count can't be negative")
            print("Seed count update rejected")

    def get_seed_count(self) -> int:
        return self._seed_count


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            self._shade_count = 0

        def show(self) -> None:
            super().show()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: float, age_v: int,
                 growth_speed: float,  trunk_diameter: float) -> None:
        super().__init__(name, height, age_v, growth_speed)
        self._trunk_diameter = 0.0
        self.stats: "Tree.Statistics" = self.Statistics(self.name)
        self.set_trunk_diameter(trunk_diameter)

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of {self._height}cm long"
            f" and {self._trunk_diameter}cm wide."
        )
        self.stats._shade_count += 1

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


def display_statistics(plant: Plant) -> None:
    plant.stats.show()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.useless_fun(30)
    Plant.useless_fun(400)

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.5, "Red")
    rose.show()
    rose.stats.show()
    print(f"[asking the {rose.name} to bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    rose.stats.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.5, 5.0)
    oak.show()
    oak.stats.show()
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    oak.stats.show()

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 0.0, 45, 0.3, "Yellow", 0)
    sunflower.show()
    sunflower.grow_in_days(10)
    sunflower.bloom()
    sunflower.show()
    sunflower.stats.show()

    print("\n=== Anonymous")
    unknown = Plant.create_unknown()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
