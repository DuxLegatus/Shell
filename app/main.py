import sys
import shutil
import subprocess
import os
from pathlib import Path
import shlex

commands = {
    "echo": lambda *args: " ".join(args),
    "exit": lambda *code: sys.exit(int(code[0])) if code else sys.exit(0),
    "pwd": lambda: os.getcwd(),
    "cd": lambda path: cd(path),
    "type": lambda *command: shell_type(command),
}
def cd(path):
    if path == "~":
        os.chdir(Path.home())
    elif os.path.exists(path):
        os.chdir(path)
    else:
        print(f"cd: {path}: No such file or directory")

def shell_type(command):
    cmd = command[0]
    if cmd in commands:
        return f"{cmd} is a shell builtin"
    elif shutil.which(cmd):
        return f"{cmd} is {shutil.which(cmd)}"
    else:
        return f"{cmd}: not found"

def redirecting(args: list):
    redir_type = None
    if "1>" in args:
        redir_type = "stdout"
        idx = args.index("1>")
    elif "2>" in args:
        redir_type = "stderr"
        idx = args.index("2>")
    elif ">" in args:
        redir_type = "stdout"
        idx = args.index(">")
    else:
        return False

    cmd = args[:idx]
    outfile = args[idx + 1]

    command = cmd[0] if cmd else ""
    command_args = cmd[1:]

    with open(outfile, "w") as f:
        if command in commands:
            result = commands[command](*command_args)
            if result is not None:
                if redir_type == "stdout":
                    f.write(str(result) + "\n")
                elif redir_type == "stderr":
                    f.write(str(result) + "\n")
        elif shutil.which(command):
            if redir_type == "stdout":
                subprocess.run([command] + command_args, stdout=f, stderr=subprocess.DEVNULL)
            elif redir_type == "stderr":
                subprocess.run([command] + command_args, stderr=f, stdout=subprocess.DEVNULL)
        else:
            if redir_type == "stdout":
                f.write(f"{command}: command not found\n")
            elif redir_type == "stderr":
                f.write(f"{command}: command not found\n")
    return True

def main():
    while True:
        sys.stdout.write("$ ")
        try:
            line = input().strip()
            if not line:
                continue
            tokens = shlex.split(line)
            if redirecting(tokens):
                continue
            command = tokens[0]
            args = tokens[1:]

            if command in commands:
                result = commands[command](*args)
                if result is not None:
                    print(result)
            elif shutil.which(command):
                subprocess.run([command] + args)
            else:
                print(f"{command}: command not found")
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()