# -*- coding: utf-8 -*-

a = int(input('enter num='))
def posled(a):
    s = []
    s.append(a)
    while str(a) != '0':
        b = int(input('enter num='))
        if str(b) != '0':
            s.append(a)
            s.append(b)
            mins = min(s)
            maxim = max(s)
            for i in range(len(s)):
                if s[i] > mins and s[i] < maxim:
                    mins = s[i]
        else:
            print(mins)
            break
print(posled(a))
