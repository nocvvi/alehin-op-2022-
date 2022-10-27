# -*- coding: utf-8 -*-
def chocolate(n,m,k):
    if k % n == 0 or k % m == 0:
        print('Да')
        return
    print('Нет')

N=int(input("n:"))
M=int(input("m:"))
K=int(input("k:"))
print(chocolate(N,M,K))
