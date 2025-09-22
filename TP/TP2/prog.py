from random import *

pos_l = 0
pos_t = 0
t_win = 0
l_win = 0
winner = "Tortue"
i = 0
while i < 1000:
    pos_l = 0
    pos_t = 0
    while pos_t < 6 and pos_l < 6:
        lancer = randint(1, 6)
        if lancer == 6:
            pos_l = 6
            winner = "Lievre"
            l_win += 1
        else:
            pos_t += lancer % 2 + 1
            if pos_t >= 6:
                winner = "Tortue"
                t_win += 1
    i += 1
    print(winner)
print("Nb victoires tortue: " + str(t_win))
print("Nb victoires lievres: " + str(l_win))