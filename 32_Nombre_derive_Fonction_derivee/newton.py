#TP sur la méthode de Newton (Déclic 1ere spé page 95)
# Objectif: Résolution approchée de f(x)=0

#Fonction f
def f(x):
    return 0.2*x**3+0.5*x**2-x-1

#Dérivée de f
def df(x):
   return 0.6*x**2+x-1

#Méthode de Newton
# N: nb d'itérations réalisées
# x0: point de départ de la méthode de Newton
def Newton(N,x0):
    liste=[x0]
    for n in range(0,N):
        a=liste[-1]
        b=a-f(a)/df(a)
        liste.append(b)
    return liste


#Pour aller plus loin prendre f(x)=x**2-2 et df(x)=2*x
#Puis f(x)=x**3-5 et df(x)=3*x**2