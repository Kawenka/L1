print("Coucou")
answer = input("Stop ou encore ? ")
while (answer):
    if (answer == "encore"):
        print("Coucou !")
    else:
        print("Au revoir !")
        break
    answer = input("Stop ou encore ? ")