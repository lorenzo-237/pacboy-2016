#!/usr/bin/python
from tkinter import *
from random import randint
from tkinter.messagebox import *

def Liste():
    global L
    L=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
    M=[1,2,3,4,5,6,7,8]
    for i in range(0,8):
        k=M.pop(randint(0,len(M)-1))
        for i in range(0,2):
            j,h=randint(0,3),randint(0,3)
            while L[j][h]!=0:
                j,h=randint(0,3),randint(0,3)
            L[j][h]=k

def condition():
    for j in range(4):
        if x==0 and y ==j:
                 prem_colonne[j]= can.create_image(0,100*j, anchor=NW, image=fond)
        elif x==1 and y ==j:
                 deux_colonne[j]= can.create_image(100*x,100*j, anchor=NW, image=fond)
        elif x==2 and y ==j:
                 trois_colonne[j]= can.create_image(100*x,100*j, anchor=NW, image=fond)
        elif x==3 and y ==j :
                 quat_colonne[j]= can.create_image(100*x,100*j, anchor=NW, image=fond)
def condition2():
    for j in range(4):
            if xx==0 and yy ==j:
                     prem_colonne[j]= can.create_image(0,100*j, anchor=NW, image=fond)
            elif xx==1 and yy ==j:
                     deux_colonne[j]= can.create_image(100*xx,100*j, anchor=NW, image=fond)
            elif xx==2 and yy ==j:
                     trois_colonne[j]= can.create_image(100*xx,100*j, anchor=NW, image=fond)
            elif xx==3 and yy ==j :
                     quat_colonne[j]= can.create_image(100*xx,100*j, anchor=NW, image=fond)

def identique():
    if (xx != x and yy != y or xx == x and yy != y or xx != x and yy==y) \
       and L[x][y] == L[xx][yy]:
        L[x][y]=" "
        L[xx][yy]=" "
        condition()
        condition2()
        # verifie si la partie est terminÃ©e
        fin()
    elif (xx ==x and yy ==y) and L[x][y] == L[xx][yy]:
        can.delete(item1)
        can.delete(item2)
    elif (xx == x and yy != y) or (xx != x and yy==y) or (xx!=x and yy!=y):
        can.delete(item1)
        can.delete(item2)
"""
1er2eme3eme4eme_colonne sont des dictionnaires.
Le premier correspond Ã  la premiÃ¨re colonne de la grille et ainsi de suite
chaque case a un indice [i] , [0] = 1ere case , [1] = 2eme case , ...
"""
def grille():
    global prem_colonne,deux_colonne,trois_colonne,quat_colonne
    # ce sont des dictionnaires on peut ainsi donner un indice Ã  une variable
    prem_colonne,deux_colonne,trois_colonne,quat_colonne={},{},{},{}
    for i in range(4):
        for j in range(4):
            prem_colonne[i]= can.create_image(0,j*100, anchor=NW, image=base)
            deux_colonne[i]= can.create_image(100,j*100, anchor=NW, image=base)
            trois_colonne[i]= can.create_image(200,j*100, anchor=NW, image=base)
            quat_colonne[i]= can.create_image(300,j*100, anchor=NW, image=base)

def souris(event):
    global clic
    global x,y,fond1,item1
    global xx,yy,fond2,item2
    if clic ==1:
        x, y,=event.x//100, event.y//100
        if L[x][y] != " ":
            fond1= PhotoImage(file="img"+str(L[x][y])+".gif")
            item1 = can.create_image(100*x, 100*y, anchor=NW, image=fond1)
            clic=2
    else:
       xx, yy=event.x//100 , event.y//100
       if L[xx][yy] != " ":
          fond2=PhotoImage(file="img"+str(L[xx][yy])+".gif")
          item2 = can.create_image(100*xx, 100*yy,anchor=NW,image=fond2)
          clic=1
          # reactualise le canvas apres 500 millisecondes le temps de verifier si les cases sont identiques
          can.after(500,identique)

def fin():
    if L==[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]:
        showinfo("FIN DE PARTIE","Partie terminÃ©e ! BRAVO")

fen=Tk()
can= Canvas(fen, width=400, height=400, bg='white')
can.pack(side=TOP,padx=5, pady=5)
base = PhotoImage(file='img0.gif')
fond = PhotoImage(file='img .gif')
grille()
Liste()
clic =1
can.bind('<ButtonPress-1>', souris)
fen.mainloop()


