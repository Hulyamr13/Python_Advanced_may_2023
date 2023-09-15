from custom_module.fibonacci_sequence import create_sequence, locate_number

def main():
    while True:
        command = input()
        if command == "Stop":
            break

        try:
            if command.startswith("Create Sequence"):
                count = int(command.split()[2])
                sequence = create_sequence(count)
                print(" ".join(map(str, sequence)))
            elif command.startswith("Locate"):
                number = int(command.split()[1])
                result = locate_number(number)
                print(result)
            else:
                print("Invalid command. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid command.")


if __name__ == "__main__":
    main()
