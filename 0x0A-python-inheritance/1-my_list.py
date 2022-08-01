#!/usr/bin/python3
''' Mylist Module
'''


class MyList(list):
    '''Represents a MyList
    '''
    

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        print(sorted(self))
