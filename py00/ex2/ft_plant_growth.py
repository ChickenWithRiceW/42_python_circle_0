class Plant:
    def __init__(self, name: str, height: float, age_v: int,
                 growth_speed: float) -> None:
        self.name:          str = name.capitalize()
        self.height:        float = height
        self.age_v:         int = age_v
        self.growth_speed:  float = growth_speed

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.age_v} days old")

    def grow(self) -> None:
        self.height += self.growth_speed

    def age(self) -> None:
        self.age_v += 1

    def grow_in_days(self, days: int = 1) -> None:
        for day in range(days):
            self.grow()
            self.age()


def main() -> None:
    print("=== Garden Plant Growth ===")

    sunflower: Plant = Plant("Sunflower", 10.00, 10, 3.00)
    # bamboo: Plant = Plant("Bamboo", 1.00, 1, 20.00)
    plant: Plant = sunflower
    old_height: float = plant.height
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        plant.show()
        plant.grow_in_days()
    print(f"Growth this week: {round(plant.height - old_height, 2)}cm")


if __name__ == "__main__":
    main()
