#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def inherits_from(obj, a_class):
    '''Finds if an object is an instance of a class'''
    if isinstance(obj, a_class):
        if obj.__class is a_class:
            return False
        return True
    return True
