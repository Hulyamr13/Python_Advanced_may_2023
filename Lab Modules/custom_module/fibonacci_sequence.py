def create_sequence(count):
    fib_sequence = [0, 1]  # Initialize the sequence with the first two numbers
    for _ in range(2, count):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence


def locate_number(number):
    fib_sequence = create_sequence(number + 1)  # Generate the sequence up to the specified number
    if number in fib_sequence:
        index = fib_sequence.index(number)
        return f"The number - {number} is at index {index}"
    else:
        return f"The number {number} is not in the sequence"
