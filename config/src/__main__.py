#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from pathlib import Path
import configparser
from BaseConfig import BaseConfig

confpath = Path.cwd() / 'example.conf'

config = configparser.ConfigParser()
config.read(confpath)

# Get the link to the desired section
general = config['GENERAL']

# Get settings from the selected section and default path of document
x = Path(general.get('doc_path', Path.cwd()/'docs.conf'))

wsp = config['WORKPLACES']

wp_codes = list(wsp.values())

for code in wp_codes:
    # Some keys can be missing, catch exceptions
    try:
        wp = config[code]
    except KeyError:
        continue
    ip = wp.get('IP', None)
    port = wp.get('Port', None)
    if port is not None:
        port = int(port)
    print(f'Code: {code}')
    print(f'IP: {ip}')
    print(f'Port: {port}')
    print(40*'=')

myconf = BaseConfig(confpath)

print(myconf.doc_path)

for ws in myconf.workplaces:
    print(myconf.workplace(ws))

