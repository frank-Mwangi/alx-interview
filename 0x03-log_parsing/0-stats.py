#!/usr/bin/python3
"""
    This script reads stdin line by line and computes metrics.
"""

import sys


def print_msg(codes, file_size):
    """
    Prints the computed metrics: total file size and status code counts.
    """
    print("File size:", file_size)
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


# Initialize variables
file_size = 0
count_lines = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        # Split the line into parts and reverse for easier extraction
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count_lines += 1

            if count_lines <= 10:
                # Update total file size and status code counts
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if code in codes:
                    codes[code] += 1

            if count_lines == 10:
                # Print metrics and reset count_lines
                print_msg(codes, file_size)
                count_lines = 0

finally:
    # Print metrics in case of a keyboard interruption
    print_msg(codes, file_size)
