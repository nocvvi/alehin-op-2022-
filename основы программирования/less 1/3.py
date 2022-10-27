# -*- coding: utf-8 -*-

age = int(input('Age: '))
name = input('Name: ')
if (0 < age < 75) and (name.lower() != 'Иван'):
    if (age >= 16):
        print('Поздравляем вы поступили в ВГУИТ')
    else:
        print('Сначала нужно окончить школу! Осталось лет:', 16 - age)
