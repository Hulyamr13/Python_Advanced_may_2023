def get_fibonacci(n, memo):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    result = get_fibonacci(n - 1, memo) + get_fibonacci(n - 2, memo)
    memo[n] = result

    return result


def main():
    n = int(input())
    memo = {}

    print(get_fibonacci(n, memo))


if __name__ == "__main__":
    main()
