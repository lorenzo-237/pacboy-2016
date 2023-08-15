from tkinter import *

def afficher():
    nbc = choix.get()
    print(nbc)

fen = Tk()



Alkyles = [None, "Méthyle","Ethyle","Propyle","Butyle","Pentyle"]
Carbones = [None, 1,2,3,4,5]
choix = StringVar()

txt = Label(fen, text='Choisissez votre alkyle', fg='red', font=('Calibri',15,'bold'))
txt.grid()

for n in range(1,len(Alkyles)):
    bout = Radiobutton(fen, text = Alkyles[n], variable=choix, value=Carbones[n], command=afficher)
    bout.grid(row=1, column=(n-1), padx=40)

bouton = Button(fen, text='VALIDER')
bouton.grid(row=2, column=2, pady=10)

fen.mainloop()
