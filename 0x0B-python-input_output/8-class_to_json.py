#!/usr/bin/python3
'''
    class to JSON
'''


def class_to_json(obj):
    ''' function that returns dictionary description
        with simple data structure
    '''
    return obj.__dict__
