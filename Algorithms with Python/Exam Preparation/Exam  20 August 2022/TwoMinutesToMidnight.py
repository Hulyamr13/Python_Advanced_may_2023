def main():
    n = int(input())
    k = int(input())

    cache = {}

    print(get_binom(n, k, cache))

def get_binom(row, col, cache):
    id_str = f"{row} {col}"

    if id_str in cache:
        return cache[id_str]

    if col == 0 or col == row:
        return 1

    result = get_binom(row - 1, col, cache) + get_binom(row - 1, col - 1, cache)
    cache[id_str] = result
    return result

if __name__ == "__main__":
    main()
