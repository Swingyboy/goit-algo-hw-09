from typing import List


def find_coins_greedy(amount: int, coins: List[int]) -> dict:
    change = {}
    coins.sort(reverse=True)
    for coin in coins:
        count = amount // coin
        if count > 0:
            change[coin] = count
        amount -= coin * count
    return change


def find_min_coins(amount: int, coins: List[int]) -> dict:
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_used[x] = coin

    change = {}
    if min_coins[amount] == float('inf'):
        return {}

    while amount > 0:
        coin = coin_used[amount]
        if coin in change:
            change[coin] += 1
        else:
            change[coin] = 1
        amount -= coin

    return change
