def reverse_array(arr, start_index, end_index):
    if start_index >= end_index:
        print(' '.join(arr))
        return


    arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    reverse_array(arr, start_index + 1, end_index - 1)


arr = input().split()
reverse_array(arr, 0, len(arr) - 1)