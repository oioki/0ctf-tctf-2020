#!/usr/bin/env python3

import string
import urllib

import requests


for l in range(1, 40):
    cmd = 'x' * l
    url = 'http://pwnable.org:47780/?action=upload&data=' + cmd
    r = requests.get(url)
    print("Payload length = {} => {}".format(l, r.text))

for c in string.printable:
    cmd = urllib.parse.quote_plus(c)
    url = 'http://pwnable.org:47780/?action=upload&data=' + cmd
    r = requests.get(url)
    print("Payload contains '{}' => {}".format(c, r.text))
