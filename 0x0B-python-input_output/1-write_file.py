#!/usr/bin/python3
"""
function that writes a string to a text file
"""


def write_file(filename="", text=""):
    '''writes a string and to a text file
    Returns number of characters
    '''
    count = 0
    with open(filename, "w+", encoding="UTF-8") as newfile:
        return newfile.write(text)
