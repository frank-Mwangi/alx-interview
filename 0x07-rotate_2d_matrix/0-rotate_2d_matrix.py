#!/usr/bin/python3

"""
Module to rotate a 2D Matrix clockwise 90 degrees
"""


def rotate_2d_matrix(matrix):
    """The rotating function"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
