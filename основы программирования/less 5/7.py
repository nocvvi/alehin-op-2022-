# -*- coding: utf-8 -*-
def lenght ():
    i = 0
    n = int(input('add n;'))
    while True:
        if n == 0:
            break
        next = int(input('n1:'))
        if next>n:
            i+=1
        n=next
    print('', i)
lenght()