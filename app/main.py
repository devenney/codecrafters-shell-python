import os
import platform
import re
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


@register_command("type")
def shellType(command):
    if command in commands.keys():
        print(f"{command} is a shell builtin")
        return
    else:
        result = findCommandInPath(command)
        if result is None:
            print(f"{command}: not found")
            return

        print(f"{command} is {result}")


# TODO(devenney): replace with shutil.which once we're done with learning file traversal
def findCommandInPath(file):
    path = os.environ["PATH"]

    dirs = []
    if platform.system() == "Windows":
        dirs = re.split(r'[;]', path)
    else:
        dirs = re.split(r'[:]', path)

    for dir in dirs:
        candidate = os.path.join(dir, file)
        if os.path.isfile(candidate):
            return candidate
    return


@register_command("exit")
def shellExit(code):
    try:
        sys.exit(int(code))
    except ValueError:
        print(f"exit: {code}: numeric argument required")


def shellNotFound(command):
    print(f"{command[0]}: command not found")


def run_command(cmd):
    command, *args = cmd

    # Empty or pure whitespace
    if not command or command == "":
        return

    # Builtin command
    if command in commands:
        try:
            commands[command](*args)
        except TypeError as error:
            print(f"{command}: invalid arguments ({error})")
        return


def main():
    while True:
        # Print prompt
        sys.stdout.write("$ ")

        # Collect input
        try:
            cmd = input().split(" ")
        except (EOFError, KeyboardInterrupt):
            break

        run_command(cmd)


if __name__ == "__main__":
    main()
