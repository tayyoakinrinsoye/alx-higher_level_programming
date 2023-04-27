#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS -i 0.0.0.0:5000 | grep "Allow" | cut -d " " -f2-
