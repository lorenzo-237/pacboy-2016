from tkinter import *
from random import *
import time

 # --- Fonctions --- # 

def mise_en_mouvement():
    global homme, n_img, absc, interrupteur, compteur, temps_en_seconde
    c = tuple(canvas.coords(homme))
    affichage_temps()
    if interrupteur == True and temps_en_seconde < 60: # 60 représente le temps de la partie en seconde (le programmeur peut changer)
        canvas.delete(homme) 
        homme = canvas.create_image(x+5*absc,y, image=image_homme[n_img])
        absc= absc+1            # variable qui permet de faire varier l'abscisse
        n_img = n_img+1         # variable qui permet de définir quelle image doit être crée
        if n_img ==8:   n_img=0         # il n'y que 8 images( de 0 à 7)  donc si n_img arrive a 8 c'est la 9eme image QUI n'existe pas donc on remet n_img à 0 pour recommencer le mouvement
    
        # reconnaitre si l'homme doit continuer ou entrer par la porte
        if aleat==1: # ICI L'HOMME ENTRE PAR LA PORTE
            if c[0] >= 730:
                interrupteur = False
                canvas.delete(homme)
                compteur = compteur + 1 # si il entre alors ajouter 1 au compteur
                print("c = ", compteur)
                """ MESSAGE : EFFACE LE print(compteur) QUAND TU N'EN AS PLUS BESOIN, C'EST POUR TOI QUE JE L'AI LAISSE. SI TU LANCES LE PRGM IL S'AFFICHERA
                CA TE PERMET DE VISUALISER"""
                affichage_homme() 
            else:
                canvas.after(4,mise_en_mouvement) # sinon relancer la fonction mouvement après ... millisec (ici 200)
        elif aleat==0: # ICI L'HOMME CONTINUE LA ROUTE
            if c[0] >= int(xmax):
                interrupteur = False
                canvas.delete(homme) # si il n'entre pas il n'y a pas d'ajout au compteur 
                affichage_homme() 
            else:
                canvas.after(3,mise_en_mouvement)
    elif interrupteur == True and temps_en_seconde >=60:  # 60 représente le temps de la partie en seconde (si le programmeur a changé en haut, penser à changer ici aussi)
        interrupteur == False
        fenetre_de_reponse()

def affichage_homme():
    global homme, interrupteur,n_img,absc,aleat
    aleat=randint(0,1)
    homme = canvas.create_image(x+5,y, image=img0)
    interrupteur= True
    absc = 1
    n_img = 0
    mise_en_mouvement()

def mise_en_mouvement2(): # rajouter 2 devant mise en mouvement
    global homme2, n_img2, absc2, interrupteur2, compteur, temps_en_seconde # rajouter 2 devant homme, interrupteur
    c2 = tuple(canvas.coords(homme2)) # rajouter 2 devant c, homme
    if interrupteur2 == True and temps_en_seconde < 60:  # rajouter 2 devant interrupteur
        canvas.delete(homme2) # rajouter 2 devant homme
        homme2 = canvas.create_image(x2+5*absc2,y, image=image_homme[n_img2]) # rajouter 2 devant homme et x
        absc2= absc2+1            
        n_img2 = n_img2+1         
        if n_img2 ==8:   n_img2=0 
    
        if aleat2==1: # rajouter 2 devant aleat
            if c2[0] >= 730: # rajouter 2 devant c
                interrupteur2 = False # rajouter 2 devant interrupteur
                canvas.delete(homme2) # rajouter 2 devant homme
                compteur = compteur + 1
                print("c = ", compteur)
                affichage_homme2()  # rajouter 2 devant affichage_homme
            else:
                canvas.after(4,mise_en_mouvement2) # rajouter 2 devant mise en mouvement
        elif aleat2==0:  # rajouter 2 devant aleat
            if c2[0] >= int(xmax): # rajouter 2 devant c 
                interrupteur2 = False # rajouter 2 devant interrupteur
                canvas.delete(homme2) # rajouter 2 devant homme
                affichage_homme2()  # rajouter 2 devant affichage_homme
            else:
                canvas.after(3,mise_en_mouvement2) # rajouter 2 devant mise en mouvement
    elif interrupteur2 == True and temps_en_seconde >=60: # rajouter 2 devant interrupteur
        interrupteur2 == False # rajouter 2 devant interrupteur

def affichage_homme2(): # rajouter 2 devant affichage homme
    global homme2, interrupteur2,n_img2,absc2,aleat2 # rajouter 2 devant homme, interrupteur, aleat
    aleat2=randint(0,1) # rajouter 2 devant aleat
    homme2 = canvas.create_image(x2+5,y, image=img0) # rajouter 2 devant homme
    interrupteur2= True # rajouter 2 devant interrupteur
    absc2 = 1
    n_img2 = 0
    mise_en_mouvement2() # rajouter 2 devant mise en mouvement

