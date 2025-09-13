"""
Tracé de rosaces par rotation de polygones.
"""
from turtle import *

# Paramètres
nb_cotes = 4
lg_cote = 100
angle_poly = 360 / nb_cotes
nb_petales = 9
angle_rosace = 360 / nb_petales
# Tracé de la rosace
compteur_petales = 0
while compteur_petales < nb_petales:
    compteur_petales = compteur_petales + 1
    # Tracé d'un pétale
    compteur_cotes = 0
    while compteur_cotes < nb_cotes:
        compteur_cotes = compteur_cotes + 1
        forward(lg_cote)
        left(angle_poly)
    left(angle_rosace)

exitonclick()
