import sys
import shutil
import os

def main():
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        # Wait for user input
        command, *args = input().split(" ")
        match command:
            case "exit":
                break
            case "echo":
                print(" ".join(args))
            case "type": 
                if "".join(args) in ["echo", "exit", "type"]:
                    print(f"{"".join(args)} is a shell builtin")
                elif path := shutil.which("".join(args)):
                    print(f"{"".join(args)} is {path}") 
                else:
                    sys.stdout.write(f"{"".join(args)}: not found\n")           
            case default:
                if os.path.isfile(command):
                    os.system(command)
                else:
                    print(f"{command}: command not found")
    return
if __name__ == "__main__":
    main()
