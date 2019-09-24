from tkinter import *
from tkinter import ttk



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

    global canvasTab  # Déclaration tableau qui contient les canvas des tabs
    canvasTab = []

    def CreateTab(self):                # Fonction pour créer fenetre

        TabName = ttk.Frame(tabControl)
        tabControl.add(TabName)
        ttk.Label(TabName, text="This is Tab {}".format(tabControl.index(TabName))).grid(column=0, row=0, padx=10, pady=10)
        tabControl.tab(TabName, text= tabControl.index(TabName))  # Affiche numéro tab dans titre

        tabControl.select(TabName)
        self.canvas = Canvas(TabName, width=TabName.winfo_width(), height=TabName.winfo_height(), cursor="cross" ,bg="red")  #Creer zone dessin pour le graph
        self.canvas.grid(row=0, column=0, sticky=N + S + E + W)

        print(TabName.winfo_width())
        canvasTab.append(self.canvas)
        # print(canvasTab)
    def MenuButtonGraph(self, Fenetre):             #Boutton dessin point a la main
        canvasButton = Canvas(Fenetre, width=Fenetre.winfo_width(), height=25)
        canvasButton.pack(fill=X)
        self.buttonPoint = Button(canvasButton, command=self.CreatePoint, width=3).place(x=5,y=2)
        self.buttonPoint

    def CreatePoint(self):          #lie le canvas de la tab et l evenement du click souris
        canvasTab[tabControl.index(tabControl.select())].bind("<ButtonPress-1>", self.on_button_press)
        canvasTab[tabControl.index(tabControl.select())].bind("<ButtonRelease-1>", self.on_button_release)


    def on_button_press(self, event):  #récupère les positions de la souris au click et dessine un point

        canvasTab[tabControl.index(tabControl.select())].create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20,
                                                                     fill="blue", outline="#DDD", width=4)


    def on_button_release(self, event):
        pass

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

        #def handle_configure(event):
         #   canvasConsole.config(width = Fenetre.winfo_width()*(1/4), height = Fenetre.winfo_height())

        #Fenetre.bind("<Configure>", handle_configure)

        self.CreationMenu(Fenetre)
        self.MenuButtonGraph(Fenetre)
        # print(Fenetre.winfo_width(), Fenetre.winfo_height())
        canvasConsole.pack(side=RIGHT, fill=Y)
        global tabControl  # Global pour être reconnu dans autres fonctions
        tabControl = ttk.Notebook(canvasFenetre)  # Tabs dépendent du canvas
        tabControl.pack(expand=1, fill="both")  # Pack to make visible

        Fenetre.mainloop()
