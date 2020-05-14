#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import threading
from http.server import HTTPServer
from RequestHandler import RequestHandler


def run_server():
    server_address = ('', 8080)
    server = HTTPServer(server_address, RequestHandler)
    # stream service object
    thread = threading.Thread(group=None, target=server.serve_forever)
    thread.start()
    input('Press ENTER to stop server')
    # stop server
    server.shutdown()
    while thread.is_alive():
        thread.join(5.0)
        if thread.is_alive():
            x = input('Server is running, do you want wait? [Y/N]: ')
            if x == 'N' or x == 'n':
                break
