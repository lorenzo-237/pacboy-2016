## PGCD de deux nombre à l'aide de soustraction successives ##

def pgcd2(a,b):
	d = 1
	while d != 0:
		d = a - b
		a = b
		b = d
	return(a)

a = int(input("1er nombre : "))
b = int(input("2eme nombre : "))
print("Le PGCD de",str(a), "et",str(b), " est :")
print(pgcd2(a,b))
