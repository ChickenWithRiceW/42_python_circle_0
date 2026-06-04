def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 123
    elif operation_number == 4:
        1 + 1


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    range_val = [0, 1, 2, 3, 4]
    for x in range_val:
        print(f"Testing operation {x}...")
        try:
            garden_operations(x)
        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        else:
            print("Operation completed successfully")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
