#!/usr/bin/env python3
"""Return a list of lists of integers
representing the Pascal's triangle of n"""
# Return: empty list if n <= 0
# n is always an integer


def pascal_triangle(n):
    """Return an empty list if n is negative or 0"""
    if n <= 0:
        return []

    triangle = []
    row = []
    prev_row = []
    for i in range(0, n + 1):
        row = [L > 0 and L < i - 1 and i > 2 and prev_row[L - 1]
            + prev_row[L] or 1 for L in range(0, i)]
        prev_row = row
        triangle += [row]
    return triangle[1:]
