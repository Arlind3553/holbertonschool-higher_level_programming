#!/usr/bin/python3
'''
Module for demostrattive purposes
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Class for Square objects
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        '''
        Function to update instance attributes
        '''
        name_list = ['id', 'size', 'x', 'y']
        for i in range(len(args)):
            setattr(self, name_list[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return {
                "id" = self.id,
                "size" = self.size,
                "x" = self.x,
                "y" = self.y
                }
