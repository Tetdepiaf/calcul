# -*- coding: utf-8 -*-

from scipy.integrate import quad

f = lambda x : x**2

integrale = quad(f,0,1)