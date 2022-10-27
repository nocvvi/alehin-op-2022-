# -*- coding: utf-8 -*-

def divider(N):
    if N>= 2:
        for i in range(2, N+1):
            if N%i == 0:
                print(i)
                break
divider(int(input('N:')))