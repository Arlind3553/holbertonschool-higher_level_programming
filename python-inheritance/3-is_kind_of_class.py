#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def is_kind_of_class(obj, a_class):
    '''Finds if an object is an instance of a class'''
    return isinstance(obj, a_class)
