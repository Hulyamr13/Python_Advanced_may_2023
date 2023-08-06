def calc_binomial_coefficient(n, k):
    def factorial(num):
        if num <= 1:
            return 1
        return num * factorial(num - 1)

    return factorial(n) // (factorial(k) * factorial(n - k))

transactions_count = int(input())
transactions_could_be_picked = int(input())
print(calc_binomial_coefficient(transactions_count, transactions_could_be_picked))
