import sys


def main():
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        user_input = input()
        command = user_input.split()[0]
        args = user_input.split()[1:]

        match command:
            case "exit":
                if len(args) > 0:
                    exit(args[0])
                else:
                    exit()
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
