#!/usr/bin/python3
'''
Module for demostrattive purposes
'''


class Base:
    '''
    Class for Base objects
    '''

    __nd_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nd_objects
