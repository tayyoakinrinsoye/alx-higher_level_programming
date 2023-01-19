#!/usr/bin/python3
""" Script that fetches
 - https://alx-intranet.hbtn.io/status
 - using urllib package
"""

if __name__ ==  '__main__':
	import urllib.request

	with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
		the_page = response.read()
		print("Body response:")
		print("\t- type: {}".format(type(the_page)))
		print("\t- content: {}".format(the_page))
        	print("\t- utf8 content: {}".format(the_page.decode('utf-8')))
