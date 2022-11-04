# -*- coding: utf-8 -*-
def sum_af(*arrays, total=[]):
    for arr in arrays:
        s, af = sum(arr), sum(arr) / len(arr)
        total.append((s, af))
    return total
print(sum_af([2, 2, 5, 7, 6, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 2, 3]))