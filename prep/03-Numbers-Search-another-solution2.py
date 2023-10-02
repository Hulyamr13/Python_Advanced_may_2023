def numbers_searching(*args):
    numbers = len(args)
    duplicates = []

    for i in range(numbers):
        k = i + 1
        for j in range(k, numbers):
            if args[i] == args[j] and args[i] not in duplicates:
                if args[i] > 0:                           # eventualno
                    duplicates.append(args[i])
    duplicates.sort()

    missing = [ele for ele in range(min(duplicates), max(duplicates)+1) if ele not in duplicates][0]

    return [missing, duplicates]



print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(0, 0, 100, 200, 100, 200, 500, 400))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48, 1000, 1000, 5, 5, -1, -1, -5, -5, -4, -4))