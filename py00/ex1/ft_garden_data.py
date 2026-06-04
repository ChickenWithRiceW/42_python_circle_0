class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name:      str = name.capitalize()
        self.height:    int = height
        self.age:       int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    rose:       Plant = Plant("Rose", 120, 120)
    sunflower:  Plant = Plant("sunflower", 180, 120)
    melon:      Plant = Plant("melon", 20, 60)

    rose.show()
    sunflower.show()
    melon.show()


if __name__ == "__main__":
    main()
