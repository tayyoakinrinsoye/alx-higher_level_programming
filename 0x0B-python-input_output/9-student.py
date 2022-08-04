#!/usr/bin/python3
'''Student to JSON
'''


class Student:
    '''module class student
    '''


    def __init__(self, first_name, last_name, age):
        '''method __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        method to json
        '''
        return self.__dict__
