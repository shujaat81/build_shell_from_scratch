import sys


def main():
    # Uncomment this block to pass the first stage
    exit_message = 'exit 0'
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if len(command) != 0:
            first_input = command.split()[0]
            if first_input == "echo":
                print(f"{command[len(first_input)+1:]}")
        if command == exit_message:
            sys.exit(0)
        


if __name__ == "__main__":
    main()
