#### debut de partie a modifier ####

t = int(input("Veuillez entrer la taille de l'écran: ")) # taille
n = int(input("Veuillez entrer le nombre de figures: ")) #nombre de forme
dr = False # boolean de dessin
p = 0.05 # vitesse

c0 = "pink" # couleur du text
c1 = "blue" # coueur des carrés
c2 = "red" # couleur des ronds
c3 = "" # couleur de l'intérieur des carrés
c4 = "" # couleur de l'intérieur des ronds

#### fin de partie a modifier ####




### NE PAS MODIFIER CE QUI SUIT

from fltk import *
from random import randrange
from time import sleep


def test_couleurs(c):
	if not c in {"", "black", "blue", "red", "green", "yellow", "pink", "purple", "orange"}:
		print(c + " n'est pas une couleur.") 
		quit()


def rectangle_aleatoire(x,y,temps):
	rectangle(x, y, x+temps, y+temps, c1, c3)


def cercle_aleatoire(x,y,temps):
	cercle(x, y, temps/2, c2, c4)


def ready():
    texte(t/2,t/2,"Tapez sur une touche !",c0,"center")
    attend_ev()
    efface_tout()


if __name__ == '__main__':

	test_couleurs(c0)
	test_couleurs(c1)
	test_couleurs(c2)
	test_couleurs(c3)
	test_couleurs(c4)

	cree_fenetre(t, t)
	ready()

	temps=1

	while temps != n:
		# geler le programme pendant p secondes
		sleep(p)

		# attente d'un événement
		ev = donne_ev()
		typeEv = type_ev(ev)
		if typeEv == "ClicGauche":
			dr = not dr
		elif typeEv == "Quitte":
			break

		# tirage aléatoire de deux entiers entre 0 et t-1
		x, y = randrange(0, t), randrange(0, t)
		if dr :
			rectangle_aleatoire(x, y, temps)
		else: 
			cercle_aleatoire(x, y, temps)
		temps = temps + 1

		mise_a_jour()

	attend_ev()
	ferme_fenetre()
