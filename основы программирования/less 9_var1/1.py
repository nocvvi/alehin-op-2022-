# -*- coding: utf-8 -*-
c = 0
s = 0
n = 3
a = []
for i in range (n):
    b=[]
    for j in range (n):
        print('Введите [', i,' ,', j,'] элемент')
        b.append(int(input('add')))
    a.append(b)

for i in range (n):
    for j in range (n):
        print("%2d " % A[i][j], end='')
    print()

for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            s += a[i][j]
            c += 1
print("колличество:",c)
print("sum:",s)