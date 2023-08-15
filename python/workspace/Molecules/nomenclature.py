from tkinter import *

class Nomenclature:
    def __init__(self,boss):
        self.boss=boss
        boss.bind("<Button-1>", self.ou_est_le_clic)
        # initialisation des compteurs
        self.NBC,self.NBH=0,0
        self.NBALKYLE,self.NBGROUPE, self.SAVALKYLE= 0,0,0
        self.POSALKYLE = []
        self.ALCARBONE = []
        # chargement des images
        self.carbone = PhotoImage(file ="atomes/carbone.png")
        self.hydrogene = PhotoImage(file ="atomes/hydrogene.png")
        self.oxygene = PhotoImage(file ="atomes/oxygene.png")
        self.amine = PhotoImage(file ="atomes/amine.png")
        self.alkyle = PhotoImage(file ="atomes/alkyle.png")
        self.alcool = PhotoImage(file ="atomes/alcool.png")
        self.aldehyde = PhotoImage(file ="atomes/aldehyde.png")
        self.cetone = PhotoImage(file ="atomes/cetone.png")
        self.acide = PhotoImage(file ="atomes/acide.png")
        self.ester = PhotoImage(file ="atomes/ester.png")
        self.amide = PhotoImage(file ="atomes/amide.png")
        self.alcene = PhotoImage(file ="atomes/alcene.png")
        self.posalkyle = PhotoImage(file ="imgs/posalkyle.png")
        self.posalcool = PhotoImage(file ="imgs/posalcool.png")
        self.poscetone = PhotoImage(file ="imgs/poscetone.png")
        Nomenclature.lancement(self)
        Nomenclature.creation_menu(self)
        
    def lancement(self):
        self.boss.delete(ALL)
        Nomenclature.text(self)
        Nomenclature.create_atomes(self)
        Nomenclature.create_groupes(self)
        Nomenclature.create_pos(self)
    
    def text(self):
        self.TXTC = self.boss.create_text(200, 100, text="C : {0}".format(self.NBC), fill = 'blue', font=('Helvetica', 10, 'bold'))
        self.TXTINFO = self.boss.create_text(150, 220, text="Choisissez le nombre de carbone\nUNIQUEMENT présent dans \nla chaîne principale", fill = 'blue', font=('Helvetica', 12, 'italic'))
        self.TXTALKYLE = self.boss.create_text(600, 100, tex= "Nombre d'alkyle(s) : {0}".format(self.NBALKYLE), fill='blue', font=('Helvetica', 10, 'bold'))
        self.TXTALCOOL = None 
        self.TXTALDEHYDE = None 
        self.TXTCETONE = None 
        self.TXTACIDE = None 
        self.TXTESTER = None 
        self.TXTAMINE =None 
        self.TXTAMIDE = None 
        self.boss.create_text(100, 35, text="Atomes", fill='red', font=('Calibri', 20, 'bold'))
        self.boss.create_text(600, 35, text="Groupes \nCaractéristiques", fill='red', font=('Calibri', 20, 'bold'))
        self.boss.create_text(900, 35, text="Positions \nsur la chaîne", fill='red', font=('Calibri', 20, 'bold'))
        self.boss.create_line(5,0,5,700, fill= 'black', width=5) # séparateur
        self.boss.create_line(400,0,400,700, fill= 'black', width=5) # séparateur
        self.boss.create_line(800,0,800,700, fill= 'black', width=5) # séparateur
        self.boss.create_line(1195,0,1195,700, fill= 'black', width=5) # séparateur

    # AJOUT DES ATOMES
    def add_carbone(self,event):
        self.boss.delete(self.TXTC)
        self.NBC+= 1
        self.TXTC = self.boss.create_text(200, 100, text="C : {0}".format(self.NBC), fill = 'blue', font=('Helvetica', 10, 'bold'))

    # AJOUT DES GROUPES CARACTERISTIQUES
    def add_alkyle(self,event):
        self.boss.delete(self.TXTALKYLE)
        self.POSALKYLE = []
        self.NBALKYLE += 1
        self.SAVALKYLE = self.NBALKYLE
        self.TXTALKYLE = self.boss.create_text(600, 100, tex= "Nombre d'alkyle(s) : {0}".format(self.NBALKYLE), fill='blue', font=('Helvetica', 10, 'bold'))

    def add_alcool(self,event):
        self.boss.delete(self.TXTALCOOL)
        if self.NBGROUPE < 1:
            self.NBGROUPE+=1
            self.TXTALCOOL = self.boss.create_text(600, 160, text="OH : {0}".format(self.NBGROUPE), fill = 'blue', font=('Helvetica', 10, 'bold'))
        else:
            self.TXTALCOOL = self.boss.create_text(600, 160, text="Erreure 1", fill = 'blue', font=('Helvetica', 10, 'bold'))
            self.NBGROUPE = 0
            self.boss.after(500, self.lancement)

    def add_aldehyde(self,event):
        self.boss.delete(self.TXTALDEHYDE)
        if self.NBGROUPE < 1:
            self.NBGROUPE += 1
            self.TXTALDEHYDE = self.boss.create_text(610, 220, tex= "C = O (bout de chaîne) : {0}".format(self.NBGROUPE), fill='blue', font=('Helvetica', 10, 'bold'))
        else:
            self.TXTALDEHYDE = self.boss.create_text(610, 220, text="Erreure 2", fill = 'blue', font=('Helvetica', 10, 'bold'))
            self.NBGROUPE = 0
            self.boss.after(500, self.lancement)

    def add_cetone(self,event):
        self.boss.delete(self.TXTCETONE)
        if self.NBGROUPE < 1:
            self.NBGROUPE += 1
            self.TXTCETONE = self.boss.create_text(610, 280, tex= "C = O (milieu de chaîne) : {0}".format(self.NBGROUPE), fill='blue', font=('Helvetica', 10, 'bold'))
        else:
            self.TXTCETONE = self.boss.create_text(610, 280, text="Erreure 3", fill = 'blue', font=('Helvetica', 10, 'bold'))
            self.NBGROUPE = 0
            self.boss.after(500, self.lancement)
            
    def add_acide(self,event):
        self.boss.delete(self.TXTACIDE)
        if self.NBGROUPE < 1:
            self.NBGROUPE+=1
            self.POSACIDE=1
            self.TXTACIDE = self.boss.create_text(600, 340, text= """C = O  :   {0}
|
OH""".format(self.NBGROUPE), fill='blue', font=('Helvetica', 10, 'bold'))
        else:
            self.TXTACIDE = self.boss.create_text(600, 340, text="Erreure 4", fill='blue', font=('Helvetica', 10, 'bold'))
            self.NBGROUPE = 0
            self.POSACIDE = 0
            self.boss.after(500, self.lancement)
            
    def add_ester(self,event):
        self.boss.delete(self.TXTESTER)
        if self.NBGROUPE < 1:
            self.NBGROUPE += 1
            self.POSESTER = 1
            self.TXTESTER = self.boss.create_text(600, 400, text= """C = O  :   {0}
|
O _""".format(self.NBGROUPE), fill='blue', font=('Helvetica', 10, 'bold'))
        else:
            self.TXTESTER = self.boss.create_text(600, 400, text="Erreure 5", fill='blue', font=('Helvetica', 10, 'bold'))
            self.NBGROUPE= 0
            self.POSESTER = 0
            self.boss.after(500, self.lancement)            

    def add_amine(self,event):
        self.boss.delete(self.TXTAMINE)
        if self.NBGROUPE < 1:
            self.NBGROUPE += 1
            self.TXTAMINE = self.boss.create_text(600, 460, text="N : {0}".format(self.NBGROUPE), fill = 'blue', font=('Helvetica', 10, 'bold'))
        else:
            self.TXTAMINE = self.boss.create_text(600, 460, text="Erreure 6", fill = 'blue', font=('Helvetica', 10, 'bold'))
            self.NBGROUPE = 0
            self.boss.after(500, self.lancement)
            
    def add_amide(self,event):
        self.boss.delete(self.TXTAMIDE)
        if self.NBGROUPE < 1:
            self.NBGROUPE += 1
            self.TXTAMIDE = self.boss.create_text(600, 520, text= """C = O  :   {0}
|
NH _""".format(self.NBGROUPE), fill='blue', font=('Helvetica', 10, 'bold'))
        else:
            self.TXTAMIDE = self.boss.create_text(600, 520, text="Erreure 7", fill = 'blue', font=('Helvetica', 10, 'bold'))
            self.NBGROUPE = 0
            self.boss.after(500, self.lancement)

    def add_alcene(self,event):
        self.boss.delete(self.TXTALCENE)

    # CREATION DES IMAGES A L'ECRAN     
    def create_atomes(self):
        Atomes = [None,"carbone"]
        x,y = 70, 100
        for i in range(1,len(Atomes)):
            # tag_bind(<nom du tag>, <nom event>, <fonction callback>)
            if i ==1:
                self.boss.create_image(x, y, image=self.carbone, tag=Atomes[i])
                self.boss.tag_bind(Atomes[i], "<Button-1>",self.add_carbone)

    def create_groupes(self):
        Type = [None,"alkyle","alcool","aldehyde","cetone","acide","ester","amine","amide","alcene"]
        x,y = 470, 100
        for i in range(1, len(Type)):
            if i ==1:
                self.boss.create_image(x,y, image=self.alkyle, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_alkyle)
            elif i ==2:
                self.boss.create_image(x,y+60, image=self.alcool, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_alcool)
            elif i ==3:
                self.boss.create_image(x,y+120, image=self.aldehyde, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_aldehyde)
            elif i ==4:
                self.boss.create_image(x,y+180, image=self.cetone, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_cetone)
            elif i ==5:
                self.boss.create_image(x,y+240, image=self.acide, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_acide)
            elif i ==6:
                self.boss.create_image(x,y+300, image=self.ester, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_ester)
            elif i == 7:
                self.boss.create_image(x, y+360, image=self.amine, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_amine)
            elif i ==8:
                self.boss.create_image(x,y+420, image=self.amide, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_amide)
            elif i ==9:
                self.boss.create_image(x,y+480, image=self.alcene, tag=Type[i])
                self.boss.tag_bind(Type[i], "<Button-1>", self.add_alcene)

    def create_pos(self):
        x, y = 900, 150
        self.boss.create_image(x, y, image=self.posalkyle)
        self.boss.create_image(x+200, y, image=self.posalcool)
        self.boss.create_image(x, y+150, image=self.poscetone)
        
    # GESTION DES POSITIONS
    def valider(self):
        self.info.destroy()
        if self.par == 1:
            self.SAVALKYLE -= 1
            self.POSALKYLE.append(self.saisir.get())
            print(self.saisir.get())
            if self.SAVALKYLE > 0:
                self.boss.after(500, self.info_alkyle)
            else: self.SAVALKYLE = 0
        elif self.par == 2:
            None
        elif self.par == 3:
            None
        self.lancement()
                            
    def afficher(self):
        txt = Label(self.info, text='Choisir la position : ', fg='yellow', bg='navy', font=('Calibri',15,'bold'))
        txt.grid(row=2, column=1)
        self.saisir = StringVar()
        self.saisir.set('Chiffre')
        self.saisie = Entry(self.info, textvariable=self.saisir, width = 30, font="Arial 13")
        self.saisie.grid(row=2, column=2, pady=10)
        
    def info_alkyle(self):
        self.info = Toplevel(bg='navy')
        if self.par == 1:
            if self.SAVALKYLE ==0:
                Label(self.info, text="Votre nombre d'alkyle(s) est de 0.\nAugmentez le pour pouvoir choisir leur position", fg='yellow', bg='navy', font=('Calibri',15,'bold')).pack()
                self.boss.after(2000, self.info.destroy)
            else:
                Alkyles = [None, "Méthyle","Ethyle","Propyle","Butyle","Pentyle"]
                Carbones = [None, 1,2,3,4,5]
                self.choix = StringVar()
                txt = Label(self.info, text='Choisissez votre alkyle', fg='yellow', bg='navy', font=('Calibri',15,'bold'))
                txt.grid()
                for n in range(1,len(Alkyles)):
                    bout = Radiobutton(self.info, text = Alkyles[n], font=('Calibri',12,'bold'), variable=self.choix, value=Carbones[n], command=self.afficher)
                    bout.grid(row=1, column=(n-1), padx=40)
                bouton = Button(self.info, text='VALIDER', command=self.valider)
                bouton.grid(row=3, column=1, pady=10)
                bouton = Button(self.info, text='ANNULER', command=self.info.destroy)
                bouton.grid(row=3, column=3, pady=10)
        elif self.par == 2:
            None
        elif self.par == 3:
            None

    # EVENEMENT

    def ou_est_le_clic(self, event):
        self.x, self.y = event.x, event.y
        print(self.x, self.y)
        if 850 <= self.x <= 950 and 100 <= self.y <= 200:
            self.par = 1
            self.info_alkyle()
        elif 1050 <= self.x <= 1150 and 100 <= self.y <= 200:
            self.par = 2
            self.info_alkyle()
            
        
    # CREATION DU MENU
    def creation_menu(self):
        main_menu = Menu(fen)
        menu1 = Menu(main_menu, tearoff = 0)
        menu1.add_command(label='Aide', command=self.info_alkyle)
        main_menu.add_cascade(label='A propos', menu=menu1)
        fen.config(menu=main_menu)
        

        

# -- Programme -- #

fen = Tk()
can = Canvas(fen, height=700, width=1200, bg ='ivory')
can.pack()
Nomen = Nomenclature(can)
fen.mainloop()
