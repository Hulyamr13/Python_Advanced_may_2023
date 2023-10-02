def best_list_pureness(numbers: list, k: int):
    best_rotation = 0
    best_pureness = -1000000000

    for rotation in range(k +1):
        pureness = 0

        for position in range(len(numbers)):
            pureness += (position * numbers[position])

        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation

        numbers = numbers[-1:] + numbers[:-1]

    return f'Best pureness {best_pureness} after {best_rotation} rotations'


# test = ([0, 1], 4)
# result = best_list_pureness(*test)
# print(result)

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)