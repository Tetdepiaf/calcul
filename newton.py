# -*- coding: utf-8 -*-

def Newton (f,fprime,x0,eps) :
    while (abs(f(x0)) > eps) :
        x0 = x0 - f(x0)/fprime(x0)
    return x0