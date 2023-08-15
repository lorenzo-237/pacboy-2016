from tkinter import *

 # --- Fonctions --- # 

def movement():
    global homme, n, k, interrupteur
    c = tuple(can.coords(homme)) # contient les coords de l'image a chaque mouvement c[0]= l'abscisse et c[1]= l'ordonnée
    if interrupteur == True: # interrupteur ON
        can.delete(homme) # on supprime l'ancienne image
        homme = can.create_image(x+30*n,y, image=Sauvegarde[k]) # on affiche la nouvelle image en faisant varier sont abscisse de 30*n (peut etre modifier selon l'utilisateur)
        k = k+1 # variable qui permet de définir quelle image doit être crée
        n = n+1 # variable qui permet de faire varier l'abscisse
        if k ==8:k=0 # il n'y que 8 images( de 0 à 7)  donc si k arrive a 8 c'est la 9eme image QUI n'existe pas donc on remet k à 0 pour recommencer le mouvement
    else:
        print("Interrupteur OFF")
    if c[0] >= int(xmax)-70: interrupteur = False  # condition : si l'abscisse de l'image est arrivé au bout de la fenêtre alors eteindre l'interrupteur
    else: can.after(200,movement) # sinon relancer la fonction mouvement après ... millisec (ici 200)
    
 # --- Début du programme --- #
 
fen = Tk()

#Initialisation
 
interrupteur = True
x, y = 100,350 # positions initiales

# chargement des images (manuel mais peut être "automatiser" avec une fonction)
img0 = PhotoImage(file="Gabano0.png")
img1 = PhotoImage(file="Gabano1.png")
img2 = PhotoImage(file="Gabano2.png")
img3 = PhotoImage(file="Gabano3.png")
img4 = PhotoImage(file="Gabano4.png")
img5 = PhotoImage(file="Gabano5.png")
img6 = PhotoImage(file="Gabano6.png")
img7 = PhotoImage(file="Gabano7.png")
Sauvegarde = {0:img0,1:img1,2:img2,3:img3,4:img4,5:img5,6:img6,7:img7} # on stock les images dans un dictionnaire
k = 0 # variable qui permet de définir quelle image doit être crée
n = 1 # variable qui permet de faire varier l'abscisse

# création du canevas 
can = Canvas(fen, height=700, width=1000)
can.pack()
xmax = can.cget('width') # trouve l'abscisse maximale du canevas donc 1000 ici

# création de l'image dans le canevas
homme = can.create_image(x,y, image=img0)

movement()

fen.mainloop()
