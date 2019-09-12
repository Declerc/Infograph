# coding: utf-8

from tkinter import * 
from tkinter import ttk
import createGraph
def alert():
    showinfo("alerte", "Ca marche !")

Fenetre = Tk()
Fenetre.title("Infograph")
Fenetre['bg'] = 'grey'
Fenetre.geometry('1000x1200')

tabControl = ttk.Notebook(Fenetre)


def CreateTab():
    TabName = ttk.Frame(tabControl)
    tabControl.add(TabName, text="1")

#<editor-fold desc="Creation menu">
Menubar = Menu(Fenetre)
Menu1 = Menu(Menubar, tearoff=0)
Menu1.add_command(label="Créer", command=CreateTab)
Menu1.add_command(label="Editer")
Menu1.add_separator()
Menu1.add_command(label="Quitter", command=Fenetre.quit)
Menubar.add_cascade(label="Fichier", menu=Menu1)

Menu2 = Menu(Menubar, tearoff=0)

Menu2.add_command(label="Couper")
Menu2.add_command(label="Copier")
Menu2.add_command(label="Coller")
Menubar.add_cascade(label="Editer", menu=Menu2)

Menu3 = Menu(Menubar, tearoff=0)
Menu3.add_command(label="A propos", command=alert)

Menubar.add_cascade(label="Fenêtre", menu=Menu3)

Menu4 = Menu(Menubar, tearoff=0)

Menu4.add_command(label="Bellman")
Menu4.add_command(label="Ford")
Menu4.add_command(label="Dijkstra")
Menu4.add_separator()
Menu4.add_command(label="Matrice")

Menubar.add_cascade(label="Algorithmes", menu=Menu4)

Menu5 = Menu(Menubar, tearoff=0)

Menu5.add_command(label="A propos")
Menubar.add_cascade(label="Aide", menu=Menu5)

Fenetre.config(menu=Menubar)
# </editor-fold>)


fWidth = Fenetre.winfo_screenwidth()
MenuBouton = Canvas(Fenetre, width=fWidth, height=25, background='white')
# MenuBouton.pack(side = TOP)
tabControl.grid(row=1,column=0,columnspan=4,padx=5)
Fenetre.minsize(700, 300)
tabControl.mainloop()




