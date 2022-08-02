#!/usr/bin/python3
"""
function to append to a file
"""


def append_write(filename="", text=""):
    '''function to append a string at the end of a text file
    '''
    with open(filename, "a", encoding="UTF-8") as newfile:
        return newfile.write(text)
