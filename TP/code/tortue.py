from math import *

#### debut de partie a modifier ####

nbLignes = int(input("Entrer le nombre de lignes: "))
rayon = 200
lgLigne = 2 * rayon * sin(pi / nbLignes)
angle = 360 / nbLignes
xInit = lgLigne / 2 * -1
yInit = -rayon

#### fin de partie a modifier ####







### Ne pas modifier ce qui suit ###

from turtle import *

setup(600, 600)
reset()
up()
goto(xInit, yInit)
down()
a=0
while a<nbLignes:
  a+=1
  forward(lgLigne)
  left(angle)
 
exitonclick()
