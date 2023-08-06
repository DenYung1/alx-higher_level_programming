#!/usr/bin/python3

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    bodyresp = response.read()
    print("Body response:")
    print('\t- type: {}'.format(type(bodyresp)))
    print('\t- content: {}'.format(bodyresp))
    print('\t- utf8 content: {}'.format(bodyresp.decode('utf-8')))
