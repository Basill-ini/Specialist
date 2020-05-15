#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler
import json
import queue


class RequestHandler(BaseHTTPRequestHandler):
    # the constructor method is not created since class
    # instances are created automatically by the server

    # create a request handler method
    def do_GET(self):
        if self.path == '/count':
            # send the number of items in the queue
            N = self.server.queue.qsize()
            self.send_response(200)
            self.send_header('Content-type',
                             'text/html; charset=utf-8')
            self.end_headers()
            answer = f'''
                <html>
                    <body>
                        <p> In queue {N} elements </p> 
                    </body>
                </html>
            '''.encode('utf-8')
            self.wfile.write(answer)

        elif self.path == '/first':
            # send the first item in the queue
            self.send_response(200)
            self.send_header('Content-type',
                             'text/html; charset=utf-8')
            self.end_headers()

            try:
                elem = self.server.queue.get(block=True, timeout=3)
                name = elem['title']
                price = elem['price']
                answer = f'''
                    <html>
                        <body>
                            <table border="1">
                                <tr><td>Name</td><td>{name}</td></tr>
                                <tr><td>Price</td><td>{price}</td></tr>
                            </table>
                        </body>
                    </html>
                '''.encode('utf-8')
            except queue.Empty:
                answer = f'''
                <html>
                    <body>
                        <p> Queue is empty </p> 
                    </body>
                </html>
            '''.encode('utf-8')
            self.wfile.write(answer)
        else:
            self.send_error(404, 'Path not found')

    def do_POST(self):

        try:
            data_size = int(self.headers['Content-length'])
            data = self.rfile.read(data_size)
            data = data.decode('utf-8')
            data = json.loads(data)
            self.server.queue.put(data, block=True, timeout=5)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            # send response headers
            self.end_headers()
            answer = 'Message accepted'.encode('utf-8')
            self.wfile.write(answer)

        except queue.Full:
            self.send_error(423, 'Queue is full')
