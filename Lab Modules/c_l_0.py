from math import log

number = int(input())
base = input()

if base == "natural":
    logarithm = log(number)
else:
    base = float(base)
    logarithm = log(number, base)

print(f'{logarithm:.2f}')
