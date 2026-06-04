import sys
import typing


def main() -> None:
    argc = len(sys.argv)
    print("=== Cyber Archives Recovery ===")

    if argc != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    # Trying to open the file
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        io: typing.IO[str] = open(sys.argv[1], 'r')
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return

    # Trying to read the file
    try:
        file = io.read()
    except Exception as e:
        print(f"Error: {e}")
        return
    else:
        print("---\n")
        print(file)
        print("\n---")
    finally:
        io.close()
        print(f"File '{sys.argv[1]}' closed")


if __name__ == "__main__":
    main()