def affichage_temps():
    global temps_en_seconde
    temps_en_seconde = time.time() - temps_depart
    chrono.delete(ALL)                                                                                                                  #  font = ('nom de la police', taille d'écriture, 'style d'écriture(facultatif)')
    chrono.create_text(100,50, text="Time : {} sec ".format(temps_en_seconde//1), fill='yellow', font = ('Calibri', 20, 'bold')) # tu peux changer la couleur

def fenetre_de_reponse():
    global formulaire, saisie
    # Ici on va demander au joueur d'entrer sa réponse
    formulaire = Toplevel(bg='navy')
    question = Label(formulaire, text="Combien de bonhomme(s) sont entrés dans la maison ? ", fg='yellow', bg='navy', font = ('Calibri', 20, 'bold'))
    question.grid(row=1, column=1)
    txt = Label(formulaire, text='Votre réponse : ', fg='yellow', bg='navy', font=('Calibri',20,'bold'))
    txt.grid(row=2, column = 1)
    saisie = Entry(formulaire, width = 20,font=("Calibri", 20))
    saisie.grid(row=3, column=1, pady=5)
    bouton = Button(formulaire, text='VALIDER', command=valider)
    bouton.grid(row=4, column=1, pady=10)

def valider():
    if int(saisie.get()) == compteur:
        canvas.delete(ALL)
        canvas.configure(bg='green')
        canvas.create_text(700, 300, text ="Félicitation, c'est exact !", fill='orange', font = ('Calibri', 40, 'bold'))
        formulaire.destroy()
    else:
        canvas.delete(ALL)
        canvas.configure(bg='green')
        canvas.create_text(700, 300, text ="Dommage c'est faux ! La réponse exacte est {}".format(compteur), fill='orange', font = ('Calibri', 40, 'bold'))
        formulaire.destroy()

        
def lancement_jeu():
    global temps_depart
    """ time.time() = temps depuis le 1er janvier 1970 jusqu'au moment de son appelle
    au lancement du jeu on appelle un time.time() qu'on stock dans une variable. Ainsi plus tard on appellera un deuxieme time.time(),
    qui sera différent du premier (logique). Il suffit de soustraire le 1er time.time() au 2eme pour obtenir le temps qui s'est écoulé en seconde
    entre les deux.   """
    temps_depart = time.time() 
    mise_en_mouvement()
    mise_en_mouvement2()
    
 # --- Début du programme --- #
 
root = Tk()

# chargement des images (manuel mais peut être "automatiser" avec une fonction)
img0 = PhotoImage(file="Gabano0n.png")
img1 = PhotoImage(file="Gabano1n.png")
img2 = PhotoImage(file="Gabano2n.png")
img3 = PhotoImage(file="Gabano3n.png")
img4 = PhotoImage(file="Gabano4n.png")
img5 = PhotoImage(file="Gabano5n.png")
img6 = PhotoImage(file="Gabano6n.png")
img7 = PhotoImage(file="Gabano7n.png")
image_homme = {0:img0,1:img1,2:img2,3:img3,4:img4,5:img5,6:img6,7:img7} # on stock les images dans un dictionnaire

### création du canevas avec l'homme
image = PhotoImage(file="image1.jpg")  
canvas = Canvas(root, width = 1500, height = 600) # J'AI REDUIS TA FENETRE DE 100 PIXEL EN ORDONNEE , POUR AFFICHER LE SOL AVEC LE TEMPS EN BAS ! (à effacer après lecture mdr)
canvas.create_image(0,0, anchor = NW, image=image) 
canvas.pack()
xmax = canvas.cget('width') 
y1max= canvas.cget('height')

### on crée un canvas qui affiche le temps
chrono= Canvas(root, width=1500, height=100, bg='navy') # navy est la couleur, tu peux changer à ta guise (red, green, ...)
chrono.pack()

# Initialisation
aleat=randint(0,1)
interrupteur = True
compteur = 0
absc = 1
n_img = 0
x, y = 130,550 # positions initiales
x2 = 150 # ou une valeur au choix (c'est l'abscisse de l'homme 2)
aleat2 = randint(0,1)
interrupteur2 = True
absc2 =1
n_img2 = 0
homme2 = canvas.create_image(x2,y, image=img0)
homme= canvas.create_image(x,y, image=img0) # création de l'image dans le canevas

# Lancement du jeu
lancement_jeu()

root.mainloop()
