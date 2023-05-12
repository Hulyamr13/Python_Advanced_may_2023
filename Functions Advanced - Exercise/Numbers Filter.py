def even_odd_filter(**lists):
    result = {}
    for key, value in lists.items():
        if key == 'even':
            result[key] = [num for num in value if num % 2 == 0]
        elif key == 'odd':
            result[key] = [num for num in value if num % 2 != 0]
    return dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))


# Test case 1
print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2]))
# Output: {'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}

# Test case 2
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5]))
# Output: {'odd': [5]}
