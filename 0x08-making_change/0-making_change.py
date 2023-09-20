#!/usr/bin/python3
"""
Find least amount of coins needed to make change
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coinsArr = [float('inf')] * (total + 1)
    coinsArr[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                coinsArr[i] = min(coinsArr[i], coinsArr[i - coin] + 1)
    if coinsArr[total] == float('inf'):
        return -1
    else:
        return coinsArr[total]
