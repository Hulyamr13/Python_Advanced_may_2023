def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        element = arr[mid]

        if element == key:
            return mid

        if key > element:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = list(map(int, input().split()))
key = int(input())

print(binary_search(arr, key))
