#!/usr/bin/python3
'''Module of pascal triangle'''


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) < n:
        prevrow = triangle[-1]
        newrow = [1]
        for i in range(len(prevrow) - 1):
            newvalue = prevrow[i] + prevrow[i + 1]
            newrow.append(newvalue)
        newrow.append(1)
        triangle.append(newrow)
    return triangle
