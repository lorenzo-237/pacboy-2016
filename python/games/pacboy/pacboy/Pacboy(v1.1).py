##############################################
#   Jeu :   PacBoy                           #
#   <Projet ISN>, Années 2015 - 2016         #                                                                                          
#   Auteurs : MAGNI Lorenzo , DIPOKO Willia  #
##############################################

from tkinter import *
from random import choice
from tkinter.messagebox import *
import time
import pygame
from pygame.locals import *
from math import *

                                                                                        ######################
                                                                                        #### --- CLASSE --- ##
                                                                                        ######################

# -------------------------------------------------- JEU PACBOY -------------------------------------------------- #

class Pacboy:
    # __init__ / self  : sont des noms donnés par convention
    # __init__ = le constructeur , où on initialise les valeurs et lançons les méthodes (fonctions) utiles
    # self = est le nom donné par convention à la variable "moteur" de la classe, dans les variables que nous souhaitons réutiliser dans toute la classe nous mettrons self.nomdelavariable
    # boss = représente  la référence du widget "maître" généralement un canvas dans lequel on y ajoute des éléments

    def __init__(self,boss,CR,CB,TIME):
        """-- Stockage des paramètres -- """
        self.boss=boss                  # référence du canevas
        self.x0=self.y0=5                                       # début du premier abscisse et du premier ordonnée de la grille (identique pour les deux)
        self.n0=55                                                        # début du premier abscisse et du premier ordonnée des CENTRES de la grille
        self.x1, self.y1 = 55,55                                              # coordonnées du premier pion (pion bleu)
        self.x2, self.y2 = 955,655                                          # coordonnées du second pion (pion rouge)
        self.compteur_rouge=CR  # Compteur Rouge, le paramètre donné est stocké dans une variable de la classe (donc réutilisable dans la classe)
        self.compteur_bleu=CB    # Compteur Bleu
        self.temps=TIME               # le paramètre TIME est stocké dans une variable
        """-- Initialisation -- """
        self.longueur,self.largeur=9,6                        # longueur(axe abscisses) et largeur(axe ordonnées)
        self.Abscisses,self.Ordonnees = [self.x0],[self.y0]     # initialisation listes des abscisses et des ordonnées avec le paramète xy (identique pour les deux)
        self.Centres_X,self.Centres_Y = [self.n0],[self.n0]        # initialisation  listes des CENTRES des abscisses et des ordonnées avec le paramètre n
        self.Extremitees=[0,69]                                 # Liste des cases où doivent finir les pions
        self.nombre_de_pastilles=15                              # changer ce nombre changera le nombre de pastilles
        self.nombre_de_pastilles_speciales=2
        """-- Lancement des méthodes de la classe Pacboy --"""
        self.centres()
        self.abscisses()
        self.ordonnees()
        self.creation_grille()
        self.creation_obstacle()
        self.creation_pastille()
        self.creation_pastille_speciale()
        self.pion()
        self.tableau_score()

        """une méthode = une fonction dans une classe : on attribue une variable "moteur" à chaque méthode (ici c'est le self) ce qui nous permet de reprendre les variables
        initialiser dans le constructeur """
    def centres(self):
        """ définit les centres des cases"""
        for i in range(self.longueur): # il y a 10 cases en abscisse mais i varie de 0 à 9 ! RAPPEL : une liste est indexée de 0 à n
            centre1 = self.Centres_X[i]+100   # On ajoute tous les centres des cases, possibles en abscisse dans une liste
            self.Centres_X.append(centre1)
        for j in range(self.largeur): 
            centre2 = self.Centres_Y[j]+100 # On ajoute tous les centres des cases, possibles en ordonnée dans une liste
            self.Centres_Y.append(centre2)
            
    def abscisses(self):
        """ définit les abscisses de la grille """
        for i in range(self.longueur):
            add_ab= self.Abscisses[i]+100 # On ajoute les abscisses denotre grille dans une liste
            self.Abscisses.append(add_ab)
            
    def ordonnees(self):
        """ définit les ordonnées de la grille """
        for i in range(self.largeur):
            add_or = self.Ordonnees[i]+100 # On ajout les ordonnées denotre grille dans une liste
            self.Ordonnees.append(add_or)
            
    def creation_grille(self):
        """ Création des lignes horizontales """
        for i in range(self.longueur+2):
            k = 100*i+5                 # Décalage de la grille de 5 pixels afin de voir les premiers tracés
            self.boss.create_line(k,5,k,705)
        """ Création des lignes verticales """
        for j in range(self.largeur+2):
            k = 100*j+5
            self.boss.create_line(5,k,1005,k)
        """ Colore d'une couleur différentes, de celle de la grille, les cases ou doivent finir les pions (Manuel)"""
        self.boss.create_rectangle(5,5,105,105, fill="pink")
        self.boss.create_rectangle(905,605,1005,705, fill="pink")
    
    def pion(self):
        """ Création du pion bleu """
        self.p_bleu = self.boss.create_image(self.x1,self.y1, image = bluepion) # crée une image de coords(x,y)
        self.boss.bind('<KeyPress-z>', self.move_blue)
        self.boss.bind('<KeyPress-q>', self.move_blue)  # ".bind" attend la pression d'une touche 
        self.boss.bind('<KeyPress-s>', self.move_blue)  # pour faire appel à la fonction indiquée
        self.boss.bind('<KeyPress-d>', self.move_blue)
        """ Création du pion rouge """
        self.p_rouge = self.boss.create_image(self.x2,self.y2, image = redpion) # crée une image de coords(x2,y2)
        self.boss.bind('<Up>', self.move_red)
        self.boss.bind('<Down>', self.move_red)
        self.boss.bind('<Right>', self.move_red)
        self.boss.bind('<Left>', self.move_red)
        
    def creation_obstacle(self,color="dark green"):
        self.CaseObstacles = []       # initialisation liste contenant les numéros des cases des obstacles (au début vide)
        for i in range(15):
            a = choice(self.Abscisses)                                                                                      # choice choisit aléatoirement une valeur dans la liste
            b = choice(self.Ordonnees)
            case_obstacle=(b-self.y0)/10+(a-self.x0)/100                                                         # formule qui détermine le numéro de la case grâce à l'abscisse et l'ordonnée
            """
            Empêche l'obstacle de se mettre sur les cases 0,10,1 et 69,59,68 (cases d'apparition des pions + cases autour)
            et sur une case où il y a déjà un obstacle (Manuel) (Possibilité futur : automatiser pour que le pion ne soit pas bloqué)
            """
            while case_obstacle == 0 or case_obstacle == 10 or case_obstacle == 1 \
                    or case_obstacle == 69 or case_obstacle == 59 or case_obstacle == 68 \
                    or (case_obstacle in self.CaseObstacles) == True \
                    or (case_obstacle-10 in self.CaseObstacles) == True \
                    or (case_obstacle+20 in self.CaseObstacles) == True \
                    or (case_obstacle-1 in self.CaseObstacles) == True \
                    or (case_obstacle+1 in self.CaseObstacles) == True:
                a = choice(self.Abscisses)
                b = choice(self.Ordonnees)                              # on répète le choix des coords des obstacles si on est dans un des cas ci-dessus
                case_obstacle=(b-self.y0)/10+(a-self.x0)/100
            c = a+100
            d = b+100
            self.CaseObstacles.append(case_obstacle) # ajoute de la "case de l'obstacle"  dans la "liste contenant les cases des obstacles"
            self.boss.create_rectangle(a,b,c,d, fill =color) # crée l'obstacle (un carré)
            
    def creation_pastille(self):
        CoordsPX = []
        CoordsPY = []
        self.pastille ={} # pastille est un dictionnaire (vide au début), on peut ainsi donner un indice appelé "clé" à une variable et différencier la pastille[1] de la pastille[2]
        self.CasePastilles= [] # initialisation liste contenant les numéros des cases des pastilles (au début vide)
        for n in range(self.nombre_de_pastilles):  # nombre de pastille
            a = choice(self.Centres_X[1:8])                                                                     # choisit aléatoirement une valeur entre l'indice 1 et 8 
            b = choice(self.Centres_Y[1:6])                                                                     # choisit aléatoirement une valeur entre l'indice 1 et 6
            case_pastille = (b-self.n0)/10 + (a-self.n0)/100                                             # formule qui détermine le numéro de la case
            """ Empêche la pastille de se mettre sur une case où se situe un obstacle ou sur une case où se situe déjà une
            autre pastille"""
            while (case_pastille in self.CaseObstacles) == True or (case_pastille in self.CasePastilles) == True:
                a = choice(self.Centres_X[1:8]) 
                b = choice(self.Centres_Y[1:6]) 
                case_pastille = (b-self.n0)/10 + (a-self.n0)/100
            CoordsPX.append(a)                             # ajoute les coords des pastilles dans deux listes afin d'aligner 
            CoordsPY.append(b)                             # coords(x,y) de chaque pastille
            self.CasePastilles.append(case_pastille)    # ajoute de la "case de la pastille"  dans la "liste contenant les cases des pastilles"
            self.pastille[n+1]= self.boss.create_image(CoordsPX[n],CoordsPY[n], image = yellowpion)
            """ n variant de 0 à nb_pastille crée pastille[1], pastille[2]... pour les différencier les unes des autres"""

    def creation_pastille_speciale(self):
        CoordsPX = []
        CoordsPY = []
        self.pastillespe ={}
        self.CasePastilleSpeciales = []
        for n in range(self.nombre_de_pastilles_speciales):
            a = choice(self.Centres_X[1:8])                                                                     # choisit aléatoirement une valeur entre l'indice 1 et 8 
            b = choice(self.Centres_Y[1:6])                                                                     # choisit aléatoirement une valeur entre l'indice 1 et 6
            case_pastille = (b-self.n0)/10 + (a-self.n0)/100                                             # formule qui détermine le numéro de la case
            while (case_pastille in self.CaseObstacles) == True or (case_pastille in self.CasePastilles) == True or (case_pastille in self.CasePastilleSpeciales) == True:
                a = choice(self.Centres_X[1:8]) 
                b = choice(self.Centres_Y[1:6])
                case_pastille = (b-self.n0)/10 + (a-self.n0)/100
            CoordsPX.append(a)                             # ajoute les coords des pastilles dans deux listes afin d'aligner 
            CoordsPY.append(b)                             # coords(x,y) de chaque pastille
            self.CasePastilleSpeciales.append(case_pastille)
            self.pastillespe[n+1]= self.boss.create_image(CoordsPX[n],CoordsPY[n], image = purplepion)
            
    def tableau_score(self):
        """ Tableau affichant en permanence les compteurs et le score des pions (Manuel)"""
        can2.delete(ALL) # supprime tout dans le canvas 2 et rafraichit avec de nouveaux éléments
        can2.create_line(0,150,300,150,width=20, fill='yellow') # width permet de créer une ligne épaisse
        can2.create_text(150,30, text="Bleu vs Rouge ! Fight !", fill='purple',font=('Helvetica', 10, 'bold')) # Création de text dans le canvas AIDE = ('Helvetica', 10, 'bold') = Police , taille , gras
        can2.create_text(90,75, text= "Compteur Bleu : {0} ".format(self.compteur_bleu), fill='blue',font =('Helvetica', 10, 'bold')) # .format() permet d'associer à {0} une variable
        can2.create_text(90,100, text="Score Bleu : {0}".format(score_bleu_final), fill='blue',font =('Helvetica', 10, 'bold'))
        can2.create_text(90,225, text="Compteur Rouge : {0}".format(self.compteur_rouge), fill='red', font =('Helvetica', 10, 'bold'))
        can2.create_text(90,250, text="Score Rouge  : {0}".format(score_rouge_final), fill='red',font =('Helvetica', 10, 'bold'))
    
    def calcul_score(self,compteurR,compteurB,temps):
        """ nécessite 3 paramètres la valeur des compteur et le temps"""
        global score_rouge_final, score_bleu_final # fait sortir, de la fonction, le score_final calculé
        """ calcul "intermédiaire" des scores """
        score_rouge = (compteurR+200)//temps + score_rouge_final
        score_bleu = (compteurB+200)//temps  + score_bleu_final 
        # stock le score dans une nouvelle variable pour ensuite l'additionner lors
        # de la prochaine manche à l'ancien score (dans le calcul intermédiaire)
        score_rouge_final = score_rouge
        score_bleu_final = score_bleu
        # on renitialise les compteurs pour la prochaine manche
        self.compteur_rouge=self.compteur_bleu=0 # RAPPEL : self. permet de réutiliser la variable dans toute la classe

    def verifier_gagnant(self):
        """ actions à faire en comparant les scores des pions"""
        self.boss.delete(ALL) # on efface les images à l'écran
        if score_rouge_final>score_bleu_final: showinfo("GAGNE","Le pion rouge a gagné BRAVO !") # showinfo affiche une fênêtre d'informations
        elif score_rouge_final==score_bleu_final: showinfo("EGALITE ","Félicitation aux deux joueurs ! ")
        else: showinfo("GAGNE","Le pion bleu a gagné BRAVO !")
    
    def case_finale(self,case,case_bis):
        """Test si le pion se trouve sur la case où il doit terminer lorsque toutes les pastilles ont été mangées"""
        global manche # fait sortir, de la fonction, le numéro de la manche
        if  (case == self.Extremitees[1] or case_bis== self.Extremitees[0]):  #case = case du pion bleu / case_bis = case du pion rouge
            # si les manches sont encore en cours
            if manche < 3 and self.CasePastilleSpeciales == [" "," "]: 
                self.temps=time.time()-temps_depart
                """ time.time() = le temps depuis janvier 1970 jusqu'au moment où on appelle time.time()
                temps_départ est une variable associée à un time.time() définit au début d'une manche(cf. fonction lancement_pacboy plus bas)
                Ainsi on soustrait le temps actuelle au temps d'avant, nous donnant ainsi les secondes passées entre avant et maintenant."""
                self.calcul_score(self.compteur_rouge,self.compteur_bleu,self.temps)    # on appelle la fonction qui calcul les scores(définit plus haut)
                manche = manche + 1                                                                                # après le calcul on ajoute 1 manche
                decompte()                         # on recommence la manche avec la fonction(définit plus bas)
            # si les manches sont terminées
            elif manche ==3 and self.CasePastilleSpeciales == [" "," "]:
                self.temps=time.time()-temps_depart
                self.calcul_score(self.compteur_rouge,self.compteur_bleu,self.temps)
                can.after(300,self.verifier_gagnant) # apres 300ms lance la fonction
                
    def case(self,i,j):
        """ Afin de pouvoir poser les conditions plus tard, on définit les cases en haut/bas/droite/gauche du pion
        la fonction attend 2 paramètre i et j (index des listes Centres X et Centres Y"""   
        self.case_haut = (j-1)*10 + i
        self.case_bas= (j+1)*10 + i
        self.case_droite= j*10 + (i+1)
        self.case_gauche= j*10 + (i-1)
        self.case_sans_importance = -4 # Cette case permet de passer une condition dans la fonction case_finale (définit ci-dessous)
        """Cette fonction est appelée dans les mouvements des pions """
        
    def bleu_supprime_pastille(self,case):
        """ Action à faire lorsque le pion bleu quitte une pastille """
        self.boss.coords(self.p_bleu,self.x1,self.y1) # changer les coord(x,y) du pion avec de nouvelles coords.
        for n in range(self.nombre_de_pastilles):
            if case == self.CasePastilles[n]: # si la case où se situe le pion est dans la liste des cases des pastilles
                    self.compteur_bleu= self.compteur_bleu + 100   # on incrémante le compteur bleu de 100
                    self.CasePastilles[n] = " "                                     # on remplace dans la liste des cases pastilles la case où se situe le pion par " "   
                    self.boss.delete(self.pastille[n+1])                        # dans le dictionnaire on supprime la pastille[n] qui vient d'être mangée
        for i in range(self.nombre_de_pastilles_speciales):
            if case == self.CasePastilleSpeciales[i]:
                self.CasePastilleSpeciales[i] = " "                             # on remplace dans la liste des cases pastilles speciales la case où se situe le pion par " "
                self.boss.delete(self.pastillespe[i+1])                       # dans le dictionnaire on supprime la pastillespe[n] qui vient d'être mangée
                son_pastillespe.play()              # on joue le son lorsque le pion mange la pastille
                self.who = "blue" # who = blue signifie que c'est le pion bleu qui a mangé la pastille
                self.boss.coords(self.p_bleu,self.x1,self.y1)
                can3.focus_set() # on change le temporairement le focus sur un canevas inutile pour empêcher les mouvements des pions jusqu'au moment où, le joueur termine le jeu Shurika
                if i == 0:
                    self.shuriken(200,500)
                elif i == 1:
                    self.blast(50,600)

    def rouge_supprime_pastille(self,case):
        """ Action à faire lorsque le pion rouge quitte une pastille """
        self.boss.coords(self.p_rouge,self.x2,self.y2)
        for n in range(self.nombre_de_pastilles):
            if case == self.CasePastilles[n]:
                    self.compteur_rouge= self.compteur_rouge + 100
                    self.CasePastilles[n] = " "
                    self.boss.delete(self.pastille[n+1])
        for i in range(self.nombre_de_pastilles_speciales):
            if case == self.CasePastilleSpeciales[i]:
                self.CasePastilleSpeciales[i] = " "
                self.boss.delete(self.pastillespe[i+1])
                son_pastillespe.play()
                self.who = "red" # who = red signifie que c'est le pion rouge qui a mangé la pastille
                can3.focus_set()
                if i == 0:
                    self.shuriken(200,500)
                elif i == 1:
                    self.blast(50,600)
             
    def move_blue(self,event):
        """ Mouvement du pion bleu """
        i = self.Centres_X.index(self.x1) # i et j sont la valeur de l'index dans les listes des centres 
        j = self.Centres_Y.index(self.y1) # des coords(x,y) du pion
        mouvement = 100
        self.case(i,j) # on détermine les cases utiles pour la gestion des collisions
        case_actuelle= j*10 + i # la case où se situe le pion avant sont mouvement
        if event.keysym == "z" and self.y1 > 55 and  (self.case_haut in self.CaseObstacles) == False and self.case_haut != (self.Centres_X.index(self.x2)+self.Centres_Y.index(self.y2)*10):
            """ si pression sur z , si la coord y est supérieur a 55 (limite de la grille), si case d'en haut n'a pas d'obstacle, si case d'en haut n'est pas la case où se situe l'autre pion actuellement
            alors faire varier la position sur l'axe des ordonnées du pion et vérifier si la case où il se situe contient une pastille"""
            self.y1 = self.y1 - mouvement
            self.bleu_supprime_pastille(case_actuelle)
        elif event.keysym == "s" and self.y1 < 655 and (self.case_bas in self.CaseObstacles) == False and self.case_bas != (self.Centres_X.index(self.x2)+self.Centres_Y.index(self.y2)*10):
            self.y1 = self.y1 + mouvement
            self.bleu_supprime_pastille(case_actuelle)
        elif event.keysym == "q" and self.x1 > 55 and (self.case_gauche in self.CaseObstacles) == False and self.case_gauche != (self.Centres_X.index(self.x2)+self.Centres_Y.index(self.y2)*10):
            self.x1 = self.x1- mouvement
            self.bleu_supprime_pastille(case_actuelle)
        elif event.keysym == "d" and self.x1 < 955 and (self.case_droite in self.CaseObstacles) == False and self.case_droite != (self.Centres_X.index(self.x2)+self.Centres_Y.index(self.y2)*10):
            self.x1 = self.x1 + mouvement
            self.bleu_supprime_pastille(case_actuelle)
        else: son_bloque.play()
            
        self.case_finale(case_actuelle,self.case_sans_importance) # vérifier si le pion n'est pas à l'extremitée opposée à sa position de debut de partie
        try : self.tableau_score() # rafraichir l'affichage du score
        except: None # try + except empeche l'apparition d'une erreure lors de la fermeture du jeu après avoir pris une pastille violette
        
    def move_red(self,event):
        """ Mouvement du pion rouge """
        i = self.Centres_X.index(self.x2)
        j = self.Centres_Y.index(self.y2)
        mouvement = 100
        self.case(i,j)
        case_actuelle = j*10 + i
        if event.keysym == "Up" and self.y2 > 55 and (self.case_haut in self.CaseObstacles) == False and self.case_haut != (self.Centres_X.index(self.x1)+self.Centres_Y.index(self.y1)*10):
            self.y2 = self.y2 - mouvement
            self.rouge_supprime_pastille(case_actuelle)
        elif event.keysym == "Down" and self.y2 < 655 and (self.case_bas in self.CaseObstacles) == False and self.case_bas != (self.Centres_X.index(self.x1)+self.Centres_Y.index(self.y1)*10):
            self.y2 = self.y2 + mouvement
            self.rouge_supprime_pastille(case_actuelle)
        elif event.keysym == "Left" and self.x2 > 55 and (self.case_gauche in self.CaseObstacles) == False and self.case_gauche != (self.Centres_X.index(self.x1)+self.Centres_Y.index(self.y1)*10):
            self.x2 = self.x2 - mouvement
            self.rouge_supprime_pastille(case_actuelle)
        elif event.keysym == "Right" and self.x2 < 955 and (self.case_droite in self.CaseObstacles) == False and self.case_droite != (self.Centres_X.index(self.x1)+self.Centres_Y.index(self.y1)*10):
            self.x2 = self.x2 + mouvement
            self.rouge_supprime_pastille(case_actuelle)
        else: son_bloque.play()
            
            
        self.case_finale(self.case_sans_importance,case_actuelle) # inversion case_sans_importance et case_actuelle (par rapport au pion bleu)
                                                                                                         # ASTUCE : permet de passer une condition
        try: self.tableau_score() # rafraichir l'affichage du score
        except: None # try + except empeche l'apparition d'une erreure lors de la fermeture du jeu après avoir pris une pastille violette

