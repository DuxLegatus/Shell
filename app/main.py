import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        print(f"{command}: command not found")
        sys.exit("exit 0")


    # Wait for user input


if __name__ == "__main__":
    main()
