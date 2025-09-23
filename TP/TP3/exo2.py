from random import randint

n = randint(0, 100)
guess = int(input("Devine le nombre : "))
again = True
while (again == True):
    while (guess != n):
        if (guess > n):
            print("Moins !")
        else:
            print("Plus !")
        guess = int(input("Réessaye :"))
    answer = input("Encore ? o/n")
    if (answer == "n"):
        again = False
print("Bravo !")