#------------------------------------------------------------------------------
# Fonctions permettant de tracer des barres composées de "gros" pixels.
#												+---+
# Chaque gros pixel est une "cellule" carrée :	|   |
#												+---+
#------------------------------------------------------------------------------

def horizontal(nb_cell) :
    """Trace une ligne de démarcation horizontale correspondant à la dimension de nb_cell cellules.
    nb_cell doit être un entier strictement positif."""
    trace = "+---+"
    i = 1
    while i < nb_cell :
        trace += "---+"
        i += 1
    print(trace)
    
def vertical(nb_cell) :
    """Trace les lignes de démarcation verticale correspondant à la dimension de nb_cell cellules.
    nb_cell doit être un entier strictement positif."""
    trace = "|   |"
    i = 1
    while i < nb_cell :
        trace += "   |"
        i += 1
    print(trace)


#------------------------------------------------------------------------------
# Série d'appels donnée en exemple
#------------------------------------------------------------------------------

# horizontal(3)
# vertical(3)
# horizontal(3)
# vertical(1)
# horizontal(1)
# vertical(1)
# horizontal(1)

#=================================================
# question 2 : A compléter -----------------------

# horizontal(1)
# vertical(1)
# horizontal(2)
# vertical(2)
# horizontal(3)
# vertical(3)
# horizontal(3)
# vertical(2)
# horizontal(2)
# vertical(1)
# horizontal(1)

#=================================================
# Question 3 -------------------------------------
def grille(l,h) :
    """permet de tracer une grille de largeur l et de hauteur h"""
    i = 0
    while (i < h):
        horizontal(l)
        vertical(h)
        i += 1
    horizontal(l)
    pass

def triangle(hauteur):
    i = 1
    total = 0
    while (i <= hauteur):
        horizontal(i)
        vertical(i)
        total += i
        i += 1
    horizontal(i - 1)
        
    return total

print(str(triangle(5)))

    