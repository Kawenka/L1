n = int(input("Veuillez entrer un nombre "))
if ((n % 2 == 0) and (n % 3 == 0)):
    print("divisible par 2 et 3")
elif (n % 2 == 0):
    print("divisible par 2")
elif (n % 3 == 0):
    print("divisible par 3")