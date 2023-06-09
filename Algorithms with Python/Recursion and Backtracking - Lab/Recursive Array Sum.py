def get_sum(arr, index):
    if index >= len(arr):
        return 0
    return arr[index] + get_sum(arr, index + 1)

def main():
    arr = list(map(int, input().split()))
    result = get_sum(arr, 0)
    print(result)

if __name__ == "__main__":
    main()
