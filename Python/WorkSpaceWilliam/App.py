from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class MyTab(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)

        self.root = root
        #self.name = name

        #self.entry = Entry(self)
        #self.entry.pack(side=TOP)

        #self.entry.bind('<FocusOut>', self.alert)
        #self.entry.bind('<Key>', self.printing)

class App:
    @property   # Getter Setter
    def Width(self):
        return self._width
    @Width.setter
    def Width(self,value):
        self._width = value
    @property
    def Height(self):
        return self._height
    @Height.setter
    def Height(self, value):
        self._height = value

    def __init__(self, width, height): # Constructeur
        self.Width = width
        self.Height = height


    def CreationMenu(self, Fenetre):
        Menubar = Menu(Fenetre)
        Menu1 = Menu(Menubar, tearoff=0)
        Menu1.add_command(label="Créer", command=self.CreateTab)
        Menu1.add_command(label="Editer")
        Menu1.add_command(label="Supprimer", command=self.DeleteTab)
        Menu1.add_separator()
        Menu1.add_command(label="Quitter", command=Fenetre.quit)
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

        Fenetre.config(menu=Menubar)

    #global canvasTab  # Déclaration tableau qui contient les canvas des tabs
    canvasTab = []

    def CreateTab(self):                # Fonction pour créer fenetre
        tab = MyTab(self)
        self.tabControl.add(tab, text=tabControl.index(tab))
        tabControl.select(tab)


        TabName = ttk.Frame(tabControl)
        print(TabName)
        tabControl.add(TabName)
        tabControl.tab(TabName, text=tabControl.index(TabName))  # Affiche numéro tab dans titre

        tabControl.select(TabName)
        self.canvas = Canvas(TabName, width=TabName.winfo_width(), height=TabName.winfo_height(), cursor="cross" ,bg="red")  #Creer zone dessin pour le graph
        self.canvas.grid(row=0, column=0, sticky=N + S + E + W)
        self.Con_func = tabControl.bind('<Configure>', self.d, "+") #Bind tabName à la fonction qui change la taille des canvas dynamiquement
        self.canvasTab.append(self.canvas)

    def start_generating(self):
        self.tabs['ky'] += 1
        self.addTab('tab')

    def DeleteTab(self): #  FIXME: FINIR POUR ENLEVER BUGS
        tabControl.forget(tabControl.select())
        print("Tab select ", tabControl.select())
        print("Tab frame ", ttk.Frame(tabControl))
        print("Tabs ", tabControl.tabs())

    def handle_tab_changed(self, event):  # TODO: FAIRE EN SORTE QUE TOUTE LES TABS SOIENT RESPONSIVE
        selection = event.widget.select()
        #tabControl.unbind('<Configure>')
        print(tabControl)
        tab = event.widget.tab(selection, "text")

        #self.canvas.config(width=self.Width, height=self.Height)

    def MenuButtonGraph(self, Fenetre):             #Boutton dessin point a la main
        canvasButton = Canvas(Fenetre, width=Fenetre.winfo_width(), height=25)
        canvasButton.pack(fill=X)
        self.buttonPoint = Button(canvasButton, command=self.CreatePoint, width=3).place(x=5,y=2)


       # if not tabControl.get() :

    def CreatePoint(self):          #lie le canvas de la tab et l evenement du click souris
        try:
            self.canvasTab[tabControl.index(tabControl.select())].bind("<ButtonPress-1>", self.on_button_press)
            self.canvasTab[tabControl.index(tabControl.select())].bind("<ButtonRelease-1>", self.on_button_release)
        except TclError:
            messagebox.showerror("Erreur Tab", "Vous devez créer une table pour dessiner un graphe : \nFichier > Créer")




    def on_button_press(self, event):  #récupère les positions de la souris au click et dessine un point
        self.canvasTab[tabControl.index(tabControl.select())].create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20,
                                                                     fill="blue", outline="#DDD", width=4)

    def on_button_release(self, event):
        pass

    def d(self, event):     #Permet que la taille des canvas des dessins soit responsive
        print(event)
        self.canvas.config(width=event.width, height=event.height)

    def RunFenetre(self):
        Fenetre = Tk()
        Fenetre.title("Infograph")
        Fenetre['bg'] = 'grey'
        # Mettre en global pour etre reconnu dans createTab

        Fenetre.geometry("{}x{}".format(self._width, self._height))
        Fenetre.minsize(800, 600)

        Fenetre.update_idletasks()  # Permet que winfo_height et width ne soit pas égaux à 1.
        canvasFenetre = Canvas(Fenetre, width=Fenetre.winfo_width()*(3/4), height=Fenetre.winfo_height()).place(x= 0, y = 0)  # Canvas de toute la fenetre
        canvasConsole = Canvas(Fenetre, bg = "black", width = Fenetre.winfo_height()*(1/4), height = Fenetre.winfo_height()) # Canvas console

        self.CreationMenu(Fenetre)
        self.MenuButtonGraph(Fenetre)
        # print(Fenetre.winfo_width(), Fenetre.winfo_height())
        canvasConsole.pack(side=RIGHT, fill=Y)
        global tabControl  # Global pour être reconnu dans autres fonctions
        tabControl = ttk.Notebook(canvasFenetre)  # Tabs dépendent du canvas
        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        tabControl.bind("<<NotebookTabChanged>>", self.handle_tab_changed)
        Fenetre.mainloop()
