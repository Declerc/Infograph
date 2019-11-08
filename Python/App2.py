from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class MyTab(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)

        self.root = root

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

        self.notebook = ttk.Notebook(self.canvas_fenetre)
        self.notebook.pack(expand=1, fill="both")
        self.add_tab()



    def add_tab(self):
        self.tab = MyTab(self.notebook)
        self.notebook.add(self.tab)  # Add tab to the notebook
        self.notebook.tab(self.tab, text=self.notebook.index(self.tab))  # Add title to the tab
        self.notebook.select(self.tab)

    def delete_tab(self):
        self.notebook.forget(self.notebook.select())

    def start_generating(self):
        self.tabs['ky'] += 1
        self.add_tab()

    def menu_button_graph(self):
        canvas_button = Canvas(self.root, width=self.root.winfo_width(), height=25)
        canvas_button.pack(fill=X)
        self.buttonPoint = Button(canvas_button, command=self.create_point, width=3).place(x=5, y=2)

    def create_point(self):          #TODO: A FAIRE CAR NE MARCHE PAS, PAS D’EQUIVALENCE AVEC PRECEDENTE VARIABLE
        try:
            self.tab[self.notebook.index(self.notebook.select())].bind("<ButtonPress-1>", self.on_button_press)
            self.tab[self.notebook.index(self.notebook.select())].bind("<ButtonRelease-1>", self.on_button_release)
        except TclError:
            messagebox.showerror("Erreur Tab", "Vous devez créer une table pour dessiner un graphe : \nFichier > Créer")

    def on_button_press(self, event):  #récupère les positions de la souris au click et dessine un point
        self.tab[self.notebook.index(self.notebook.select())].create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20,
                                                                     fill="blue", outline="#DDD", width=4)

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
