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
    """ Dessine une rue de maisons aléatoires, espacées aléatoirement dans la fenêtre

    :param nb_maisons: le nombre de maisons à dessiner à la suite
    """
    up()
    # Définir les limites horizontales de l'écran
    espace_total = 550  # De -250 à environ +300
    
    # Calculer l'espace entre chaque maison
    if nb_maisons > 1:
        espace_entre_maisons = espace_total / (nb_maisons - 1)
    else:
        espace_entre_maisons = 0
    
    # Calculer une taille maximale pour les maisons
    taille_max = min(espace_entre_maisons * 0.7, 600 / (nb_maisons + 2))
    size = taille_max
    
    # Positionnement initial
    right(90)
    start_x = -250
    goto(start_x, -100)
    y = ycor()
    
    for i in range(nb_maisons):
        # Positionner à l'emplacement actuel
        x = start_x + (i * espace_entre_maisons)
        goto(x, y + (randint(-20, 20)))
        
        # Dessiner la maison
        maison(size)
        left(30)
        

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
        pensize(5)
        color("darkgreen")
        forward(size)
        backward(size)
        return
    
    # Tronc (branches principales)
    pensize(size/15)  # Épaisseur proportionnelle à la taille
    color("#8B4513")
    forward(size / 3)
    
    # Réduire l'épaisseur pour les branches secondaires
    pensize(size/20)
    
    left(30)
    draw_tree(size * 2 / 3)
    right(60)
    draw_tree(size * 2 / 3)
    left(30)
    backward(size / 3)
    up()

def dessiner_paysage(style="arrondi"):
    """
    Dessine le paysage avec un fond bleu nuit et un sol vert
    
    :param style: "droit" pour un sol plat ou "arrondi" pour un sol légèrement courbé
    """
    # Fond bleu nuit
    bgcolor("#000033")  # Bleu très foncé
    
    # Dessiner le sol en vert foncé
    up()
    pensize(1)
    goto(-300, -200)  # Position de départ à gauche de l'écran
    down()
    
    # Colline en vert foncé
    color("darkgreen")
    fillcolor("#003300")  # Vert très foncé
    begin_fill()
    
    if style == "droit":
        # Sol droit
        goto(300, -200)  # Ligne droite jusqu'à l'autre côté
    else:
        # Sol légèrement arrondi (courbe simple)
        for x in range(-300, 310, 10):
            # Créer une courbe douce avec une fonction parabolique simple
            y = -200 + 30 * ((x / 300) ** 2 - 1)  # Forme de U inversé
            goto(x, y)
    
    # Compléter la forme pour le remplissage
    goto(300, -300)  # Coin bas droit
    goto(-300, -300)  # Coin bas gauche
    goto(-300, -200)  # Retour au point de départ
    
    end_fill()

############################################################################
##### Zone du programme qui dessine votre nuit étoilée #######
############################################################################

if __name__ == '__main__':

    nombre_maisons = int(input("Combien de maisons voulez-vous ?  (<15)  "))          	# <- ne pas modifier !!!
    nombre_etoiles = int(input("Combien d'étoiles voulez-vous ?  "))					# <- ne pas modifier !!!
    tree_size = int(input("Taille de l'arbre: "))

    setup(600, 600)
    speed(0)
    rue(nombre_maisons)
    color("yellow")
    ciel_etoile(nombre_etoiles)
    up()
    goto(0, -290)
    down()
    setheading(90)
    color("green")
    draw_tree(tree_size)
    dessiner_paysage()
    exitonclick()
