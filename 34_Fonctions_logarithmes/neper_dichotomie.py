#Méthode de calcul du logarithme népérien par dichotomie
#Barbazo Mathématiques Terminale spécialité exo 60 page 198

from math import *

def equation(k):
    a=0
    b=100
    while b-a>0.01:
        if exp((a+b)/2)>k:
            b = (a+b)/2
        else:
            a = (a+b)/2
    return a,b


print("La valeur de ln(10) est comprise entre ", equation(10)[0], " et ", equation(10)[1])
print("Valeur exacte de ln(10) ", log(10))