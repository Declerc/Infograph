# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
import createGraph
def alert():
    showinfo("alerte", "Ca marche !")

Fenetre = Tk()
Fenetre.title("Infograph")
Fenetre['bg'] = 'grey'
Fenetre.geometry('1000x600')


 


Menubar = Menu(Fenetre)

Menu1 = Menu(Menubar, tearoff=0)
Menu1.add_command(label="Créer", command=creat(nb))
Menu1.add_command(label="Editer", command=alert)
Menu1.add_separator()
Menu1.add_command(label="Quitter", command=Fenetre.quit)
Menubar.add_cascade(label="Fichier", menu=Menu1)

Menu2 = Menu(Menubar, tearoff=0)
Menu2.add_command(label="Couper", command=alert)
Menu2.add_command(label="Copier", command=alert)
Menu2.add_command(label="Coller", command=alert)
Menubar.add_cascade(label="Editer", menu=Menu2)

Menu3 = Menu(Menubar, tearoff=0)
Menu3.add_command(label="A propos", command=alert)
Menubar.add_cascade(label="Fenêtre", menu=Menu3)

Menu4 = Menu(Menubar, tearoff=0)
Menu4.add_command(label="Bellman", command=alert)
Menu4.add_command(label="Ford", command=alert)
Menu4.add_command(label="Dijkstra", command=alert)
Menu4.add_separator()
Menu4.add_command(label="Matrice", command=alert)
Menubar.add_cascade(label="Algorithmes", menu=Menu4)

Menu5 = Menu(Menubar, tearoff=0)
Menu5.add_command(label="A propos", command=alert)
Menubar.add_cascade(label="Aide", menu=Menu5)

Fenetre.config(menu=Menubar)

fWidth= Fenetre.winfo_screenwidth()
MenuBouton = Canvas(Fenetre, width=fWidth, height=25, background='white')
#MenuBouton.pack(side = TOP)

Fenetre.minsize(700,300)

Fenetre.mainloop()