from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import networkx as nx
from pprint import pprint


class MyTab(Frame):  # Classe qui gère les Tabs

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):  # Classe des canvas des tabs
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        # wscale = float(event.width)/self.width
        # hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        # self.scale("all",0,0,wscale,hscale)


class Graph():  # Classe des graphes
    def __init__(self, canvasTableau,
                 parentNotebook):  # Passe en paramètre le canvas de la Tab et le notebook qui gère tout les canvas
        self.start_x = None
        self.start_y = None
        self.premierNode = None
        self.derniereNode = None
        self.ligne = None
        self.graph = nx.Graph()
        self.tabCoordNodes = [[], []]
        self.tabNodesEdges = [[], []]
        self.x = 0
        self.z = 0
        self.y = 1
        self.canvasTab = canvasTableau
        self.notebook = parentNotebook
        self.debut = 1
        self.tabPrim = []

    def create_point(self):
        # print(self.canvasTab[self.notebook.index(self.notebook.select())])
        try:
            self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>",
                                                                             self.on_button_pressOval)
            self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonRelease-1>",
                                                                             self.on_button_release)
        except TclError:
            messagebox.showerror("Erreur Tab", "Vous devez créer une table pour dessiner un graphe : \nFichier > Créer")

    def createTrait(self):
        self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>", self.on_button_pressTrait)

    def createTraitWeight(self):
        self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>",
                                                                         self.on_button_pressTraitWeight)

    def on_button_pressOval(self, event):
        # save mouse drag start position
        h = 0
        if self.y == 1:
            self.canvasTab[self.notebook.index(self.notebook.select())].create_oval(event.x - 20, event.y - 20,
                                                                                    event.x + 20, event.y + 20,
                                                                                    fill="blue", outline="#DDD",
                                                                                    width=4)
            self.tabCoordNodes[0].append(event.x)
            self.tabCoordNodes[1].append(event.y)
            self.graph.add_node(self.y - 1)
            self.canvasTab[self.notebook.index(self.notebook.select())].create_text(event.x, event.y, text=self.y - 1,
                                                                                    fill="lightgreen")
            self.y = self.y + 1
        else:
            for i in range(len(self.tabCoordNodes[0])):
                if self.tabCoordNodes[0][i] + 20 > event.x and self.tabCoordNodes[0][i] - 20 < event.x and \
                        self.tabCoordNodes[1][i] + 20 > event.y and self.tabCoordNodes[1][i] - 20 < event.y:
                    h = 1
            if h == 0:
                self.canvasTab[self.notebook.index(self.notebook.select())].create_oval(event.x - 20, event.y - 20,
                                                                                        event.x + 20, event.y + 20,
                                                                                        fill="blue", outline="#DDD",
                                                                                        width=4)
                self.tabCoordNodes[0].append(event.x)
                self.tabCoordNodes[1].append(event.y)
                self.graph.add_node(self.y - 1)
                self.canvasTab[self.notebook.index(self.notebook.select())].create_text(event.x, event.y,
                                                                                        text=self.y - 1,
                                                                                        fill="lightgreen")
                self.y = self.y + 1

    def on_button_release(self, event):
        pass

    def on_button_releaseTrait(self, event):
        # tabCoordEdges[0].append(event.x)
        # tabCoordEdges[1].append(event.y)
        for i in range(len(self.tabCoordNodes[0])):
            if self.tabCoordNodes[0][i] + 20 > event.x and self.tabCoordNodes[0][i] - 20 < event.x and \
                    self.tabCoordNodes[1][i] + 20 > event.y and self.tabCoordNodes[1][i] - 20 < event.y:
                if self.start_x + 40 > event.x and self.start_x - 40 < event.x and self.start_y + 40 > event.y and self.start_y - 40 < event.y:
                    pass
                else:
                    self.ligne = self.canvasTab[self.notebook.index(self.notebook.select())].create_line(self.start_x,
                                                                                                         self.start_y,
                                                                                                         event.x,
                                                                                                         event.y)
                    self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>",
                                                                                     self.on_button_pressTrait)
                    self.derniereNode = i + 1
                    self.graph.add_edge(self.premierNode - 1, self.derniereNode - 1)
                    self.tabNodesEdges[1].append(self.derniereNode - 1)

    def on_button_pressTrait(self, event):
        for i in range(len(self.tabCoordNodes[0])):
            if self.tabCoordNodes[0][i] + 20 > event.x and self.tabCoordNodes[0][i] - 20 < event.x and \
                    self.tabCoordNodes[1][i] + 20 > event.y and self.tabCoordNodes[1][i] - 20 < event.y:
                # save mouse drag start position

                self.start_x = event.x
                self.start_y = event.y
                self.premierNode = i + 1
                self.tabNodesEdges[0].append(self.premierNode - 1)
                print(self.premierNode)

                # tabCoordEdges[0].append(event.x)
                # tabCoordEdges[1].append(event.y))
                self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>",
                                                                                 self.on_button_releaseTrait)

    def on_button_pressTraitWeight(self, event):
        for i in range(len(self.tabCoordNodes[0])):
            if self.tabCoordNodes[0][i] + 20 > event.x and self.tabCoordNodes[0][i] - 20 < event.x and \
                    self.tabCoordNodes[1][i] + 20 > event.y and self.tabCoordNodes[1][i] - 20 < event.y:
                # save mouse drag start position

                self.start_x = event.x
                self.start_y = event.y
                self.premierNode = i + 1
                self.tabNodesEdges[0].append(self.premierNode - 1)

                # tabCoordEdges[0].append(event.x)
                # tabCoordEdges[1].append(event.y)
                self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>",
                                                                                 self.on_button_releaseTraitWeight)

    def on_button_releaseTraitWeight(self, event):
        # tabCoordEdges[0].append(event.x)
        # tabCoordEdges[1].append(event.y)
        for i in range(len(self.tabCoordNodes[0])):
            if self.tabCoordNodes[0][i] + 20 > event.x and self.tabCoordNodes[0][i] - 20 < event.x and \
                    self.tabCoordNodes[1][i] + 20 > event.y and self.tabCoordNodes[1][i] - 20 < event.y:
                if self.start_x + 40 > event.x and self.start_x - 40 < event.x and self.start_y + 40 > event.y and self.start_y - 40 < event.y:
                    pass
                else:
                    self.ligne = self.canvasTab[self.notebook.index(self.notebook.select())].create_line(self.start_x,
                                                                                                         self.start_y,
                                                                                                         event.x,
                                                                                                         event.y)
                    self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>",
                                                                                     self.on_button_pressTraitWeight)
                    self.derniereNode = i + 1

                    def RecupData():
                        self.debut = entr1.get()
                        self.graph.add_edge(self.premierNode - 1, self.derniereNode - 1, weight=int(self.debut))
                        self.creationTabPrim(self.premierNode - 1, self.derniereNode - 1, self.tabPrim)
                        fen1.destroy()

                    fen1 = Tk()
                    fen1.geometry("350x160")
                    fen1.title('Poids de l\'arc')

                    consigne = Label(fen1, text='Renseignez le champ suivant avec un entier :')
                    txt1 = Label(fen1, text='Poid :')
                    entr1 = Entry(fen1)
                    button = Button(fen1, text='submit', command=RecupData)

                    consigne.grid(row=0, columnspan=2, pady=15, padx=20)
                    txt1.grid(row=1)
                    entr1.grid(row=1, column=1)

                    button.grid(row=3, columnspan=3, pady=15)
                    # self.creationTabPrim(self.premierNode-1,self.derniereNode-1,self.tabPrim)
                    # graph.add_edge(self.premierNode-1,self.derniereNode-1, weight=self.debut)
                    self.tabNodesEdges[1].append(self.derniereNode - 1)

    def creationTabPrim(self, premierNode, derniereNode, tabPrim):

        # print(premierNode)
        # print(derniereNode)
        print(self.debut)
        try:
            tabPrim[premierNode][derniereNode] = int(self.debut)
        except:
            try:
                tabPrim[premierNode].append(0)
                self.creationTabPrim(premierNode, derniereNode, tabPrim)
            except:
                tabPrim.append([])
                self.creationTabPrim(premierNode, derniereNode, tabPrim)
        try:
            tabPrim[derniereNode][premierNode] = int(self.debut)
            return tabPrim
        except:
            try:
                tabPrim[derniereNode].append(0)
                self.creationTabPrim(premierNode, derniereNode, tabPrim)
            except:
                tabPrim.append([])
                self.creationTabPrim(premierNode, derniereNode, tabPrim)
        # print(tabPrim)

    def ActionShortest_Path(self):
        try:
            p = nx.shortest_path(self.graph, 1, 4)
            messagebox.showinfo("Chemin le plus court", p)
        except:
            messagebox.showinfo("Chemin le plus court", "Pas de chemin entre ... et ...")

    def ActionDijkstra(self, debut, fin):
        try:

            p = nx.dijkstra_path(self.graph, int(debut), int(fin))
            messagebox.showinfo("dijkstra", p)
        except:
            messagebox.showinfo("dijkstra", "Pas de Path entre ... et ...")

    def FenetreDijkstra(self):
        def RecupData():
            debut = entr1.get()
            fin = entr2.get()
            fen1.destroy()
            self.ActionDijkstra(debut, fin)

        fen1 = Tk()
        fen1.geometry("350x160")
        fen1.title('Algorithme de dijkstra')

        consigne = Label(fen1, text='Renseignez les 2 champs suivants avec des entiers :')
        txt1 = Label(fen1, text='Noeud de départ :')
        txt2 = Label(fen1, text='Noeud  d\'arrivée  :')
        entr1 = Entry(fen1)
        entr2 = Entry(fen1)
        button = Button(fen1, text='submit', command=RecupData)

        consigne.grid(row=0, columnspan=2, pady=15, padx=20)
        txt1.grid(row=1)
        txt2.grid(row=2)
        entr1.grid(row=1, column=1)
        entr2.grid(row=2, column=1, pady=3)

        button.grid(row=3, columnspan=3, pady=15)

    def FenetreBellman(self):
        def RecupData():
            source = entr1.get()
            fen1.destroy()
            self.ActionBellman_Ford(source)

        fen1 = Tk()
        fen1.geometry("350x160")
        fen1.title('Algorithme de bellman')

        consigne = Label(fen1, text='Renseignez le champ suivant avec un entier :')
        txt1 = Label(fen1, text='Noeud de départ :')
        entr1 = Entry(fen1)
        button = Button(fen1, text='submit', command=RecupData)
        consigne.grid(row=0, columnspan=2, pady=15, padx=20)
        txt1.grid(row=1)
        entr1.grid(row=1, column=1)
        button.grid(row=3, columnspan=3, pady=15)

    def ActionBellman_Ford(self, source):
        try:
            pred, dist = nx.bellman_ford_predecessor_and_distance(self.graph, int(source))
            messagebox.showinfo("Bellman_Ford", 'Predécédents : ' + str(pred) + ' Distances : ' + str(dist))
        except:
            messagebox.showinfo("Bellman_Ford", "Mauvaise source ou cycle poids négatif")

    def ActionPrim(self):
        ok = self.graph.number_of_nodes()
        print(ok)
        print(self.tabPrim)
        for j in range(0, ok):
            while (len(self.tabPrim[j]) != self.graph.number_of_nodes()):
                self.tabPrim[j].append(0)
        T = []
        n = len(self.tabPrim)
        # self.tabPrim[n-1].append(0)
        print(self.tabPrim)
        plusProche = []
        distanceMin = []

        for i in range(0, n):
            plusProche.append(0)
            distanceMin.append(0)

        for i in range(1, n):
            plusProche[i] = 0
            distanceMin[i] = self.tabPrim[i][0]

        for i in range(0, n - 1):
            min = None
            for j in range(1, n):
                if ((min and distanceMin[j] and 0 <= distanceMin[j] < min) or (
                        not min and distanceMin[j] is not None and 0 <= distanceMin[j])):
                    min = distanceMin[j]
                    k = j

            T.append((k, plusProche[k]))
            # print(T)

            distanceMin[k] = -1
            distanceMin[plusProche[k]] = -1

            for j in range(1, n):
                if ((distanceMin[j] and self.tabPrim[k][j] and self.tabPrim[k][j] < distanceMin[j]) or not distanceMin[j]):
                    distanceMin[j] = self.tabPrim[k][j]
                    distanceMin[k] = self.tabPrim[j][k]

                    plusProche[j] = k
                    plusProche[k] = j

        try:
            message = "L\'arbre est \n"
            for i in range(0, len(T)):
                message += str(T[i][0]) + " relie a " + str(T[i][1]) + "\n"
            messagebox.showinfo("Prim", message)
        except:
            messagebox.showinfo("Prim", "erreur")
        return T


