#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import argparse
from server import run_server
from client import run_client


parser = argparse.ArgumentParser(description='Networking')
parser.add_argument('--server', dest='mode', action='store_const', const=run_server,
                    default=None, help='Run as server')
parser.add_argument('--client', dest='mode', action='store_const', const=run_client,
                    default=None, help='Run as client')

ARGS = parser.parse_args()

if ARGS.mode is not None:
    ARGS.mode()
else:
    print('Unknown option')

