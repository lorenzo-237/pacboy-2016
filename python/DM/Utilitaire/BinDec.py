## Conversion de binaire vers décimal ##

# N = 0
# L = len(N2) # donne la taille de la chaîne, ici N2

# print("Il y a ",L," caractère(s) dans votre chaîne")
# print("")

# for i in N2: 
   # N = N + int(i)*2**(L-1)
   # L = L-1

# print(N2," en base 2 s'écrit ", N," en base 10.")
    
def bin_to_dec(N2):
    N10 = 0
    L = len(N2) # donne la taille de la chaîne, ici N2
    
    for i in N2: 
        N10 = N10 + int(i)*2**(L-1)
        L = L-1
    return(N10)

N2 = input("Entrer un nombre en binaire : ")
print(bin_to_dec(N2), "en base 10")
   
    
