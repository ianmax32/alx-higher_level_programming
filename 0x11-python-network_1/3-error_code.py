#!/usr/bin/python3
"""
this script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


from urllib import request, parse, error
from sys import argv


if __name__ == "__main__":
    try:
        req = request.Request(argv[1])
        with request.urlopen(req) as ans:
            print(ans.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
