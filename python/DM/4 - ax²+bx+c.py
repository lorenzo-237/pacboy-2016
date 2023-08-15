### Résout une équation de la forme ax² + bx + c = 0 ###

def equation():
    from math import sqrt
    a = int(input(" a = "))
    b = int(input(" b = "))
    c = int(input(" c = "))
    delta = b**2 - 4*a*c
    print("DELTA = ",delta)
    if delta > 0:
        print("L'équation admet deux solutions X1 et X2")
        X1 = (-b - sqrt(delta))/(2*a)
        X2 = (-b + sqrt(delta))/(2*a)
        return(print("X1 = ", X1 , "et X2 = ", X2))
    elif delta == 0:
        print("L'équation admet une solution")
        S = (-b)/(2*a)
        return(print("S = ", S))
    else:
        return(print("L'équation n'admet pas de solutions car delta est négatif."))

equation()
