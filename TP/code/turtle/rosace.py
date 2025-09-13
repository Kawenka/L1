"""
Tracé de rosaces par rotation de polygones.
"""
from turtle import *
from math import sin, pi

# Paramètres initiaux
taille_fenetre = 600
nb_cotes = int(input('Nombre de côtés : '))
nb_poly = int(input('Nombre de polygones : '))

# Paramètres dérivés
angle_rosace = 360 / nb_poly
angle_poly = 360 / nb_cotes
taille_marge = .01 * taille_fenetre
lgLigne = (taille_fenetre/2) * sin(pi / nb_cotes) - taille_marge

# Initialisation
setup(taille_fenetre, taille_fenetre)
reset()  # Vider la fenêtre
                # et place la tortue en (0,0)
speed(10)    # Tortue rapide
color('red', 'yellow')   # Couleurs
begin_fill()  # Colorier

# Tracé de la rosace
compteur_poly = 0
while compteur_poly < nb_poly:
    compteur_poly = compteur_poly + 1
    # Tracé d'un polygone
    compteur_cotes = 0
    while compteur_cotes < nb_cotes:
        compteur_cotes = compteur_cotes + 1
        # Tracer un côté du polygone
        forward(lgLigne)
        # Tourner à gauche de l'angle indiqué
        left(angle_poly)
    left(angle_rosace)

end_fill()
ht()  # Cacher le curseur
exitonclick()
