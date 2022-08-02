#!/usr/bin/python3
"""
Function that reads a text file
"""


def read_file(filename=""):
    """reads a text fule (UTF8) and prints it to stdout
    Returns none
    """
    with open(filename, "r", encoding="UTF-8") as newfile:
        print(newfile.read())
