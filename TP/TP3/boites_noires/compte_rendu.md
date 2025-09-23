Liste des tests effectués :

Programme 1:
print(prog1.run(2147483647000000)) : Renvoie 2147483647000000
print(prog1.run(-100)) : Renvoie 100
print(prog1.run(-21474836399999999999991)) : Renvoie 21474836399999999999991

Hypothèse avant tests supplémentaires : Le programme renvoie la valeur mise en paramètre
Hypothèse après tests supplémentaires : Le programme renvoie la valeur absolue de la valeur mise en paramètre
Conclusion finale : Le programme renvoie la valeur absolue de la valeur mise en paramètre

Programme 2:

print(prog2.run(0, 10, 100, 1, 11, 101, -1, -2, -100, -101)) : Renvoie la liste des nombres pairs mis en paramètre

Hypothèse avant tests supplémentaires : Le programme prend en paremetre une liste d'entiers et renvoie les valeurs paires.
Hypothèse après tests supplémentaires : C'est correct, et ça ne fonctionne pas si on met des chaînes de caractères dans la liste et les floats
Conclusion finale : Le programme prend en paramètre une liste de nombres entiers et renvoie la liste uniquement avec les nombres pairs

Programme 3:

Hypothèse avant tests supplémentaires : Le programme prend en paramètre une chaîne de caractères et la renvoie en mettant tous les mots séparés, par des espaces, à l'envers.
Hypothèse après tests supplémentaires : Hypothèse correct, le programme conserve également le nombre d'espaces
Conclusion finale : Le programme prend en paramètre une chaîne de caractères et la renvoie en mettant les mots, séparés par un ou plusieurs espaces, à l'envers.

Programme 4:

Hypothèse avant tests supplémentaires : Le programme prend une chaîne de caracères et un nombre en paramètre et renvoie la chaîne de caractères en décalant dans l'alphabet, chaque lettre composant la chaîne n fois.
Hypothèse après tests supplémentaires : Hypothèse correct, le programme fonctionne aussi avec les nombres négatifs
Conclusion finale : Le programme prend une chaîne de caracères et un nombre en paramètre et renvoie la chaîne de caractères en décalant dans l'alphabet, chaque lettre composant la chaîne n fois.

Programme 5:

Hypothèse avant tests supplémentaires : Le programme semble effectuer des divisions par 2 sur le nombre en parametres puis renvoie le nombre en parametre + le nombre de calcul
Hypothèse après tests supplémentaires : Le programme semble simplement renvoyer la valeur du nombre en parametre fois 2
Conclusion finale : Le programme renvoie le nombre en paramètre fois 2