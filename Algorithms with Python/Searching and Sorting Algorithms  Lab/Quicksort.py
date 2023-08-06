def quick_sort(numbers, start_index, end_index):
    if start_index >= end_index:
        return

    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index

    while left_index <= right_index:
        if numbers[left_index] > numbers[pivot_index] and numbers[right_index] < numbers[pivot_index]:
            numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index]

        if numbers[left_index] <= numbers[pivot_index]:
            left_index += 1

        if numbers[right_index] >= numbers[pivot_index]:
            right_index -= 1

    numbers[pivot_index], numbers[right_index] = numbers[right_index], numbers[pivot_index]

    is_left_subarray_smaller = right_index - 1 - start_index < end_index - (right_index + 1)

    if is_left_subarray_smaller:
        quick_sort(numbers, start_index, right_index - 1)
        quick_sort(numbers, right_index + 1, end_index)
    else:
        quick_sort(numbers, right_index + 1, end_index)
        quick_sort(numbers, start_index, right_index - 1)


input_list = list(map(int, input().split()))
quick_sort(input_list, 0, len(input_list) - 1)
print(' '.join(map(str, input_list)))
