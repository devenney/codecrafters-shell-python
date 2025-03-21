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
    elif findCommandInPath(command):
        return
    print(f"{command}: not found")


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
            print(f"{file} is {candidate}")
            return True
    return False


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
            except TypeError as error:
                print(f"{command}: invalid arguments ({error})")
        else:
            shellNotFound(cmd)


if __name__ == "__main__":
    main()
