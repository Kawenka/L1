from fltk import *

cree_fenetre(600, 600)
n = int(input("Taille du damier: "))
size = 600 / n

for i in range(n):
    for j in range(n):
        x1 = j * size
        y1 = i * size
        x2 = (j + 1) * size
        y2 = (i + 1) * size

        if (i + j) % 2 == 0:
            couleur = "black"
        else:
            couleur = "white"
        
        rectangle(x1, y1, x2, y2, remplissage=couleur)

attend_fermeture()