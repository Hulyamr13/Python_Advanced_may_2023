numbers = input().split(", ")
result = 1.0

for i in range(len(numbers)):
    number = int(numbers[i])

    if number <= 5:
        result *= number
    elif number > 5 and number <= 10:
        result /= number

print(result)
