def recursive_power(number, power):
    if power == 0:
        return 1
    else:
        return number * recursive_power(number, power-1)


print(recursive_power(2, 10))  # should output 1024
print(recursive_power(10, 100))  # should output 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
