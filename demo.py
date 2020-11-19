# -*- coding: utf-8 -*-
from faker import Factory
import datetime

today = datetime.datetime.now()
print(today.year)
print('%02d' % today.month)
print('%02d' % today.day)
print('%02d' % today.hour)
print('%02d' % today.minute)

# a = 'abcdefg'
# for i in a:
#     if i == 'c' or i == 'f':
#         continue
#     print('Now printing -> {}'.format(i))

# f = Factory.create()
#
# print(f.user_agent())
# print(f.user_agent())
# print(f.user_agent())
# print(f.user_agent())


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         print('after first yield')
#         yield b*10
#         print('after second yield')
#         # print b
#         a, b = b, a + b
#         n = n + 1
#
#
# for i in fab(10):
#     print(i)
