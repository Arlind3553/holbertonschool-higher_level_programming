#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
def add_integer(a, b=98):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    return a+b
