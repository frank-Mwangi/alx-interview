#!/usr/bin/python3
"""
Function to check if a series of lockboxes can all be accessed
"""


def canUnlockAll(boxes):
    if not any(isinstance(box, list) for box in boxes):
        return False
    n = len(boxes)
    if n == 1:
        return True
    open_boxes = [0]
    keys_available = boxes[0].copy()
    while keys_available:
        key = keys_available.pop()
        if key not in open_boxes and 0 <= key < n:
            open_boxes.append(key)
            keys_available.extend(boxes[key])
    return len(open_boxes) == n
