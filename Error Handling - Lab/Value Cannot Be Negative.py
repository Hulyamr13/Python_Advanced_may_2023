class ValueCannotBeNegative(Exception):
    pass

numbers = []
for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
    numbers.append(num)

print(numbers)
