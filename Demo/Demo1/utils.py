# -*- coding: utf-8 -*-

import time


def func_cost(func):
    def wrapper(*args):
        tbegin = time.time()
        function_return = func(*args)
        tend = time.time()
        tcost = tend - tbegin
        print('time cost -> %f' % tcost)
        return function_return
    return wrapper
