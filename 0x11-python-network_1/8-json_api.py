#!/usr/bin/python3
"""
this script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys


if __name__ == "__main__":
    try:
        value = ""
        if sys.argv == 2:
            value = sys.argv[1]
            r = requests.post('http://0.0.0.0:5000/search_user',
                             info={'q': value}).json()
            r.raise_for_status()
            if ('name' in r) and ('id' in r):
                print('[{}] {}'.format(r['id'], r['name']))
            else:
                print('No result')
        else:
            print('Not a valid JSON')
    except:
        print('Error code {}'.format(r.status_code))
