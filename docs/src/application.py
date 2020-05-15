#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import docs
from decimal import Decimal
import pickle
from CmdParams import CmdParams
from BaseConfig import BaseConfig

class Application(CmdParams, BaseConfig):

    def __init__(self):
        CmdParams.__init__(self)
        BaseConfig.__init__(self, self.config_path)
        self.__current_document = None
        self.__no_doc = {
            '1': ('Create nakladnaya', self.create_nakl),
            '7': ('Load document', self.load_current_doc),
            '8': ('Create Invoice', self.create_invoice)
        }
        self.__with_nakladnaya = {
            '2': ('Add position in nakladnay', self.add_pos_in_nakl),
            '3': ('Show document', self.current_doc_show),
            '4': ('Change number of document', self.number_change),
            '5': ('Save document', self.save_current_doc),
            '6': ('Delete document', self.delete_current_doc),
            '9': ('Enter delivery address', self.set_address)
        }
        self.__with_invoice = {
            '3': ('Show document', self.current_doc_show),
            '4': ('Change number of document', self.number_change),
            '5': ('Save document', self.save_current_doc),
            '6': ('Delete document', self.delete_current_doc)
        }

    def available_commands(self):
        if self.__current_document is None:
            return self.__no_doc
        elif isinstance(self.__current_document, docs.Nakladnaya):
            return self.__with_nakladnaya
        elif isinstance(self.__current_document, docs.Invoice):
            return self.__with_invoice
        else:
            raise NotImplementedError('Unknown type of document')

    def user_actions_sequnce(self):
        while True:
            cmd = self.available_commands()
            for symbol, contents in cmd.items():
                print(f'{symbol} - {contents[0]}')
            print('0 - Exit')
            action = input(':  ').strip()
            if action == '0':
                break
            elif action in cmd:
                yield cmd[action][1]  # this is link for handler function
            else:
                print('Unknown command')

    def create_nakl(self):
        num = input('Number: ').strip()
        self.__current_document = docs.Nakladnaya(number=int(num))

    def create_invoice(self):
        num = input('Number: ').strip()
        self.__current_document = docs.Invoice(number=int(num))

    def add_pos_in_nakl(self):
        title = input('Title: ').strip()
        quantity = input('Quantity: ').strip()
        price = input('Price: ').strip()
        summa = input('Summa: ').strip()
        quantity = int(quantity)
        if price == '':
            price = None
        else:
            price = Decimal(price)
        if summa == '':
            summa = None
        else:
            summa = Decimal(summa).quantize(Decimal('0.01'))
        self.__current_document.add_pos(title, quantity, price, summa)

    def number_change(self):
        number = input('Enter new number: ').strip()
        self.__current_document.number = int(number)

    def set_address(self):
        addr = input('Enter delivery address: ').strip()
        self.__current_document.address = addr

    def current_doc_show(self):
        self.__current_document.show()

    def delete_current_doc(self):
        self.__current_document = None

    def save_current_doc(self):
        filepath = input('File: ').strip()
        with open(filepath, 'wb') as trg:
            pickle.dump(self.__current_document, trg, fix_imports=False)

    def load_current_doc(self):
        filepath = input('File: ').strip()
        with open(filepath, 'rb') as src:
            self.__current_document = pickle.load(src, fix_imports=False)

    def run(self):
        for action in self.user_actions_sequnce():
            action()
