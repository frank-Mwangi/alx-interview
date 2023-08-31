#!/usr/bin/python3
"""
N Queens

usage: nqueens N
"""

import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
N = sys.argv[1]
try:
    N = int(N)

except:
    print('N must be a number')
    exit(1)

k = 1


def printSol(board):
    """Utility function t print solution"""
    queens = []
    global k
    k = k + 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j]:
            return False
        i = i + 1
        j = j - 1
    return True


def solveNQUtil(board, col):
    """solve n queens"""
    if col == N:
        printSol(board)
        return True
    res = False
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res


def solveNQ():
    """Methos to solve NQ"""
    board = [[0 for j in range(N)] for i in range(N)]
    if solveNQUtil(board, 0) is False:
        pass
        return
    return


solveNQ()
