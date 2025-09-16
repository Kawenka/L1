from random import randint

dividende = randint(100, 999)
diviseur = randint(2, 9)

if (dividende % diviseur == 0):
    est_divisible = True
else:
    est_divisible = False

answer = "a"
while ((answer != "o") and (answer != "n")):
    print("Le nombre ", dividende, " est divisible par" , diviseur, " ?")
    answer = input("[o/n]")
if ((answer == "o" and est_divisible) or (answer == "n" and est_divisible == False)):
    print("Bravo !")
else:
    print("Perdu !")
    
