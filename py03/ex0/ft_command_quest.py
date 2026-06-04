import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argc = len(sys.argv)
    if argc < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
