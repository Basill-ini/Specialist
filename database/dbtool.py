#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import logging
import sys
from contextlib import contextmanager


@contextmanager
def transaction(connection, operation_name='Operation'):
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        exc_type, _, _ = sys.exc_info()
        if exc_type is not None:
            connection.rollback()
            logging.info(f'{operation_name} canceled')
        else:
            connection.commit()
            logging.info(f'{operation_name} execute')
