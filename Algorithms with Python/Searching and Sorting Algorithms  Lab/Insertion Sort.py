def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


input_list = list(map(int, input().split()))
sorted_list = insertion_sort(input_list)
print(' '.join(map(str, sorted_list)))
