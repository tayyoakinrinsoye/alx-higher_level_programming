#!/usr/bin/python3

class Base:
    ''' initiating clase named base
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
            base.__nb_objects += 1
            self.id = base.__nb_objects
