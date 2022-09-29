# -*- coding: utf-8 -*-
from functools import reduce
def sum(n):
    end = 0
    for i in range(1, n + 1):
        end += reduce((lambda x, y: x * y), range(1, i + 1))
    return end
print(sum(int(input('n: '))))
