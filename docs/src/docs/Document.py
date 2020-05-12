#!/usr/bin/env python 3
# -*- confing: utf-8 -*-

from datetime import datetime


class Document(object):

    def __init__(self, number=None):
        self.__date_of_creation = datetime.now()
        self.__number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        self.__number = new_number

    @property
    def date_creation(self):
        return self.__date_of_creation

    def show(self):
        print(40*'=')
        print(f'Document No: {self.__number}')
        ct = self.date_creation.strftime('%Y.%m.%d %H:%M')
        print(f'Created: {ct}')
        print(40 * '=')