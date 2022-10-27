# -*- coding: utf-8 -*-
def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return ("Да")
    else:
        return ("Нет")
Year = int(input('add year:'))
print(leap(Year))
