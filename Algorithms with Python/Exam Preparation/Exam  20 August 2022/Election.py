def main():
    min_val = int(input())
    n = int(input())
    numbers = [0] * n

    for i in range(n):
        numbers[i] = int(input())

    sums = {}

    for i in range(1, n):
        current_num = numbers[i]

        if current_num not in sums:
            sums[current_num] = 1

        past_sums = list(sums.keys())
        for sum_val in past_sums:
            new_sum = sum_val + current_num
            if new_sum not in sums:
                sums[new_sum] = 0

            sums[new_sum] += 1

    count = sum(value for key, value in sums.items() if key >= min_val)
    print(count)

if __name__ == "__main__":
    main()
