#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler
import json


class RequestHandler(BaseHTTPRequestHandler):
    # the constructor method is not created since class
    # instances are created automatically by the server

    # create a request handler method
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        # send response headers
        self.end_headers()
        answer = 'Работает'.encode('utf-8')
        self.wfile.write(answer)

    def do_POST(self):

        data_size = int(self.headers['Content-length'])

        data = self.rfile.read(data_size)
        data = data.decode('utf-8')
        data = json.loads(data)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        # send response headers
        self.end_headers()
        answer = 'Все хорошо'.encode('utf-8')
        self.wfile.write(answer)
