# -*- coding:Latin-1 -*-

from PIL import Image       # appel de la bibliothèque
from random import randint

def crea_image(largeur,hauteur,nom):
    fichier = open(nom + ".ppm", "w")
    fichier.write("P3" + "\n")
    fichier.write(str(largeur) + " " + str(hauteur) + "\n")
    fichier.write("255" + "\n")
    nb_pixels = largeur*hauteur
    for i in range(largeur):
        for j in range(hauteur): # if (i+j)%2 == 0 : F.W("0\n" ou 1)
            for k in range(3): #pour P3 car r v b 
                fichier.write(str(randint(0,255)) + " ")
        fichier.write("\n")
    fichier.close()

crea_image(100,100,"essai")


# if 29<i<41 and 59<j<91:
#                fichier.write("255 0 0" + " ")
#           else:
#                fichier.write("255 255 255" + " ")
