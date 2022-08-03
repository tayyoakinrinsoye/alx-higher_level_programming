#!/usr/bin/python3
'''
Create object from a JSON file
'''
import json


def load_from_json_file(filename):
    """
    function to create an object from a JSON file
    """
    with open(filename, "r+", encoding="UTF-8") as f:
        return json.load(f)
