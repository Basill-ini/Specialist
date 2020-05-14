#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from http.server import HTTPServer
from RequestHandler import RequestHandler
from queue import Queue


class HttpServer(HTTPServer):

    def __init__(self, server_address, queue_size=10):
        super().__init__(server_address, RequestHandler)
        self.__queue = Queue(queue_size)

    @property
    def queue(self):
        return self.__queue
