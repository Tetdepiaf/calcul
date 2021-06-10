# -*- coding: utf-8 -*-

import numpy as np

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

def F(u):
    du = np.empty(2)
    du[0] = u[1]
    du[1] = -kp*kp*np.sin(u[0])
    return du

def euler(F,U0,ti,tf,N):
    m = np.size(U0)
    dt = (tf-ti)/N # taille du pas
    t = np.linspace(ti, tf, N+1)
    u = np.empty([N+1,m]); u[0,:] = U0
    for k in range(N):
        du = F(u[k,:])
        u[k+1,:] = u[k,:] + du*dt
    return (t, u)
t, u = euler(F, [theta0, omega0], ti, tf, N)