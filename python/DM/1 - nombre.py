### Informe si le nombre réel est + , - , ou nul ###

def  nombre():
    x = int(input("Votre nombre : "))
    if x < 0: return(print("Votre nombre est négatif."))
    elif x == 0: return(print("Votre nombre est nul."))
    else: return(print("Votre nombre est positif."))
    

nombre()
                
