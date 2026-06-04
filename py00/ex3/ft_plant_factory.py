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
    sunflower: Plant = Plant("Sunflower", 2.0, 10, 2.5)
    rose: Plant = Plant("Rose", 10.0, 30, 1.5)
    carrot: Plant = Plant("Carrot", 1.0, 10, 1.2)
    bamboo: Plant = Plant("Bamboo", 2.0, 10, 10.00)
    salad: Plant = Plant("Salad", 4.0, 20, 5.00)

    plants = [sunflower, rose, carrot, bamboo, salad]
    for plant in plants:
        print("Created: ", end='')
        plant.show()


if __name__ == "__main__":
    main()
