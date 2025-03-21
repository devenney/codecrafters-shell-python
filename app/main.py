import sys


def main():
    while True:
        # Print prompt
        sys.stdout.write("$ ")

        # Collect input
        cmd = input().split(" ")

        # Process input
        match cmd:
            case ["echo", *words]:
                print(f"{' '.join(words)}")
            case ["exit", code]:
                exit(int(code))
            case [""]:
                continue
            case _:
                print(f"{cmd[0]}: command not found")


if __name__ == "__main__":
    main()
