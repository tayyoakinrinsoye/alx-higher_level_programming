#!/usr/bin/python3
''' MODULE: 4-inherits_from
'''



def inherits_from(obj, a_class):
    ''' the object is an instance of a class that inherited (directly or indirectly)
    obj: an object
    a_class: a class
    returns None
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
