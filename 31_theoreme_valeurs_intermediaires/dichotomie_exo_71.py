#Exercice de synthèse avec utilisation du théorème des valeurs intermédiaires, exo 71

from math import e

def f(x):
    return e**(-3*x)+3*x-5

#Encadrement de l'antécédent positif de zéro par f
def dicho(precision):
    a = 0.
    b = 5.
    while (b-a)>precision:
        c = (b+a)/2
        if f(c)<0:
            a=c
        else:
            b=c
    return a,b



def testalpha(x):
    if x<=0:
        a = True
    else:
        y = e**(-3*x)+3*x-5
        a = (y<0)
    return a

