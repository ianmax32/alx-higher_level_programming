#!/usr/bin/python3
"""
this script takes your GitHub credentials (username and password) 
and uses the GitHub API to display your id
"""


import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get('https://api.github.com/user',
                         auth=(argv[1], argv[2])).json()
        print(r.get('id'))
    except:
        print('None')
