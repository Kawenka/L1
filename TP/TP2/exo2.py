from random import randint

mystere = randint(0,1)
nombre = int(input("Veuillez entrer un nombre "))
if (mystere == nombre):
    message = "la foce est avec toi !"
else:
    message = "Essaie encore jeune padawan."
print(message)