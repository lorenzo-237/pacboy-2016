## Conversion base 2 à la base 10 ##

def bin_to_dec(N2):
    N10 = 0
    L = len(N2) # donne la taille de la chaîne, ici N2
    
    for i in N2: 
        N10 = N10 + int(i)*2**(L-1)
        L = L-1
    return(N10)

## Conversion base 16 vers base 10 ##

def B16_B10(N16):
        N10 = 0
        L = len(N16)

        for i in N16:
                if i == "A": a=10
                elif i == "B": a=11
                elif i == "C": a=12
                elif i == "D": a=13
                elif i == "E": a=14
                elif i == "F": a=15
                else: a = int(i)
                N10 = N10 + a*16**(L-1)
                L = L-1
        return(N10)

## Programme principal ##

b = int(input("Choisissez votre base : "))
n = input("Votre nombre : ")
if b==2:
        print(bin_to_dec(n))
if b==16:
        print(B2_B16(n))


