#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -o /dev/null -s -w -L "%{http_code}" "$1"
