#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

# this file will modify functions in main.py for measuring runtime
# actually we'll make a simple decorator
import logging
from datetime import datetime


# decorator
def trace(function):
    def traced_function(*args, **kwargs):
        t0 = datetime.now()
        result = function(*args, **kwargs)
        t = datetime.now() - t0
        name = function.__name__
        logging.debug(f'Функция {name} выполнялась {t} сек')
        return result

    return traced_function
