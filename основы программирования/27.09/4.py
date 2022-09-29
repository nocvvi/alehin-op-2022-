# -*- coding: utf-8 -*-
def sum(N):
    end = 0
    for i in range(N):
        end += int(input(str(i + 1) + ' number: '))
    print(end)

print((sum(int(input('N: ')))))
