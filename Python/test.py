from tkinter import *
from tkinter import ttk
import math
import sys

myApp = Tk()
myApp.title(" Program ")
myApp.geometry("1000x1200")

tasktabs=ttk.Notebook(myApp)


def AddNewWork():


    TabName=ttk.Frame(tasktabs)
    tasktabs.add(TabName,text="ie")


AddWorkButton=Button(myApp,text=' Add ', command=AddNewWork)
AddWorkButton.grid(row=0,column=4, sticky="W", padx=5, pady=5)


tasktabs.grid(row=1,column=0,columnspan=4,padx=5)

myApp.mainloop()