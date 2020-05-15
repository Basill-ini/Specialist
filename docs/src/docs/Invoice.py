#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from .Document import Document
from datetime import datetime


class Invoice(Document):

    def __init__(self, number=None):
        super().__init__(number)
        self.__counterparty = None

    @property
    def counterparty(self):
        return self.__counterparty

    @counterparty.setter
    def counterparty(self, new_counterparty):
        self.__counterparty = new_counterparty

