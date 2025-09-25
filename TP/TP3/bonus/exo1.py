from turtle import *

def star(n):
    down()
    for i in range (5):
        forward(n)
        left(180 - 36)
    up()
    
def triangle_equilateral(n):
    x = xcor()
    y = ycor()
    left(30)
    forward(n)
    left(120)
    forward(n)
    goto(x, y)

def house(n):
    down()
    forward(n)
    left(90)
    forward(n)
    left(90)
    forward(n)
    triangle_equilateral(n)
    up()
    

setup(600, 600)
reset()
up()
goto(-200, 0)
star(int(input("Taille de l'étoile: ")))
goto(100, 100)
right(90)
house(int(input("Taille de la maison: ")))
exitonclick()