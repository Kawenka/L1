from math import *

def valeur_approchee(f):
    a, b = f
    return (a / b)

def simplifier(f):
    a, b = f
    diviseur = gcd(a, b)
    a //= diviseur
    b //= diviseur
    return (a, b)

def oppose(f):
    a, b = f
    a *= -1
    b *= -1
    if (a < 0 and b < 0):
        b *= -1
    return simplifier((a, b))

def inverse(f):
    a, b = f
    temp = a
    a = b
    b = temp
    return simplifier((a ,b))

def multiplier(f, g):
    a, b = f
    c, d = g
    return simplifier((a * c, b * d))

def diviser(f, g):
    a, b = g
    inverse_g = (b, a)
    return simplifier(multiplier(f, inverse_g))
    
def addition(f, g):
    a, b = f
    c, d = g
    if (b == d):
        return (a + c, b + d)
    else:
        return ( (a * d) / (c * d) + (b * c) / (d * c))
    
def soustraction(f, g):
    a, b = f
    c, d = g
    if (b == d):
        return (a - c, c - d)
    else:
        return ( simplifier(addition(f, oppose)) )
    # 3/4 et 5/2
    

print("Valeur approchee: " + str(valeur_approchee((3, 4))))
print("Simplifier : " + str(simplifier((20, 10))))
print("Oppose : " + str(oppose([3, 4])))
print("Inverse : " + str(inverse([3, 4])))
print("Multiplier : " + str(multiplier([3, 4], [3, 4])))
print("Diviser : " + str(diviser([3, 4], [3, 4])))
print("Addition : " + str(addition((3, 4), (3, 3))))
print("Soustraction : " + str(soustraction((3, 4), (3, 4))))