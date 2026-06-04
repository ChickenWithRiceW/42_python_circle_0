import sys
import typing


def main() -> None:
    argc = len(sys.argv)
    print("=== Cyber Archives Recovery & Preservation ===")

    if argc != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    # Trying to open the file
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        io: typing.IO[str] = open(sys.argv[1], "r")
    except Exception as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
              file=sys.stderr)
        return

    # Trying to read the file
    try:
        file = io.read()
    except Exception as e:
        print(f"[STDERR] Error: {e}", file=sys.stderr)
        return
    else:
        print("---\n")
        print(file)
        print("\n---")
    finally:
        io.close()
        print(f"File '{sys.argv[1]}' closed")

    # Add the '#' before the newline
    print("\nTransform data:")
    new_content = ""
    for char in file:
        if char == "\n":
            new_content += "#"
        new_content += char

    print("---\n")
    print(new_content)
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    # Flush forces the terminal to post the write message
    sys.stdout.flush()
    file_name = sys.stdin.readline()
    file_name = file_name[:-1]

    if file_name == "":
        print("Not saving data.")
        return

    try:
        print(f"Saving data to '{file_name}'")
        new_file: typing.IO[str] = open(file_name, "w")
    except Exception as e:
        print(f"[STDERR] Error: {e}", file=sys.stderr)
        return

    try:
        new_file.write(new_content)
    except Exception as e:
        print(f"[STDERR] Error: {e}", file=sys.stderr)
        return
    else:
        print(f"Data saved in file '{file_name}'.")
    finally:
        new_file.close()


if __name__ == "__main__":
    main()
