import sys
import shutil
import subprocess
import os
from pathlib import Path
import shlex


commands = {
    "echo": lambda *args:" ".join(args),
    "exit":lambda exit_code:sys.exit(int(exit_code[0])) if exit_code else 0,
    "pwd": lambda: os.getcwd(),
    "cd":lambda path: cd(path),
    "type":lambda *command: shell_type(command),
    
}

def cd(path):
    if path == "~":
        os.chdir(Path.home())
    elif os.path.exists(path):
        os.chdir(path)
    else:
        print(f"cd: {path}: No such file or directory")
    

def redirecting(args:list):
    for i in args:
        if i in [">", "1>"]:
            idx = args.index(i)
            first = args[:idx]
            second = args[idx+1:]
            with open(second[0],"w") as f:
                f.write(commands[first[0]](*first[1:]))

            break



def shell_type(command):
    if command[0] in commands:
        return(f"{command[0]} is a shell builtin")    
    elif shutil.which(command[0]):
        return(f"{command[0]} is {shutil.which(command[0])}")
    else:
        return(f"{command[0]}: not found")



def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        first = shlex.split(input().strip())
        if ">" in first or "1>" in first:
            redirecting(first)
            continue
        command = first[0] if first else ""

        args = first[1:]
        if command in commands:
            print(commands[command](*args))
        elif shutil.which(command):
            subprocess.run([command] + args)
           
        else:
            print(f"{command}: command not found")
        


if __name__ == "__main__":
    main()
