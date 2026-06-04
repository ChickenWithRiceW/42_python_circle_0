class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def garden_operations(operation_number: str) -> None:
    if operation_number == "PlantError":
        raise PlantError("The tomato plant is wilting!")
    elif operation_number == "WaterError":
        raise WaterError("Not enough water in the tank!")


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    testing_errors = ["PlantError", "WaterError"]
    for x in testing_errors:
        print(f"Testing {x}")
        try:
            garden_operations(x)
        except PlantError as e:
            print(f"Caught PlantError: {e}\n")
        except WaterError as e:
            print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for x in testing_errors:
        try:
            garden_operations(x)
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
