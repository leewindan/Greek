# -*- coding: utf-8 -*-

import time
from utils import func_cost


@func_cost
def man(name):
    time.sleep(5)
    print('%s is working' % name)


@func_cost
def woman(name):
    time.sleep(6)
    print('%s is sleeping' % name)


man('liwei')
woman('zhoudandan')

