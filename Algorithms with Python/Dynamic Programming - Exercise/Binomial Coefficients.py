def get_binom(row, col, cache={}):
    # Construct the cache key
    key = f"{row} {col}"

    # Check if the value has already been calculated
    if key in cache:
        return cache[key]

    # Base cases
    if col == 0 or col == row:
        return 1

    # Recursive case
    result = get_binom(row - 1, col) + get_binom(row - 1, col - 1)

    # Store the calculated value in the cache
    cache[key] = result

    return result


row = int(input())
col = int(input())

result = get_binom(row, col)
print(result)