def multiply(factor):
    def decorator(function):
        def wrapper(number):
            result = function(number)
            return result * factor
        return wrapper
    return decorator

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))  # Output: 39

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))  # Output: 80
