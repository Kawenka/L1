"""
Tracé de polygones réguliers.
"""
# On importe les fonctions du module turtle
from turtle import *
# Paramètres
nbCotes=4
lgCote=250
angle=90
# Tracé
compteur = 0
while compteur < nbCotes:
    # Tracer un côté : fonction du module turtle
    forward(lgCote)
    # Tourner à gauche : fonction du module turtle
    left(angle)
    # On incrémente le compteur
    compteur = compteur + 1

exitonclick()
