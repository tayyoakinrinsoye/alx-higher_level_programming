#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    status = req.status_code
    print(req.text) if status < 400 else print(\
        f"Error code: {req.status_code}")
