#!/usr/bin/python3
"""
Module to check if provided dataset
is in UTF-8 encoding
"""


def validUTF8(data):
    """Method to validate UTF-8 encoding"""
    remaining_bytes = 0
    for num in data:
        if remaining_bytes == 0:
            if num >> 7 == 0b0:
                remaining_bytes = 0
            elif num >> 5 == 0b110:
                remaining_bytes = 1
            elif num >> 4 == 0b1110:
                remaining_bytes = 2
            elif num >> 3 == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            remaining_bytes -= 1
        return remaining_bytes == 0
