from collections import deque


def numbers_searching(*nums):
    compare_to = deque(nums)

  #  whole_list = list(sorted(nums))
    duplicates = []
    no_dupll = set(nums)


    while compare_to:
        element = compare_to.popleft()
    #    return element
        if element in compare_to and element not in duplicates:
            duplicates.append(element)

    sort_it = list(sorted(duplicates))

#    return sort_it


    start_from = min(no_dupll)
    end_at = max(no_dupll)
    missing = 0
    final_list = []

    for i in range(start_from, end_at):
        if i not in no_dupll:
            missing = i


    final_list.append(missing)
    final_list.append(sort_it)


    return final_list


print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))