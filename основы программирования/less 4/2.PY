# -*- coding: utf-8 -*-
def number(A, B):
    if A < B:
        for i in range(A, B + 1):
            print(i)
    else:
        for i in range(A, B - 1, -1):
            print(i)
A1 = int(input('add number A:'))
B1 = int(input('add number B:'))
print(number(A1,B1))
