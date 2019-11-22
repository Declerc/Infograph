from tkinter import *
from tkinter import ttk

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

    def CreationMenu(self, Fenetre):
        Menubar = Menu(Fenetre)
        Menu1 = Menu(Menubar, tearoff=0)
        Menu1.add_command(label="Créer", command=self.CreateTab)
        Menu1.add_command(label="Editer", command=self.CreatePoint)
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
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        #if not self.rect:
        self.canvas.create_arc(event.x, event.y, event.x,event.y, fill="blue", outline="#DDD", width=4)


    def on_button_release(self, event):
        pass  
        
        



app = App(1000, 1200)
app.RunFenetre()