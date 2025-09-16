from random import randint

choices = ["Pierre", "Feuille", "Ciseaux"]
answer = "Rien"  # input("Pierre, feuille, ou ciseaux ? Ou Stop ? ")
stop = 0
player_score = 0
robot_score = 0
while (stop == 0):
        answer = input("Pierre, feuille, ou ciseaux ? Ou Stop ? ")
        while ((answer != "Pierre") and (answer != "Feuille") and (answer != "Ciseaux") and (answer != "Stop")):
            answer = input("Pierre, feuille, ou ciseaux ? Ou Stop ?")
        robot = choices[randint(0,2)]
        if (answer == "Stop"):
            stop = 1
        if (answer == robot):
            print("Egalité !")
        elif ((answer == "Pierre" and robot == "Ciseaux") or (answer == "Feuille" and robot == "Pierre") or (answer == "Ciseaux" and robot == "Feuille")):
            print("Gagné !")
            player_score += 1
        else:
            print("Perdu !")
            robot_score += 1
print("Score robot :", robot_score, "\nScore joueur :", player_score)
if (player_score == robot_score):
    print("Egalité")
elif (player_score > robot_score):
    print("Vous avez gagné !")
else:
    print("Vous avez perdu !")