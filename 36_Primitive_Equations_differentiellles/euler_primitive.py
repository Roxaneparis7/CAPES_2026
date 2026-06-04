#Utilisation de la méthode d'Euler pour résoudre
# une équation différentielle y'=f
# où f est une fonction dont on ne sait pas calculer de primitive
#Barbazo exo 72 p234 f(x)=exp(-x²) et F(0)=0

from math import exp

def f(x):
    return exp(-x**2)

n=10**4

#Fonction renvoyant une valeur approchée de F(1)
def Euler(n):
    x=0
    F=0
    h=1./n
    for i in range(0,n):
        F = F+h*f(x)
        x=x+h
    print(x)
    return F

print("Pour n= ",n  ," valeur approchée de F(1)=", Euler(n))

