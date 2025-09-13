"""
Tracé de polygones réguliers.
"""
import turtle
from math import sin, tan, pi

# Paramètres initiaux
tailleFenetre = 600
nbLignes = int(input('Nombre de côtés : '))
anglePoly = 360 / nbLignes

# Paramètres dérivés
tailleMarge = .01 * tailleFenetre
lgLigne = tailleFenetre * sin(pi / nbLignes) - 2 * tailleMarge
xInit = -lgLigne / 2
yInit = (-lgLigne / 2) / tan(pi / nbLignes)

# Initialisation
turtle.setup(tailleFenetre, tailleFenetre)
turtle.reset()
turtle.up()
turtle.goto(xInit, yInit)
turtle.down()

# Tracé d'un polygone
b = 0
while b < nbLignes:
    b = b + 1
    # Tracer un côté du polygone
    turtle.forward(lgLigne)
    # Tourner à gauche de l'angle indiqué
    turtle.left(anglePoly)

turtle.ht()
turtle.exitonclick()
