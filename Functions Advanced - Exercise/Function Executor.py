def func_executor(*args):
    result = []
    for f, arg in args:
        func_name = f.__name__
        func_result = f(*arg)
        result.append(f"{func_name} - {func_result}")
    return "\n".join(result)

# Test case 1
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

# Test case 2
def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

