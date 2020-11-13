# -*- coding: utf-8 -*-

from faker import Factory

f = Factory.create()

print(f.user_agent())
print(f.user_agent())
print(f.user_agent())
print(f.user_agent())


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b+1
        # print b
        a, b = b, a + b
        n = n + 1

for i in fab(10):
    print(i)
