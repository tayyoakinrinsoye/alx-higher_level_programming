#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    auth = HTTPBasicAuth(username, passwd)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
