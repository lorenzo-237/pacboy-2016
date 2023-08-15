## Conversion d'un entier de la base 10 vers la base 2 ##

N = int(input("Entrez un entier : "))
N2 = ""
q = N

print("")
while q != 0:
    N2 = str(q % 2) + N2
    q = q // 2

print(N, "s'écrit ",N2, "en base 2")
print("")
print("Terminé")
    
