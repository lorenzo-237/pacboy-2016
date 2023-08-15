### PGCD de deux nombres grâce a a la division Euclidienne###

def pgcd(a,b):
    r = 1
    while r != 0:
        r = a%b
        a = b
        b = r
    return(a)

a = int(input("1er nombre :"))
b = int(input("2eme nombre :"))
print(pgcd(a,b))




    
