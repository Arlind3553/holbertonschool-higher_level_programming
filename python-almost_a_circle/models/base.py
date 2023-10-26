#!/usr/bin/python3
'''
Module for demostrattive purposes
'''


import json


class Base:
    '''
    Class for Base objects
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Return list of dictionaries to JSON string
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Method that writes the JSON string representation of a list to a file
        '''
        dic = []
        if list_objs is not None:
            for obj in list_objs:
                dic.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        '''
        Static method that returns the list of the Json string represenation
        '''
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Class method that returns an instance with all attributes already set
        '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        Class method that returns a list of instances
        '''
        filename = cls.__name__ + ".json"
        list_i = []
        if filename is None:
            return []
        with open(filename, 'r') as file:
            list_dic = Base.from_json_string(file.read())
            for items in list_dic:
                instances = cls.create(**items)
                list_i.append(instances)
        return list_i
