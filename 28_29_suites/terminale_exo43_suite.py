#Exercice de terminale spécialité
#Mathématiques Terminale spécialité chap. 2 exo 43 p64


#Question 1: déterminer nb de jours pour colorier le carré à 90%

n = 0
u = 1
while u>0.1:
    n = n+1
    u = u - 0.5*u
print("Carré colorié à 90% au bout de", n, " jours")


#Question 2: fonction Python prenant en argument un réel a et qui renvoie le nb n de jours pour que le carré soit colorié à plus de a%

def jours(a):
    n = 0
    u = 1
    while u>(1-a):
        n = n+1
        u = u - 0.5*u
    return n

print("Carré colorié à 95% au bout de", jours(0.95), " jours")
print("Carré colorié à 99% au bout de", jours(0.99), " jours")
print("Carré colorié à 99.9% au bout de", jours(0.999), " jours")