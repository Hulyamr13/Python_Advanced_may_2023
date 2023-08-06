coins = list(map(int, input().split(", ")))
target = int(input())

sorted_coins = sorted(coins, reverse=True)

counter = 0
coins_index = 0
used_coins = {}

while target > 0 and coins_index < len(sorted_coins):
    current_coin = sorted_coins[coins_index]
    coins_count = target // current_coin

    if coins_count > 0:
        counter += coins_count
        target -= current_coin * coins_count
        used_coins[current_coin] = coins_count

    coins_index += 1

if target == 0:
    print(f"Number of coins to take: {counter}")
    for coin, count in used_coins.items():
        print(f"{count} coin(s) with value {coin}")
else:
    print("Error")
