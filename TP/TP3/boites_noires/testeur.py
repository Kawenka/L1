import prog1
import prog2
import prog3
import prog4
import prog5

print("=== Test prog1 ===")
print(prog1.run(7))
print(prog1.run(12))
print(prog1.run(2147483647000000)) # Tests avec d'autres valeurs aléatoires 
print(prog1.run(-100))
print(prog1.run(-21474836399999999999991))

# 1) Le programme renvoie la valeur mise en paramètre
# 2) Le prog1 renvoie la valeur absolue de la valeur mise en parametre.


print("\n=== Test prog2 ===")
print(prog2.run(1, 2, 3, 4, 5,))
print(prog2.run(0, 10, 100, 1, 11, 101, -1, -2, -100, -101)) # Test avec plein de valeurs différentes, negatifs et positifs
# print(prog2.run(abc, test)
print(prog2.run(1.1, 3, 2.2, 2.1, 3/2))

# 1) Le programme prend en paremetre une liste d'entiers et renvoie les valeurs paires.
# 2) Ca m'a l'air correct

print("\n=== Test prog3 ===")
print(prog3.run("Bonjour tout le monde"))
# print(prog3.run(3))
print(prog3.run("Bonjour     tout    le    monde")) # Test avec plusieurs espaces à la suite


# 1) Le programme prend une chaine de caracteres en parametres et met tous les mots séparés par des espaces à l'envers, on conservant l'ordre des mots
# 2) Conserve aussi le nombre d'espaces

print("\n=== Test prog4 ===")
print(prog4.run("abc", 2))
print(prog4.run("a", 0))
print(prog4.run("a", -2)) # tests avec nombre negatifs

# 1) Ce programme prend des lettres en parametres ainsi qu'un nombre, puis renvoie la chaine de caracteres décalé n fois.
# 2) Le programme fonctionne aussi avec les nombres négatifs

print("\n=== Test prog5 ===")
print(prog5.run(10))
print(prog5.run(1))
print(prog5.run(-1)) # Tests de nombres negatifs
print(prog5.run(-3))


# 1) Le programme semble effectuer des divisions par 2 sur le nombre en parametres puis renvoie le nombre en parametre + le nombre de calcul
# 2) Le programme semble simplement renvoyer la valeur du nombre en parametre fois 2
