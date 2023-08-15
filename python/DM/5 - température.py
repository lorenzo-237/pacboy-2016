### Convertir Degrés Celsius en Fahrenheit ###

def F_to_C(F):
    return((F-32)/1.8)

def C_to_F(C):
    return(C*1.8 + 32)

for i in range(-273,1001):
    K = F_to_C(i)
    L = C_to_F(i)
    if K == L:
        print("La température" , i , " °F ou °C coïncide dans les deux unités.")
