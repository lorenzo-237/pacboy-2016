# Exo sur Canevas et les évènements

from tkinter import *
from random import *

# --- Fonctions --- #

def draw_line():
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)

    # modif. des coord. de la ligne suivante
    y2,y1 = y2+10, y1-10

def change_color():
    global coul
    LIST = ["purple","cyan","maroon","green","red","blue","orange","yellow"]
    r = randrange(8)
    coul = LIST[r]

# --- Programme --- #

x1, y1, x2, y2 = 10, 190, 190,  10  # coord. ligne
coul = "dark green"                 # couleur ligne

# Création du widget principal
fen1 = Tk()

# Création des widgets secondaires
can1 = Canvas(fen1, bg="dark grey", height=200, width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=draw_line)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=change_color)
bou3.pack()

fen1.mainloop()
fen1.destroy()
