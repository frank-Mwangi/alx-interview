#!/usr/bin/python3
"""
Function to check if a series of lockboxes can all be accessed
"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    stack = [0]
    while stack:
        box = stack.pop()
        visited.add(box)
        for key in boxes[box]:
            if key not in visited and 0 <= key < n:
                stack.append(key)
    return len(visited) == n
