import sys


def main():
    # Uncomment this block to pass the first stage
    exit_message = 'exit 0'
    loop = True
    while loop:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        print(f"{command}: command not found")
        if command == exit_message:
            loop = False
            sys.exit(0)
        


if __name__ == "__main__":
    main()
