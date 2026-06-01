#Approximation du nombre e par encadrement par des suites (u(n)) et (v(n))
# Déclic 1ere spécialité page 203

from pylab import *
from math  import exp

#Suite minorante de e
def suite_u(n):
    L = []
    k=2
    while k<=n:
        u=(1+1/k)**k
        L.append(u)
        k =k+1
    return L

#Suite majorante de e
def suite_v(n):
    L = []
    k=2
    while k<=n:
        v=(1+1/(k-1))**k
        L.append(v)
        k=k+1
    return L

n=50

#Valeur de e
e = exp(1)
Y = [e]*(n-1)


plot(list(range(2,n+1)),suite_u(n),'+',label="u_n")
plot(list(range(2,n+1)),suite_v(n),'o',label="v_n")
plot(list(range(2,n+1)),Y,'-',label="e")
legend(loc="best")
grid()
show()
