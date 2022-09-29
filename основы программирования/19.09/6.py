# -*- coding: utf-8 -*-
def chess(h1,w1,h2,w2):
    if ((h1 % 2 != 0 and w1 % 2 != 0) and ((h2 % 2 != 0) and (w2 % 2 != 0))) or ((h1 % 2 != 0 and w1 % 2 != 0) and (h2 % 2 == 0 and w2 % 2 == 0))\
            or ((h1 % 2 == 0 and w1 % 2 == 0) and (h2 % 2 == 0 and w2 % 2 == 0)) or ((h1 % 2 == 0 and w1 % 2 == 0) and (h2 % 2 != 0 and w2 % 2 != 0))\
            or ((h1 % 2 == 0 and w1 % 2 != 0) and (h2 % 2 == 0 and w2 % 2 != 0)) or ((h1 % 2 != 0 and w1 % 2 == 0) and (h2 % 2 != 0 and w2 % 2 == 0))\
            or ((h1 % 2 == 0 and w1 % 2 != 0) and (h2 % 2 != 0 and w2 % 2 == 0)) or ((h1 % 2 != 0 and w1 % 2 == 0) and (h2 % 2 != 0 and w2 % 2 == 0)):
        return("ДА")
    else:
        return("НЕТ")
H1=int(input("add column (from 1 to 8) first cell:"))
W1=int(input("add line (from 1 to 8) first cell:"))
H2=int(input("add column (from 1 to 8) second cell:"))
W2=int(input("add line (from 1 to 8) second cell:"))
print(chess(H1,W1,H2,W2))
