#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from .Document import Document
from .NakPos import NakPos


class Nakladnaya(Document):

    def __init__(self, number=None):
        super().__init__(number)
        self.__delivery_address = None
        self.__positions = []

    @property
    def good(self):
        if self.__delivery_address is None:
            return False
        if len(self.__positions) == 0:
            return False
        else:
            return all((p.good for p in self.__positions))

    @property
    def address(self):
        return self.__delivery_address

    @address.setter
    def address(self, new_address):
        self.__delivery_address = new_address

    @property
    def totalAmount(self):
        s = (x.summa for x in self.__positions)
        return sum(s)

    # Realize method
    def add_pos(self, *args, **kwargs):
        pos_info = NakPos(*args, **kwargs)
        self.__positions.append(pos_info)

    # polymorphic method
    def show(self):
        print(40 * '=')
        print(f'Nakladnaya No {self.number}')
        print(40 * '=')
        ct = self.date_creation.strftime('%Y.%m.%d %H:%M')
        print(f'Date of creation: {ct}')
        if self.address is not None:
            print(f'Delivery address: {self.address}')  # self.address it is property!
        else:
            print('Address is missing')
        print(40 * '-')
        for k, pos in enumerate(self.__positions, 1):
            print(f'{k:3}.  {pos}')
        print(f'Total: {self.totalAmount:7.2f}')
        print(40 * '=')
        if not self.good:
            print('Warning! Incorrect document')
        else:
            print('The document is ready for certification')
        print(40 * '=')