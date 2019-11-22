from tkinter import *
from tkinter import ttk

def CreateTab(tabControl):
    TabName = ttk.Frame(tabControl)
    tabControl.add(TabName, text="1")

    ttk.Label(TabName, text="This is Tab 1").grid(column=0, row=0, padx=10, pady=10)
