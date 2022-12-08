# -*- coding: utf-8 -*-
def posled():
    n = int(input('add number:'))
    if n == 0:
        return [float('-inf')]
    return sorted([n] + posled())
def run():
    print(posled()[-2])
run()