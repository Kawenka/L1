from fltk import *

# création de la fenêtre graphique
cree_fenetre(600,600)



# sélection des coins et dessin du premier rectangle
x1, y1 = attend_clic_gauche()
x2, y2 = attend_clic_gauche()
rectangle(x1, y1, x2, y2, couleur='blue', epaisseur=3)

x_bleu_haut_gauche = x1
y_bleu_haut_gauche = y1
x_bleu_bas_drotie = x2
y_bleu_bas_droite = y2

# sélection des coins et dessin du second rectangle
x3, y3 = attend_clic_gauche()
x4, y4 = attend_clic_gauche()
rectangle(x3, y3, x4, y4, couleur='red', epaisseur=3)

x_rouge_haut_gauche = x3
y_route_haut_gauche = y3
x_rouge_bas_droite = x4
y_rouge_bas_droite = y4


# partie à compléter
if x1 > x2:
    x_bleu_haut_gauche, x_bleu_bas_drotie = x2, x1
if y1 > y2:
    y_bleu_haut_gauche, y_bleu_bas_droite = y2, y1
if x3 > x4:
    x_rouge_haut_gauche, x_rouge_bas_droite = x4, x3
if y3 > y4:
    y_route_haut_gauche, y_rouge_bas_droite = y4, y3

rectangles_disjoints = ((x_bleu_bas_drotie < x_rouge_haut_gauche) or 
    (x_bleu_haut_gauche > x_rouge_bas_droite) or
    (y_bleu_bas_droite < y_route_haut_gauche) or
    (y_bleu_haut_gauche > y_rouge_bas_droite)
)

red_in_blue = False
if (x3 < x1 and x4 < x2 and y3 < y1 and y4 < y2):
    red_in_blue = True

if rectangles_disjoints:
    message = "Les rectangles sont disjoints"
elif red_in_blue:
    message = "Le carré rouge est entièrement dans le carré bleu"
else:
    message = "Les rectangles se chevauchent"

texte(300, 300, message, taille=24, ancrage="center")

# fermeture de la fenêtre
attend_fermeture()