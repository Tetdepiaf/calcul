# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import fsolve, fmin
from scipy.integrate import quad, odeint
import matplotlib.pyplot as plt

f = lambda x : x**2


""" Zéros, min, max """ 

# Algorithme de Dichotomie 

def dichotomie (f,a,b,eps) :
    c = (a+b)/2
    
    while (abs(f(c)) > eps) :
        if (f(a)*f(b) < 0) :
            b =c
        else :
            a = c
        c = (a+b)/2
    return c
    
# Méthode de Newton

def Newton (f,fprime,x0,eps) :
    while (abs(f(x0)) > eps) :
        x0 = x0 - f(x0)/fprime(x0)
    return x0


# Fonction fsolve
   
x0 = np.linspace(-10,10,20) # liste de valeurs initiales

zeros = fsolve(f,x0) # x0 est une liste de valeurs initiales
zeros = np.around(zeros, decimals=4)  # arrondit les racines à une certaine précision
zeros = np.unique(zeros) # enlève les racines en double

# Recherche des minimums locaux d'une fonction (pour rechercher les maximums on utilise -f(x))

min_loc = fmin(f,0) # Il faut entrer une valeur initiale

""" Intégration """

# Méthode des rectangles

def rectangle (f,a,b,n) : # a et b sont les bornes et n la précision de l'intervalle
    integrale = 0
    for i in range(0,n-1) :
        integrale += f(a+(i*(b-a))/n)
    integrale *= (b-a)/n
    return integrale


# Méthode du point-mileu

def point_milieu (f,a,b,n) :
    integrale = 0
    for i in range(0,n-1) :
        integrale += f(a+((i+1/2)*(b-a))/n)
    integrale *= (b-a)/n
    return integrale

# Méthode des trapèzes

def trapeze (f,a,b,n) :
    integrale = f(a)/2+f(b)/2
    for i in range(1,n-1) :
        integrale += f(a+(i*(b-a))/n)
    integrale *= (b-a)/n
    return integrale

# Fonction quad

integrale = quad(f,0,1)
 

""" Dérivation """

def derivee(f,x,h) :
    fprime = []
    for i in x :
        fprime.append((f(i+h)-f(i-h))/(2*h))
    return fprime

def derivee_seconde(f,x,h) :
    fseconde = []
    for i in x :
        fseconde.append((f(i+h)-2*f(i)+f(i-h))/(h**2))
    return fseconde

""" Résolution des équation différentielle ordinaires """

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

# Méthode d'Euler 

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

# Fonction odeint

def Fode(u,t):
    du = np.empty(2)
    du[0] = u[1]
    du[1] = - kp*kp*np.sin(u[0])
    return du

tode = np.linspace(ti, tf, N+1) # = t
uode = odeint(Fode, [theta0, omega0], tode)

# Méthode de Runge-Kutta d'ordre 4

""" Résolution des systèmes d'équations Ax = b """

# Méthode de Gauss sans pivotage (obtention d'un système triangulaire supérieur)

def pivot(A,k) :
    n, nn = np.shape(A)
    assert n == nn
    G = np.ones((n,n))
    G = np.diagflat(np.diag(G))
    for i in range(k+1,n) : 
        G[i,k] = -A[i,k]/A[k,k]           
    return G
    
def Gauss(A,b) :
    n,nn = A.shape
    assert n == nn
    An = A
    bn = b
    for i in range (0,n-1) :
        G = pivot(An,i)
        An = G.dot(An)
        somme = [0]*n
        for j in range (0,n) :
            for k in range(0,n) :
                somme[j] += G[j,k]*bn[k]
        bn = somme
        print(An,bn)
    return An, bn


# Algorithme de descente (matrice triangulaire inférieure)
    
def descente(L,b) :
    n, nn = L.shape
    assert n == nn
    x = [b[0]/L[0,0]]
    for i in range (1,n) :
        somme = 0
        for j in range(0,i) :
            somme += (b[i]-L[i,j]*x[j])/L[i,i]
        x.append(somme)
    return x
    
# ALgorithme de remontée (matrice triangulaire supérieure)
    
def remontee(U,b) :
    n, nn = U.shape
    assert n == nn
    x = [b[n-1]/U[n-1,n-1]]
    for i in range (n-1,0,-1) :
        somme = 0
        for j in range(n-1,i,-1) :
            somme += (b[i]-U[i,j]*x[n-1-j])/U[i,i]
        x.append(somme)
    x.reverse()
    return x
"""
A = np.array([[1,0,0],[2,3,0],[1,2,3]])
C = np.array([[1,2,3],[0,2,3],[0,0,1]])
b = [2,5,4]

print(descente(A,b))
print(remontee(C,b))
"""
# SSOR, GCP (p27)
    
""" Valeurs propres et vecteurs propres """

# Méthode de la puissance itérée

# Méthode de Jacobi

""" Interpolation polynomiale """

# Polynôme de Lagrange

# Méthode de smoindres carrés