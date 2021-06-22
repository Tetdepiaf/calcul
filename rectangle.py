# -*- coding: utf-8 -*-

def rectangle (f,a,b,n) : # a et b sont les bornes et n la précision de l'intervalle
    integrale = 0
    for i in range(0,n-1) :
        integrale += f(a+(i*(b-a))/n)
    integrale *= (b-a)/n
    return integrale