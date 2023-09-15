import math

number = int(input())
base = input()

if base == "natural":
    logarithm = math.log(number)
elif base == "10":
    logarithm = math.log10(number)
else:
    base = float(base)
    logarithm = math.log(number, base)

print(f'{logarithm:.2f}')
