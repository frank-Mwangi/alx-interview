#!/usr/bin/python3
"""
Prime game, where each player removes a prime
number and all its multiples from a set of 0 to n
"""


def isWinner(x, nums):
    """Find winner of the prime game"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if n == 1:
            ben_wins += 1
        elif n % 2 == 0:
            maria_wins += 1
        elif is_prime(n):
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
