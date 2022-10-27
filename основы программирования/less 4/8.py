# -*- coding: utf-8 -*-

def steps(n):
    ts = ''
    for i in range(1, n + 1):
        ts += ''.join(map(str, range(1, i + 1))) + '\n'
    return ts
print(steps(int(input('n: '))))
