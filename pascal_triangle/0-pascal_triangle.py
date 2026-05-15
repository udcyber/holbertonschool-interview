#!/usr/bin/env python3
"""Return a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """Return an empty list if n is negative or 0"""
    if n <= 0:
        return []

    pascal_triangle = [[1]]
    while len(pascal_triangle) != n:
        previous = pascal[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        pascal_triangle.append(current)
    return pascal_triangle
