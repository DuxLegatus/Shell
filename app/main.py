import sys

commands = {
    "echo": lambda args: print(" ".join(args)),
    "exit":lambda exit_code:sys.exit(int(exit_code[0])) if exit_code else 0,
    "type":lambda command:print("exit is a shell builtin") if command[0] in commands else print(f"{command}: command not found")
}
def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        first = input().strip().split()
        command = first[0]
        args = first[1:]
        if command in commands:
            commands[command](args)
        


if __name__ == "__main__":
    main()
