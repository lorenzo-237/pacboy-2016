## conversion base 10 en base 16 ##

N = int(input(" Entrer un nombre décimal : "))
N2 = ""
q = N

while q != 0:
    r = q % 16  # % = le reste
    if r == 10:
        N2 = "A" + N2
    elif r == 11:
        N2 = "B" + N2
    elif r == 12:
        N2 = "C" + N2
    elif r == 13:
        N2 = "D" + N2
    elif r == 14:
        N2 = "E" + N2
    elif r == 15:
        N2 = "F" + N2
    else:
        N2 = str(r) + N2
        
    q = q // 16  # // = ne prendre que la partie entière de la division

print(N, " en base 10, s'écrit", N2, "en base 16")
