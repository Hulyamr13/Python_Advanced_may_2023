def numbers_searching(*nums):
    nums_set = set(nums)
    duplicates = []
    missing = None

    for i in range(min(nums_set), max(nums_set)):
        if i not in nums_set:
            missing = i
            break

    for n in nums_set:
        if nums.count(n) > 1:
            duplicates.append(n)

    duplicates.sort()

    return [missing, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))  # [3, [2, 4]]
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))  # [6, [5, 7, 9]]
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))  # [46, [44, 45, 47, 48, 50]]
