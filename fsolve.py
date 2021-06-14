# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import fsolve

x0 = np.linspace(-10,10,20) # liste de valeurs initiales
f = lambda x : x**2

zeros = fsolve(f,x0) # x0 est une liste de valeurs initiales
zeros = np.around(zeros, decimals=4)  # arrondit les racines à une certaine précision
zeros = np.unique(zeros) # enlève les racines en double