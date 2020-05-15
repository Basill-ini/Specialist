#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import requests
import json


def run_client():
    title = input('Title: ').strip()
    price = input('Price: ').strip()
    if price == '':
        price = 0
    else:
        price = int(price)

    # pack object data into JSON
    data = {
        'title': title,
        'price': price
    }
    data = json.dumps(data).encode('utf-8')

    # post data to server
    response = requests.post('http://192.168.1.69:8080/tovar', data=data)
    print(response.text)
