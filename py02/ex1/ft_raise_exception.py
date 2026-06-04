def input_temperature(input_val: str) -> int:
    print(f"Input data is '{input_val}'")
    int_input = int(input_val)
    if int_input > 40:
        raise Exception(f"{int_input}°C is too hot for plants (max 40°C)")
    elif int_input < 0:
        raise Exception(f"{int_input}°C is too cold for plants (min 0°C)")
    return (int_input)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]
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
