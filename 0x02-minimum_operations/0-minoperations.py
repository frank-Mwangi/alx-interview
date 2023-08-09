#!/usr/bin/python3
"""
Dynamic Programming - Minimum operations
"""


def minOperations(n: int) -> int:
    """Function to return fewest no of operations to result in exactly
    n H characters in a file that only allows copy all and
    paste operations"""
    if (n == 1):
        return 0
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i
    for j in range(2, i):
        if i % j == 0:
            dp[i] = min(dp[i], dp[j] + (i // j))
    return dp[n]
