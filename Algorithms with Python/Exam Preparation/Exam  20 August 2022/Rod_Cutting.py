def main():
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 5

    optimal = cut_rod(prices, n)
    print(optimal)

def cut_rod(prices, n):
    if n == 0:
        return 0

    optimal = -1

    for i in range(1, n + 1):
        optimal = max(optimal, prices[i] + cut_rod(prices, n - i))

    return optimal

if __name__ == "__main__":
    main()