# -------------------------------------------------- JEU SHURIKA -------------------------------------------------- #
    def shuriken(self,abss, ordo):
        self.FenShurika= Toplevel()
        self.FenShurika.title("Shurika")
        self.main=Canvas(self.FenShurika, height=650,width=1300, bg='ivory') # référence du canevas
        self.main.pack()
        self.main.focus_set()
        self.u=abss # coords initiales 
        self.v=ordo
        self.main.delete(ALL) # supprime tout pour réactualiser
        """ creation du fond du canevas """
        self.fond = PhotoImage(file='shurika/fond.png')
        self.main.create_image(0, 0, image=self.fond, anchor=NW)
        """ creation de l'image d'un shuriken """
        self.img1 = PhotoImage(file='shurika/shurikenr.png') # Rouge
        self.img2 = PhotoImage(file='shurika/shurikenb.png') # Bleu
        if self.who =='red':     self.shu =  self.main.create_image(abss,ordo, image=self.img1) # si c'est le pion rouge qui a activé le jeu, prendre l'image rouge
        elif self.who=='blue':   self.shu =  self.main.create_image(abss,ordo, image=self.img2) # si c'est le pion bleu qui  a activé le jeu, prendre l'image bleue
        # retrouver la hauteur du canevas (cad l'ord. maximale)
        self.yMax = int(self.main.cget('height'))
        # retrouver la largeur du canevas (cad l'abs. maximale)
        self.xMax = int(self.main.cget('width'))
        """ Attente des évènements """
        self.main.bind("<Button-1>", self.mouse_down)             # pression sur le bouton gauche de la souris
        self.main.bind("<Button1-Motion>", self.mouse_move)   # mouvement de la souris une fois le bouton maintenu
        self.anim = False       # interrupteur d'animation (gère l'arrêt et le debut du mouvement)
        """ Chargment des images du shuriken (plusieurs images pour gérer la rotation de l'objet) """
        # IMAGE D'UN SHURIKEN BLEU
        shurikenb0= PhotoImage(file='shurika/shurikenb0.png')
        shurikenb1= PhotoImage(file='shurika/shurikenb1.png')
        shurikenb2= PhotoImage(file='shurika/shurikenb2.png')
        shurikenb3= PhotoImage(file='shurika/shurikenb3.png')
        shurikenb4= PhotoImage(file='shurika/shurikenb4.png')
        shurikenb5= PhotoImage(file='shurika/shurikenb5.png')
        # IMAGE D'UN SHURIKEN ROUGE
        shurikenr0= PhotoImage(file='shurika/shurikenr0.png')
        shurikenr1= PhotoImage(file='shurika/shurikenr1.png')
        shurikenr2= PhotoImage(file='shurika/shurikenr2.png')
        shurikenr3= PhotoImage(file='shurika/shurikenr3.png')
        shurikenr4= PhotoImage(file='shurika/shurikenr4.png')
        shurikenr5= PhotoImage(file='shurika/shurikenr5.png')
        # DICTIONNAIRES (B/R) CONTENANT LES IMAGES
        self.DicoPosB = {0:shurikenb0,1:shurikenb1,2:shurikenb2,3:shurikenb3,4:shurikenb4,5:shurikenb5} # Dico des images Bleu
        self.DicoPosR = {0:shurikenr0,1:shurikenr1,2:shurikenr2,3:shurikenr3,4:shurikenr4,5:shurikenr5} # Dico des images Rouge
        self.cibles()
        self.FenShurika.mainloop()
        
    def calcul_cos_angle(self,abscisseS, ordonneeS): # attend 2 paramètres les coords du points S (S comme Shuriken)
        """ Formule d'Al Kashi pour trouver le cos d'un angle
        Soit A un point de coord fixe, B un point d'abscisse fixe et S le point représentant les coords du Shuriken"""
        pA = (self.u,self.v)                                                                      # le point A 
        pB = (600,ordonneeS)                                                               # le point B
        segSA=sqrt((abscisseS-self.u)**2 + (ordonneeS-self.v)**2)   # Formule qui calcul les longueurs des segments du triangle ABS
        segSB=sqrt((abscisseS-600)**2)                                            # le point B et le point S ont la même ordonnée donc la longueur SB dépend des abscisses
        segAB=sqrt((self.u-600)**2 + (self.v-ordonneeS)**2)
        self.cosangleASB= (-(segAB)**2+(segSA)**2+(segSB)**2)/(2*(segSA)*(segSB))
        # Formule d'Al Kashi 
        
    def cibles(self):
        """ Stock dans des listes les coords occupées par les cibles du jeu """
        S = [1200,1300]                                                                # intervalle sur l'axe des abs. occupé par les cibles
        LY = [[498, 599],[398, 499],[298, 399],[198, 299],[98, 199],[0, 100]] # intervalles sur l'axe des ord. occupés par les cibles, ils ont été déterminés par le programmeur
        self.LX = []        # liste avec les coords. en abs. des cibles 
        self.Cible = {} # dictionnaire qui regroupe les listes de l'axe des ord.
        for i in range(S[0],S[1]):
            self.LX.append(i) # on ajoute toutes les valeurs entre l'intervalle 
        for n in range(len(LY)):
            Sav = [] # liste pour sauvegarder qui sera ajouter au dictionnaire
            for i in range(LY[n][0], LY[n][1]):
                Sav.append(i) # on ajoute toutes les valeurs entre les intervalles 
            self.Cible[n]= Sav  # on ajoute la liste formée au dictionnaire puis on recommence la boucle

    def mouse_down(self,event):
        """ pression du bouton """ 
        self.u1, self.v1 = event.x, event.y                               # coords du clic effectué
        self.item = self.main.find_closest(self.u1, self.v1)  # renvoie la référence du dessin le plus proche
        self.main.lift(self.item)                                             # fait passer le dessin à l'avant-plan
        
    def mouse_move(self,event):
        """ le bouton est maintenu et la souris bouge """
        self.u2, self.v2 = event.x, event.y                             # coords de la souris à chaque mouvement de celle-ci
        if self.u2 <= 320 and self.v2 <= 590:                       # conditions qui fixent une zone pour déplacer le Shuriken
            self.calcul_cos_angle(self.u2, self.v2)  # calcul le cos de l'angle qui nous interresse
            dx, dy = self.u2-self.u1, self.v2-self.v1   # coords de déplacement de l'objet sur les deux axes
            self.main.move(self.item, dx, dy)     # la souris est mise en mouvement et l'objet se déplace à chaque fois de (dx, dy)
            self.u1, self.v1 = self.u2, self.v2 # l'objet a été déplacé donc ses coords ont changés
            self.main.bind("<Button1-ButtonRelease>", self.mouse_up) # relâchement du bouton gauche
            
    def mouse_up(self,event):
        """ le bouton a été relâché """
        if not self.anim: # si l'interrupteur : OFF 
            self.anim = True # interrupteur : ON
            self.time=time.time() # lancement du chrono. (pour le temps)
            """ Définition de la force du lancé """
            if 150<self.u2<200:
                self.vit = 5+self.v2/115
            elif 100<self.u2<150:                                                   # ces conditions fixent la vitesse en fonction
                self.vit = 10+self.v2/110                                           # des coords (x,y) de l'objet au moment du
            else:                                                                               # relâchement du clic gauche
                self.vit=15+self.v2/105
            self.n=0    # variable qui permet dans la fonction animation de changer l'image à chaque mouvement et donner l'effet de rotation
            self.angle = acos(self.cosangleASB) # arc cos de l'angle pour retrouver la valeur de l'angle (ici en RADIAN)
            self.animer_shuriken() # appelle la fonction qui lancement l'animation du Shuriken (voir plus bas)

    """ les trois prochaines fonctions se répètents à chaque mouvement car elles sont appelées dans la fonction animation """
    
    def verifier_sol(self):
        """ verifier si le Shuriken atteint le sol (le bas du canevas) """
        c = tuple(self.main.coords(self.shu))        # dans un tuple on stock les coords du shuriken à chaque mouvement
        self.x0, self.y0 = c[0], c[1]   # les coords (x,y) du shuriken sont dans le tuple donc on les attribue une variable pour les réutiliser simplement
        if self.y0+60 > self.yMax or self.x0 > self.xMax: # si les coords. sont proche du bord (à 60pixels près pour l'ord. max.)
            self.anim=False     # interrupteur : OFF , arrêt de l'animation
            self.level = 0 # lorsque level = 0 on sait que nous avons touché le sol
            self.point = -300 # le nb de point quand on touche le sol
            self.main.after(1000,self.afficher_resultat)
            
    def verifier_cible(self):
        """ verifier la zone où le Shuriken est arrivé pour attribuer les points """
        for h in range(len(self.Cible)):                                        # on rappelles que les coords sont stockers
            if (self.x0 in self.LX and self.y0 in self.Cible[h]):       # on cherche dans quelle liste se trouve les coords. du Shuriken (donc la cible où il se trouve)
                self.point = h*100                                                # une fois trouvée, on calcul les points grâce a la zone où se trouve le Shuriken
                self.anim=False # interrupteur : OFF
                self.level = 1 # lorsque level = 1 on sait que nous avons touché la cible
                self.main.after(1000,self.afficher_resultat)
                
    def rotation(self):
        """ gestion de la rotation du shuriken """
        self.main.delete(self.shu) # on supprime l'ancien shuriken
        if self.who == 'red':       self.shu =self.main.create_image(self.x0, self.y0, image=self.DicoPosR[self.n])
        elif self.who == 'blue':    self.shu =self.main.create_image(self.x0, self.y0, image=self.DicoPosB[self.n])
        # on réaffiche un nouveau grâce à self.n qui est incrémenté dans la fonction animation (ci-dessous) 
            
    def animer_shuriken(self):
        self.verifier_sol()
        self.verifier_cible()
        if self.anim: # si interrupteur : ON , début animation
            self.posx = self.vit * cos(self.angle) *(time.time()-self.time) # équation horaire x(t)
            self.rotation() 
            self.n=self.n+1 # changement de la prochaine image dans la fonction rotation qui est appelée tant que l'interrupteur est ON
            """ il n'y a que 6 image (img0 - img 5) donc une fois qu'on a afficher l'img5 on remet a 0 pour afficher l'img0 (ainsi de suite) """
            if self.n==6: self.n=0
            """ Conditions qui déterminent si le shuriken est orienté vers le bas ou vers le haut. L'équation horaire y(t) diffère alors
            car on rappelle que sur tkinter l'axe des ord. est vers le bas.
            Shuriken orienté vers le bas : le champs de pesanteur est dans le même sens du mouvement
            Shuriken orienté vers le haut : le champs de pesanteur est dans le sens contraire du mouvement"""
            if self.v2-self.v < 0: # vers le bas 
                self.posy = 0.5 * 9.81 * ((time.time()-self.time)**2) + self.vit * sin(self.angle) * (time.time()-self.time)
                self.main.move(self.shu, int(self.posx), int(self.posy)) # . move fait bouger l'image du shuriken en fontion abs / ord
            else:                       # vers le haut
                self.posy = -0.5 * 9.81 * ((time.time()-self.time)**2) + self.vit * sin(self.angle) * (time.time()-self.time)
                self.main.move(self.shu, int(self.posx), int(-self.posy)) # - posy car on "remonte" l'axe des ord. (qui est sur tkinter vers le bas)
            self.main.after(20, self.animer_shuriken) # toutes les 20ms on rappelle la fonction animation pour faire bouger le Shuriken

    def afficher_resultat(self):
        """Après la fin du jeu Shurika, affiche le résultat au joueur"""
        self.main.delete(ALL) # Supprime tous ce qui est affiché à l'écran
        if self.level == 1: # level permet de reconnaitre si le shuriken a touché le sol / la cible
            self.main.create_line(150,150,150,620,  width=2, fill='blue')
            self.main.create_text(350,100, text="~~ Shurika ~~", fill="red", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(100,200, text=" S ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(100,300, text=" C ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))                                            # Cette suite de commande représente les écritures
            self.main.create_text(100,400, text=" O ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))                                            # affichées à l'écran, à la fin d'une partie
            self.main.create_text(100,500, text=" R ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(100,600, text=" E ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(600,200, text="Bravo jeune disciple !", fill="purple",font=('Viner Hand ITC', 40, 'bold'))
            self.main.create_text(730,300, text="Vous avez touché la cible, continuez ainsi.", fill="purple",font=('Viner Hand ITC', 40, 'bold'))
            self.main.create_text(600,500, text="Vos points : {}".format(self.point), fill="purple",font=('Viner Hand ITC', 40, 'bold'))
            if self.who == 'red':                self.compteur_rouge = self.compteur_rouge + self.point
            elif self.who == 'blue':                self.compteur_bleu = self.compteur_bleu + self.point
            self.tableau_score() # actualise le tableau
            self.main.after(2000, self.quitter) #après 2 sec, lance la fonction qui ferme la fenetre
        elif self.level ==0: # level permet de reconnaitre si le shuriken a touché le sol / la cible
            self.main.create_line(150,150,150,620,  width=2, fill='blue')
            self.main.create_text(350,100, text="~~ Shurika ~~", fill="red", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(100,200, text=" S ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(100,300, text=" C ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(100,400, text=" O ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(100,500, text=" R ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(100,600, text=" E ", fill="blue", font=('Viner Hand ITC', 60, 'bold'))
            self.main.create_text(600,200, text="Mauvais lancé !", fill="purple",font=('Viner Hand ITC', 40, 'bold'))
            self.main.create_text(730,300, text="Ce n'est pas bon, entrainez vous encore.", fill="purple",font=('Viner Hand ITC', 40, 'bold'))
            self.main.create_text(600,500, text="Votre score : {}".format(self.point), fill="purple",font=('Viner Hand ITC', 40, 'bold'))
            if self.who == 'red':                self.compteur_rouge = self.compteur_rouge + self.point
            elif self.who == 'blue':                self.compteur_bleu = self.compteur_bleu + self.point
            self.tableau_score() # actualise le tableau
            self.main.after(2000, self.quitter) #après 2 sec, lance la fonction qui ferme la fenetre

    def quitter(self):
        """ ferme la fenetre de score affichée"""
        self.FenShurika.destroy()
        self.boss.focus_set()    # remet le focus sur le canevas principal pour autoriser les pions à bouger

# -------------------------------------------------- JEU BLAST -------------------------------------------------- #

    def blast(self,abz,orz):
        self.FenBlast= Toplevel()
        self.FenBlast.title("Bl@st")
        self.jeu=Canvas(self.FenBlast, height=700,width=1100, bg='ivory') # référence du canevas
        self.jeu.pack()
        self.jeu.focus_set()
        self.x=abz
        self.y=orz
        self.ang=0
        self.lb=50
        self.r=20
        self.xb = abz+40
        self.yb = orz
        self.no=5
        if self.who == 'red':
            self.coul='red'
            self.coulb = 'blue'
        elif self.who == 'blue':
            self.coul='blue'
            self.coulb = 'red'
        self.font = PhotoImage(file='blast/font.png')
        self.jeu.create_image(550,350,image=self.font)
        self.yMax = int(self.jeu.cget('height'))
        self.xMax = int(self.jeu.cget('width'))
        self.jeu.bind("<Button-1>",self.click)
        self.jeu.bind("<B1-Motion>",self.calcul)
        self.anim = False           # indicateurs d'animation 
        self.explo = False          #    et d'explosion
        self.mouvement=False
        self.canon(self.x,self.y,self.xb,self.yb)
        self.rand()
        self.FenBlast.mainloop()

    def canon(self,x,y,xb,yb):
        if self.mouvement == True:
            self.jeu.delete(self.bouche,self.corps,self.boulet)
        self.bouche = self.jeu.create_line(x,y,xb,yb, width=10)
        self.corps = self.jeu.create_oval(x-self.r,y-self.r,x+self.r,y+self.r,fill=self.coul)
        self.boulet = self.jeu.create_oval(0,0,0,0,fill=self.coul)

    def rand(self):
        self.cbls=[0,1,2]
        self.cbl=choice(self.cbls)
        if self.cbl==0:
            self.cible(1000,600)
        elif self.cbl==1:
            self.cible(500,300)
        elif self.cbl==2:
            self.cible(250,150)
    
    def cible(self,x4,y4):
        self.x4 = x4
        self.y4 = y4
        self.r2 = 30
        self.cibl = self.jeu.create_rectangle(x4-self.r2,y4-self.r2,x4+self.r2,y4+self.r2,fill=self.coulb)
        
    def orientation(self,ACB):       
        self.xb = int(self.x + self.lb * cos(ACB))
        self.yb = int(self.y - self.lb * sin(ACB))       
        self.canon(self.x, self.y, self.xb, self.yb)
        
        
    def click(self,event):
        self.t1=time.time()
        
    def feu(self,event):
          "tir d'un obus - seulement si le précédent a fini son vol"
          if not (self.anim or self.explo):
              self.anim =True
              # position de départ de l'obus (c'est la bouche du canon) :
              self.jeu.coords(self.boulet, self.xb -5, self.yb -5, self.xb +5, self.yb +5)
              v =10*((time.time())-self.t1)            # vitesse initiale
              # composantes verticale et horizontale de cette vitesse :
              self.vy = -v *sin(self.ACB)
              self.vx = v *cos(self.ACB)
              self.animer_obus()

    def animer_obus(self):
         "animer l'obus (trajectoire balistique)"
         if self.anim:
             self.jeu.move(self.boulet, int(self.vx), int(self.vy))
             c = self.jeu.coords(self.boulet)     # coord. résultantes
             xo, yo = c[0] +5, c[1] +5      # coord. du centre de l'obus
             self.test_obstacle(xo, yo)     # a-t-on atteint un obstacle ?
             self.vy += .4                  # accélération verticale
             self.boss.after(20, self.animer_obus)
         elif self.anim == False and self.touche==False:
             # animation terminée - cacher l'obus et déplacer les canons :
             self.fin_animation()

    def test_obstacle(self, xo, yo):
        if yo >self.yMax or xo <0 or xo >self.xMax:
          self.anim =False
          self.touche=False
          
        if xo < self.x4 +self.r2 and xo > self.x4 -self.r2 \
        and yo < self.y4 +self.r2 and yo > self.y4 -self.r2 :            
            self.anim =False
            self.touche=True
            # dessiner l'explosion de l'obus (cercle jaune) :
            self.explo = self.jeu.create_oval(xo -12, yo -12,xo +12, yo +12, fill ='yellow', width =0)
            print("ok")
            self.jeu.after(150, self.fin)
             
    def fin_animation(self):
     "actions à accomplir lorsque l'obus a terminé sa trajectoire"
     # cacher l'obus (en l'expédiant hors du canevas) :
     self.no=(self.no)-1
     self.jeu.coords(self.boulet, -10, -10, -10, -10)
     print("ok2")
     if self.no==0:
         print("ok3")
         self.fin()
         
    def fin(self):
         "effacer l'explosion ; ré-initaliser l'obus ; gérer le score; ou victoire"
         if self.touche==True:
             self.pts = 100*(self.no+1)
             print(self.pts)
             print("ok4")
             if self.who == 'red': self.compteur_rouge = self.compteur_rouge + self.pts
             elif self.who == 'blue':self.compteur_bleu = self.compteur_bleu + self.pts
             showinfo('Vous avez réussi!, vous marquez des points : ',self.pts)
             self.tableau_score() # actualise le tableau
             self.jeu.after(2000,self.quit)
                  
         else:
             self.pts = -200
             if self.who == 'red': self.compteur_rouge = self.compteur_rouge + self.pts
             elif self.who == 'blue':self.compteur_bleu = self.compteur_bleu + self.pts
             self.jeu.delete(self.explo)    # effacer l'explosion
             self.explo =False               # autoriser un nouveau tir
             showinfo('Vous avez échoué!, vous perdez des points : ',self.pts)
             self.tableau_score() # actualise le tableau
             self.jeu.after(2000,self.quit)

    def quit(self):
        """ ferme la fenetre de score affichée"""
        self.FenBlast.destroy()
        self.boss.focus_set()    # remet le focus sur le canevas principal pour autoriser les pions à bouger
                            
    def calcul(self,event):
        self.x3 = event.x
        self.y3 = event.y
        self.A = (self.x3,self.y3)   #les points A, B et C déterminent respectivement                                                                    # le point A 
        self.B = (self.x3,self.y)                                                               
        self.C = (self.x,self.y)
        self.AC=sqrt((self.x-self.x3)**2 + (self.y-self.y3)**2)   # Formule qui calcul les longueurs des segments du triangle ABC
        self.BC=sqrt((self.x-self.x3)**2)                       # le point B et le point C ont la même ordonnée donc la longueur SB dépend des abscisses
        self.AB=sqrt((self.y-self.y3)**2)
        if self.x==self.x3:
            self.cosACB = 1
        else:
            self.cosACB=(((self.AC)**2 + (self.BC)**2 - (self.AB)**2)/(2*(self.AC)*(self.BC)))
            self.ACB = acos(self.cosACB)#en radians
        self.mouvement=True
        self.orientation(self.ACB)
        self.jeu.bind("<ButtonRelease>",self.feu)
    
                                                                                        ########################
                                                                                        ### --- FONCTION --- ###
                                                                                        ########################

# -------------------------------------------------- JEU PACBOY -------------------------------------------------- #
def initialiser():
    """Initialisation des valeurs  en début de partie"""
    global manche, compteur_rouge, compteur_bleu
    global score_rouge_final, score_bleu_final, dec
    manche,compteur_rouge,compteur_bleu=1,0,0
    score_rouge_final=score_bleu_final=0
    dec=3 # nombre du décompte
    
"""Gestion du déblocage lorsque des obstacles gênent"""
def set_focus(): 
    can.focus_set() # focus sur le canvevas principal (celui qui reçoit les touches du clavier)
    
def sound_debloquer():
    son_bip.play() # joue le son lié à la touche " R " (sert à recommencer une partie)
    can.after(3000, set_focus) # rétablit le focus sur la fenetre après 3s (durée du son)
    
def debloquer(event):
    # si des obstacles bloquent le passage des pions alors utiliser cette commande SHIFT + r soit R #
    compteur_rouge=compteur_bleu=0
    can3.focus_set() # change le focus sur un canevas inutile ainsi le canevas principal ne reçoit plus les évènements du clavier
    son_bip.stop() # arrête le son
    lancement_pacboy(compteur_rouge,compteur_bleu) # relance le jeu
    can.after(500, sound_debloquer) # son de quelques seconde laissant aux joueurs le temps de se préparer
    
""" éléments du décompte """
def sound_decompte():
    """ Ici on souhaite faire un décompte, dec est la variable qui permet de reconnaitre à quel moment du décompte on se situe"""
    global dec
    if dec==3:
        son3.play() # jouer le son 3 
        can3.delete(ALL)  # supprime tout
        can3.create_image(150,202,image=img_three) # affiche un  chiffre 3 
        dec =dec-1 # on passe au 2
    elif dec ==2:
        son2.play() # jouer le son 2
        can3.delete(ALL)
        can3.create_image(150,202,image=img_two)
        dec =dec-1 # on passe au 1 
    elif dec ==1:
        son1.play() # jouer le son 1
        can3.delete(ALL)
        can3.create_image(150,202,image=img_one)
        dec =dec-1 # on passe au 0
    elif dec ==0:
        son_gong.play() # jouer le son du gong = début de la partie
        can3.delete(ALL)
        can3.create_image(150,202,image=img_go)
        can.focus_set() # changement de focus, le canevas principal (celui des pions) reçoit les évènements
        dec = 3 # décompte est remis à 3 pour la prochaine manche
        
def decompte():
    """ crée un décompte qui s'affiche à côté de la grille"""
    can3.focus_set() # Détermine quel widget a le focus et reçoit les évenements clavier
    lancement_pacboy(compteur_rouge,compteur_bleu) # on affiche la partie mais les pions de peuvent pas bouger car ce n'est pas leur widget qui recoit les touches clavier
    for i in range(4):
        can3.after(1000*(i+1), sound_decompte) # lorsque i = 3 les pions peuvent bouger (cf. fonction ci dessus)
        
def lancement_pacboy(CR,CB): # attend 2 paramètres Compteur Rouge et Compteur Bleu
    """Lance les manches du jeu"""
    global temps_depart
    temps_depart=time.time()            # temps depuis janvier 1970 jusqu'à maintenant (Le chrono. démarre donc dans notre jeu)
    can.delete(ALL)                             # on supprime tout , pour rafraîchir le canevas avec de nouveaux éléments
    son_game.stop()                           # on arrete le son du jeu, utile lorsque le joueur recommence le jeu
    """RAPPEL DE L'ORDRE DES PARAMETRES : boss,compteur rouge, compteur bleu, TIME"""
    pacboy = Pacboy(can,CR,CB,temps_depart) # appelle de la classe Pacboy (celle qui contient donc le jeu)
    son_game.play() # joue le son du jeu 

# --------------------------------------------------  MENU  -------------------------------------------------- #
def creation_menu():
    menuprincipal = Menu(fen1)

    menu1 = Menu(menuprincipal, tearoff=0)
    menu1.add_command(label="Nouvelle Partie", command=message)
    menu1.add_command(label="Quitter", command=fen1.destroy)
    menuprincipal.add_cascade(label="Jeu", menu=menu1)

    menu2 = Menu(menuprincipal, tearoff=0)
    menu2.add_command(label="A propos", command=alert)
    menu2.add_command(label="Règles - Pacboy",command=regles_pacboy)
    menu2.add_command(label="Règles - Shurika",command=regles_shuriken)
    menu2.add_command(label="Règles - Blast",command=regles_blast)
    menuprincipal.add_cascade(label="Aide", menu=menu2)

    fen1.config(menu=menuprincipal)
    
def message():
    # demande oui ou non, si oui continuer si non ne rien faire #
    if askyesno('Nouvelle Partie', 'Êtes vous sûr ?'):
        initialiser()
        decompte()
        
def alert():
    # info #
    showinfo("A propos", "Jeu : Pacboy\n<Projet ISN>\nAnnées 2015 - 2016\nAuteurs : MAGNI Lorenzo , DIPOKO William")                                                                                                                 
    
def regles_pacboy():
    # Toplevel = une fenêtre affichée séparément, au premier plan #
    principe = Toplevel(bg ='ivory', height = 400)
    principe.title('REGLES PACBOY')
    CanPacb = Canvas(principe, width=1000, height=600)
    CanPacb.pack()
    CanPacb.create_image(0,0, image = ReglePac, anchor=NW)
    
def regles_shuriken():
    """ fonction lié au menu, affiche les règles du jeu shurika (by Lorenzo)"""
    top = Toplevel()
    top.title('REGLES SHURIKA') # titre de la fenêtre
    CanRegle= Canvas(top, width=1000, height=500) # on crée un canevas dans cette fenetre
    CanRegle.pack()
    CanRegle.create_image(0,0, image = RegleShu, anchor=NW) # on y affiche l'image que j'ai crée et qui donne les instruction du jeu

def regles_blast():
    mess = Toplevel()
    mess.title('REGLES BLAST')
    CanRules = Canvas(mess,width=1000,height=500)
    CanRules.pack()
    CanRules.create_image(0,0, image = RegleBla, anchor=NW)
    
    
                                                                                        #########################
                                                                                        ### --- PROGRAMME --- ###
                                                                                        #########################
    
# -------------------------------------------------- Création de la fenêtre + menu avec les commandes  -------------------------------------------------- #
fen1 = Tk()
fen1.title('PacBoy')
creation_menu()

pygame.init() # initialisation de pygame (permet d'utiliser les commandes de pygame)

# -------------------------------------------------- Chargement des sons --------------------------------------------------  #
son1 = pygame.mixer.Sound("son/1.wav")
son2 = pygame.mixer.Sound("son/2.wav")
son3 = pygame.mixer.Sound("son/3.wav")
son_gong = pygame.mixer.Sound("son/gong.wav")
son_bip = pygame.mixer.Sound("son/321.wav")
son_game = pygame.mixer.Sound("son/jeu.wav")
son_pastillespe = pygame.mixer.Sound("son/pastillespe.wav")
son_bloque = pygame.mixer.Sound("son/bloc.wav")

# -------------------------------------------------- Chargement des images  -------------------------------------------------- #
redpion = PhotoImage(file ='imgs/p_rouge.png')
bluepion = PhotoImage(file ='imgs/p_bleu.png')
yellowpion = PhotoImage(file ='imgs/jaune.png')
purplepion = PhotoImage(file ='imgs/purple.png')
img_one=PhotoImage(file="imgs/one.png")
img_two=PhotoImage(file="imgs/two.png")
img_three=PhotoImage(file="imgs/three.png")
img_go=PhotoImage(file="imgs/go.png")
ReglePac =PhotoImage(file="imgs/pacboy_regle.png")
RegleShu = PhotoImage(file="imgs/shurika_regles.png")
RegleBla=PhotoImage(file="imgs/blast_regles.png")

#  -------------------------------------------------- Creation canevas -------------------------------------------------- #
can = Canvas(fen1, height=705, width=1010, bg = 'ivory') # canevas principal avec les pions ! 
can.pack(side=RIGHT)
can2 = Canvas(fen1, height= 300, width=300,bg ='#75ff23') # canevas secondaire avec le score !
can2.pack(side=TOP)
can3 = Canvas(fen1, height=405, width=300) # canevas qui affiche le décompte !
can3.pack(side=BOTTOM)

can.bind("<KeyPress-R>",debloquer) #  Touche pour relancer la manche en cours R majuscule

# -------------------------------------------------- Début de partie : initialisation des valeurs + affichage du jeu avec le décompte -------------------------------------------------- #
initialiser()
decompte()

# -------------------------------------------------- Fin -------------------------------------------------- #
fen1.mainloop()
