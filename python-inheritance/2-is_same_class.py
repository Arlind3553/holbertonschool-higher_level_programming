#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def is_same_class(obj, a_class):
    '''Finds if an object is an instance of a class'''
    if type(obj) is a_class:
        return True
    return False
