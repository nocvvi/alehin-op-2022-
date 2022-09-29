# -- coding: utf-8 --
def shoe(a1,b1,l1,N1):
    return 2*l1+2*(b1*((N1-2)/2))+a1*(N1-1)
a=int(input('width:'))
b=int(input('length:'))
l=int(input('length of free lace:'))
N=int(input('quantity:'))
print(shoe(a,b,l,N))
