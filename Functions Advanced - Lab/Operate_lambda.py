import functools

def operate(operator, *args):
    return {
        '+': lambda: sum(args),
        '-': lambda: args[0] - sum(args[1:]),
        '*': lambda: functools.reduce(lambda a, b: a * b, args),
        '/': lambda: functools.reduce(lambda a, b: a / b, args)
    }[operator]()


print(operate("+", 1, 2, 3))  # should output 6
print(operate("*", 3, 4))  # should output 12