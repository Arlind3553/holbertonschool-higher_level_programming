#!/usr/bin/python3

'''
    Simple module for creating a
    Rectnagle class with instance methods
    and class methods
'''


class Rectangle:
    '''
        Rectangle class with two attributes

    '''

    def __init__(self, width=0, height=0):
        '''
            Init function for Rectangle class

        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
            Width attribute getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Width attribute setter
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
            Height attribute getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Height attribute setter
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
