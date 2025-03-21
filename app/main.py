import sys


def main():
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        user_input = input()
        command = user_input.split()[0]
        arg_str = user_input.removeprefix(command + ' ')

        match command:
            case "echo":
                print(f"{arg_str}")
            case "exit":
                if len(arg_str) > 0:
                    exit(int(arg_str))
                else:
                    exit()
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
