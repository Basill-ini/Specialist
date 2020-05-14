#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import requests

def run_client():

    requests.get('http://192.168.1.69:8080/')
    print(response.text)
