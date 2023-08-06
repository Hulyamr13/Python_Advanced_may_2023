prices = [3, 8, 13, 15, 18, 20, 22]
new_prices = []
connector_price = 1

def main():
    global prices, new_prices, connector_price
    prices = list(map(int, input().split(' ')))
    connector_price = int(input())

    new_prices = [0] * len(prices)

    for i in range(len(new_prices)):
        new_prices[i] = cut_rod(i)

    print(' '.join(str(x) for x in new_prices))

def cut_rod(n):
    if n == -1:
        return 0

    if new_prices[n] > 0:
        return new_prices[n]

    optimal = prices[n]

    for i in range(n):
        new_price = prices[i] + cut_rod(n - i - 1) - (2 * connector_price)
        optimal = max(optimal, new_price)

    return optimal

if __name__ == "__main__":
    main()
