# -*- coding: utf-8 -*-

import numpy as np

def pivot(A,k) :
    n, nn = np.shape(A)
    assert n == nn
    G = np.ones((n,n))
    G = np.diagflat(np.diag(G))
    for i in range(k+1,n) : 
        G[i,k] = -A[i,k]/A[k,k]           
    return G
    
def Gauss(A,b) :
    n,nn = A.shape
    assert n == nn
    An = A
    bn = b
    for i in range (0,n-1) :
        G = pivot(An,i)
        An = G.dot(An)
        somme = [0]*n
        for j in range (0,n) :
            for k in range(0,n) :
                somme[j] += G[j,k]*bn[k]
        bn = somme
        print(An,bn)
    return An, bn