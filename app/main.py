import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            sys.exit()
        print(f"{command}: command not found")


    # Wait for user input


if __name__ == "__main__":
    main()
