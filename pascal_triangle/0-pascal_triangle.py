#!/usr/bin/env python3
"""Return a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """Pascal's triangle of size n"""
    if n <= 0:
        return []

    pascal_triangle = []
    row = []
    prev_row = []
    for i in range(0, n + 1):
        row = [x > 0 and x < i - 1 and i > 2 and prev_row[x-1] +
               prev_row[x] or 1 for x in range(0, i)]
        prev_row = row
        pascal_triangle += [row]
    return pascal_triangle[1:]
