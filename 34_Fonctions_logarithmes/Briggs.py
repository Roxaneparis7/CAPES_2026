#Méthode historique pour calcul du logarithme décimal
#Algorithme de Briggs
#Barbazo Mathématiques Terminale spécialité page 190

from math import sqrt,log

#On calcule log_10(X) à 10**(-6) près

def Briggs(X):
    A=1
    B=10
    lA = 0
    lB = 1.
    while B-X>10**(-6):
        if X<sqrt(A*B):
            B = sqrt(A*B)
            lB = (lA+lB)/2.
        else:
            A = sqrt(A*B)
            lA = (lA+lB)/2.
    return (lA+lB)/2.

log2 = Briggs(2)
log_ex = log(2,10)
print("Valeur approchée de log10(2), ", log2)
print("Valeur exacte de log10(2) ",log_ex)