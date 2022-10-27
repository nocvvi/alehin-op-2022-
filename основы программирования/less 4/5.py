# -*- coding: utf-8 -*-
def sum(n,s):
    s=0
    for i in range(1,n+1):
        s+=i**3
    return(s)
n=int(input("add Number:"))
k=0
print(sum(n,k))