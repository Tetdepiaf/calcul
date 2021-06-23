# -*- coding: utf-8 -*-

def remontee(U,b) :
    n, nn = U.shape
    assert n == nn
    x = [b[n-1]/U[n-1,n-1]]
    for i in range (n-1,0,-1) :
        somme = 0
        for j in range(n-1,i,-1) :
            somme += (b[i]-U[i,j]*x[n-1-j])/U[i,i]
        x.append(somme)
    x.reverse()
    return x