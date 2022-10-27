# -*- coding: utf-8 -*-
y = int(input('add y:'))
def run(x):
    d = 1
    while y-x > 0:
        x =x+(x/100*10)
        d += 1
    print('день № ', d)

run(int(input('add x: ')))
