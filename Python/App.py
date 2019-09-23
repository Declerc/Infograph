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



    def CreateTab(self):                # Fonction pour créer fenetre
        TabName = ttk.Frame(tabControl, width=200, height=200)
        tabControl.add(TabName)
        ttk.Label(TabName, text="This is Tab {}".format(tabControl.index(TabName))).grid(column=0, row=0, padx=10, pady=10)
        tabControl.tab(TabName, text= tabControl.index(TabName))  # Affiche numéro tab dans titre

        self.canvas = Canvas(TabName, width=TabName.winfo_width(), height=TabName.winfo_height(), cursor="cross")  #Creer zone dessin pour le graph
        self.canvas.grid(row=0, column=0, sticky=N + S + E + W)

    def MenuButtonGraph(self, Fenetre):             #Boutton dessin point a la main
        canvasButton = Canvas(Fenetre, width=Fenetre.winfo_width(), height=30)
        canvasButton.pack()
        self.buttonPoint = Button(canvasButton, command=self.CreatePoint)
        self.buttonPoint.pack(side=LEFT)

    def CreatePoint(self):          #lie le canvas de la tab et l evenement du click souris
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)


    def on_button_press(self, event):  #récupère les positions de la souris au click et dessine un point
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        # if not self.rect:
        self.canvas.create_arc(event.x, event.y, event.x, event.y, fill="blue", outline="#DDD", width=15)

    def on_button_release(self, event):
        pass

    def RunFenetre(self):
        Fenetre = Tk()
        Fenetre.title("Infograph")
        Fenetre['bg'] = 'grey'
        # Mettre en global pour etre reconnu dans createTab

        Fenetre.geometry("{}x{}".format(self._width, self._height))



        Fenetre.update_idletasks()  # Permet que winfo_height et width ne soit pas égaux à 1.
        canvasFenetre = Canvas(Fenetre, width=Fenetre.winfo_width(), height=Fenetre.winfo_height()).place(x= 0, y = 0)  # Canvas de toute la fenetre
        canvasConsole = Canvas(Fenetre, bg = "black", width = 100, height = Fenetre.winfo_height()) # Canvas console

        self.CreationMenu(Fenetre)
        self.MenuButtonGraph(Fenetre)
        # print(Fenetre.winfo_width(), Fenetre.winfo_height())
        canvasConsole.pack(side=RIGHT)
        global tabControl  # Global pour être reconnu dans autres fonctions
        tabControl = ttk.Notebook(canvasFenetre)  # Tabs dépendent du canvas
        tabControl.pack(expand=1, fill="both")  # Pack to make visible

        Fenetre.mainloop()
