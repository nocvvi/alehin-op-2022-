# -*- coding: utf-8 -*-
from math import floor
n = int(input('add a minutes'))
n = n % (60 * 24)
h = floor(n/60)
n = floor(n%60)
print(f'{str(h).zfill(2)}:{str(n).zfill(2)}')
