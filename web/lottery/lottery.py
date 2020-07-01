#!/usr/bin/env python3

import base64
import json
import time
import sys

import requests

URL_REGISTER = 'http://pwnable.org:2333/user/register'
URL_LOGIN = 'http://pwnable.org:2333/user/login'
URL_LOTTERY_BUY = 'http://pwnable.org:2333/lottery/buy'
URL_LOTTERY_INFO = 'http://pwnable.org:2333/lottery/info'
URL_LOTTERY_CHARGE = 'http://pwnable.org:2333/lottery/charge'
URL_USER_INFO = 'http://pwnable.org:2333/user/info'


def jprint(s):
    return
    print(json.dumps(s, indent=2))

def hexprint(enc):
    print('URL: http://pwnable.org:2333/lottery.html#' + enc)
    # return
    base64_bytes = enc.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    hx = message_bytes.hex()
    for block in range(8):
        print(hx[block*32:(block+1)*32])

def register_login_user(username, password):
    data = {
        "username": username,
        "password": password,
    }
    r = requests.post(URL_REGISTER, data=data)
    # jprint(r.json())
    user_uuid = r.json()['user']['uuid']


    r = requests.post(URL_LOGIN, data=data)
    # jprint(r.json())
    return r.json()['user']['api_token']


def buy_lottery(api_token):
    data = {
        "api_token": api_token,
    }
    r = requests.post(URL_LOTTERY_BUY, data=data)
    jprint(r.json())
    return r.json()['enc']

def lottery_info(enc):
    r = requests.post(URL_LOTTERY_INFO, data={'enc': enc})
    jprint(r.json())
    return r.json()


if len(sys.argv) == 1:
    api_token_1 = register_login_user("oioki_{}".format(time.time()), "123")
    print('document.cookie="api_token={}"'.format(api_token_1))

    enc = buy_lottery(api_token_1)
    print(enc)

    j = lottery_info(enc)
    last_lottery_byte = j['info']['lottery'][-2:]
    print('Last lottery byte: ' + last_lottery_byte)

else:
    # output from "acceptor" mode
    enc = 'i5VeFFu0KrUjvGwZxJmGepS4OzgyqalkkUHG5flFe92+gbg/MoV9P76EPnyWZK7pBnzWzO+YYdEDsRBi2CvefThAtNCadCrW53Og2C2dFoij8gxpYhYEGxvuKNLG+DJBjB1krI4SV5QlYc6hVxqsVvbSt9reYD8AcCI4hIXsxZg='
    last_lottery_byte = 'e5'

    # hexprint(enc)
    bytes1 = base64.b64decode(enc.encode('ascii'))

    while True:
        api_token_2 = register_login_user("oioki2_" + str(time.time()), "123")
        enc2 = buy_lottery(api_token_2)
        # hexprint(enc2)
        jj = lottery_info(enc2)

        bytes2 = base64.b64decode(enc2.encode('ascii'))

        # replace lottery_uuid block
        tampered_bytes = bytes2[0:3*16] + bytes1[3*16:]

        base64_encoded_data = base64.b64encode(tampered_bytes)
        enc_candidate = base64_encoded_data.decode('utf-8')

        last_lottery_byte2 = jj['info']['lottery'][-2:]
        print('Last byte:', last_lottery_byte2)
        if last_lottery_byte2 == last_lottery_byte:
            print('URL: http://pwnable.org:2333/lottery.html#' + enc_candidate)
            print('LUCKY!!!')
