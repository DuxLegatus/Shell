import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    command = input()
    print(f"{command}: command not found")


    # Wait for user input
    input()


if __name__ == "__main__":
    main()
