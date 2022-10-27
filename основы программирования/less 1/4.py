# -*- coding: utf-8 -*-

from math import floor

seconds = int(input('Enter a value: '))
days = floor(seconds / 3600 / 24)
seconds -= days * 3600 * 24
hours = floor(seconds / 3600)
seconds -= hours * 3600
minutes = floor(seconds / 60)
seconds -= minutes * 60
print(f'{days}:{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
