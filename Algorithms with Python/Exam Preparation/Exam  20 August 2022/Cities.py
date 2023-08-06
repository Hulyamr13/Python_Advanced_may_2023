def main():
    n = int(input())
    numbers = [0] * n

    for i in range(n):
        tokens = input().split()
        numbers[i] = int(tokens[0])

    lis = [0] * n
    lis_prev = create_array(n)

    lis[0] = 1
    lis_prev[0] = -1

    for i in range(n):
        lis[i] = 1
        for j in range(i):
            if numbers[i] > numbers[j] and lis[i] <= lis[j]:
                lis[i] += 1
                lis_prev[i] = j

    lds = [0] * n
    lds_prev = create_array(n)

    lds[n - 1] = 1
    lds_prev[n - 1] = -1

    for i in range(n - 1, -1, -1):
        lds[i] = 1
        for j in range(n - 1, i, -1):
            if numbers[i] > numbers[j] and lds[i] <= lds[j]:
                lds[i] += 1
                lds_prev[i] = j

    max_val = 0

    for i in range(n):
        current_max = lis[i] + lds[i] - 1
        if current_max > max_val:
            max_val = current_max

    print(max_val)

def create_array(n):
    return [-1] * n

if __name__ == "__main__":
    main()
