# -*- coding: utf-8 -*-
def the_same(a, b, c):
    if a == b and b == c:
        return ('3')
    elif a == b or b == c or a == c:
        return ('2')
    else:
        return ('0')
A=int(input('a:'))
B=int(input('b:'))
C=int(input('c:'))
print(the_same(A,B,C))
