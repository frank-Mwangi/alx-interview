#!/usr/bin/python3
"""Log parsing script"""

import sys


def print_statistics(file_size, status_counts):
    """Function to print file size and status counts"""
    print("File size:", file_size)
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")


def main():
    file_size = 0
    status_counts = {}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            parts = line.split()

            if len(parts) != 10:
                continue

            ip, _, _, date, _, request, status_code, size = parts
            if request != ' "GET /projects/260 HTTP/1.1" ':
                continue

            try:
                size = int(size)
                status_code = int(status_code)
            except ValueError:
                continue

            file_size += size
            if status_code in (200, 301, 400, 401, 403, 404, 405, 500):
                status_counts[status_code] = status_counts.get
                (status_code, 0) + 1

            if line_number % 10 == 0:
                print_statistics(file_size, status_counts)
                print()

    except KeyboardInterrupt:
        print_statistics(file_size, status_counts)


if __name__ == "__main__":
    main()
