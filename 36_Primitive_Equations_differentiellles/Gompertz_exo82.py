#Modèle de Gompertz: modélisation population en voie d'extinction
#Barbazo exo 82 p 235

from math import exp

s=0.01
t=0
while exp(4.-4*exp(t/50))>s:
    t=t+1

print("A l'année ", t, " la population existante représente ", s*100, "% de la population initiale")