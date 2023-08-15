def mise_en_mouvement2(): # rajouter 2 devant mise en mouvement
    global homme2, n_img, absc, interrupteur2, compteur, temps_en_seconde # rajouter 2 devant homme, interrupteur
    c2 = tuple(canvas.coords(homme2)) # rajouter 2 devant c, homme
    """ ICI ON A SUPPRIMER affichage_temps() CA NE SERT A RIEN DANS LES COPIE - PASTE DE LA PRINCIPALE """
    if interrupteur2 == True and temps_en_seconde < 60:  # rajouter 2 devant interrupteur
        canvas.delete(homme2) # rajouter 2 devant homme
        homme2 = canvas.create_image(x2+5*absc,y, image=image_homme[n_img]) # rajouter 2 devant homme et x
        absc= absc+1            
        n_img = n_img+1         
        if n_img ==8:   n_img=0 
    
        if aleat2==1: # rajouter 2 devant aleat
            if c2[0] >= 730: # rajouter 2 devant c
                interrupteur2 = False # rajouter 2 devant interrupteur
                canvas.delete(homme2) # rajouter 2 devant homme
                compteur = compteur + 1
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
        fenetre_de_reponse()

def affichage_homme2(): # rajouter 2 devant affichage homme
    global homme2, interrupteur2,n_img,absc,aleat2 # rajouter 2 devant homme, interrupteur, aleat
    aleat2=randint(0,1) # rajouter 2 devant aleat
    homme2 = canvas.create_image(x2+5,y, image=img0) # rajouter 2 devant homme
    interrupteur2= True # rajouter 2 devant interrupteur
    absc = 1
    n_img = 0
    mise_en_mouvement2() # rajouter 2 devant mise en mouvement

### DANS LA PARTIE INNITIALISATION EN BAS DU CODE RAJOUTER
x2 = 150 # ou une valeur au choix (c'est l'abscisse de l'homme 2)
aleat2 = randint(0,1)
interrupteur2 = True
homme2 = canvas.create_image(x2,y, image=img0)


### DANS LA FONCTION lancement_jeu() RAJOUTER EN BAS
mise_en_mouvement2()
