import sys


commands = {}


def register_command(name):
    def decorator(func):
        commands[name] = func
        return func
    return decorator


@register_command("echo")
def shellEcho(*args):
    print(f"{' '.join(args)}")


@register_command("exit")
def shellExit(code):
    try:
        sys.exit(int(code))
    except ValueError:
        print(f"exit: {code}: numeric argument required")


def shellNotFound(command):
    print(f"{command[0]}: command not found")


def main():
    while True:
        # Print prompt
        sys.stdout.write("$ ")

        # Collect input
        cmd = input().split(" ")
        command, *args = cmd

        # Handle empty or pure whitespace
        if not command or command == "":
            continue

        # Dispatch command
        if command in commands:
            try:
                commands[command](*args)
            except TypeError:
                print(f"{command}: invalid arguments")
        else:
            shellNotFound(cmd)


if __name__ == "__main__":
    main()
