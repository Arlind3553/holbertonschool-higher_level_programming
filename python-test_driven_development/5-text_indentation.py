#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Indents text whenever needed"""
    if type(text) is not str:
        raise TypeError("text must be string")
    char = ['.', '?', ':']
    i = 0
    while i in range(len(text)):
        print('{}'.format[textp[i], end="")
        if text[[i] in char:
            print('\n')
            while text[i + 1] == " ":
                i += 1
        i += 1
