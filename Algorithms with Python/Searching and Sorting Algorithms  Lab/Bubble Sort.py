def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(1, n - i):
            if numbers[j - 1] > numbers[j]:
                numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]


numbers = list(map(int, input().split()))
bubble_sort(numbers)
print(' '.join(map(str, numbers)))
