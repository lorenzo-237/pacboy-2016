### Programme qui trouve la prochaine année redondante ###
"""
AIDE
Une année est redondante lorsque qu'elle peut s'écrire de la forme
(10a + b)*a*b
EXEMPLE
1992 = (10*8 + 3)*8*3
"""
K = 0
for x in range(2015,2051): # on cherche dans l'intervalle 2015 - 2050 si il y a une année redondante
    for a in range(1,11):
        for b in range(1,11):
            S = ((x/a)/b) - 10*a - b
            if S == 0:
                K = x
                L = a
                M = b

print("Nous sommes en 2015, la prochaine année redondante est l'année : ",K)
print(K , "= (10 x", L , " +", M , ") x", L , " x", M)


