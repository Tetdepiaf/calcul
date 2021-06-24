# -*- coding: utf-8 -*-

def trapeze (f,a,b,n) :
    integrale = f(a)/2+f(b)/2
    for i in range(1,n-1) :
        integrale += f(a+(i*(b-a))/n)
    integrale *= (b-a)/n
    return integrale