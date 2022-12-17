#!/usr/bin/python3
"""
this script takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""


from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    email = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], email)
    with request.urlopen(req) as ans:
        print(ans.read().decode('utf-8'))
