#Méthode d'Euler pour résoudre une équation différentielle'
#Barbazo exo 70 page 233
# y'+y²=4 avec y(0)=0 et I=[0;2]


import matplotlib.pyplot as plt

h=0.1
xmin=0
xmax=2
n=int((xmax-xmin)/h)

#Initialisation
X = [xmin]
Y = [0]
x=xmin
y=0

#Calcul de la solution approchée
for i in range(1,n):
    x=x+h
    X.append(x)
    y = y-h*(y**2-4)
    Y.append(y)

#Courbe représentative
plt.plot(X,Y,'-o')
plt.ylabel("y(x)")
plt.xlabel("x")
plt.title("Représentation de la solution approchée de y'+y²=4 par la méthode d'Euler h=0.1")
plt.grid()
plt.show()


