# -*- coding: utf-8 -*-

def dichotomie (f,a,b,eps) :
    c = (a+b)/2
    
    while (abs(f(c)) > eps) :
        if (f(a)*f(b) < 0) :
            b =c
        else :
            a = c
        c = (a+b)/2
    return c