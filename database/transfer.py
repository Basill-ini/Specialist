#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from dbtool import transaction
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
connection = sqlite3.connect('accounts.sqlite3')


# context manager
with transaction(connection, 'Payment for services') as cursor:
    cursor.execute('''
        update accounts
            set sum = sum - 100
            where id = 1;
    ''')

    cursor.execute('''
        update accounts
            set sum = sum + 100
            where id = 2;
    ''')

with transaction(connection) as cursor:
    cursor.execute('''
        select id, name, sum
            from accounts;
    ''')

for id, name, sum in cursor:
    print(id, name, sum)

connection.close()
