#!/usr/bin/python3

import json

class Base:
    ''' initiating class named base
        This class will be the base of all other classes in this project
        This class will manage the id attribute for all classes
        Arguments:
            @id: The id for specific instance
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
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
