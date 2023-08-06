combination = []
result = []

def main():
    maxSum = int(input())
    currentSum = 0
    create_limited_sum(currentSum, maxSum)
    print(''.join(result))

def create_limited_sum(currentSum, maxSum):
    global combination, result

    if currentSum > maxSum:
        return
    else:
        result.append(' '.join(map(str, combination)) + '\n')
        for i in range(1, maxSum + 1):
            combination.append(i)
            currentSum += i

            create_limited_sum(currentSum, maxSum)

            combination.pop()
            currentSum -= i

if __name__ == "__main__":
    main()
