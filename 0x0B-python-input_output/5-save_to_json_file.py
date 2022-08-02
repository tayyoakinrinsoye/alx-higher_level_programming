#!/usr/bin/python3
"""Save object to file"""

import json


def save_to_json_file(my_obj, filename):
    '''function that writes an object to a text file using JSON representation'''

    nf = json.dumps(my_obj)
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(nf)