class App():
    @property  # Getter Setter
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

    def __init__(self, width, height):  # Constructor
        self.tabs = {'ky': 1}
        self.Width = width
        self.Height = height

        self.root = Tk()
        self.root.minsize(300, 300)
        self.root.geometry("{}x{}".format(self._width, self._height))

        self.root.update_idletasks()  # Permet que winfo_height et width ne soit pas égaux à 1.
        self.canvas_fenetre = Canvas(self.root, width=self.root.winfo_width(),
                                     height=self.root.winfo_height()).place(x=0, y=0)  # Canvas de toute la fenetre
        #self.canvas_console = Canvas(self.root, bg="black", width=self.root.winfo_height() * (1 / 4), height=self.root.winfo_height())  # Canvas console
        #self.canvas_console.pack(side=RIGHT, fill=Y)

        self.canvasTab = []  # Tableau qui contient les canvas des Tabs
        self.notebook = ttk.Notebook(self.canvas_fenetre)
        self.notebook.pack(expand=1, fill="both")
        self.add_tab()

    def add_tab(self):
        tab = MyTab(self.notebook)
        self.notebook.add(tab)  # Add tab to the notebook
        self.notebook.tab(tab, text=self.notebook.index(tab))  # Add title to the tab
        self.notebook.select(tab)
        canvas = ResizingCanvas(tab, width=tab.winfo_width(), height=tab.winfo_height(), highlightthickness=0)
        canvas.pack(fill=BOTH, expand=YES)
        self.canvasTab.append(canvas)
        self.graph = Graph(self.canvasTab, self.notebook)

        # print(self.notebook.tabs())
        # print(self.notebook.tab(tab))
        # print(self.notebook.winfo_children())

    def delete_tab(self):  # marche mais rend impossible la création de graphes sur les tabs créées après
        self.notebook.forget(self.notebook.select())
        # self.notebook.select().destroy()
        self.tabs['ky'] -= 1

    def start_generating(self):
        self.tabs['ky'] += 1
        self.add_tab()

    def menu_button_graph(self):  # Creation des boutons pour points et arêtes
        canvas_button = Canvas(self.root, width=self.root.winfo_width(), height=25)
        canvas_button.pack(fill=X)
        self.buttonPoint = Button(canvas_button, command=self.graph.create_point, text="sommet").place(x=5, y=2)
        self.buttonTrait = Button(canvas_button, command=self.graph.createTrait, text="arete poids 1").place(x=105, y=2)
        self.buttonTraitWeight = Button(canvas_button, command=self.graph.createTraitWeight, text="arete poids n").place(x=205, y=2)

    def on_button_release(self, event):
        pass

    def creation_menu(self, fenetre):
        Menubar = Menu(fenetre)
        Menu1 = Menu(Menubar, tearoff=0)
        Menu1.add_command(label="Créer", command=self.start_generating)
        Menu1.add_command(label="Editer")
        Menu1.add_command(label="Supprimer", command=self.delete_tab)
        Menu1.add_separator()
        Menu1.add_command(label="Quitter", command=fenetre.quit)
        Menubar.add_cascade(label="Fichier", menu=Menu1)

        Menu2 = Menu(Menubar, tearoff=0)

        Menu2.add_command(label="Couper")
        Menu2.add_command(label="Copier")
        Menu2.add_command(label="Coller")
        Menubar.add_cascade(label="Editer", menu=Menu2)

        Menu3 = Menu(Menubar, tearoff=0)
        Menu3.add_command(label="A propos")

        Menubar.add_cascade(label="Fenêtre", menu=Menu3)

        Menu4 = Menu(Menubar, tearoff=0)

        Menu4.add_command(label="Shortest path", command=self.graph.ActionShortest_Path)
        Menu4.add_command(label="Dijkstra", command=self.graph.FenetreDijkstra)
        Menu4.add_command(label="Bellman", command=self.graph.FenetreBellman)
        Menu4.add_command(label="Prim", command=self.graph.ActionPrim)
        Menu4.add_separator()
        Menu4.add_command(label="Matrice")

        Menubar.add_cascade(label="Algorithmes", menu=Menu4)

        Menu5 = Menu(Menubar, tearoff=0)

        Menu5.add_command(label="A propos")
        Menubar.add_cascade(label="Aide", menu=Menu5)

        fenetre.config(menu=Menubar)

    def run(self):
        self.creation_menu(self.root)
        self.menu_button_graph()
        self.root.mainloop()


app = App(1000, 500)
app.run()
