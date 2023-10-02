def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(numbers):
    for number in numbers:
        if is_prime(number):
            yield number


print(list(get_primes([-2, 0, 0, 1, 1, 0])))