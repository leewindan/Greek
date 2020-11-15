# -*- coding: utf-8 -*-
from faker import Factory

a = 'abc[12P]|def|hij - Bt7086'
b = a.split('|')
print(b)


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
