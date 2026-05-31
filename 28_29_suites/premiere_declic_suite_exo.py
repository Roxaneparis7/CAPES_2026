#Exercice de premiere spécialité
#Déclic 1ère spécialité chap.5 n°56 p 157

#Fonction Python rang(M): renvoie le plus petit entier n tq u(n)>= M

def rang(M):
    n=0
    u=3
    while u<M:
        n = n+1
        u = 3*u-2
    return n

#Test avec M=1000
M = 1000
print("On a u(n)>=", M, " pour n>=", rang(1000))
