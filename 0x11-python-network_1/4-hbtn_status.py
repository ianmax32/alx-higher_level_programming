#!/usr/bin/python3
"""
this script fetches https://alx-intranet.hbtn.io/status
using the package requests
"""


import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r)))
    print('\t- content: {}'.format(r))
