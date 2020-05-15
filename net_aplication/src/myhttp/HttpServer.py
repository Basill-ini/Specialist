#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from http.server import HTTPServer
from .RequestHandler import RequestHandler
from queue import Queue
import threading


class HttpServer(HTTPServer):

    def __init__(self, server_address, queue_size=10):
        super().__init__(server_address, RequestHandler)
        self.__queue = Queue(queue_size)

    @property
    def queue(self):
        return self.__queue

    @classmethod
    def srv_start(cls, server_address, queue_size):
        server = cls(server_address, 20)
        # stream service object
        thread = threading.Thread(group=None, target=server.serve_forever)
        thread.start()

        return (server, thread)
