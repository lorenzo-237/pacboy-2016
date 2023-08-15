from tkinter import *
from math import *
import time

class Shuriken:
    """ Reprend la classe self et, définit les évènements, les conditions pour que le jeu fonctionne """
    def __init__(self, boss, x, y):
        self.boss=boss # référence du canevas
        self.x=x # coords initiales 
        self.y=y 
        boss.delete(ALL) # supprime tout pour réactualiser
        """ creation du fond du canevas """
        self.photo = PhotoImage(file='shurika/fond.png')
        boss.create_image(0, 0, image=self.photo, anchor=NW)
        """ creation de l'image d'un shuriken """
        self.img = PhotoImage(file='shurika/shuriken.png')
        self.shu =  boss.create_image(x,y, image=self.img)
        # retrouver la hauteur du canevas (cad l'ord. maximale)
        self.yMax = int(boss.cget('height'))
        # retrouver la largeur du canevas (cad l'abs. maximale)
        self.xMax = int(boss.cget('width'))
        """ Attente des évènements """
        boss.bind("<Button-1>", self.mouse_down)             # pression sur le bouton gauche de la souris
        boss.bind("<Button1-Motion>", self.mouse_move)   # mouvement de la souris une fois le bouton maintenu
        self.anim = False       # interrupteur d'animation (gère l'arrêt et le debut du mouvement)
        """ Chargment des images du shuriken (plusieurs images pour gérer la rotation de l'objet) """
        shuriken0= PhotoImage(file='shurika/shuriken0.png')
        shuriken1= PhotoImage(file='shurika/shuriken1.png')
        shuriken2= PhotoImage(file='shurika/shuriken2.png')
        shuriken3= PhotoImage(file='shurika/shuriken3.png')
        shuriken4= PhotoImage(file='shurika/shuriken4.png')
        shuriken5= PhotoImage(file='shurika/shuriken5.png')
        self.DicoPos = {0:shuriken0,1:shuriken1,2:shuriken2,3:shuriken3,4:shuriken4,5:shuriken5} # sauvegarde ces images dans un dictionnaire
        Shuriken.cibles(self)
        
    def CalculCosAngle(self,abscisseS, ordonneeS): # attend 2 paramètres les coords du points S (S comme Shuriken)
        """ Formule d'Al Kashi pour trouver le cos d'un angle
        Soit A un point de coord fixe, B un point d'abscisse fixe et S le point représentant les coords du Shuriken"""
        self.pA = (self.x,self.y)                                                                      # le point A 
        self.pB = (600,ordonneeS)                                                               # le point B
        self.segSA=sqrt((abscisseS-self.x)**2 + (ordonneeS-self.y)**2) 
        self.segSB=sqrt((abscisseS-600)**2)                                             # Formule qui calcul les longueurs des segments du triangle ABS
        self.segAB=sqrt((self.x-600)**2 + (self.y-ordonneeS)**2)
        self.cosangleASB= (-(self.segAB)**2+(self.segSA)**2+(self.segSB)**2)/(2*(self.segSA)*(self.segSB))
        # Formule d'Al Kashi 
        
    def cibles(self):
        """ Stock dans des listes les coords occupées par les cibles du jeu """
        S = [1200,1300]                                                                # intervalle sur l'axe des abs. occupé par les cibles
        LY = [[498, 599],[398, 499],[298, 399],[198, 299],[98, 199],[0, 100]] # intervalles sur l'axe des ord. occupés par les cibles
        self.LX = []
        self.Cible = {} # dictionnaire qui regroupe les listes de l'axe des ord.
        for i in range(S[0],S[1]):
            self.LX.append(i) # on ajoute toutes les valeurs entre l'intervalle 
        for n in range(6):
            Sav = [] # liste pour sauvegarder qui sera ajouter au dictionnaire
            for i in range(LY[n][0], LY[n][1]):
                Sav.append(i) # on ajoute toutes les valeurs entre les intervalles 
            self.Cible[n]= Sav  # on ajoute la liste formée au dictionnaire puis on recommence la boucle

    def mouse_down(self,event):
        """ pression du bouton """ 
        self.x1, self.y1 = event.x, event.y                               # coords du clic effectué
        self.item = self.boss.find_closest(self.x1, self.y1)  # renvoie la référence du dessin le plus proche
        self.boss.lift(self.item)                                             # fait passer le dessin à l'avant-plan
        
    def mouse_move(self,event):
        """ le bouton est maintenu et la souris bouge """
        self.x2, self.y2 = event.x, event.y                             # coords de la souris à chaque mouvement de celle-ci
        if self.x2 <= 320 and self.y2 <= 590:                       # conditions qui fixent une zone pour déplacer le Shuriken
            self.CalculCosAngle(self.x2, self.y2)  # calcul le cos de l'angle qui nous interresse
            dx, dy = self.x2-self.x1, self.y2-self.y1   # coords de déplacement de l'objet sur les deux axes
            try:
                self.boss.move(self.item, dx, dy)     # la souris est mise en mouvement et l'objet se déplace à chaque fois de (dx, dy)
                self.x1, self.y1 = self.x2, self.y2 # l'objet a été déplacé donc ses coords ont changés
                self.boss.bind("<Button1-ButtonRelease>", self.mouse_up) # relâchement du bouton gauche
            except:
                #print("Il faut cliquer sur le Shuriken pas sur le décors")
                None
                
    def mouse_up(self,event):
        """ le bouton a été relâché """
        if not self.anim: # si l'interrupteur : OFF 
            self.anim = True # interrupteur : ON
            self.time=time.time() # lancement du chrono. (pour le temps)
            """ Définition de la force du lancé """
            if 150<self.x2<200:
                self.vit = 5+self.y2/115
            elif 100<self.x2<150:                                                   # ces conditions fixent la vitesse en fonction
                self.vit = 10+self.y2/110                                           # des coords (x,y) de l'objet au moment du
            else:                                                                               # relâchement du clic gauche
                self.vit=15+self.y2/105
            self.n=0    # variable qui permet dans la fonction animation de changer l'image à chaque mouvement et donner l'effet de rotation
            self.angle = acos(self.cosangleASB) # arc cos de l'angle pour retrouver la valeur de l'angle (ici en RADIAN)
            self.animer_shuriken() # appelle la fonction qui lancement l'animation du Shuriken (voir plus bas)

    """ les trois prochaines fonctions se répètents à chaque mouvement car elles sont appelées dans la fonction animation """
    
    def verifier_sol(self):
        """ verifier si le Shuriken atteint le sol (le bas du canevas) """
        c = tuple(self.boss.coords(self.shu))        # dans un tuple on stock les coords du shuriken à chaque mouvement
        try:
            self.x0, self.y0 = c[0], c[1]   # les coords (x,y) du shuriken sont dans le tuple donc on les attribue une variable pour les réutiliser simplement
            if self.y0+60 > self.yMax or self.x0 > self.xMax: # si les coords. sont proche du bord (à 60pixels près pour l'ord. max.)
                self.anim=False     # interrupteur : OFF , arrêt de l'animation
                print("Mauvais lancé ! Reprenez l'entrainement !")
        except:
            """ il peut y avoir une erreur si l'utilisateur appuit la touche pour recommencer (R) alors que le Shuriken est encore en mouvement.
            Donc permet d'afficher "proprement" ce qui ce passe à l'utilisateur """
            print("PARTIE ANNULEE - RESTART AUTO")
            self.anim=False 
            
    def verifier_cible(self):
        """ verifier la zone où le Shuriken est arrivé pour attribuer les points """
        for h in range(len(self.Cible)):                                        # on rappelles que les coords sont stockers
            if (self.x0 in self.LX and self.y0 in self.Cible[h]):# on cherche dans quelle liste se trouve les coords. du Shuriken (donc la cible où il se trouve)
                self.point = h*100 # une fois trouvée, on calcul les points grâce a la zone où se trouve le Shuriken
                self.anim=False # interrupteur : OFF
                self.boss.delete(self.shu)
                self.shu = self.boss.create_image(self.x0, self.y0, image = self.img)
                print("Bravo Ninja ! {} points pour vous ! Continuez ainsi ".format(self.point))
                
    def rotation(self):
        """ gestion de la rotation du shuriken """
        self.boss.delete(self.shu) # on supprime l'ancien shuriken
        self.shu =self.boss.create_image(self.x0, self.y0, image=self.DicoPos[self.n])
        # on réaffiche un nouveau grâce à self.n qui est incrémenté dans la fonction animation (ci-dessous) 
            
    def animer_shuriken(self):
        self.verifier_sol()
        self.verifier_cible()
        if self.anim: # si interrupteur : ON , début animation
            self.posx = self.vit * cos(self.angle) *(time.time()-self.time) # équation horaire x(t)
            self.rotation() 
            self.n=self.n+1 # changement de la prochaine image dans la fonction rotation qui sera "re-appeller"
            """ il n'y a que 6 image (img0 - img 5) donc une fois qu'on a afficher l'img5 on remet a 0 pour afficher l'img0 (ainsi de suite) """
            if self.n==6: self.n=0
            """ Conditions qui déterminent si le shuriken est orienté vers le bas ou vers le haut. L'équation horaire y(t) diffère alors
            car on rappelle que sur tkinter l'axe des ord. est vers le bas.
            Shuriken orienté vers le bas : le champs de pesanteur est dans le même sens du mouvement
            Shuriken orienté vers le haut : le champs de pesanteur est dans le sens contraire du mouvement"""
            if self.y2-self.y < 0: # vers le bas 
                self.posy = 0.5 * 9.81 * ((time.time()-self.time)**2) + self.vit * sin(self.angle) * (time.time()-self.time)
                self.boss.move(self.shu, int(self.posx), int(self.posy))
            else:                       # vers le haut
                self.posy = -0.5 * 9.81 * ((time.time()-self.time)**2) + self.vit * sin(self.angle) * (time.time()-self.time)
                self.boss.move(self.shu, int(self.posx), int(-self.posy)) # - posy car on "remonte" l'axe des ord. (qui est sur tkinter vers le bas)
            self.boss.after(20, self.animer_shuriken) # toutes les 20ms on rappelle la fonction animation pour faire bouger le Shuriken
            

### --- FONCTION --- ###
            
def game():
    """ Début du jeu """
    ninja = Shuriken(can, 200,500)
    
def start(event):
    """ permet de recommencer losqu'on appuit R (Maj) """
    game()

### --- PROGRAME --- ###
    
fen = Tk()
fen.title("Shurika")

can=Canvas(fen, height=650,width=1300)
can.pack()
can.focus_set() # détermine quel canevas a le focus et reçoit les évènements clavier
can.bind("<KeyPress-R>", start) # recommencer avec R 

game() # lancement du jeu (automatique quand on ouvre le programme)

# FIN #
fen.mainloop()
