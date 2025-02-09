import sys
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
            case "type" if "".join(args) in ["echo", "exit", "type"]:
                print(f"{"".join(args)} is a shell builtin")
            case "type":
                sys.stdout.write(f"{"".join(args)}: not found\n")           
            case default:
                sys.stdout.write(f"{command}: command not found\n")
    return
if __name__ == "__main__":
    main()
