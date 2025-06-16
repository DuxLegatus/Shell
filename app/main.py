import sys
import shutil
import subprocess

commands = {
    "echo": lambda args: print(" ".join(args)),
    "exit":lambda exit_code:sys.exit(int(exit_code[0])) if exit_code else 0,
    "type":lambda command:type(command)
}
def type(command):
    if command[0] in commands:
        print(f"{command[0]} is a shell builtin")    
    elif shutil.which(command[0]):
        print(f"{command[0]} is {shutil.which(command[0])}")
    else:
        print(f"{command[0]}: not found")



def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        first = input().strip().split()
        command = first[0] if first else ""
        args = first[1:]
        if command in commands:
            commands[command](args)
        elif shutil.which(command[0]):
            subprocess.run([command] + args)
           
        else:
            print(f"{command}: command not found")
        


if __name__ == "__main__":
    main()
