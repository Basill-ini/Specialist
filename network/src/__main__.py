#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import argparse
from server import run_server
from client import run_client


parser = argparser.ArgumentParser(description='Networking')
parser.add_argument('--server', dest='mode', action='store_const', const='server',
                    default=None, help='Run as server')
parser.add_argument('--client', dest='mode', action='store_const', const='client',
                    default=None, help='Run as client')

run_server()
