# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import odeint

# Equation différentielle : d²x/dt² + k²x = 0 (pendule conservatif)

L = 1 # m
g = 9.81 # m.s^(-2)
kp = g/L
Tp = 2*np.pi/kp # période (s)
ti = 0. # s (temps initial)
tf = 3.*Tp # s (temps final)
theta0 = np.pi/4 # radians
omega0 = 0. # radians/s
N = 10000

def Fode(u,t):
    du = np.empty(2)
    du[0] = u[1]
    du[1] = - kp*kp*np.sin(u[0])
    return du

tode = np.linspace(ti, tf, N+1) # = t
uode = odeint(Fode, [theta0, omega0], tode)