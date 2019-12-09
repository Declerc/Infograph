import random as random
from pprint import pprint
#import pygame
#from pygame.locals import *
from tkinter import * 
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from tkinter import messagebox

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
        self.premierNode = None
        self.derniereNode = None
        self.ligne = None
        self.x = self.y = 0
        self.tabPrim = []
        self.debut = 1


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
        Menu2.add_command(label="CouperWeight",command=self.CreateTraitWeight)
        Menu2.add_command(label="Copier")
        Menu2.add_command(label="Coller")
        Menubar.add_cascade(label="Editer", menu=Menu2)

        Menu3 = Menu(Menubar, tearoff=0)
        Menu3.add_command(label="A propos")

        Menubar.add_cascade(label="Fenêtre", menu=Menu3)

        Menu4 = Menu(Menubar, tearoff=0)

        Menu4.add_command(label="Shortest Path", command=self.ActionShortest_Path)
        Menu4.add_command(label="Dijkstra", command=self.ActionDijkstra)
        Menu4.add_command(label="Bellman", command=self.ActionBellman_Ford)
        Menu4.add_command(label="Prim", command=self.ActionPrim)
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
        self.canvas.grid(row=0,column=0, sticky=N+S+E+W)

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
        #self.canvas.bind("<ButtonPress-1>", self.on_button_releaseTrait)
    def CreateTraitWeight(self):
        self.canvas.bind("<ButtonPress-1>", self.on_button_pressTraitWeight)
        #self.canvas.bind("<ButtonPress-1>", self.on_button_releaseTrait)
    def on_button_pressOval(self, event):
        # save mouse drag start position
        global y
        global graph
        global tabCoordNodes
        h=0
        if y==1:
            self.canvas.create_oval(event.x-20, event.y-20, event.x+20,event.y+20, fill="blue", outline="#DDD", width=4)
            tabCoordNodes[0].append(event.x)
            tabCoordNodes[1].append(event.y)
            graph.add_node(y)  
            self.canvas.create_text(event.x, event.y, text=y-1, fill="lightgreen")
            y= y+1
        else:
            for i in range(len(tabCoordNodes[0])):
                if tabCoordNodes[0][i]+20 > event.x and tabCoordNodes[0][i]-20 < event.x and tabCoordNodes[1][i]+20 > event.y and tabCoordNodes[1][i]-20 < event.y:
                    h=1
            if h==0:
                    self.canvas.create_oval(event.x-20, event.y-20, event.x+20,event.y+20, fill="blue", outline="#DDD", width=4)
                    tabCoordNodes[0].append(event.x)
                    tabCoordNodes[1].append(event.y)
                    graph.add_node(y)
                    self.canvas.create_text(event.x, event.y, text=y-1, fill="lightgreen")
                    y= y+1
        
    def on_button_release(self, event):
        pass
    
    
    def oui(self,premierNode,derniereNode,tabPrim):
        try:
            tabPrim[premierNode-1][derniereNode-1]=int(self.debut)
        except:
            try:
                tabPrim[premierNode-1].append(0)
                self.oui(premierNode,derniereNode,tabPrim)
            except:
                tabPrim.append([])
                self.oui(premierNode,derniereNode,tabPrim)
        try:
            tabPrim[derniereNode-1][premierNode-1]=int(self.debut)
            return tabPrim
        except:
            try:
                tabPrim[derniereNode-1].append(0)
                self.oui(premierNode,derniereNode,tabPrim)
            except:
                tabPrim.append([])
                self.oui(premierNode,derniereNode,tabPrim)
        #print(tabPrim)
        
        
    def on_button_releaseTrait(self, event):
        #tabCoordEdges[0].append(event.x)
        #tabCoordEdges[1].append(event.y)
        for i in range(len(tabCoordNodes[0])):
            if tabCoordNodes[0][i]+20 > event.x and tabCoordNodes[0][i]-20 < event.x and tabCoordNodes[1][i]+20 > event.y and tabCoordNodes[1][i]-20 < event.y:
                if self.start_x +40 > event.x and self.start_x -40 < event.x and self.start_y +40 > event.y and self.start_y -40 < event.y : 
                    pass
                else:
                    self.ligne = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y)
                    self.canvas.bind("<ButtonPress-1>", self.on_button_pressTrait)
                    self.derniereNode = i+1
                    #print(self.premierNode)
                    #print(self.derniereNode)
                    graph.add_edge(self.premierNode,self.derniereNode)
                    tabNodesEdges[1].append(self.derniereNode)
                    
    def on_button_releaseTraitWeight(self, event):
        #tabCoordEdges[0].append(event.x)
        #tabCoordEdges[1].append(event.y)
        for i in range(len(tabCoordNodes[0])):
            if tabCoordNodes[0][i]+20 > event.x and tabCoordNodes[0][i]-20 < event.x and tabCoordNodes[1][i]+20 > event.y and tabCoordNodes[1][i]-20 < event.y:
                if self.start_x +40 > event.x and self.start_x -40 < event.x and self.start_y +40 > event.y and self.start_y -40 < event.y : 
                    pass
                else:
                    self.ligne = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y)
                    self.canvas.bind("<ButtonPress-1>", self.on_button_pressTraitWeight)
                    self.derniereNode = i+1
                    #print(self.premierNode)
                    #print(self.derniereNode)
                    
                    def RecupData():
                        self.debut = entr1.get()
                        graph.add_edge(self.premierNode,self.derniereNode, weight=int(self.debut))
                        fen1.destroy()
                    
                    fen1 = Tk()
                    fen1.geometry("350x160")
                    fen1.title('Algorithme de dijkstra')
                    
                    consigne = Label(fen1, text='Renseigné les 2 champs suivants avec des entiers :')
                    txt1 = Label(fen1, text='Noeud de départ :')
                    entr1 = Entry(fen1)
                    button = Button(fen1, text='submit', command=RecupData)
                    
                    consigne.grid(row=0, columnspan=2,pady=15, padx=20)
                    txt1.grid(row=1)
                    entr1.grid(row=1, column=1)
                    
                    button.grid(row=3,columnspan=3, pady=15)
                    self.oui(self.premierNode,self.derniereNode,self.tabPrim)
                    graph.add_edge(self.premierNode,self.derniereNode, weight=self.debut)
                    print(self.debut)
                    tabNodesEdges[1].append(self.derniereNode)
    
    def on_button_pressTrait(self, event):
        for i in range(len(tabCoordNodes[0])):
            if tabCoordNodes[0][i]+20 > event.x and tabCoordNodes[0][i]-20 < event.x and tabCoordNodes[1][i]+20 > event.y and tabCoordNodes[1][i]-20 < event.y:
            # save mouse drag start position
                    
                self.start_x = event.x
                self.start_y = event.y
                self.premierNode = i+1
                tabNodesEdges[0].append(self.premierNode)
                
                
                #tabCoordEdges[0].append(event.x)
                #tabCoordEdges[1].append(event.y)
                self.canvas.bind("<ButtonPress-1>", self.on_button_releaseTrait)
                
    def on_button_pressTraitWeight(self, event):
        for i in range(len(tabCoordNodes[0])):
            if tabCoordNodes[0][i]+20 > event.x and tabCoordNodes[0][i]-20 < event.x and tabCoordNodes[1][i]+20 > event.y and tabCoordNodes[1][i]-20 < event.y:
            # save mouse drag start position
                    
                self.start_x = event.x
                self.start_y = event.y
                self.premierNode = i+1
                tabNodesEdges[0].append(self.premierNode)

                
                
                #tabCoordEdges[0].append(event.x)
                #tabCoordEdges[1].append(event.y)
                self.canvas.bind("<ButtonPress-1>", self.on_button_releaseTraitWeight)
                
    def ActionShortest_Path(self):
        global graph
        try:
            p=nx.shortest_path(graph,1,4)
            messagebox.showinfo("Chemin le plus court",p)
        except:
            messagebox.showinfo("Chemin le plus court", "Pas de chemin entre ... et ...")
            
    def ActionDijkstra(self):
        global graph
        try:
            p=nx.dijkstra_path(graph,1,4)
            messagebox.showinfo("dijkstra",p)
        except:
            messagebox.showinfo("dijkstra", "Pas de Path entre ... et ...")
            
    def ActionBellman_Ford(self):
        global graph
        try:
            pred, dist=nx.bellman_ford_predecessor_and_distance(graph,1)
            messagebox.showinfo("Bellman_Ford",'Predécédents : '+str(pred)+' Distances : '+str(dist))    
        except:
            messagebox.showinfo("Bellman_Ford", "Mauvaise source ou cycle poids négatif")
    def ActionPrim(self):
        ok = graph.number_of_nodes()
        """for i in range(0,ok):"""
        for j in range(0,ok):
            if len(self.tabPrim[j])==graph.number_of_nodes():
                pass
            else:
                self.tabPrim[j].append(0)
                """try:
                    self.tabPrim[i][j]=self.tabPrim[i][j]
                    print("oui")
                except:
                    self.tabPrim[i][j].append(0)
                    print("non")"""
                    
        T = []
        n = len(self.tabPrim)
        #self.tabPrim[n-1].append(0)
        print(self.tabPrim)
        plusProche = []
        distanceMin = []
     
        for i in range(0,n):
          plusProche.append(0)
          distanceMin.append(0)
     
        for i in range(1,n):
          plusProche[i] = 0
          distanceMin[i] = self.tabPrim[i][0]
     
        for i in range(0,n-1):
          min = None
          for j in range(1,n):
            if ((min and distanceMin[j] and 0 <= distanceMin[j] < min) or (not min and distanceMin[j] is not None and 0 <= distanceMin[j])):
              min = distanceMin[j]
              k = j
     
          T.append((k, plusProche[k]))
          print(T)
     
          distanceMin[k] = -1
          distanceMin[plusProche[k]] = -1
     
          for j in range(1,n):
            if ((distanceMin[j] and self.tabPrim[k][j] and self.tabPrim[k][j] < distanceMin[j]) or not distanceMin[j] ):
              distanceMin[j] = self.tabPrim[k][j]
              distanceMin[k] = self.tabPrim[j][k]
     
              plusProche[j] = k
              plusProche[k] = j
     
        return T 
        # try:
              
        #except:
         #   messagebox.showinfo("Prim", "Mauvaise source ou cycle poids négatif")
          


        
        
        
#tabCoordNodes x=tabCoordNodes[0]  / y=tabCoordNodes[1]

tabCoordNodes= [[],[]]
#tabCoordEdges= [[],[]]
tabNodesEdges = [[],[]]
y=1
graph = nx.Graph()
app = App(1000, 1200)
app.RunFenetre()
pprint(tabNodesEdges)
nx.draw(graph) 
P.show()


  