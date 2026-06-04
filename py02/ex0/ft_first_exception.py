def input_temperature(input_val: str) -> int:
    print(f"Input data is '{input_val}'")
    return int(input_val)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    tests = ["25", "abc"]
    for test in tests:
        print("")
        try:
            temp = input_temperature(test)
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
        else:
            print(f"Temperature is now {temp}°C")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
