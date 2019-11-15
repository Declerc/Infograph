from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import networkx as nx
from pprint import pprint



class MyTab(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        #wscale = float(event.width)/self.width
        #hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        #self.scale("all",0,0,wscale,hscale)


class Graph():
    def __init__(self, canvasTableau, parentNotebook):
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

    def create_point(self):
        try:
            self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>", self.on_button_pressOval)
            self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonRelease-1>", self.on_button_release)
        except TclError:
            messagebox.showerror("Erreur Tab", "Vous devez créer une table pour dessiner un graphe : \nFichier > Créer")

    def createTrait(self):
        self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>", self.on_button_pressTrait)

    def on_button_pressOval(self, event):
        # save mouse drag start position
        h = 0
        if self.y == 1:
            self.canvasTab[self.notebook.index(self.notebook.select())].create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20,
                                                                                    fill="blue", outline="#DDD", width=4)
            self.tabCoordNodes[0].append(event.x)
            self.tabCoordNodes[1].append(event.y)
            self.graph.add_node(self.y)
            self.y = self.y + 1
        else:
            for i in range(len(self.tabCoordNodes[0])):
                if self.tabCoordNodes[0][i] + 20 > event.x and self.tabCoordNodes[0][i] - 20 < event.x and self.tabCoordNodes[1][
                    i] + 20 > event.y and self.tabCoordNodes[1][i] - 20 < event.y:
                    h = 1
            if h == 0:
                self.canvasTab[self.notebook.index(self.notebook.select())].create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20,
                                                                                        fill="blue", outline="#DDD", width=4)
                self.tabCoordNodes[0].append(event.x)
                self.tabCoordNodes[1].append(event.y)
                self.graph.add_node(self.y)
                self.y = self.y + 1

    def on_button_release(self, event):
        pass

    def on_button_releaseTrait(self, event):
        # tabCoordEdges[0].append(event.x)
        # tabCoordEdges[1].append(event.y)
        for i in range(len(self.tabCoordNodes[0])):
            if self.tabCoordNodes[0][i] + 20 > event.x and self.tabCoordNodes[0][i] - 20 < event.x and self.tabCoordNodes[1][i] + 20 > event.y and self.tabCoordNodes[1][i] - 20 < event.y:
                if self.start_x + 40 > event.x and self.start_x - 40 < event.x and self.start_y + 40 > event.y and self.start_y - 40 < event.y:
                    pass
                else:
                    self.ligne = self.canvasTab[self.notebook.index(self.notebook.select())].create_line(self.start_x, self.start_y, event.x, event.y)
                    self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>", self.on_button_pressTrait)
                    self.derniereNode = i + 1
                    self.graph.add_edge(self.premierNode, self.derniereNode)
                    self.tabNodesEdges[self.z].append(self.derniereNode)
                    print(self.z)
                    self.z = self.z - 1

    def on_button_pressTrait(self, event):
        for i in range(len(self.tabCoordNodes[0])):
            if self.tabCoordNodes[0][i] + 20 > event.x and self.tabCoordNodes[0][i] - 20 < event.x and self.tabCoordNodes[1][i] + 20 > event.y and self.tabCoordNodes[1][i] - 20 < event.y:
                # save mouse drag start position

                self.start_x = event.x
                self.start_y = event.y
                self.premierNode = i + 1
                self.tabNodesEdges[self.z].append(self.premierNode)
                print(self.premierNode)
                print(self.z)
                self.z = self.z + 1

                # tabCoordEdges[0].append(event.x)
                # tabCoordEdges[1].append(event.y))
                self.canvasTab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>", self.on_button_releaseTrait)

    def actionDijkstra(self):
        messagebox.showinfo("Title", nx.dijkstra_path(self.graph, 1, 4))


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
        self.canvas_fenetre = Canvas(self.root, width=self.root.winfo_width()*(3/4), height=self.root.winfo_height()).place(x= 0, y = 0)  # Canvas de toute la fenetre
        self.canvas_console = Canvas(self.root, bg="black", width = self.root.winfo_height()*(1/4), height=self.root.winfo_height())  # Canvas console
        self.canvas_console.pack(side=RIGHT, fill=Y)

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

    def delete_tab(self):
        self.notebook.forget(self.notebook.select())

    def start_generating(self):
        self.tabs['ky'] += 1
        self.add_tab()

    def menu_button_graph(self):
        canvas_button = Canvas(self.root, width=self.root.winfo_width(), height=25)
        canvas_button.pack(fill=X)
        canvas_button2 = Canvas(self.root, width=self.root.winfo_width(), height=25)
        canvas_button2.pack(fill=X)
        self.buttonPoint = Button(canvas_button, command=self.graph.create_point, width=3).place(x=5, y=2)
        self.buttonTrait = Button(canvas_button2, command=self.graph.createTrait, width=5).place(x=15, y=2)


    #def on_button_press(self, event):  #récupère les positions de la souris au click et dessine un point
        #self.canvasTab[self.notebook.index(self.notebook.select())].create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20,
                                                                     #fill="blue", outline="#DDD", width=4)

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

        Menu4.add_command(label="Bellman")
        Menu4.add_command(label="Ford")
        Menu4.add_command(label="Dijkstra")
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
