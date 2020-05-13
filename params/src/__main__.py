#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import logging
from CmdParams import CmdParams

par = CmdParams()

logging.basicConfig(level=par.param('level'))

print(f'Code of workplace  = {par.wp_name}')
print(f'Path to config  = {par.config_path}')

# output application log
# constant option
logging.debug('This is debug message')
logging.info('This is information message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical error')

# access via internet
# switch option
if par.param('internet_on'):
    print('Доступ по итернету возможен')
else:
    print('Интернет отключен')
