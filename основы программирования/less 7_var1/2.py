# -*- coding: utf-8 -*-
def ar():
    a = [1, 0, 2, 3, 0, 4, 5]
    sr = 0
    for i in range(len(a)):
        sr = sum(a) / len(a)
        if a[i] == 0:
            a[i] = sr
    print(a)
ar()