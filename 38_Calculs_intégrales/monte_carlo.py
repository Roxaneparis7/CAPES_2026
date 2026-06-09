#Calcul approché d'intégrale avec la méthode de Monte Carlo
#Barbazo exo 69 page 264

from random import random, uniform
from math import exp

import matplotlib.pyplot as plt

#Calcul approché de l'intégrale de x->x² sur [0;1]
def Monte_Carlo(n):
    u=0
    for i in range(n):
        x=random()
        y=random()
        if y<=x**2:
            u=u+1
            plt.plot(x,y,'r.')
    #plt.title("Intégrale approchée par Monte-Carlo avec n=",n)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    return u/n

#Généralisation pour l'utiliser avec d'autres fonctions f
def f(x):
    return exp(x**2/2)

def Monte_Carlo2(f,n):
    u=0
    L = f(1)
    for i in range(n):
        x=random()
        y=uniform(0,L)
        if y<=f(x):
            u=u+1
            plt.plot(x,y,'r.')
    #plt.title("Intégrale approchée par Monte-Carlo avec n=",n)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    return L*u/n

