#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class MyList(list):
    '''Prints a sorted list'''
    def print_sorted(self):
        ls = self.copy()
        ls.sort()
        print(ls)
        return ls
