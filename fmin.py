# -*- coding: utf-8 -*-

from scipy.optimize import fmin
f = lambda x : x**2

min_loc = fmin(f,0) # Il faut entrer une valeur initiale