### Informe de la catégorie correspondante à un âge donné ###

def age():
    x = int(input("Entrez votre âge : "))
    if 6 <= x <= 7: return("Poussin")
    elif 8 <= x <= 9: return("Pupile")
    elif 10 <= x <= 11: return("Minime")
    elif 12 <= x <= 15: return("Cadet")
    elif 16 <= x <= 17: return("Junior")
    elif x >= 18: return("Senior")


print("Votre catégorie est : ", age())
