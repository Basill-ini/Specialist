#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import logging
from trace import trace

logging.basicConfig(level=logging.DEBUG)

from time import sleep


@trace                  # func1 = trace(func1)
def func1(x, y):
    sleep(1.5)
    return 2 * x + y


@trace
def func2(a, b, c):
    sleep(2.0)
    return a + b * c


func1(20, 11)
func2(2, 3, 4)
func1(128, 16.3)
func2('Hello', 'world', 2)
