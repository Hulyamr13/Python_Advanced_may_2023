numbers_list = list(map(int, input().split(", ")))

result = 1
for number in numbers_list:
    result *= number if number <= 5 else 1 / number if 5 < number <= 10 else 1

print(result)
