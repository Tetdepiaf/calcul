# -*- coding: utf-8 -*-

def point_milieu (f,a,b,n) :
    integrale = 0
    for i in range(0,n-1) :
        integrale += f(a+((i+1/2)*(b-a))/n)
    integrale *= (b-a)/n
    return integrale