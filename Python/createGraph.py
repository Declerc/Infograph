from tkinter import *
from tkinter import ttk

def CreateTab(tabControl, page, i):
    page.append(ttk.Frame(tabControl))
    tabControl.add(page[i], text='Tab1')
    i += 1
    return i
