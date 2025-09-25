
from turtle import *
from random import randint

######################################################################
###### Zone de définition des fonctions utiles #######################
######################################################################

def triangle_equilateral(n):
    x = xcor()
    y = ycor()
    left(30)
    forward(n)
    left(120)
    forward(n)
    goto(x, y)

def maison(cote):
    """ Doit dessiner une maison simple (carré + triangle par dessus)

    :param cote: longueur des côtés du carré et du triangle
    """
    # Compléter la fonction ici
    down()
    forward(cote)
    left(90)
    forward(cote)
    left(90)
    forward(cote)
    triangle_equilateral(cote)
    up()
    

def rue(nb_maisons):
    """ Doit dessiner une rue de maisons aléatoires, espacées aléatoirement dans la fenêtre

    :param nb_maisons: le nombre de maisons à dessiner à la suite
    """
    # Compléter la fonction ici
    up()
    size = 600 / (nb_maisons + 2)
    right(90)
    goto(-250, -100)
    y = ycor()
    x = xcor()
    for i in range (nb_maisons):
        maison(size)
        left(30)
        x += size + 2
        goto(x ,y + (randint(-20, 20)))
        

def etoile(diametre, rotation):     # étoile à 5 branches
    """ Doit dessiner une étoile à 5 branches de diamètre donné, en partant avec un angle donné

    :param diamètre: diamètre de l'étoile (longueur des segments)
    :param rotation: angle de départ du crayon
    """
    # Compléter la fonction ici
    down()
    setheading(rotation)
    for i in range (5):
        forward(diametre)
        left(180 - 36)
    up()
    

def ciel_etoile(nb_etoiles):
    """ Doit produire un ciel étoilé au dessus de la maison en utilisant la fonction etoile

    :param nb_etoiles: nombre d'étoiles à dessiner
    """
    # Compléter la fonction ici
    up()
    goto(-290, 0)
    y = ycor()
    x = xcor()
    for i in range (nb_etoiles):
        etoile(randint(5, 20), randint(0, 360))
        goto(randint(-270, 300), randint(0, 270))
    
def draw_tree(size):
    down()
    if size < 10:
        forward(size)
        backward(size)
        return
    forward(size / 3)
    left(30)
    draw_tree(size * 2 / 3)
    right(60)
    draw_tree(size * 2 / 3)
    left(30)
    backward(size / 3)
    up()

############################################################################
##### Zone du programme qui dessine votre nuit étoilée #######
############################################################################

if __name__ == '__main__':
    nombre_maisons = int(input("Combien de maisons voulez-vous ?  (<15)  "))          	# <- ne pas modifier !!!
    nombre_etoiles = int(input("Combien d'étoiles voulez-vous ?  "))					# <- ne pas modifier !!!
    tree_size = int(input("Taille de l'arbre: "))

    setup(600, 600)
    speed(1000)
    rue(nombre_maisons)
    color("yellow")
    ciel_etoile(nombre_etoiles)
    up()
    goto(0, -290)
    down()
    setheading(90)
    color("green")
    draw_tree(tree_size)
    exitonclick()
