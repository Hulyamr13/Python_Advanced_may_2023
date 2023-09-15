import math

number = int(input())
base = input()

if base == "natural":
    logarithm = math.log(number)
else:
    base = float(base)
    logarithm = math.log(number, base)

print(f'{logarithm:.2f}')
