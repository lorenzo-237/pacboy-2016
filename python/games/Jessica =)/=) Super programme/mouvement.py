from tkinter import *
from random import *

 # --- Fonctions --- # 

def movement():
    global homme, n, k, interrupteur,detective, compteur
    c = tuple(canvas.coords(homme)) # contient les coords de l'image a chaque mouvement c[0]= l'abscisse et c[1]= l'ordonnée
    if interrupteur == True: # interrupteur ON
        canvas.delete(homme) # on supprime l'ancienne image
        homme = canvas.create_image(x+5*n,y, image=Sauvegarde[k]) # on affiche la nouvelle image en faisant varier sont abscisse (peut etre modifier selon l'utilisateur)
        k = k+1 # variable qui permet de définir quelle image doit être crée
        n = n+1 # variable qui permet de faire varier l'abscisse
        if k ==8:k=0 # il n'y que 8 images( de 0 à 7)  donc si k arrive a 8 c'est la 9eme image QUI n'existe pas donc on remet k à 0 pour recommencer le mouvement
    
    else:
        print("Interrupteur OFF")
   
    if aleat==1:
        if c[0] >= 730:
            interrupteur = False  # condition : si l'abscisse de l'image est arrivé au bout de la fenêtre alors eteindre l'interrupteur
            canvas.delete(homme)
            compteur = compteur + 1
            print(compteur)
            autrui()
        else: canvas.after(4,movement) # sinon relancer la fonction mouvement après ... millisec (ici 200)
    elif aleat==0:
        if c[0] >= int(xmax):
            interrupteur = False
            canvas.delete(homme)
            autrui()
        else: canvas.after(3,movement)

def movement2():
    global homme2, n2, k2, interrupteur2,detective2
    c = tuple(canvas.coords(homme2)) # contient les coords de l'image a chaque mouvement c[0]= l'abscisse et c[1]= l'ordonnée
    if interrupteur2 == True: # interrupteur ON
        canvas.delete(homme2) # on supprime l'ancienne image
        homme2 = canvas.create_image((x+30)+5*n2,y, image=Sauvegarde[k2]) # on affiche la nouvelle image en faisant varier sont abscisse de 30*n (peut etre modifier selon l'utilisateur)
        k2 = k2+1 # variable qui permet de définir quelle image doit être crée
        n2 = n2+1 # variable qui permet de faire varier l'abscisse
        if k2 ==8:k2=0 # il n'y que 8 images( de 0 à 7)  donc si k arrive a 8 c'est la 9eme image QUI n'existe pas donc on remet k à 0 pour recommencer le mouvement
    else:
        print("Interrupteur2 OFF")
   
    if aleat2==1:
        if c[0] >= 730:
            interrupteur2 = False  # condition : si l'abscisse de l'image est arrivé au bout de la fenêtre alors eteindre l'interrupteur
            canvas.delete(homme2)
            detective2=1
            autrui2()
        else: canvas.after(3,movement2) # sinon relancer la fonction mouvement après ... millisec (ici 200)
    elif aleat2==0:
        if c[0] >= int(xmax):
            interrupteur2 = False
            canvas.delete(homme2)
            detective2=1
            autrui2()
        else: canvas.after(4,movement2)

def parachute ():
    global bonhomme, n3, k3, interrupteur3, detective3
    c = tuple (canvas.coords(bonhomme))
    if interrupteur3 == True:
        canvas.delete(bonhomme)
        bonhomme = canvas.create_image((x1+30)+5*n3,y1+0.5*n3, image=Sauvegarde3[k3]) # je fais varier l'abscisse et l'ordonnée du parachute pour donner un effet de descente
        k3 = k3+1
        n3 = n3+1
        if k3 ==5:k3=0
    else:
        print ("Interrupteur OFF")

    if aleat3==1:
        if c[0] >=640: #abscisse de la cheminée
            interrupteur3 = False
            canvas.delete(bonhomme)
            detective3=1
            autrui3()
        else: canvas.after(100,parachute)
    elif aleat3==0:
        if c[0] >= int(xmax):
            interrupeteur3 = False
            canvas.delete(bonhomme)
            detective3=1
            autrui3()
        else: canvas.after(100,parachute)

def autrui():
    global homme, interrupteur,k,n,aleat
    homme = canvas.create_image(x+5,y, image=img0)
    interrupteur= True
    k = 0
    n = 1
    aleat=randint(0,1)
    movement()

def autrui2():
    global homme2, interrupteur2,k2,n2,aleat2
    if detective2==1:
        homme2 = canvas.create_image(x+30,y, image=img0)
        interrupteur2= True
        k2 = 0
        n2 = 1
        aleat2=randint(0,1)
        movement2()

def autrui3():
    global bonhomme, interrupteur3,k3,n3,aleat3
    if detective3==1:
        bonhomme = canvas.create_image(x1,y1, image=chut0)
        interrupteur3= True
        k3 = 0
        n3 =1
        aleat3=randint(0,1)
        parachute()
        
 # --- Début du programme --- #
 
root = Tk()

#Initialisation
aleat=randint(0,1)
aleat2=randint(0,1)
aleat3=randint(0,1)
interrupteur = True
x, y = 100,550 # positions initiales
interrupteur2= True
interrupteur3= True
x1, y1 =90,50
compteur = 0
# chargement des images (manuel mais peut être "automatiser" avec une fonction)
img0 = PhotoImage(file="Gabano0n.png")
img1 = PhotoImage(file="Gabano1n.png")
img2 = PhotoImage(file="Gabano2n.png")
img3 = PhotoImage(file="Gabano3n.png")
img4 = PhotoImage(file="Gabano4n.png")
img5 = PhotoImage(file="Gabano5n.png")
img6 = PhotoImage(file="Gabano6n.png")
img7 = PhotoImage(file="Gabano7n.png")
Sauvegarde = {0:img0,1:img1,2:img2,3:img3,4:img4,5:img5,6:img6,7:img7} # on stock les images dans un dictionnaire
k = 0 # variable qui permet de définir quelle image doit être crée
n = 1 # variable qui permet de faire varier l'abscisse
k2 = 0
n2 = 1

chut0 =PhotoImage(file="chuti.png")
chut1 =PhotoImage(file="chuti1.png")
chut2 =PhotoImage(file="chuti2.png")
chut3 =PhotoImage(file="chuti3.png")
chut4 =PhotoImage(file="chuti4.png")
Sauvegarde3 ={0:chut0, 1:chut1, 2:chut2, 3:chut3, 4:chut4}
k3 = 0
n3 = 1
### création du canevas
image = PhotoImage(file="image1.jpg")  
canvas = Canvas(root, width = 1500, height = 700)  
canvas.create_image(0,0, anchor = NW, image=image) 
canvas.pack()

xmax = canvas.cget('width') # trouve l'abscisse maximale du canevas donc 1000 ici
y1max= canvas.cget('height')
# création de l'image dans le canevas
homme2= canvas.create_image(x,y, image=img0)
homme= canvas.create_image(x+30,y, image=img0)
bonhomme= canvas.create_image(x1,y1, image=chut0)
movement()
movement2()
parachute()
root.mainloop()
