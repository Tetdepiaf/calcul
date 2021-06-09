# -*- coding: utf-8 -*-

def descente(L,b) :
    n, nn = L.shape
    assert n == nn
    x = [b[0]/L[0,0]]
    for i in range (1,n) :
        somme = 0
        for j in range(0,i) :
            somme += (b[i]-L[i,j]*x[j])/L[i,i]
        x.append(somme)
    return x