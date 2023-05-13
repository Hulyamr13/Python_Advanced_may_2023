def best_list_pureness(lst, k):
    n = len(lst)
    max_pureness = float('-inf')
    max_rotation = 0

    for i in range(k + 1):
        pureness = sum((j * lst[j]) for j in range(n))
        if pureness > max_pureness:
            max_pureness = pureness
            max_rotation = i
        lst.insert(0, lst.pop())

    return f"Best pureness {max_pureness} after {max_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
