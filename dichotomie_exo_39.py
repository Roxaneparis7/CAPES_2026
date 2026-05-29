#Exercice d'application: exercice 39, théorème des valeurs intermédiaires

from math import e

def alpha(precision):
    a = 0
    b = 1
    while (b-a)>precision:
        c = (b+a)/2
        f = c**2*e**c
        if f<= 1.0:
            a=c
        else:
            b = c
    return a,b

def f(x):
    return x**2*e**x
