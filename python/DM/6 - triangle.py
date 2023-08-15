### Vérifier si il s'agit d'un triangle et calcul de l'air ###
"""
AIDE
- 3 points vérifient l'existence d'un triangle si chaque côté est plus court que
la somme des 2 autres. Un triangle ABC existe si il vérifie les inégalités triangulaires
AB <= AC+CB ; BC <= BA + AC ; CA <= CB + BC .
- Si la sommes de 2 côtés est égale au 3 ème , alors le triangle existe mais il est
applati (3 sommets alignés)
"""

def triangle(A,B,C):
    if C < B + A:
        return(print("Il existe un triangle ABC avec ces 3 longueurs."))
    elif C == B + A:
        return(print("Il existe un triangle ABC applati avec ces 3 longueurs."))
    else:
        return(print("Il n'existe pas de triangle avec ces 3 longueurs."))

def aire():
    from math import sqrt
    triangle(A,B,C)
    p = 0.5 * (A + B + C)
    a = sqrt(p*(p-A)*(p-B)*(p-C)) # Formule d'Héron
    return(print("\nL'aire de votre triangle est ", a, "cm²."))

print("Entrez les longeurs de votre triangle en cm \n")
A = input("Longueur AB : ")
A = float(A) # float pour eviter les erreurs
B = input("Longueur BC : ")
B = float(B)
C = input("Longueur CA : ")
C = float(C)
aire()
