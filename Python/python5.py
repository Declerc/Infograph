import random as random
from tkinter import * 
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pylab as P

class App:
    @property
    def Width(self):
        return self._width
    @Width.setter
    def Width(self, value):
        self._width = value
    @property
    def Height(self):
        return self._height
    @Height.setter
    def Height(self, value):
        self._height = value

    def __init__(self, width, height):
        self.Width = width
        self.Height = height
        self.start_x = None
        self.start_y = None
        self.ligne = None
        self.x = self.y = 0


    def CreationMenu(self, Fenetre):
        Menubar = Menu(Fenetre)
        Menu1 = Menu(Menubar, tearoff=0)
        Menu1.add_command(label="Créer", command=self.CreateTab)
        Menu1.add_command(label="Editer", command=self.CreatePoint)
        Menu1.add_separator()
        Menu1.add_command(label="Quitter", command=Fenetre.quit)
        Menubar.add_cascade(label="Fichier", menu=Menu1)

        Menu2 = Menu(Menubar, tearoff=0)

        Menu2.add_command(label="Couper",command=self.CreateTrait)
        Menu2.add_command(label="Copier")
        Menu2.add_command(label="Coller")
        Menubar.add_cascade(label="Editer", menu=Menu2)

        Menu3 = Menu(Menubar, tearoff=0)
        Menu3.add_command(label="A propos")

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

    def CreateTab(self):                #Fonction pour créer fenetre
        TabName = ttk.Frame(tabControl)
        tabControl.add(TabName, text="1")
        ttk.Label(TabName, text="This is Tab {}".format(tabControl.index(tabControl.select()))).grid(column=0, row=0, padx=10, pady=10)
        self.canvas = Canvas(TabName,  cursor="cross")
        self.canvas.grid(row=0,column=0,sticky=N+S+E+W)

    def RunFenetre(self):
        Fenetre = Tk()
        Fenetre.title("Infograph")
        Fenetre['bg'] = 'grey'
        global tabControl       # Mettre en global pour etre reconnu dans createTab
        tabControl = ttk.Notebook(Fenetre)
        Fenetre.geometry("{}x{}".format(self._width, self._height))

        self.CreationMenu(Fenetre)
        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        Fenetre.mainloop()
        
    def CreatePoint(self):
        self.canvas.bind("<ButtonPress-1>", self.on_button_pressOval)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        
    def CreateTrait(self):
        self.canvas.bind("<ButtonPress-1>", self.on_button_pressTrait)
        self.canvas.bind("<B1-Motion>", self.on_move_pressTrait)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_releaseTrait)
    def on_button_pressOval(self, event):
        # save mouse drag start position
        global i
        global graph
        global tabCoordNodes
        self.canvas.create_oval(event.x-20, event.y-20, event.x+20,event.y+20, fill="blue", outline="#DDD", width=4)
        tabCoordNodes[0].append(event.x)
        tabCoordNodes[1].append(event.y)
        graph.add_node(i)  
        i= i+1
    def on_button_release(self, event):
        pass 
    
    def on_button_releaseTrait(self, event):
        tabCoordEdges[0].append(event.x)
        tabCoordEdges[1].append(event.y)
    
    def on_button_pressTrait(self, event):
        for i in range(30):
            if tabCoordNodes[0][i]+20 > event.x and tabCoordNodes[0][i]-20 < event.x and tabCoordNodes[1][i]+20 > event.y and tabCoordNodes[1][i]-20 < event.y:
            # save mouse drag start position
                self.start_x = event.x
                self.start_y = event.y
                tabCoordEdges[0].append(event.x)
                tabCoordEdges[1].append(event.y)
            # create ligne if not yet exist
            #if not self.rect:
            
                self.ligne = self.canvas.create_line(self.x, self.y, 1, 1)
   

    def on_move_pressTrait(self, event):
        curX, curY = (event.x, event.y)

        # expand ligne as you drag the mouse
        self.canvas.coords(self.ligne, self.start_x, self.start_y, curX, curY)
        
        
#tabCoordNodes x=tabCoordNodes[0]  / y=tabCoordNodes[1]

tabCoordNodes= [[],[]]
tabCoordEdges= [[],[]]
i=1
graph = nx.DiGraph()
app = App(1000, 1200)
app.RunFenetre()
nx.draw(graph) 
P.show()

  