# -*- coding: utf-8 -*-

from contextlib import redirect_stdout
def matr():
    file = open('АДА_У-222_vvod.txt', 'r')
    global A
    A = file.readlines()
    for i in range(len(A)):
        A[i] = A[i].split(' ')
        for j in range(len(A[i])):
            A[i][j] = int(A[i][j])
    file.close()

def vvod(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=' ')
        print()

def maxx(A):
    maxX=A[0][0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if maxX < A[i][j]:
                maxX = A[i][j]
                D = i
                F = j
    D1 = 0
    F1 = 0
    for i in range(len(A)):
        Z = A[i][F1]
        A[i][F1] = A[i][F]
        A[i][F] = Z
    for j in range(len(A)):
        Z = A[D1][j]
        A[D1][j] = A[D][j]
        A[D][j] = Z

A = []
matr()


with open('АДА_У-222_vivod.txt', 'w') as file:
    with redirect_stdout(file):
        print("Исходный массив:")
        vvod(A)
        maxx(A)
        print("Итоговый массив:")
        vvod(A)