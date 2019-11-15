from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#---------------------------------------------------------------------
class MyTab(Frame):

    def __init__(self, root, name):
        Frame.__init__(self, root)

        self.root = root
        self.name = name

        self.entry = Entry(self)
        self.entry.pack(side=TOP)

        self.entry.bind('<FocusOut>', self.alert)
        self.entry.bind('<Key>', self.printing)

    #-------------------------------

    def alert(self, event):
        print ('FocusOut event is working for ' + self.name + '  value: ' + self.entry.get())
        #tkMessageBox.showinfo('alert', 'FocusOut event is working for ' + self.name + '  value: ' + self.entry.get())

    #-------------------------------

    def printing(self, event):
        print(event.keysym + ' for ' + self.name)

#---------------------------------------------------------------------

class Application():

    def __init__(self):

        self.tabs = {'ky':1}

        self.root = Tk()
        self.root.minsize(300, 300)
        self.root.geometry("1000x700")

        self.notebook = ttk.Notebook(self.root, width=1000, height=650)

#       self.all_tabs = []

        self.addTab('tab1')

        self.button = Button(self.root, text='generate', command=self.start_generating).pack(side=BOTTOM)

        self.notebook.pack(side=TOP)

    #-------------------------------

    def addTab(self, name):
        tab = MyTab(self.notebook, name)
        self.notebook.add(tab, text=name)
#       self.all_tabs.append(tab)

    #-------------------------------

    def start_generating(self):
        if self.tabs['ky'] < 4:
            self.tabs['ky'] += 1
            self.addTab('tab'+ str(self.tabs['ky']))

    #-------------------------------

    def run(self):
        self.root.mainloop()

#----------------------------------------------------------------------

Application().run()