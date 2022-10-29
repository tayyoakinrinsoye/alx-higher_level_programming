#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student

        Args:
            first_name(str): The forst name of the student
            last_name(str): The last name of the student
            age(int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of student instance
        if attrs is a list of strings, represet only those attributes 
        included in the list.

        Args:
            attrs (list): (optional) The attributes to represent
        """
        if (type(attrs) == list and
                all(types(ele) == str for ele in attrs)):
            return {key: getattr(self, k) for keys in attrs if hasattr(self, k)}
        return self.__dict__