import numpy as np
import matplotlib.pyplot as plt

#Représentation graphique des termes d'une suite
#Calcul explicite un = -2n+6
n = 10
N = np.arange(n)
U = -2*N+6
print("Le ",n,"ième terme de la suite (u(n)) vaut: ", U[n-1] )
plt.plot(N,U,'o')
plt.xlabel("k")
plt.ylabel("u(k)")
plt.title("Représentation graphique des n premiers termes de (u(n))")
plt.grid()
plt.show()

#Formule de récurrence
v0 = 3
V = np.zeros(n)
V[0]=v0
for i in range(1,n):
    V[i] = 0.8*V[i-1]+1.7
print("Le ",n,"ième terme de la suite (v(n)) vaut: ", V[n-1] )
plt.plot(N,V,'o')
plt.grid()
plt.xlabel("k")
plt.ylabel("v(k)")
plt.title("Représentation graphique des n premiers termes de (v(n))")
plt.show()

#Manipuler une suite géométrique w0 = 3 et q = 0.5
#Suite décroissante
w0 = 3.0
q = 1./2
W = np.zeros(n)
W[0] = w0
#Somme des n premiers termes de la suite (w(n))
Sn = w0
for i in range(1,n):
    W[i] = W[i-1]*q
    Sn = Sn + W[i]
print("Liste des ", n, "premiers termes de (w(n)): ", W )
print("Somme des ",n," premiers termes de la suite (w(n)) ", Sn)
#Comparaison avec la formule du cours
S_cours = w0*(1-q**n)/(1-q)
print("Valeurs de la somme des ",n, " premiers termes avec la formule ", S_cours)
plt.plot(N,W,'o')
plt.grid()
plt.xlabel("k")
plt.ylabel("w(k)")
plt.title("Représentation graphique des n premiers termes de (w(n))")
plt.show()

#Exemple de suite géométrique non monotone
p0 = 1.
qp = -0.8
P = np.zeros(n)
P[0] = p0
for i in range(1,n):
    P[i] = P[i-1]*qp

plt.plot(N,P,'o')
plt.grid()
plt.xlabel("k")
plt.ylabel("p(k)")
plt.title("Représentation graphique des n premiers termes de (p(n))")
plt.show()

