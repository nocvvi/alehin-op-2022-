# -*- coding: utf-8 -*-
def maxx ():
    max = 0
    i = 0
    N = int(input('add N:'))
    while True:
        if N == 0:
            break
        next = int(input('n:'))
        if next == N:
            i += 1
            if i > max:
                max = i
        else:
            i = 0
        N = next
    print(max+1)
maxx()