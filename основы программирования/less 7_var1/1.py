# -*- coding: utf-8 -*-
array = []
n = 8
for i in range(n):
    array.append(input('Add number: '))
print('MAX: ' + str(max(array)))
print('reverse order: ' + str(list(reversed(array))))
