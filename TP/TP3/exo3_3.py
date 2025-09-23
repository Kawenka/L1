height = int(input("Taille du triangle : "))
i = 0
k = 1
while (i < height):
    j = height - i
    print(" " * j + "*" * k)
    k += 2
    i += 1