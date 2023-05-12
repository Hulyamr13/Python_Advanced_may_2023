def even_odd(*args):
    return [num for num in args[:-1] if num % 2 == (0 if args[-1] == "even" else 1)]

# First test case
even_numbers = even_odd(1, 2, 3, 4, 5, 6, "even")
print(even_numbers)  # Output: [2, 4, 6]

# Second test case
odd_numbers = even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd")