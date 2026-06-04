class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name[0].islower():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def main() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...\nOpening watering system")
    plants = ["Tomato", "Lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return
    finally:
        print("Closing watering system\n")

    plants[1] = plants[1].lower()
    print("Testing invalid plants...\nOpening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
