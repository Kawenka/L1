from turtle import *


def rectangle(longueur, largeur):
    down()
    forward(longueur)
    left(90)
    forward(largeur)
    left(90)
    forward(longueur)
    left(90)
    forward(largeur)
    left(90)
    up()


def carre(cote):
    rectangle(cote, cote)


def triangle(cote1, angle, cote2):
    x = xcor()
    y = ycor()
    down()
    forward(cote1)
    left(angle)
    forward(cote2)
    goto(x, y)
    setheading(0)
    up()


def triangle_equilateral(cote):
    triangle(cote, 120, cote)


def maison(largeur):
    x = xcor()
    y = ycor()
    hauteur = int(largeur/1.25)
    rectangle(largeur, hauteur)
    goto(x, y+hauteur)
    triangle_equilateral(largeur)
    goto(x + largeur*1//5, y + hauteur//2)
    carre(largeur//5)
    goto(x + largeur*3//5, y + hauteur//2)
    carre(largeur//5)


maison(100)
exitonclick()