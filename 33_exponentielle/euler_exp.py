#Calul approché de exp(x) avec la méthode d'Euler
#1ere spécialité Barbazo p 186

from math import exp
from pylab import *

#Objectif calculer exp(a) où a est un réel positif
# h est le pas de discrétisation de la méthode
def Exp(a,h):
    x=0
    y=1
    while x<a:
        x = x+h
        y = y*(1+h)
    return y


val_h = [0.1,0.001,0.0001,0.00001]
E_1 = []
E_2 = []
E_3 = []
e = exp(1)
e2 = exp(2)
e3 = exp(3)
for h in val_h:
    err_1 = abs(Exp(1,h)-e)/e
    err_2 = abs(Exp(2,h)-e2)/e2
    err_3 = abs(Exp(3,h)-e3)/e3
    E_1.append(err_1)
    E_2.append(err_2)
    E_3.append(err_3)

plot(val_h,E_1,'+',label="erreur e")
plot(val_h,E_2,'*',label="erreur e**2")
plot(val_h,E_3,'o',label="erreur e**3")
legend(loc="best")
yscale("log")
xscale("log")
show()

E = [e,e2,e3]
Euler = [Exp(1,1e-4),Exp(2,1e-4),Exp(3,1e-4)]
plot(list(range(1,4)),E,'-',label="exp(x)")
plot(list(range(1,4)),Euler,'+',label="Euler")
legend(loc="best")
show()


