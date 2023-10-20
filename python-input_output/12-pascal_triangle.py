#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def pascal_triangle(n):
    """
    'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
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
