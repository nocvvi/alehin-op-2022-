# -*- coding: utf-8 -*-
def ar():
    array = []
    n = int(input('add len arrary:'))
    for i in range(n):
        array.append(input('Add number: '))
    print('MAX: ' + (max(array)))
    print('reverse order: ' + str(list(reversed(array))))
ar()