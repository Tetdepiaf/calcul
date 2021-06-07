# -*- coding: utf-8 -*-

def derivee(f,x,h) :
    fprime = []
    for i in x :
        fprime.append((f(i+h)-f(i-h))/(2*h))
    return fprime