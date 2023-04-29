#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
    letter = argv[1]
    else:
    letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data={'q': letter})
    try:
        req_dict = req.json()
        id, name = req_dict.get('id'), req_dict.get('name')
        if len(req_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(req_dict.get('id'), req_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
