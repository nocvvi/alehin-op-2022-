# -*- coding: utf-8 -*-
def fib (K,N):
    s = 0
    x = 1
    y = 1
    for i in range(3, N + K):
        x, y = y, x + y
        if i >= K:
            s += y
    print('sum = ', s)
fib(int(input('ADD k: ')), int(input('ADD n: ')))