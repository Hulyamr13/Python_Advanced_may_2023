import collections


def numbers_searching(*args):
    numbers = [x for x in args]

    duplicates = [item for item, count in collections.Counter(numbers).items() if count > 1]
    duplicates.sort()

    #duplicates = sorted([item for item, count in collections.Counter(numbers).items() if count > 1])

    for el in duplicates:
        if el < 1:
            duplicates.remove(el)

    missing = [ele for ele in range(min(duplicates), max(duplicates)+1) if ele not in duplicates][0]

    return [missing, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48, 1000, 1000, 5, 5, -1, -1, -5, -5))


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48, 1000, 1000, 5, 5, -1, -1, -5, -5, -4, -4))