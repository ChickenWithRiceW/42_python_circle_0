def secure_archive(file_name: str, action: str = 'r',
                   write_str: str = "") -> tuple[bool, str]:
    try:
        with open(file_name, action) as file:
            match action:
                case 'r':
                    content = file.read()
                case 'w':
                    file.write(write_str)
                    content = "Content successfully written to file"
    except Exception as e:
        return (False, f"{e}")
    else:
        return (True, f"{content}")


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("None", 'r'))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/root/cant", 'r'))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive("text", 'r')
    print(content)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file", 'w', content[1]))


if __name__ == "__main__":
    main()
