#Calcul approché d'intégrale avec la méthode des rectangles
# et méthode du point milieu
#Barbazo pages 254 et 265
#f(x)= x*sqrt(x) calcul de l'intégrale sur [0;1]

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x*sqrt(x)

def rectangles_gauche(n):
    s=0
    for k in range(n):
        s=s+f(k/n)/n
    return s

def rectangles_droite(n):
    s=0
    for k in range(n):
        s=s+f((k+1)/n)/n
    return s

def trapezes(n):
    Ig = rectangles_gauche(n)
    Id = rectangles_droite(n)
    return (Ig+Id)/2.

def milieux(n):
    s=0
    for k in range(n):
        ck=(k/n)+1/(2*n)
        s = s + f(ck)/n
    return s

N = [5,10,50,100,500,1000]
val = 0.4
Ex = []
Rect = []
Mid = []
for k in range(len(N)):
    Rect.append(rectangles_gauche(N[k]))
    Mid.append(milieux(N[k]))
    Ex.append(val)

plt.plot(N,Rect,'r.', label="rectangles")
plt.plot(N,Mid,'b+', label="point milieu")
#plt.plot(N,Ex,'g-')
plt.xscale("log")
plt.legend(loc="best")
plt.grid()
plt.show()


