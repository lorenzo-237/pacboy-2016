## Ecrire une fonction qui prend une liste d'entiers pas forcément ordonée
  # en argument et qui retourne la médiane (et les quartiles). ##

def list_random():
    from random import randint
    L = []
    a = randint(20,21)
    for i in range(1,a):
        p = randint(1,20)
        L.append(p)
    return(L)

def mediane(L):
    L.sort()
    n = len(L)
    if n % 2 == 0:
        me = (L[n//2]+L[n//2 +1])/2
    else:
        me = L[(n + 1)// 2]
    return(print(L,me))

L1 = list_random()
L2 = list_random()

mediane(L1)
mediane(L2)
