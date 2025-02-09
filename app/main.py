import sys


def main():
    # Uncomment this block to pass the first stage
    exit_message = 'exit 0'
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if command == exit_message:
            sys.exit(0)
        print(f"\n{command}")
        


if __name__ == "__main__":
    main()
