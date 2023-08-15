### Résout une équation de la forme ax + b = 0 ###

def equation():
    a = int(input(" a = "))
    b = int(input(" b = "))
    print("Votre équation : ", a , "x +" , b , "= 0")
    if a == 0 and b != 0: return(print("L'équation n'admet pas de solutions.")) 
    elif a == 0 and b == 0: return(print("Equation indéterminée."))
    else:
        x = -b/a
        return(print("Solution : ", x))

equation()
