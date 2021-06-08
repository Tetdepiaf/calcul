# -*- coding: utf-8 -*-

def derivee_seconde(f,x,h) :
    fseconde = []
    for i in x :
        fseconde.append((f(i+h)-2*f(i)+f(i-h))/(h**2))
    return fseconde