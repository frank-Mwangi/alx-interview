#!/usr/bin/python3
"""
Dynamic Programming - Minimum operations
"""


def minOperations(n):
    """Function to return fewest no of operations to result in exactly
    n H characters in a file that only allows copy all and
    paste operations"""
    if n == 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1
    return operations
