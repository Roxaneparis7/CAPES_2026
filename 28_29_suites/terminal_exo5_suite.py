#Exercice sur les suites récurrentes
#Barbazo Terminale spécialité chap.1 exo 5 p 26

import numpy as np
import matplotlib.pyplot as plt

u0 = -2./3.
n=10
def f(x):
    return (3*x+4)/(x+3)

N = np.arange(n)
U = np.zeros(n)
#Initialisation
U[0]=u0
#Calcul des 4 termes suivants grâce à la relation de récurrence
for i in range(1,n):
    U[i]=f(U[i-1])
#Affichage des termes de la suite Un
print("Les 5 premiers termes de la suite Un: ", U)
#Représentation graphique
plt.plot(N,U,'o')
plt.title("Représentation graphique des premiers termes de la suite Un")
plt.xlabel("n")
plt.ylabel("u(n)")
plt.grid()
plt.show()
