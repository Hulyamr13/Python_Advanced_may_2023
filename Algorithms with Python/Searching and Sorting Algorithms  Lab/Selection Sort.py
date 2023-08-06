def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


input_list = list(map(int, input().split()))
sorted_list = selection_sort(input_list)
print(' '.join(map(str, sorted_list)))
