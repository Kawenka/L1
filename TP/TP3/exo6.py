def histoire(n: int):
    i = 1
    j = 0
    moutons = n
    moutons_manges = 0
    print(f"Voici la chronologie de cette terrible histoire dans laquelle il était une fois {n} moutons...")
    while i <= n and moutons_manges < n:
        j = 0
        while j < i:
            moutons_manges = moutons_manges + 1
            if (moutons_manges == n):
                print(f"Mouton(s) mangé(s) : {moutons_manges}")
                break
            print(f"Mouton(s) mangé(s) : {moutons_manges}")
            j = j + 1
            
        if j == i:
            print(f"Loup(s) repu(s) : {i}")
        elif j != i:
            print("Un pauvre loup est resté sur sa faim.\nFin de l'histoire !")
            return
        i = i + 1
        
histoire(37)