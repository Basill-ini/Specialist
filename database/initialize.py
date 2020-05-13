#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('accounts.sqlite3')

# for creation database we need client's cursor
cursor = connection.cursor()

cursor.execute('''
   create table accounts (
    id integer not null primary key,
    name text,
    sum numeric(22,2) );
''')

cursor.execute('''
   insert into accounts(id, name, sum)
    values(?,?,?);    
''', (1, 'Bredbery', 10.03))


cursor.execute('''
   insert into accounts(id, name, sum)
    values(?,?,?);    
''', (2, 'Jonson', 12.03))

cursor.execute('''
    select id, name, sum
        from accounts;
''')

# sql injection
for id, name, sum in cursor:
    print(id, name, sum)

# save all changes in database and close
connection.commit()
connection.close
