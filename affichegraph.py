# coding: utf-8
 
from tkinter import * 
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def alert():
    showinfo("alerte", "Ca marche !")



Fenetre = Tk()
Fenetre.title("Infograph")
Fenetre['bg'] = 'grey'

Menubar = Menu(Fenetre)

Menu1 = Menu(Menubar, tearoff=0)
Menu1.add_command(label="Créer", command=alert)
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
fHeight= Fenetre.winfo_screenheight()
MenuBouton = Canvas(Fenetre, width=str(fWidth), height=25, background='white')
MenuBouton.pack(side = TOP)

#Canvas = Canvas(Fenetre, width=fWidth, height=fHeight, background="Grey")
#Canvas.pack(side = TOP)

graph = nx.DiGraph()
graph.add_nodes_from('ABCDEFGH')
graph.add_edges_from([
    ('A', 'B', {'capacity': 4, 'flow': 0}),
    ('A', 'C', {'capacity': 5, 'flow': 0}),
    ('A', 'D', {'capacity': 7, 'flow': 0}),
    ('B', 'E', {'capacity': 7, 'flow': 0}),
    ('C', 'E', {'capacity': 6, 'flow': 0}),
    ('C', 'F', {'capacity': 4, 'flow': 0}),
    ('C', 'G', {'capacity': 1, 'flow': 0}),
    ('D', 'F', {'capacity': 8, 'flow': 0}),
    ('D', 'G', {'capacity': 1, 'flow': 0}),
    ('E', 'H', {'capacity': 7, 'flow': 0}),
    ('F', 'H', {'capacity': 6, 'flow': 0}),
    ('G', 'H', {'capacity': 4, 'flow': 0}),

])
pos=nx.circular_layout(graph)
f = plt.figure(figsize=(5,4))
a = f.add_subplot(111)
plt.axis('off')
a.cla()
canvas = FigureCanvasTkAgg(f, master=Fenetre)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
nx.draw(graph,pos)
#plt.show()





Fenetre.minsize(750,350)

Fenetre.mainloop()