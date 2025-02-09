import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        print(f"{command}: command not found")
        sys.exit("0")


if __name__ == "__main__":
    main()
