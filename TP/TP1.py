#TP AP1 09/09/2025

# 1. loulou = ririloulou
#    fifi = riri
#    riri = ririloulouririlouou

# 3.

#riri = "loulou"
#fifi = "riri"
#loulou = fifi + "loulou"
#riri = loulou * 2

#a = 5
#b = "5"
#c = a/5
#d = a//5
#e = b*a

#prenom = input("Veuillez entrer votre prenom: ")
#print("Hello", prenom, "!")


#def terme(n) :
#    u = 2
#    for i in range(n) :
#        u = 2 * u - 5
#    return (u)

#print("n = 5: ", terme(5))
#print("n = 100: ", terme(100))

#def seuil(nb) :
#    v  = 3
#    n = 0
#    while v < nb :
#        n = n + 1
#        v = 2 * v - 1
#    return n

# seuil(10 ** 100) = 332

# ------- exo+ --------

#Exercice 1

#Programme 1 :

#x = 1
#x = y + 1 # y n'est pas initialisé donc ça ne fonctionne pas
#y = 2

# Programme 2 :

#x = 1
#y = 0
#x + y = 1

# Aucune problème

# Programme 3 :

#y = 2
#x = 1
#x = y +- 2 # Mauvaise syntaxe

# Programme 4 :

#y = 2
#x = 1
#x = y +/- 1 # Mauvaise syntaxe

# Programme 5

y = 2
x = 1
x = y + 3

# Aucun problème

# Programme 6

y = 2
x = 1
x = x -+ 1 # Mauvaise syntaxe


# Exercice 2

#n = input("Veuillez entrer un nombre.")
#m = n - 2
#print("Votre nombre vaut ",m,"+ 2")

# La fonction input renvoie une chaine de caractere et non un int.
# Donc n - 2 ne fonctionne pas
# Correction :

n = int(input("Veuillez entrer un nombre."))
m = n - 2
print("Votre nombre vaut ", m, "+ 2")



