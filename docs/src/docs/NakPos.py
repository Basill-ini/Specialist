#!/usr/bin/env python 3
# -*- coding: utf-8 -*-


class NakPos(object):

    def __init__(self, title, quantity=1, price=None, summa=None):
        self.__title = title
        self.__quantity = quantity
        self.__price = price
        self.__summa = summa

    # Create func which will return title of position
    # @property implements a property
    @property
    def good(self):
        if self.__price is None:
            return self.__summa is not None
        return self.quantity * self.price == self.summa

    @property
    def title(self):
        return self.__title

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def summa(self):
        if self.__summa is not None:
            return self.__summa
        else:
            summa = self.quantity * self.price
        return summa

    @summa.setter
    def summa(self, new_summa):
        self.__summa = new_summa

    @summa.deleter
    def summa(self):
        self.__summa = None

    # Text representation of the object
    def __str__(self):
        if self.__price is None:
            return f'Title: {self.title:15} || ' \
                   f'Quantity: {self.quantity:3} || ' \
                   ' -----  || ' \
                   f'Total: {self.summa:6.2f} $ || '
        else:
            return f'Title: {self.title:15} || ' \
               f'Quantity: {self.quantity:3} || ' \
               f'Price: {self.price:5.2f} $ || ' \
               f'Total: {self.summa:6.2f} $ || '