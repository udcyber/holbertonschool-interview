#!/usr/bin/env python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Pascal's triangle of size n"""
    if n <= 0:
        return []

    pascal_triangle = []
    row = [1]
    pascal_triangle.append(row)

    for _ in range(1, n):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        pascal_triangle.append(row)

    return pascal_triangle
