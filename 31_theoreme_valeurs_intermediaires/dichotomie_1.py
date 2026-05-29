#Mise en oeuvre de la méthode de dichotomie pour résoudre
# f(x)=0 avec f(x)=exp(x)-2 sur l'intervalle [0,5]

from math import exp

def f(x):
    return exp(x)-2

a = 0.
b = 5.

precision = 1e-3

while b-a>precision:
    c = (a+b)/2
    if f(c)<=0:
        a=c
    else:
        b=c

print("Le zéro de f est compris entre: ", a, " et ", b)
print("f(c) =", f(c))

