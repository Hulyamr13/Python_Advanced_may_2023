first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))

n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == "Add" and command[1] == "First":
        numbers = set(map(int, command[2:]))
        first_sequence |= numbers
    elif command[0] == "Add" and command[1] == "Second":
        numbers = set(map(int, command[2:]))
        second_sequence |= numbers
    elif command[0] == "Remove" and command[1] == "First":
        numbers = set(map(int, command[2:]))
        first_sequence -= numbers
    elif command[0] == "Remove" and command[1] == "Second":
        numbers = set(map(int, command[2:]))
        second_sequence -= numbers
    elif command[0] == "Check" and command[1] == "Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

# Print the final sequences
print(", ".join(str(x) for x in sorted(first_sequence)))
print(", ".join(str(x) for x in sorted(second_sequence)))