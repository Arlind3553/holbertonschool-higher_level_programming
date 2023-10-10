#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    """
    This is the documentation for the Square class.
    The class represents a geometric square and associated operations.
    """
    def __init__(self, size=0):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) is False or len(value) != 2
                or (isinstance(value[0], int) is False or value[0] < 0)
                or (isinstance(value[1], int) is False or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for row in (self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end='')
            print()
