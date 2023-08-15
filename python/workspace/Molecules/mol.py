from tkinter import *
# INITIALISATION
nbC = 4
nbH = 0
nbO = 0
nbGrpAlk=2
nbGrpAlc=1

# FONCTIONS
def addC():
    global nbC
    nbC=nbC + 1
    print(nbC)

def addH():
    global nbH
    nbH=nbH + 1
    print(nbH)

def addO():
    global nbO
    nbO=nbO + 1
    print(nbO)

def posGrp():
    global reponses, nbGrpAlk, nbGrpAlc, nbC
    reponses = []
    choix0 = []
    choix1 = []
    if nbGrpAlk != 0:
        for i in range(nbGrpAlk):
            ask = input("Position du groupe Alkyle n°{0} : ".format(i+1))
            choix0.append(ask)
            nbC = nbC - 1 # la valeur nbC sera remplacer par le nb de carbonne de la ch. princ.
            nbCP = nbC+1
            print(nbC)
            print(nbCP)
            nbGrpAlk = nbGrpAlk - 1
        reponses.append(choix0)
    if nbGrpAlc != 0:
        for i in range(nbGrpAlc):
            ask= input("Position du groupe Alcool n°{0} : ".format(i+1))
            choix1.append(ask)
            nbGrpAlc=nbGrpAlc - 1
        reponses.append(choix1)
    print(reponses)

# IL FAUT MTN NUMEROTER LA CHAINE + LA DESSINER
    
fen = Tk()

# LES INFOS DOIVENT SUIVRE UN ORDRE ON DEMANDE AT AVANT GRP ENSUITE ON DEMANDE POS DES GRP
# QUE L'USER AURA CHOISIT PLUS HAUT / LA POS EST DETERMINEE PAR RAPPORT AU GRP CARACT /
# UNE FOIS LES INFOS RECUEILLIES ON DESSINE LA MOLECULE A L'ECRAN GRACE AU nbCP , pos des grp,
# EN DESSOUS DE CHAQUE ATOME EST ECRIT LE NUMERO (PS : FORMULE DEVELOPPE, SEMI . .. . au choix)
# ENSUITE ON ECRIT LE NOM DE LA MOLECULE EN DESSOUS
# LIEN VERS UNE PAGE WEB QUI RESUME LES GRPS, LES MOL etc . . . le cours quoi NOMENCLATURE P 288

#ATOMES
Atomes = ["carbone","hydrogène","oxygène"]
Carb = Button(fen, text=Atomes[0], fg='red', width=10, command=addC).pack()
Hydr = Button(fen, text=Atomes[1], fg='red', width=10, command=addH).pack()
Oxy = Button(fen, text=Atomes[2], fg='red', width=10, command=addO).pack()

#GROUPES
# PREMIER TYPE
Alkyles = ["méthyle", "éthyle", "propyle"]
met = Button(fen, text=Alkyles[0], fg='blue', width=10).pack()
eth = Button(fen, text=Alkyles[1], fg='blue', width=10).pack()
prop = Button(fen, text=Alkyles[2], fg='blue', width=10).pack()
# SECOND TYPE
Alcool = ["OH", "alcool"]
alc = Button(fen, text=Alcool[1], fg='green', width=10).pack()
# TROISIEME TYPE
# ...

posGrp()

fen.mainloop()
